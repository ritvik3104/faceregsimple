Simple Comparator: 
1.Checks if both images are selected.
2.Loads both images using face_recognition.load_image_file.
3.Extracts face encodings from each image.(These encodings are 128-dimensional feature vectors.)
4. Calculates the Euclidean distance between the two vectors:
