from osdu.client import SimpleOsduClient
import os
import json

data_partition = 'osdu'
token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJuRmV4RVRjMmp0WFltenlqanF6VEdYdzNGdVBsNTk0LUd0aUxpanhvR3pvIn0.eyJleHAiOjE3MTU4Mjg2MDcsImlhdCI6MTcxNTgyNTAwNywianRpIjoiMzA5YTNmZDgtYzhlNS00NDE1LWIxNGItOWIwNWQ0MDcwNTY5IiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay5wZXRyb3N5cy5jb20uYXUvcmVhbG1zL29zZHUiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiMjdlY2IzNTgtZTIwMy00Y2IyLWI4YzMtMDM3ZmQwNzg3NGZiIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoib3NkdS1hZG1pbiIsInNlc3Npb25fc3RhdGUiOiJmZDQwYTIzOS1lN2Q3LTQ0YTEtYjExMC0wMDMwMDQ0OWRiNDAiLCJhY3IiOiIxIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwiZGVmYXVsdC1yb2xlcy1vc2R1IiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJvc2R1LWFkbWluIjp7InJvbGVzIjpbInVtYV9wcm90ZWN0aW9uIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJzaWQiOiJmZDQwYTIzOS1lN2Q3LTQ0YTEtYjExMC0wMDMwMDQ0OWRiNDAiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImNsaWVudEhvc3QiOiIxMC4yNDQuMi4wIiwicHJlZmVycmVkX3VzZXJuYW1lIjoic2VydmljZS1hY2NvdW50LW9zZHUtYWRtaW4iLCJjbGllbnRBZGRyZXNzIjoiMTAuMjQ0LjIuMCIsImVtYWlsIjoib3NkdS1hZG1pbkBzZXJ2aWNlLmxvY2FsIiwiY2xpZW50X2lkIjoib3NkdS1hZG1pbiJ9.AVYI04eHYkeIeNgGhPqcT_DUp2-UE3WdBTbhMdxL4hVuRCE1hp7el4bdC19NNE5Nee1kyLovV1Jaj_Jw9d7gmaIZX0GcUSzfcq6dlVYD_ZhJUH8bLQ9fMpTUXxHE23tIwgmb14wBCOhAdmeXrFhWMzZrd3Dz9tC5A7fgO3nonEOHMEkJ9Eqg3KPCmf-LhFY5KpH_vc4mDTujg6NXPXyyAuYsTIfVG0DZMMmUIyfyD52tgBTJM_1INX2KfySOBtT1NZcgLAnXevgBYLI0h2u8Fd6THEs87x5034lYDIzUtpetV2zcT5VJA0fI81_UmfQCGTKvFLd7bYTraKe6AJK9Jw'

# With env var `OSDU_API_URL` set in current environment.
os.environ['OSDU_API_URL'] = 'https://osdu.petrosys.com.au'
osdu_client = SimpleOsduClient(data_partition, token)


query = {
    "kind": f"osdu:wks:*:*"
}


#result = osdu_client.schema.get_all_schemas()

#print(result)

sequence = {}
with open('../schema/SchemaRegistrationResources/shared-schemas/osdu/load_sequence.1.0.0.json') as seqf:
    sequence = json.loads(seqf.read())

for sch in sequence:
    result = osdu_client.schema.add_schema('../schema/SchemaRegistrationResources/' + sch['relativePath'])

print(result)

#result = osdu_client.schema.get_all_schemas()

#print(result)
