import base64
import os
import json


def encode_image(image_path):
    '''Encodes image into a base64 representation'''
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def encode_all(dir_path:str, num_files=0)->list:
    '''Takes in a directory of images and transcribes them into base64 format
    
        returns a list of dictionaries with image IDs and base64 encoded strings'''
    base64_images = []
    files = os.listdir(dir_path)
    for i, filename in enumerate(files):
        # assuming image_id is always first 4 characters
        # skips files that do not start with a number 
        if(i >= num_files):
            break
        if(filename[:4].isdigit and filename.endswith('.jpg')):
            image_path = os.path.join(dir_path, filename)
            image_id = filename[:4]
            encoded_image = encode_image(image_path)
            base64_images.append({"id": image_id, "filename" : filename, "base64": encoded_image})
        else:
            # dump outliers into their own file 
            with open('outliers.json', 'w') as f:
                json.dump(filename, f)

    return base64_images
    
def save_image_data(image_data):
    with open('image_data.json', 'w') as f:
        json.dump(image_data, f, indent=4)


def get_image_data(dir_path:str, num_files=0)->list:
    base64_images = encode_all(dir_path, num_files)
    # save_image_data(base64_images)
    return base64_images
