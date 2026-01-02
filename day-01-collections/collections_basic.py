
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


# QDRANT SUPPORTS SPARSE VECTORS AS A FIRST-CLASS CITITZEN

# collections can contain sparse vectors as additional named vectors alongside regular dense vectors

'''
 VERY IMPORTANT RULES :-

1. SPARSE VECTORS MUST BE NAMED 

"text": modles.SparseVectorParams()

2. THE NAME OF THE SPARSE & DENSE VECTORS SHOULD NOT BE THE SAME 

dense_vector_name = "embedding"
sparse_vector_name = "text"  

3. THE DISTANCE METRICS SHOULD ALWAYS BE DOT 

distance= DOT(fixed)  , because word overlap count / importnce ke liyee dot product best hota hai

client.create_collection(
      collection_name = "{collectiion_name}",
      vectors_config={} ,  no dense vectors yet
      sparse_vectors_config={
             "text" : models.SparseVectorParams(),
      },
)
'''

# checking that if the particular collection exists or not
'''
 client.collection_exists(collection_name="{collection_name}")
'''

# updating the collection parameters
'''
client.update_collection(
   collection_name = "{collection_name}",
   optimizers_config=models.OptimizersConfigDiff(indexing_threshold=10000),
)
'''

'''
UPDATING VECTOR PARAMETERS

client.update_collection(
    collection_name="{collection_name}",
    vectors_config={
        "my_vector": models.VectorParamsDiff(
            hnsw_config=models.HnswConfigDiff(
                m=32,
                ef_construct=123,
            ),
            quantization_config=models.ProductQuantization(
                product=models.ProductQuantizationConfig(
                    compression=models.CompressionRatio.X32,
                    always_ram=True,
                ),
            ),
            on_disk=True,
        ),
    },
    hnsw_config=models.HnswConfigDiff(
        ef_construct=123,
    ),
    quantization_config=models.ScalarQuantization(
        scalar=models.ScalarQuantizationConfig(
            type=models.ScalarType.INT8,
            quantile=0.8,
            always_ram=False,
        ),
    ),
)

While updating vector name should be mentioned .

models.HnswConfigDiff(
    m=32,
    ef_construct=123
)

INTUITION :
    
     m -> graph connectivity (higher means , better recall and large memory)
     ef_construct -> index build quality (slow build , better index)

Quantization :- 
                it is used to compress the vectors (precision less , memory less)

In this we can see 2 types of quantization:

PRODUCT QUANTIZATION-

models.ProductQuantization(
      product = models.ProductQuantizationConfig(
           compression= models.CompressionRatio.X32,
           always_ram= True
      )
)
meaning :- breaking down the vectors in small parts . Memory usage lowers as well as the accuracy

use case :- Use when scaling hugely , cost sensitivity , recall drop is acceptable

SCALAR QUANTIZATION -

models.ScalarQuantization(

      scalar = models.ScalarQuantizationConfig(
           type= models.ScalarType.INT8,
           quantile = 0.8,
           always_ram = False,
      )
)

meaning :- conversion from float -> UINT8 , makes it simpler and faster and it is moderate compression

use case :- want balanced performance and common choice in RAG systems

VECTOR LEVEL ALWAYS OVERRIDES COLLECTION LEVEL

'''