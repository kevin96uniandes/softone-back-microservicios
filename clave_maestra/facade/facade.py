from models.model import ClaveMaestra,  ClaveMaestraSchema, db

clave_maestra_schema = ClaveMaestraSchema()
class ClaveMaestraFacade():

    def obtener_claves_maestras():
        claves_maestras = ClaveMaestra.query.all()
        claves_maestras_schema = [clave_maestra_schema.dump(clave_maestra) for clave_maestra in claves_maestras]

        return claves_maestras_schema

    def crear_clave_maestra(data):
        clave_maestra = ClaveMaestra(
            nombre=data.get('nombre'),
            contrasena=data.get('contrasena'),
            pista=data.get('pista'),
        )
        db.session.add(clave_maestra)
        db.session.commit()

        return clave_maestra_schema.dump(clave_maestra)