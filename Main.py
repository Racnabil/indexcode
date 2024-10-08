from controller import FoodController
from View import run_app

def main():
    # Inisialisasi controller
    controller = FoodController()

    # Fetch data dari tabel food
    food_items = controller.get_food_items()

    # Fetch data dari tabel stationery
    stationery_items = controller.get_stationery_items()

    # Menjalankan GUI dengan data
    run_app(food_items, stationery_items)

    # Menutup koneksi database
    controller.close()

if __name__ == "__main__":
    main()