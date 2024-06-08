import socket
import netifaces
import time
from waveshare_epd import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont

# Initialize e-Paper display
epd = epd2in13_V2.EPD()

# Define fonts
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 12)

def get_network_info(interface='wlan0'):
    try:
        # Get network information for the specified interface
        if interface in netifaces.interfaces():
            addresses = netifaces.ifaddresses(interface)
            ip_address = addresses[netifaces.AF_INET][0]['addr']
            netmask = addresses[netifaces.AF_INET][0]['netmask']
            gateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
            return ip_address, netmask, gateway
        else:
            print(f"Interface {interface} not found.")
            return None, None, None
    except Exception as e:
        print(f"Error retrieving network information: {e}")
        return None, None, None

def display_network_info(ip_address, netmask, gateway):
    # Create new image with white background (landscape orientation)
    image = Image.new('1', (epd.height, epd.width), 255)
    draw = ImageDraw.Draw(image)

    # Clear display
    epd.init(epd.FULL_UPDATE)
    epd.displayPartBaseImage(epd.getbuffer(image))

    # Draw network information on the display
    draw.text((10, 10), f"IP Address: {ip_address}", font=font, fill=0)
    draw.text((10, 30), f"Subnet Mask: {netmask}", font=font, fill=0)
    draw.text((10, 50), f"Default Gateway: {gateway}", font=font, fill=0)

    # Rotate the image 90 degrees clockwise
    image = image.rotate(90, expand=True)

    # Display rotated image on the e-Paper display
    epd.init(epd.FULL_UPDATE)
    epd.display(epd.getbuffer(image))

    # Sleep to conserve power
    epd.sleep()

def main():

        # Get network information
        ip_address, netmask, gateway = get_network_info()
        if ip_address:
            # Display network information on the e-Paper display
            display_network_info(ip_address, netmask, gateway)

        # Wait for a minute before refreshing the display


if __name__ == '__main__':
    main()






