### Import necessary libraries (from pyspar)
from pyspark import SparkConf
from pyspark import SparkContext


### Create the Spark Configuration Object
conf = SparkConf()

### Set on the Spark Configuration 'YARN" as framework used to process the job
conf.setMaster('yarn')

### Set the Application Name
conf.setAppName('testing')

### Create the Spark Context based on the configuration define previously
sc = SparkContext(conf=conf)

### Run the parallization
rdd = sc.parallelize([1,2,3])

### Make the counting
count = rdd.count()

### Print the results
print(sc.master)
print(count) 