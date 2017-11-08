"""Spins up a Movie Trailer Website

Movie data is hardcoded in media_data py file and imported from such
Html builder is from fresh_tomatoes py file and leverages data from media data to
generate site
"""

from media_data import *
import fresh_tomatoes

fresh_tomatoes.open_movies_page(movies)
