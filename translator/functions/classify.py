from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification", model="MoritzLaurer/deberta-v3-large-zeroshot-v2.0"
)


def get_category(text: str):
    classes_verbalized = ["translate", "define"]
    prediction = classifier(
        text, classes_verbalized, hypothesis_template="{}", multi_label=False
    )
    return max(zip(prediction["labels"], prediction["scores"]), key=lambda x: x[1])[0]
