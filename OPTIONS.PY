import datetime as dt
import hashlib
import json
from micn import Nictname, NoQ
from Mint import Pencil, Night
from Britain import Mong, Mangost

class Options:
    def MenuPrincipal(self):
        print("--- MENU PRINCIPAL ---")
        print("1. Opciones de Empresa")
        print("2. Opciones de Inversionista")
        print("3. Opciones de Sector (Económico/Geográfico)")
        print("4. Salir")
        print("Opcion: ")

    def MenuEmpresa(self):
        print("--- MENU EMPRESA ---")
        print("1. Agregar Empresa")
        print("2. Mirar cronologia de la empresa")
        print("3. Mirar cronologia de inversiones de la empresa")
        print("4. Volver al Menu Principal")
        print("Opcion: ")

    def MenuInversionista(self):
        print("--- MENU INVERSIONISTA ---")
        print("1. Agregar Inversionista")
        print("2. Mirar cronologia de la empresa")
        print("3. Mirar los productosa de la empresa")
        print("4. Volver al Menu Principal")
        print("Opcion: ")

    def MenuSector(self):
        print("--- MENU SECTOR ---")
        print("1. Agregar Sector Económico")
        print("2. Agregar Sector/Barrio/Localidad (Geográfico)")
        print("3. Volver al Menu Principal")
        print("Opcion: ")

    def AddError(self, error=None):
        with open("guardador de Errores.txt", "a") as f:
            if error is not None:
                now = dt.datetime.now()
                Log_En = f"{now.strftime('%d/%m/%Y %H:%M:%S')} - {error}\n"
                f.write(Log_En)
            else:
                pass

    def Choice(self):
        try:
            choice = int(input())
            return choice
        except Exception as e:
            print("Opcion invalida")
            self.AddError(e)
            print(f"Error tipo {e}: fue generado")
            return None

        
class Security:
    def Log_Up_Admin(self, datos):
        datos_admin = {}

        print("Bienvenido usuario")
        datos_admin["Usuario"] = input("Ingrese su nombre: ")

        # Crear contraseña
        contrasena = input("Cree una contraseña: ")

        # Verificar contraseña
        while True:
            contrasena_verificar = input("Verificar contraseña: ")
            if contrasena == contrasena_verificar:
                break
            print("Las contraseñas no coinciden. Intente nuevamente.")

        # Encriptar contraseña (hash)
        hash_contra = hashlib.sha256(contrasena.encode()).hexdigest()
        datos_admin["Contrasena"] = hash_contra

        # Guardar los datos en la estructura
        datos["d_Admin"].append(datos_admin)

        # Guardar en archivo JSON
        with open("admins.json", "w") as f:
            json.dump(datos, f, indent=4)

        print("Usuario creado exitosamente")
        return datos_admin

    def Log_in_Admin(self, datos):
        print("Bienvenido usuario")
        Nombre = input("Ingrese su nombre: ")
        Contrasena_R = input("Ingrese su contraseña: ")

        # Convertir contraseña ingresada a hash
        Contrasena_R_hash = hashlib.sha256(Contrasena_R.encode()).hexdigest()

        for admin in datos["d_Admin"]:
            if admin["Usuario"] == Nombre:
                # Verificar contraseña
                while admin["Contrasena"] != Contrasena_R_hash:
                    print("Contraseña incorrecta")
                    Contrasena_R = input("Ingrese su contraseña: ")
                    Contrasena_R_hash = hashlib.sha256(Contrasena_R.encode()).hexdigest()

                print("Inicio de sesión exitoso")
                return admin

        print("Usuario no encontrado")
        return None


