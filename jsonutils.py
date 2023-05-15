import json
import re
import pandas as pd
import itertools 
import json


class Auto_Builder:
    def __init__(self, csv_data :pd.DataFrame):

        self.col_names_list = list(csv_data.columns)

        self.config_file_dict = {
                    "component_configuration": {
                        "name": None,
                        "version": None,
                        "type": None,
                        "bom-ref": None,
                        "group": None,
                        "publisher": None,
                        "purl": None,
                        "licenses":None,
                        "hashes":None,
                        "externalReferences":None,
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
        
        self.param_list = [
                        "^(n|N)ame.*", 
                        "^(v|V)ersion.*", 
                        "^(t|T)ype.*", 
                        "^(b|B)om.*(r|R)ef.*", 
                        "^(g|G)roup.*", 
                        "^(p|P)ublisher.*", 
                        "^(p|P)(u|U)(r|R)(l|L).*",
                        "^(m|M)ime.*(t|T)ype.*",
                        "^(d|D)escription.*",
                        "^(a|A)uthor.*",
                        "^(c|C)pe.*",
                        "^(s|S)wid.*",
                        "^(p|P)edigree.*",
                        "^(c|C)omponent.*",
                        "^(e|E)vidence.*",
                        "^(r|R)el.*(n|N)ot.*",
                        "^(c|C)opyright.*",
                        ]

        self.hashes_dict = {
                                "hash_alg": None,
                                "hash_content": None
                            }
        
        self.hashes_alg = ".*(?=.*(h|H)ash.*).*(?=.*(a|A)lg.*).*(?=[0-9]).*"
        self.hashes_content = ".*(?=.*(h|H)ash.*).*(?=.*(c|C)ontent.*).*(?=[0-9]).*"

        self.licenses_dict = {
                                "license_name": None,
                                "license_url": None,
                                "license_id": None
                            }

        self.license_name = ".*(?=.*license.*).*(?=.*name.*).*(?=[0-9]).*"
        self.license_url = ".*(?=.*license.*).*(?=.*url.*).*(?=[0-9]).*"
        self.license_id = ".*(?=.*license.*).*(?=.*id.*).*(?=[0-9]).*"

        self.ext_ref_dict = {
                                "er_type": None,
                                "er_url": None
                            }

        self.external_ref_type = ".*(?=.*(e|E)xt.*).*(?=.*(r|R)ef.*).*(?=.*(t|T)ype)(?=[0-9]).*"
        self.external_ref_url = ".*(?=.*(e|E)xt.*).*(?=.*(r|R)ef.*).*(?=.*(u|U)rl)(?=[0-9]).*"



    def assemble(self):
        regex_save = ""
        output_dict = {}
        config_dict = self.config_file_dict.get("component_configuration")
        config_list = list(config_dict.keys())
        for i in config_list:
            for j in self.param_list:
                if re.match(j, i):
                    regex_save = j
                    for k in self.col_names_list:
                        if re.match(regex_save, k):
                            output_dict[i] = k
        
        license_name_list = [i for i in self.col_names_list if re.match(self.license_name, i)]
        license_url_list = [i for i in self.col_names_list if re.match(self.license_url, i)]
        license_id_list = [i for i in self.col_names_list if re.match(self.license_id, i)] 

        hash_alg_list = [i for i in self.col_names_list if re.match(self.hashes_alg, i)]
        hash_content_list = [i for i in self.col_names_list if re.match(self.hashes_content, i)]

        exref_type_list = [i for i in self.col_names_list if re.match(self.external_ref_type, i)]
        exref_url_list = [i for i in self.col_names_list if re.match(self.external_ref_url, i)]

 
        self.licenses_dict["license_name"] = sorted(license_name_list)
        self.licenses_dict["license_url"] = sorted(license_url_list)
        self.licenses_dict["license_id"] = sorted(license_id_list)

        licenses = [dict(zip(self.licenses_dict, vals)) for vals in zip(*self.licenses_dict.values())]
        if licenses == []:
            licenses = None

        self.hashes_dict["hash_alg"] = sorted(hash_alg_list)
        self.hashes_dict["hash_content"] = sorted(hash_content_list)

        hashes = [dict(zip(self.hashes_dict, vals)) for vals in zip(*self.hashes_dict.values())]
        if hashes == []:
            hashes = None

        self.ext_ref_dict["er_type"] = sorted(exref_type_list)
        self.ext_ref_dict["er_url"] = sorted(exref_url_list)

        ext_ref = [dict(zip(self.ext_ref_dict, vals)) for vals in zip(*self.ext_ref_dict.values())]
        if ext_ref == []:
            ext_ref = None

        
        if licenses is not None: output_dict["licenses"] = licenses
        if hashes is not None: output_dict["hashes"] = hashes
        if ext_ref is not None: output_dict["externalReferences"] = ext_ref
        total_len = len(config_dict)
        pop_len = len(output_dict)

        pop_len_title = pop_len
        for i in output_dict.values():
            if isinstance(i, list):
               pop_len_title += len(i) 

        title_len = len(self.col_names_list)
        perc_filled = (pop_len / total_len) * 100
        perc_extracted = (pop_len_title / title_len) * 100
        print(f"managed to populate {int(perc_filled)}% of total config template, using {int(perc_extracted)}% of .csv columns")
        if int(perc_extracted) < 100:
             print("further manual population may be neccessary")
        json_data = json.dumps(output_dict, indent=4)
        with open("auto_build.json", "w") as file:
            file.write(json_data)
        return output_dict





