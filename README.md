# 🎵 Music Recommender Simulation

## Project Summary

This project is a small content-based music recommender. It compares each
song's genre, mood, and energy to a user's taste profile, gives every song a
score, and returns the top matches along with the reasons for each score.

---

## How The System Works

Real apps like Spotify use two ideas: collaborative filtering (recommending
what similar users liked) and content-based filtering (recommending songs
whose attributes are similar to ones you like). My version only uses
content-based filtering, because I have no other users' data.

**What features does each Song use?**
Each song has genre, mood, energy, tempo, valence, danceability, and
acousticness. My scoring only uses genre, mood, and energy.

**What information does the UserProfile store?**
A favorite genre, a favorite mood, and a target energy level (0.0 to 1.0).

**How does the Recommender compute a score for each song?**
- +2.0 points if the song's genre matches
- +1.0 point if the song's mood matches
- Up to +1.0 point for energy closeness: 1 - |song energy - target energy|

Every score also comes with a list of reasons, so the user can see why a
song was picked.

**How do you choose which songs to recommend?**
The program scores every song in the catalog, sorts them from highest to
lowest score, and returns the top k.

**Expected bias:** Genre is worth the most points, so a song with the wrong
genre but a perfect mood and energy can rank below a weaker song in the
right genre.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   python -m src.main
   ```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Output from running `python -m src.main` with four profiles, using the
original weights (genre 2.0, mood 1.0, energy up to 1.0):

```
Loading songs from data/songs.csv...
Loaded songs: 18

=== High-Energy Pop ===
Profile: {'genre': 'pop', 'mood': 'happy', 'energy': 0.85}

1. Sunrise City by Neon Echo - Score: 3.97
   Because: genre match (+2.0), mood match (+1.0), energy closeness (+0.97)
2. Gym Hero by Max Pulse - Score: 2.92
   Because: genre match (+2.0), energy closeness (+0.92)
3. Rooftop Lights by Indigo Parade - Score: 1.91
   Because: mood match (+1.0), energy closeness (+0.91)
4. Storm Runner by Voltline - Score: 0.94
   Because: energy closeness (+0.94)
5. Concrete Crown by Kid Atlas - Score: 0.93
   Because: energy closeness (+0.93)


=== Chill Lofi ===
Profile: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.35}

1. Library Rain by Paper Lanterns - Score: 4.00
   Because: genre match (+2.0), mood match (+1.0), energy closeness (+1.00)
2. Midnight Coding by LoRoom - Score: 3.93
   Because: genre match (+2.0), mood match (+1.0), energy closeness (+0.93)
3. Focus Flow by LoRoom - Score: 2.95
   Because: genre match (+2.0), energy closeness (+0.95)
4. Spacewalk Thoughts by Orbit Bloom - Score: 1.93
   Because: mood match (+1.0), energy closeness (+0.93)
5. Coffee Shop Stories by Slow Stereo - Score: 0.98
   Because: energy closeness (+0.98)


=== Deep Intense Rock ===
Profile: {'genre': 'rock', 'mood': 'intense', 'energy': 0.92}

1. Storm Runner by Voltline - Score: 3.99
   Because: genre match (+2.0), mood match (+1.0), energy closeness (+0.99)
2. Gym Hero by Max Pulse - Score: 1.99
   Because: mood match (+1.0), energy closeness (+0.99)
3. Pulse Festival by Arc Nova - Score: 0.97
   Because: energy closeness (+0.97)
4. Iron Skyline by Blackforge - Score: 0.95
   Because: energy closeness (+0.95)
5. Sunrise City by Neon Echo - Score: 0.90
   Because: energy closeness (+0.90)


=== Conflicted (edge case) ===
Profile: {'genre': 'folk', 'mood': 'sad', 'energy': 0.9}

1. Rainy Window by Oak & Ember - Score: 3.35
   Because: genre match (+2.0), mood match (+1.0), energy closeness (+0.35)
2. Storm Runner by Voltline - Score: 0.99
   Because: energy closeness (+0.99)
3. Gym Hero by Max Pulse - Score: 0.97
   Because: energy closeness (+0.97)
4. Pulse Festival by Arc Nova - Score: 0.95
   Because: energy closeness (+0.95)
5. Iron Skyline by Blackforge - Score: 0.93
   Because: energy closeness (+0.93)
```

---

## Experiments You Tried

**Weight shift:** I halved the genre weight (2.0 → 1.0) and doubled the
energy weight (max 1.0 → 2.0). The mood weight stayed at 1.0. The output
above uses the original weights. The output below uses the shifted weights.

```
=== High-Energy Pop ===
Profile: {'genre': 'pop', 'mood': 'happy', 'energy': 0.85}

