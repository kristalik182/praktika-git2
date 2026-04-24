def show_menu():
    print("   ТРЕКЕР ПРИВЫЧЕК")
    print("1. Добавить привычку")
    print("2. Список привычек")
    print("3. Отметить выполнение")
    print("4. Статистика")
    print("5. Выход")
def main():
    while True:
        show_menu()
        choice = input("Выберите пункт (1-5): ")
        if choice == "5":
            print("До свидания!")
            break
        else:
            print(f"\n[Функция {choice} - будет добавлена позже]")
if __name__ == "__main__":
    main()