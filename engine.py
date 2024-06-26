import torch
from torchvision import models, transforms
from PIL import Image
import numpy as np
from anime_classes import animes
import streamlit as st

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = models.resnet50(pretrained=True)

# Modifying the fully connected layer
num_classes = 231
model.fc = torch.nn.Linear(model.fc.in_features, num_classes)
model = model.to(device)

# Load the model checkpoint
model_checkpoint_path = 'Model assests/20epoch-model.pth'
model.load_state_dict(torch.load(model_checkpoint_path, map_location=device))
model.eval()

transform = transforms.Compose([
    transforms.Resize(256),  # Resize to 256x256
    transforms.CenterCrop(224),  # Center crop to 224x224
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Function for image prediction
def prediction(image_path):
    try: 
        # Load and preprocess the image
        image = Image.open(image_path)
        image = transform(image).unsqueeze(0).to(device)  # Add batch dimension and move to device

        # perform prediction
        with torch.no_grad():
            output = model(image)
            output = output.cpu().numpy()
        
        index = np.argmax(output)
        return index
    
    except Exception as e:
        st.write(f"Error processing image {image_path}")

