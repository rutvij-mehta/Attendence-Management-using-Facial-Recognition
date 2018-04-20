import face_recognition
import os
import numpy as np

directory = "/home/rutvij/Desktop/data"

dataset = []
for filename in os.listdir(directory):
    if filename.endswith(".jpg"): 
        dataset.append(filename)
        
    else:
        continue

dataset.sort()
print dataset


encodings = []
for i in dataset:
    p = face_recognition.load_image_file(i)
    encod = face_recognition.face_encodings(p)[0]
    encodings.append(encod)



print len(dataset)
print len(encodings)

np.save('encod.npy',encodings)
np.save('dataset.npy',dataset)
