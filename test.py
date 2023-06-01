from PIL import Image
import requests
from io import BytesIO

# Web URL of the PNG image
url = 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-ZbTizCWiojJBpiXxrIMnD778/user-WgN1akOX6pRly5oh9K9fYm6t/img-OZdIoc8ILTX6uiWBCp7TiPoh.png?st=2023-06-01T11%3A07%3A49Z&se=2023-06-01T13%3A07%3A49Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-05-31T20%3A33%3A01Z&ske=2023-06-01T20%3A33%3A01Z&sks=b&skv=2021-08-06&sig=MWmENZbAEdPC9FDThIszAZ1ld/fiAmRlGPQ6tEOg/w8%3D'

# Send a GET request to fetch the image data
response = requests.get(url)

# Open the image from the response content
image = Image.open(BytesIO(response.content))

# Convert the image to JPEG format
image = image.convert('RGB')

# Save the image as JPEG
image.save('output.jpg', 'JPEG')