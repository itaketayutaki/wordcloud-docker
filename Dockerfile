FROM python:3.12

WORKDIR /app

RUN wget https://fonts.google.com/download?family=Noto%20Sans%20JP -O /tmp/fonts_noto.zip && \
    mkdir -p /usr/share/fonts &&\
    unzip /tmp/fonts_noto.zip -d /usr/share/fonts

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY user_dic.csv /app

RUN sudachipy ubuild -s /usr/local/lib/python3.12/site-packages/sudachidict_core/resources/system.dic user_dic.csv
RUN sed -i -e '2i "userDict" : [ "/app/user.dic" ],' /usr/local/lib/python3.12/site-packages/sudachipy/resources/sudachi.json

COPY . /app

CMD ["python", "app.py"]
