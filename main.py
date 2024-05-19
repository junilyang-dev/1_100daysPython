import requests

movie_ids = [
    238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430
]

for movie_id in movie_ids:
    url = f"https://nomad-movies.nomadcoders.workers.dev/movies/{movie_id}"
    response = requests.get(url)
    movie_data = response.json()
    print(
        "title : ",movie_data["title"],
        "\n overview : " ,movie_data["overview"], 
        "\n vote_average : ",movie_data["vote_average"],
        "\n -----------------------------------------------"
        )