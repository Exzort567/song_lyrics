document.addEventListener('DOMContentLoaded', (event) => {
    const playBtn = document.querySelector('.play-btn');
    const body = document.querySelector('.body');
    const lyricsContainer = document.getElementById('lyrics');

    const lyrics = [
        { text: "And anytime you,", delay: 0.06 },
        { text: "feel the pain,", delay: 0.08 },
        { text: "Hey, Jude, refrain,", delay: 0.1 },
        { text: "Don't carry the world", delay: 0.12 },
        { text: "upon your shoulders", delay: 0.09 },
        { text: "For well you know", delay: 0.08 },
        { text: "that it's a fool ", delay: 0.08 },
        { text: "Who plays it cool", delay: 0.1 },
        { text: "By making his world", delay: 0.08 },
        { text: "a little colder", delay: 0.2 },
        { text: "Na, na na, na na,", delay: 0.1 },
        { text: "na na, na na", delay: 0.15 }
    ];

    const delays = [0.12, 0.23, 0.6, 0.5, 3, 0.3, 0.5, 0.7, 0.8, 1, 0.1, 2];

    async function displayLyrics() {
        for (let i = 0; i < lyrics.length; i++) {
            let line = lyrics[i].text;
            let charDelay = lyrics[i].delay;
            for (let char of line) { 
                lyricsContainer.innerHTML += char;
                await new Promise(resolve => setTimeout(resolve, charDelay * 1000));
            }
            await new Promise(resolve => setTimeout(resolve, delays[i] * 1000));
            lyricsContainer.innerHTML += '\n';
            lyricsContainer.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
        }
    }

    playBtn.addEventListener('click', () => {
        playBtn.style.display = 'none';

        // Create a new div for the background animation
        const backgroundFade = document.createElement('div');
        backgroundFade.className = 'background-fade';
        backgroundFade.style.backgroundImage = 'url("./images/sadCat.jpg")';
        body.appendChild(backgroundFade);

        displayLyrics();
    });
});