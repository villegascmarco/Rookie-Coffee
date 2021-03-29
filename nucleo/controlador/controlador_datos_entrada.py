from functools import wraps
from flask import current_app,request,jsonify
from werkzeug.exceptions import BadRequest
import json

def validar_solicitud(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        try:

            if request.headers.get('Content-Type') is None:
                raise Exception
            else:
                json_dic = json.loads(json.dumps(request.json))   
                
                # for key in json_dic:
                #     if not(type(json_dic[key]) == int or type(json_dic[key]) == float):
                #         json_dic[key] = remover_indeseados(json_dic[key])
                    

        except BadRequest as br:
            msg = "La carga de la petición no contiene datos"
            return jsonify({
                'estado' : 'ERROR',
                'mensaje': msg
                }), 400

        except Exception as e:
            msg = "La carga de la petición debe ser tipo JSON"
            return jsonify({
                'estado' : 'ERROR',
                'mensaje': msg
                }), 400
        return f(*args, **kwargs)
  
    return decorator


