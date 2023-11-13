from EtoEmlProject import logger
from EtoEmlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'>>>>>>> Stage {STAGE_NAME} started <<<<<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nX===============')
except Exception as e:
    logger.exception(e)
    raise e 
