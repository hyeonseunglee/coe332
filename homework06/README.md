# Homework 6 README

This is the README for the 6th homework assignment of COE 332 SP21. 
## Files that were created for this assignment

1. `hslee21-test-redis-PVC.yml `
2. `hslee21-test-redis-deployment.yml `
3. `hslee21-test-redis-service.yml `
4. `hslee21-test-flask-deployment.yml`
5. `hslee21-test-flask-service.yml`

## Image for this assignment

1. We are using the homework03 image `hyeonseunglee/hw3`.
 
## Step 1: Persistent Volume Claim

1. Run `kubectl apply -f hslee21-test-redis-PVC.yml`
2. Output is `persistentvolumeclaim/hslee21-pvc created`
3. Run `kubectl get pvc`
4. Output is
```
NAME          STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
hslee21-pvc   Bound    pvc-f8d28cbd-ad86-4f5e-99b7-6c2ffc4d0fca   1Gi        RWO            rbd            19s
```

## Step 2: Redis DB Deployment

1. Run `kubectl apply -f hslee21-test-redis-deployment.yml`
2. Output is `deployment.apps/hslee21-pvc-deployment created`
3. Run `kubectl get deployments`
4. Output is
```
NAME                     READY   UP-TO-DATE   AVAILABLE   AGE
hslee21-pvc-deployment   1/1     1            1           98s
``` 

## Step 3: Redis DB Service

1. Run `kubectl apply -f hslee21-test-redis-service.yml`
2. Output is `service/hslee21-test-redis created`
3. Run `kubectl get services`
4. Output is 
```
NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
hslee21-test-redis   ClusterIP   10.103.217.46   <none>        6379/TCP         62s
```

## Step 4: Flask Deployment

1. Run `kubectl apply -f hslee21-test-flask-deployment.yml`
2. Output is `deployment.apps/hslee21-flask-deployment created`
3. Run `kubectl get deployments`
4. Output is
```
NAME                       READY   UP-TO-DATE   AVAILABLE   AGE
hslee21-flask-deployment   2/2     2            0           55s
hslee21-pvc-deployment     1/1     1            1           11m
```

## Step 5: Flask Service

1. Run `kubectl apply -f hslee21-test-flask-service.yml`
2. Output is `service/hslee21-test-flask created`
3. Run `kubectl get services`
4. Output is
```
NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
hslee21-test-flask   ClusterIP   10.107.138.36   <none>        5000/TCP         43s
hslee21-test-redis   ClusterIP   10.103.217.46   <none>        6379/TCP         10m
```
