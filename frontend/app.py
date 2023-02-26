from fastapi import FastAPI, Request, Form, Response, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# from algosdk.v2client import algod
# from algosdk import mnemonic, transaction, encoding, name
# from pyteal import *


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/{page}', response_class=HTMLResponse)
async def display_page(request: Request, page: str):
    return templates.TemplateResponse(f"{page}.html", {"request": request})


@app.post("/search", response_class=HTMLResponse)
async def search(request: Request, domain_name: str = Form("domain_name")):

    request = 1
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

    # Your domain search logic here
    return templates.TemplateResponse("search.html",
                                      {"request": request, "domain_name": domain_name, "domain_info": domain_info,
                                       "parent": parent, "registrant": registrant, "controller": controller,
                                       "expiration_date": expiration_date, "resolver": resolver, "email": email,
                                       "url": url, "avatar": avatar, "description": description, "notice": notice,
                                       "keywords": keywords, "dicord": dicord, "github": github, "reddit": reddit,
                                       "telegram": telegram})



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



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
