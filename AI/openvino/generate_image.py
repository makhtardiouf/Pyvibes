
from optimum.intel.openvino import OVStableDiffusionPipeline

# Uncomment if the image wasn't already downloaded
# model_id = "echarlaix/stable-diffusion-v1-5-openvino"
# pipeline = OVStableDiffusionPipeline.from_pretrained(model_id, safety_checker=None)
#
prompt = "sailing ship in storm by Rembrandt"
# images = pipeline(prompt).images

# PyTorch model
model_id = "runwayml/stable-diffusion-v1-5"
pipeline = OVStableDiffusionPipeline.from_pretrained(model_id, export=True, safety_checker=None)
images = pipeline(prompt).images

pipeline.save_pretrained("openvino-local-sd-v1.5")

# model_id = "openvino-local-sd-v1.5"
# pipeline = OVStableDiffusionPipeline.from_pretrained(model_id)

# Define the shapes related to the inputs and desired outputs
batch_size, num_images, height, width = 1, 1, 512, 512
# Statically reshape the model
pipeline.reshape(batch_size=batch_size, height=height, width=width, num_images_per_prompt=num_images)
# Compile the model before the first inference
pipeline.compile()

# Run inference
images = pipeline(prompt, height=height, width=width, num_images_per_prompt=num_images).images
images.save("ai_sailingship.png")
