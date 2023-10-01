import requests
from datetime import datetime
from dataclasses import dataclass


@dataclass
class data_node:
    node_uid: str
    node_val: str
    node_name: str
    node_rw_direction: str
    node_last_update: datetime


class data_concentrator:
    def __init__(self, srv_ip: str):
        # IP of the data concentrator "server"
        self.srv_ip = srv_ip

    # Get all the nodes
    def get_all_dnode(self):
        url: str = f"{self.srv_ip}/getall/bucket"

        resp = requests.get(url)

        ret_arr = []

        for r in resp.json():
            dn = data_node(
                r["node_uid"],
                r["node_val"],
                r["node_name"],
                r["node_rw_direction"],
                datetime.fromtimestamp(
                    float(r["node_last_update"]["$date"]["$numberLong"]) / 1000
                ),
            )
            ret_arr.append(dn)

        return ret_arr

    # Get the value for a specific dnode
    # Returns only the value itself
    def get_dnode_value(self, node_uid: str):
        url: str = f"{self.srv_ip}/r/{node_uid}"
        resp = requests.get(url)

        # Since the .json() method gives a dict, the value can be returned from that
        return resp.json()["node_val"]

    # Write the value of a specific dnode
    # Returns the change_count. (Should be 1)
    def write_dnode_value(self, node_uid: str, node_val: str):
        url: str = f"{self.srv_ip}/w"
        w_data = {"node_uid": node_uid, "node_val": node_val}
        resp = requests.post(url, json=w_data)
        return resp.json()


if __name__ == "__main__":
    dc = data_concentrator("http://127.0.0.1:8000")
    all_arr = dc.get_all_dnode()
    print(all_arr)

    dnode_value = dc.get_dnode_value("ayH7nFocwL2urRvOQOfQ")
    print(dnode_value)

    dnode_written = dc.write_dnode_value("ayH7nFocwL2urRvOQOfQ", "111")
    print(dnode_written)
