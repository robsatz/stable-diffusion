import os
from PIL import Image

identifier = 'gerhardsatz'
id_class = 'man'
parent_dir = 'training_samples'
src_dir = 'src' # folder containing source images
extensions = ('.jpg', '.JPG', '.png', '.HEIC')

src_path = os.path.join(parent_dir, src_dir)
i = 1
for filename in os.listdir(src_path):
    if filename.endswith(extensions):
        im = Image.open(os.path.join(src_path, filename))
        new_filename = os.path.join(parent_dir, id_class, f'{identifier} {id_class}_{str(i).zfill(3)}.png')
        im.save(new_filename)
        i += 1
