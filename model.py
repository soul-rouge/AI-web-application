from transformers import ViltProcessor, ViltForQuestionAnswering   
#transformers is a library developed by huggingface that allows us to use their models.
#pipeline is their high-level API and ViltProcessor is their lower-level API that lets us specify the processor and other things.
#import requests
from PIL import Image   #library for image processing.

# prepare image + question
#url = "http://images.cocodataset.org/val2017/000000039769.jpg"
#image = Image.open(requests.get(url, stream=True).raw)
#text = "How many cats are there?"

processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
# We don't want to initialize the model again and again so it should be outside the below function.

def model_pipeline(text: str, image: Image):

    # prepare inputs
    encoding = processor(image, text, return_tensors="pt")

    # forward pass
    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()
    return model.config.id2label[idx]
