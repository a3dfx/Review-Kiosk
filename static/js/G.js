G = {};

G.controls = {};

G.addControl = function(className, control) {
	var self = this;
	if (control) {
		control.className = className;
		self.controls[className] = control;
		return self;
	}
}

G.timer;

G.refreshPage = function() {
	location.reload(true);
}

G.restartTimeout = function() {
	if (G.timer) {
		G.timerOn = false;
		clearTimeout(G.timer);
		G.doTimer();
	}
}

G.doTimer = function() {
	if (!G.timerOn) {
		G.timerOn = true;
		G.timer = setTimeout(G.refreshPage, 60000*20);
	}
}