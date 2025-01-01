const lyricsContainer = document.getElementById('lyrics');

const lyrics = [
  "Cause you know how to give me that",
  "you know how to pull me back",
  "when I go runnin', runnin'",
  "tryna get away from loving ya",
  "you know how to love me hard",
  "I won't lie, I'm falling hard",
  "yep, I'm falling for ya",
  "but there's nothing wrong with that",
  "you da one that I dream",
  "about all day",
  // ... rest of the lyrics
];

const delays = [1.1, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 1, 0.3, 1, 0.3, 0.3 , 0.6, 0.8, 0.6, 2];

async function printLyrics() {
  for (const line of lyrics) {
    let displayedLine = "";
    for (let char of line) {
      displayedLine += char;
      lyricsContainer.textContent = displayedLine; // Update content with each character
      await new Promise(resolve => setTimeout(resolve, delays[lyrics.indexOf(line)] * 1000 / line.length)); // Delay based on line length
    }
    lyricsContainer.textContent += "\n"; // Add newline after the line
    await new Promise(resolve => setTimeout(resolve, delays[lyrics.indexOf(line)] * 1000)); // Delay between lines
  }
}

printLyrics();
