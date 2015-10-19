# ------------------------------------------------------------------------------
# Name:         media
# Purpose:      Creates movie objects for use with entertainemnt_center.py &
#               Fresh_tomatoes.py
#
# Author:       Jordan Alexander Watt
#
# Created:      27-09-2015
# Copyright:    (c) Jordan 2015
# ------------------------------------------------------------------------------

import webbrowser


# Object containing properties relating to film details
class Movie(object):

    def __init__(self, title, movie_synopsis, cast_list, poster_image,
                 trailer_youtube, imdb_url):
        self.title = title
        self.movie_synopsis = movie_synopsis
        self.cast_list = cast_list
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.imdb_url = imdb_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)
