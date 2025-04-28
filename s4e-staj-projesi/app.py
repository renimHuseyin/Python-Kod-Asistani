from flask import Flask, render_template, request # type: ignore
import requests # type: ignore
import re

app = Flask(__name__)

def ollama_query(prompt):
    url = 'http://host.docker.internal:11434/api/generate'
    
    system_instruction = (
        "Aşağıdaki kullanıcı isteğine göre yalnızca Python dilinde kod üret.\n"
        "Cevabın ilk satırı açıklayıcı bir başlık olsun.\n"
        "Başlıktan sonra yalnızca bir adet Python kod bloğu ver.\n"
        "Kod bloğunu ```python ... ``` içinde ver.\n"
        "Açıklama ya da fazladan metin ekleme.\n\n"
    )

    full_prompt = system_instruction + prompt

    payload = {
        "model": "mistral",
        "prompt": full_prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    result = response.json()
    return result['response']

def extract_code_and_title(response):
    code_block = re.search(r"```python(.*?)```", response, re.DOTALL)
    code = code_block.group(1).strip() if code_block else "Kod bulunamadı."

    lines = response.strip().split('\n')
    title = lines[0] if lines else "Başlık bulunamadı."

    return title, code

@app.route('/', methods=['GET', 'POST'])
def index():
    title = None
    code = None

    if request.method == 'POST':
        prompt = request.form['prompt']
        response = ollama_query(prompt)
        title, code = extract_code_and_title(response)

    return render_template('index.html', title=title, code=code)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
