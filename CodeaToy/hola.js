const prompt = require('prompt-sync')();
let nombre = prompt("¿Cuál es tu nombre?");
let trabajo = prompt("¿Cuál es tu trabajo?");
let adj1 = prompt("Dime un adjetivo:");
let adj2 = prompt("Otro adjetivo:");
let comida1 = prompt("¿Cuál es tu comida favorita?");
let comida2 = prompt("¿Y otra comida que te guste?");
let sentimiento = prompt("¿Cómo te sientes hoy?");

console.log(`Un día, ${nombre}, el ${adj1} ${trabajo} estaba ${sentimiento}. 
Decidió prepararse una ${adj2} ${comida1} para sentirse mejor. Mientras comía,
recordó la vez que probó por primera vez ${comida2} y sonrió.`);