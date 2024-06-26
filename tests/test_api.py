import pytest
from packageurl import PackageURL
from csv2cdx.cy_api import cybeats_API
import os


def test_params():
    url =  os.environ.get("APIURL")
    access_key = os.environ.get("ACCESSKEY")
    secret_key = os.environ.get("SECRETKEY")
    purl = PackageURL.from_string('pkg:pypi/appkit@0.2.8')

    pkg = "pypi"

    check = {
            'name': 'AppKit', 
            'version': '0.2.8', 
            'purl': 'pkg:pypi/appkit@0.2.8', 
            'licenses': [
                            {'id': 'MIT'}
                        ]
        }
    
    
    api = cybeats_API(url, access_key, secret_key, pkg)

    ret = api.search_package(purl)

    assert ret == check

