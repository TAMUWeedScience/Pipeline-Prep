from pathlib import Path
from PIL import Image


class ImageResize:
    def __init__(self, cfg): #cfg is to access the config.yaml 
        
        #(cfg.general.workdir) is how we call workdir from the config.yaml file
        self.data_dir = str(Path(cfg.paths.workdir)) 
        #input file name
        self.file_path = Path(cfg.paths.file_path)
        # Ouput file name
        self.output_imgpath = Path(self.data_dir, self.file_path.stem  + "_resized.jpeg")
        # newsize of the image
        self.newsize = (cfg.args.newsize1, cfg.args.newsize2)

        """
        It is better to put all pull all configurations in the __init__ method
        example: the image.resize() in functin 'resize_image' needs a new size. It is better
        to define it in the  __init__ method (self.newsize).
        """

    def resize_image(self):

        #use Image.open to open the image in PIL's Image module
        image = Image.open(self.file_path)

        #use .resize to resize the image and save it
        img_rs = image.resize(self.newsize)
        # Retain original image name with "resized" appended
        img_rs.save(self.output_imgpath)
