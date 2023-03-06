import banana_dev as banana
import base64
from io import BytesIO
from PIL import Image
import sys
import os

def extract_image(out):
    # Extract the image and save to output.jpg
    image_byte_string = out["modelOutputs"][0]["images"][0]
    image_encoded = image_byte_string.encode('utf-8')
    image_bytes = BytesIO(base64.b64decode(image_encoded))
    image = Image.open(image_bytes)
    image.save("output.jpg")

def main(argv):
    # concatenate the arguements
    argv = " ".join(argv)
    model_inputs = {
        "endpoint": "txt2img",
        "params": {
            "prompt": argv,
            "negative_prompt": "cartoonish, low quality",
            "steps": 25,
            "sampler_name": "Euler a",
            "cfg_scale": 7.5,
            "seed": 42,
            "batch_size": 1,
            "n_iter": 1,
            "width": 512,
            "height": 512,
            "tiling": "false"
        }
    }

    # Load API and Model Keys from .env
    api_key = os.environ.get("API_KEY")
    model_key = os.environ.get("MODEL_KEY")

    # Run the model
    out = banana.run(api_key, model_key, model_inputs)

    # extract the image
    extract_image(out)


if __name__ == "__main__":
    # take in commandline arguements
    main(sys.argv[1:])