from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Crear una instancia de la base para crear tablas
Base=declarative_base()

#Listado de modelos de la APLICACION
#USUARIO
class Usuario(Base):
    __tablename__="usuarios"
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(50))
    edad=Column(Integer)
    telefono=Column(String(12))
    correo=Column(String(20))
    contraseña=Column(String(10))
    fechaRegistro=Column(Date)
    ciudad=Column(String(50))


#GASTO
class Gasto(Base):
    id=Column(Integer, primary_key=True, autoincrement=True)
    monto=Column(Integer(50))
    fecha=Column(Date)
    descripcion=Column(String(50))
    nombre=Column(String(50))

#CATEGORIA
class Categoria(Base):
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreCategoria=Column(String(50))
    descripcion=Column(String(50))
    fotoIcono=Column(String(50))
    
#METODOS DE PAGO
class MetodoPago(Base):
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreMetodo=Column(String(50))
    descripcion=Column(String(50))


#FACTURA
class Factura(Base):
    pass