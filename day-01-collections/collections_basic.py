
# 1. We are creating a basic collection 


from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams , Distance

# creating a local qdrant , no docker is required it will store everything in the folder we create locally , no docker and no cloud

client = QdrantClient(path="./qdrant_data")

client.recreate_collection(
    collection_name = "day_01_collections",
    vectors_config=VectorParams(
        size = 384,
        distance=Distance.COSINE
    )

)

print("COLLECTION CREATED ")


# 2. We are checking the collection's information 

info = client.get_collection("day_01_collections")
print(info)


# collection with multiple vectors example :-

#client.create_collection(
#     collection_name="{collection_name}",
#     vectors_config={
#         "image": models.VectorParams(size=4, distance=models.Distance.DOT),
#         "text": models.VectorParams(size=8, distance=models.Distance.COSINE),
#     },
# )


# Use float32 when:

# Small dataset
# Max accuracy needed
# Prototyping / research

# Use uint8 when:

# Millions of vectors
# Production RAG
# Cost matters

# from qdrant_client.models import (
#     VectorParams, Distance, QuantizationConfig
# )

# VectorParams(
#     size=768,
#     distance=Distance.COSINE,
#     quantization_config=QuantizationConfig(
#         scalar=True   # enables uint8 quantization
#     )
# )

# Use binary when:

# Massive scale (10M+)
# First-stage retrieval
# Speed > precision

# from qdrant_client.models import BinaryQuantization

# VectorParams(
#     size=768,
#     distance=Distance.COSINE,
#     quantization_config=BinaryQuantization(
#         always_ram=True
#     )
# )
