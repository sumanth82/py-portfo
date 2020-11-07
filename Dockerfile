FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_ENV=development 
ENV FLASK_APP=portfolio.py

EXPOSE 5000/tcp

#CMD [ "python", "./portfolio.py" ]

CMD [ "flask", "run", "--host=0.0.0.0" ]

