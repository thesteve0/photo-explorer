import os
import fiftyone as fo
import fiftyone.zoo as foz
import fiftyone.operators as foo
import fiftyone.brain as fob
import numpy as np

os.environ['FIFTYONE_ALLOW_LEGACY_ORCHESTRATORS'] = 'true'

dataset = fo.load_dataset("photo-album")

resnet18_zoo_model = foz.load_zoo_model("resnet18-imagenet-torch")
openclip_zoo_model = foz.load_zoo_model("open-clip-torch")

# https://github.com/harpreetsahota204/aim-embeddings-plugin?tab=readme-ov-file#operator-usage-via-sdk
aim_embeddings = foo.get_operator("@harpreetsahota/aimv2_embeddings/compute_aimv2_embeddings")



fob.compute_visualization(dataset, model=resnet18_zoo_model, embeddings="resnet18_zoo_embedding",
                          brain_key="resnet18_zoo_embed")

fob.compute_visualization(dataset, model=openclip_zoo_model, embeddings="openclip_zoo_embedding",
                          brain_key="openclip_zoo_embed")

aim_embeddings(
    dataset,
    model_name="apple/aimv2-huge-patch14-448",  # Choose any supported model
    embedding_types="cls",  # Either "cls" or "mean"
    emb_field="aimv2-plugin-embedding",  # Name for the embeddings field
)

fob.compute_visualization(dataset, embeddings="aimv2_plugin_embedding", brain_key="aimv2_plugin_embed")

openclip_resnet_concat = np.concatenate((dataset.values("resnet18_zoo_embedding"), dataset.values("openclip_zoo_embedding")), axis=1)
all_model_embed_concat = np.concatenate((dataset.values("resnet18_zoo_embedding"), dataset.values("openclip_zoo_embedding"), dataset.values("aimv2_plugin_embedding")), axis=1)
fob.compute_visualization(dataset, embeddings=openclip_resnet_concat, brain_key="openclip_resnet_concat")
fob.compute_visualization(dataset, embeddings=all_model_embed_concat, brain_key="all_model_embed_concat")

