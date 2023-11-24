import numpy as np
import pandas as pd
import cv2
from tensorflow.keras.models import load_model

# Загрузка данных
train_csv_path = 'video.ittensive.com/machine-learning/clouds/train.csv.gz'
train_images_path = 'video.ittensive.com/machine-learning/clouds/train_images_small.tar.gz'
test_images_path = 'video.ittensive.com/machine-learning/clouds/test_images_small.tar.gz'

# Загрузка моделей
unet_model = load_model('video.ittensive.com/machine-learning/clouds/unet.fish.h5')
fpn_model = load_model('video.ittensive.com/machine-learning/clouds/fpn.fish.h5')
pspnet_model = load_model('video.ittensive.com/machine-learning/clouds/pspnet.fish.h5')

# Функция для сегментации изображений
def predict_image(model, image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (384, 256))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)
    return prediction[0]

# Функция для создания ансамбля предсказаний
def ensemble_predictions(models, image_path):
    predictions = [predict_image(model, image_path) for model in models]
    ensemble_prediction = np.mean(predictions, axis=0)
    return ensemble_prediction

# Загрузка тестовых данных
test_df = pd.read_csv('video.ittensive.com/machine-learning/clouds/sample_submission.csv.gz')

# Прогнозирование и создание ансамбля предсказаний
ensemble_predictions_list = []

for idx, row in test_df.iterrows():
    image_id = row['ImageId']
    image_path = f'{test_images_path}/{image_id}.jpg'

    unet_pred = predict_image(unet_model, image_path)
    fpn_pred = predict_image(fpn_model, image_path)
    pspnet_pred = predict_image(pspnet_model, image_path)

    ensemble_pred = ensemble_predictions([unet_pred, fpn_pred, pspnet_pred], image_path)
    ensemble_predictions_list.append(ensemble_pred)

# Сохранение результатов в формате sample_submission.csv
output_df = pd.DataFrame({'ImageId': test_df['ImageId'].values})
for i in range(1, 17):
    output_df[f'EncodedPixels_{i}'] = ensemble_predictions_list[:, :, i - 1].reshape(-1)

output_df.to_csv('path/to/ensemble_predictions.csv', index=False)
