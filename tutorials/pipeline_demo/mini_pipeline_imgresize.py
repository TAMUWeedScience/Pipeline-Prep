import PIL
from PIL import Image, TiffImagePlugin
from PIL.ExifTags import TAGS
import json
from pathlib import Path

class Image_resize_exifdata:
    
    def __init__(self, file_path):
        """_summary_

        Args:
            file_path (_type_): _description_
        """

        # Common data directory
        self.data_dir = str(Path(file_path).parent)
        
        # Input
        self.file_path = Path(file_path)
        # Ouput file names
        self.output_imgpath = Path(self.data_dir, self.file_path.stem  + "_resized.png")
        self.save_json_path = Path(self.data_dir, self.file_path.stem  + "_resized.json")

    def resize_image(self, new_size):
        """_summary_

        Args:
            new_size (_type_): _description_
        """
        #use Image.open to open the image in PIL's Image module
        image = Image.open(self.file_path)

        #use .resize to resize the image and save it
        img_rs = image.resize((new_size))
        # Retain original image name with "resized" appended
        img_rs.save(self.output_imgpath)

	
    def exif_data_json(self):
        """_summary_

        Args:
            file_path (_type_): _description_
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

if __name__ == "__main__":
    
    file_path = "../../data/MD_Row-10_1656090862.jpg"
    Image1 = Image_resize_exifdata(file_path)
    Image1.resize_image((200,200))
    Image1.exif_data_json()

