# Quickstart

Easiest way to get started is by installing the pip package. Sadly spacy and spacey was taken so its located at spacie.

    pip install spacie

Once that is done, you have access to the commands `spacy_server.py` to run the server.

To start the client run

    spacy_client.py domainname.com

Where domainname.com is either the ip of the host or the domain where the server is located. In order for this to work across the internet, the computer that is hosting the server must have port 6699 open.

# Develop

Clone the github, make a virtualenv and install requirements.txt

    git clone git@github.com:Tsangares/Spacy.git
    cd Spacy
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt


Then you can access the commands located in the spacy directory.

     ./spacy/spacy_server.py 	 	    #runs the server
     ./spacy/spacy_client.py domainname.py  #runs the client



