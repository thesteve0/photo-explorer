'''
We are not using this today in the talk because I already loaded up the data (not much fun to watch).
That said, I think this is an important example of how to import your own photos into FiftyOne
'''

from doctest import debug
from pathlib import Path

import fiftyone as fo
import exifread


# this is the name the for the dataset inside fiftyone
NAME = "photo_album"

# this is the path where the images are located
# It assume all images are in one directory
SOURCE_IMAGE_DIR = "/your/photo/directory"



# according to the doc it will read any image that has an image mim-type and ignore the rest
# it will go recuresively down through directories
def simple_import_and_create():
    # Create the dataset. If we don't care about any of the EXIF data or unique information per photo, this one works with a directory of images.
    dataset = fo.Dataset.from_dir(
        dataset_dir=SOURCE_IMAGE_DIR,
        dataset_type=fo.types.ImageDirectory,
        compute_metadata=True,
        name=NAME,
    )

def import_and_create_with_fields():

    # Create an empty dataset and we want it to persist between sessions in FiftyOne
    dataset = fo.Dataset(NAME, overwrite=True, persistent=True)

    relevant_exif_fields = ["Image Model", "EXIF ExposureTime", "EXIF FNumber", "EXIF DateTimeOriginal", "EXIF ShutterSpeedValue",
                            "EXIF ApertureValue", "EXIF Flash", "EXIF SensingMethod", "EXIF SubjectDistance", "EXIF FocalLength"]

    path = Path(SOURCE_IMAGE_DIR)

    # This will hold all the FiftyOne sample objects we create from the images
    samples = []

    # Most Computer Vision libraries do not work with HEIC or RAW formats. I already converted them all to JPEGs
    for sample_file in path.rglob('*.JPG'):
        exif_fields = {}

        # Open the image file to read as a binary
        f = open(sample_file, 'rb')

        try:
            tags = exifread.process_file(f, details=False)
            # Gather up all the valid exif fields
            for field in relevant_exif_fields:
                if field in relevant_exif_fields and tags.get(field) is not None:
                    exif_fields[field] = str(tags.get(field))

            # We have built our dict of exif info. Time to make the sample
            # Each exif tag will end up as a separate field on the sample
            sample = fo.Sample(filepath = sample_file, **exif_fields)

            # Now add that sample to the list of samples
            samples.append(sample)
        except:
            print("The file: " + str(sample_file) +  " the follow exif data threw an exception" + str(tags))
            pass
        f.close()

    # We have gone through all the files and created a List of samples. Time to add them to the dataset
    dataset.add_samples(samples)

    # We always need to call save on a dataset when we change any of the values
    dataset.save()


# This is how we launch the app from code
def start_fiftyone():
    dataset = fo.load_dataset(NAME)
    session = fo.launch_app(dataset)

    # We keep the session open so the app doesn't close. This means this program won't exit unless we signal a break
    session.wait(-1)

    # To delete the dataset
    # https://docs.voxel51.com/user_guide/using_datasets.html#deleting-a-dataset

if __name__ == "__main__":
    print("reading in data")
    import_and_create_with_fields()
    #start_fiftyone()
    print("done")