1. Sunrise City by Neon Echo - Score: 3.94
   Because: genre match (+1.0), mood match (+1.0), energy closeness (+1.94)
2. Gym Hero by Max Pulse - Score: 2.84
   Because: genre match (+1.0), energy closeness (+1.84)
3. Rooftop Lights by Indigo Parade - Score: 2.82
   Because: mood match (+1.0), energy closeness (+1.82)
4. Storm Runner by Voltline - Score: 1.88
   Because: energy closeness (+1.88)
5. Concrete Crown by Kid Atlas - Score: 1.86
   Because: energy closeness (+1.86)


=== Chill Lofi ===
Profile: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.35}

1. Library Rain by Paper Lanterns - Score: 4.00
   Because: genre match (+1.0), mood match (+1.0), energy closeness (+2.00)
2. Midnight Coding by LoRoom - Score: 3.86
   Because: genre match (+1.0), mood match (+1.0), energy closeness (+1.86)
3. Focus Flow by LoRoom - Score: 2.90
   Because: genre match (+1.0), energy closeness (+1.90)
4. Spacewalk Thoughts by Orbit Bloom - Score: 2.86
   Because: mood match (+1.0), energy closeness (+1.86)
5. Coffee Shop Stories by Slow Stereo - Score: 1.96
   Because: energy closeness (+1.96)


=== Deep Intense Rock ===
Profile: {'genre': 'rock', 'mood': 'intense', 'energy': 0.92}

1. Storm Runner by Voltline - Score: 3.98
   Because: genre match (+1.0), mood match (+1.0), energy closeness (+1.98)
2. Gym Hero by Max Pulse - Score: 2.98
   Because: mood match (+1.0), energy closeness (+1.98)
3. Pulse Festival by Arc Nova - Score: 1.94
   Because: energy closeness (+1.94)
4. Iron Skyline by Blackforge - Score: 1.90
   Because: energy closeness (+1.90)
5. Sunrise City by Neon Echo - Score: 1.80
   Because: energy closeness (+1.80)


=== Conflicted (edge case) ===
Profile: {'genre': 'folk', 'mood': 'sad', 'energy': 0.9}

1. Rainy Window by Oak & Ember - Score: 2.70
   Because: genre match (+1.0), mood match (+1.0), energy closeness (+0.70)
2. Storm Runner by Voltline - Score: 1.98
   Because: energy closeness (+1.98)
3. Gym Hero by Max Pulse - Score: 1.94
   Because: energy closeness (+1.94)
4. Pulse Festival by Arc Nova - Score: 1.90
   Because: energy closeness (+1.90)
5. Iron Skyline by Blackforge - Score: 1.86
   Because: energy closeness (+1.86)
```

**What changed:**
- High-Energy Pop: the top 3 stayed the same, but Rooftop Lights (right
  mood, wrong genre) went from far behind Gym Hero to almost tied with it
  (2.82 vs 2.84), because a missing genre now costs less.
- Chill Lofi: the order did not change at all. The scores just got higher.
- Deep Intense Rock: the order stayed the same, but Gym Hero moved much
  closer to the top song (2.98 vs 3.98).
- Conflicted (sad folk at energy 0.9): Rainy Window still came first, even
  though its energy is only 0.25. Genre plus mood (2.0 points) still beat
  the best high-energy songs (1.98).

**Takeaway:** The change made the recommendations different, but not more
accurate. Doubling energy shrank the gaps between songs without fixing the
conflicted profile. To fix it, I would need to lower the genre and mood
weights much further, or only give genre and mood points when the energy is
also close.

---

## Limitations and Risks

- The catalog is tiny (18 songs), so most genres have only one or two songs.
- Genre and mood together are worth up to 3.0 points, but energy is only
  worth 1.0. In my "Conflicted" test (sad folk at high energy), a quiet,
  low-energy song ranked first because it matched genre and mood.
- Once a user's genre and mood matches run out, the rest of the list is
  chosen only by energy, so unrelated genres show up in positions 3-5.
- It ignores lyrics, language, tempo, and everything else about a song.

---

## Reflection

Read and complete [`model_card.md`](model_card.md).

I learned that a recommender can be very simple and still feel smart. Adding
up a few points for genre, mood, and energy closeness was enough to produce
lists that matched my intuition, and the "reasons" list made it easy to see
exactly why each song ranked where it did. The experiment showed me that
changing the weights changes the scores more than it changes the winners.

Bias can show up in the choices a designer makes. I gave genre the most
points, so users who like unusual genres only get one or two good matches
before the list fills up with unrelated songs. A small catalog and made-up
labels like "mood" make this worse, because the system can only recommend
what it was given.