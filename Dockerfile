FROM python:3.10-slim
#is the base image your container uses, slim is used here because it is smaller and faster to download/build
WORKDIR /app
#sets the working directory inside the container to /app, any commands (RUN,COPY) are relative to this folder
COPY requirements.txt .
#copies the requirements.txt from your host into /app in the container
RUN pip install --no-cache-dir -r requirements.txt
#install python packages listed in requirements.txt
#--no-cache-dir avoids caching downloaded packages, keeping the image smaller
COPY . .
#copies all project files from host to /app in the container, after packages are installed 
EXPOSE 8000
#This tells docker and other developers which port your app uses
CMD ["python3", "manage.py"]
#is the default command executed when container starts