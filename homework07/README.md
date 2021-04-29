# Homework 7 README

This is the README for the 7th homework assignment of COE 332 SP21. 

## Section A Part 1: Building an image: run the following codes

1. `docker build -t hyeonseunglee/flask-hw7 .`
2. `docker push hyeonseunglee/flask-hw7`

## Deploy test redis environment

1. `kubectl apply -f hslee21-test-redis-PVC.yml`
2. `kubectl apply -f hslee21-test-redis-deployment.yml`
3. `kubectl apply -f hslee21-test-redis-service.yml`
4. `kubectl get service`: Output looks like this
```
NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
hslee21-test-redis   ClusterIP   10.111.94.157   <none>        6379/TCP         2d
```
5. Copy and paste in the `CLUTER-IP` address for hslee21-test-redis into both `hslee21-hw7-worker-deployment.yml` and `hslee21-hw7-flask-deployment.yml`
```
 env:
          - name: REDIS_IP
            value: 10.111.94.157
``` 

## Section A Part 2: Deploy worker and flask

1. `kubectl apply -f hslee21-hw7-worker-deployment.yml`
2. `kubectl apply -f hslee21-hw7-flask-deployment.yml`
3. `kubectl get pods -o wide`: Output looks like this
```
NAME                                            READY   STATUS    RESTARTS   AGE   IP              NODE                         NOMINATED NODE   READINESS GATES
hslee21-hw7-flask-deployment-6dfcfd8495-4wt9t   1/1     Running   0          19m   10.244.13.234   c11                          <none>           <none>
hslee21-hw7-worker-555c968985-fbg5d             1/1     Running   0          19m   10.244.12.34    c12                          <none>           <none>
hslee21-hw7-worker-555c968985-fz6w4             1/1     Running   0          18m   10.244.13.235   c11                          <none>           <none>
hslee21-pvc-deployment-779fdb55f7-j6xwb         1/1     Running   0          10h   10.244.12.9     c12                          <none>           <none>
```
Remember the flask pod IP address.

## Section A Part 3: Deploy and enter the debug container

1. `kubectl apply -f deployment-python-debug.yml`
2. Run `kubectl get pods` and copy the name of the debug pod
3. `kubectl exec -it py-debug-deployment-5cc8cdd65f-hnw6v -- /bin/bash`, except paste in the name of the pod in place of the placeholder name I have in this code.

## Section A Part 3a

1. curl statement: `curl -X POST -H "content-type: application/json" -d '{"start": "1", "end
":"2"}' 10.244.13.234:5000/jobs`
2. Output: `{"id": "ec411060-8ae0-4d6e-b643-8722c152c05f", "status": "submitted", "start": "1", "end": "2"}`

## Section A Part 3b

1. Python Statements:
```
root@py-debug-deployment-5cc8cdd65f-hnw6v:/# python3
Python 3.9.2 (default, Feb 19 2021, 17:11:58)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import redis
>>> import hotqueue
>>> rd =redis.StrictRedis(host='10.111.94.157',port=6379,db=0)
>>> rd.hgetall('job.ec411060-8ae0-4d6e-b643-8722c152c05f')
```
2. Output: `{b'id': b'ec411060-8ae0-4d6e-b643-8722c152c05f', b'status': b'complete', b'start': b'1', b'end': b'2'}`
 
## Section B Part 2

`add_worker_IP` is added to `jobs.py` and `worker.py` is also updated accordingly.

## Section C Part 1

