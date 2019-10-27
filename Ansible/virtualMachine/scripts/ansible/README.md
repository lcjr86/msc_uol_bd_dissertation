### Ansible testing:

https://docs.ansible.com/ansible/latest/reference_appendices/test_strategies.html

### under the Ansible host machine (MAC) the 'ansible.cfg' is:
```
/usr/local/Cellar/ansible
```

### Running Spark

1. Become root

```sudo -i```

2. Navegate to the spark folder

```cd /opt/hadoop/spark```

3. Start Spark

```spark-shell```

### Run simple spark test (count the number of non blank lines from a .txt file)

1. Navegate to the folder

```cd /home/hadoop```

2. Get a text as example

- Download the text

```wget -O alice.txt https://www.gutenberg.org/files/11/11-0.txt```

3. create a hdfs folder

```hdfs dfs -mkdir /inputs```

4. move the file to the hdfs folder

```hdfs dfs -put /opt/hadoop/alice.txt /inputs```

5. open Spark (check topic 'running Spark')

6. On Spark, run:

```var input = spark.read.textFile("/inputs/alice.txt")```

Then:

```input.filter(line => line.length()>0).count()```

The output should be something like: ```res0: Long = 2791```