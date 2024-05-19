## When you are done building the image using the above code.

docker build --t pythonflask .

to run a docker container run the following command.

docker run -d -e CLIENT=Name-Of-A-Client -p PORT:5000 docker-image
