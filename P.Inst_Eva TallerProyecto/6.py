import json
import os

class InventoryManager:
    def __init__(self, filename="inventory.json"):
        self.filename = filename
        self.inventory = self.load_inventory()

    def load_inventory(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_inventory(self):
        with open(self.filename, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_product(self):
        nombre = input("Ingrese el nombre del producto: ")
        if nombre in self.inventory:
            print("Error: El producto ya existe.")
            return

        try:
            cantidad = int(input("Ingrese la cantidad disponible: "))
            precio = float(input("Ingrese el precio unitario: "))
            if cantidad < 0 or precio < 0:
                print("Error: Los valores no pueden ser negativos.")
                return
        except ValueError:
            print("Error: Por favor ingrese valores numéricos válidos.")
            return

        self.inventory[nombre] = {
            "cantidad": cantidad,
            "precio": precio
        }
        self.save_inventory()
        print("Producto añadido exitosamente.")

    def update_product(self):
        self.show_inventory()
        if not self.inventory:
            return

        nombre = input("Ingrese el nombre del producto a actualizar: ")
        if nombre not in self.inventory:
            print("Error: El producto no existe.")
            return

        try:
            cantidad = int(input("Ingrese la nueva cantidad (Enter para mantener): "))
            precio = float(input("Ingrese el nuevo precio (Enter para mantener): "))
            if cantidad < 0 or precio < 0:
                print("Error: Los valores no pueden ser negativos.")
                return
            self.inventory[nombre]["cantidad"] = cantidad
            self.inventory[nombre]["precio"] = precio
            self.save_inventory()
            print("Producto actualizado exitosamente.")
        except ValueError:
            print("Error: Por favor ingrese valores numéricos válidos.")

    def delete_product(self):
        self.show_inventory()
        if not self.inventory:
            return

        nombre = input("Ingrese el nombre del producto a eliminar: ")
        if nombre in self.inventory:
            del self.inventory[nombre]
            self.save_inventory()
            print("Producto eliminado exitosamente.")
        else:
            print("Error: El producto no existe.")

    def show_inventory(self):
        if not self.inventory:
            print("\nEl inventario está vacío.")
            return

        print("\nInventario actual:")
        print("-" * 50)
        print(f"{'Producto':<20} {'Cantidad':<10} {'Precio':<10}")
        print("-" * 50)
        for producto, datos in self.inventory.items():
            print(f"{producto:<20} {datos['cantidad']:<10} ${datos['precio']:.2f}")
        print("-" * 50)


def main():
    manager = InventoryManager()

    while True:
        print("\nMenú de opciones:")
        print("1. Añadir producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("\nSeleccione una opción de 1 a 5: ")

        if opcion == "1":
            manager.add_product()
        elif opcion == "2":
            manager.update_product()
        elif opcion == "3":
            manager.delete_product()
        elif opcion == "4":
            manager.show_inventory()
        elif opcion == "5":
            print("¡Gracias por usar el sistema de inventario!")
            break
        else:
            print("Opción no válida. Por favor intente de nuevo.")


if __name__ == "__main__":
    main()