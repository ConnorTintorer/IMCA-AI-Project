import OpenAIPrompting
import convertbase64
import pandas as pd
import csv


PATH = 'C:/Users/conno/IMCATestProject/data/People'

def call_gpt(image_data:list)->list:
    ''' loops through all the images and makes api calls for each of them
    
        Args: image_data: list of dictionarys containing the image data

        Returns: Unfilitered query response'''
    
    request = "Describe the provided image by giving a list of single-word keywords"
    for image in image_data:
        OpenAIPrompting.get_image_query(request, image[2])

def filter_response():
    """Filters the gpt responses to assemble a list of classifications for each artwork"""
    pass

def main():
    image_data = convertbase64.get_image_data(PATH)
    classified_images = call_gpt(image_data)