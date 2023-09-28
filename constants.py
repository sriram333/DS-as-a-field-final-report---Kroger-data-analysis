#Store the secret keys and constants here

# These are obtained by registering in kroger's developer's portal and created an application to generate these keys
import base64

cl_id = 'ecommerceanalytics-602f40aff74f587e1da2270d1f4906b86074759455565888471'

cl_secret = 'aldpZBA87C6ZhfqxTuSr9H8SCiESeXvhKPDgpEnz'

url = 'https://api.kroger.com/v1/connect/oauth2/token'

headers = {
   'Content-Type': 'application/x-www-form-urlencoded',
   'Authorization': 'Basic ' + base64.b64encode(f'{cl_id}:{cl_secret}'.encode()).decode()
}

data = {
   'grant_type': 'client_credentials',
   'scope':['product.compact']
}

