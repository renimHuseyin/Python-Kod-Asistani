import requests # type: ignore
import re

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

def extract_code_and_title(response):
    # Kod bloğunu çek
    code_block = re.search(r"```python(.*?)```", response, re.DOTALL)
    code = code_block.group(1).strip() if code_block else "Kod bulunamadı."

    # İlk satırları başlık olarak al
    lines = response.strip().split('\n')
    title = lines[0] if lines else "Başlık bulunamadı."

    return title, code

# Test prompt
response_text = ollama_query("Basit bir Python for döngüsü örneği ver ve açıklamasını yap.")
title, code = extract_code_and_title(response_text)

print("📌 Başlık:")
print(title)
print("\n💻 Kod:")
print(code)
