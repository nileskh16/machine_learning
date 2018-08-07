from flask import render_template, flash, redirect, request, jsonify
from app import app
from app.model.preprocessor import Preprocessor as img_prep
from app.model.alpha_cnn_predict import LiteOCR
import json, sys

@app.route('/')
@app.route('/index')
def index():
	user = {'name': 'SK2504'}
	title = 'SK is Great'
	return render_template('index.html', title=title, user=user)

@app.route('/do_ocr', methods = ['GET', 'POST'])
def do_ocr():
	app.logger.debug("Accessed _do_ocr page with image data")
	# flash('Just hit the _add_numbers function')
	# a = json.loads(request.args.get('a', 0, type=str))
	data = request.args.get('imgURI', 0, type=str)
	app.logger.debug("Data looks like " + data)
	index = request.args.get('index', 0, type=int)
	vocab = json.loads(request.args.get('vocab',0,type=str))

	pp = img_prep(fn="dataset.txt")
	ocr = LiteOCR(fn="app/model/alpha_weights.pkl")
	char_prediction= ocr.predict(pp.preprocess(data))

	result = "You entered a: " + char_prediction
	app.logger.debug("Recognized a character")
	return jsonify(result=result)
