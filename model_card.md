# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0**

---

## 2. Intended Use

VibeFinder suggests songs from a small catalog based on a user's favorite
genre, favorite mood, and target energy level. It gives the top 5 songs and
a reason for each one.

It assumes the user can describe their taste with one genre, one mood, and
one energy number. This is a classroom project, not a real product. It
should not be used for real users or real music apps.

---

## 3. How the Model Works

Every song gets a score, and the songs with the highest scores are
recommended.

- If the song's genre matches the user's favorite genre, it gets 2 points.
- If the song's mood matches the user's favorite mood, it gets 1 point.
- Energy is worth up to 1 point. The closer the song's energy is to what the
  user wants, the more points it gets. A perfect match gets the full point.

The program scores every song, sorts them from highest to lowest, and shows
the top 5. It also lists the reasons for each score, so the user can see why
a song was picked.

The starter code had empty functions, so I wrote the scoring rules, the song
loading, and the ranking myself.

---

## 4. Data

The catalog has 18 songs. It started with 10 songs, and I added 8 more to
cover genres and moods that were missing.

- There are 15 genres. Lofi has 3 songs and pop has 2. Every other genre
  has only 1 song.
- There are 13 moods, such as happy, chill, intense, sad, and romantic.
- Each song also has tempo, valence, danceability, and acousticness, but my
  scoring does not use them.

Lots of musical taste is missing: lyrics, language, artist popularity, and
how a user's taste changes over time. With so few songs, one genre can only
give one or two good matches.

---

## 5. Strengths

The system works well for users with clear, common tastes. Chill Lofi and
Deep Intense Rock both got a top song that matched all three preferences.
For Chill Lofi, the top 4 songs were all lofi or chill, which matched my
intuition.

The reasons list is also a strength. It shows exactly which rule gave each
point, so the results are easy to understand and check.

---

## 6. Limitations and Bias

The biggest weakness is that genre and mood together are worth up to 3
points, but energy is only worth 1 point. In my "Conflicted" test (sad folk
at energy 0.9), the top song was Rainy Window, a quiet acoustic song with
energy 0.25. It won only because it matched the genre and mood. A person who
asked for very high energy would probably not enjoy it.

Genres with only one song are another problem. After that one song, the rest
of the list is filled using energy alone, so unrelated genres show up. For
the rock profile, positions 3 to 5 were EDM, metal, and pop.

The system also treats genre and mood as exact matches. "Indie pop" gets no
credit for being close to "pop," and "relaxed" gets no credit for being close
to "chill." Users with more unusual tastes get less useful lists.

---

## 7. Evaluation

I tested four profiles:

- High-Energy Pop (pop, happy, energy 0.85)
- Chill Lofi (lofi, chill, energy 0.35)
- Deep Intense Rock (rock, intense, energy 0.92)
- Conflicted (folk, sad, energy 0.9), made to see if the scoring could be
  tricked

I checked whether the top songs felt right, and whether the scoring reasons
made sense.

**Comparing the profiles:**

- **Pop vs. Lofi:** Pop picks bright, high-energy songs like Sunrise City.
  Lofi picks slow, quiet ones like Library Rain. They share no songs, which
  makes sense, because their genre, mood, and energy are all opposite.
- **Pop vs. Rock:** Both want high energy, so some songs overlap. Gym Hero is
  on both lists, and Sunrise City shows up for rock too. This makes sense,
  because both profiles are close in energy.
- **Lofi vs. Rock:** These two lists are completely different. Lofi wants
  energy near 0.35 and rock wants about 0.92, so no song fits both.
- **Rock vs. Conflicted:** Both want very high energy. After the single
  matching song for each, the rest of both lists is almost the same:
  Storm Runner, Gym Hero, Pulse Festival, and Iron Skyline. This shows that
  energy decides the list when genre and mood run out.

**What surprised me:** Gym Hero keeps showing up. It is an intense, very
high-energy pop song. For a pop user it gets genre points. For a rock user
it gets mood points. Its energy is also close to most high-energy targets.
So it collects points from several places, even for someone who only wanted
happy pop. The system never checks if the song really feels like what the
user wants.

**Experiment:** I halved the genre weight and doubled the energy weight. The
rankings barely changed, and the Conflicted profile still put Rainy Window
first. The results were different, but not more accurate.

---

## 8. Future Work

- Add more song features, such as tempo, valence, and acousticness, so
  energy is not the only number.
- Count close genres and moods as partial matches, like pop and indie pop.
- Add a diversity rule, so the top 5 does not repeat the same artist or
  genre.
- Support users who like more than one genre or mood.
- Add many more songs, so each genre has more than one or two songs.

---

## 9. Personal Reflection

(Write this in your own words. A few ideas to include: what you learned
about how recommenders turn data into predictions, how you used AI and what
you had to double-check, what surprised you, and how this changes how you
think about apps like Spotify.)