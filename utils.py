import json

def safe_json_load(text):
    try:
        return json.loads(text)
    except:
        text = text.strip("```json").strip("```")
        return json.loads(text)

def pretty_print(data):
    print(json.dumps(data, indent=2, ensure_ascii=False))
