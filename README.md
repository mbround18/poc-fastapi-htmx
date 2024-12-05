# Reactive Chat Room: Proof of Concept

This repo is a simple demo to test building a **real-time chat room** using just **htmx**, **FastAPI**, and **Tailwind CSS**—no heavy tools like bundlers or frameworks. The goal is to explore lightweight, reactive web design.

---

## How to Run It

1. Install dependencies with [PDM](https://pdm.fming.dev/):

   ```bash
   pdm install
   ```

2. Start the app:

   ```bash
   pdm run uvicorn main:app --reload
   ```

3. Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## Try It Out

1. In one tab, enter a username like **Test1** and join the chat.
2. In another tab, enter a different username like **Test2** and join.
3. Send messages in either tab, and they’ll show up live in both.

---

## What’s the Point?

- **No Build Tools**: No bundlers, packers, or frameworks—just HTML, CSS, and Python.
- **Reactive Simplicity**: Real-time messaging with minimal setup.
- **For Experimenting**: A playground for lightweight web design ideas. 

