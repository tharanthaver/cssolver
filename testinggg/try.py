import requests

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0aGFyYW50aGF2ZXIzM0BnbWFpbC5jb20iLCJpYXQiOjE3MzU2NTA0OTJ9.7D9gesc4e3JZALLy2W-YqdJhgjX_PYhVieDno7I3pV8"
url = "https://api.hyperbolic.xyz/v1/chat/completions"
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

# Ask the API to calculate the factorial of 5
data = {
    "messages": [{"role": "user", "content": "how is earth"}],
    "model": "meta-llama/Llama-3.3-70B-Instruct",
    "max_tokens": 50  # Increase max_tokens to allow more of the response
}


response = requests.post(url, headers=headers, json=data)

print(response.status_code, response.text)
