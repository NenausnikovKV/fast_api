# request to root orl

# --verbose verbose request
http -v localhost:8080/hi
# --body print only response body
http -b localhost:8080/hi
# print full respones
http localhost:8080/hi


# request containing query params
http localhost:8080/hi who==Germany
http localhost:8080/hi who==Mom other==Son


# request containing body params
http localhost:8080/hi_body who=Mom
http localhost:8080/hi_body who=Mom other=son


#request containing additional header
http localhost:8080/hi_header who:Mo
