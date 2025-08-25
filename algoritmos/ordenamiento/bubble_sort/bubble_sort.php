<?php
// Algoritmo Burbuja (bubble sort)
function ordenarBurbuja($lista) {
    $n = count($lista);
    for ($i = 0; $i < $n - 1; $i++) {
        for ($j = 0; $j < $n - $i - 1; $j++) {
            if ($lista[$j] > $lista[$j + 1]) {
                // intercambiar elementos
                $temporal = $lista[$j];
                $lista[$j] = $lista[$j + 1];
                $lista[$j + 1] = $temporal;
            }
        }
    }
    return $lista;
}

// Ejemplo: Ordenar números dentro de un array
$numeros = [5, 3, 8, 4, 2];
$ordenados = ordenarBurbuja($numeros);
print_r($ordenados);
?>
