# ------------------------------------------------------------------------------
# Name:         entertainment_center
# Purpose:      Creates list of Movie objects using static properites provided
#
# Author:       Jordan Alexander Watt
#
# Modified:     16-10-2015
# Created:      27-09-2015
# Copyright:    (c) Jordan 2015
# ------------------------------------------------------------------------------

import media
import fresh_tomatoes


# Creates Movie instances using the provided properties
jurassic_park = media.Movie("Jurassic Park",
                            "Based on the novel by 'Michael Crichton'. An "
                            "amusment park with a prehistoric twist!",
                            ["Sam Neill", "Laura Dern", "Jeff Goldblum"],
                            "https://upload.wikimedia.org/wikipedia"
                            "/en/e/e7/Jurassic_Park_poster.jpg",
                            "https://youtu.be/lc0UehYemQA",
                            "http://www.imdb.com/title/tt0107290/")

i_am_legend = media.Movie("I Am Legend",
                          "One man and his dog must survive the post-"
                          "apocalyptic city by day and hide away by night",
                          ["Will Smith"], "https://upload.wikimedia.org/"
                          "wikipedia/en/d/df/I_am_legend_teaser.jpg",
                          "https://youtu.be/dtKMEAXyPkg",
                          "http://www.imdb.com/title/tt0480249/")

inception = media.Movie("Inception",
                        "Technology to enter peoples dreams enables the "
                        "dangerous prospect of stealing or even planting "
                        "ideas",
                        ["Leonardo DiCaprio", "Joseph Gordon-Levitt",
                         "Ellen Page"],
                        "https://upload.wikimedia.org/wikipedia/en/7/7f/"
                        "Inception_ver3.jpg", "https://youtu.be/8hP9D6kZseM",
                        "http://www.imdb.com/title/tt1375666/")

five_hundred = media.Movie("500 Days of Summer",
                           "A romantic story about a relationship over 500 "
                           "days.",
                           ["Zooey Deschanel", "Joseph Gordon-Levitt"],
                           "https://upload.wikimedia.org/wikipedia/en/d/d1/"
                           "Five_hundred_days_of_summer.jpg",
                           "https://youtu.be/PsD0NpFSADM",
                           "http://www.imdb.com/title/tt1022603/")

safety_not_garanteed = media.Movie("Safety Not Garanteed",
                                   "Reporters investigate the truth behind an "
                                   "ad for a time traveling partner.",
                                   ["Aubrey Plaza", "Mark Duplass"],
                                   "https://upload.wikimedia.org/wikipedia/en/"
                                   "3/3a/SafetyNotGuaranteed.jpg",
                                   "https://youtu.be/73jSnAs7mq8",
                                   "http://www.imdb.com/title/tt1862079/")

ten_things = media.Movie("10 Things I Hate About You",
                         "What happens when a girl cannot date until her "
                         "sister, the meanest person in high school, "
                         "finds one?",
                         ["Heath Ledger", "Julia Stiles",
                          "Joseph Gordon-Levitt"],
                         "https://upload.wikimedia.org/wikipedia/en/9/95/10_"
                         "Things_I_Hate_About_You_film.jpg",
                         "https://youtu.be/AWmjzCZr0Jw",
                         "http://www.imdb.com/title/tt0147800/")

cloud_atlas = media.Movie("Cloud Atlas",
                          "Lives spread over countless centuries "
                          "shaping past and future.",
                          ["Tom Hanks", "Halle Berry", "Hugh Grant"],
                          "https://upload.wikimedia.org/wikipedia/en/2/20/"
                          "Cloud_Atlas_Poster.jpg",
                          "https://youtu.be/ByehYal_cCs",
                          "http://www.imdb.com/title/tt1371111/")

spirited_away = media.Movie("Spirited Away",
                            "A girl wanders through the world "
                            "of gods and spirits.",
                            ["Daveigh Chase", "Suzanne Pleshette"],
                            "https://upload.wikimedia.org/wikipedia/en/3/30/"
                            "Spirited_Away_poster.JPG",
                            "https://youtu.be/ByXuk9QqQkk",
                            "http://www.imdb.com/title/tt0245429/")

princess_bride = media.Movie("The Princess Bride",
                             "Not your typical old fashioned love story.",
                             ["Cary Elwes", "Mandy Patinkin", "Robin Wright"],
                             "https://upload.wikimedia.org/wikipedia/en/d/db/"
                             "Princess_bride.jpg",
                             "https://youtu.be/VYgcrny2hRs",
                             "http://www.imdb.com/title/tt0093779/")

# Compiles movie objects into a list to be utilized in fresh_tomatoes.py
movies = [jurassic_park, i_am_legend, inception, five_hundred,
          safety_not_garanteed, ten_things, cloud_atlas, spirited_away,
          princess_bride]

fresh_tomatoes.open_movies_page(movies)
