class SaldoTidakMencukupiError(Exception):
    pass

class NominalTidakValidError(Exception):
    pass

saldo_tersedia = 500000

try:
    input_nominal = input("Masukkan nominal yang ingin ditarik: ")
    
    if not input_nominal.isdigit():
        raise ValueError("Nominal yang dimasukkan harus berupa angka.")
    
    nominal_tarik = int(input_nominal)
    
    if nominal_tarik <= 0:
        raise NominalTidakValidError("Nominal penarikan harus lebih dari 0.")
        
    if nominal_tarik > saldo_tersedia:
        raise SaldoTidakMencukupiError("Saldo Anda tidak mencukupi untuk penarikan ini.")
        
    saldo_tersedia -= nominal_tarik
    print(f"Penarikan berhasil. Sisa saldo Anda: Rp {saldo_tersedia}")

except ValueError as e:
    print("Error:", e)
except NominalTidakValidError as e:
    print("Error Input:", e)
except SaldoTidakMencukupiError as e:
    print("Error Transaksi:", e)
except Exception as e:
    print("Terjadi kesalahan sistem:", e)