# rename-cesium-tiles
Cesium tiles and directories have plus (+) sign in the name(title), which makes the url inaccessible while accessing tileset from S3. This tool removes the plus sign from each file, directory and also update the same in tileset.json file. 

# Function for accessing nested key, value from python dict 
json_extract
it takes dictionary and desired key(no matter how it is nested) as parameter and returns array of values for that key. you can update the value of nested key through this, return obj in that case. 
