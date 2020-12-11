import requests

class BlockExplorer (object):

        REST_API_URL = 'https://block-explorer.constellationnetwork.io'

        #Snapshot chapter

        def latest_snapshot(self):

            '''Get latest (the highest) snapshot

            {
            "hash": "1ae6e0f9161b7a29c96e8accb853fb479e0ea026832850ff5def773b5ff00c00",
            "height": 58186,
            "checkpointBlocks": [
                "0922bd4a63353040589547cfed00f2660fb736ce694199384f1df2adaac54fe6",
                "0c27a295e1f58e41582538b8deb18a3aea4ae4b52b7e53c529ed80c03eaaeed1"
            ],
            "timestamp": "2020-05-12T10:16:14Z"
            }
            '''
            url = self.REST_API_URL + '/snapshot/latest'
            response = requests.get(url)
            return response.headers, response.content

        def snapshot(self, parameter):

            '''Get snapshot by hash
            {
            "hash": "1ae6e0f9161b7a29c96e8accb853fb479e0ea026832850ff5def773b5ff00c00",
            "height": 58186,
            "checkpointBlocks": [
                "0922bd4a63353040589547cfed00f2660fb736ce694199384f1df2adaac54fe6",
                "0c27a295e1f58e41582538b8deb18a3aea4ae4b52b7e53c529ed80c03eaaeed1"
            ],
            "timestamp": "2020-05-12T10:16:14Z"
            }
            '''
            if parameter.isdigit():
                print ('Snapshot by height')
            else:
                print ('Snapshot by hash')

            url = self.REST_API_URL + '/snapshot/' + parameter
            response = requests.get(url)
            return response.headers, response.content
           
        #Checkpoint block

        def checkpoint_block_hash (self, hash):

            '''Get checkpoint block by hash

            {
            "hash": "0923bd4a633f3040589547cfed00f2660fb736ce694199384f1df2adaac54fe6",
            "height": {
                "min": 58187,
                "max": 198640
            },
            "transactions": [
                "adf1ba091a15a2dbj930a7245b36f8abbef7d9eaf0147466bc6069a3eacc4ef6",
                "2fd12a358a59q6ee0f59687126ff7a984f993fa8002614169085348477ba5ba0"
            ],
            "notifications": [
                "6ec1ba091315a2dg2930472a5bdaf8aebe77d9eaf0147466bc6069a3eacc4ef6"
            ],
            "observations": [
                "e9g1ba091215a25b2930472a5bd6f8abbef7d9eaf0147466bc6069a3eacc4efa"
            ],
            "children": 2,
            "snapshotHash": "1ae6e0f9161b7a29c96e8accb853fb479e0ea026832850ff5def773b5ff00c00",
            "timestamp": "2020-05-12T10:16:14Z"
            }
            '''
            url = self.REST_API_URL + '/checkpoint-block/' + hash
            response = requests.get(url)
            return response.headers, response.content


        #Transaction

        def transaction (self, hash):

            '''Get transaction by hash

            {
            "hash": "6ec1ba091915f2db2930472a5bd6f8abbef7d9eaf0147466bc6069a3eacc4ef6",
            "amount": 0,
            "receiver": "DAG2ERrUzev7LoZcs8xeiVqLFQcVXSmEmg5cZ9wW",
            "sender": "DAG2V3L7efRpk16UGcPHLcqLJthzWxpMoPR3vToD",
            "fee": 0,
            "isDummy": true,
            "lastTransactionRef": {
                "prevHash": "",
                "ordinal": 0
            },
            "snapshotHash": "1ee6e0f9161b7a29c96e8accb853fb479e0ea026832850ff5def773b5ff00c00",
            "checkpointBlock": "0923bd4a63353040589547cfed00f2660fb736ce694199384f1df2adaac54fe6",
            "timestamp": "2020-05-12T10:16:14Z",
            "transactionOriginal": null
            }
            '''
            url = self.REST_API_URL + '/transaction/' + hash
            response = requests.get(url)
            return response.headers, response.content

        def latest_transaction(self, limit = '', search_after = ''):

            '''Get transactions from the latest snapshot

            Int limit - Limit (size) of the response items
            String search_after - ISOString to search after given timestamp

            [
            {
                "hash": "6ec1ba091915f2db2930472a5bd6f8abbef7d9eaf0147466bc6069a3eacc4ef6",
                "amount": 0,
                "receiver": "DAG2ERrUzev7LoZcs8xeiVqLFQcVXSmEmg5cZ9wW",
                "sender": "DAG2V3L7efRpk16UGcPHLcqLJthzWxpMoPR3vToD",
                "fee": 0,
                "isDummy": true,
                "lastTransactionRef": {
                "prevHash": "",
                "ordinal": 0
                },
                "snapshotHash": "1ee6e0f9161b7a29c96e8accb853fb479e0ea026832850ff5def773b5ff00c00",
                "checkpointBlock": "0923bd4a63353040589547cfed00f2660fb736ce694199384f1df2adaac54fe6",
                "timestamp": "2020-05-12T10:16:14Z",
                "transactionOriginal": null
            }
            ]
            '''
            
            parameters = {'limit': limit, 'search_after': search_after}
            
            url = self.REST_API_URL + '/snapshot/latest/transaction'
            response = requests.get(url, params=parameters)
            print (response.url)
            return response.headers, response.content

        def transactions_from_snapshot (self, parameter, limit = '', search_after = ''):

            '''Get transactions for the given snapshot
            
            Int limit - Limit (size) of the response items
            String search_after - ISOString to search after given timestamp

            [
            {
                "hash": "6ec1ba091915f2db2930472a5bd6f8abbef7d9eaf0147466bc6069a3eacc4ef6",
                "amount": 0,
                "receiver": "DAG2ERrUzev7LoZcs8xeiVqLFQcVXSmEmg5cZ9wW",
                "sender": "DAG2V3L7efRpk16UGcPHLcqLJthzWxpMoPR3vToD",
                "fee": 0,
                "isDummy": true,
                "lastTransactionRef": {
                "prevHash": "",
                "ordinal": 0
                },
                "snapshotHash": "1ee6e0f9161b7a29c96e8accb853fb479e0ea026832850ff5def773b5ff00c00",
                "checkpointBlock": "0923bd4a63353040589547cfed00f2660fb736ce694199384f1df2adaac54fe6",
                "timestamp": "2020-05-12T10:16:14Z",
                "transactionOriginal": null
            }
            ]
            '''

            if parameter.isdigit():
                print ('Snapshot by height')
            else:
                print ('Snapshot by hash')

            parameters = {'limit': limit, 'search_after': search_after}
            
            url = self.REST_API_URL + '/snapshot/' + parameter + '/transaction'
            response = requests.get(url, params=parameters)
            print (response.url)
            return response.headers, response.content

        def transactions_from_wallet (self, address, limit = '', search_after = ''):
            
            '''Get transactions for the given address

            Int limit - Limit (size) of the response items
            String search_after - ISOString to search after given timestamp

            [
            {
                "hash": "6ec1ba091915f2db2930472a5bd6f8abbef7d9eaf0147466bc6069a3eacc4ef6",
                "amount": 0,
                "receiver": "DAG2ERrUzev7LoZcs8xeiVqLFQcVXSmEmg5cZ9wW",
                "sender": "DAG2V3L7efRpk16UGcPHLcqLJthzWxpMoPR3vToD",
                "fee": 0,
                "isDummy": true,
                "lastTransactionRef": {
                "prevHash": "",
                "ordinal": 0
                },
                "snapshotHash": "1ee6e0f9161b7a29c96e8accb853fb479e0ea026832850ff5def773b5ff00c00",
                "checkpointBlock": "0923bd4a63353040589547cfed00f2660fb736ce694199384f1df2adaac54fe6",
                "timestamp": "2020-05-12T10:16:14Z",
                "transactionOriginal": null
            }
            ]
            '''

            parameters = {'limit': limit, 'search_after': search_after}

            url = self.REST_API_URL + '/snapshot/' + address + '/transaction'
            response = requests.get(url, params=parameters)
            return response.headers, response.content

        def sent_transactions (self, address, limit = '', search_after = ''):

            '''Get sent transactions by the given address

            Int limit - Limit (size) of the response items
            String search_after - ISOString to search after given timestamp

            [
            {
                "hash": "6ec1ba091915f2db2930472a5bd6f8abbef7d9eaf0147466bc6069a3eacc4ef6",
                "amount": 0,
                "receiver": "DAG2ERrUzev7LoZcs8xeiVqLFQcVXSmEmg5cZ9wW",
                "sender": "DAG2V3L7efRpk16UGcPHLcqLJthzWxpMoPR3vToD",
                "fee": 0,
                "isDummy": true,
                "lastTransactionRef": {
                "prevHash": "",
                "ordinal": 0
                },
                "snapshotHash": "1ee6e0f9161b7a29c96e8accb853fb479e0ea026832850ff5def773b5ff00c00",
                "checkpointBlock": "0923bd4a63353040589547cfed00f2660fb736ce694199384f1df2adaac54fe6",
                "timestamp": "2020-05-12T10:16:14Z",
                "transactionOriginal": null
            }
            ]
            '''

            parameters = {'limit': limit, 'search_after': search_after}

            url = self.REST_API_URL + '/snapshot/' + address + '/transaction/sent'
            response = requests.get(url, params=parameters)
            return response.headers, response.content

        def received_transactions (self, address, limit = '', search_after = ''):

            '''Get received transactions by the given address

            Int limit - Limit (size) of the response items
            String search_after - ISOString to search after given timestamp

            [
            {
                "hash": "6ec1ba091915f2db2930472a5bd6f8abbef7d9eaf0147466bc6069a3eacc4ef6",
                "amount": 0,
                "receiver": "DAG2ERrUzev7LoZcs8xeiVqLFQcVXSmEmg5cZ9wW",
                "sender": "DAG2V3L7efRpk16UGcPHLcqLJthzWxpMoPR3vToD",
                "fee": 0,
                "isDummy": true,
                "lastTransactionRef": {
                "prevHash": "",
                "ordinal": 0
                },
                "snapshotHash": "1ee6e0f9161b7a29c96e8accb853fb479e0ea026832850ff5def773b5ff00c00",
                "checkpointBlock": "0923bd4a63353040589547cfed00f2660fb736ce694199384f1df2adaac54fe6",
                "timestamp": "2020-05-12T10:16:14Z",
                "transactionOriginal": null
            }
            ]
            '''

            parameters = {'limit': limit, 'search_after': search_after}

            url = self.REST_API_URL + '/snapshot/' + address + '/transaction/received'
            response = requests.get(url, params=parameters)
            return response.headers, response.content


if __name__ == "__main__":
    Check = BlockExplorer()
    print(Check.latest_transaction())