FROM python

WORKDIR /app

COPY . . 

RUN pip install -r requirment.txt

EXPOSE 3000

CMD [ "python","app.py" ]