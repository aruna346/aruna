# Use an official Python runtime as a parent image
FROM python:3.8-slim
RUN pip install flask
# Set the working directory in the container
WORKDIR /testwork

 


# Copy the Python script to the container
COPY restapi.py /testwork/

 

# Run the Python script when the container launches
ENTRYPOINT ["python", "/testwork/restapi.py"]
