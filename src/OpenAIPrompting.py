from openai import OpenAI
import convertbase64

# API key: 
# sk-proj-YEo5jXJ0n2Dl9UCy2PmkT3BlbkFJt5wuh5o3nTg2gsJMg4e4
client = OpenAI(api_key= "sk-proj-YEo5jXJ0n2Dl9UCy2PmkT3BlbkFJt5wuh5o3nTg2gsJMg4e4")

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
def get_image_query(request:str, image_url:str) -> str:
    """Completes a GPT4o Query with the specified request string and image url string
        Returns a string containing the AI response"""
    
    #ex: image_url = "https://wikipedia.org/xyz"
    response = client.chat.completions.create(
        model = "gpt-4o",
        max_tokens = 500,
        messages = [
            {"role": "system", "content": "You are an assistant that provides information about a museum's artwork via providing a list of classifications"},
            {"role": "user", "content": request},
            {"type": "image_url", "image_url": {"url": image_url}, 
             "detail": "low"}
            
        ]
    )

    return response.choices[0].message.content

    # print("Image Response: " + response.choices[0].message.content)