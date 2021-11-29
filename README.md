How to use this crawler to download raw Handwritten Text transcriptions from Ticha:

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
