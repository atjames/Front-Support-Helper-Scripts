import requests
import json

url = "FRONT_API_URL_HERE"
API_TOKEN = "YOUR_API_TOKEN_HERE" # get your own API Token dude 

headers = {
    'Authorization': f'Bearer {API_TOKEN}', 
}

# Adjust requests method based on endpoint. For this template it's issuing a GET Request to the url string. 

response = requests.get(url, headers=headers)

# Adjust error handling depending on endpoint being used. Our endpoints might not always return 200, 202, or 204 status codes. 

if response.status_code in {200, 202, 204}:
    if response.content: 
        print("Request successful. Content returned.")
        try:
            data = response.json()
            print(data)
            with open("response_data.txt", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print("Response logged to txt file")
        except json.decoder.JSONDecodeError as e:
            print("JSON decoding error:", e)
            print("Response content:", response.text)
    else:
        print("Request successful. No content returned.")
else:
    try:
        data = response.json()
        print(data)
        with open("response_data.txt", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("Response logged to txt file")
    except json.decoder.JSONDecodeError as e:
        print("JSON decoding error:", e)
        print("Response content:", response.text)