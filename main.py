from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

# Datos simulados
facultades = {
    "ingenieria": {
        "nombre": "Facultad de Ingeniería y Tecnologías",
        "correo": "ingenieria@ucaldas.edu.co",
        "programas": {
            "ingenieria_sistemas": {
                "nombre": "Ingeniería en Sistemas",
                "email": "sistemas@ucaldas.edu.co"
            },
            "ingenieria_alimentos": {
                "nombre": "Ingeniería de Alimentos",
                "email": "alimentos@ucaldas.edu.co"
            }
        }
    }
}
# ubicacio, telefono 

tramites = [
    {
        "nombre": "Solicitud de certificado",
        "dependencia": {
            "nombre": "Oficina de Registro",
            "correo": "registro@ucaldas.edu.co"
        },
        "requerimientos": ["Documento de identidad", "Formulario firmado"]
    },
    {
        "nombre": "Atención psicológica",
        "dependencia": {
            "nombre": "Bienestar Universitario",
            "correo": "bienestar@ucaldas.edu.co"
        },
        "requerimientos": ["Carnet estudiantil"]
    }
]
# telefono dependce...

# ENDPOINTS

@app.get("/facultad")
def get_facultades():
    return facultades

@app.get("/programa")
def get_programas():
    programas = {}
    for fac in facultades.values():
        programas.update(fac["programas"])
    return programas

@app.get("/tramites")
def get_tramites():
    return tramites
