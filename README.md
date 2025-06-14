# 🎬 Smart Movie Recommender

This is a simple movie recommendation API built with FastAPI.  
It suggests similar movies based on your favorite titles using content-based filtering.

I started this project to improve my back-end development skills and explore recommendation systems using real-world data.

---

## 🚀 Features

- RESTful API built with FastAPI
- Content-based recommendation engine
- Clean and modular Python architecture
- Ready to be extended with more advanced AI models

---

## 🛠️ Technologies

- Python 3.10+
- FastAPI
- pandas
- scikit-learn
- Uvicorn

---

## 📁 Project Structure

```
smart-movie-recommender/
├── app/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   ├── models/
│   └── data/
├── requirements.txt
├── README.md
```

---

## ⚙️ Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yigithanozturk/smart-movie-recommender.git
cd smart-movie-recommender
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# For macOS/Linux:
source venv/bin/activate
# For Windows:
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
uvicorn app.main:app --reload
```

---

## 📫 Contact

Created by **Yiğithan Öztürk**  
📧 yigithanozturk.dev@gmail.com  
🔗 [github.com/yigithanozturk](https://github.com/yigithanozturk)
