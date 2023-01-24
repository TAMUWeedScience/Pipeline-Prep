import PIL
from PIL import Image, TiffImagePlugin
from PIL.ExifTags import TAGS
import json
from pathlib import Path
import yaml
from omegaconf import DictConfig, OmegaConf
import hydra

class Image_resize_exifdata:
    
    def __init__(self, file_path):
        """
        This function will define the data file path, data directory and 
        names of the output json file and the resized image.

        Args:
            file_path (str): file path of the image to be processed.
        """

        # Common data directory
        self.data_dir = str(Path(file_path).parent)
        
        # Input
        self.file_path = Path(file_path)
        # Ouput file names
        self.output_imgpath = Path(self.data_dir, self.file_path.stem  + "_resized.png")
        self.save_json_path = Path(self.data_dir, self.file_path.stem  + "_resized.json")
        self.save_yaml_path = Path(self.data_dir, self.file_path.stem  + "_resized.yaml")

    def resize_image(self, new_size):
        """
        This function change the size of an image and save it as a new file.

        Args:
            new_size (tuple): Input required file size. eg: (200,200)
        """
        #use Image.open to open the image in PIL's Image module
        image = Image.open(self.file_path)

        #use .resize to resize the image and save it
        img_rs = image.resize((new_size))
        # Retain original image name with "resized" appended
        img_rs.save(self.output_imgpath)

	
    def exif_data_json(self):
        """
        This function extract exif data of an image and write it in a json file.
        """
        image = Image.open(self.file_path)
        
        exif_table={}
        for k, v in image.getexif().items():
            if k in PIL.ExifTags.TAGS:
                if isinstance(v, TiffImagePlugin.IFDRational):
                    v = float(v)
                elif isinstance(v, tuple):
                    v = tuple(float(t) if isinstance(t, TiffImagePlugin.IFDRational) else t for t in v)
                elif isinstance(v, bytes):
                    v = v.decode(errors="replace")
                exif_table[PIL.ExifTags.TAGS[k]] = v

        #use json.dumps to write the exifdata in a json file
        
        with open(self.save_json_path, "w") as json_data:
            json.dump(exif_table, json_data)

    def json_to_yaml(self):
        """
        This function converts the json file to yaml file.
        """
        with open(self.save_json_path, "r") as json_file:
            json_data = json.load(json_file)

        with open(self.save_yaml_path, "w") as yaml_file:
            yaml.dump(json_data, yaml_file)


if __name__ == "__main__":
    
    file_path = "../../data/MD_Row-10_1656090862.jpg"
    Image1 = Image_resize_exifdata(file_path)
    Image1.resize_image((200,200))
    Image1.exif_data_json()
    Image1.json_to_yaml()

"""
Trying @hydra
"""
@hydra.main(version_base=None, config_path="data_directory", config_name="config_file.yaml")
def hydra_try(cfg: DictConfig):
    print(cfg.keys())
    print("Sensei! This is all i could do with hydra rn. I'll do more. :D")
    
if __name__ == "__main__":
    hydra_try()