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

# How to use this crawler to download Handwritten Text transcriptions raw:
#
# 1. Uplodad this file to the server at:
#    ticha.haverford.edu:/srv/ticha-django-site
# 2. On the server, run
#    `$ source /usr/local/lib/python-virtualenv/ticha-django/bin/activate`
#    to activate the virtual environment
# 3. Run `$ python manage.py shell` to start the shell inside the project
# 4. Run `>>> import crawler` to import this code
# 5. Run `>>> crawler.crawl()`
# 6. Exit and check the `crawl-output` folder for your output
# 7. Move the `crawl-output` folder to your home directory on the server:
#    `$ cp -r crawl-output ~/`
# 8. (Clean up after yourself: `$ rm -r crawler.py crawl-output`)
# 9. From your computer, remote copy the output: `$ scp -r username@ticha.haverford.edu:~/crawl-output .`
