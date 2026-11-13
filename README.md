# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

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
Delete the starter prompts. The “Some prompts to answer” bullets and the “Explain your design” line should be replaced by this text, not kept above it.
Use your own words. Reword a few sentences so it sounds like you.
Project Summary still needs a paragraph. At the top of the README, replace “Replace this paragraph with your own summary” with 2-3 sentences about what your version does. For example: “This project is a small content-based music recommender. It scores songs by genre, mood, and energy against a user’s taste profile and returns the top matches with reasons.”

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

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

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



