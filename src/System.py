import OpenAIPrompting
import convertbase64
import pandas as pd
import csv




def call_gpt(image_data:list)->list:
    ''' loops through all the images and makes api calls for each of them
    
        Args: image_data: list of dictionarys containing the image data

        Returns: List of Unfilitered query responses'''
    
    request = "Describe the provided image by returning a list of single-word keyword classifications"
    # other example to filter for specific, provided keywords
    # request = """
    # Given the following image data, please check if the image contains any of the following keywords:
    # - people
    # - animals
    # - mountains
    # - buildings
    # - trees

    # Return a list of the keywords that are present in the image.
    # Image data: {base64_image}
    # """
    response_list = [] # list of dictionaries where each dictionary contains id, gpt4o response

    for image in image_data:
        base64 = image["base64"]

        api_response = OpenAIPrompting.get_image_query(request, base64)
        response_list.append({"id": image['id'], "filename": image['filename'], "response": api_response})

    return response_list


def filter_response(classified_images:list)->pd.DataFrame:
    """Filters the gpt responses to convert the string response into a list of classifications for each artwork
    
        Args: classified_images: List of dictionaries including id, filename, gpt-4o response in string format"""
    
    for image in classified_images:
        image['classifications'] = image['response'].strip().split() # splits response by word
        del image['response'] # removes raw string response, replacing it with a classifications list

    df = pd.DataFrame(classified_images)
    df['classifications'] = df['classifications'].apply(lambda x: ', '.join(x))
    
    return df


def write_to_csv(filtered:pd.DataFrame)->None:
    """Writes all relevant data to a csv file including:
            image_id
            classification list
            filename
        
        Args: filtered -> list of dictionarys containing the filtered data with the above key, value pairs
        
        Returns: None"""
    
    # fieldnames = ["id", "classifications", "filename"]
    # with open("image_data.csv", 'w', newline='') as f:
    #     writer = csv.DictWriter(f, fieldnames=fieldnames)
    #     writer.writeheader()
       
    #     for item in filtered:
    #         item['classifications'] = ', '.join(item['classifications'])
    #         writer.writerow(item)

    filtered.to_csv("image_data.csv", index=False)

def process_images(path):
    """Processes all the images in the given directory
        Writes results to csv file"""
    image_data = convertbase64.get_image_data(path)
    classified_images = call_gpt(image_data)
    filtered_images = filter_response(classified_images)
    write_to_csv(filtered_images)
    return 0

PATH = 'C:/Users/conno/IMCATestProject/data/People'

if __name__ == "__main__":
    # for testing only
    process_images(PATH)
    