import dlib
import sys
from skimage import io
from os.path import basename
from scipy.spatial.distance import euclidean


sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()
rects = []
shapes=[]
descriptors=[]

def open_image_web(pass_to_photo):
    ''''''
    name_image = []
    image_photo_web = io.imread(pass_to_photo)
    name = basename(pass_to_photo)
    name_image.append(name)
    return image_photo_web, name_image_web

def open_image_passport(pass_to_passport):
    ''''''
    image_photo_passport = io.imread(pass_to_photo)
    return image_photo_passport, name_image_passport

def create_list_passes(pass_to_passport):
    name_photo_file = (glob.glob('{0}/*.jpg'.format(pass_to_passport)))
    list_passes=[i.replace('\\', '/') for i in name_photo_file]
    return list_passes

def search_pass_to_passport(list_passes, name_image):
    i = ''
    for i in list_passes:
        text = i
        for j in name_image:
            find = re.search(j, text)
            if find:
                pass_to_passport=i
                return pass_to_passport


def list_image(name_image_web, name_image_passport):


def search_descriptors(rects, shapes, descriptors):
    for photo in list_names:
        detect_photo = detector(image_photo, 1)
        rects.append(detect_photo[0])
        shape = sp(image_photo, detect_photo[0])
        shapes.append(shape)
        face_desc = facerec.compute_face_descriptor(image_photo, shape)
        euclidean_distance = descriptors.append(face_desc)

        return euclidean_distance


def decision_making(euclidean_distance):
    if euclidean_distance < 0.6:
        return print("Verification Passed")
    else:
        return print("Verification not Passed !!!!")




def main_algoritm(pass_to_photo, key, path):
    """main algoritm"""
    image, photo = open_image(pass_to_photo, pass_to_passport)




    if key == 'run':
        cv2.imwrite(path_to_save, image_with_contours)  # run and get result
    elif key == 'save':
                                                        # save descriptors
    else key = 'time':




if __name__ == "__main__":
    
    print(sys.argv)

    try:
        pass_to_photo =  sys.argv[1]
        pass_to_passport = 'data_base/passports'
        path_to_save 
        main_algoritm()

        key = sys.argv[2]
            if key not in ['run', 'save', 'time']:
                assert False, 'Error'
            if key == 'o':
                try:
                    path_to_save = 'data_base/save/out.jpg'
                except:
                    print('Error')


    except Exception as error:
        print(error)
        raise AttributeError
        

    

   
