# 🧙‍♂️ Harry Potter Invisibility Cloak — with OpenCV + Python

This project brings Harry Potter’s magic to real life using **Computer Vision**!  
By using **OpenCV**, **Python**, and a bit of **color masking**, we can make a cloak disappear in real time — just like the invisibility cloak in the movies. ✨

---

## 🚀 How It Works
1. Capture the static background before the person enters the frame.
2. Detect the cloak color (e.g., red, green, or blue) using **HSV color space**.
3. Create a mask for the cloak and replace that region with the background.
4. Display the combined frame so the cloak (and the person) look invisible!

---

## 🛠 Tech Stack
- **Python** — Core programming language
- **OpenCV** — Real-time video processing
- **NumPy** — Fast array operations
- **Color Detection & Masking** — Hide the cloak in the video feed

---

## 📂 Project Files
- `cloak.py` → Main script to run the invisibility effect
- `requirements.txt` → Required libraries
- `notebook.ipynb` → Step-by-step explanation (optional)
- `demo.gif` → Output demo

---

## ✅ Skills Learned
- Real-time video processing
- Image masking & segmentation
- Basic object tracking
- Debugging & problem solving

---

## 🎥 Demo
(Add a gif or short video of you using the cloak)

---

## ⚡ Run It
```bash
# Clone this repo
git clone https://github.com/<your-username>/Invisibility-Cloak-OpenCV.git
cd Invisibility-Cloak-OpenCV

# Install dependencies
pip install -r requirements.txt

# Run the project
python cloak.py
