import AminoLab
import pyfiglet
from colored import fore, back, style, attr
attr(0)
print(fore.LIGHT_STEEL_BLUE + style.BOLD)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminoantibanbo", font="smslant"))
client = AminoLab.Client()
email = input("Email >> ")
password = input("Password >> ")
client.auth(email=email, password=password)
clients = client.my_communities()
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
ndcId = clients.ndcId[int(input("Select the community >> ")) - 1]
print("""[1] On AntiBan
[2] Off AntiBan""")
select = input("Select >> ")

content = open("antiban_text.txt").read()

if select == "1":
    try:
        client.EditMyProfile(ndcId=ndcId, content=content)
        print("AntiBan Onned!")
    except Exception as e:
        print(e)

elif select == "2":
    try:
        content = "github.com/LilZevi"
        client.edit_profile(ndcId=ndcId, content=content)
        print("AntiBan Offed")
    except Exception as e:
        print(e)
