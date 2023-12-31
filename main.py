from EtoEmlProject import logger
from EtoEmlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from EtoEmlProject.pipeline.stage_02_data_validation import  DataValidationTrainingPipeline
from EtoEmlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline
from EtoEmlProject.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from EtoEmlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

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

STAGE_NAME = 'Data Transformation Stage'
try:
    logger.info(f'>>>>>>> Stage {STAGE_NAME} started <<<<<<<<')
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f'>>>>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nX===============')
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = 'Model Trainer Stage'
try:
    logger.info(f'>>>>>>> Stage {STAGE_NAME} started <<<<<<<<')
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f'>>>>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nX===============')
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = 'Model Evaluation stage'
try:
    logger.info(f'>>>>>>> Stage {STAGE_NAME} started <<<<<<<<')
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f'>>>>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nX===============')
except Exception as e:
    logger.exception(e)
    raise e 
