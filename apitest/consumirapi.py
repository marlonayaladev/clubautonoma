#response = respuesta      payload = informacion      request = solicitudes

#https://pokeapi.co/api/v2/pokemon-form/

import requests 


if __name__ == "__main__":
    url = "https://pokeapi.co/api/v2/pokemon-form/"

    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        resultados = payload.get("results", [])
        print(resultados)

        if resultados:
            for xd in resultados:
                name = xd["name"]
                print(name)

    

       
        
        
        

        
