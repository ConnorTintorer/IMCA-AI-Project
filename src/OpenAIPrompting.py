from openai import OpenAI
    
# gets API key from private file
with open('C:/Users/conno/IMCATestProject/IMCA-AI-Project/misc/Key.txt', 'r', encoding='utf-8') as file:
    key = file.read().rstrip()
    
client = OpenAI(api_key= key)
# total_tokens = 0

def get_text_query(request:str) -> str:

    MODEL = "gpt-3.5-turbo"

    # TEXT BASED INPUT/RESPONSE
    response = client.chat.completions.create(
        model = MODEL,
        temperature = 0.2,
        max_tokens = 500,
        messages = [
            {"role": "system", "content": "You are an assistant that provides information about a museum's artwork via a list of classifications"},
            {"role": "user", "content": request}
        ]
    )

    # print("Response: " + response.choices[0].message.content)
    return response.choices[0].message.content

#IMAGE INPUT/RESPONSE
def get_image_query(request:str, base64_image:str) -> str:
    """Completes a GPT4o Query with the specified request string and image url string
        Returns a string containing the AI response"""
    
    #ex: image_url = "https://wikipedia.org/xyz"
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [
            {"role": "system", "content": "You are an assistant that provides information about a museum's artwork via providing a list of single-word classifications"},
            {"role": "user", "content": [
                {"type": "text", "text": request},
                {"type": "image_url", 
                "image_url": {"url": f"data:image/jpeg;base64,{base64_image}",
                "detail": "low"}
                }
            ]}
        ],
        max_tokens = 300,
    )
    
    # total_tokens += response.usage.total_tokens
    
    return response.choices[0].message.content # gives just the text generated by the prompt

    # print("Image Response: " + response.choices[0].message.content)

# def print_total_tokens():
#     print(total_tokens)

# Batch
def create_batch(json_data):  
    """Uploads batch input file and creates a batch
        Returns batch object with metadata about batch"""
    batch_input_file = client.files.create(
    file=open(json_data, "rb"),
    purpose="batch"
    )
    
    # create batch
    batch_input_file_id = batch_input_file.id

    batch = client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/chat/completions",
    completion_window="24h",
    metadata={
      "description": "Art Classifications"
        }
    )
    
    return batch

def retrieve_batch(file:str)->str:
    """Takes in file path containing batch data
        Returns the results as a string"""
    file_response = client.files.content(file)
    return file_response.text
    
def cancel_batch(batch):
    """Cancels batch request"""
    client.batches.cancel(batch)
    