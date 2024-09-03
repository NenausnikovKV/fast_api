# request to root orl
http localhost:8080

# --verbose verbose request
http -v localhost:8080
# --body print only response body
http -b localhost:8080
# print full respones
http localhost:8080


# request containing path params
http localhost:8080/hi/path/Bob

# request containing query params
http localhost:8080/hi/query who==Germany
http localhost:8080/hi who==Mom other==Son


# request containing body params
http localhost:8080/hi/body who=Mom
http localhost:8080/hi/body who=Mom other=son


#request containing additional header
# explicitly set post request
http POST localhost:8080/hi/header who:Mo
