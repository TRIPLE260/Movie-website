from flask import Flask, render_template

app = Flask(__name__)

# Movie Data (For now, later we can connect to a database)
movies = [
    {"title": "Cascade (2023)", "image": "cascade-hollywood-movie.jpg", "link": "https://nkiri.com"},
    {"title": "Guardians of the Galaxy Vol.3", "image": "Guardians-of-the-Galaxy-Vol.-3-hollywood-movie.jpg", "link": "https://nkiri.com"},
    {"title": "Money Heist S05", "image": "money-heist-s05-poster-691x1024.jpg", "link": "https://nkiri.com"},
    {"title": "Spider-Man No Way Home", "image": "spider-man-no-way-home-hollywood-movie.jpg", "link": "https://nkiri.com"},
    {"title": "The King's Man", "image": "the-kings-man-hollywood-movie.jpg", "link": "https://nkiri.com"},
    {"title": "The Lost City", "image": "the-lost-city-hollywood-moview.jpg", "link": "https://nkiri.com"},
    {"title": "The Out-Laws", "image": "The-Out-Laws-683x1024.jpg", "link": "https://nkiri.com"},
    {"title": "Warrior Nun S01", "image": "warrior-nun-tv-series.jpg", "link": "https://nkiri.com"}
]

@app.route("/")
def home():
    return render_template("index.html", movies=movies)

if __name__ == "__main__":
    from waitress import serve  # Production-ready server
    serve(app, host="0.0.0.0", port=5000)
