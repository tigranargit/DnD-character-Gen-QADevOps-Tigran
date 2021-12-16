#Use Python 3.6 as a base image
FROM python:3.6
# Copy contents into image
COPY . .
# install pip dependencies from requirements file
RUN pip install -r requirements.txt
# state the environment variables

ENV MYSQL_USER=tigran@dnd-database
ENV MYSQL_PWD=QAproject21
ENV MYSQL_IP=dnd-database.mysql.database.azure.com
ENV MYSQL_DB=dnd-database
ENV MYSQL_SK=sdlkfjsdfkj

# Expose correct port
EXPOSE 5000
# Create an entrypoint
ENTRYPOINT ["python", "app.py" ]