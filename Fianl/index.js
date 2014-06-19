var read = require('node-readability');
var fs = require('fs');
var readline = require('readline');
var exec = require('child_process').exec;

var rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
//'http://blog.xuite.net/ca062/blog/221677672'
rl.question("Please type the html or url to extract content: \n", function(answer) {
	// TODO: Log the answer in a database
	console.log("Processing: ", answer);

	read(answer, function(err, article, meta) {
		fs.writeFile('output.html', article.content, function (err) {
			if (err) throw err;
			console.log('Finish!!!');
			rl.close();
			exec("explorer output.html");
		});
	});
});



