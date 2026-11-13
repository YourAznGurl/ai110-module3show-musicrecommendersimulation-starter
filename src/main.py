"""
Command line runner for the Music Recommender Simulation.
"""

from src.recommender import load_songs, recommend_songs


def show_results(name, user_prefs, songs):
    """Prints the top 5 songs for one user profile."""
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(f"\n=== {name} ===")
    print(f"Profile: {user_prefs}\n")

    # enumerate() counts the loop, starting at 1, so we can number results
    for number, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{number}. {song['title']} by {song['artist']} - Score: {score:.2f}")
        print(f"   Because: {explanation}")
    print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    # each profile is a dictionary of the user's taste
    profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.85},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.35},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.92},
        # edge case: high energy but a sad mood, which rarely go together
        "Conflicted (edge case)": {"genre": "folk", "mood": "sad", "energy": 0.9},
    }

    # loop through the dictionary: name = the key, prefs = the value
    for name, prefs in profiles.items():
        show_results(name, prefs, songs)


if __name__ == "__main__":
    main()