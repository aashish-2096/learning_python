from ollama import chat, ChatResponse

def chatResponse( message: dict, model:str):
    print("Received Req")
    print(str(dict))
    response: ChatResponse = chat(model= model, messages=[message,])
    return response.message.content