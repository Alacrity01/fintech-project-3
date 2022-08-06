from bdb import GENERATOR_AND_COROUTINE_FLAGS
import os
from pathlib import Path
from time import time_ns
# from dotenv import load_dotenv
# import streamlit as st
# import numpy as np

import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
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

pdf_options={
	'orientation': 'Landscape',
	'page-size': 'A5',
	'margin-top': '5',
	'margin-right': '12',
	'margin-left': '12',
	'margin-bottom': '5',
	'zoom': '1.0',
	'encoding': "UTF-8",
}
config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("poc.html")

token_id = "81405704395467559496933594381628460974054685579683453278760615753834800711328"
contract_address = "0xeA36c84Ab4F8E33CF421EEfa9D05778B818EA46A"

student_account = "0x148ED3De2C1cD97d202F539d283C9f45bad6C3e3"
certificate_name = "Basic Math Competency"

html = template.render(
	subject=certificate_name,
	contract_address=contract_address,
	wallet_address=student_account,
	token_id = token_id,
	date=date.today().strftime("%Y-%m-%d"),
	timestamp = time_ns()
)


pdf = pdfkit.from_string(html, options=pdf_options, output_path="HERE_IT_IS_VERSION_TWO_POINT_OH.pdf", configuration=config)


# print(generate_pdf(html, WKHTMLTOPDF_PATH, ''))
print("DONE" * 20)

