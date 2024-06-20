# AnimeVision

Welcome to **AnimeVision**, a deep learning-powered tool that recognizes anime characters from images and provides detailed information about the anime using the Jikan REST API.

## Features

- **Image Recognition:** Finetuned ResNet50 model to detect anime names from uploaded images.
- **Anime Information:** Fetches details like title, synopsis, trailer, and genres based on the detected anime.
- **User-Friendly Interface:** Created using Streamlit for a seamless user experience.
- **Model Tuning:** Implemented in PyTorch for fine-tuning the ResNet50 model.

## How It Works

1. **Upload an Image:** Upload an image of an anime character.
2. **Model Detection:** Our finetuned ResNet50 model identifies the anime.
3. **Information Retrieval:** Fetches information related to the anime using the Jikan REST API.
4. **Display Information:** Presents the anime title, synopsis, trailer, and genres.

## Getting Started

### Prerequisites

- Python 3.7+
- PyTorch
- Streamlit
- Requests (for API calls)

### Demo video
![Untitled video - Made with Clipchamp (4)](https://github.com/Abhi-vish/Animevision/assets/109618783/bca69021-4664-4e3d-9ea1-cfa382fcde03)


### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Abhi-vish/Animevision.git
    cd Animevision
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the App

To run the Streamlit app, use the following command:
```sh
streamlit run app.py