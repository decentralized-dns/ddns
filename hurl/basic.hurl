GET https://ddns.fly.dev/
User-Agent: hurl/2.0.1

HTTP/2 200
content-type: text/html; charset=utf-8
[Asserts]
xpath "string(/html/head/title)" == "Home"
xpath "string(/html/body/div[1]/h1)" == "A revolutionary Web3 naming service"
