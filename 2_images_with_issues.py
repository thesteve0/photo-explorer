import fiftyone as fo
import fiftyone.operators as foo


dataset = fo.load_dataset("photo-album")

### Load the operators from the plugin
compute_brightness = foo.get_operator("@jacobmarks/image_issues/compute_brightness")
compute_blurriness = foo.get_operator("@jacobmarks/image_issues/compute_blurriness")
compute_noise = foo.get_operator("@jacobmarks/image_issues/compute_salt_and_pepper")

compute_brightness(dataset)
compute_blurriness(dataset)
compute_noise(dataset)

# session = fo.launch_app(dataset)
# session.wait(-1)


