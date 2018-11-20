# Bears App

Simple web app that classifies images with bears.

## Getting Started

Clone the repo
```
git clone https://github.com/adai183/bears_app_flask.git
cd bears_app_flask
```

Build docker image
```
docker build -t bears_app_flask .
```

Run your new docker build locally
```
docker run -d -p 5000:5000 bears_app_flask
```

Test the Api via curl with this command
```
curl -X POST -F image=@example.png 'http://localhost:5000/predict'
```

