import xml.etree.ElementTree as ET
import json
import sys
import argparse

"""generates adictionary  used as argument to the SubElement function"""
def DictForParamTAG(name,value):
    one_dic ={}
    one_dic["name"]=name
    one_dic["value"]=str(value)
    return one_dic


parser = argparse.ArgumentParser(description='')
parser.add_argument('json', help='json file with configurations')
parser.add_argument('xml', help='xml base file')
parser.add_argument('-id', help='product id', default = "mxb")

args = parser.parse_args()

if len(sys.argv) < 3:
    print("error:no params")
   
tree = ET.parse(str(args.xml))
root = tree.getroot()

with open(str(args.json)) as json_file:
    data = json.load(json_file)
json_file.close()
     
for k,v  in data.items():
    if v != -2:
        element = ET.SubElement(root.find('nvm'), 'param', 
                                DictForParamTAG(k,v))

root.set('productID', str(args.id))

tree.write('max4.xml')