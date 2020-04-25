# Minidemo
A quick flask app to demo minicloud

to run:
```
docker build -t minidemo . 
docker run -p 5000:5000 minidemo
```

to test:
```
$ curl -X PUT http://localhost:5000/world --data 'greeting=hello world'  
{"world": "hello world"}
$ curl http://localhost:5000/world
"hello world"
```