# IMCA Artwork Keyword Classification
```text
 
  _    _    _____   _____     _____   __  __    _____            
 | |  | |  / ____| |_   _|   |_   _| |  \/  |  / ____|     /\    
 | |  | | | |        | |       | |   | \  / | | |         /  \   
 | |  | | | |        | |       | |   | |\/| | | |        / /\ \  
 | |__| | | |____   _| |_     _| |_  | |  | | | |____   / ____ \ 
  \____/   \_____| |_____|   |_____| |_|  |_|  \_____| /_/    \_\
                                                                 
                                                                 
```                                                  
                                                     
## **About**
The IMCA Artwork Keyword Classification is designed to generate and assign keyword "tags" to artworks in a museum's collection. The program is designed to allow for high scalibility as the collection of the museum increases.
The program takes in a directory of images and returns a list of classifications related to each image. The classifications are currently a predetermined, set list of around 30 words.
OpenAI's GPT-4o model is used to generate responses based on image input. 
Keyword classification data is stored in image_data.csv with the format "id, filename, classification"

## **Using your API Key**
To use your OpenAI key create a text file under /src titled "Key.txt" and paste your API key.

## **How to Run**
To run the program you just need to run Interface.py. This will create a GUI window from which you can select the directory of images as well as how many images you want to process. After selecting the folder, wait for the program to finish. The runtime will be printed to the terminal and the list of classifications will be written to "image_data.csv"

## **Constraints/Details**
**Model**
- Currently, GPT4o is the only model with vision capabilities so this model must be used
- Specific restraints relating to GPT4o and Vision can be read about here: (https://platform.openai.com/docs/guides/vision)

**Image format**
- Filenames of all images must be unique and correlate to the desired ID of the image
- Images must be JPEG
- Each image must be below 20MB

**Runtime**
- Large directories will likeley take a _very_ long time to run. For reference, a folder of 15 images takes around 60 seconds to run
- As the GUI uses tkinter without threading, the window will freeze after a folder is selected. Simply wait for the operation to complete

**Cost**
- Uses the API key linked with your openAI account to generate responses
- a folder of 15 images costs about $0.03 USD
- Image detail is set to "low" to decrease costs
- max_tokens is set to 300 per image response (note this does not include the amount of tokens required for the prompt itself)

**Responses**
- Assigned keywords are stored in "image_data.csv"
- It has been observed that sometimes keywords not included in the initial prompt are generated anyway.  



## **Libraries Used**
- OpenAI: (https://platform.openai.com/docs/api-reference/introduction)
- pandas: (https://pandas.pydata.org/docs/)
- pillow: (https://pillow.readthedocs.io/en/stable/)
