import socket
from waveshare_epd import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont

# Initialize e-Paper display
epd = epd2in13_V2.EPD()

# Define font size
FONT_SIZE = 12

# Define font
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', FONT_SIZE)

def get_ip_address():
    # Get IP address of the current network interface
    try:
        # Create a socket connection to a remote host (Google DNS)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        print(f"Error retrieving IP address: {e}")
        return None

def display_ip_address(ip_address):
    # Create new image with white background (landscape orientation)
    image = Image.new('1', (epd.height, epd.width), 255)
    draw = ImageDraw.Draw(image)

    # Clear display
    epd.init(epd.FULL_UPDATE)
    epd.displayPartBaseImage(epd.getbuffer(image))

    # Draw IP address on the display with specified font size
    draw.text((10, 10), "IP Address:", font=font, fill=0)
    draw.text((10, 30), ip_address, font=font, fill=0)

    # Rotate the image 90 degrees clockwise
    image = image.rotate(90, expand=True)

    # Display rotated image on the e-Paper display
    epd.init(epd.FULL_UPDATE)
    epd.display(epd.getbuffer(image))

    # Sleep to conserve power
    epd.sleep()

def main():
    # Get IP address
    ip_address = get_ip_address()
    if ip_address:
        # Display IP address on the e-Paper display
        display_ip_address(ip_address)

if __name__ == '__main__':
    main()