class Op_inversion:
    """
    Trazabilidad histórica: Permite registrar y visualizar la cronología 
    de logros e inversiones de las empresas mediante una Lista Doblemente Enlazada,
    facilitando el seguimiento de su desarrollo en el tiempo.
    """
    def __init__(self):
        # Diccionario para almacenar listas doblemente enlazadas por empresa
        self.cronologias_empresas = {}
    
    def _CrearListaEmpresa(self, empresa):
        """Crea una nueva lista doblemente enlazada para una empresa"""
        if empresa not in self.cronologias_empresas:
            # Crear nodo cabecera con info de la empresa
            nodo_cabecera = NoQ(f"EMPRESA: {empresa}")
            self.cronologias_empresas[empresa] = {
                "cabecera": nodo_cabecera,
                "ultimo": nodo_cabecera,
                "cantidad": 0
            }
    
    def AgregarInversion(self, datos):
        print("\n--- AGREGAR INVERSION ---")
        print("Nombre de la empresa receptora:")
        empresa = input().strip()
        
        print("Nombre del inversionista:")
        inversionista = input().strip()
        
        print("Monto de inversión:")
        try:
            monto = float(input())
        except ValueError:
            print("Error: Monto inválido")
            return None
        
        print("Fecha de inversión (DD/MM/AAAA):")
        fecha = input().strip()
        
        # Crear registro de inversión
        registro = {
            "tipo": "INVERSION",
            "inversionista": inversionista,
            "monto": monto,
            "fecha": fecha,
            "timestamp": dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        }
        
        # Crear lista si no existe
        self._CrearListaEmpresa(empresa)
        
        # Crear nuevo nodo y agregarlo al final
        nuevo_nodo = NoQ(registro)
        ultimo_nodo = self.cronologias_empresas[empresa]["ultimo"]
        
        # Enlazar el nuevo nodo
        ultimo_nodo.csig = nuevo_nodo
        nuevo_nodo.Prant = ultimo_nodo
        
        # Actualizar el último nodo
        self.cronologias_empresas[empresa]["ultimo"] = nuevo_nodo
        self.cronologias_empresas[empresa]["cantidad"] += 1
        
        print(f"✓ Inversión registrada exitosamente para {empresa}")
        print(f"Total de registros: {self.cronologias_empresas[empresa]['cantidad']}")
        return registro
    
    def AgregarLogro(self, datos):
        print("\n--- AGREGAR LOGRO ---")
        print("Nombre de la empresa:")
        empresa = input().strip()
        
        print("Descripción del logro:")
        descripcion = input().strip()
        
        print("Fecha del logro (DD/MM/AAAA):")
        fecha = input().strip()
        
        # Crear registro de logro
        registro = {
            "tipo": "LOGRO",
            "descripcion": descripcion,
            "fecha": fecha,
            "timestamp": dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        }
        
        # Crear lista si no existe
        self._CrearListaEmpresa(empresa)
        
        # Crear nuevo nodo y agregarlo al final
        nuevo_nodo = NoQ(registro)
        ultimo_nodo = self.cronologias_empresas[empresa]["ultimo"]
        
        # Enlazar el nuevo nodo
        ultimo_nodo.csig = nuevo_nodo
        nuevo_nodo.Prant = ultimo_nodo
        
        # Actualizar el último nodo
        self.cronologias_empresas[empresa]["ultimo"] = nuevo_nodo
        self.cronologias_empresas[empresa]["cantidad"] += 1
        
        print(f"✓ Logro registrado exitosamente para {empresa}")
        print(f"Total de registros: {self.cronologias_empresas[empresa]['cantidad']}")
        return registro
    
    def MirarCronologiaEmpresa(self, datos):
        print("\n--- CRONOLOGIA DE LA EMPRESA ---")
        print("Nombre de la empresa:")
        empresa = input().strip()
        
        if empresa not in self.cronologias_empresas:
            print(f"No se encontró información para la empresa: {empresa}")
            return None
        
        lista_empresa = self.cronologias_empresas[empresa]
        
        print(f"\n{'='*50}")
        print(f"  CRONOLOGIA DE {empresa}")
        print(f"{'='*50}")
        print(f"Total de registros: {lista_empresa['cantidad']}")
        
        # Opción de visualización
        print("\n¿Cómo desea visualizar la cronología?")
        print("1. Desde el más antiguo al más reciente (Adelante)")
        print("2. Desde el más reciente al más antiguo (Atrás)")
        print("Opción: ", end="")
        
        try:
            opcion = int(input())
        except ValueError:
            opcion = 1
        
        registros = []
        
        if opcion == 1:
            # Recorrer hacia adelante (del primero al último)
            print(f"\n--- CRONOLOGIA (Más antiguo → Más reciente) ---\n")
            nodo_actual = lista_empresa["cabecera"].csig  # Saltar cabecera
            contador = 1
            
            while nodo_actual is not None:
                reg = nodo_actual.Idat
                registros.append(reg)
                
                if isinstance(reg, dict):
                    print(f"{contador}. [{reg['tipo']}]")
                    if reg['tipo'] == 'INVERSION':
                        print(f"   Inversionista: {reg['inversionista']}")
                        print(f"   Monto: ${reg['monto']:,.2f}")
                    elif reg['tipo'] == 'LOGRO':
                        print(f"   Descripción: {reg['descripcion']}")
                    print(f"   Fecha: {reg['fecha']}")
                    print(f"   Registrado: {reg['timestamp']}")
                    print()
                    contador += 1
                
                nodo_actual = nodo_actual.csig
        
        else:
            # Recorrer hacia atrás (del último al primero)
            print(f"\n--- CRONOLOGIA (Más reciente → Más antiguo) ---\n")
            nodo_actual = lista_empresa["ultimo"]
            contador = 1
            
            while nodo_actual is not None and nodo_actual != lista_empresa["cabecera"]:
                reg = nodo_actual.Idat
                registros.append(reg)
                
                if isinstance(reg, dict):
                    print(f"{contador}. [{reg['tipo']}]")
                    if reg['tipo'] == 'INVERSION':
                        print(f"   Inversionista: {reg['inversionista']}")
                        print(f"   Monto: ${reg['monto']:,.2f}")
                    elif reg['tipo'] == 'LOGRO':
                        print(f"   Descripción: {reg['descripcion']}")
                    print(f"   Fecha: {reg['fecha']}")
                    print(f"   Registrado: {reg['timestamp']}")
                    print()
                    contador += 1
                
                nodo_actual = nodo_actual.Prant
        
        return registros


