from PIL import Image

# # First, I convert my photo and watermark to RGBA:
# image = Image.open(photo_image_path).convert('RGBA')
# watermark = Image.open(watermark_image_path).convert('RGBA')

# # then I сreate an empty layer with the same size as image
# # and put watermark in x/y position
# layer = Image.new('RGBA', image.size, (0, 0, 0, 0))
# layer.paste(watermark, (x, y))

# # then add transparency 
# layer.putalpha(128)

# # and merge image with logo
# result = Image.alpha_composite(image, layer)


# # Read the two images
# # baseRoute = 'C:\Users\ASUS-TUF\Downloads'
# image1 = Image.open("C:\\Users\\ASUS-TUF\\Downloads\\night_mountains.png")
# image2 = Image.open("C:\\Users\\ASUS-TUF\\Downloads\\droplets_on_feather.png")

# #resize, first image
# image2 = image2.resize(image1.size)

# # Create a new image with an alpha channel
# image2_with_alpha = Image.new("RGBA", image1.size)
# # Paste the second image onto the alpha image
# image2_with_alpha.paste(image2, (0, 0))
# # Set the transparency level (adjust the alpha value as needed)
# alpha = 128  # This sets the second image to be semi-transparent
# image = Image.alpha_composite(image1.convert("RGBA"), image2_with_alpha)
# # Save or display the merged image
# image.save("merged_image.png")
# image.show()



# Read the two images
image1 = Image.open("C:\\Users\\ASUS-TUF\\Downloads\\night_mountains.png")
image2 = Image.open("C:\\Users\\ASUS-TUF\\Downloads\\droplets_on_feather.png")

# Resize the second image to match the size of the first image
image2 = image2.resize(image1.size)

# Create a new image with an alpha channel
image2_with_alpha = Image.new("RGBA", image1.size)

# Paste the second image onto the alpha image
image2_with_alpha.paste(image2, (0, 0))

# Set the transparency level (adjust the alpha value as needed)
alpha = 128  # This sets the second image to be semi-transparent

# Composite the images
merged_image = Image.alpha_composite(image1.convert("RGBA"), image2_with_alpha)
# Save the merged image as PNG
merged_image.save("merged_image.png")
merged_image.show()

# # Convert the merged image to RGB color mode (JPEG doesn't support alpha)
# merged_image_rgb = merged_image.convert("RGB")
# # Save the merged image as JPEG
# merged_image_rgb.save("merged_image.jpg")  # Output as JPEG

# Display the merged image
# merged_image_rgb.show()