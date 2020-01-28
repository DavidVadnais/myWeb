##DockerFile
#Pulling base python image from dockerhub
FROM python:3.6
# Create app directory as working directory
WORKDIR /app
# Copy code from root repo to the working directory
COPY . /app
#Run python commands to build and serve the application
RUN apt-get update && \
    apt-get install -y python3-dev && \
    apt-get install build-essential -y && \
    pip install -r requirements.txt && \
    apt-get install nginx -y
#Copying nginx conf file to nginx configuration path
COPY nginx.conf /etc/nginx
#Giving executable permission
RUN chmod 755 start.shCMD [“./start.sh”]