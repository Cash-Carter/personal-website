var names = [
    "def greet():\n    print(\"Hi, I'm Cash Carter\")",
    "static void greet() {\n    System.out.println(\"Hi, I'm Cash Carter\");\n}",
    "function greet() {\n    console.log(\"Hi, I'm Cash Carter\");\n}",
    "greet :: IO ()\ngreet = print \"Hi, I'm Cash Carter\"",
];
var languages = [
    "Python",
    "Java",
    "JavaScript",
    "Haskell"
];

var nameElement;
var languageElement;

var currentName = -1;
var currentChar = 0;
var typeWriterSpeed = 25;

function changeName() {
    nameElement.innerHTML = "";
    currentChar = 0;
    currentName++;
    if (currentName == names.length) currentName = 0;
    languageElement.innerHTML = languages[currentName];
    typeWriter();
}

function typeWriter() {
    if (currentChar < names[currentName].length) {
        if (names[currentName][currentChar] == "\n") {
            nameElement.appendChild(document.createElement("br"));
        } else {
            nameElement.innerHTML += names[currentName].charAt(currentChar);
        }
        currentChar++;
        setTimeout(typeWriter, typeWriterSpeed);
    }
}

document.addEventListener("DOMContentLoaded", (event) => {
    nameElement = document.getElementById("name");
    languageElement = document.getElementById("language");
    changeName();
    setInterval(changeName, 5000);
});