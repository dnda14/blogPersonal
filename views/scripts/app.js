let numeroSecreto = Math.floor(Math.random() *100)+10;
let numeroUser;
let contador = 1;
let cantMaxIntentos = 9;
while (1) {
    numeroUser = parseInt(prompt("Me indica un numero: "));
    console.log(numeroUser);
    if (numeroUser === numeroSecreto) {
        console.log("la respuesta es ", numeroSecreto == numeroUser ,`, el numero es ${numeroSecreto}`+ " y su respuesta: " + numeroUser+ " es correcta");
        alert(`obtuvo la respuesta en ${contador} ${contador >1 ?"intentos": "intento"}`)
        break;
    }else if(contador < cantMaxIntentos){
        if (numeroUser < numeroSecreto) {
            console.log("el numero es mayor que " + numeroUser);
            
        }else if (numeroUser > numeroSecreto) {
            console.log("el numero es menor que " + numeroUser);
        }
        contador++;
        
    }else{
        alert("tus intentos se han terminado");
        break;
    }
    
}
