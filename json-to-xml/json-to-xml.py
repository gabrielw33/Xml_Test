import xml.etree.ElementTree as ET
import json 
import sys

"""generates adictionary  used as argument to the SubElement function"""
def DictForParamTAG(name,value):
    one_dic ={}
    one_dic["name"]=name
    one_dic["value"]=str(value)
    return one_dic 

if len(sys.argv) < 3:
    print("error:no params")
   
tree = ET.parse(str(sys.argv[2]))
root = tree.getroot()

with open(str(sys.argv[1])) as json_file:
    data = json.load(json_file)
json_file.close()
     
for k,v  in data.items():
    if v != -2:
        element = ET.SubElement(root.find('nvm'), 'param', DictForParamTAG(k,v))

if len(sys.argv) > 3:
    root.set('productID', str(sys.argv[3]))
else:    
    root.set('productID', "mxb")

tree.write('max4.xml')
