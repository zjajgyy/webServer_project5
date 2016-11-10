FROM ubuntu:16.04
FROM python:3.5.2

ADD service.py /
ADD sqlite.db /

RUN pip install flask -i https://mirrors.ustc.edu.cn/pypi/web/simple
RUN pip install python-consul -i https://mirrors.ustc.edu.cn/pypi/web/simple

#EXPOSE 8080

CMD ["python", "./service.py"]

