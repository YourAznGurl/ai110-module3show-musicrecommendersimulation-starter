import csv  # built-in Python tool for reading CSV files
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

# Scoring weights: change these numbers to run experiments
GENRE_WEIGHT = 2.0
MOOD_WEIGHT = 1.0
ENERGY_WEIGHT = 1.0


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"


def load_songs(csv_path: str) -> List[Dict]:
    """Reads songs.csv and returns a list of song dictionaries."""
    print(f"Loading songs from {csv_path}...")
    songs = []  # empty list that will hold every song

    # open the file; "with" closes it automatically when we're done
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)  # turns each row into a dictionary
        for row in reader:  # go through the songs one at a time
            # CSV values are all text, so convert numbers to real numbers
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)  # add this song to the list

    print(f"Loaded songs: {len(songs)}")
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores one song and returns (score, list of reasons)."""
    score = 0.0     # running total of points
    reasons = []    # plain-language notes explaining the score

    # genre match: worth GENRE_WEIGHT points
    if song["genre"] == user_prefs["genre"]:
        score += GENRE_WEIGHT
        reasons.append(f"genre match (+{GENRE_WEIGHT})")

    # mood match: worth MOOD_WEIGHT points
    if song["mood"] == user_prefs["mood"]:
        score += MOOD_WEIGHT
        reasons.append(f"mood match (+{MOOD_WEIGHT})")

    # energy: the closer to the target, the more points
    # abs() turns a negative gap into a positive one
    gap = abs(song["energy"] - user_prefs["energy"])
    energy_points = ENERGY_WEIGHT * (1.0 - gap)
    score += energy_points
    reasons.append(f"energy closeness (+{energy_points:.2f})")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores every song and returns the top k, best first."""
    scored = []  # will hold (song, score, explanation) for every song

    for song in songs:  # judge each song with score_song
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)  # join the reasons into one string
        scored.append((song, score, explanation))

    # sorted() makes a new sorted list; key says "sort by the score"
    # (item[1]); reverse=True puts the highest score first
    ranked = sorted(scored, key=lambda item: item[1], reverse=True)

    return ranked[:k]  # keep only the first k results