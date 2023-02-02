import hydra
import logging
import getpass

from mini_pipeline_imgresize import ImageResizeExifData
from omegaconf import DictConfig

log = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="conf", config_name="config")
def run_pipiline(cfg:DictConfig):
    
    whoami = getpass.getuser()
    log.info(f"{whoami} started the pipeline")

    #class instance
    ired = ImageResizeExifData(cfg)

    #class method

    try: 
        log.info(f"Resizing image.")
        ired.resize_image()
    except Exception as e:
        log.error(f"Failed: {e}. Error resizing image")

    #ired.exif_data_json()

    try: 
        log.info(f"Creating metadata")
        ired.exif_data_json()
    except Exception as e:
        log.error(f"Failed: {e}. Error creating metadata")
        
if __name__ == "__main__":
    run_pipiline()
