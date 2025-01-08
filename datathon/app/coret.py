import torch
from PIL import Image
import open_clip
from qdrant_client import QdrantClient
from qdrant_client.http import models as qdrant_models
from qdrant_client.models import Distance, VectorParams
from open_clip import tokenizer
# Specify the path to your locally downloaded model
model_path = "../marqo-gcl-vitl14-124-gs-full_states.pt"
device = "cuda" if torch.cuda.is_available() else "cpu"
# # Load the model and preprocessing transformations
model, _, preprocess = open_clip.create_model_and_transforms('ViT-L-14', pretrained=model_path)
# tokenizer = open_clip.get_tokenizer('ViT-L-14')
model=model.to(device)
qdrant_client = QdrantClient(
    timeout=60,
    url="https://daf543ed-e223-4c78-a983-9da7e433e6e1.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key="APAxJWtNYHML7RgL6-Cruc4Yk65jex4yiKyIE_rgNI7YklAxcHI-7g",
)
print('client DONE')
title = ["Earmuffs"]
inputs = tokenizer.tokenize(title).to(device)
with torch.no_grad():
    query = model.encode_text(inputs).cpu().numpy()


# img = Image.open(r"D:\Dafa\Project\datathon-24\final\image\images_wfash\forest.jpg").convert("RGB")
# img = preprocess(img).unsqueeze(0).to(device)
# with torch.no_grad():
#     img_embedding = model.encode_image(img).cpu().numpy()

title = ["white"]
inputs = tokenizer.tokenize(title).to(device)
with torch.no_grad():
    query2 = model.encode_text(inputs).cpu().numpy()

search_results = qdrant_client.query_points(
    collection_name="titles_collection",
     query=[query2[0], query[0]],
     limit=18,
)
print(search_results)

qdrant_client.close()