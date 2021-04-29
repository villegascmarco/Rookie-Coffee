
# Rookie Coffee

Software to manage [Transformation processes](https://www.open.edu/openlearn/money-business/leadership-management/understanding-operations-management/content-section-3.4).


Tracks the ingredients status until they are sold as a product to a customer.

## Tech Stack

**Client:** React, HTML, CSS

**Server:** Python, MySQL

  
## Run Locally

Clone the project

```bash
  git clone https://github.com/villegascmarco/rookie-coffee.git
```

Go to the project directory

```bash
  cd rookie-coffee
```

Open and install DB sample file located in the following path:

```bash
   .\base_datos_estructura\db-backup.sql
```

Run bash file

```bash
  # This file will initialize the virtual env and install all the necessary dependencies.
  ./flask_run.bat
```

  
## Usage/Examples

### Login
#### Input
```json
POST http://glassware.pythonanywhere.com/security/login HTTP/1.1
Authorization: Basic {user:password}
Content-Type: application/json

{
    "dispositivo" : "Chrome",
    "direccion_ip": "XXX.XXX.XX.XXX"
}
```
#### Output
```json
{
    "nombre": "Full name",
    "nombre_acceso": "Username",
    "rol": "Admin",
    "token": Your_Token
}
```

### Create Sales Order
#### Input
```json
POST http://127.0.0.1:5000/venta/registrar HTTP/1.1
Content-Type: application/json
x-access-tokens: {Your_Token}

{
    "total_venta": "140",
    "detalles": [
        {
            "producto": 32,
            "precio_historico": 40,
            "cantidad": 1
        },
        {
            "producto": 34,
            "precio_historico": 50,
            "cantidad": 2
        }
    ]
}
```
#### Output
```json
{
    "contenido": {
        "_id": 72,
        "detalle_venta": [
            {
                "_id": 100,
                "cantidad": 1,
                "estatus": "Activo",
                "precio_historico": 40.0,
                "producto_descripcion": "Taza Chica de Cafe Chapuchino Vainilla caliente, perfecto para tomar en las mañanas  ",
                "producto_id": 32,
                "producto_nombre": "Cafe Capuchino Vainilla / Chico",
                "venta": 72
            },
            {
                "_id": 101,
                "cantidad": 2,
                "estatus": "Activo",
                "precio_historico": 50.0,
                "producto_descripcion": "2 piezas de bisquet con mermelada",
                "producto_id": 34,
                "producto_nombre": "Bisquets con mermelada",
                "venta": 72
            }
        ],
        "estatus": "Activo",
        "fecha": "2021-04-29T13:16:27",
        "total_venta": 140.0,
        "usuario": "root"
    },
    "estado": "OK",
    "mensaje": "Venta registrada"
}
```

### Request Sales Orders
#### Input
```json
POST http://127.0.0.1:5000/venta/registrar HTTP/1.1
Content-Type: application/json
x-access-tokens: {Your_Token}

{
    "metodo_busqueda":"mensual",
    "fecha_inicial":"2021-04-15T03:36:00",
    "fecha_final":"2021-04-15T03:36:02"
}
```
Accepted values in `metodo_busqueda` are  `dia`,`semanal`,`mensual`,`especifico` y `general`

`fecha_inicial` and `fecha_final` are necessary when `metodo_busqueda:especifico`
#### Output
```json
{
    "contenido": [
        {
            "_id": 71,
            "detalle_venta": [
                {
                    "_id": 99,
                    "cantidad": 1,
                    "estatus": "Activo",
                    "precio_historico": 40.0,
                    "producto_descripcion": "Taza Chica de Cafe Chapuchino Vainilla caliente, perfecto para tomar en las mañanas  ",
                    "producto_id": 32,
                    "producto_nombre": "Cafe Capuchino Vainilla / Chico",
                    "venta": 71
                }
            ],
            "estatus": "Activo",
            "fecha": "2021-04-29T13:14:54",
            "total_venta": 90.0,
            "usuario": "villegasUser"
        },
        {
            "_id": 72,
            "detalle_venta": [
                {
                    "_id": 100,
                    "cantidad": 1,
                    "estatus": "Activo",
                    "precio_historico": 40.0,
                    "producto_descripcion": "Taza Chica de Cafe Chapuchino Vainilla caliente, perfecto para tomar en las mañanas  ",
                    "producto_id": 32,
                    "producto_nombre": "Cafe Capuchino Vainilla / Chico",
                    "venta": 72
                },
                {
                    "_id": 101,
                    "cantidad": 2,
                    "estatus": "Activo",
                    "precio_historico": 50.0,
                    "producto_descripcion": "2 piezas de bisquet con mermelada",
                    "producto_id": 34,
                    "producto_nombre": "Bisquets con mermelada",
                    "venta": 72
                }
            ],
            "estatus": "Activo",
            "fecha": "2021-04-29T13:16:27",
            "total_venta": 140.0,
            "usuario": "villegasUser"
        }
    ],
    "estado": "OK",
    "mensaje": "Información consultada correctamente",
    "registros": 2
}
```

### Cancel Sales Order
#### Input
```json
POST http://127.0.0.1:5000/venta/desactivar HTTP/1.1
Content-Type: application/json
x-access-tokens: {Your_Token}

{
   "_id":"2",
   "fecha":"2021-03-19T12:21:04"
}
```
`_id`: Sales Order ID that will be cancel.

`fecha`: Needs to have the date when the related Sales Order was created.
#### Output
```json
{
    "contenido": [
        {
            "_id": 71,
            "detalle_venta": [
                {
                    "_id": 99,
                    "cantidad": 1,
                    "estatus": "Activo",
                    "precio_historico": 40.0,
                    "producto_descripcion": "Taza Chica de Cafe Chapuchino Vainilla caliente, perfecto para tomar en las mañanas  ",
                    "producto_id": 32,
                    "producto_nombre": "Cafe Capuchino Vainilla / Chico",
                    "venta": 71
                }
            ],
            "estatus": "Activo",
            "fecha": "2021-04-29T13:14:54",
            "total_venta": 90.0,
            "usuario": "villegasUser"
        },
        {
            "_id": 72,
            "detalle_venta": [
                {
                    "_id": 100,
                    "cantidad": 1,
                    "estatus": "Activo",
                    "precio_historico": 40.0,
                    "producto_descripcion": "Taza Chica de Cafe Chapuchino Vainilla caliente, perfecto para tomar en las mañanas  ",
                    "producto_id": 32,
                    "producto_nombre": "Cafe Capuchino Vainilla / Chico",
                    "venta": 72
                },
                {
                    "_id": 101,
                    "cantidad": 2,
                    "estatus": "Activo",
                    "precio_historico": 50.0,
                    "producto_descripcion": "2 piezas de bisquet con mermelada",
                    "producto_id": 34,
                    "producto_nombre": "Bisquets con mermelada",
                    "venta": 72
                }
            ],
            "estatus": "Activo",
            "fecha": "2021-04-29T13:16:27",
            "total_venta": 140.0,
            "usuario": "villegasUser"
        }
    ],
    "estado": "OK",
    "mensaje": "Información consultada correctamente",
    "registros": 2
}
```
## Documentation

[Documentation, Diagrams, Requirements, ...](https://drive.google.com/drive/u/0/folders/1Mb4uEqwE9WGLaCfJ64EI7ObdQ_dpkLuU)

  
## Authors

- [@MoiMorua - Backend Developer](https://github.com/MoiMorua)
- [@OscarHendrix10 - Backend Developer](https://github.com/OscarHendrix10)
- [@villegascmarco - Backend Developer](https://github.com/villegascmarco)
- [@ximenaTo - Frontend Developer](https://github.com/ximenaTo)
- [@pablotz - Frontend Developer](https://github.com/pablotz)

  