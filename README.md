ticha-corpusmaker

Make a searchable plaintext corpus from Ticha transcriptions

# Background

This project is part of my final project for Linguistics 215: Structure of Colonial Valley Zapotec.

More about Ticha: https://ticha.haverford.edu/en/about/

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

# License

[MIT](LICENSE)
