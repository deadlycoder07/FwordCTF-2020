var page = require('webpage').create();
var args=require('system').args;
var url = args[1];
var session= args[2];
var timeout = 2000;
phantom.cookies=[{
    'name': 'Flag',
    'value': 'FwordCTF{Y0u_Only_h4vE_T0_cH4in_4nd_Th1nk_w3ll}',
    'domain': 'web1.fword.wtf',
// TODO change domain to 127.0.0.1 when debugging localy
    'path': '/',
    'httponly': false
},
{
    'name': 'PHPSESSID',
    'value': session,
    'domain': 'web1.fword.wtf',
// TODO change domain to 127.0.0.1 when debugging
    'path': '/',
    'httponly': true
}]

page.onNavigationRequested = function(url, type, willNavigate, main) {
    console.log("[URL] URL="+url);  
};
page.settings.resourceTimeout = timeout;
page.onResourceTimeout = function(e) {
    setTimeout(function(){
        console.log("[INFO] Timeout")
        phantom.exit();
    },5000);
};

window.setTimeout(function(){
page.open(url, function(status) {
	
	window.setTimeout(function(){
        console.log("success");
        phantom.exit();
    }, 200);
});
},100);
    
