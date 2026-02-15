import cv2
import os
import numpy as np
import pickle
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

model, le = pickle.load(open("model/model.pkl", "rb"))

X_test, y_test = [], []
DATASET = "dataset/test"

for label in os.listdir(DATASET):
    path = os.path.join(DATASET, label)
    for img_name in os.listdir(path):
        img_path = os.path.join(path, img_name)
        img = cv2.imread(img_path)
        img = cv2.resize(img, (64, 64))
        X_test.append(img.flatten())
        y_test.append(label)

X_test = np.array(X_test)
y_test = le.transform(y_test)

pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))

cm = confusion_matrix(y_test, pred)
sns.heatmap(cm, annot=True, fmt="d",
            xticklabels=le.classes_,
            yticklabels=le.classes_)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
