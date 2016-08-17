/* Javascript Usage:                                                        *
 * var ws = new WebSocket('ws://localhost:8000/ws');                        *
 * ws.onopen = function(event){ console.log('socket open'); }               *
 * ws.onclose = function(event){ console.log('socket closed'); }            *
 * ws.onerror = function(error){ console.log('error:', err); }              *
 * ws.onmessage = function(event){ console.log('message:', event.data); }   *
 * //... wait for connection to open                                        *
 * ws.send('hello world')                                                   */

var app = (function ($) {
    var config = $('#config'),
        app = JSON.parse(config.text());
    return app;
})(jQuery);