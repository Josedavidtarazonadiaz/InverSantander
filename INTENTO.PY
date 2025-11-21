from OPTIONS import *
import os
import json

class SistemaGestion:
    def __init__(self):
        # Inicializar módulos del sistema
        self.opciones = Options()
        self.seguridad = Security()
        self.op_inversion = Op_inversion()
        self.op_empresa = Op_empresa(capacidad=100)
        self.op_sector = Op_sector()
        
        # Datos del sistema
        self.datos = {
            "d_Admin": [],
            "empresas": [],
            "inversionistas": [],
            "sectores_economicos": [],
            "sectores_geograficos": []
        }
        
        # Usuario actual
        self.usuario_actual = None
        self.tipo_usuario = None  # 'ADMIN', 'EMPRESA', 'INVERSIONISTA'
        
        # Cargar datos si existen
        self.cargar_datos()
    
    def limpiar_pantalla(self):
        """Limpia la consola"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def cargar_datos(self):
        """Carga los datos del sistema desde archivos JSON"""
        try:
            if os.path.exists("admins.json"):
                with open("admins.json", "r") as f:
                    datos_cargados = json.load(f)
                    self.datos.update(datos_cargados)
                print("✓ Datos cargados exitosamente")
        except Exception as e:
            print(f"⚠ No se pudieron cargar datos previos: {e}")
            self.opciones.AddError(e)
    
    def guardar_datos(self):
        """Guarda los datos del sistema en archivos JSON"""
        try:
            with open("admins.json", "w") as f:
                json.dump(self.datos, f, indent=4)
            print("✓ Datos guardados exitosamente")
        except Exception as e:
            print(f"✗ Error al guardar datos: {e}")
            self.opciones.AddError(e)
    
    def mostrar_banner(self):
        """Muestra el banner del sistema"""
        self.limpiar_pantalla()
        print("=" * 60)
        print(" " * 10 + "SISTEMA DE GESTION DE INVERSIONES")
        print(" " * 15 + "Y EMPRESAS EMERGENTES")
        print("=" * 60)
        print()
    
    def menu_inicio(self):
        """Menú principal de inicio del sistema"""
        while True:
            self.mostrar_banner()
            print("--- MENU DE INICIO ---")
            print("1. Iniciar Sesión como Administrador")
            print("2. Registrarse como Administrador")
            print("3. Acceso como Empresa")
            print("4. Acceso como Inversionista")
            print("5. Salir del Sistema")
            print("\nSeleccione una opción: ", end="")
            
            opcion = self.opciones.Choice()
            
            if opcion == 1:
                self.login_administrador()
            elif opcion == 2:
                self.registro_administrador()
            elif opcion == 3:
                self.acceso_empresa()
            elif opcion == 4:
                self.acceso_inversionista()
            elif opcion == 5:
                print("\n¡Gracias por usar el sistema!")
                self.guardar_datos()
                break
            else:
                print("\n✗ Opción inválida")
                input("Presione ENTER para continuar...")
    
    def login_administrador(self):
        """Login para administradores"""
        self.mostrar_banner()
        print("--- LOGIN ADMINISTRADOR ---\n")
        
        if not self.datos["d_Admin"]:
            print("⚠ No hay administradores registrados.")
            print("Por favor, regístrese primero.")
            input("\nPresione ENTER para continuar...")
            return
        
        admin = self.seguridad.Log_in_Admin(self.datos)
        
        if admin:
            self.usuario_actual = admin
            self.tipo_usuario = 'ADMIN'
            self.menu_administrador()
        else:
            input("\nPresione ENTER para continuar...")
    
    def registro_administrador(self):
        """Registro de nuevos administradores"""
        self.mostrar_banner()
        print("--- REGISTRO ADMINISTRADOR ---\n")
        
        admin = self.seguridad.Log_Up_Admin(self.datos)
        
        if admin:
            print("\n✓ ¡Registro exitoso!")
            print("Ya puede iniciar sesión")
        
        input("\nPresione ENTER para continuar...")
    
    def acceso_empresa(self):
        """Acceso para empresas"""
        self.mostrar_banner()
        print("--- ACCESO EMPRESA ---\n")
        print("Ingrese el nombre de su empresa:")
        nombre_empresa = input().strip()
        
        # Verificar si la empresa existe
        empresa_encontrada = None
        for empresa in self.datos["empresas"]:
            if empresa["nombre"].lower() == nombre_empresa.lower():
                empresa_encontrada = empresa
                break
        
        if empresa_encontrada:
            self.usuario_actual = empresa_encontrada
            self.tipo_usuario = 'EMPRESA'
            print(f"\n✓ Bienvenido {empresa_encontrada['nombre']}")
            input("Presione ENTER para continuar...")
            self.menu_empresa()
        else:
            print("\n⚠ Empresa no encontrada en el sistema")
            print("Contacte a un administrador para registrarse")
            input("\nPresione ENTER para continuar...")
    
    def acceso_inversionista(self):
        """Acceso para inversionistas"""
        self.mostrar_banner()
        print("--- ACCESO INVERSIONISTA ---\n")
        print("Ingrese su nombre:")
        nombre_inversionista = input().strip()
        
        # Verificar si el inversionista existe
        inversionista_encontrado = None
        for inv in self.datos["inversionistas"]:
            if inv["nombre"].lower() == nombre_inversionista.lower():
                inversionista_encontrado = inv
                break
        
        if inversionista_encontrado:
            self.usuario_actual = inversionista_encontrado
            self.tipo_usuario = 'INVERSIONISTA'
            print(f"\n✓ Bienvenido {inversionista_encontrado['nombre']}")
            input("Presione ENTER para continuar...")
            self.menu_inversionista()
        else:
            print("\n⚠ Inversionista no encontrado")
            print("¿Desea registrarse? (S/N): ", end="")
            respuesta = input().strip().upper()
            if respuesta == 'S':
                self.registro_inversionista()
            else:
                input("\nPresione ENTER para continuar...")
    
    def registro_inversionista(self):
        """Registro de nuevo inversionista"""
        print("\n--- REGISTRO INVERSIONISTA ---")
        inversionista = {}
        
        print("Nombre completo:")
        inversionista["nombre"] = input().strip()
        
        print("Email:")
        inversionista["email"] = input().strip()
        
        print("Teléfono:")
        inversionista["telefono"] = input().strip()
        
        print("Capital disponible para inversión:")
        try:
            inversionista["capital"] = float(input())
        except ValueError:
            inversionista["capital"] = 0
        
        inversionista["fecha_registro"] = dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        
        self.datos["inversionistas"].append(inversionista)
        
        print(f"\n✓ Inversionista {inversionista['nombre']} registrado exitosamente")
        
        self.usuario_actual = inversionista
        self.tipo_usuario = 'INVERSIONISTA'
        
        input("\nPresione ENTER para continuar...")
        self.menu_inversionista()
    
    def menu_administrador(self):
        """Menú principal para administradores"""
        while True:
            self.mostrar_banner()
            print(f"Usuario: {self.usuario_actual['Usuario']} (ADMINISTRADOR)\n")
            self.opciones.MenuPrincipal()
            
            opcion = self.opciones.Choice()
            
            if opcion == 1:
                self.submenu_empresa_admin()
            elif opcion == 2:
                self.submenu_inversionista_admin()
            elif opcion == 3:
                self.submenu_sector_admin()
            elif opcion == 4:
                print("\n✓ Cerrando sesión...")
                self.usuario_actual = None
                self.tipo_usuario = None
                input("Presione ENTER para continuar...")
                break
            else:
                print("\n✗ Opción inválida")
                input("Presione ENTER para continuar...")
    
    def submenu_empresa_admin(self):
        """Submenú de empresa para administradores"""
        while True:
            self.mostrar_banner()
            print(f"Usuario: {self.usuario_actual['Usuario']} (ADMINISTRADOR)\n")
            self.opciones.MenuEmpresa()
            
            opcion = self.opciones.Choice()
            
            if opcion == 1:
                empresa = self.op_empresa.AgregarEmpresa(self.datos)
                if empresa:
                    # Indexar en el árbol binario
                    self.op_sector.IndexarEmpresaPorCapital(empresa)
                input("\nPresione ENTER para continuar...")
            elif opcion == 2:
                # Agregar solicitud de inversión
                self.op_empresa.AgregarSolicitudInversion(self.datos)
                input("\nPresione ENTER para continuar...")
            elif opcion == 3:
                # Procesar solicitudes de inversión
                self.op_empresa.ProcesarSolicitudInversion(self.datos)
                input("\nPresione ENTER para continuar...")
            elif opcion == 4:
                break
            else:
                print("\n✗ Opción inválida")
                input("Presione ENTER para continuar...")
    
    def submenu_inversionista_admin(self):
        """Submenú de inversionista para administradores"""
        while True:
            self.mostrar_banner()
            print(f"Usuario: {self.usuario_actual['Usuario']} (ADMINISTRADOR)\n")
            self.opciones.MenuInversionista()
            
            opcion = self.opciones.Choice()
            
            if opcion == 1:
                self.registro_inversionista()
            elif opcion == 2:
                # Ver cronología de inversiones
                self.op_inversion.MirarCronologiaEmpresa(self.datos)
                input("\nPresione ENTER para continuar...")
            elif opcion == 3:
                # Agregar inversión
                self.op_inversion.AgregarInversion(self.datos)
                input("\nPresione ENTER para continuar...")
            elif opcion == 4:
                break
            else:
                print("\n✗ Opción inválida")
                input("Presione ENTER para continuar...")
    
    def submenu_sector_admin(self):
        """Submenú de sector para administradores"""
        while True:
            self.mostrar_banner()
            print(f"Usuario: {self.usuario_actual['Usuario']} (ADMINISTRADOR)\n")
            self.opciones.MenuSector()
            
            opcion = self.opciones.Choice()
            
            if opcion == 1:
                self.op_sector.AgregarSectorEconomico(self.datos)
                input("\nPresione ENTER para continuar...")
            elif opcion == 2:
                self.op_sector.AgregarSectorBarrio(self.datos)
                input("\nPresione ENTER para continuar...")
            elif opcion == 3:
                break
            else:
                print("\n✗ Opción inválida")
                input("Presione ENTER para continuar...")
    
    def menu_empresa(self):
        """Menú para empresas"""
        while True:
            self.mostrar_banner()
            print(f"Empresa: {self.usuario_actual['nombre']}\n")
            print("--- MENU EMPRESA ---")
            print("1. Ver información de la empresa")
            print("2. Crear solicitud de inversión")
            print("3. Ver mis solicitudes pendientes")
            print("4. Ver cronología de inversiones recibidas")
            print("5. Agregar logro empresarial")
            print("6. Presentar queja o reclamo")
            print("7. Cerrar sesión")
            print("\nSeleccione una opción: ", end="")
            
            opcion = self.opciones.Choice()
            
            if opcion == 1:
                self.ver_info_empresa()
            elif opcion == 2:
                # Prellenar datos de la empresa actual
                print("\n--- CREAR SOLICITUD DE INVERSION ---")
                print(f"Empresa: {self.usuario_actual['nombre']}")
                print("Monto solicitado:")
                try:
                    monto = float(input())
                    print("Descripción del proyecto:")
                    descripcion = input().strip()
                    
                    solicitud = {
                        "empresa": self.usuario_actual['nombre'],
                        "monto": monto,
                        "descripcion": descripcion,
                        "fecha": dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                        "estado": "PENDIENTE"
                    }
                    
                    self.op_empresa.cola_solicitudes_inversion.enqueQ(solicitud)
                    print(f"\n✓ Solicitud creada exitosamente")
                except ValueError:
                    print("\n✗ Error en el monto")
                
                input("\nPresione ENTER para continuar...")
            elif opcion == 3:
                self.ver_solicitudes_empresa()
                input("\nPresione ENTER para continuar...")
            elif opcion == 4:
                # Ver cronología de inversiones
                print(f"\nEmpresa: {self.usuario_actual['nombre']}")
                self.op_inversion.MirarCronologiaEmpresa(self.datos)
                input("\nPresione ENTER para continuar...")
            elif opcion == 5:
                # Agregar logro
                print("\n--- AGREGAR LOGRO ---")
                print(f"Empresa: {self.usuario_actual['nombre']}")
                print("Descripción del logro:")
                descripcion = input().strip()
                print("Fecha del logro (DD/MM/AAAA):")
                fecha = input().strip()
                
                registro = {
                    "tipo": "LOGRO",
                    "descripcion": descripcion,
                    "fecha": fecha,
                    "timestamp": dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                }
                
                # Agregar a la cronología
                self.op_inversion._CrearListaEmpresa(self.usuario_actual['nombre'])
                nuevo_nodo = NoQ(registro)
                ultimo_nodo = self.op_inversion.cronologias_empresas[self.usuario_actual['nombre']]["ultimo"]
                ultimo_nodo.csig = nuevo_nodo
                nuevo_nodo.Prant = ultimo_nodo
                self.op_inversion.cronologias_empresas[self.usuario_actual['nombre']]["ultimo"] = nuevo_nodo
                self.op_inversion.cronologias_empresas[self.usuario_actual['nombre']]["cantidad"] += 1
                
                print("\n✓ Logro registrado exitosamente")
                input("\nPresione ENTER para continuar...")
            elif opcion == 6:
                self.op_empresa.AgregarQueja(self.datos)
                input("\nPresione ENTER para continuar...")
            elif opcion == 7:
                print("\n✓ Cerrando sesión...")
                self.usuario_actual = None
                self.tipo_usuario = None
                input("Presione ENTER para continuar...")
                break
            else:
                print("\n✗ Opción inválida")
                input("Presione ENTER para continuar...")
    
    def menu_inversionista(self):
        """Menú para inversionistas"""
        while True:
            self.mostrar_banner()
            print(f"Inversionista: {self.usuario_actual['nombre']}\n")
            print("--- MENU INVERSIONISTA ---")
            print("1. Ver mi información")
            print("2. Realizar inversión en una empresa")
            print("3. Ver cronología de una empresa")
            print("4. Buscar empresas por capital")
            print("5. Ver estadísticas del mercado")
            print("6. Ver mis inversiones realizadas")
            print("7. Cerrar sesión")
            print("\nSeleccione una opción: ", end="")
            
            opcion = self.opciones.Choice()
            
            if opcion == 1:
                self.ver_info_inversionista()
            elif opcion == 2:
                self.realizar_inversion()
            elif opcion == 3:
                self.op_inversion.MirarCronologiaEmpresa(self.datos)
                input("\nPresione ENTER para continuar...")
            elif opcion == 4:
                self.buscar_empresas_capital()
            elif opcion == 5:
                self.op_sector.ObtenerEstadisticasCapital()
                input("\nPresione ENTER para continuar...")
            elif opcion == 6:
                self.ver_inversiones_realizadas()
            elif opcion == 7:
                print("\n✓ Cerrando sesión...")
                self.usuario_actual = None
                self.tipo_usuario = None
                input("Presione ENTER para continuar...")
                break
            else:
                print("\n✗ Opción inválida")
                input("Presione ENTER para continuar...")
    
    def ver_info_empresa(self):
        """Muestra información de la empresa actual"""
        print("\n--- INFORMACION DE LA EMPRESA ---")
        print(f"Nombre: {self.usuario_actual.get('nombre', 'N/A')}")
        print(f"NIT: {self.usuario_actual.get('nit', 'N/A')}")
        print(f"Tipo: {self.usuario_actual.get('tipo', 'N/A')}")
        print(f"Fecha de creación: {self.usuario_actual.get('fecha_creacion', 'N/A')}")
        print(f"Dirección: {self.usuario_actual.get('direccion', 'N/A')}")
        print(f"Capital: ${self.usuario_actual.get('capital', 0):,.2f}")
        input("\nPresione ENTER para continuar...")
    
    def ver_info_inversionista(self):
        """Muestra información del inversionista actual"""
        print("\n--- INFORMACION DEL INVERSIONISTA ---")
        print(f"Nombre: {self.usuario_actual.get('nombre', 'N/A')}")
        print(f"Email: {self.usuario_actual.get('email', 'N/A')}")
        print(f"Teléfono: {self.usuario_actual.get('telefono', 'N/A')}")
        print(f"Capital disponible: ${self.usuario_actual.get('capital', 0):,.2f}")
        print(f"Fecha de registro: {self.usuario_actual.get('fecha_registro', 'N/A')}")
        input("\nPresione ENTER para continuar...")
    
    def ver_solicitudes_empresa(self):
        """Muestra las solicitudes de la empresa actual"""
        print("\n--- MIS SOLICITUDES ---")
        
        # Recorrer la cola y buscar solicitudes de esta empresa
        nodo_actual = self.op_empresa.cola_solicitudes_inversion.top
        contador = 0
        
        while nodo_actual is not None:
            solicitud = nodo_actual.Idat
            if solicitud.get("empresa") == self.usuario_actual['nombre']:
                contador += 1
                print(f"\n{contador}. Solicitud #{solicitud.get('id', 'N/A')}")
                print(f"   Monto: ${solicitud.get('monto', 0):,.2f}")
                print(f"   Descripción: {solicitud.get('descripcion', 'N/A')}")
                print(f"   Estado: {solicitud.get('estado', 'N/A')}")
                print(f"   Fecha: {solicitud.get('fecha', 'N/A')}")
            
            nodo_actual = nodo_actual.csig
        
        if contador == 0:
            print("No tiene solicitudes registradas")
    
    def realizar_inversion(self):
        """Permite al inversionista realizar una inversión"""
        print("\n--- REALIZAR INVERSION ---")
        print(f"Inversionista: {self.usuario_actual['nombre']}")
        print(f"Capital disponible: ${self.usuario_actual.get('capital', 0):,.2f}\n")
        
        print("Empresa a invertir:")
        empresa = input().strip()
        
        print("Monto a invertir:")
        try:
            monto = float(input())
            
            if monto > self.usuario_actual.get('capital', 0):
                print("\n✗ Capital insuficiente")
                input("\nPresione ENTER para continuar...")
                return
            
            print("Fecha de inversión (DD/MM/AAAA):")
            fecha = input().strip()
            
            # Crear registro de inversión
            registro = {
                "tipo": "INVERSION",
                "inversionista": self.usuario_actual['nombre'],
                "monto": monto,
                "fecha": fecha,
                "timestamp": dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            }
            
            # Agregar a la cronología de la empresa
            self.op_inversion._CrearListaEmpresa(empresa)
            nuevo_nodo = NoQ(registro)
            ultimo_nodo = self.op_inversion.cronologias_empresas[empresa]["ultimo"]
            ultimo_nodo.csig = nuevo_nodo
            nuevo_nodo.Prant = ultimo_nodo
            self.op_inversion.cronologias_empresas[empresa]["ultimo"] = nuevo_nodo
            self.op_inversion.cronologias_empresas[empresa]["cantidad"] += 1
            
            # Actualizar capital del inversionista
            self.usuario_actual['capital'] -= monto
            
            print(f"\n✓ Inversión realizada exitosamente")
            print(f"Capital restante: ${self.usuario_actual['capital']:,.2f}")
            
        except ValueError:
            print("\n✗ Monto inválido")
        
        input("\nPresione ENTER para continuar...")
    
    def buscar_empresas_capital(self):
        """Busca empresas por rango de capital"""
        print("\n--- BUSCAR EMPRESAS POR CAPITAL ---")
        print("Capital mínimo:")
        try:
            cap_min = float(input())
            print("Capital máximo:")
            cap_max = float(input())
            
            self.op_sector.BuscarEmpresasPorRangoCapital(cap_min, cap_max)
        except ValueError:
            print("\n✗ Valores inválidos")
        
        input("\nPresione ENTER para continuar...")
    
    def ver_inversiones_realizadas(self):
        """Muestra todas las inversiones realizadas por el inversionista"""
        print("\n--- MIS INVERSIONES REALIZADAS ---")
        print(f"Inversionista: {self.usuario_actual['nombre']}\n")
        
        contador = 0
        total_invertido = 0
        
        # Recorrer todas las cronologías de empresas
        for empresa, lista_empresa in self.op_inversion.cronologias_empresas.items():
            nodo_actual = lista_empresa["cabecera"].csig
            
            while nodo_actual is not None:
                reg = nodo_actual.Idat
                
                if isinstance(reg, dict) and reg.get('tipo') == 'INVERSION':
                    if reg.get('inversionista') == self.usuario_actual['nombre']:
                        contador += 1
                        total_invertido += reg.get('monto', 0)
                        
                        print(f"{contador}. Inversión en: {empresa}")
                        print(f"   Monto: ${reg.get('monto', 0):,.2f}")
                        print(f"   Fecha: {reg.get('fecha', 'N/A')}")
                        print()
                
                nodo_actual = nodo_actual.csig
        
        if contador == 0:
            print("No ha realizado inversiones aún")
        else:
            print(f"Total de inversiones: {contador}")
            print(f"Monto total invertido: ${total_invertido:,.2f}")
        
        input("\nPresione ENTER para continuar...")


def main():
    """Función principal del sistema"""
    sistema = SistemaGestion()
    sistema.menu_inicio()


if __name__ == "__main__":
    main()