import getpass
import logging
import os
import traceback
from pathlib import Path

import hydra
from hydra.utils import get_method
from mini_pipeline_imgresize import ImageResizeExifData
from omegaconf import DictConfig, OmegaConf

log = logging.getLogger(__name__)

@hydra.main(version_base=None, config_path="conf", config_name="config")
def run_pipiline(cfg:DictConfig):

    whoami = getpass.getuser()
    log.info(f"{whoami} is running the pipeline")

    #class instance
    ired = ImageResizeExifData(cfg)

    #class method resize
    try:
        log.info(f"Resizing image.")
        ired.resize_image()
    except Exception as e:
        log.error(f"Error resizing image")
    
    try:
        log.info(f"Creating metadata")
        ired.exif_data_json()
    except Exception as e:
        log.error(f"Error creating metadata")

    try:
        log.info(f"...")
        ired.check_output()    
    except Exception as e:
        log.error(f"Error...")

if __name__ == "__main__":
    run_pipiline()