//paridad de un numero
let numero = 7;

if (numero % 2 === 0) {
    console.log(`${numero} es un número par.`);
} else {
    console.log(`${numero} es un número impar.`);
}

//sumatoria acumulativa
let suma = 0;

for (let i = 1; i <= 50; i++) {
    suma += i;
}

console.log(`La suma de los números del 1 al 50 es: ${suma}`);

//Traductor de Días
let dia = 3;
switch (dia) {
    case 1: console.log("Lunes"); break;
    case 2: console.log("Martes"); break;
    case 3: console.log("Miércoles"); break;
    case 4: console.log("Jueves"); break;
    case 5: console.log("Viernes"); break;
    case 6: console.log("Sábado"); break;
    case 7: console.log("Domingo"); break;
    default: console.log("Número inválido. Debe ser del 1 al 7.");
}

//Cuenta Regresiva
let contador = 10;
while (contador >= 0) {
    console.log(contador);
    if (contador === 0) {
        console.log("¡Despegue! 🚀");
    }
    contador--;
}

//Clasificador de Letras
let letra = 'a';
let letraMinuscula = letra.toLowerCase();
if (letraMinuscula === 'a' || letraMinuscula === 'e' || letraMinuscula === 'i' || letraMinuscula === 'o' || letraMinuscula === 'u') {
    console.log(`${letra} es una vocal.`);
} else {
    console.log(`${letra} es una consonante.`);
}

//El Algoritmo FizzBuzz
for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        console.log("FizzBuzz");
    } else if (i % 3 === 0) {
        console.log("Fizz");
    } else if (i % 5 === 0) {
        console.log("Buzz");
    } else {
        console.log(i);
    }
}

//Calculadora Básica
let num1 = 10;
let num2 = 0;
let operador = "/"; 
switch (operador) {
    case "+": console.log(`${num1} + ${num2} = ${num1 + num2}`); break;
    case "-": console.log(`${num1} - ${num2} = ${num1 - num2}`); break;
    case "*": console.log(`${num1} * ${num2} = ${num1 * num2}`); break;
    case "/":
        if (num2 === 0) {
            console.log("Error: No se puede dividir entre cero.");
        } else {
            console.log(`${num1} / ${num2} = ${num1 / num2}`);
        }
        break;
    default: console.log("Operador no válido.");
}

//Cálculo de Factorial
let n = 5;
let factorial = 1;
for (let i = n; i > 0; i--) {
    factorial *= i;
}
console.log(`El factorial de ${n} es: ${factorial}`);

//Verificador de Primos
let numPrimo = 29;
let esPrimo = true;
if (numPrimo <= 1) {
    esPrimo = false;
} else {
    for (let i = 2; i <= numPrimo / 2; i++) {
        if (numPrimo % i === 0) {
            esPrimo = false;
            break;
        }
    }
}
console.log(`¿El número ${numPrimo} es primo?: ${esPrimo}`);

//Patrón Cuadrado
let dimension = 5;
for (let i = 0; i < dimension; i++) {
    let fila = "";
    for (let j = 0; j < dimension; j++) {
        fila += "* ";
    }
    console.log(fila);
}

//Sucesión de Fibonacci
let a = 0, b = 1;
console.log(a);
console.log(b);
for (let i = 3; i <= 15; i++) {
    let siguiente = a + b;
    console.log(siguiente);
    a = b;
    b = siguiente;
}

//Conjetura de Collatz
let nCollatz = 6;
console.log(`Secuencia de Collatz para ${nCollatz}:`);
while (nCollatz !== 1) {
    console.log(nCollatz);
    if (nCollatz % 2 === 0) {
        nCollatz = nCollatz / 2;
    } else {
        nCollatz = (nCollatz * 3) + 1;
    }
}
console.log(1);

//Número Perfecto
let numPerfecto = 28;
let sumaDivisores = 0;
for (let i = 1; i < numPerfecto; i++) {
    if (numPerfecto % i === 0) {
        sumaDivisores += i;
    }
}
if (sumaDivisores === numPerfecto) {
    console.log(`${numPerfecto} es un número perfecto.`);
} else {
    console.log(`${numPerfecto} NO es un número perfecto.`);
}

//Decimal a Binario
let decimal = 25;
let temporal = decimal;
let binario = "";
if (temporal === 0) {
    binario = "0";
} else {
    while (temporal > 0) {
        let bit = temporal % 2;
        binario = bit + binario;
        temporal = Math.floor(temporal / 2);
    }
}
console.log(`El número decimal ${decimal} en binario es: ${binario}`);

//Triángulo de Números
let filasTriangulo = 5;
for (let i = 1; i <= filasTriangulo; i++) {
    let fila = "";
    for (let j = 1; j <= i; j++) {
        fila += j + " ";
    }
    console.log(fila);
}