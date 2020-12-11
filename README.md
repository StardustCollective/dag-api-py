# DAG API

 ## Python API for connecting to a Constellation Network.

 # Getting start

 ```
 pip install DagApi==0.1.2
 ```
 
 ```python
 from DAGAPI import BlockExplorerApi as BEA

dagapi = BEA.BlockExplorer()

print(dagapi.latest_snapshot())
```
