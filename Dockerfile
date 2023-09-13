FROM python:3.8-slim
ENV FLASK_APP restapi.py
# Set the working directory in the container
WORKDIR /testwork

# Copy the current directory contents into the container at /getapi
COPY restapi.py /testwork
COPY config_users.json /testwork
# Install Flask and any other dependencies
RUN pip install Flask

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the Flask app when the container launches
CMD ["flask", "run", "--host", "0.0.0.0"]
