import importlib
from datetime import datetime
from pathlib import Path

from pydantic import BaseModel
from sqlalchemy import Column, DateTime, Integer, orm

# Classe Base para os modelos SQLAlchemy


class Base(orm.DeclarativeBase):
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default="now()")
    updated_at = Column(DateTime(timezone=True),
                        onupdate=datetime.now(), insert_default=datetime.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)


# Classe HelpModel com Pydantic para validação e serialização
class BaseSchema(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime

    class Config:
        from_attributes = True


def import_models_from_modules():
    # Ajuste este caminho se necessário
    base_dir = Path(__file__).parent.parent
    modules_dir = base_dir / "modules"
    for module_dir in modules_dir.iterdir():
        if module_dir.is_dir():
            # Procura arquivos que terminam com _model.py
            model_file = module_dir / f"{module_dir.name}_model.py"
            if model_file.exists():
                # Importa o módulo usando importlib
                module_name = f"app.modules.{
                    module_dir.name}.{module_dir.name}_model"
                importlib.import_module(module_name)
