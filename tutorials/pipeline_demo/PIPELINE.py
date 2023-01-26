import hydra
from mini_pipeline_imgresize import ImageResizeExifdata
from omegaconf import DictConfig, OmegaConf

"""
Trying @hydra
"""
@hydra.main(version_base="1.3", config_path="conf", config_name="config.yaml")
def main(cfg: DictConfig):
    
    # class instance
    ired = ImageResizeExifdata(cfg)
    # class methods
    ired.resize_image()
    ired.exif_data_json()
    
if __name__ == "__main__":
    main()