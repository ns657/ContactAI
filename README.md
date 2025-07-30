# ✨ AI-Powered Contact Form – Django + ML + GSAP ✨

This is an interactive, ML-enhanced contact form built using **Django**, integrated with a **machine learning classifier** to automatically label messages as Feedback, Complaint, or Inquiry. On top of that, it features beautiful **GSAP animations** for a modern, professional UI experience.

---

## 🚀 Features

- **Contact Form** with animated transitions (GSAP)
- **AI Classification** of messages (Scikit-learn)
- **View Previous Submissions** with filter options
- Submissions stored in SQLite for easy access
- **ScrollTrigger + Loading Animations** (GSAP)

---

## 🧠 AI Model

- Trained using sample labeled data
- Uses **TF-IDF vectorizer** + **Multinomial Naive Bayes**
- Model saved as `classifier.joblib`
- Integrated seamlessly into Django view logic

---

## 🛠️ Tech Stack

| Frontend      | Backend     | AI / Data      |
|---------------|-------------|----------------|
| HTML, CSS     | Django      | scikit-learn   |
| JavaScript (GSAP) | SQLite     | joblib, pandas |
| ScrollTrigger | Django ORM | TF-IDF Vectorizer |

---

## 📁 Project Structure

```

contactsite/
├── contact/
│   ├── templates/
│   │   ├── contact.html
│   │   ├── submissions.html
│   │   └── success.html
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── classifier.joblib
├── contactsite/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── db.sqlite3
├── manage.py
└── train\_model.py

````

---

## 📦 Setup Instructions

1. **Clone this repo**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Train or use existing model**

   * Already trained model: `contact/classifier.joblib`
   * Or run:

     ```bash
     python train_model.py
     ```

5. **Run the server**

   ```bash
   python manage.py runserver
   ```

---

## 🧪 Sample Filter Usage (Submissions View)

* Filter by `Feedback`, `Complaint`, or `Inquiry` using the dropdown
* Smooth animated transitions between views

