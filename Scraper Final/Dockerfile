FROM python:3.8

ADD scraper.py .
ADD parser.py .

RUN pip install requests pandas pymongo redis pickle5 bs4 subprocess.run

CMD [ "python", "./scraper.py" ]