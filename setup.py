from setuptools import setup, find_packages

setup(
    name='stable-audio-tools',
    version='0.0.21',
    url='https://github.com/Stability-AI/stable-audio-tools.git',
    author='Stability AI',
    description='Training and inference tools for generative audio models from Stability AI',
    packages=find_packages(),
    install_requires=[
        'alias-free-torch==0.0.6',
        'auraloss==0.4.0',
        'descript-audio-codec==1.0.0',
        'einops',
        'einops-exts',
        'ema-pytorch>=0.2.3',
        'encodec==0.1.1',
        'gradio>=3.42.0',
        'huggingface_hub',
        'importlib-resources==5.12.0',
        'k-diffusion==0.1.1',
        'laion-clap==1.1.4',
        'local-attention==1.8.6',
        'pandas==2.0.2',
        'prefigure==0.0.9',
        'pytorch_lightning==2.1.0',
        # 'PyWavelets==1.4.1', # removed for inference only
        # 'pypesq==1.2.4', # removed for inference only
        'safetensors',
        'sentencepiece==0.2.0',
        'torch>=2.0.1',
        'torchaudio>=2.0.2',
        'torchmetrics==0.11.4',
        'tqdm',
        'transformers',
        'v-diffusion-pytorch==0.0.2',
        'vector-quantize-pytorch==1.14.41',
        'wandb==0.15.4',
        'webdataset==0.2.100',
        'x-transformers>=1.31.14'
    ],
)
