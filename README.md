MCP Server - Minimal Command Platform

A full-stack project that allows users to upload folders and perform file operations (create, edit, delete) within that folder using a web interface.  
Built using Flask (backend) and HTML/CSS/JavaScript (frontend).


🚀 Features

- 📂 Upload folders (with subfolders and files)
- 📃 List all files in the folder
- ✍️ Create new files with content
- ✏️ Edit existing files
- 🗑️ Delete files
- 💡 Sidebar to quickly select/edit files
- ✅ Fully sandboxed – no access to system files


📁 Folder Structure

MCP-Server/
├── backend/
│   ├── server.py              # Flask server
│   └── requirements.txt       # Python dependencies
├── frontend/
│   ├── index.html             # Web UI
│   └── style.css              # Styling
└── README.md


🛠️ Tech Stack

Layer     | Tech Stack                      
--------- | ----------------------------------
Frontend  | HTML, CSS, JavaScript (Vanilla)
Backend   | Python (Flask + flask-cors)
Styling   | Pure CSS (Modern, Responsive)


🔧 Prerequisites

- Python 3.x
- pip (Python package manager)
- Web browser


⚙️ Setup Instructions

Backend
1. Navigate to backend folder:
   cd backend

2. Install dependencies:
   pip install -r requirements.txt

3. Run the Flask server:
   python server.py

   Server runs at: http://localhost:5000

Frontend
Simply open the frontend/index.html file in your browser (double-click or right-click → open in browser).
No need for a separate server; it's static HTML/CSS/JS.


💻 Usage

1. Upload a folder via the Upload section
2. Enter the same folder name in "Manage Files"
3. Use sidebar to view files or manually input relative file path
4. Add/edit/delete content using the UI


📂 Where Files Are Stored?

All operations are sandboxed inside:
~/mcp_workspace

On your system, this resolves to:
- Windows: C:\Users\YourUsername\mcp_workspace
- Linux/macOS: /home/yourname/mcp_workspace

✅ No system files are accessed or modified.


🔐 Security Notes

- Only relative paths allowed
- All paths are joined with BASE_DIR
- Directory traversal (../) can be optionally blocked
