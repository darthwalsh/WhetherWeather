from PIL import Image, ImageDraw

width, height = 600, 200
image = Image.new('RGB', (width, height), 'white')

# Draw a black circle
draw = ImageDraw.Draw(image)
circle_radius = 50
circle_center = (width // 2, height // 2)
draw.ellipse(
    (circle_center[0] - circle_radius, circle_center[1] - circle_radius,
     circle_center[0] + circle_radius, circle_center[1] + circle_radius),
    fill='black'
)

# Save the image
image.save('black_circle.png')
