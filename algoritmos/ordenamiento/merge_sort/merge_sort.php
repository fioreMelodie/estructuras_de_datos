<?php
// Algoritmo (Merge sort)
function merge_sort($lista) {
    $n = count($lista);
    if ($n <= 1) {
        return $lista; // lista de 0 o 1 elemento ya está ordenada
    }

    $medio = intdiv($n, 2);
    $izquierda = array_slice($lista, 0, $medio);
    $derecha = array_slice($lista, $medio);

    // ordenar recursivamente
    $izquierda = merge_sort($izquierda);
    $derecha = merge_sort($derecha);

    // fusionar listas ordenadas
    return fusionar($izquierda, $derecha);
}

function fusionar($izquierda, $derecha) {
    $resultado = [];
    while (count($izquierda) > 0 && count($derecha) > 0) {
        if ($izquierda[0] <= $derecha[0]) {
            $resultado[] = array_shift($izquierda);
        } else {
            $resultado[] = array_shift($derecha);
        }
    }
    // añadir los elementos restantes
    return array_merge($resultado, $izquierda, $derecha);
}

// Ejemplo
$numeros = [5, 3, 8, 4, 2];
$ordenados = merge_sort($numeros);
print_r($ordenados);
?>
