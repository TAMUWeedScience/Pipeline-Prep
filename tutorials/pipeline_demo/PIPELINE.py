import hydra
from mini_pipeline_imgresize import ImageResizeExifData
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base="1.3", config_path="conf", config_name="config.yaml")
def main(cfg: DictConfig):
    
    # class instance
    ired = ImageResizeExifData(cfg)
    # class methods
    ired.resize_image()
    ired.exif_data_json()
    
if __name__ == "__main__":
    main()