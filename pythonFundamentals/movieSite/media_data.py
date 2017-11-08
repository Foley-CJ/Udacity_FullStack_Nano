"""Leverages Movie class from the media class to hardcode data related to
six different movies.Stores these objects into a class called movie.

Udacity Reviewer:  Pep8 guidelines followed except for line length.
                   breaking urls is not an optimal approach.

"""

import media_classes


toyStory = media_classes.Movie("Toy Story",
                               "A story of toys that come to life",
                               "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                               "https://www.youtube.com/watch?v=vwyZH85NQC4")  # noqa

seven = media_classes.Movie("Seven",
                            "The seven deadly sins",
                            "https://upload.wikimedia.org/wikipedia/en/6/68/Seven_%28movie%29_poster.jpg",  # noqa
                            "https://www.youtube.com/watch?v=znmZoVkCjpI")  # noqa

up = media_classes.Movie("Up",
                         "A grand adventure to the sky",
                         "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",  # noqa
                         "https://www.youtube.com/watch?v=qas5lWp7_R0")  # noqa

blindSide = media_classes.Movie("The Blind Side",
                                "Football changes lives",
                                "https://upload.wikimedia.org/wikipedia/en/6/60/Blind_side_poster.jpg",  # noqa
                                "https://www.youtube.com/watch?v=gvqj_Tk_kuM")  # noqa

rudy = media_classes.Movie("Rudy",
                           "Notre Dame football",
                           "https://upload.wikimedia.org/wikipedia/en/2/29/Rudy2.jpg",  # noqa
                           "https://www.youtube.com/watch?v=eDKOlH0I0nQ")  # noqa

ladder49 = media_classes.Movie("Ladder 49",
                               "Warehouse fire gone bad",
                               "https://upload.wikimedia.org/wikipedia/en/f/f8/Ladder_49_poster.JPG",  # noqa
                               "https://www.youtube.com/watch?v=76Wgm28hUpg")  # noqa


movies = [toyStory, seven, up, blindSide, rudy, ladder49]
