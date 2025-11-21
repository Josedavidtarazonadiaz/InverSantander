# 🏢 Sistema de Gestión de Inversiones y Empresas Emergentes

Sistema integral para la administración de empresas emergentes, inversionistas y procesos de inversión, implementado con estructuras de datos avanzadas en Python.

## 📋 Descripción

Este sistema permite gestionar de manera eficiente:
- Registro y administración de empresas emergentes
- Gestión de inversionistas y su capital disponible
- Procesamiento de solicitudes de inversión
- Seguimiento cronológico de inversiones y logros empresariales
- Organización por sectores económicos y geográficos
- Indexación y búsqueda de empresas por capital

## 🔑 Características Principales

### 1. **Gestión de Usuarios**
- **Administradores**: Control total del sistema con autenticación segura (SHA-256)
- **Empresas**: Acceso a sus datos, solicitudes y cronología
- **Inversionistas**: Visualización de oportunidades y gestión de inversiones

### 2. **Estructuras de Datos Implementadas**

#### 📊 Cola (Queue)
- Gestión de solicitudes de inversión (FIFO)
- Procesamiento de quejas y reclamos
- Archivo: `micn.py` - Clase `Nictname`

#### 🔗 Lista Doblemente Enlazada
- Trazabilidad histórica de inversiones y logros
- Navegación bidireccional en cronologías
- Archivo: `micn.py` - Clase `NoQ`

#### 🌲 Árbol Binario de Búsqueda (BST)
- Indexación de empresas por capital
- Búsqueda eficiente por rangos de capital
- Cálculo de estadísticas (promedio, mínimo, máximo)
- Archivo: `Mint.py` - Clase `Pencil`

#### 🌳 Árbol General N-ario
- Organización jerárquica de sectores
- Estructura flexible para múltiples hijos
- Archivo: `Britain.py` - Clase `Mong`

## 🚀 Instalación

### Requisitos
- Python 3.7 o superior
- Sistema operativo: Windows, Linux o macOS

### Pasos de Instalación

```bash
# Clonar o descargar el repositorio
git clone [URL_DEL_REPOSITORIO]

# Navegar al directorio del proyecto
cd sistema-gestion-inversiones

# Ejecutar el sistema
python INTENTO.py
```

## 📂 Estructura del Proyecto

```
proyecto/
│
├── INTENTO.py          # Archivo principal del sistema
├── OPTIONS.py          # Clases de opciones, seguridad y operaciones
├── micn.py            # Implementación de Cola y Lista Doblemente Enlazada
├── Mint.py            # Implementación de Árbol Binario de Búsqueda
├── Britain.py         # Implementación de Árbol N-ario
├── admins.json        # Datos persistentes (generado automáticamente)
└── README.md          # Este archivo
```

## 💻 Uso del Sistema

### Inicio de Sesión

1. **Primera vez**: Registrarse como administrador
2. **Usuarios existentes**: Iniciar sesión según tipo de usuario

### Menú Principal (Administrador)

```
1. Opciones de Empresa
   - Agregar empresa
   - Ver cronología de inversiones
   - Procesar solicitudes

2. Opciones de Inversionista
   - Registrar inversionista
   - Realizar inversiones
   - Ver cronologías

3. Opciones de Sector
   - Agregar sector económico
   - Agregar sector geográfico
```

### Funcionalidades por Tipo de Usuario

#### 👨‍💼 Empresas
- Ver información de la empresa
- Crear solicitudes de inversión
- Ver solicitudes pendientes
- Consultar cronología de inversiones recibidas
- Agregar logros empresariales
- Presentar quejas o reclamos

#### 💰 Inversionistas
- Ver información personal
- Realizar inversiones en empresas
- Ver cronología de empresas
- Buscar empresas por capital
- Ver estadísticas del mercado
- Consultar inversiones realizadas

#### 🔐 Administradores
- Control completo del sistema
- Gestión de empresas e inversionistas
- Procesamiento de solicitudes
- Administración de sectores

