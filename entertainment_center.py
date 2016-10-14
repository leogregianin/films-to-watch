import media
import html_generator

sal_terra = media.Movie("O Sal da Terra",
	"O fotógrafo brasileiro Sebastião Salgado viaja a 40 anos através dos continentes aos passos de uma humanidade sempre em mutação. O filme retrata esta história. Uma homenagem à beleza do planeta.",
	"https://raw.githubusercontent.com/leogregianin/films-to-watch/master/poster/sal-terra.jpg?token=ABmyVfW2WjKPjsbPX0gzarr7PhCRqShOks5YCXskwA%3D%3D",
	"https://www.youtube.com/watch?v=dT7wv2HSkYE")

ensaio_cegueira = media.Movie("Ensaio sobre a Cegueira",
	"Filme baseado no livro de mesmo nome do autor português José Saramago.",
	"https://raw.githubusercontent.com/leogregianin/films-to-watch/master/poster/cegueira.jpg?token=ABmyVeck95D7CCf0QaDT4emLTdUV7Dqrks5YCXsLwA%3D%3D",
	"https://www.youtube.com/watch?v=J6oW64PrmUM")

sobral_pinto = media.Movie("Sobral: O Homem que não tinha Preço",
	"Documentário sobre a história da vida de um dos mais emblemáticos advogados brasileiros Sobral Pinto.",
	"https://raw.githubusercontent.com/leogregianin/films-to-watch/master/poster/sobral.jpg?token=ABmyVUEXEplYDtxUzYsl6pYk2kQEey5uks5YCXs4wA%3D%3D",
	"https://www.youtube.com/watch?v=xvU4NGJ7CMk")

movies = [sal_terra, ensaio_cegueira, sobral_pinto]
html_generator.open_movies_page(movies)
