#from datetime import datetime
#from elasticsearch import Elasticsearch, helpers
#import json

#index_name = "log_test_1"

#Elasticsearch.indices.refresh(index_name)
#Elasticsearch.cat.count(index_name, params={"format": "json"})

#es=Elasticsearch([{'host':'localhost','port':'9200','timeout':60}]) 
#res = es.count(index=index_name)["count"]

#print(res)

from elk_obj_create import Create_Elk_Obj

index_name = "log_test_11"

client = Create_Elk_Obj().get_elk_obj()

try:
    cnt = Create_Elk_Obj().get_elk_count(index_name)
except:
    cnt = 0
    print("This is a new index pattern", flush= True)

print(cnt)