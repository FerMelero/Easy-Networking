import subprocess
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import config
from api.entities import Scan, DiscoveredHost, DiscoveredPort
from api.entities import Base
from flask import request


engine = config.engine
Session = sessionmaker(bind=engine)

def crear_tablas():
    print("Estableciendoconexión con Postgres")
    Base.metadata.create_all(engine)
    print("Tablas creadas")

def prueba_conexion():
    session = Session()
    result = session.query(Scan).all()
    print(result)

def prueba_escaneo(target, scan_type, timing, ports, detect_version, scan_vuln, fragment):
    print(f"DEBUG: Escaneando {target} con versión={detect_version}")
    command = f"nmap {target} {scan_type} {timing} {ports}"
    return f"Lógica recibida: Versión={detect_version}, Vuln={scan_vuln}, Comando = {command}"

