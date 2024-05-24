from osdu.client import SimpleOsduClient
import os
import json

data_partition = 'osdu'
token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ0VU1zaWJLalA0YmxfeTNmcWdFT251NllhR0VWdy1oWmxwZWJOY0VGZEs0In0.eyJleHAiOjE3MTY1NDI3NzksImlhdCI6MTcxNjUzOTE3OSwianRpIjoiYzMwYTExMWMtYWY5ZS00NjJmLWFiMzQtZDU1ZDM0NGM3NjQ4IiwiaXNzIjoiaHR0cDovL2tleWNsb2FrLmxvY2FsaG9zdC9yZWFsbXMvb3NkdSIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiIyMDJkNThhOS03MDQ2LTRjMTUtOGFmMy02OWE0ZGFjMjlkMjAiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJvc2R1LWFkbWluIiwic2Vzc2lvbl9zdGF0ZSI6ImI5YjAzNmNmLTA1MWItNDA1MC1hYTNhLWNjZTk1MjY3ZWNkMSIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJkZWZhdWx0LXJvbGVzLW9zZHUiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7Im9zZHUtYWRtaW4iOnsicm9sZXMiOlsidW1hX3Byb3RlY3Rpb24iXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoicHJvZmlsZSBlbWFpbCIsInNpZCI6ImI5YjAzNmNmLTA1MWItNDA1MC1hYTNhLWNjZTk1MjY3ZWNkMSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiY2xpZW50SG9zdCI6IjEwLjEuMzYuNjAiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJzZXJ2aWNlLWFjY291bnQtb3NkdS1hZG1pbiIsImNsaWVudEFkZHJlc3MiOiIxMC4xLjM2LjYwIiwiY2xpZW50X2lkIjoib3NkdS1hZG1pbiIsImVtYWlsIjoib3NkdS1hZG1pbkBzZXJ2aWNlLmxvY2FsIn0.icHPcueyNDM7aei9HQnRkgKnazcVw2kHWRKOMfjDOHGeDRrO7Wv3ml4kI7jsR8LobJ4oVx329qvu4g2uda-k-tcbuRGxmKLyNlMl2zzDnN_3I6dnDww6CCD1y44mJb_cOwKw4j8IKOAoHrZy_rCgAnv_ymEUeoHJWI8M7w2iwEfogI1kQYg3iLCYYa72cRFp7BhX3o-SfGfZC1oHDmObRWxiOELoXhsZC4l4jvwpZl9ZNPznR6QJx5gEi8M0hPC7kQ4CsJkv_7fviC602wdt6Bjo1_WndwuXtLzBSVS3p3gv4MJ-dJqr4helueccCX2PSV3d7H089Afb2J_P45afQQ'

# With env var `OSDU_API_URL` set in current environment.
#os.environ['OSDU_API_URL'] = 'https://osdu.petrosys.com.au'
os.environ['OSDU_API_URL'] = 'http://osdu.localhost'
osdu_client = SimpleOsduClient(data_partition, token)


query = {
    "kind": f"osdu:wks:*:*"
}


#result = osdu_client.schema.get_all_schemas()

#print(result)

sequence = {}
with open('../schema/ReferenceValues/Manifests/reference-data/IngestionSequence.json') as seqf:
    sequence = json.loads(seqf.read())
    
replacements = {
    'NAMESPACE': 'osdu',
    'DATA_OWNERS_GROUP' : 'data.default.owners@osdu.group',
    'DATA_VIEWERS_GROUP' : 'data.default.viewers@osdu.group',
    'LEGAL_TAG': 'osdu-ps-default',
    'ISO_3166_ALPHA_2_CODE': 'US'
}


for sch in sequence:
    with open('../schema/' + sch['FileName']) as refFile:
        refFileText = refFile.read()
        
        for key in replacements:
            refFileText = refFileText.replace('{{' + key + '}}', replacements[key])
    
        print('*****************')
        print(json.dumps(sch, indent=2))
        result = osdu_client.workflow.osdu_ingest(json.loads(refFileText))
        print('-- Response --')
        print(json.dumps(result, indent=2))
        print('*****************')
        print('')
    exit

#result = osdu_client.schema.get_all_schemas()

#print(result)
