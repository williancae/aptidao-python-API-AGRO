from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from app.config.migrate import create_async_engine
from app.config.settings import DATABASE_URL
from app.modules.planting_area.planting_area_model import PlantingAreaModel
from app.modules.rural_producer.rural_producer_model import RuralProducerModel
from app.modules.seed.seed_model import SeedModel


async def populate_db():

    engine = create_async_engine(DATABASE_URL)
    async_session = sessionmaker(engine,
                                 expire_on_commit=False,
                                 class_=AsyncSession
                                 )
    session = async_session()

    try:

        seed1 = SeedModel(name="Milho")
        seed2 = SeedModel(name="Soja")
        seed3 = SeedModel(name="Trigo")

        rural_producer1 = RuralProducerModel(
            document_number="12345678901", name="João Silva", farm_name="Fazenda Boa Vista", city="Uberaba", state="MG"
        )
        rural_producer2 = RuralProducerModel(
            document_number="98765432100",
            name="Maria Oliveira",
            farm_name="Sítio Bela Vista",
            city="Ribeirão Preto",
            state="SP",
        )

        planting_area1 = PlantingAreaModel(
            total_area=100.0, cultivable_area=80.0, vegetation_area=20.0, rural_producer=rural_producer1, seed=seed1
        )
        planting_area2 = PlantingAreaModel(
            total_area=150.0, cultivable_area=100.0, vegetation_area=50.0, rural_producer=rural_producer2, seed=seed2
        )

        session.add_all([seed1, seed2, seed3, rural_producer1,
                        rural_producer2, planting_area1, planting_area2])

        await session.commit()

        print("Seeds inseridos com sucesso!")
    except Exception as e:
        await session.rollback()
        print(f"Erro ao popular o banco: {e}")
    finally:
        await session.close()
