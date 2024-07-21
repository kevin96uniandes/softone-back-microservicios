from models.model import Elemento, ElementoSecreto, ElementoLogin, db, ElementoSchema

elemento_schema = ElementoSchema()
class ElementoFacade():

    def get_elementos():
        elementos = Elemento.query.all()
        elementos_schema = [elemento_schema.dump(elemento) for elemento in elementos]

        return elementos_schema

    def create_elemento(data):

        tipo = data.get('tipo')
    
        if tipo == 'SECRETO':
            elemento = ElementoSecreto(
                nombre_elemento=data.get('nombre_elemento'),
                tipo=tipo,
                notas=data.get('notas'),
                secreto=data.get('secreto'),
                clave_id=data.get('clave_id')
            )
            db.session.add(elemento)
            db.session.commit()
    
        elif tipo == 'LOGIN':
            elemento = ElementoLogin(
                nombre_elemento=data.get('nombre_elemento'),
                tipo=tipo,
                notas=data.get('notas'),
                usuario=data.get('usuario'),
                url=data.get('url'),
                email=data.get('email'),
                clave_id=data.get('clave_id')
            )
            db.session.add(elemento)
            db.session.commit()
    
        else:
            elemento = Elemento(
                nombre_elemento=data.get('nombre_elemento'),
                tipo=tipo,
                notas=data.get('notas')
            )
            db.session.add(elemento)
            db.session.commit()

        return elemento_schema.dump(elemento)