# Example

This folder contains an example data.csv data file and example_config.json configuration file.

The csv file contains synthetic data containing component :

* names
* versions
* hashes
* descriptions

A resulting sbom json file can be made by running the command

```bash
python3 -m csv2cdx build -pn csv2cdx_example -pv 1.0.0 -t application -c config.json -f example.csv -pt generic 
```
