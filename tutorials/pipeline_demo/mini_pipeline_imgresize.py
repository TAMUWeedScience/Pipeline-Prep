<<<<<<< HEAD
import json
from pathlib import Path

import hydra
import PIL
import yaml
from omegaconf import DictConfig, OmegaConf
from PIL import Image, TiffImagePlugin
from PIL.ExifTags import TAGS


class ImageResizeExifData:
    
    def __init__(self, file_path):
=======
import PIL
import hydra
import json
from PIL import Image, TiffImagePlugin
from PIL.ExifTags import TAGS
from pathlib import Path
from omegaconf import DictConfig, OmegaConf


@hydra.main(version_base=None, config_path="conf", config_name="config")
class ImageResizeExifdata:
    def __init__(self, cfg):
>>>>>>> 47211151b85bb0c370f59dc4cd11541c0e520a27
        """
        This function will define the data file path, data directory and 
        names of the output json file and the resized image.

        Args:
            file_path (str): file path of the image to be processed.
        """

        # Common data directory
        self.data_dir = str(Path(cfg.general.file_path).parent)
        
        # Input
        self.file_path = Path(cfg.general.file_path)
        # Ouput file names
        self.output_imgpath = Path(self.data_dir, self.file_path.stem  + "_resized.png")
        self.save_json_path = Path(self.data_dir, self.file_path.stem  + "_resized.json")

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
            if k in TAGS:
                if isinstance(v, TiffImagePlugin.IFDRational):
                    v = float(v)
                elif isinstance(v, tuple):
                    v = tuple(float(t) if isinstance(t, TiffImagePlugin.IFDRational) else t for t in v)
                elif isinstance(v, bytes):
                    v = v.decode(errors="replace")
                exif_table[TAGS[k]] = v

        #use json.dumps to write the exifdata in a json file
        
        with open(self.save_json_path, "w") as json_data:
            json.dump(exif_table, json_data, indent=4)

<<<<<<< HEAD
"""
Trying @hydra
"""
@hydra.main(version_base="1.3", config_path="conf", config_name="config.yaml")
def hydra_try(cfg: DictConfig):
    print(cfg.keys())
    print("Sensei! This is all i could do with hydra rn. I'll do more. :D")
    
if __name__ == "__main__":
    hydra_try()
=======
if __name__ == "__main__":
    
    file_path = "sample.jpeg"
    Image1 = ImageResizeExifdata(file_path)
    # Image1.resize_image((200,200))
    # Image1.exif_data_json()
>>>>>>> 47211151b85bb0c370f59dc4cd11541c0e520a27
