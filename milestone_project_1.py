MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

movies = []


def movie_info():
  title = input("Enter the movie title: ")
  director = input("Enter the movie director: ")
  year = input("Enter the movie release year: ")

  movies.append({
      'title': title,
      'director': director,
      'year': year
  })
  

def list_movies():
   for movie in movies:
      print(movie['title'])


def find_movie():
   movie_query = input("Enter the movie title: ")
   for movie in movies:
      if movie_query == movie['title']:
         print(f"{movie_query} is in the movie list.  It was directed by {movie['director']}. It was released in {movie['year']}.") 


def menu_selector():
  selection = input(MENU_PROMPT)
  while selection != 'q':
      if selection == "a":
          # pass
          movie_info()
      elif selection == "l":
          # pass
          list_movies()
      elif selection == "f":
          # pass
          find_movie()
      else:
          print('Unknown command. Please try again.')

      selection = input(MENU_PROMPT)

menu_selector()