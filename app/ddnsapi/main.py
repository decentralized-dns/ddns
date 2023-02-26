
# from ddnsapi.routes.home import router as home_router
from ddnsapi.routes.ping import router as ping_router
from fastapi import FastAPI, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


def get_application() -> FastAPI:
    app = FastAPI(debug=True, title="DDNS", version="0.1.0")
    # app.include_router(home_router)
    app.include_router(ping_router)

    # Set all CORS enabled origins
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.mount("/static", StaticFiles(directory="static"), name="static")
    return app


app = get_application()

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/{page}', response_class=HTMLResponse)
async def display_page(request: Request, page: str):
    return templates.TemplateResponse(f"{page}.html", {"request": request})


@app.post("/search", response_class=HTMLResponse)
async def search(request: Request, domain_name: str = Form("domain_name")): #,
    # domain_name= request.args['domain_name']
    # print("-" * 40)
    # print("domain_name", domain_name)
    # print("-"*40)
    # print(request)
    # print("-" * 40)
    domain_info = 1
    parent = 1
    registrant = 1
    controller = 1
    expiration_date = 1
    resolver = 1
    email = 1
    url = 1
    avatar = 1
    description = 1
    notice = 1
    keywords = 1
    dicord = 1
    github = 1
    reddit = 1
    telegram = 1
    address = 1

    # Your domain search logic here
    return templates.TemplateResponse("search.html",
                                      {"request": request, "domain_name": domain_name, "domain_info": domain_info,
                                       "parent": parent, "registrant": registrant, "controller": controller,
                                       "expiration_date": expiration_date, "resolver": resolver, "email": email,
                                       "url": url, "avatar": avatar, "description": description, "notice": notice,
                                       "keywords": keywords, "dicord": dicord, "github": github, "reddit": reddit,
                                       "telegram": telegram, "address":address})



@app.get('/addressinfo', response_class=HTMLResponse)
async def get_address_info(request: Request, account_address: str = Form(...)):
    default_domain = get_default_domain(account_address)
    asso_domains = get_asso_domains(account_address)
    return templates.TemplateResponse(
        "search.html",
        {"request": request,
         "account_address": account_address,
         "default_domain": default_domain,
         "asso_domains": asso_domains}
    )
def get_default_domain(account_address):
    return 'TestDomain'

def get_asso_domains(account_address):
    return ('AABB','CCDD')



@app.get('/register', response_class=HTMLResponse)
async def register_status(request: Request, register_name: str = Form(...),
                          register_duration: str = Form(...)):
    reg_status = register_name(register_name, register_duration)
    return {"reg_status": reg_status}

def register_name(register_name, register_duration):
    return "Success"


@app.get('/extend', response_class=HTMLResponse)
async def extend_status(request: Request, extend_name: str = Form(...),
                          extend_duration: str = Form(...)):
    extend_status = extend_name(extend_name, extend_duration)
    return templates.TemplateResponse(
        "manage.html",
        {"request": request,
         "extend_status": extend_status}
    )

def extend_name(extend_name, extend_duration):
    return "Success"



@app.get('/renew', response_class=HTMLResponse)
async def renew_status(request: Request, renew_name: str = Form(...),
                          renew_duration: str = Form(...)):
    renew_status = renew_name(renew_name, renew_duration)
    return templates.TemplateResponse(
        "manage.html",
        {"request": request,
         "renew_status": renew_status}
    )

def renew_name(renew_name, renew_duration):
    return "Success"


@app.get("/connect-pera")
async def connect_pera(request: Request):
    # Request the AlgoSigner API to connect to the Pera wallet
    payload = {
        "ledger": "TestNet",
        "wallet": {
            "name": "Pera",
            "type": "WalletConnect",
            "url": "https://app.pera.finance/",
            "icon": "https://app.pera.finance/favicon.ico"
        }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post("https://api.algosigner.io/v2/wallets", data=json.dumps(payload), headers=headers)

    # Check if the connection was successful
    if response.status_code == 200:
        return {"message": "Connected to Pera Wallet"}
    else:
        return {"message": "Failed to connect to Pera Wallet"}
