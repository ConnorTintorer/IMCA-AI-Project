import OpenAIPrompting
import convertbase64
import pandas as pd
import json


PROMPT = """Given the following image data, please check if the image contains any of the following keywords:
    Abstract, Night, Body of Water, Boat, Person, Mountain, Fruit, Still-life, Trees, Landscape, House, Infrastructure, Building, Bridge, Day, Light, Transportation, Animal, Dog, Cat, Horse, Cow, River, Lake, Ocean, Flower, Nude, Historical, Portraiture, Genre, Woman, Man, Child, Bird, Garden, Geometric, Biomorphic, Monochrome, Gestural Abstraction, Symmetry, Text, Forshortening, Pattern, Brushstrokes

    Please return the identified keywords as a comma-separated list. If no keywords are identified, return 5 custom keywords not on the list."
    """

# alternative prompt for generating descriptions for the artwork
#PROMPT = "Given the following image, provide a visual description of the artwork"

def get_descriptions_instead(image_data:list):
    request = "Provide a brief, 2-3 sentence description for the following image"
    response_list = [] # list of dictionaries where each dictionary contains id, gpt4o response

    for image in image_data:
        base64 = image["base64"]

        api_response = OpenAIPrompting.get_image_query(request, base64)
        response_list.append({"id": image['id'], "filename": image['filename'], "response": api_response})

    return response_list

def call_gpt(image_data:list)->list:
    ''' loops through all the images and makes api calls for each of them
    
        Args: image_data: list of dictionarys containing the image data

        Returns: List of Unfilitered query responses'''
    
    # request = "Describe the provided image by returning a list of single-word keyword classifications"
    # other example to filter for specific, provided keywords
    request = PROMPT
    response_list = [] # list of dictionaries where each dictionary contains id, gpt4o response

    with open("raw_response.csv", 'w', encoding='utf-8') as file:
        for image in image_data:
            base64 = image["base64"]

            api_response = OpenAIPrompting.get_image_query(request, base64)
            response_list.append({"id": image['id'], "filename": image['filename'], "response": api_response})
            file.write(f"filename: {image['filename']}, response:  {api_response}")

    return response_list


def filter_response(classified_images:list)->pd.DataFrame:
    """Filters the gpt responses to convert the string response into a list of classifications for each artwork
    
        Args: classified_images: List of dictionaries including id, filename, gpt-4o response in string format"""
    
    for image in classified_images:
        image['classifications'] = image['response'].strip().split() # splits response by word
        del image['response'] # removes raw string response, replacing it with a classifications list

    df = pd.DataFrame(classified_images)
    df['classifications'] = df['classifications'].apply(lambda x: ' '.join(x))
    
    return df


def write_to_csv(filtered:pd.DataFrame)->None:
    """Writes all relevant data to a csv file including:
            image_id
            classification list
            filename
        
        Args: filtered -> list of dictionarys containing the filtered data with the above key, value pairs
        
        Returns: None"""

    filtered.to_csv("image_data.csv", index=False)

@staticmethod
def process_images(path, num_files=0):
    """Processes all the images in the given directory
        Writes results to csv file"""
    image_data = convertbase64.get_image_data(path, num_files)
    classified_images = call_gpt(image_data)
    filtered_images = filter_response(classified_images)
    write_to_csv(filtered_images)
    # print(OpenAIPrompting.print_total_tokens())
    return 0

def batch_api_call(path):
    image_data = convertbase64.get_image_data(path)
    load_into_json(image_data)
    batch = OpenAIPrompting.create_batch("image_descriptions.jsonl")
    return batch
    
    
def get_results(batch)->str:
    """Takes in batch object
    Gets the results of the batch after 24 hours
    Returns the string of results"""
    results = OpenAIPrompting.retrieve_batch(batch)
    return results

def load_into_json(image_data):
    """Loads the image data into a json file so that it can be used for batch API calls"""
    model = "gpt-4o"
    prompt = PROMPT
    for image in image_data:
        base64_image = image["base64"] # or use image["url"] if using URLs
        request_data = {
            "model": model,
            "max_tokens": 500,
            "image_id": image["id"],  # Including image ID for reference in the response
            "messages": [
                {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                            "detail": "low"
                        }
                    }
                ]
                }
            ]
            
        }
        # jsonl_data.append(request_data)
        
    with open("image_descriptions.json", "a") as f:
        f.write(json.dumps(request_data) + '\n')

#PATH = 'C:/Users/conno/IMCATestProject/data/People'
PATH = ''

if __name__ == "__main__":
    # for testing only
    process_images(PATH)
    