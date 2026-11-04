from student_functions import (
    read_csv,
    display_total_records,
    display_headings,
    display_all_records,
    display_first_rows,
    display_summary,
    display_average,
    display_counts,
)

FILENAME = "/Users/patryklickowski/Documents/GitHub/procedural_programming/lab_work/week5/part_c/students.csv"


def show_menu():
    print("\n=== Student Data Menu ===")
    print("1. Show total number of records")
    print("2. Show column headings")
    print("3. Show all records")
    print("4. Show first 5 records")
    print("5. Show summary statistics")
    print("6. Show average age")
    print("7. Show students per gender")
    print("8. Quit")


def main():
    df = read_csv(FILENAME)
    if df is None:
        return

    while True:
        show_menu()
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            display_total_records(df)
        elif choice == "2":
            display_headings(df)
        elif choice == "3":
            display_all_records(df)
        elif choice == "4":
            display_first_rows(df)
        elif choice == "5":
            display_summary(df)
        elif choice == "6":
            display_average(df, "age")
        elif choice == "7":
            display_counts(df, "gender")
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