## 🔐 Seguridad

- **Autenticación**: Sistema de login con contraseñas encriptadas (SHA-256)
- **Persistencia**: Datos guardados en formato JSON
- **Validación**: Verificación de entradas y manejo de errores
- **Log de errores**: Registro automático en `guardador de Errores.txt`

## 📊 Estructuras de Datos - Detalles Técnicos

### Cola de Solicitudes
```python
# Capacidad configurable (default: 100)
cola_solicitudes = Nictname(capacidad=100)

# Operaciones: O(1)
- enqueQ(dato)    # Agregar al final
- DeqQ(dato)      # Remover del frente
- frentENQ()      # Ver frente
- UltimENQ()      # Ver último
```

### Lista Doblemente Enlazada (Cronología)
```python
# Navegación bidireccional
- csig (siguiente)
- Prant (anterior)

# Ventajas:
- Recorrido hacia adelante y atrás
- Inserción eficiente al final: O(1)
- Ideal para historial temporal
```

### Árbol Binario de Búsqueda
```python
# Indexación por capital
arbol = Pencil()

# Operaciones: O(log n) promedio
- InsertNod(capital)              # Insertar
- LNE(min, max)                   # Buscar rango
- CalcularPromedio()              # Estadísticas
- IdentificarFB(nodo)            # Factor de balance
```

## 📈 Casos de Uso

### 1. Registrar una Empresa
```
Admin → Opciones Empresa → Agregar Empresa
→ Ingresar: nombre, NIT, tipo, fecha, dirección, capital
→ Empresa indexada automáticamente en árbol BST
```

### 2. Procesar Solicitud de Inversión
```
Empresa → Crear solicitud → Especificar monto y proyecto
→ Solicitud agregada a cola (FIFO)
→ Admin procesa en orden de llegada
→ Aprobación/Rechazo
```

### 3. Buscar Empresas por Capital
```
Inversionista → Buscar por capital
→ Ingresar rango (min - max)
→ Búsqueda eficiente en árbol BST
→ Listado de empresas en el rango
```

### 4. Ver Cronología de Empresa
```
Usuario → Cronología de empresa
→ Seleccionar empresa
→ Elegir orden: antiguo→reciente o reciente→antiguo
→ Lista doblemente enlazada permite ambas direcciones
```

## 🛠️ Mantenimiento

### Respaldo de Datos
Los datos se guardan automáticamente en `admins.json`. Se recomienda:
- Hacer copias de seguridad periódicas
- Verificar integridad del archivo JSON

### Log de Errores
El sistema genera automáticamente `guardador de Errores.txt` con:
- Fecha y hora del error
- Descripción del problema
- Útil para debugging

## 🤝 Contribución

Para contribuir al proyecto:
1. Fork del repositorio
2. Crear rama para nueva funcionalidad
3. Commit de cambios
4. Push a la rama
5. Crear Pull Request

## 📝 Notas Técnicas

- **Complejidad temporal**:
  - Búsqueda en BST: O(log n) promedio
  - Operaciones de cola: O(1)
  - Inserción en lista enlazada: O(1)

- **Persistencia**: JSON para facilitar lectura/escritura

- **Escalabilidad**: Estructuras de datos eficientes para grandes volúmenes

## 🐛 Solución de Problemas

### Problema: No se guardan los datos
**Solución**: Verificar permisos de escritura en el directorio

### Problema: Error al cargar datos
**Solución**: Verificar formato del archivo `admins.json`

### Problema: Cola llena
**Solución**: Aumentar capacidad en `Op_empresa(capacidad=100)`

## 📧 Contacto y Soporte

Para reportar bugs o solicitar funcionalidades, consultar la documentación del código o contactar al equipo de desarrollo.

## 📄 Licencia

Este proyecto es de uso académico/educativo. Consultar términos específicos de uso.

---

**Versión**: 1.0  
**Última actualización**: 2025  
**Desarrollado con**: Python 3.13.0
