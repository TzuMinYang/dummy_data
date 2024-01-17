import json
from itertools import product
import tqdm

sample = {"_id":{"$oid":"60c40bc22395d81f6e3304ac"},"timestamp":{"$date":"2021-06-12T01:16:34Z"},"ipaddress":"1.0.133.100","geo_country":"Thailand","geo_city":"Sing Buri","lat":14.8879,"lon":100.4046,"status":"已封鎖","events":"Auto block 1.0.133.100 cause WAF block 5 times in 1 min","createby":"francis","apiaddress":"172.16.252.241","u_at":{"$date":"2021-06-12T01:20:02.758Z"},"c_at":{"$date":"2021-06-12T01:20:02.758Z"}}

if __name__ == "__main__":
    sample.pop("_id") # mongodb會自己生id
    ipaddresses = product(range(1, 58), repeat=4)
    print(type(ipaddresses))
    with open("dummy_mongo_blocklist_16.json", "w") as f:
        for ipaddress in ipaddresses:
            sample["ipaddress"] = ".".join(map(str, ipaddress))
            f.write(json.dumps(sample) + "\n")
    print("Done")