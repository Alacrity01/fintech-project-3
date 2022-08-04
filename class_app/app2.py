import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
import numpy as np

import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe

st.markdown("# Proof of Competency: Basic Math")

# WKHTMLTOPDF_PATH = '/usr/local/bin/wkhtmltopdf'

# def generate_pdf(html, static_path,  _path):
#     config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
#     _status = pdfkit.from_string(
#         html,
#         os.path.join(static_path, _path),
#         configuration=config,
#         options={
#             'page-size': 'A4',
#             'margin-top': '0',
#             'margin-right': '0',
#             'margin-left': '0',
#             'margin-bottom': '0',
#             'zoom': '1.2',
#             'encoding': "UTF-8",
#         })
#     return _path if _status else ''

load_dotenv()

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
    with open(Path('./contracts/compiled/certificate_abi.json')) as f:
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



# name = st.text_input('Name')
# if not name:
#   st.warning('Please input a name.')
#   st.stop()
# st.success('Thank you for inputting a name.')



with st.form("my_form"):
    choice1 = st.selectbox("What is one quarter of 1,000?", ["25", "250", "2500"])
    choice2 = st.selectbox("Which is larger: 50%, five-eights, or three-quarters?", ["50%", "5/8ths", "3/4s"])
    choice3 = st.selectbox("How many sides, in total, would three triangles and three rectangles have?", ["23", "21", "18"])



    score = 0
    if choice1 == "250":
        score += 1
    if choice2 == "3/4s":
        score += 1
    if choice3 == "21":
        score += 1
    


    # slider_val = st.slider("Form slider")
    # checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.

    passed = False

    submitted = st.form_submit_button("Submit")
    if submitted and score != 3:
        st.write("FAIL!!! Study harder next time!")
    elif submitted and score == 3:
        st.write("Congratulations! You have proved your competency in basic math! \nPlease confirm your information below before minting your certificate.")
        passed = True




# with st.container():
#     st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    # st.bar_chart(np.random.randn(50, 3))

# st.write("This is outside the container")




################################################################################
# Award Certificate
################################################################################

# accounts = w3.eth.accounts
# account = accounts[0]



student_account = "0x148ED3De2C1cD97d202F539d283C9f45bad6C3e3"
certificate_name = "Basic Math Competency"


if passed == False:
    confirmation = st.checkbox(certificate_name, value=False, disabled=True)
else:
    confirmation = st.checkbox(certificate_name, value=False, disabled=False)

# st.checkbox(label, value=False, disabled=False):



env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")

token_id = "81405704395467559496933594381628460974054685579683453278760615753834800711328"


if confirmation == True:
    if st.button("Mint NFT"):
        # contract.functions.awardCertificate(student_account, certificate_name).transact({'from': student_account, 'gas': 1000000})






        ################################################################################
        # Display Certificate
        ################################################################################

    # submit = form.form_submit_button("Generate PDF")
    # if submit:
    # if st.button("Display Certificate"):
        # Get the certificate owner
        # certificate_owner = contract.functions.ownerOf(token_id).call()
        st.write(f"The Proof of {certificate_name} NFT was awarded to {student_account}")

        # Get the certificate's metadata
        # certificate_uri = contract.functions.tokenURI(token_id).call()




        



# ################################################################################
# # PDF Minter
# ################################################################################



        html = template.render(
            subject=certificate_name,
            # skill="Multiplication",
            # level = "1",
            # course="Basic Mathematics",
            wallet_address=f"{student_account}",
            date=date.today().strftime("%B %d, %Y"),
            token_id = token_id
        )

        pdf = pdfkit.from_string(html, False)
        st.balloons()


        # generate_pdf(html, WKHTMLTOPDF_PATH, _path)


        st.write(f"🎉 Your certificate was generated!")


        st.write(html, unsafe_allow_html=True)
        st.write("")
        st.download_button(
            "⬇️ Download PDF",
            data=pdf,
            file_name="certificate.pdf",
            mime="application/octet-stream",
        )

        # st.image("../Images/metamask_icon.png",width=45)

        st.markdown("![alt='Picture4'](../Images/metamask_icon.png)")
        

        st.download_button(
            "⬇️ Add to Wallet",
            data=pdf,
            file_name="certificate.pdf",
            mime="application/octet-stream",
        )
# ################################################################################
# # PDF Minter
# ################################################################################


















# ################################################################################
# # Award Certificate
# ################################################################################

# accounts = w3.eth.accounts
# account = accounts[0]
# student_account = st.selectbox("Select Account", options=accounts)
# certificate_name = st.text_input("Certificate Details", value="FinTech Certificate of Completion")
# if st.button("Award Certificate"):
# # if st.button("Award Certificate" and passed == True):
#     contract.functions.awardCertificate(student_account, certificate_name).transact({'from': account, 'gas': 1000000})
# else:
#     st.write(f"You have to pass to earn a certificate")

# ################################################################################
# # Display Certificate
# ################################################################################
# token_id = st.number_input("Enter a Certificate Token ID to display", value=0, step=1)
# if st.button("Display Certificate"):
#     # Get the certificate owner
#     certificate_owner = contract.functions.ownerOf(token_id).call()
#     st.write(f"The certificate was awarded to {certificate_owner}")

#     # Get the certificate's metadata
#     certificate_uri = contract.functions.tokenURI(token_id).call()
#     st.write(f"The certificate's tokenURI metadata is {certificate_uri}")
