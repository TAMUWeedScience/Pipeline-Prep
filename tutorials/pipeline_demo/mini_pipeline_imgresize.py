import json
from pathlib import Path

from PIL import Image, TiffImagePlugin
from PIL.ExifTags import TAGS


class ImageResizeExifData:
    def __init__(self, cfg):
        """
        This function will define the data file path, data directory and 
        names of the output json file and the resized image.

        Args:
            cfg for config.yaml
        """

        # Common data directory
        self.data_dir = str(Path(cfg.general.file_path).parent)
        # Input
        self.file_path = Path(cfg.general.file_path)
        # Ouput file names
        self.output_imgpath = Path(self.data_dir, self.file_path.stem  + "_resized.png")
        self.save_json_path = Path(self.data_dir, self.file_path.stem  + "_resized.json")
        self.size1 = cfg.arg.newsize1
        self.size2 = cfg.arg.newsize2


    def resize_image(self):
        """
        This function change the size of an image and save it as a new file.

        """
        #use Image.open to open the image in PIL's Image module

        # LOG EXAMPLE
        # if not self.file_path.exists():
        #     "give me a log message telling me something went wrong so I know more specifically why."
        #     print()
        
        image = Image.open(self.file_path)

        #use .resize to resize the image and save it
        img_rs = image.resize((self.size1, self.size2))
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

