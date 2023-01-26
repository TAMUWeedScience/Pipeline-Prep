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
        # Common data directory
        self.data_dir = str(Path(cfg.general.file_path).parent)
        
        # Input
        self.file_path = Path(cfg.general.file_path)
        # Ouput file names
        self.output_imgpath = Path(self.data_dir, self.file_path.stem  + "_resized.png")
        self.save_json_path = Path(self.data_dir, self.file_path.stem  + "_resized.json")

    def resize_image(self, cfg):

        #use Image.open to open the image in PIL's Image module
        image = Image.open(self.file_path)
        new_size = (cfg.general.newsize1, cfg.general.newsize1)
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
                exif_table[PIL.ExifTags.TAGS[k]] = v

        #use json.dumps to write the exifdata in a json file
        
        with open(self.save_json_path, "w") as json_data:
            json.dump(exif_table, json_data, indent=4)

if __name__ == "__main__":
    
    
    Image1 = ImageResizeExifdata()
    # Image1.resize_image((200,200))
    Image1.exif_data_json()
