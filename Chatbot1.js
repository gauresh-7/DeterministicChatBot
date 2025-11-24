document.addEventListener("DOMContentLoaded", () => {
  const input = document.getElementById("userinput");
  const button = document.getElementById("ask-button");
  const responseEl = document.getElementById("bot-response");

  async function askQuestion() {
    const question = (input.value || "").trim();
    if (!question) {
      responseEl.textContent = "Please type a question first.";
      return;
    }

    try {
      const res = await fetch("/answer", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question }),
      });

      if (!res.ok) {
        responseEl.textContent = "Error talking to the bot.";
        return;
      }

      const data = await res.json();
      responseEl.textContent = data.answer ?? "No answer returned.";
    } catch (err) {
      responseEl.textContent = "Network error talking to the bot.";
    }
  }

  button.addEventListener("click", askQuestion);

  input.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
      askQuestion();
    }
  });
});