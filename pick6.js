const readline = require('readline-sync');

function ticket() {
    let user_ticket = []
    for (let i = 0; i < 5; ++i)
    user_ticket.push(Math.floor(((Math.random() * 100) + 1)))
    console.log(user_ticket);
}

console.log(ticket());