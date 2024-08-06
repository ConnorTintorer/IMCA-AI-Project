# IMCA-AI-Project
```text
 
  _    _    _____   _____     _____   __  __    _____            
 | |  | |  / ____| |_   _|   |_   _| |  \/  |  / ____|     /\    
 | |  | | | |        | |       | |   | \  / | | |         /  \   
 | |  | | | |        | |       | |   | |\/| | | |        / /\ \  
 | |__| | | |____   _| |_     _| |_  | |  | | | |____   / ____ \ 
  \____/   \_____| |_____|   |_____| |_|  |_|  \_____| /_/    \_\
                                                                 
                                                                 
```                                                  
                                                     
## **Description**
Takes a directory of images labeled with IDs and returns a list of classifications related to the image
Uses ChatGPT-4o Vision API to generate responses
Stores keyword classification data in image_data.csv

## **Using your API Key**
To use your OpenAI key create a text file under /src titled "Key.txt" and paste your API key.

## **Libraries Used**
- OpenAI: (https://platform.openai.com/docs/api-reference/introduction)
- pandas: (https://pandas.pydata.org/docs/)
- pillow: (https://pillow.readthedocs.io/en/stable/)