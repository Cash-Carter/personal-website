/*
Copyright 2026 Cash Carter

This program is free software: you can redistribute it and/or
modify it under the terms of the GNU Affero General Public License
as published by the Free Software Foundation, either version 3
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
*/

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