apiVersion: "sparkoperator.k8s.io/v1beta2"
kind: SparkApplication
metadata:
 name: spark-pi
 namespace: spark-jobs
spec:
 type: Scala
 mode: cluster
 image: "registry.cn-hangzhou.aliyuncs.com/public-namespace/spark:v3.1.1"
 imagePullPolicy: Always
 mainClass: org.apache.spark.examples.SparkPi
 mainApplicationFile: "local:///opt/spark/examples/jars/spark-examples_2.12-3.1.1.jar"
 sparkVersion: "3.1.1"
 restartPolicy:
   type: Never
 driver:
   cores: 1
   coreLimit: "1200m"
   memory: "512m"
   labels:
     version: 3.1.1
   serviceAccount: spark
   affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: kubernetes.io/hostname
            operator: In
            values:
            - sttc-gpu-01

 executor:
   cores: 1
   instances: 1
   memory: "512m"
   labels:
     version: 3.1.1
   affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: kubernetes.io/hostname
            operator: In
            values:
            - sttc-gpu-01
