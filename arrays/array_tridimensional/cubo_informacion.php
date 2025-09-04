<?php
// Cubo de información como array 3D en PHP
// Eje 0: Meses (Enero, Febrero, Marzo)
// Eje 1: Productos (A, B, C)
// Eje 2: Regiones (Norte, Sur, Centro)

$cubo = [
    // Enero
    [
        [120, 0, 0],   // Producto A
        [200, 0, 0],   // Producto B
        [150, 0, 0]    // Producto C
    ],
    // Febrero
    [
        [0, 180, 0],   // Producto A
        [0, 220, 0],   // Producto B
        [0, 90, 0]     // Producto C
    ],
    // Marzo
    [
        [0, 0, 160],   // Producto A
        [0, 0, 210],   // Producto B
        [0, 0, 130]    // Producto C
    ]
];

// Acceder a un valor:
// Ventas de Febrero (índice 1), Producto B (índice 1), Región Sur (índice 1)
$ventas = $cubo[1][1][1];

echo "Ventas de Producto B en Febrero (Sur): " . $ventas;
