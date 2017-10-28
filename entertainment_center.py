import os, sys
import media
import html_generator
import json

__file__ = 'films.json'

def generator():

	if not os.path.isfile(__file__):
		print("File %s not exist. Exit." % __file__)
		sys.exit(1)
	
	data = json.load(open(__file__))
	movies = []

	for i in range(len(data["films"])):

		data["films"][i]["key"] = media.Movie(
			data["films"][i]["title"],
			data["films"][i]["storyline"],
			data["films"][i]["poster_image_url"],
			data["films"][i]["trailer_youtube_url"])

		movies.append(data["films"][i]["key"])

	html_generator.open_movies_page(movies)

if __name__ == '__main__':
	generator()