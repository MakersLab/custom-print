import yaml
import json
import os
import uuid

def loadFromFile(path, bytes=False):
    from config import PATH
    if not os.path.isabs(path):
      path = os.path.join(PATH, path)
    readType = 'r' if not bytes else 'rb'
    encoding = 'utf-8' if not bytes else None
    fileContents = None
    with open(path, readType, encoding=encoding) as file:
        fileContents = file.read()
        file.close()
    return fileContents

def loadYaml(fileName):
    return yaml.load(loadFromFile(fileName))

def loadJson(fileName):
    return json.loads(loadFromFile(fileName))

def writeFile(fileName, content):
    path = '/'.join(os.path.dirname(__file__).split('/')[0:-1])
    with open((os.path.join(path,fileName)), 'w') as file:
        file.write(content)
        file.close()

def getPath(path):
  from config import PATH
  return os.path.join(PATH, path)

def addUniqueIdToFile(filename):
    splitFilename = filename.split('.')
    splitFilename[0] = '{filename}-{id}'.format(filename=splitFilename[0], id=str(uuid.uuid4())[:6])
    return '.'.join(splitFilename)

def removeValueFromDict(k, value):
  for key in k:
    del k[key][value]
  return k

def additionalDeliveryInfo(delivery):
  if delivery == 'express':
    return 'express dodání(+30% ceny)'
  else:
    return delivery

def loadFilaments(path):
  filamentsConfig = loadYaml(path)
  filaments = {}
  for material in filamentsConfig:
    for color in filamentsConfig[material]['colors']:
      filamentId = '{0}_{1}'.format(material, color['code'])
      filaments[filamentId] = {
        'material': material,
        'price': filamentsConfig[material]['price'],
        'color-name': color['name'],
        'color-code': color['code'],
      }
  return filaments
