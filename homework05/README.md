# Homework 5 README and ANSWERS

This is the README for the fifth homework assignment of COE 332 SP21. This includes several answers for the assignment.

## Part A

1. Include the yaml file used and the command issued to create the pod: The yaml file used is `part_one.yml`. The command issued to create the pod is `kubectl apply -f part_one.yml`. 
2. Issue a command to get the pod using an appropriate `selector`. Copy and paste the command used and the output: The command used is `kubectl get pods --selector "greeting=personalized"`. The output is the following:
```
NAME      READY   STATUS        RESTARTS   AGE
partone   1/1     Running       0          7s
```
3. Check the logs of the pod. What is the output? Is that what you expected?: The command used is `kubectl logs partone`. The output is `Hello, !`. This was expected since no value was specified for `$NAME`.
4. Delete the pod. What command did you use?: `kubectl delete pod partone`.
 
## Part B

1. Include the yaml file used and the command issued to create the pod: The yaml file used is `part_two.yml`. The command issued to create the pod is `kubectl apply -f part_two.yml`.
2. Check the logs of the pod. What is the output? Copy and paste the command used and the output: The command used is `kubectl logs parttwo`. The output is `Hello, Shawn Lee!`.
3. Delete the pod. What command did you use?: `kubectl delete pod parttwo`

## Part C

1. Include the yaml file used to create a deployment with 3 replica pods, and include the command issued to create the deployment: The yaml file used is `part_three.yml`. The command used is `kubectl apply -f part_three.yml`.
2. First, use kubectl to get all the pods in the deployment and their IP address. Copy and paste the command used and the output: The command used is `kubectl get pods -o wide`. The output is the following:
```
NAME                         READY   STATUS    RESTARTS   AGE   IP             NODE                         NOMINATED NODE   READINESS GATES
partthree-558d6f4895-28hrm   1/1     Running   0          95s   10.244.12.73   c12                          <none>           <none>
partthree-558d6f4895-hkxmm   1/1     Running   0          95s   10.244.10.74   c009.rodeo.tacc.utexas.edu   <none>           <none>
partthree-558d6f4895-jtmp5   1/1     Running   0          95s   10.244.13.75   c11                          <none>           <none>
```
3. Now, check the logs associated with each pod in the deployment. Does it match what you got in 2? Copy and paste the commands and the output: Listed below are the commands and their respective outputs:
Command: `kubectl logs partthree-558d6f4895-28hrm`, Output: `Hello, Shawn Lee from IP 10.244.12.73!`
Command: `kubectl logs partthree-558d6f4895-hkxmm`, Output: `Hello, Shawn Lee from IP 10.244.10.74!`
Command: `kubectl logs partthree-558d6f4895-jtmp5`, Output: `Hello, Shawn Lee from IP 10.244.13.75!`

The IPs mentioned in the logs match the IPs listed from 2.
