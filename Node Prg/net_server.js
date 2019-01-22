const net = require('net');
var server = net.createServer((soclet) => {
	socket.end('goodbye\n');
}).on('error',(err) => {
	//handle error here
	throw err;
});
	//grab a random port.
server.listen(() => {
	address = server.address();
	console.log('opened server on %j', address);
});
