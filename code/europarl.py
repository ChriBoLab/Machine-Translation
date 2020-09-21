########################################################################
#
# Functions for downloading the Europarl data-set from the internet
# and loading it into memory. This data-set is used for translation
# between English and most European languages.
#
# http://www.statmt.org/europarl/
#
# Implemented in Python 3.6
#
# Usage:
# 1) Set the variable data_dir with the desired storage directory.
# 2) Determine the language-code to use e.g. "da" for Danish.
# 3) Call maybe_download_and_extract() to download the data-set
#    if it is not already located in the given data_dir.
# 4) Call load_data(english=True) and load_data(english=False)
#    to load the two data-files.
# 5) Use the returned data in your own program.
#
# Format:
# The Europarl data-set contains millions of text-pairs between English
# and most European languages. The data is stored in two text-files.
# The data is returned as lists of strings by the load_data() function.
#
# The list of currently supported languages and their codes are as follows:
#
# bg - Bulgarian
# cs - Czech
# da - Danish
# de - German
# el - Greek
# es - Spanish
# et - Estonian
# fi - Finnish
# fr - French
# hu - Hungarian
# it - Italian
# lt - Lithuanian
# lv - Latvian
# nl - Dutch
# pl - Polish
# pt - Portuguese
# ro - Romanian
# sk - Slovak
# sl - Slovene
# sv - Swedish
#


import os
import download

########################################################################

# Directory where you want to download and save the data-set.
# Set this before you start calling any of the functions below.
data_dir = "data/europarl/"

# Base-URL for the data-sets on the internet.
data_url = "http://www.statmt.org/europarl/v7/"


########################################################################
# Public functions that you may call to download the data-set from
# the internet and load the data into memory.


def maybe_download_and_extract(language_code="el"):
 

    # Create the full URL for the file with this data-set.
    url = data_url + language_code + "-en.tgz"

    download.maybe_download_and_extract(url=url, download_dir=data_dir)


def load_data(english=True, language_code="da", start="", end=""):
    

    if english:
        # Load the English data.
        filename = "europarl-v7.{0}-en.en".format(language_code)
    else:
        # Load the other language.
        filename = "europarl-v7.{0}-en.{0}".format(language_code)

    # Full path for the data-file.
    path = os.path.join(data_dir, filename)

    # Open and read all the contents of the data-file.
    with open(path, encoding="utf-8") as file:
        # Read the line from file, strip leading and trailing whitespace,
        # prepend the start-text and append the end-text.
        texts = [start + line.strip() + end for line in file]

    return texts


########################################################################
