from setuptools import setup, find_packages

setup(
    name='computer_vision_workshop',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'opencv-python',
        'ultralytics',
        'torch',
        'torchvision',
        'torchaudio',
        'matplotlib'
    ],
)