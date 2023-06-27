FROM python:3.11-slim

WORKDIR /code

# install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


# copy project
COPY . /code/

# Expose the port the app runs on
EXPOSE 8000

# Start the application
#CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]