#Details of Movies are stored which dispalys on a HTML Page
import fresh_tomatoes    #helps in creating HTML page
import media

#Movie Instances created - Can be more than six
manto = media.Movie("Manto",
                    "Manto is a 2018 Indian biographical drama film. The film stars Nawazuddin Siddiqui in the title character of Indo-Pakistani, Urdu author, writer Saadat Hasan Manto.",
                    "https://upload.wikimedia.org/wikipedia/en/d/dc/Manto_film_poster_2017.jpg",
                    "https://www.youtube.com/watch?v=QFbUei2DDhc")

batti_gul_meter_chalu = media.Movie("Batti Gul Meter Chalu",
                                    "The film tells the story of electricity theft in rural India",
                                    "https://upload.wikimedia.org/wikipedia/en/thumb/0/0a/Batti_Gul_Meter_Chalu_Poster.jpg/220px-Batti_Gul_Meter_Chalu_Poster.jpg",
                                    "https://www.youtube.com/watch?v=BoLTSoVPzQ0")

paltan = media.Movie("Paltan",
                     "Paltan is Indian war film based on 1967 Nathu La and Cho La clashes along the Sikkim border after 1962 Sino-Indian War.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/6/64/Paltan_2018.jpg/220px-Paltan_2018.jpg",
                     "https://www.youtube.com/watch?v=4qspiginsaU")

raazi = media.Movie("Raazi",
                    "Film is about an Indian spy married to a Pakistani military officer prior to the Indo-Pakistani War of 1971 on the order of her father.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/2/2f/Raazi_-_Poster.jpg/220px-Raazi_-_Poster.jpg",
                    "https://www.youtube.com/watch?v=YjMSttRJrhA")

stree = media.Movie("Stree",
                    "The film is based on the Indian urban legend, Nale Ba, about a witch who knocks on people's doors at night.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/4/4f/Stree_-_2018_Movie_Poster.jpg/220px-Stree_-_2018_Movie_Poster.jpg",
                    "https://www.youtube.com/watch?v=gzeaGcLLl_A")

sanju = media.Movie("Sanju",
                    "The film follows the life of Bollywood actor Sanjay Dutt, his addiction with drugs, arrest for alleged association with the 1993 Bombay bombings, relationship with his father, comeback in the industry, the eventual drop of charges from bombay blasts, and release after completing his jail term.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/e/e5/Sanju_-_Theatrical_poster.jpg/220px-Sanju_-_Theatrical_poster.jpg",
                    "https://www.youtube.com/watch?v=1J76wN0TPI4")

movies = [manto, batti_gul_meter_chalu, paltan, raazi, stree, sanju]   #Movie Instances in a list
fresh_tomatoes.open_movies_page(movies)   #Opens a webpage on a default browser

print(media.Movie.__doc__)
