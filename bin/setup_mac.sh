# requirements
# - docker
# - pip

# get the code
git clone https://oauth2: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@github.com/ocean-core/ocean.git

#checkout the right branch
cd ocean

# run docker
cd ocean-server
docker-compose up -d --build

# install ocean-client
cd ../ocean-client
pip install --upgrade pip # you have to do this or it will use UNKNOWN as the package name
pip install .
