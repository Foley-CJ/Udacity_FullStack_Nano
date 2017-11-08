'''
Building a movie class for our movie website
'''
import webbrowser


class MediaShow:
    """
    Parent Class for TvShow, not used directly in this project, but ideal
    state for refactoring to stem both Movie and TvShow.
    """
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie:
    """
    Object that contains multiple informations related to movies

    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, posterImageUrl, trailerYoutubeUrl):
        self.title = title
        self.story_line = storyline
        self.poster_image_url = posterImageUrl
        self.trailer_youtube_url = trailerYoutubeUrl

    def show_trailer(self):
        webbrowser.open(self.trailerYoutubeUrl)


class TvShow(MediaShow):
    """
    Objet that contains multiple pieces of information related to TvShows

    Parent: MediaShow

    After Refactored-
        Sibling: Movie
    """

    def __init__(self, channel, seasons):
        MediaShow.__init__(self)
        self.channel = channel
        self.seasons = seasons
