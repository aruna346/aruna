# Use an official Python runtime as a parent image
FROM python:3.8-slim
#FROM mysql:latest
# Install necessary packages
RUN apt-get update && apt-get install -y default-libmysqlclient-dev
# Install Flask and any other dependencies
RUN apt-get update && apt-get install -y mariadb-server default-libmysqlclient-dev

 

# Install Flask and mysql-connector-python
RUN pip install flask mysql-connector-python
# Set the working directory in the container
WORKDIR /app
ENV FLASK_APP main1.py
ENV FLASK_RUN_HOST 0.0.0.0
# Copy your Flask application code into the container
COPY main1.py /app/
COPY db_operations.py /app/
COPY config_user.json /app/
# Expose the port your Flask app will run on
EXPOSE 5000

 

# Define environment variables if needed
# ENV MY_ENV_VAR=value

 

# Run your Flask application
CMD ["flask","run"]

