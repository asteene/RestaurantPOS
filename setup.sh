chmod +x *.sh
cd database && chmod +x *.sh && ./resetDB.sh && cd ..
python3.10 -m pip install -r requirements.txt