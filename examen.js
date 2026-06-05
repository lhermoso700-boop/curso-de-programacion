console.log("Ejercicio 1");
const nombreProducto = "Tablet 10 pulgadas";
let precio = 450.99;
let stock = 25;
const envioGratis = true;

console.log("Nombre del producto: " + nombreProducto);
console.log("Precio: $" + precio);
console.log("Cantidad en stock: " + stock);
console.log("¿Tiene envío gratis?: " + envioGratis);

console.log("Ejercicio 2");
const cantidadComprada = 2;
const subtotal = precio * cantidadComprada;
const impuesto = subtotal * 0.07;
const totalFinal = subtotal + impuesto;

console.log("Subtotal: $" + subtotal.toFixed(2));
console.log("Total final (con 7% de impuesto): $" + totalFinal.toFixed(2));