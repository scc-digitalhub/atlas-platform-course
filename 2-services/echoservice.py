import json

def init(context):
    print("some initialization function")
    setattr(context, "value", "some value")

def serve(context, event):

    if isinstance(event.body, bytes):
        body = json.loads(event.body)
    else:
        body = event.body
    context.logger.info(f"Received event: {body}")
    text = body["text"]

    return {"result": f"hello {text} from '{context.value}'"}
