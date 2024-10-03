FROM python:3.9
WORKDIR app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python" , "markethub/manage.py" , "runserver" , "0.0.0.0:8000"]
