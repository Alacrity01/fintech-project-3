from bdb import GENERATOR_AND_COROUTINE_FLAGS
import os
from pathlib import Path
from time import time_ns
# from dotenv import load_dotenv
# import streamlit as st
# import numpy as np

import pdfkit
# from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import jinja2
# import streamlit as st
# from streamlit.components.v1 import iframe


WKHTMLTOPDF_PATH = '/usr/local/bin/wkhtmltopdf'

# def generate_pdf(html, static_path, _path):
#     config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
#     _status = pdfkit.from_string(
#         html,
#         os.path.join(static_path, _path),
#         configuration=config,
#         options={
# 			'orientation': 'Landscape',
#             'page-size': 'A6',
#             'margin-top': '0',
#             'margin-right': '0',
#             'margin-left': '0',
#             'margin-bottom': '0',
#             'zoom': '1.2',
#             'encoding': "UTF-8",
#         })
#     return _path if _status else '**************NO STATUS**************'

# pdf_options={
# 	'orientation': 'Landscape',
# 	'page-size': 'A4',
# 	'margin-top': '5',
# 	'margin-right': '12',
# 	'margin-left': '12',
# 	'margin-bottom': '5',
# 	'zoom': '1.0',
# 	'encoding': "UTF-8",
# 	"enable-local-file-access": True,
# }
# config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

# env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
# template = env.get_template("poc.html")

# token_id = "81405704395467559496933594381628460974054685579683453278760615753834800711328"
# contract_address = "0xeA36c84Ab4F8E33CF421EEfa9D05778B818EA46A"

# student_account = "0x148ED3De2C1cD97d202F539d283C9f45bad6C3e3"
# subject_name = "Basic Math Competency"

# html = template.render(
# 	subject=subject_name,
# 	contract_address=contract_address,
# 	wallet_address=student_account,
# 	token_id = token_id,
# 	date=date.today().strftime("%Y-%m-%d"),
# 	timestamp = time_ns()
# )

# pdf_name = f"certificate-{str(time_ns())}.pdf"

# pdf = pdfkit.from_string(html, options=pdf_options, output_path="certificate.pdf", configuration=config)
# pdf = pdfkit.from_string(html, options=pdf_options, output_path=pdf_name, configuration=config)


# print(generate_pdf(html, WKHTMLTOPDF_PATH, ''))







WKHTMLTOPDF_PATH = '/usr/local/bin/wkhtmltopdf'
student_account = "0x148ED3De2C1cD97d202F539d283C9f45bad6C3e3"
contract_address = "0xeA36c84Ab4F8E33CF421EEfa9D05778B818EA46A"
subject_name = "Basic Math Competency"
token_id = "81405704395467559496933594381628460974054685579683453278760615753834800711328"

# env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
# absolute_path_to_html = "/Users/jeffbrinker/OneDrive\ -\ SPR\ Consulting/fintech/homework-all/00-projects/project_3/poc.html"
# template = env.get_template(absolute_path_to_html)

	# contract.functions.awardCertificate(student_account, subject_name).transact({'from': student_account, 'gas': 1000000})






	################################################################################
	# Display Certificate
	################################################################################

# submit = form.form_submit_button("Generate PDF")
# if submit:
# if st.button("Display Certificate"):
	# Get the certificate owner
	# certificate_owner = contract.functions.ownerOf(token_id).call()



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


# env = Environment(loader=PackageLoader('poc_app.py', 'templates'))


templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "template.html"
template = templateEnv.get_template(TEMPLATE_FILE)
# outputText = template.render()  # this is where to put args to the template renderer

# env = Environment(loader=FileSystemLoader("./templates"), autoescape=select_autoescape(
#     enabled_extensions=('html'),
#     default_for_string=True,
# ))
# template = env.get_template("poc.html")

html = template.render(
	subject_name=subject_name,
	contract_address=contract_address,
	wallet_address=student_account,
	token_id = token_id,
	date=date.today().strftime("%B %d, %Y"),
	timestamp = time_ns()
)

date_suffix = date.today().strftime("%Y-%m-%d")
pdf_name = f"certificate-{date_suffix}.pdf"

# pdf = pdfkit.from_string(html, options=pdf_options, output_path=pdf_name, configuration=config)

# pdf = pdfkit.from_string(html, configuration=config, options=pdf_options)
pdfkit.from_string(html, options=pdf_options, output_path="certificate.pdf", configuration=config)

# generate_pdf(html, WKHTMLTOPDF_PATH, _path)

# st.image("../Images/metamask_icon.png",width=45)

# st.markdown("![''](../Images/metamask_icon.png)")


#         st.download_button(
#             "⬇️ Add to Wallet",
#             data=pdf,
#             file_name="certificate.pdf",
#             mime="application/octet-stream",
#         )
# # ################################################################################
# # PDF Minter
# ################################################################################


print("DONE" * 20)

