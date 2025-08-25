<?php
// Algoritmo Selección (Selection sort)
function ordenarSeleccion($lista) {
    $n = count($lista);
    for ($i = 0; $i < $n - 1; $i++) {
        $indice_minimo = $i;
        for ($j = $i + 1; $j < $n; $j++) {
            if ($lista[$j] < $lista[$indice_minimo]) {
                $indice_minimo = $j; // actualizar índice del mínimo
            }
        }
        // intercambiar el mínimo con el elemento en posición i
        $temporal = $lista[$i];
        $lista[$i] = $lista[$indice_minimo];
        $lista[$indice_minimo] = $temporal;
    }
    return $lista;
}

// Ejemplo
$numeros = [5, 3, 8, 4, 2];
$ordenados = ordenarSeleccion($numeros);
print_r($ordenados);
?>
