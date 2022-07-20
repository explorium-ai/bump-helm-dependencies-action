import os
import yaml

dct = yaml.load(os.environ["PATHS"],yaml.Loader)

# path/to/my/chart:
#     dependencies:
#         - name: redis
#         value: 1.0.4

def set_version(path,dependency_name,version):
    with open(os.path.join(path,'Chart.yaml')) as f:
        doc = yaml.safe_load(f)

    for d in doc['dependencies']:
        if d["name"] == dependency_name:
            d["version"] = version

    with open(os.path.join(path,'Chart.yaml'), 'w') as f:
        yaml.dump(doc, f)

for key in dct:
    print(key)
    for d in dct[key]["dependencies"]:
        print(d["name"],d["version"])
        set_version(key,d["name"],d["version"])