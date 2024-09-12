from typing import Optional

from pycpfcnpj import cpfcnpj
from pydantic import BaseModel, field_validator, model_validator


class CreateRuralProducerSchema(BaseModel):
    document_number: str
    name: str
    farm_name: str
    city: str
    state: str

    class Config:
        from_attributes = True

    @classmethod
    @model_validator(mode='after')
    def verify_document_number(self):
        if not cpfcnpj.validate(self.document_number):
            raise ValueError("CPF ou CNPJ inválido")


class UpdateRuralProducerSchema(BaseModel):
    document_number: Optional[str] = "CPF or CNPJ"
    name: Optional[str] = "Willian Caetano"
    farm_name: Optional[str] = "Fazenda Jacaré"
    city: Optional[str] = "Campinorte"
    state: Optional[str] = "GO"

    class Config:
        from_attributes = True
