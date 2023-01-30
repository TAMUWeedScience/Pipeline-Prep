import hydra
from my_script import ImageResize #to import the ImageResize class from my_script.py

@hydra.main(version_base=None, config_path="conf", config_name="config")
def pipeline(cfg):
    ir = ImageResize(cfg) #calling the class from my_script.py
    ir.resize_image() #callig the function resize.image
    
if __name__ == "__main__":
    pipeline()