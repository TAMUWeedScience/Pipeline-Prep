import PIL
from PIL import Image, TiffImagePlugin
from PIL.ExifTags import TAGS
import json

class Image_resize_exifdata:
	#function to resize
    def resize_image(new_size, file_path):
        #use Image.open to open the image in PIL's Image module
        image = Image.open(file_path)

        #use .resize to resize the image and save it
        img_rs = image.resize((new_size))
        img_rs.save("image_resized.jpeg")

	
    def exif_data_json(file_path):
        image = Image.open(file_path)
       
        # use getexif() to get exif data (https://medium.com/geekculture/extract-exif-data-from-photos-using-python-440e598274f1)
        # use TAGS.get in a for loop to write into an empty dictionary
        # exif_table={}
        # for k, v in image.getexif().items():
        #     tag=TAGS.get(k)
        #     exif_table[tag]=v
        #THIS SIMPLER METHOD DIDN'T WORK USING json.dump. Error:IFDRational is not JSON serializable

        #So, found a solution here: https://github.com/python-pillow/Pillow/issues/6199
        # (i bet there is a simpler way to do this)
        
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
        with open("exif_data.json", "w") as json_data:
            json.dump(exif_table, json_data)


Image1 = Image_resize_exifdata()
Image_resize_exifdata.resize_image((200,200), "rambo.jpeg")
Image_resize_exifdata.exif_data_json("rambo.jpeg")