import os
import traceback
import logging
import getpass

from mini_pipeline_imgresize import ImageResizeExifData

import hydra
from hydra.utils import get_method
from omegaconf import DictConfig, OmegaConf

log = logging.getLogger(__name__)

@hydra.main(version_base=None, config_path="conf", config_name="config")
def run_pipiline(cfg:DictConfig):

    #class instance
    ired = ImageResizeExifData(cfg)

    #class method
    #ired.resize_image()
    ired.exif_data_json()

    #log information
    cfg = OmegaConf.create(cfg)
    whoami = getpass.getuser()
    log.info(f"{whoami} is running the pipeline")
    
if __name__ == "__main__":
    run_pipiline()
    if os.path.exists("sample_resized.png"): 
        log.info("Pipeline ran successfully.")
        print("Congratulaitons, this pipeline works.")
    else:
        log.error("The pipeline has some error")
        print("Pipeline didn't work correctly. Check for errors please.")