// Developed by @WhMonkey
// Version: 1.0.0
// License: MIT
// Enjoy!

// User Interface, real one coming soon
wait(1000);
alert("🍪 Welcome to Cookie Clicker Hack! 🍪\n\nPress CTRL + ALT + C to open the cheat panel. \n\n🍪 Enjoy! 🍪");



// Main function

document.addEventListener("keyup",function(evt){
    if(evt.keyCode=="67"&&evt.altKey&&evt.ctrlKey){
        main();
    }});

function main() {
    // Get the user's input
    var input = prompt("                                           🍪 -- Cheat Panel -- 🍪\n\nAdd Cookies (1) \n\n Set Cookies (2) \n\n Ruin the Fun (3) \n\n Set Bakery Name (4) \n\n Get All Upgrades (Doesn't Work) (5) \n\n Get All Achievements (Half Works) (6)\n\n Dump Logs (7) \n\nOpen Another Panel (8)\n\n🍪 More Coming Soon <3 🍪");
    // Check if the user's input is valid
    if (input == null || input == "") {
        // If the user's input is invalid, show an error
        alert("You need to enter something to hack!");
    } else {
     

        // Start the hack
        if (input == "1") {
            let cookies = prompt("How many cookies would you like to add?");
            
            Game.cookies = Game.cookies + parseInt(cookies);
            exit();
        } else if (input == "2") {
            let cookies = prompt("How many cookies would you like to set?");
            
            Game.cookies = parseInt(cookies);
            exit();
        } else if (input == "3") {
            Game.RuinTheFun();
            exit();
        } else if (input == "4") {
            let name = prompt("What would you like to name your bakery?");
            Game.bakeryName=name;
            Game.bakeryNameRefresh();
            exit();
        } else if (input == "5") {
            Game.SetAllUpgrade(1);
            exit();
        } else if (input == "6") {
            Game.SetAllAchievs(1);
            exit();
        } else if (input == "7") {
           console.log("Dumping Logs...");
              console.log("Cookies: " + Game.cookies);
                console.log("Cookies Per Second: " + Game.cookiesPs);
                console.log("Cookies Per Click: " + Game.cookiesPs);
                console.log("Bakery Name: " + Game.bakeryName);
                console.log("Frenzy: " + Game.frenzy);
                console.log("Frenzy Power: " + Game.frenzyPower);
                console.log("Frenzy Time: " + Game.frenzyTime);
                console.log("Frenzy Max: " + Game.frenzyMax);
                console.log("Frenzy Min: " + Game.frenzyMin);
                console.log("Dumped Logs!");
        } else if (input == "8") {
            Game.OpenSesame();
        } else {
            alert("Invalid Input!")
        }
    }
}

function wait(ms) {
    var start = new Date().getTime();
    var end = start;
    while (end < start + ms) {
        end = new Date().getTime();
    }
}
