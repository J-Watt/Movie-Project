#-------------------------------------------------------------------------------
# Name:         fresh_tomatoes
# Purpose:      Generates html file using properties from Movie objects
#
# Author:       Udacity
# Modified by:  Jordan Alexander Watt
# Modified On:  16-10-2015
#-------------------------------------------------------------------------------

import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        .page-content {
            padding-top: 80px;
            padding-bottom: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            min-width: 300px;
            margin-bottom: 20px;
            padding: 20px 0px 20px 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
        }
        .movie-poster {
            padding: 0px;
        }
        .movie-poster:hover {
            cursor: pointer;
        }
        .movie-text ul {
            display: inline-block;
            text-align: left;
        }
        .movie-text a {
            display: block;
        }
        .navbar-default {
            background-color: #285149;
            border-color: #0d3831;
        }
        .navbar-default .navbar-brand {
            color: #becdd6;
        }
        .navbar-default .navbar-brand:hover, .navbar-default .navbar-brand:focus {
            color: #8ba7cc;
        }
        .btn-default {
            display: block;
            margin: auto;
            background-color: inherit;
        }
        .btn-default:focus {
            background-color: inherit;
        }
        #footer {
            height: 60px;
            background-color: #EEE;
        }
        #footer p {
         margin-top: 20px;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-poster', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads and collapsing buttons
        $(document).ready(function () {
            $('.movie-tile').hide().first().show(375, function showNext() {
                $(this).next("div").show(375, showNext);
            });
            $('.movie-text .btn').on('click', function(e) {
                e.preventDefault();
                var $this = $(this);
                var $collapse = $this.closest('.collapse-group').find('.collapse');
                $collapse.collapse('toggle');
                $this.find('span').toggleClass('glyphicon-menu-down glyphicon-menu-up');
            });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
<body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="navbar navbar-default navbar-fixed-top" role="navigation">
        <div class="container-fluid">
            <div class="navbar-header">
                <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
            </div>
        </div>
    </div>

    <div class="page-content">
        <div class="container">

            <!-- Movie instances -->
                {movie_tiles}
        </div>
    </div>
    <div id="footer">
        <div class="container">
            <p class="text-muted text-center"><a href="http://www.udacity.com" target="_blank">Udacity</a> Nanodegree Project One by <a href="README.txt">Jordan A Watt</a>.</p>
        </div>
    </div>
</body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
            <div class="col-md-6 col-lg-4 movie-tile">
                <div class="row">
                    <div class="col-xs-4 movie-poster" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
                        <img class="pull-right" src="{poster_image_url}" width="121" height="188">
                    </div>
                    <div class="col-xs-8 movie-text text-center collapse-group">
                        <h2>{movie_title}</h2>
                        <button type="button" class="btn btn-default"><span class="glyphicon glyphicon-menu-down"></span></button>
                        <p class="collapse">{movie_synopsis}</p>
                        <ul>Starring:
                            {cast_list}
                        </ul>
                        <a href="{imdb_url}" target="_blank">More info!</a>
                    </div>
                </div>
            </div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Compile cast list items into a string
        cast_list = ""
        for star in movie.cast_list:
            cast_list += "<li>"+star+"</li>"

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            movie_synopsis=movie.movie_synopsis,
            imdb_url=movie.imdb_url,
            trailer_youtube_id=trailer_youtube_id,
            cast_list=cast_list
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
