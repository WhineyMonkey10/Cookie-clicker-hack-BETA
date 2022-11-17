// Developed by @WhMonkey
// Version: 1.0.0
// License: MIT
// Enjoy!

// User Interface, real one coming soon
main();

// Main function

function main() {
    // Get the user's input
    var input = prompt("Add cookies (1)       set cookies (2)       ruin the fun (3)       set cookies per second (4, not curerntly working)       set bakery name (5)       get all upgrades (6)       get all achievements (7)       more coming soon <3");
    // Check if the user's input is valid
    if (input == null || input == "") {
        // If the user's input is invalid, show an error
        alert("You need to enter something to hack!");
    } else {
        // If the user's input is valid, show a success message
        alert("Close this to start the hack!");
        // Start the hack
        if (input == "1") {
            let cookies = prompt("How many cookies would you like to add?");
            
            Game.cookies = Game.cookies + parseInt(cookies);
        } else if (input == "2") {
            let cookies = prompt("How many cookies would you like to set?");
            
            Game.cookies = parseInt(cookies);
        } else if (input == "3") {
            Game.RuinTheFun();
        } else if (input == "4") {
            let cps = prompt("How many cookies per second would you like to set?");
            
            Game.cookiesPs=parseInt(cps);
        } else if (input == "5") {
            let name = prompt("What would you like to name your bakery?");
            
            Game.bakeryName="name";
        } else if (input == "6") {
            Game.UpgradesById.forEach(function(upgrade) {
                upgrade.bought = 1;
            });
        } else if (input == "7") {
            Game.AchievementsById.forEach(function(achievement) {
                achievement.won = 1;
            });
        } else {
            alert("Invalid input!");
        }
    }
}

