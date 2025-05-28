# 🛒 Sistema de Gestión de Negocio

Este proyecto permite gestionar clientes, empleados, productos y ventas de un negocio.

## 🚀 Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/usuario/mi_negocio.git

Identificación de Entidades y Atributos

-- Cliente

ID_Cliente

Nombre

Apellido

Email

Teléfono

-- Producto

ID_Producto

Nombre

Precio

Stock

Categoría

-- Venta

ID_Venta

Fecha

Total

ID_Cliente (FK)

Productos comprados

-- Empleado

ID_Empleado

Nombre

Apellido

Puesto

Salario

                  -- -- Grafica -- --
                        Persona
                           |
          ---------------------------------
          |                               |
       Cliente                        Empleado


