function copyButton(className, label, getText) {
  const button = document.createElement("button");
  button.type = "button";
  button.className = className;
  button.textContent = label;
  button.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(getText());
      button.textContent = "Copied!";
    } catch {
      button.textContent = "Select and copy";
    }
    setTimeout(() => (button.textContent = label), 2000);
  });
  return button;
}

// Add a Copy button to every prompt and command.
document.querySelectorAll("pre.prompt, pre.command").forEach((pre) => {
  const button = copyButton("copy", "Copy", () => pre.textContent.trim());
  const wrapper = document.createElement("div");
  wrapper.className = "copyable";
  pre.replaceWith(wrapper);
  wrapper.append(pre, button);
});

// Add a Copy button to each Level 1 topic question.
document.querySelectorAll(".topic-question").forEach((question) => {
  question.after(copyButton("copy-question", "Copy question", () => question.textContent.trim()));
});

// Fill in code listings from the files in code/, so the page always matches the downloads.
document.querySelectorAll("pre.code[data-src]").forEach(async (pre) => {
  try {
    const response = await fetch(pre.dataset.src);
    if (!response.ok) throw new Error(response.status);
    pre.textContent = await response.text();
  } catch {
    pre.textContent = `Couldn't load ${pre.dataset.src}. Download the zip instead.`;
  }
});
