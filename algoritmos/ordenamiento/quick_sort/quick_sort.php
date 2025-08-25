<?php
// Algoritmo Quick sort: ordena una lista dividiéndola en partes más pequeñas
/*
Cómo funciona:
- Escoge un pivote (un elemento de la lista, por ejemplo el primero).
- Compara todos los demás elementos con el pivote:
- Los menores que el pivote van a la izquierda.
- Los mayores que el pivote van a la derecha.
Ahora tienes tres partes: [menores] + [pivote] + [mayores].
*/
function quick_sort($lista) {
    if (count($lista) <= 1) {
        return $lista; // lista de 0 o 1 elemento ya está ordenada
    }

    $pivote = $lista[0];
    $menores = [];
    $mayores = [];

    for ($i = 1; $i < count($lista); $i++) {
        if ($lista[$i] <= $pivote) {
            $menores[] = $lista[$i];
        } else {
            $mayores[] = $lista[$i];
        }
    }

    return array_merge(quick_sort($menores), [$pivote], quick_sort($mayores));
}

// Ejemplo
$numeros = [5, 3, 8, 4, 2];
$ordenados = quick_sort($numeros);
print_r($ordenados);
?>
