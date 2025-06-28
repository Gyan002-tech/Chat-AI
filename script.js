const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");
const sidebar = document.getElementById("sidebar");
const sidebarToggle = document.getElementById("sidebar-toggle");
const modeToggle = document.getElementById("mode-toggle-checkbox");

sidebarToggle.addEventListener("click", () => {
  sidebar.classList.toggle("hidden");
});

modeToggle.addEventListener("change", () => {
  document.body.classList.toggle("dark-mode");
});

sendButton.addEventListener("click", sendMessage);
userInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    sendMessage();
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const newConversationBtn = document.getElementById("new-conversation-btn");
  const conversationContent = document.querySelector(".conversation-content");
  const chatContainer = document.querySelector(".chat-container");

  newConversationBtn.addEventListener("click", function () {
    conversationContent.textContent = "New Conversation Started!";
  });

  modeToggleCheckbox.addEventListener("change", function () {
    chatContainer.classList.toggle("light-mode");
    chatContainer.classList.toggle("dark-mode");
  });
});

function sendMessage() {
  const message = userInput.value.trim();
  if (message !== "") {
    appendMessage("user", message);
    getResponse(message);
    userInput.value = "";
  }
}

function appendMessage(sender, message) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("chat-message");
  if (sender === "user") {
    messageDiv.classList.add("user");
  } else {
    messageDiv.classList.add("bot");
  }
  const bubble = document.createElement("div");
  bubble.classList.add("bubble");
  bubble.classList.add(sender === "user" ? "user" : "bot");
  bubble.textContent = message;
  messageDiv.appendChild(bubble);
  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}

// ✅ Updated: send input to FastAPI backend
function getResponse(message) {
  fetch("http://127.0.0.1:5000/get-response", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ question: message }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      const reply = data.response || "Sorry, I couldn't find an answer.";
      appendMessage("ChatGPT", reply);
    })
    .catch((error) => {
      console.error("Error fetching response:", error);
      appendMessage("ChatGPT", "Oops! Something went wrong.");
    });
}

// The following functions are still used for offline commands like "joke", etc.
// You can remove them if no longer needed
function getCurrentTime() {
  const now = new Date();
  return `Current time is ${now.toLocaleTimeString()}`;
}

function getCurrentDate() {
  const now = new Date();
  return `Today's date is ${now.toDateString()}`;
}

function getWeatherInfo() {
  const weatherData = {
    temperature: getRandomNumber(10, 35),
    condition: getRandomElement(["Sunny", "Cloudy", "Rainy", "Windy"]),
  };
  return `Current weather: ${weatherData.temperature}°C, ${weatherData.condition}`;
}

function getJoke() {
  const jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
  ];
  return getRandomElement(jokes);
}

function getFact() {
  const facts = [
    "Ants stretch when they wake up in the morning.",
    "A group of flamingos is called a flamboyance.",
    "Honey never spoils.",
    "The shortest war in history lasted only 38 minutes.",
    "Octopuses have three hearts.",
  ];
  return getRandomElement(facts);
}

function getQuote() {
  const quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "In the middle of difficulty lies opportunity. – Albert Einstein",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
  ];
  return getRandomElement(quotes);
}

function getRandomElement(array) {
  const randomIndex = Math.floor(Math.random() * array.length);
  return array[randomIndex];
}

function getRandomNumber(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
