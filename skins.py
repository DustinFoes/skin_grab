import json, requests
import traceback
import webbrowser


    
def getskin(option, **img: bool):
    
    with open('skins/skins.json', encoding="utf-8") as f:
        skins = json.load(f)

    # check if option is a digit
    if isinstance(option, int):
        for i in skins.keys():
            if i == option: return skins[option]

    # check if option is a string
    elif isinstance(option, str):
        for i in skins.keys():
            try:
                if skins[i].lower() == option:
                    if img:
                        # If img argument is True, perform a Google image search
                        search_query = f"{skins[i]} skin"
                        search_url = f"https://www.google.com/search?q={search_query}&tbm=isch"
                        webbrowser.open(search_url)
                    return i
            except:
                return(traceback.format_exc())
    else:
        # tell me what the option is
        print(type(option))
        print(option)
