FROM python:3.11-alpine

ADD *.py .

ADD DNDDICE.COM_Character_Sheet.webp . 

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p character_sheets

CMD [ "python", "./main.py" ]