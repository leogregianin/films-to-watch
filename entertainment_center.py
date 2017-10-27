import media
import html_generator
import json

data = json.load(open('films.json'))
movies = []

for i in range(len(data["films"])):

	data["films"][i]["key"] = media.Movie(
		data["films"][i]["title"],
		data["films"][i]["storyline"],
		data["films"][i]["poster_image_url"],
		data["films"][i]["trailer_youtube_url"])

	movies.append(data["films"][i]["key"])

html_generator.open_movies_page(movies)
