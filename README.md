# Stable Diffusion Client

This tool allows users to enter prompts and generates images using the backend self-hosted server of Stable Diffusion. With this tool, you can easily experiment with Stable Diffusion and create amazing images with just a few commands.

___

### Setup

**Step 1 - Host a Stable Diffusion Server on [Banana Dev](https://banana.dev)**

*Note: If you're a noob, I have already done that part. You just need to email me to get the API Keys.*

**Step 2 - Setup the client**

Assuming you have `python` and `pipenv` installed.
(Please see [this](https://pipenv.pypa.io/en/latest/install/) if you want help with that).

```
pipenv install
```

Then create a `.env` file in the root folder with the API keys like so:
```
API_KEY=<your api key here>
MODEL_KEY=<you model key here>
```

___
### Run
I have built a commandline tool to take in your prompt and give the output image
```
./draw "<Insert Your Prompt Here>"
```

___
### Config
You can configure the `size`, `negative prompts` and other aspects of the image through `config.json`

Example **config.json**
```
{
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
```

___
### Dev Notes
- Currently this tool has only been tested with the `Automatic1111-stable-diffusion` mod. The image saving feature might not work with other models since they give the outputs in different formats. I'm working on writing the adapters for those.

___
### Roadmap
This tool is just made for testing and seeing whethdr there is a demand for such software in the market yet. Based on the results, I will work on this further if need be.
