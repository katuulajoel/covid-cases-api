from api.ma import ma
from api.v1.models.cases import CaseModel

class CaseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CaseModel
        load_instance = True
        include_fk= True