const inputFileName = "games.json";
const outputFileName = "games-formatted.import";

var fs = require('fs');

fs.readFile('games.json', 'utf8', function (err, data) {
    if (err) {
        throw err;
    }

    var games = JSON.parse(data);
    var counter = 1;
    var formattedStrings = games.map(game => {
        var headerRow = `{"index":{"_index":"games", "_type":"games", "_id": "${counter}"}}`;
        var docRow = JSON.stringify(game);
        counter++;
        return headerRow + '\n' + docRow;
    });

    console.log(`${formattedStrings.length * 2} objects generated`);

    var finalOutput = formattedStrings.join('\n') + '\n'; // must have newline at the end
    fs.writeFile(outputFileName, finalOutput, function(err) {
        if(err) {
            console.log(err);
            return;
        }
    
        console.log(`${outputFileName} has been generated`)
    }); 

    
});