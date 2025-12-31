
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

