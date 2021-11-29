from handwritten_texts.models import HandwrittenText
import os

def crawl():
    # Build Query Object containing the right Handwritten Texts
    checked = HandwrittenText.objects.filter(language="Zapotec",trptn_status="Completed and Checked")
    completed = HandwrittenText.objects.filter(language="Zapotec",trptn_status="Completed but not Checked")
    completedAndChecked = checked | completed

    # Make output folder if it doesn't exist
    os.makedirs("crawl-output", exist_ok=True)

    for object in completedAndChecked:
        handwritten_text = object.__dict__
        tichaID = handwritten_text["slug"]
        transcription = handwritten_text["transcription"]

        # Make a file for the Handwritten Text transcription
        with open(f'crawl-output/{tichaID}.txt', 'w') as f:
            f.write(transcription)

        # Get corresponding translation object if it exists
        try:
            translation = HandwrittenText.objects.get(slug=f'{tichaID}T').__dict__
            t_tichaID = translation["slug"]
            t_transcription = translation["transcription"]
            with open(f'crawl-output/{t_tichaID}.txt', 'w') as f:
                f.write(t_transcription)
        except:
            print(f"Couldn't find corresponding translation for handwritten text {tichaID}!")
