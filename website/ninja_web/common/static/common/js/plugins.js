
// usage: log('inside coolFunc', this, arguments);
// paulirish.com/2009/log-a-lightweight-wrapper-for-consolelog/
window.log = function(){
  log.history = log.history || [];   // store logs to an array for reference
  log.history.push(arguments);
  arguments.callee = arguments.callee.caller;
  if (this.console) {
    console.log( Array.prototype.slice.call(arguments) );
  }
};

// make it safe to use console.log always
(function(b){function c(){}for(var d="assert,count,debug,dir,dirxml,error,exception,group,groupCollapsed,groupEnd,info,log,markTimeline,profile,profileEnd,time,timeEnd,trace,warn".split(","),a;a=d.pop();)b[a]=b[a]||c})(window.console=window.console||{});

var navInfo = window.navigator.appVersion.toLowerCase();
var os = 'What system de you use?? Contact us and tell !!';
function retornarSO() {
	if (navInfo.indexOf('win') != -1) {
		os = 'Windows';
	} else if (navInfo.indexOf('linux') != -1) {
		os = 'Linux';
	} else if (navInfo.indexOf('mac') != -1) {
		os = 'Mac';
	}
	return os;
}

// place any jQuery/helper plugins in here, instead of separate, slower script files.
