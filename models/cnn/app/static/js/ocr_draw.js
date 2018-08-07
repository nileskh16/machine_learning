var vocab = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9",":)", ":(","triangle","5star","scribble"];
var index = -1;

function clearCanvas() {
	const canvasRef = document.getElementById("paint"),
	context = canvasRef.getContext('2d');
	context.clearRect(0, 0, canvasRef.width, canvasRef.height);
}

function submitDrawing() {
	const cnnCanvas = document.getElementById("paint"),
	imageData = cnnCanvas.toDataURL('image/jpeg', 0.5);
	
	$.getJSON($SCRIPT_ROOT + '/do_ocr', {
		imgURI: imageData,
		index: index,
		vocab: JSON.stringify(vocab)
	}, function(data) {
		$('#result').text(data.result);
		$('input[name=a]').focus().select();
	});

	document.getElementById("result").innerHTML = "Working...";
	return false;
}

(function() {
	var tempCanvas = document.querySelector('#paint');
    	var tempCtx = tempCanvas.getContext('2d');
    
    	var sketch = document.querySelector('#sketch');
    	var sketch_style = getComputedStyle(sketch);
    	tempCanvas.width = parseInt(sketch_style.getPropertyValue('width'));
	tempCanvas.height = parseInt(sketch_style.getPropertyValue('height'));

	//Create a temp canvas
	var canvas = document.createElement('canvas');
	var ctx = canvas.getContext('2d');
	canvas.id = 'temp_canvas';
	canvas.width = canvas.width;
	canvas.height = canvas.height;

	//sketch.appendChild(tempCanvas);
	var mouse = {x: 0, y: 0}, last_mouse = {x: 0, y: 0};

	var ppts = [];

	//Capture Mouse events
	tempCanvas.addEventListener('mousemove', function(e) {
		mouse.x = typeof e.offsetX !== 'undefined' ? e.offsetX : e.layerX;
		mouse.y = typeof e.offsetY !== 'undefined' ? e.offsetY : e.layerY;
	}, false);
	
	//Draw on temporary canvas
	tempCtx.lineWidth = 15;
	tempCtx.strokeStyle = 'blue';
	tempCtx.lineCap = 'round';
	tempCtx.lineJoin = 'round';
	tempCtx.fillStyle = 'blue';

	tempCanvas.addEventListener('mousedown', function(e) {
		tempCanvas.addEventListener('mousemove', onPaint, false);
		mouse.x = typeof e.offsetX !== 'undefined' ? e.offsetX : e.layerX;
		mouse.y = typeof e.offsetY !== 'undefined' ? e.offsetY : e.layerY;

		ppts.push({x: mouse.x, y: mouse.y});
		onPaint();
	});

	tempCanvas.addEventListener('mouseup', function() {
		tempCanvas.removeEventListener('mousemove', onPaint, false);
		ctx.drawImage(tempCanvas, 0, 0);
		ppts = [];
		tempCtx.clearRect(0, 0, tempCanvas.widht, tempCanvas.height);	
	}, false);

	var onPaint = function() {
		ppts.push({x: mouse.x, y: mouse.y});
		if(ppts.length < 3) {
			var b = ppts[0];
			tempCtx.beginPath();
			tempCtx.arc(b.x, b.y, tempCtx.lineWidth / 2, 0, Math.PI * 2, !0);
			tempCtx.fill();
			tempCtx.closePath();
			return;
		}

		tempCtx.clearRect(0, 0, tempCanvas.width, tempCanvas.height);
		tempCtx.beginPath();
		tempCtx.moveTo(ppts[0].x, ppts[0].y);

		for(var i=0; i < ppts.length - 2; i++) {
			var c = (ppts[i].x + ppts[i + 1].x) / 2,
			d = (ppts[i].y + ppts[i + 1].y) / 2;
			tempCtx.quadraticCurveTo(ppts[i].x, ppts[i].y, c, d);
		}

		tempCtx.quadraticCurveTo(ppts[i].x, ppts[i].y, ppts[i+1].x, ppts[i+1].y);
		tempCtx.stroke();
	}
}());
