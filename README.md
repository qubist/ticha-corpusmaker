ticha-corpusmaker

Make a searchable plaintext corpus of Colonial Valley Zapotec from Ticha transcriptions

# Background

This project is part of my final project for Linguistics 215: Structure of Colonial Valley Zapotec.

More about Ticha: https://ticha.haverford.edu/en/about/

Read the full paper associated with this code and data: FIXME

# Documentation

## crawler.py

How to use the crawler to download raw Handwritten Text transcriptions from Ticha:

1. Uplodad this file to the server at:
   ticha.haverford.edu:/srv/ticha-django-site
2. On the server, run
   `$ source /usr/local/lib/python-virtualenv/ticha-django/bin/activate`
   to activate the virtual environment
3. Run `$ python manage.py shell` to start the shell inside the project
4. Run `>>> import crawler` to import this code
5. Run `>>> crawler.crawl()`
6. Exit and check the `crawl-output` folder for your output
7. Move the `crawl-output` folder to your home directory on the server:
   `$ cp -r crawl-output ~/`
8. (Clean up after yourself: `$ rm -r crawler.py crawl-output`)
9. From your computer, remote copy the output: `$ scp -r username@ticha.haverford.edu:~/crawl-output .`

## cleaner.py

How to use the cleaner to clean raw Handwritten Text transcriptions:

1. Run `$ python3 cleaner.py /path/to/crawl-output`, replacing the path as appropriate.

* A new folder named `clean-output` will be created with cleaned files in it.
* You can change the code to remove more or less extra information from the files.
* If you run the cleaner again, the files in the `clean-output` folder will be overwritten.

# Searching the corpus

Words in the corpus are not spelled consistently. This is because of inconsistencies in the CVZ writing system, as well as in Ticha's transcription.

Inconsistent spelling makes searching hard. Here are some strategies.

## Search in the Spanish translations

The corpus includes Spanish translations of the Zapotec documents. Most documents have translations. The Spanish spelling and transcription is much more regular than the Zapotec, so searches for words of interest in Spanish can be performed, and the corresponding Zapotec words can be found after.

* Spanish used in the translations is not modern, so although spelling is consistent, it might not be what you expect.

* To help find the corresponding Zapotec for a word in the Spanish translation, you can use names—which are usually written the same way in both texts—to orient yourself.

## Using regexes

Use regular expressions to search across know spelling variations

Maguey `ma[gq]((uey)|(ei))`

## Common spelling/transcription variation

### In Zapotec

Consonants are sometimes doubled: `toba` -> `ttoba`

Vowels are often doubled

### In Spanish

`b` sometimes appears as `v` or `u`

`s` and `z` are interchangeable

`v` and `b` sometimes interchangeable

## Searching across lines

Sometimes words are split across lines so watch out for that.


# License

Code in `cleaner.py` and `crawler.py` is licensed under the [MIT](LICENSE) license. Contents of the `corpus` directory are property of [Ticha](https://ticha.haverford.edu) and license information can be found there.
