<?php
// Algoritmo Inserción (Insertion sort)
function ordenarInsercion($lista) {
    $n = count($lista);
    for ($i = 1; $i < $n; $i++) {
        $clave = $lista[$i]; // elemento a insertar
        $j = $i - 1;
        // mover los elementos mayores a la derecha
        while ($j >= 0 && $lista[$j] > $clave) {
            $lista[$j + 1] = $lista[$j];
            $j--;
        }
        $lista[$j + 1] = $clave; // insertar en la posición correcta
    }
    return $lista;
}

// Ejemplo
$numeros = [5, 3, 8, 4, 2];
$ordenados = ordenarInsercion($numeros);
print_r($ordenados);
?>
