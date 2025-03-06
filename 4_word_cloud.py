import os
import fiftyone as fo
import fiftyone.operators as foo
import fiftyone.zoo as foz

os.environ['FIFTYONE_ALLOW_LEGACY_ORCHESTRATORS'] = 'true'

dataset = fo.load_dataset("photo-album")

moondream_operator = foo.get_operator("@harpreetsahota/moondream2/moondream")

moondream_operator(
    dataset,
    revision="2025-01-09",
    operation="query",
    output_field="one_word_moonbeam",
    query_text="what is one word to describe this image?",
    allow_delegated_execution=True,
    default_choice_to_delegated=True,
    delegate=True
)

model = foz.load_zoo_model(
    "open-clip-torch",
    text_prompt="what is one word to describe this image?"
)

dataset.apply_model(model, label_field="one_word_openclip")

# session = fo.launch_app(dataset)
# session.wait(-1)