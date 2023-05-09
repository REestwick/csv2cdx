import json
import re
import pandas as pd




config_file = {
                    "component_configuration": {
                        "name": None,
                        "version": None,
                        "type": None,
                        "bom-ref": None,
                        "group": None,
                        "publisher": None,
                        "purl": None,
                        "licenses": [
                        {
                            "license_name": None,
                            "license_url": None,
                            "license_id": None
                        }
                        ],
                        "hashes": [
                        {
                            "hash_alg": None,
                            "hash_content": None
                        }
                        ],
                        "externalReferences": [
                        {
                            "er_type": None,
                            "er_url": None
                        }
                        ],
                        "mime type": None,
                        "description": None,
                        "author": None,
                        "cpe": None,
                        "swid": None,
                        "pedigree": None,
                        "components":None,
                        "evidence":None,
                        "releaseNotes":None,
                        "copyright":None
                    }
                }




class Auto_Builder:
    def __init__(self, csv_title :pd.DataFrame):
        self.config_file = {
                    "component_configuration": {
                        "name": None,
                        "version": None,
                        "type": None,
                        "bom-ref": None,
                        "group": None,
                        "publisher": None,
                        "purl": None,
                        "licenses": [
                        {
                            "license_name": None,
                            "license_url": None,
                            "license_id": None
                        }
                        ],
                        "hashes": [
                        {
                            "hash_alg": None,
                            "hash_content": None
                        }
                        ],
                        "externalReferences": [
                        {
                            "er_type": None,
                            "er_url": None
                        }
                        ],
                        "mime type": None,
                        "description": None,
                        "author": None,
                        "cpe": None,
                        "swid": None,
                        "pedigree": None,
                        "components":None,
                        "evidence":None,
                        "releaseNotes":None,
                        "copyright":None
                    }
                }
        
    

    hashes_alg = "^(h|H)ash.*alg.*[0-9]$"
    hashes_content = "^(h|H)ash.*cont.*[0-9]$"
    licenses = "^(l|L)icenses.*[0-9]$"
    external_ref = "^(e|E)xt.*(r|R)ef.*[0-9]$"

