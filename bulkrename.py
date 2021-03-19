import json
import os
folder = r".\saadat"

# Give any key, it will give you value for that. No matter how much it is nested.
def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        newJsonObject = {}
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    # update value of input key
                    obj[k] = v.replace("+","")
                    # add value of desired key to list
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        # arr consist of values for input key
        # return arr
        # obj contains updated values for key
        return obj

    values = extract(obj, arr, key)
    return values

def RemovePlusFromJson(jsonfile):
    updatedtileset = None
    with open(jsonfile) as f:
        tileset = json.load(f)
        updatedtileset = json_extract(tileset, 'uri')
        # print(names)
    with open(jsonfile, 'w') as f:
        if updatedtileset is not None:
            json.dump(updatedtileset, f)
            print(jsonfile)
    
    
#Rename all directories
for root, dirs, filenames in os.walk(folder):
    for dir in dirs:
        if "+" in dir:
            newdir = dir.replace("+","")
            os.rename(os.path.join(root, dir), os.path.join(root, newdir))


#Rename all files and paths within json
for root, dirs, filenames in os.walk(folder):
    for filename in filenames:
        if "+" in filename:
            newfilename = filename.replace("+","")
            os.rename(os.path.join(root, filename), os.path.join(root, newfilename))
        if filename.endswith("json"):
            # print(root + "\" +filename)
            myroot = root.replace("\\","/")
            RemovePlusFromJson(myroot + "/" + filename)
        

