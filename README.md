#Sistema de Ventas Pandilla de Duendes

##El sistema se encuentra dividido en distintos modulos con opciones internas, se puede acceder mediante un menu de opciones anidados, en varios modulos se comparte distinta informacion desde los Json. Por ejemplo: En ventas no solo se accede al.json de ventas, sino que al de inventario tambien.
nota:Los ID en todo el ERP se manejan de manera secuencial(desde 1.)

-Modulo 1, Ventas:

El sistema utiliza archivos JSON locales para la persistencia de datos (Ventas, Inventario, Empleados).

Características del Módulo de Ventas
El sistema ofrece un flujo de venta robusto y detallado:

1.Gestión de la Venta (Registrar Venta)

Selección de Empleado: Toda venta debe ser asociada a un empleado registrado.

Flujo Interactivo: Menú dinámico para añadir, modificar o quitar productos de la venta actual.

Verificación de Stock: Comprobación de disponibilidad de stock antes de agregar productos y antes de confirmar la transacción.

Descuentos: Aplicación de porcentajes de descuento al total de la venta. ATENCION!!! debe ser mayor a 0 y menor o igual a 98, acepta enteros y decimales.

Transaccionalidad: Confirmación final de la venta, se almacena en el json de ventas y actualiza el stock en el inventario.

2.Documentación y Registro

Facturación en Pantalla: Impresión detallada de la "Factura de Venta" una vez completada la transacción, mostrando ID, fecha, empleado, desglose de ítems y costo final.

Registro de Datos: Guarda la información de la venta (detallada) datos_ventas.json.

3.Gestión de Promociones (Módulo Secundario)

Permite aplicar y gestionar promociones temporales basadas en la categoría de los productos. Estas se registran FUERA de las ventas, mientras que los descuentos no.

Las promociones establecen un nuevo precio_promocion que se usa automáticamente al registrar una venta, teniendo prioridad sobre el precio original, cuando se elimine la promocion, se volvera a trabajar con el precio original.

                                    EJEMPLO DE JSON DE VENTAS:
                                        {
                                        "ventas": [
                                            {
                                            "id": "1",
                                            "venta": 10000.0,
                                            "fecha_venta": "2025-11-05",
                                            "info_venta": [
                                                {
                                                "id": "1",
                                                "nombre": "lapiz",
                                                "cantidad": 10,
                                                "costo": 10000.0
                                                }
                                            ],
                                            "descuento": 0.0,
                                            "empleado_id": "1",
                                            "empleado_nombre": "Lucas Gamer"
                                            }
                                        ],
                                        "prox_id": 2
                                                             }

-Modulo 2: Inventario.

1.Registrar Producto (agregar_producto): Permite el alta de nuevos artículos con detalles como nombre, costo, precio de venta, stock y categoría. Incluye validación de precios (el precio de venta debe ser superior al costo y a $50) y registro de la fecha de alta.

2.Ver Todos los Productos (ver_todos_los_productos): Muestra un listado completo de todos los artículos en el inventario, incluyendo sus atributos clave y estado. Utiliza un sistema de paginación (imprimir_tabla_x_paginas) para manejar grandes volúmenes de datos en la consola.

3.Ver Detalles del Producto (detalles_producto): Permite seleccionar un producto para visualizar todos sus datos en detalle, incluyendo fechas de alta y última modificación.

4.Actualizar Producto (actualizar_producto): Permite seleccionar un producto y modificar selectivamente cualquiera de sus atributos principales (precio, nombre, costo, stock, categoría, o rotación). Registra la fecha de la última modificación.

5.Cambiar Estado Producto (estado_producto): Alterna el estado de un producto entre "activo" e "inactivo". El estado de inactividad no te permite registrarlos en ventas posteriormente y ademas, en caso de ser listado en alguna funcion, se NOTIFICARA ese estado.

6.Eliminar Producto (eliminar_producto): Permite la eliminación permanente de un artículo, pero restringe esta acción si el producto tiene historial de ventas asociado (requiriendo que el usuario use la opción de Cambiar Estado).

7.Buscar Producto (buscar_producto): Ofrece un menú de búsqueda avanzada con múltiples criterios de filtro: por Nombre, Categoría, Rango de Precio, Rango de Stock, Rotación (Alta/Baja) y Estado (Activo/Inactivo). Muestra los resultados en una tabla paginada.

8.Mostrar Productos con Bajo Stock (alerta_stock_bajo): Genera alertas sobre productos cuyo stock es menor o igual a 20 unidades. Permite filtrar las alertas para ver solo los productos de Alta Rotación o ver la lista completa.
EJEMPLO DE JSON INVENTARIO:

                                        {
                                        "productos": [
                                            {
                                            "id": "1",
                                            "nombre": "lapiz",
                                            "costo": 300.0,
                                            "precio": 1000.0,
                                            "stock": 290,
                                            "alta_rotacion": "si",
                                            "categoria": "util escolar",
                                            "fecha_alta": "2025-11-05",
                                            "ultima_modificacion": "2025-11-05",
                                            "estado": "activo"
                                            }
                                        ],
                                        "prox_id": 2
                                                             }
-Modulo 3: Empleados.
El sistema ofrece herramientas esenciales para la gestión del personal, reflejadas en las opciones de su menú principal:

1.Registrar Nuevo Empleado (registrar_empleados): Permite el alta de nuevos empleados, asignándoles un ID , registrando su nombre, puesto y sueldo. Incluye validación de sueldo (debe ser un valor positivo) y registra la fecha de alta automáticamente.

