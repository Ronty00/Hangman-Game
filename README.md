🎭 Hangman - Command Line Game

Welcome to Hangman 🎉 – a classic word-guessing game where you try to save the stick figure by guessing the correct letters before running out of attempts! This version is powered by Python and utilizes NLTK for word selection and clues. ⚡

🚀 Features:

🎮 Interactive command-line gameplay
📝 Random word selection using NLTK
🔎 Word clue feature using WordNet
🎨 Colorful output with Colorama
📜 Dynamic ASCII Hangman drawing
✅ Proper input validation
🏆 Win or lose messages with fun variations
📜 How to Play
1️⃣ Run the script in the terminal.
2️⃣ You will be given a random word with a clue.
3️⃣ Enter one letter at a time to guess the word.
4️⃣ If the letter is correct, it will be revealed in the word.
5️⃣ If incorrect, you lose a life, and the hangman starts forming.
6️⃣ You have limited attempts before the stick figure is fully drawn! ☠️
7️⃣ Win by guessing all letters before running out of attempts. 🎉


🔧 Installation & Requirements:

Make sure you have Python 3+ installed.

📦 Install Dependencies:

First, install the required libraries:

pip install nltk colorama

🛠️ Download NLTK Word Data

Run this command only once to download the required datasets:

import nltk

nltk.download("words")

nltk.download("wordnet")

nltk.download("omw-1.4")

🚀 Run the Game
Clone the repository and start playing:

bash
Copy
Edit
git clone https://github.com/Ronty00/hangman-cli.git
cd hangman-cli
python hangman.py
🎭 Game Preview
Here's an example gameplay session:

less
Copy
Edit
Welcome to Hangman! 🎭

Clue: A small domesticated carnivorous mammal

_ _ _

Remaining Attempts: 6

Guess a letter: c
✅ Good guess!  
C _ _

Guess a letter: t
✅ Good guess!  
C _ T

Guess a letter: a
✅ Good guess!  
C A T

🎉 Congratulations! You've guessed the word!
🛠️ Upcoming Features
🔜 More word categories (e.g., Animals, Movies, Countries)
🔜 Multiplayer mode (Play with a friend)
🔜 Leaderboard tracking

🤝 Contributing
Want to improve this game? Feel free to fork, submit PRs, or suggest new features! 🚀

Fork the repo 🍴
Create a new branch 🏗️
Commit your changes 📌
Push and submit a PR 🚀
📜 License
This project is open-source under the MIT License. Feel free to modify and share!

⚡ Enjoy the game and happy guessing! 🎉
