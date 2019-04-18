FROM python:3

COPY requirement.txt /
COPY Voting /
#COPY Model_Load.py /
COPY app.py /

RUN pip install -r requirement.txt

#CMD ["python", "PickleFile_Download_local.py"]
CMD ["python", "app.py"]