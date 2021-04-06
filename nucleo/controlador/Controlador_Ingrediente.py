from nucleo.modelo.Ingrediente import Ingrediente, Ingrediente_producto
from nucleo.controlador import controlador_log_acciones_usuario as log
from app_main.conexion import db
from datetime import datetime

ahora = datetime.now()

def agregar(nombre, descripcion, cantidad_disponible,unidad_medida, fecha_registro, usuario):
    
    if cantidad_disponible >=1000 and unidad_medida == "g":
        convercion = cantidad_disponible/1000
        unidad_medida = "kg"
    elif cantidad_disponible >=1000 and unidad_medida == "ml":
        convercion = cantidad_disponible/1000
        unidad_medida = "l"
    else: 
         convercion = cantidad_disponible   
         
    ingrediente = Ingrediente(
        nombre = nombre,
        descripcion = descripcion,
        cantidad_disponible = convercion,
        unidad_medida = unidad_medida,
        usuario = usuario,
        fecha_registro = ahora.strftime("%d/%m/%Y  %H:%M:%S")
    )
    db.session.add(ingrediente)
    db.session.flush()
    
    log.registrar_log(usuario,'Agregar',Ingrediente.__tablename__,ingrediente._id)
    
    return True


def modificar(_id, nombre, descripcion, cantidad_disponible,unidad_medida, fecha_registro, usuario):
    ingredienteModificar =  db.session.query(Ingrediente).filter(Ingrediente._id == _id).first()
    ingredienteModificar.nombre = nombre
    ingredienteModificar.descripcion = descripcion
    ingredienteModificar.cantidad_disponible = cantidad_disponible
    ingredienteModificar.unidad_medida = unidad_medida
    ingredienteModificar.usuario = usuario
    fecha_registro = ahora.strftime("%d/%m/%Y  %H:%M:%S")
    ingredienteModificar.fecha_registro = fecha_registro
    db.session.add(ingredienteModificar)
    db.session.flush()

    log.registrar_log(usuario,'Modificar',Ingrediente.__tablename__,ingredienteModificar._id)
    return True

def desactivar(_id, usuario):
    ingredienteDesactivar = db.session.query(Ingrediente).filter(Ingrediente._id == _id).first()
    ingredienteDesactivar.estatus = 'Inactivo'
    db.session.add(ingredienteDesactivar)
    db.session.flush()
    
    log.registrar_log(usuario,'Desactivar',Ingrediente.__tablename__,ingredienteDesactivar._id)
    return True

def reactivar(_id, usuario):
    ingredienteReactivar = db.session.query(Ingrediente).filter(Ingrediente._id == _id).first()
    ingredienteReactivar.estatus = 'Activo'
    db.session.add(ingredienteReactivar)
    db.session.flush()
    
    log.registrar_log(usuario,'Reactivar',Ingrediente.__tablename__,ingredienteReactivar._id)
    return True

def consultarallIngredientes():
    return Ingrediente.query.all()

def consultar(_id):
    if _id == 0:
        return Ingrediente.query.all()
    else:
        return db.session.query(Ingrediente).filter(Ingrediente._id == _id).first()




########### ACCIONES DE LA TABLA IGREDIENTE-PRODUCTO  ############################
def agregarIgrePro(objeto ,usuario, producto):   
    
    ingredienteProducto = Ingrediente_producto(
        cantidad_requerida = objeto.get("cantidad_requerida"),
        producto = producto,
        ingrediente = objeto.get("ingrediente"), 
        usuario = usuario,
        fecha_registro = ahora.strftime("%d/%m/%Y  %H:%M:%S")
    )
    db.session.add(ingredienteProducto)
    return True


def modificarIgrePro(objeto):
    ingredienteProductoModificar =  db.session.query(Ingrediente_producto).filter(Ingrediente_producto._id == objeto.get("_id")).first()
    print(ingredienteProductoModificar)
    ingredienteProductoModificar.cantidad_requerida = objeto.get("cantidad_requerida"),
    ingredienteProductoModificar.ingrediente = objeto.get("ingrediente"),
    ingredienteProductoModificar.fecha_registro = ahora.strftime("%d/%m/%Y  %H:%M:%S")
    db.session.add(ingredienteProductoModificar)
    
    return True

def desactivarIgrePro(_id):
    ingredienteProductoDesactivar = db.session.query(Ingrediente_producto).filter(Ingrediente_producto.producto.like(_id)).all()
    for a in ingredienteProductoDesactivar:
            a.estatus = 'Inactivo'
    db.session.add(a)
    return True

def reactivarIgrePro(_id):
    ingredienteProductoReactivar = db.session.query(Ingrediente_producto).filter(Ingrediente_producto.producto.like(_id)).all()
    for a in ingredienteProductoReactivar:
        a.estatus = 'Activo'
    db.session.add(a)
    return True

def consultarallIngredientesProductos():
    return Ingrediente_producto.query.all()

def consultarIngrePro(_id):
    if _id == 0:
        return Ingrediente_producto.query.all()
    else:
        return db.session.query(Ingrediente_producto).filter(Ingrediente_producto._id == _id).first()
    

def restarCantidadDisponible(_idProducto, CantidadComprada):
   ingrediente_producto = db.session.query(Ingrediente_producto).filter(Ingrediente_producto.producto == _idProducto).all()
   
   for ingrepro in ingrediente_producto:
       
       cantidadreque = ingrepro.cantidad_requerida*CantidadComprada
       
       ingrediente_ingrediente = db.session.query(Ingrediente).filter(Ingrediente._id == ingrepro.ingrediente).first()

       if ingrediente_ingrediente.unidad_medida in ("kg", "l") :
           ingrediente_ingrediente.cantidad_disponible -= cantidadreque/1000
           
           if ingrediente_ingrediente.cantidad_disponible < 1:
               if ingrediente_ingrediente.unidad_medida == "kg":
                   ingrediente_ingrediente.unidad_medida = "g"
               else:
                   ingrediente_ingrediente.unidad_medida = "ml" 
                          
               ingrediente_ingrediente.cantidad_disponible *= 1000
       else:
        ingrediente_ingrediente.cantidad_disponible -= cantidadreque
              
       db.session.add(ingrediente_ingrediente)  

    
