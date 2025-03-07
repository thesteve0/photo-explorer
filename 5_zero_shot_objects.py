# Don't forget embeddings on objects

import os
import fiftyone as fo
import fiftyone.utils.ultralytics as fou

from ultralytics import YOLO
import fiftyone.zoo as foz
from fiftyone.utils.transformers import torch

os.environ['FIFTYONE_ALLOW_LEGACY_ORCHESTRATORS'] = 'true'

dataset = fo.load_dataset("photo-album")

### Read the classification classes
with open("zero-shot-classes.csv", 'r', encoding='utf-8') as file:
    lines = file.readlines()

classes = [line.rstrip('\n').replace("\"", "") for line in lines]

# aim_classification_model = foz.load_zoo_model(
#     "zero-shot-classification-transformer-torch",
#     name_or_path="apple/aimv2-large-patch14-224-lit",
#     classes=classes,
#     device="cuda" if torch.cuda.is_available() else "cpu",
# )
#
# dataset.apply_model(aim_classification_model, label_field="zero_shot_labels")

model = YOLO("yolo11s.pt")
dataset.apply_model(model, label_field="zero_shot_objects")

