# AUTHOR  :  Ankith Kumar                  
# INSTA   : ( itz.ankith.sharma )          
# PROJECT : doc-print                      
# ( THIS IS UPLOAD MODULE FOR CUSTOMERS  )  

import time
import streamlit as st 
from pathlib import Path
from supabase import create_client, Client
import streamlit.components.v1 as components

# - - - - - DB Credentials - - - - ->
URI = st.secrets['URI']
KEY = st.secrets['KEY']
BUCKET = st.secrets['BUCKET_NAME']


# Get Store_ID from URL
query_params = st.query_params
SID = query_params.get("store_ID", " ")


# - - - - - SUPERBASE CLIENT - - - - - - - - - - - ->
supabase: Client = create_client(URI, KEY)


# - - - - - IMPORTING CSS FILE - - - - - - - -> 
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "main.css"


# - - - - - - - Session state initialization - - - - ->
if 'store_name' not in st.session_state:
    st.session_state.store_name = SID
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'reset_key' not in st.session_state:
    st.session_state.reset_key = 0


# - - - - - UI Components  - - - - - - - - - - - - ->
st.header('doc-print')
st.write('Print Smart, Print Secure')
components.html('<hr>', height=50)

msg = st.empty()

StoreName = st.text_input('SID', value=st.session_state.store_name, key=f"sid_{st.session_state.reset_key}").upper() 
UserName = st.text_input('User name', value=st.session_state.user_name, key=f"user_{st.session_state.reset_key}")
pdf_files = st.file_uploader('Select files', accept_multiple_files=True, type=['pdf'], key=f"files_{st.session_state.reset_key}")

btn = st.button('SEND', use_container_width=True, type="primary")


if btn:
    # - - - - - Check all input fields - - - - - - - - - - - ->
    if pdf_files and StoreName and UserName:
        msg.info(f"UPLOADING : {len(pdf_files)} FILES . . . .")
        success_count = 0

        # - - - - - UPLOAD FILE ONE AFTER ANOTHER - - - - - - ->
        for i, pdf_file in enumerate(pdf_files):
            try:
                # GET FILE NAME
                filename = pdf_file.name
                
                # READ CONTENT
                file_content = pdf_file.read()
                
                # CREATING FILE STRUCTURE IN 'BUCKET' WITH SID
                file_path = f"{StoreName}/{UserName}/{filename}"
                
                # UPLOAD TO BUCKET
                response = supabase.storage.from_(BUCKET).upload(
                    file=file_content,
                    path=file_path,
                    file_options={"content-type": "application/pdf"}
                )
                
                if response:
                    msg.success(f'✅ Files uploaded : {filename}')
                    success_count += 1
                else:
                    msg.error(f'❌ FAILED TO UPLOAD : {filename}')
            except Exception as e:
                msg.error(f'❌ ERROR UPLODING : {pdf_file.name} : {str(e)}')
        else:
            msg.error('Enter Valid Store ID')
        # st.write(f"📊 Successfully uploaded {success_count}/{len(pdf_files)} files")
        
        # - - - - RESET ALL FIELDS - - - - - - - - - ->
        if success_count > 0:
            msg.success("✅ All files uploaded !")
            
            # RESET  INPUT FEILDS USING SESSION STATE
            st.session_state.store_name = SID
            st.session_state.user_name = ""
            st.session_state.reset_key += 1  # Force widget recreation

            # DELAY BY 2-SECONDS
            time.sleep(2)
            st.rerun()

    elif not pdf_files:
        msg.warning("⚠️  Please select pdf files")
    elif not StoreName:
        msg.warning("⚠️  Invalid SID")
    elif not UserName:
        msg.warning("⚠️  Please enter  user name")
else:
    if pdf_files:
        msg.info(f"📁 {len(pdf_files)} file(s) selected. click 'send' to upload")


# - - - - - - - - - - - - - - - - - - - ->
st.session_state.store_name = StoreName
st.session_state.user_name = UserName


# - - - - - - APPLYING CSS - - - - - - - - - ->
with open(css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
