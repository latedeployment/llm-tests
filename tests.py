import ollama

def get_installed_model_names():
    return [m['name'] for m in ollama.list()['models']]

def get_requests():
    requests = []
    with open('requests.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if not line.startswith('#'):
                 requests.append(line)

    return requests



def main():
    requests = get_requests()
    models = get_installed_model_names()
    for r in requests:
        print(f'REQUEST {r}')
        for m in models:
            print(f"IN {m}")
            response = ollama.chat(model=m, messages=[{'role': 'user', 'content': r}])
            print(response['message']['content'])



main()




