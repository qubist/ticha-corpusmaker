from vocabulary.models import Page
import os

def crawl():
    # Build Query Object containing the right Handwritten Texts
    pages = Page.objects.all()

    # Make output folder if it doesn't exist
    os.makedirs("crawl-output", exist_ok=True)

    for object in pages:
        page = object.__dict__
        letter = page["letter"]
        contents = page["contents"]

        # Make a file for the Handwritten Text transcription
        with open('crawl-output/' + letter + '.txt', 'w') as f:
            f.write(contents)
