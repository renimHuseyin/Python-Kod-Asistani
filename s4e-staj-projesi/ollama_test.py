import requests # type: ignore

def ollama_query(prompt):
    url = 'http://localhost:11434/api/generate'
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    result = response.json()
    return result['response']

# Test edelim
cevap = ollama_query("Merhaba! Basit bir Python döngüsü yaz.")
print(cevap)
