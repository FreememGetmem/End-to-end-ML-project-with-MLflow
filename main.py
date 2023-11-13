from EtoEmlProject import logger
from EtoEmlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from EtoEmlProject.pipeline.stage_02_data_validation import  DataValidationTrainingPipeline


STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f'>>>>>>> Stage {STAGE_NAME} started <<<<<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nX===============')
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = 'Data Validation Stage'
try:
    logger.info(f'>>>>>>> Stage {STAGE_NAME} started <<<<<<<<')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'>>>>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nX===============')
except Exception as e:
    logger.exception(e)
    raise e 
