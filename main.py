from fastapi import FastAPI
from database import * 
from models import *
from schemas import *
#from fastapi.middleware.cors import CORSMiddleware


from routers import capteurs_routes
from routers import centrales_routes
from routers import donnees_capteurs_routes
from routers import reservoirs_routes
from routers import seuils_routes
from routers import type_donnes_routes
from routers import utilisateurs_routes
from routers import login_routes


app = FastAPI()
        

app.include_router(router= capteurs_routes.capteur_router, prefix= "/api/capteur")
app.include_router(router= centrales_routes.centrale_router, prefix= "/api/centrale")
app.include_router(router= donnees_capteurs_routes.donnees_router, prefix= "/api/donnees")
app.include_router(router= reservoirs_routes.reservoir_router, prefix= "/api/reservoirs")
app.include_router(router= seuils_routes.seuil_router, prefix= "/api/seuils")
app.include_router(router= type_donnes_routes.type_router, prefix= "/api/type_donnees")
app.include_router(router= utilisateurs_routes.utilisateur_router, prefix= "/api/utilisateurs")
app.include_router(router= login_routes.login_router, prefix= "/api/login")


"""app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)"""