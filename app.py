from stable_audio_tools.interface.gradio import create_ui
import subprocess
import torch
import os
import gdown

def main():
    args = {
        "model_config": "model_config.json",
        "ckpt_path": "stable-audio_loop_names_ft.ckpt",
        "username": "output",
        "password": "becreative",
        "model_half": True
    }
    torch.manual_seed(42)
    # https://drive.google.com/file/d/1-BUWjuYb5UIlOtYEjs8iyMFb3rdbIMY-/view?usp=sharing
    #
    if not os.path.exists("stable-audio_loop_names_ft.ckpt"):
        gdrive_id = "1-BUWjuYb5UIlOtYEjs8iyMFb3rdbIMY-"
        gdown.download(f"https://drive.google.com/uc?id={gdrive_id}", "stable-audio_loop_names_ft.ckpt", quiet=False)
    interface = create_ui(
        model_config_path = args["model_config"],
        ckpt_path=args["ckpt_path"],
        model_half=args["model_half"]
    )
    interface.queue()
    interface.launch(debug = False, auth=(os.environ.get("USERNAME"), os.environ.get("PASSWORD")), ssr_mode=False, share=True)

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='Run gradio interface')
    # parser.add_argument('--pretrained-name', type=str, help='Name of pretrained model', required=False)
    # parser.add_argument('--model-config', type=str, help='Path to model config', required=False)
    # parser.add_argument('--ckpt-path', type=str, help='Path to model checkpoint', required=False)
    # parser.add_argument('--pretransform-ckpt-path', type=str, help='Optional to model pretransform checkpoint', required=False)
    # parser.add_argument('--share', action='store_true', help='Create a publicly shareable link', required=False)
    # parser.add_argument('--username', type=str, help='Gradio username', required=False)
    # parser.add_argument('--password', type=str, help='Gradio password', required=False)
    # parser.add_argument('--model-half', action='store_true', help='Whether to use half precision', required=False, default=True)
    # args = parser.parse_args()

    main()