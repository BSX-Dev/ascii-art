import argparse

# This is the main block of code that runs every time someone runs our
# script from the command line.
#
def main():
    args = parse_args()
    img = load_image(args.image_filename)
    frame = convert_image(img, args.reverse)
    frames = [frame]  # Can change this later to add animations.
    display_frames(frames)

# Load an image from a file, process it, and return to caller.
#
# FIXTHIS 
def load_image(filename):
    print "Loading image file: " + filename
    #...
    return "FIXTHIS"

# Convert image to ASCII, and return ASCII string to caller.  If the
# 'reverse' variable is set to be true, then use the inverse
# conversion where darks become lights and vice versa. 
#
# FIXTHIS
def convert_image(img, reverse=False):
    print "Converting image."
    if reverse:
        print "(Conversion will be done in reverse.)"
        #...
    #...
    return "FIXTHIS"

# Given a list of frames represented by ASCII strings, print each
# frame in the list to the screen in order, pausing for 500ms between
# each frame.
#
def display_frames(frames):
    print "Displaying " + str(len(frames)) +
    " frames; press [Enter] to start."
    #...


# Helper function for parsing command line arguments. 
#
def parse_args():
    parser = argparse.ArgumentParser(description='Generate ASCII Art from Images')

    parser.add_argument('image_filename', type=str,
                        help='file containing image')
    parser.add_argument('-r', '--reverse', action='store_true',
                        help='reverse the colors of the image')
    parser.add_argument('-i', '--fade-in', action='store_true',
                        help='animate image to fade in from darkness')
    parser.add_argument('-o', '--fade-out', action='store_true',
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







