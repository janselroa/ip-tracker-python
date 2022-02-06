import requests
option = input("Quiere ver los datos de su direccion ip o de un dominio externo(PC/WEB)\n\n").lower()

api_key=""
with open("api_key.txt","r") as file:
    api_key=file.read()
url=f"https://geo.ipify.org/api/v2/country,city?apiKey={api_key}"

def show_data(data):
   location = data['location']
   time_zone = location['timezone'].replace("-","")
   print(f"IP: {data['ip']}\nname: {data['as']['name']}")
   print(f"location: {location['region']}, {location['country']}")
   print(f"Hora: {time_zone}")
   print(f"Proveedor de internet: {data['isp']}")

if option == "pc":
   ip = requests.get("https://api.ipify.org/?format=json").json()['ip']
   response = requests.get(f"{url}&ipAddress={ip}")
   user_data = response.json()
   show_data(user_data)

elif option == "web":
   address = input("Ingrese la direccion del sitio web:\n").lower()
   response = requests.get(f"{url}&domain={address}")
   data = response.json()
   show_data(data)
