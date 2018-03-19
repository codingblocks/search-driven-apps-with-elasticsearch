const inputFileName = "data/games.json";
const outputFileName = "data/games-formatted.import";

var fs = require('fs');

fs.readFile(inputFileName, 'utf8', function (err, data) {
    if (err) {
        throw err;
    }

    var games = JSON.parse(data);
    var counter = 1;
    var formattedStrings = games.map(game => {
      var headerRow = `{"index":{"_index":"games", "_type":"boardgame", "_id": "${counter}"}}`;
        game.mechanics = game.mechanics.split(',').map(g => g.trim());
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