2.Editar Datos de Empleado (editar_datos_de_empleados): Permite la selección de un empleado y la modificación de la mayoría de sus atributos (nombre, puesto, sueldo). Restringe la modificación de campos sensibles como id y fecha_de_alta.

3.Registrar Asistencia (registrar_asistencia): Permite marcar la entrada de un empleado, registrando la fecha y hora actual en una lista de asistencias. Solo permite el registro para empleados cuyo estado es "Activo".

4.Asignar Roles a Empleados (asignar_roles): Permite seleccionar un empleado y asignarle un campo de rol personalizado .

Dar de Baja o Alta a un Empleado (dar_de_baja_alta): Controla el estado operativo de un empleado, alternándolo entre "Activo" e "Inactivo".

Mostrar empleados (mostrar_empleados): Visualiza todos los empleados registrados en el sistema mediante una tabla paginada.

EJEMPLO DE JSON DE EMPLEADOS:

                                        {
                                        "empleados": [
                                            {
                                            "id": "1",
                                            "nombre": "Lucas Gamer",
                                            "puesto": "Jefe",
                                            "sueldo": 30000,
                                            "fecha_de_alta": "2025-11-05",
                                            "asistencias": [],
                                            "estado": "Activo"
                                            }
                                        ],
                                        "prox_id": 2
                                                             }
-Modulo 4: Proveedores.
Registrar Proveedor (registrar_provedores): Permite el alta de nuevos proveedores. Requiere que se ingrese al menos la marca o el tipo de producto con el que trabaja el proveedor para asegurar un registro. Registra automáticamente la fecha de alta.

2.Pedidos (pedidos): Accede al submenú de gestión de pedidos, que incluye las siguientes opciones:

        -Registrar Pedido (registrar_pedidos): Permite seleccionar un proveedor y cargar una lista de productos y cantidades a solicitar. Guarda el pedido en el registro del proveedor.

        -Ver Pedidos (ver_pedidos): Muestra una lista de todos los proveedores que tienen pedidos pendientes, con el detalle de los ítems y cantidades solicitadas.

        -Eliminar Pedidos (eliminar_pedidos): Elimina un pedido asignado a un proveedor.

3.Buscar Proveedores (buscar_proveedor): Ofrece un menú de búsqueda avanzada que permite encontrar proveedores mediante filtros por Nombre, Marca o Tipo de Producto.

4.Mostrar proveedores (mostrar_proveedores): Muestra una lista organizada de proveedores. Filtrandolos por MARCA, en caso de no tener registrada una marca, aparecera en otros.

                                    EJEMPLO JSON PROVEEDORES:
                                    {
                                        "proveedores": [
                                            {
                                            "nombre": "juan",
                                            "marca": "coca",
                                            "tipo_de_producto": "no info",
                                            "fecha_alta": "2025-11-05",
                                            "pedido": []
                                            },
                                            {
                                            "nombre": "gabriel",
                                            "marca": "no info",
                                            "tipo_de_producto": "gaseosas",
                                            "fecha_alta": "2025-11-05",
                                            "pedido": []
                                            }
                                        ],
                                        "prox_id": 3
                                                            }

-Modulo 5: Reportes.
El módulo está dividido en tres áreas principales de análisis: Inventario, Ventas y Empleados.

1.Reportes de Inventario. Incluye las siguientes 3 opciones:

    I.Ver Productos Inactivos (ver_inactivos): Muestra un listado simple de todos los productos que han sido marcados con el estado "inactivo".

    II.Ver Valor Total del Inventario (ver_valor_del_inventario): Calcula el valor total del stock considerando el COSTO del mismo. Desglosa este valor entre productos de Alta Rotación (AR) y productos que No son de Alta Rotación (NOAR).Finalmente, se muestra un total.

    III.Ver Valor por Categoría (valor_inventario_por_categoria): Agrupa y resume el inventario por categoría. Muestra el valor total del stock por categoría, el stock total y el número de productos activos e inactivos en esa categoría.

2.Reportes de Venta. Incluye las siguientes 5 opciones:

    I.Mostrar Ventas por Período de Tiempo (mostrar_reporte_por_periodo): Permite segmentar el historial de ventas para generar reportes por períodos Diarios, Mensuales o Anuales, mostrando el monto total vendido en el período.

    II.Ventas por Empleado (reporte_ventas_por_empleado): Genera un resumen que muestra el monto total vendido y la cantidad de transacciones realizadas por cada empleado.

    III.Top Productos Vendidos (reporte_top_productos): Identifica los 5 productos más vendidos en la historia del sistema, basándose en la cantidad total de unidades vendidas.

    IV.Margen por Producto (reporte_margen_por_producto): Reporte analítico detallado que calcula el Ingreso, el Costo Estimado (stock x costo unitario) y el Margen de Ganancia (Monto y Porcentaje) para cada producto vendido.

    V.Ventas por Categoría (reporte_ventas_por_categoria): Agrupa los ingresos totales por la categoría del producto, mostrando la cantidad vendida y el porcentaje de  esa categoría en los ingresos totales.

3.Reportes de Empleados: Incluye las siguientes 2 opciones.

    I.Reporte Asistencias (reporte_asistencias): Muestra una tabla con el total de asistencias registradas por cada empleado desde su fecha de alta.

    II.Reporte Sueldos (reporte_sueldos): Lista el sueldo de cada empleado. Proporciona Informacion clave general como sueldo mas bajo, mas alto, promedio.

Con esto concluimos, en caso de surgir algun cambio en una version posterior, se añadira en novedades.md y se actualizara en este mismo archivo.
Att: Pandilla De Duendes.
