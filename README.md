# Project 3 – Minting and Printing NFT Certificates (*Proof of Competency*)

## Background (*Problem Statement*)

One of the biggest problems in the world today is misinformation and disinformation. Whether it be Twitter, Facebook, TikTok, Truth Social, or any other social media app, everyone can have a voice in the public square. While freedom of speech is the first amendment to the Constitution, it does not say all speech deserves to be heard by everyone. 

## Proof of Concept (*User Story*)

We envision a world where instead of seeing posts and comments from everyone, users can filter them and only see information from those who have verifiable expertise in the subject being discussed. If someone wants to be able to contribute to the public conversation about a certain topic, they must show they have a minimum acquired knowledge. As a proof of concept, once a user passes a test, an ERC721 NFT will be minted and passed to their wallet. This will be a key that will give them access to read & write within a forum. Users without a valid NFT Certificate will have  read-only access. Users can be pseudonymous while also being trusted experts, depending on the number of NFTs. NFTs are tied to public addresses and visible to all.

## Minimimum Viable Product (*MVP*)

A user can submit answers to a short test.

The submission will be checked against an answer key.

If the answers are correct (passing threshold), the user can mint an NFT certificate tied to their address.

The certficate ID will be added to a file.

Certificate IDs in this file can be read for "proof of competency", which grants a user write permissions (boolean).

## Additional Features (*Future / Time Allowing*)

- A forum to read from

	- Write only with valid NFT certificate

- Print/download the NFT as a pdf.

- Image/Design on the pdf (visually catchy)

## Resources


We plan on using the following systems to run our app:

	- Remix
	- Ganache
	- Streamlit
	- Jupyter Lab (?)

	- Initial Imports and Environment tools (pending development)