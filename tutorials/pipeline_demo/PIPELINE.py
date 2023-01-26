import hydra
from mini_pipeline_imgresize import ImageResizeExifData
from omegaconf import DictConfig, OmegaConf

"""
Trying @hydra
"""
@hydra.main(version_base="1.3", config_path="conf", config_name="config.yaml")
def hydra_try(cfg: DictConfig):
    print(cfg.keys())
    print("Sensei! This is all i could do with hydra rn. I'll do more. :D")
    
if __name__ == "__main__":
    hydra_try()