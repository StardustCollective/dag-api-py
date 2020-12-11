from DAGAPI import BlockExplorerApi as BEA

dagapi = BEA.BlockExplorer()

print(dagapi.latest_snapshot())
