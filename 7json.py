import json

config = json.loads(open('C:\\Users\kiran\\Documents\\WorkSpace\\Python3\\rhinoscriptsyntax.json').read())


medical =config["office"]["medical"]

print(medical)
