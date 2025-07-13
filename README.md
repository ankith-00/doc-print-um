# doc-print-um

📄 doc-print file upload module <br>
- This module enables customers to upload PDF files to a specific store for printing or processing. It’s designed to streamline document submission and ensure files are routed correctly based on store selection. <br>
- view app : https://doc-print.streamlit.app
<br>


## ✅ Features
- Upload multiple PDF files at once
- Store-specific routing using embedded store ID
- Real-time upload feedback and error handling
- Clean UI with custom styling via CSS

<br>

## ⚙️ Tech Stack
| Technology  | Purpose                |
|-------------|------------------------|
| Streamlit   | Frontend interface     |
| Supabase    | File storage and DB    |
| Python      | Backend logic          |
| CSS         | Custom styling         |

<br>


## 📦 Installation

```bash
git clone https://github.com/ankith-00/doc-print-um.git
cd doc-print-um
pip install -r requirements.txt
streamlit run main.py
```

## Configure Streamlit Secrets.toml file 
```bash
URI = "your_supabase_url"
KEY = "your_supabase_key"
BUCKET_NAME = "your_bucket_name"
TABLE_NAME = "your_table_name"
STORE_ID = "your_store_id_column"
```



## 📁 File Structure 
doc-print-um/ <br>
├── main.py   <br>
├── main.css  <br>
├── README.md <br>
├── requirements.txt  <br>
└── .streamlit/       <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    └── secrets.toml  <br>


<br>
Application Visual : 
<img src="https://i.ibb.co/1YG3gfxX/Screenshot-20250712-104827-Chrome.jpg" width="350">
<br>
