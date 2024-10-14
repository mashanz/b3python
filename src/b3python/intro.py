# # # parameter dalam python

x = 2

print(f"nilai x = {x} dan tipe datanya adalah {type(x)}")

# # # operasi aritmatika
# # x =  1 + 1 / 2 * 5

# # operasi logika (if/else)
# y = 10
# if y < 1:
#     print("kurang dari 1")
# elif y == 1:
#     print(" ye adalah satu")
# else:
#     print("Ye suka suka, ga kurang dan ga sama")


def luas_persegi(panjang: int, lebar: int) -> int:
    """Fungsi menghitung luas Persegi

    input
    ======
    p -> panjang
    l -> luas

    return
    ======
    hasil dari panjang kali lebar
    ```py
        print(p * l)
    ```
    """
    return panjang * lebar


if __name__ == "__main__":
    print(luas_persegi(2, 3))
