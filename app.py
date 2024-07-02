import streamlit as st
from engine import prediction
from anime_classes import animes
from PIL import Image
import requests
import json

def get_anime_details(anime_name):
    url = "https://api.jikan.moe/v4/anime"
    params = {
        "q": anime_name,
        "sfw": 'true'  # Correctly passing the boolean value as a string
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        with open('response.json', 'w') as f:
            json.dump(response.json(), f, indent=4)
        return response.json()
    else:
        with open('error.json', 'w') as f:
            json.dump(response.json(), f, indent=4)
        return f"Error: {response.status_code}, {response.json()}"


def predict(uploaded_file):
    if uploaded_file is not None:
        # Load and preprocess the image
        image = Image.open(uploaded_file)
        class_index = prediction(uploaded_file)
        label = animes[class_index]
        return image, class_index, label
    else:
        return None, None, None


def main():
    st.title('Anime Detection App')

    uploaded_file = st.file_uploader("Choose an Image...", type=["jpg", "jpeg", "png"])
    image, class_index, label = predict(uploaded_file)

    if uploaded_file is not None and label:
        st.image(image)
        st.write("Prediction : ", label)
        st.divider()

        anime_details = get_anime_details(anime_name=label)
        st.title("Anime Details")
        st.divider()

        if anime_details and isinstance(anime_details, dict) and anime_details.get('data'):
            image_url = anime_details['data'][0]['images']['jpg']['image_url']
            st.image(image_url)
            title = anime_details['data'][0]['title']
            st.write(f"Title : {title}")
            st.write(f"English Title : {anime_details['data'][0]['title_english']}")
            st.write(f"Japanese Title : {anime_details['data'][0]['title_japanese']}")
            
            genres = anime_details['data'][0]['genres']
            st.write(f"Genres : {[name['name'] for name in genres]}")

            st.divider()

            synopsis = anime_details['data'][0]['synopsis']
            st.write("Synopsis")
            st.write(synopsis)

            st.divider()

            st.write("Trailer")
            trailer = anime_details['data'][0]['trailer']
            try:
                st.image(trailer['images']['maximum_image_url'])
                st.write(f"Url : {trailer['url']}")
            except:
                st.write("Trailer not available")
        else:
            st.error("Anime details not found or API request failed.")


if __name__ == '__main__':
    main()
