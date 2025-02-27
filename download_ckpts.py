from huggingface_hub import hf_hub_download

hf_hub_download(repo_id="stabilityai/stable-audio-open-1.0", filename="model.ckpt", local_dir="ckpts")
hf_hub_download(repo_id="stabilityai/stable-audio-open-1.0", filename="model_config.json", local_dir="ckpts")