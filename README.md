# Stable Diffusion Client

This tool allows users to enter prompts and generates images using the backend self-hosted server of Stable Diffusion. With this tool, you can easily experiment with Stable Diffusion and create amazing images with just a few commands.

___

### Setup
Assuming you have `python` and `pipenv` installed.
(Please see [this](https://pipenv.pypa.io/en/latest/install/) if you want help with that).

```
pipenv install
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