class Op_empresa:
    """
    Gestión de solicitudes: Utiliza una Cola para ordenar y procesar 
    solicitudes de inversión, quejas o reclamos en orden de llegada (FIFO),
    asegurando un manejo justo y organizado.
    """
    def __init__(self, capacidad=100):
        # Cola para solicitudes de inversión
        self.cola_solicitudes_inversion = Nictname(capacidad)
        # Cola para quejas y reclamos
        self.cola_quejas = Nictname(capacidad)
        # Contador de solicitudes
        self.contador_solicitudes = 0
    
    def AgregarEmpresa(self, datos):
        print("\n--- AGREGAR EMPRESA ---")
        
        empresa_data = {}
        
        print("Nombre de la empresa:")
        empresa_data["nombre"] = input().strip()
        
        print("NIT de la empresa:")
        empresa_data["nit"] = input().strip()
        
        print("Tipo de empresa:")
        empresa_data["tipo"] = input().strip()
        
        print("Fecha de creación (DD/MM/AAAA):")
        empresa_data["fecha_creacion"] = input().strip()
        
        print("Dirección:")
        empresa_data["direccion"] = input().strip()
        
        print("Capital inicial:")
        try:
            empresa_data["capital"] = float(input())
        except ValueError:
            print("Error: Capital inválido")
            return None
        
        # Agregar a los datos generales
        if "empresas" not in datos:
            datos["empresas"] = []
        
        datos["empresas"].append(empresa_data)
        
        print(f"✓ Empresa {empresa_data['nombre']} agregada exitosamente")
        return empresa_data
    
    def AgregarSolicitudInversion(self, datos):
        print("\n--- AGREGAR SOLICITUD DE INVERSION ---")
        
        solicitud = {}
        self.contador_solicitudes += 1
        
        solicitud["id"] = self.contador_solicitudes
        
        print("Nombre de la empresa solicitante:")
        solicitud["empresa"] = input().strip()
        
        print("Monto solicitado:")
        try:
            solicitud["monto"] = float(input())
        except ValueError:
            print("Error: Monto inválido")
            return None
        
        print("Descripción del proyecto:")
        solicitud["descripcion"] = input().strip()
        
        solicitud["fecha"] = dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        solicitud["estado"] = "PENDIENTE"
        
        # Agregar a la cola
        self.cola_solicitudes_inversion.enqueQ(solicitud)
        
        print(f"✓ Solicitud #{solicitud['id']} agregada a la cola")
        print(f"Posición en cola: {self.cola_solicitudes_inversion.tam}")
        return solicitud
    
    def ProcesarSolicitudInversion(self, datos):
        print("\n--- PROCESAR SOLICITUD DE INVERSION ---")
        
        if self.cola_solicitudes_inversion.Ivacs():
            print("No hay solicitudes pendientes")
            return None
        
        # Obtener la primera solicitud (FIFO)
        solicitud = self.cola_solicitudes_inversion.frentENQ()
        
        if solicitud:
            print(f"\n--- SOLICITUD #{solicitud['id']} ---")
            print(f"Empresa: {solicitud['empresa']}")
            print(f"Monto: ${solicitud['monto']:,.2f}")
            print(f"Descripción: {solicitud['descripcion']}")
            print(f"Fecha: {solicitud['fecha']}")
            
            print("\n¿Aprobar solicitud? (S/N):")
            respuesta = input().strip().upper()
            
            if respuesta == 'S':
                solicitud['estado'] = "APROBADA"
                print("✓ Solicitud APROBADA")
            else:
                solicitud['estado'] = "RECHAZADA"
                print("✗ Solicitud RECHAZADA")
            
            # Remover de la cola
            self.cola_solicitudes_inversion.DeqQ(solicitud)
            
            return solicitud
        
        return None
    
    def AgregarQueja(self, datos):
        print("\n--- AGREGAR QUEJA O RECLAMO ---")
        
        queja = {}
        
        print("Nombre del reclamante:")
        queja["reclamante"] = input().strip()
        
        print("Empresa relacionada:")
        queja["empresa"] = input().strip()
        
        print("Tipo (QUEJA/RECLAMO):")
        queja["tipo"] = input().strip().upper()
        
        print("Descripción:")
        queja["descripcion"] = input().strip()
        
        queja["fecha"] = dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        queja["estado"] = "PENDIENTE"
        
        # Agregar a la cola de quejas
        self.cola_quejas.enqueQ(queja)
        
        print(f"✓ {queja['tipo']} agregada a la cola")
        print(f"Posición en cola: {self.cola_quejas.tam}")
        return queja
    
    def ProcesarQueja(self, datos):
        print("\n--- PROCESAR QUEJA O RECLAMO ---")
        
        if self.cola_quejas.Ivacs():
            print("No hay quejas o reclamos pendientes")
            return None
        
        # Obtener la primera queja (FIFO)
        queja = self.cola_quejas.frentENQ()
        
        if queja:
            print(f"\n--- {queja['tipo']} ---")
            print(f"Reclamante: {queja['reclamante']}")
            print(f"Empresa: {queja['empresa']}")
            print(f"Descripción: {queja['descripcion']}")
            print(f"Fecha: {queja['fecha']}")
            
            print("\n¿Marcar como resuelta? (S/N):")
            respuesta = input().strip().upper()
            
            if respuesta == 'S':
                queja['estado'] = "RESUELTA"
                print("✓ Queja/Reclamo RESUELTA")
            else:
                queja['estado'] = "EN PROCESO"
                print("→ Queja/Reclamo EN PROCESO")
            
            # Remover de la cola
            self.cola_quejas.DeqQ(queja)
            
            return queja
        
        return None
    
    def MirarCronologiaInversionEmpresa(self, datos):
        print("\n--- CRONOLOGIA DE INVERSIONES ---")
        print("Nombre de la empresa:")
        empresa = input().strip()
        
        print(f"\n=== INVERSIONES DE {empresa} ===")
        print("(Esta funcionalidad se integra con Op_inversion)")
        # Esta función se puede conectar con Op_inversion para mostrar las inversiones