```
root@py-debug-deployment-5cc8cdd65f-hnw6v:/# curl -X POST -H "content-type: application/js3" -d '{"start": "11", "end":"12"}' 10.244.10.82:5000/jobs
{"id": "79f37c1d-bd2b-4dcb-992c-ac46073ce133", "status": "submitted", "start": "11", "end": "12"}
root@py-debug-deployment-5cc8cdd65f-hnw6v:/# curl -X POST -H "content-type: application/js3" -d '{"start": "13", "end
":"14"}' 10.244.10.82:5000/jobs
{"id": "8028a805-d8a2-49ac-b0dd-626ea7827e15", "status": "submitted", "start": "13", "end": "14"}
root@py-debug-deployment-5cc8cdd65f-hnw6v:/# curl -X POST -H "content-type: application/js3" -d '{"start": "15", "end
":"16"}' 10.244.10.82:5000/jobs
{"id": "bb438587-68cf-431c-8adb-dfe75cfd62e2", "status": "submitted", "start": "15", "end": "16"}
root@py-debug-deployment-5cc8cdd65f-hnw6v:/# curl -X POST -H "content-type: application/js3" -d '{"start": "17", "end
":"18"}' 10.244.10.82:5000/jobs
{"id": "edff07a5-b03b-4f65-b33f-d83ce868c493", "status": "submitted", "start": "17", "end": "18"}
root@py-debug-deployment-5cc8cdd65f-hnw6v:/# curl -X POST -H "content-type: application/js3" -d '{"start": "19", "end
":"20"}' 10.244.10.82:5000/jobs
{"id": "b8996ed4-e55a-4452-b9c2-f315ea530db4", "status": "submitted", "start": "19", "end": "20"}
root@py-debug-deployment-5cc8cdd65f-hnw6v:/# curl -X POST -H "content-type: application/js3" -d '{"start": "21", "end
":"22"}' 10.244.10.82:5000/jobs
{"id": "8e74a592-8c35-41f5-875b-03742f3b23df", "status": "submitted", "start": "21", "end": "22"}
root@py-debug-deployment-5cc8cdd65f-hnw6v:/# curl -X POST -H "content-type: application/js3" -d '{"start": "23", "end
":"24"}' 10.244.10.82:5000/jobs
{"id": "9f481b69-1821-442c-82da-45de07e8f018", "status": "submitted", "start": "23", "end": "24"}
root@py-debug-deployment-5cc8cdd65f-hnw6v:/# curl -X POST -H "content-type: application/js3" -d '{"start": "25", "end
":"26"}' 10.244.10.82:5000/jobs
{"id": "9987dcae-a6a1-406d-b2fc-d7c01748f7ef", "status": "submitted", "start": "25", "end": "26"}
root@py-debug-deployment-5cc8cdd65f-hnw6v:/# curl -X POST -H "content-type: application/js3" -d '{"start": "27", "end
":"28"}' 10.244.10.82:5000/jobs
{"id": "17cd2b00-7297-4a85-aaf6-17f8194ee8e9", "status": "submitted", "start": "27", "end": "28"}
root@py-debug-deployment-5cc8cdd65f-hnw6v:/# curl -X POST -H "content-type: application/js3" -d '{"start": "29", "end
":"30"}' 10.244.10.82:5000/jobs
{"id": "a4f21a23-4511-4b30-8569-c31195c13cbe", "status": "submitted", "start": "29", "end": "30"}
```

## Section C Part 2
```
root@py-debug-deployment-5cc8cdd65f-hnw6v:/# python3
Python 3.9.2 (default, Feb 19 2021, 17:11:58)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import redis
>>> import hotqueue
>>> rd =redis.StrictRedis(host='10.111.94.157',port=6379,db=0)
>>> rd.hgetall('job.79f37c1d-bd2b-4dcb-992c-ac46073ce133')
{b'id': b'79f37c1d-bd2b-4dcb-992c-ac46073ce133', b'status': b'complete', b'start': b'11', b'end': b'12', b'worker': b'10.244.13.237'}
>>> rd.hgetall('job.8028a805-d8a2-49ac-b0dd-626ea7827e15')
{b'id': b'8028a805-d8a2-49ac-b0dd-626ea7827e15', b'status': b'complete', b'start': b'13', b'end': b'14', b'worker': b'10.244.10.83'}
>>> rd.hgetall('job.bb438587-68cf-431c-8adb-dfe75cfd62e2')
{b'id': b'bb438587-68cf-431c-8adb-dfe75cfd62e2', b'status': b'complete', b'start': b'15', b'end': b'16', b'worker': b'10.244.13.237'}
>>> rd.hgetall('job.edff07a5-b03b-4f65-b33f-d83ce868c493')
{b'id': b'edff07a5-b03b-4f65-b33f-d83ce868c493', b'status': b'complete', b'start': b'17', b'end': b'18', b'worker': b'10.244.10.83'}
>>> rd.hgetall('job.b8996ed4-e55a-4452-b9c2-f315ea530db4')
{b'id': b'b8996ed4-e55a-4452-b9c2-f315ea530db4', b'status': b'complete', b'start': b'19', b'end': b'20', b'worker': b'10.244.13.237'}
>>> rd.hgetall('job.8e74a592-8c35-41f5-875b-03742f3b23df')
{b'id': b'8e74a592-8c35-41f5-875b-03742f3b23df', b'status': b'complete', b'start': b'21', b'end': b'22', b'worker': b'10.244.10.83'}
>>> rd.hgetall('job.9f481b69-1821-442c-82da-45de07e8f018')
{b'id': b'9f481b69-1821-442c-82da-45de07e8f018', b'status': b'complete', b'start': b'23', b'end': b'24', b'worker': b'10.244.13.237'}
>>> rd.hgetall('job.9987dcae-a6a1-406d-b2fc-d7c01748f7ef')
{b'id': b'9987dcae-a6a1-406d-b2fc-d7c01748f7ef', b'status': b'complete', b'start': b'25', b'end': b'26', b'worker': b'10.244.10.83'}
>>> rd.hgetall('job.17cd2b00-7297-4a85-aaf6-17f8194ee8e9')
{b'id': b'17cd2b00-7297-4a85-aaf6-17f8194ee8e9', b'status': b'complete', b'start': b'27', b'end': b'28', b'worker': b'10.244.13.237'}
>>> rd.hgetall('job.a4f21a23-4511-4b30-8569-c31195c13cbe')
{b'id': b'a4f21a23-4511-4b30-8569-c31195c13cbe', b'status': b'complete', b'start': b'29', b'end': b'30', b'worker': b'10.244.10.83'}
```

## Section C Part 3

Five jobs done by worker `10.244.10.83`, and five jobs done by worker `10.244.13.237`

