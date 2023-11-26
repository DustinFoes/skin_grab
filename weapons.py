import json, requests

def update_weapons():
    print("Updating skins.json")
    url = "https://raw.githubusercontent.com/MeckeDev/cs2-inspect-gui/main/gun_ids.json"
    r = requests.get(url)
    if r.status_code == 200:
        # download skins.json
        with open('weapons/gun_ids.json', 'wb') as f:
            f.write(r.content)
        return("use_new_weapons")
            
    else:
        return("use_legacy_weapons")
    
def getweapon(option):
    update_weapons()
    print("Loading skins.json")
    if update_weapons() == "use_legacy_weapons":
        print('USING LEGACY WEAPONS!')
        with open('weapons/gun_ids_legacy.json', encoding="utf-8") as f:
            weapons = json.load(f)
    elif update_weapons() == "use_new_weapons":
        print('USING UPDATED WEAPONS!')
        with open('weapons/gun_ids.json', encoding="utf-8") as f:
            weapons = json.load(f)

    option = option.lower().replace(" ", "")  # Convert to lowercase and remove spaces

    if option.isdigit():
        for i in weapons.keys():
            if i == option: return weapons[option]
            
    elif option.isalpha():
        for i in weapons.keys():
            if weapons[i].lower().replace(" ", "") == option: return i