# Malicious_File_Scanner

# ⚡ Aayush's Cyberpunk File Scanner ⚡

A powerful, stylish, and beginner-friendly **Malware Scanner** built with **Flask**, integrated with **VirusTotal** and **Hybrid Analysis APIs**, and topped off with a **cyberpunk-inspired UI** featuring Lottie animations.

## 🚀 Features

- 🔒 Scan uploaded files using VirusTotal & Hybrid Analysis
- ⚡ Beautiful **Cyberpunk UI** with glowing neon elements
- 🎥 Lottie animation to visualize scanning progress
- 📁 Upload and scan files in real time
- 📊 Dashboard for scan history
- 📧 Email alerts for dangerous files (if configured)
- 💾 Clean modular structure for easy development

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap 5, Lottie.js
- **Backend**: Python, Flask
- **APIs**: VirusTotal API, Hybrid Analysis API
- **Deployment**: Localhost (for now), ready for Heroku or Render

---

## 📁 Project Structure

Malicious_File_Scanner/
│
├── app/
│   ├── templates/               # HTML templates
│   │   ├── index.html
│   │   └── result.html
│   ├── static/
│   │   ├── style.css
│   │   └── animations/scan.json
│   ├── uploads/                 # Uploaded files
│   ├── scanner_logic/          # VirusTotal and Hybrid Analysis integration
│   │   └── malware_scanner.py
│   └── routes.py               # Main Flask routes
│
├── run.py                      # Flask app entry point
└── README.md                   # This file

## ⚙️ Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/Malicious_File_Scanner.git
   cd Malicious_File_Scanner
Create and activate virtual environment

bash
Copy
Edit
python -m venv .venv
.\\.venv\\Scripts\\activate   # For Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Add your API keys
Create a .env file and add:

ini
Copy
Edit
VIRUSTOTAL_API_KEY=your_key_here
HYBRID_ANALYSIS_API_KEY=your_key_here
Run the application

bash
Copy
Edit
python run.py
Visit in browser
Open http://127.0.0.1:5000 to use the app

🔮 Future Enhancements
OAuth user login & user dashboards

PDF export of reports

Cloud storage for scanned files

Real-time malware signature updates

🙌 Credits
Designed & Developed by Aayush

Thanks to VirusTotal and Hybrid Analysis for free API access

Lottie Animations from LottieFiles

📜 License
This project is licensed under the MIT License.
