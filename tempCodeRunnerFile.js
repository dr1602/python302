// javascript
let data = [21, 17, 35, "🍎", 40, 15];

data.forEach((item) => {
  try {
    // Verifica si el item es un número
    if (typeof item !== 'number') {
      throw new Error('Este elemento no es un número.');
    }

    // Si es un número, verifica si es mayor o menor de edad
    if (item >= 18) {
      console.log(`El número ${item} es mayor de edad.`);
    } else {
      console.log(`El número ${item} es menor de edad.`);
    }
  } catch (error) {
    console.log(error.message);
  }
});

/*
 
 */
