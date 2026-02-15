import cv2
import os
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pickle

DATASET = "dataset/train"
X, y = [], []

for label in os.listdir(DATASET):
    path = os.path.join(DATASET, label)
    for img_name in os.listdir(path):
        img_path = os.path.join(path, img_name)
        img = cv2.imread(img_path)
        img = cv2.resize(img, (64, 64))
        X.append(img.flatten())
        y.append(label)

X = np.array(X)
y = np.array(y)

le = LabelEncoder()
y = le.fit_transform(y)

model = SVC(kernel='linear')
model.fit(X, y)

os.makedirs("model", exist_ok=True)
pickle.dump((model, le), open("model/model.pkl", "wb"))

print("Model trained successfully")

