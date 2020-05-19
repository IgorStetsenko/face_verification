import glob
import dlib
from skimage import io
from scipy.spatial.distance import euclidean
from os.path import basename
import re
import timeit
import sys

sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()

def open_image_web(pass_to_photo):
    '''Function open image of web camera
    input: path to webcam photo
    output: webcam photo'''
    image_photo_web = io.imread(pass_to_photo)
    return image_photo_web

def get_name_image(pass_to_photo):
    '''The function determines the path to the webcam
    input:path to webcam photo
    otput:photo name''' 
    name_image_web = []
    name = basename(pass_to_photo)
    name_image_web.append(name)
    return name_image_web

def create_list_passes(pass_to_passports):
    '''The function creates a list of found paths to photos with passports
    input:path to passports photo
    output: passes list'''
    name_photo_file = (glob.glob('{0}/*.jpg'.format(pass_to_passport)))
    list_passes=[i.replace('\\', '/') for i in name_photo_file]
    return list_passes

def search_pass_to_passport(list_passes, name_image):
    '''The function searches for the path to the passport 
        photo whose name matches the name of the photo from the web camera
        input: passes list, name image web camera
        output: pass to passport image'''
    pass_list = ''
    for pass_list in list_passes:
        text = pass_list
        for j in name_image:
            find = re.search(j, text)
            if find:
                pass_to_passports=pass_list
                return pass_to_passports

def open_image_passport(pass_to_passports):
    '''Function open image of passport
    input: path to passport photo
    output: passport photo'''
    image_photo_passport = io.imread(pass_to_passports)
    return image_photo_passport

def comparison_photo(pass_to_photo, pass_to_passport):
    
    list_names = []
    rectangle_face = []
    shapes=[]
    descriptors=[]
    list_names.append(pass_to_photo)
    list_names.append(pass_to_passport)
    for photo in list_names:
        image_photo = io.imread(photo)
        detect_photo = detector(image_photo, 1)
        rectangle_face.append(detect_photo[0])
        shape = sp(image_photo, detect_photo[0])
        shapes.append(shape)
        face_desc = facerec.compute_face_descriptor(image_photo, shape)
        descriptors.append(face_desc)
    return rectangle_face, shapes, descriptors

def calculate_euclidean(descriptors):
    euclidean_distance=euclidean(descriptors[0], descriptors[1])
    return euclidean_distance

def decision_making(euclidean_distance):
    if euclidean_distance < 0.6:
        return print("Verification Passed")
    else:
        return print("Verification not Passed !!!!")

def main_algoritm(**kwargs):
    """main algoritm"""
    image_photo_web = open_image_web(pass_to_photo)
    name_image_web=get_name_image(pass_to_photo)
    list_passes=create_list_passes(pass_to_photo)
    pass_to_passports=search_pass_to_passport(list_passes, name_image_web)
    image_photo_passport=open_image_passport(pass_to_passports)
    rectangle_face, shapes, descriptors=comparison_photo(pass_to_photo, pass_to_passports)
    decision_making(calculate_euclidean(descriptors))
    print("function execution time is - " + str(timeit.timeit( "main_algoritm", 
    setup="from __main__ import main_algoritm", number=1)))

if __name__ == "__main__":
    
    print(sys.argv)

    try:
        pass_to_photo =  sys.argv[1]
        pass_to_passport = 'data_base/passports' 
        
    except Exception as error:
        print(error)
        raise AttributeError

    main_algoritm()
        

    

   
