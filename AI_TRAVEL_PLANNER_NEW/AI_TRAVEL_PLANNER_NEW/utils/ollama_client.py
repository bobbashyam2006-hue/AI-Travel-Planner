import json
import requests

OLLAMA_URL = 'http://localhost:11434/api/generate'
MODEL = 'llama3:latest'

def check_ollama():
    try:
        response = requests.get('http://localhost:11434/api/tags', timeout=10)
        response.raise_for_status()
        names = [m.get('name') for m in response.json().get('models', [])]
        if MODEL not in names:
            raise RuntimeError(f'{MODEL} is not installed. Installed models: {names}. Run: ollama pull llama3')
        return True
    except requests.exceptions.ConnectionError as e:
        raise RuntimeError('Ollama is not running. Start Ollama and try again.') from e

def ask_ollama(prompt):
    check_ollama()
    payload = {'model': MODEL, 'prompt': prompt, 'stream': False, 'format': 'json', 'options': {'temperature': 0.2}}
    response = requests.post(OLLAMA_URL, json=payload, timeout=180)
    response.raise_for_status()
    return response.json()['response']

def ask_ollama_json(prompt):
    text = ask_ollama(prompt).strip()
    if text.startswith('```'):
        lines = text.splitlines()[1:]
        if lines and lines[-1].strip() == '```': lines = lines[:-1]
        text = '\n'.join(lines).strip()
    return json.loads(text)
