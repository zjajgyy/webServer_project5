FROM ubuntu:16.04
FROM python:3.5.2

ADD client.py /

RUN pip install requests -i https://mirrors.ustc.edu.cn/pypi/web/simple
RUN pip install python-consul -i https://mirrors.ustc.edu.cn/pypi/web/simple

CMD ["python", "./client.py"]

