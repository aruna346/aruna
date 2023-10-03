# Use an official Python runtime as a parent image
FROM python:3.8-slim
#RUN pip install pyats
RUN pip install pyats[full]
RUN apt-get update && apt-get install -y openssh-client

 

# Set the working directory in the container
WORKDIR /pyats

 

# Copy the Python script to the container
COPY sample_pyats.py /pyats/
COPY my_yaml.yaml /pyats/
# Run the Python script when the container launches
ENTRYPOINT ["python", "/pyats/sample_pyats.py"]

 
