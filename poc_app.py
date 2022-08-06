import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

import pdfkit
import jinja2
from datetime import date
from time import time_ns
import streamlit as st
from streamlit.components.v1 import iframe

st.markdown("# Proof of Competency: Basic Math")

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################

# Cache the contract on load
@st.cache(allow_output_mutation=True)
# Define the load_contract function
def load_contract():

    # Load Art Gallery ABI
    with open(Path('./Contracts/Compiled/certificate_abi.json')) as f:
        certificate_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=certificate_abi
    )
    # Return the contract from the function
    return contract


# Load the contract
contract = load_contract()

# accounts = w3.eth.accounts
# account = accounts[0]
WKHTMLTOPDF_PATH = '/usr/local/bin/wkhtmltopdf'
student_account = "0x148ED3De2C1cD97d202F539d283C9f45bad6C3e3"
contract_address = "0xeA36c84Ab4F8E33CF421EEfa9D05778B818EA46A"
subject_name = "Basic Math Competency"

with st.form("my_form"):
    choice1 = st.selectbox("What is one quarter of 1,000?", ("25", "250", "2500"))
    choice2 = st.selectbox("Which is larger: 50%, five-eights, or three-quarters?", ["50%", "5/8ths", "3/4s"])
    choice3 = st.selectbox("How many sides, in total, would three triangles and three rectangles have?", ["23", "21", "18"])

    score = 0
    if choice1 == "250":
        score += 1
    if choice2 == "3/4s":
        score += 1
    if choice3 == "21":
        score += 1
    
    passed = False
    submitted = st.form_submit_button("Submit")
    if submitted and score != 3:
        st.write("FAIL!!! Study harder next time!")
    elif submitted and score == 3:
        st.balloons()
        st.write("Congratulations! You have proved your competency in basic math!")
        st.write("Please confirm your information below before minting your certificate.")

        passed = True

        st.write(f"********************* NFT details *********************")
        st.write(f"Subject name: {subject_name}")
        st.write(f"Contract address: {contract_address}")
        st.write(f"Wallet address: {student_account}")
        st.write(f"*******************************************************")

################################################################################
# Award Certificate
################################################################################


if passed == False:
    confirmation = st.checkbox("Confirm", value=False, disabled=True)
else:
    confirmation = st.checkbox("Confirm", value=False, disabled=False)

# env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
# absolute_path_to_html = "/Users/jeffbrinker/OneDrive\ -\ SPR\ Consulting/fintech/homework-all/00-projects/project_3/poc.html"
# template = env.get_template(absolute_path_to_html)

if confirmation == True:
    if st.button("Mint NFT"):
        # contract.functions.awardCertificate(student_account, subject_name).transact({'from': student_account, 'gas': 1000000})

        token_id = "81405704395467559496933594381628460974054685579683453278760615753834800711328"        
        # Get the certificate owner
        # certificate_owner = contract.functions.ownerOf(token_id).call()

        st.write(f"Token ID: {token_id}")

        # Get the certificate's metadata
        # certificate_uri = contract.functions.tokenURI(token_id).call()

# ################################################################################
# # PDF Minter
# ################################################################################

        pdf_options={
            'orientation': 'Landscape',
            'page-size': 'A5',
            # 'margin-top': '5',
            # 'margin-right': '12',
            # 'margin-left': '12',
            'margin-bottom': '5',
            'zoom': '1.0',
            'encoding': "UTF-8",
            "enable-local-file-access": True,
        }
        config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

        templateLoader = jinja2.FileSystemLoader(searchpath="./")
        templateEnv = jinja2.Environment(loader=templateLoader)
        TEMPLATE_FILE = "template.html"
        template = templateEnv.get_template(TEMPLATE_FILE)

        html = template.render(
            subject=subject_name,
            contract_address=contract_address,
            wallet_address=student_account,
            token_id = token_id,
            date=date.today().strftime("%B %d, %Y"),
            timestamp = time_ns()
        )

        date_suffix = date.today().strftime("%Y-%m-%d")
        pdf_name = f"certificate-{date_suffix}.pdf"

        pdf = pdfkit.from_string(html, configuration=config, options=pdf_options)
        st.balloons()

        st.write(f"🎉 Your certificate was generated!")

        # st.write(html, unsafe_allow_html=True)
        st.write("")
        st.download_button(
            "⬇️ Download PDF",
            data=pdf,
            file_name=pdf_name,
            mime="application/octet-stream",
        )

        # st.image("../Images/metamask_icon.png",width=45)
