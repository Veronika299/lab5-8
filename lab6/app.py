import json
import os
import requests

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')


# Ensure the data file exists
if not os.path.exists('data.json'):
    with open('data.json', 'w') as file:
        json.dump([], file)


@app.get('/')
def read_root():
    return {'Hello': 'World'}



@app.get('/beauty', response_class=HTMLResponse)
async def serve_form(request: Request):
    """Serve the HTML form."""

    print()
    return templates.TemplateResponse('main.jinja2', {'request': request})


@app.post('/submit')
async def handle_form(name: str = Form(...), phone: str = Form(...), comment: str = Form(...)):
    """Handle form submission and save to JSON file."""
    new_entry = {'name': name, 'email': phone, 'comment': comment}
    # Load existing data
    with open('data.json', 'r') as file:
        data = json.load(file)

    # Append new data
    data.append(new_entry)

    # Save back to the JSON file
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

    return {'message': 'Data submitted successfully', 'data': new_entry}


@app.get('/list')
def read_root(request: Request):
    user = 'student'
    password = 'p@ssw0rd'

    list_url = f'http://lab.vntu.org/api-server/lab8.php?user={user}&pass={password}'

    response = requests.get(list_url)
    data = response.json()
    print(data)

    return templates.TemplateResponse("table_lr8.html", {"request": request, "data": data})



