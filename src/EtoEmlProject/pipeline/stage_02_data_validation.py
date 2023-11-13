from EtoEmlProject.config.configuration import ConfigurationManager
from EtoEmlProject.components.data_validation import DataValidation
from EtoEmlProject import logger

STAGE_NAME = 'Data Ingestion Stage'

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>> Stage {STAGE_NAME} started <<<<<<<')
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>> Stage {STAGE_NAME} completed <<<<<\n\nX===========================X')
    except Exception as e:
        logger.exception(e)
        raise e    
