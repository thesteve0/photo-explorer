import os
import fiftyone as fo
import fiftyone.operators as foo
from wordcloud import WordCloud
os.environ['FIFTYONE_ALLOW_LEGACY_ORCHESTRATORS'] = 'true'

dataset = fo.load_dataset("photo-album")


print("here")

# moondream_operator = foo.get_operator("@harpreetsahota/moondream2/moondream")

# moondream_operator(
#     dataset,
#     revision="2025-01-09",
#     operation="query",
#     output_field="one_word_moonbeam",
#     query_text="what is one word to describe this image?",
#     allow_delegated_execution=True,
#     default_choice_to_delegated=True,
#     delegate=True
# )

# janus_vqa = foo.get_operator("@harpreetsahota/janus_vqa/janus_vqa")
#
# janus_vqa(
#     dataset,
#     model_path="deepseek-ai/Janus-Pro-1B",
#     question="what is one word to describe this image?",
#     question_field="janus_img_q",
#     answer_field="janus_img_a",
#     delegate=True
# )

# session = fo.launch_app(dataset)
# session.wait(-1)

moonbeam_list = dataset.values("one_word_moonbeam")
janus_list = dataset.values("janus_img_a")


moonbeam_words = " ".join(moonbeam_list)
janus_words = " ".join(janus_list)

moonbeam_wordcloud = WordCloud(
    width=1920,
    height=1080,
    max_words=100,  # Limit to most frequent words to avoid overcrowding
    # min_font_size=8,  # Ensure smallest words are still readable
    # max_font_size=150,  # Allow important words to stand out
    background_color='white',
    contour_width=1,  # Subtle border
    contour_color='gray',
#    collocations=False,  # Avoid repeating word pairs
    random_state=42  # Set for reproducibility
).generate(moonbeam_words)

janus_wordcloud = WordCloud(
    width=1920,
    height=1080,
    background_color='#f7f5d0',
    max_words=100,  # Limit to most frequent words to avoid overcrowding
    min_font_size=8,  # Ensure smallest words are still readable
    max_font_size=225,  # Allow important words to stand out
    contour_width=1,  # Subtle border
    contour_color='gray',
#    collocations=False,  # Avoid repeating word pairs
    random_state=42  # Set for reproducibility
).generate(janus_words)

moonbeam_wordcloud.to_file("moonbeam_wordcloud.png")
janus_wordcloud.to_file("janus_wordcloud.png")
