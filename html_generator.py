import os, os.path
import re

# js file
js_functions = '''
// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $("#trailer-video-container").empty();
});

// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.movie-tile', function (event) {
    var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
    var sourceUrl = 'https://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
    $("#trailer-video-container").empty().append($("<iframe></iframe>", {
      'id': 'trailer-video',
      'type': 'text-html',
      'src': sourceUrl,
      'frameborder': 0
    }));
});

// Animate in the movies when the page loads
$(document).ready(function () {
  $('.movie-tile').hide().first().show("fast", function showNext() {
    $(this).next("div").show("fast", showNext);
  });
});
'''

# css file generator
css_style = '''
body {
	padding-top: 80px;
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
	margin-bottom: 20px;
	padding-top: 20px;
}

.movie-tile:hover {
	background-color: #EEE;
	cursor: pointer;
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

.footer, .push {
  height: 155px;
	background-color: #EEE;
}
'''

# html file generator
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="X-UA-Compatible" content="chrome=1" charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <title>Films to watch</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css">
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="css/films.css">
    <script src="js/films.js"></script>
</head>
'''

main_page_content = '''
  <body>
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
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Films to watch</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
	<footer class="footer">
		<div class="container">
			<p class="navbar-text navbar-center">Made by <a href="https://github.com/leogregianin">Leonardo Gregianin</a> 2017</p>
		</div>
	</footer>
  </body>
</html>
'''

movie_tile_content = u'''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
	<h2>{movie_title}</h2>
    <h5>{movie_storyline}</h5>
</div>
'''


def create_movie_tiles_content(movies):
    content = ''
    for movie in movies:
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match else None)

        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    
    # create sub-dir
    if not os.path.exists('output'):
      os.makedirs('output')

    # Create or overwrite the output js file
    if not os.path.exists('output/js'):
      os.makedirs('output/js')
    js_file = open('output/js/films.js', 'w')
    js_file.write(js_functions)
    js_file.close()

    # Create or overwrite the output css file
    if not os.path.exists('output/css'):
      os.makedirs('output/css')
    css_file = open('output/css/films.css', 'w')
    css_file.write(css_style)
    css_file.close()

    # Create or overwrite the output html file
    output_file = open('output/index.html', 'w')

    rendered_content = main_page_content.format(
      movie_tiles=create_movie_tiles_content(movies))

    output_file.write(main_page_head + rendered_content)
    output_file.close()
