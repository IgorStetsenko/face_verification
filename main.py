import dlib
import sys
from skimage import io
from scipy.spatial.distance import euclidean


sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()
rects = []
shapes=[]
descriptors=[]

def open_image(pass_to_photo):
    image_photo = io.imread(pass_to_photo)
    return image_photo

def search_descriptors(rects, shapes, descriptors):
    for photo in list_names:
    image_photo = io.imread(photo)
    detect_photo = detector(image_photo, 1)
    rects.append(detect_photo[0])
    shape = sp(image_photo, detect_photo[0])
    shapes.append(shape)
    face_desc = facerec.compute_face_descriptor(image_photo, shape)
    euclidean_distance = descriptors.append(face_desc)

    return 

def decision_making(euclidean_distance):
    if euclidean_distance >= 0,6:
        return False
    else:
        return True


def main_algoritm(path, key, path):
    """main algoritm"""


if __name__ == "__main__":
    path_to_image =  sys.argv[1]
    key = 
    main_algoritm()