class Op_sector:
    """
    Indexación y búsqueda de empresas: Usa un Árbol Binario de Búsqueda 
    para indexar y acceder rápidamente a la información de las empresas,
    como NIT, nombre o capital, mejorando la eficiencia en la recuperación de datos.
    """
    def __init__(self):
        # Árbol binario para indexar por capital
        self.arbol_por_capital = Pencil()
        # Diccionario para almacenar información completa de empresas
        self.empresas_info = {}
        # Listas para sectores
        self.sectores_economicos = []
        self.sectores_geograficos = []
    
    def AgregarSectorEconomico(self, datos):
        print("\n--- AGREGAR SECTOR ECONOMICO ---")
        
        sector = {}
        
        print("Nombre del sector económico:")
        sector["nombre"] = input().strip()
        
        print("Descripción:")
        sector["descripcion"] = input().strip()
        
        print("Código del sector:")
        sector["codigo"] = input().strip()
        
        self.sectores_economicos.append(sector)
        
        print(f"✓ Sector económico '{sector['nombre']}' agregado exitosamente")
        return sector
    
    def AgregarSectorBarrio(self, datos):
        print("\n--- AGREGAR SECTOR/BARRIO/LOCALIDAD ---")
        
        lugar = {}
        
        print("Nombre del Sector/Barrio/Localidad:")
        lugar["nombre"] = input().strip()
        
        print("Ciudad:")
        lugar["ciudad"] = input().strip()
        
        print("Código postal (opcional):")
        lugar["codigo_postal"] = input().strip()
        
        print("Características principales:")
        lugar["caracteristicas"] = input().strip()
        
        self.sectores_geograficos.append(lugar)
        
        print(f"✓ Sector geográfico '{lugar['nombre']}' agregado exitosamente")
        return lugar
    
    def IndexarEmpresaPorCapital(self, empresa_data):
        """
        Indexa una empresa en el árbol binario de búsqueda usando el capital como clave
        """
        try:
            capital = float(empresa_data.get("capital", 0))
            
            # Insertar en el árbol binario
            self.arbol_por_capital.InsertNod(capital)
            
            # Guardar información completa
            if capital not in self.empresas_info:
                self.empresas_info[capital] = []
            
            self.empresas_info[capital].append(empresa_data)
            
            print(f"✓ Empresa indexada con capital: ${capital:,.2f}")
            return True
            
        except Exception as e:
            print(f"Error al indexar empresa: {e}")
            return False
    
    def BuscarEmpresasPorRangoCapital(self, capital_min, capital_max):
        print(f"\n--- EMPRESAS CON CAPITAL ENTRE ${capital_min:,.2f} Y ${capital_max:,.2f} ---")
        
        # Usar la función LNE del árbol binario (Lista Nodos Entre)
        capitales_en_rango = self.arbol_por_capital.LNE(capital_min, capital_max)
        
        empresas_encontradas = []
        
        for capital in capitales_en_rango:
            if capital in self.empresas_info:
                for empresa in self.empresas_info[capital]:
                    empresas_encontradas.append(empresa)
                    print(f"\n• {empresa.get('nombre', 'N/A')}")
                    print(f"  NIT: {empresa.get('nit', 'N/A')}")
                    print(f"  Capital: ${capital:,.2f}")
                    print(f"  Tipo: {empresa.get('tipo', 'N/A')}")
        
        print(f"\n✓ Total de empresas encontradas: {len(empresas_encontradas)}")
        return empresas_encontradas
    
    def ObtenerEstadisticasCapital(self):
        print("\n--- ESTADISTICAS DE CAPITAL ---")
        
        if self.arbol_por_capital.rz is None:
            print("No hay empresas indexadas")
            return None
        
        promedio = self.arbol_por_capital.CalcularPromedio()
        
        print(f"Promedio de capital: ${promedio:,.2f}")
        
        # Obtener todos los capitales ordenados
        capitales = self.arbol_por_capital.Inord(self.arbol_por_capital.rz)
        
        if capitales:
            print(f"Capital mínimo: ${min(capitales):,.2f}")
            print(f"Capital máximo: ${max(capitales):,.2f}")
            print(f"Total de empresas: {len(capitales)}")
        
        return {
            "promedio": promedio,
            "minimo": min(capitales) if capitales else 0,
            "maximo": max(capitales) if capitales else 0,
            "total": len(capitales)
        }
    
    def VisualizarFactoresBalance(self):
        print("\n--- FACTORES DE BALANCE (Árbol de Capitales) ---")
        
        factores = self.arbol_por_capital.ListarTodosFB()
        
        if not factores:
            print("No hay datos en el árbol")
            return None
        
        print("\nCapital | Factor de Balance")
        print("-" * 40)
        for capital, fb in sorted(factores.items()):
            balance_str = "BALANCEADO" if fb in [-1, 0, 1] else "DESBALANCEADO"
            print(f"${capital:,.2f} | FB={fb:+d} ({balance_str})")
        
        return factores