import logic
import file

def main():
    file.clear_output_folder()

    print("Memulai...\n")
    file.loader(logic.proses)
    print("\nSelesai!")

if __name__=="__main__":
    main()