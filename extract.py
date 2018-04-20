import face_recognition
import numpy as np
from collections import Counter

#Code for calculating knn and returning result
def attendance(filename):
    #load data
    dataset = np.load('dataset.npy')
    encod = np.load('encod.npy')

    unknown_picture = face_recognition.load_image_file("static/img/{0}".format(filename))
    encodlist = face_recognition.face_encodings(unknown_picture)
    print encodlist[0]
    l = len(encodlist)
    
    #final list of roll numbers
    flist = [] 

    for i in range(l):
        unknown_face_encoding = encodlist[i]
        #face_recognition.api.compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.6)

        results = face_recognition.compare_faces(encod, unknown_face_encoding)
        #print results

        indices = [i for i, x in enumerate(results) if x == 1]
        #print indices

        data = []

        for i in indices:
            data.append(dataset[i].split('-')[0])


        cnt = Counter(data)
        if len(cnt.most_common(1))>=1:
            print(cnt.most_common(1)[0][0])
            flist.append(cnt.most_common(1)[0][0])

        flist = set(flist)
        flist = list(flist)

    return flist

