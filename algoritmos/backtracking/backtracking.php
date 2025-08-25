<?php
// Algoritmo Backtracking(Vueltra atrás)
function retroceso($maximo, $objetivo, $inicio = 1, $camino = []) {
    if ($objetivo == 0) {
        echo implode(", ", $camino) . "\n";
        return;
    }

    for ($numero = $inicio; $numero <= $maximo; $numero++) {
        if ($numero > $objetivo) continue;
        $camino[] = $numero;  // agregar número al camino actual
        retroceso($maximo, $objetivo - $numero, $numero + 1, $camino); // explorar siguiente paso
        array_pop($camino);   // deshacer elección (retroceder)
    }
}

// Ejemplo: combinaciones de 1 a 5 que sumen 5
retroceso(5, 5);
?>
