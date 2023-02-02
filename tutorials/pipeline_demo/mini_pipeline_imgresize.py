import json
import os
import logging
import getpass

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

        # Input dir
        self.input_images = (Path(cfg.general.image_folder))
        self.file_path = Path(cfg.general.image_folder).glob("*.jpeg")

        # Output dir
        self.resized_images = (Path(cfg.general.resized_images))

        # Arguments resize_image
        self.size1 = cfg.arg.newsize1
        self.size2 = cfg.arg.newsize2

        #logging
        self.log = logging.getLogger(__name__)


    def resize_image(self):
        """
        This function change the size of an image and save it as a new file.

        """
        # Loop through all images in the file_path with .jpeg ext.
        for images in self.file_path:
        # Use Image.open to open the image in PIL's Image module
            image = Image.open(images)

            #use .resize to resize the image and save it
            img_rs = image.resize((self.size1, self.size2))

            # Retain original image name with "resized" appended
            fn, fext = os.path.splitext(images)
            img_rs.save(self.resized_images/ f"{fn}_resized.png")

	
    def exif_data_json(self):
        """
        This function extract exif data of an image and write it in a json file.
        """
        # Loop through all images in the file_path with .jpeg ext.
        for images in self.file_path:
            image = Image.open(images)
            
            exif_table={} # Empty table 
            # Loop through all items in results of getexif()
            for k, v in image.getexif().items():
                if k in TAGS:
                    # Make the exifdata items readable
                    if isinstance(v, TiffImagePlugin.IFDRational):
                        v = float(v)
                    elif isinstance(v, tuple):
                        v = tuple(float(t) if isinstance(t, TiffImagePlugin.IFDRational) else t for t in v)
                    elif isinstance(v, bytes):
                        v = v.decode(errors="replace")
                    exif_table[TAGS[k]] = v # Populate the table with exifdata items

            #use json.dumps to write the exifdata in a json file
            with open(f"{images}_jsondata", "w") as json_data:
                json.dump(exif_table, json_data, indent=4)
