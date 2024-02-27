install : 
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lint:
	pylint --disable=R,C,W0621,W0612,W0611,W0632,W0621 train_model.py
		pylint --disable=R,C,W0621,W0612,W0611,W0632,W0621 predict_model.py
			pylint --disable=R,C,W0621,W0612,W0611,W0632,W0621 app.py
run:
	python train_model.py
		python predict_model.py
			python app.py

all: install lint run 		
