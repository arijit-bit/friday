from duckgpt import DuckGPT
try:
    client = DuckGPT(model="gpt-4o-mini")
    # models = client.Models()
    response = client.Chat("can you response like a human in chat", [])
    print(response)
except Exception as e :
    print(e)