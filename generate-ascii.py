import time
import argparse
from PIL import Image
# This is the main block of code that runs every time someone runs our
# script from the command line.
#

global our_width 
our_width = 58

def main():
    args = parse_args()
    img = load_image(args.image_filename)
    frame = convert_image(img, args.reverse)
    frames = [frame]  # Can change this later to add animations.
    if args.fadein: 
        frames = fadein(img, args.reverse)	
    display_frames(frames)

def fadein(img, reverse):
    print "Fading in..."
    frames = []
    divisionValue = 250
    for i in range(24):
        print divisionValue
        frame = convert_image(img, reverse, divisionValue) 
        divisionValue -= 10
        frames.append(frame)
    return frames
    

# Load an image from a file, process it, and return to caller.
#
# FIXTHIS 
def load_image(filename):
    print "Loading image file: " + filename
    new_img = Image.open(filename)
    width, height = new_img.size 
    new_height = our_width
    new_image = new_img.resize((our_width, new_height))
    new_image = new_image.convert("L")
    return new_image 

# Convert image to ASCII, and return ASCII string to caller.  If the
# 'reverse' variable is set to be true, then use the inverse
# conversion where darks become lights and vice versa. 
#
# FIXTHIS
def convert_image(img, reverse=False, divisionValue=13):
   #charlist = ['#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.'] 
    charlist = ['#','@', '&', '$', '%', 'A', 'X', '+', '!', '<', '*', '^', '"', '=', '~', '-',':', '`', ',' , '.']
    if reverse: 
        print "(Conversion will be done in reverse.)"
        charlist = list(reversed(charlist))
    pixelValues = list(img.getdata())  
    pixelChars = []
    for value in pixelValues:
        pixelChars.append(charlist[value/divisionValue])
    return pixelChars  #A list of characters. 

# Given a list of frames represented by ASCII strings, print each
# frame in the list to the screen in order, pausing for 500ms between
# each frame.

def display_frames(frames):
    print "Displaying " + str(len(frames)) + " frames; press [Enter] to start."
    raw_input("")
    for frame in frames:
        display_frame(frame) 
        time.sleep(0.5)

def display_frame(frame):    
    global our_width 
    for i in range(0, len(frame), our_width):
        line = frame[i:i+our_width]
        print ''.join(line)
	
# Helper function for parsing command line arguments. 
#
def parse_args():
    parser = argparse.ArgumentParser(description='Generate ASCII Art from Images')

    parser.add_argument('image_filename', type=str,
                        help='file containing image')
    parser.add_argument('-r', '--reverse', action='store_true',
                        help='reverse the colors of the image')
    parser.add_argument('-i', '--fadein', action='store_true',
                        help='animate image to fade in from darkness')
    parser.add_argument('-o', '--fadeout', action='store_true',
                        help='animate image to fade out to darkness')
    parser.add_argument('-s', '--scroll', action='store_true',
                        help='animate image to scroll horizontally')
    parser.add_argument('-m', '--morph', nargs=1, type=str,
                        help='animate image morphing into second given image')
    return parser.parse_args()

# Check whether someone is actually running our script from the command line
# (rather than simply importing it as a module.)
#
if __name__ == "__main__":
    main()







