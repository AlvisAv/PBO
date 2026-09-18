# Jawaban Latihan Bab 3: Eksepsi (Nomor 1-3)

## 1. Mengapa Program Perlu Mekanisme Penanganan Error dan Dampaknya
**Pertanyaan:** Mengapa sebuah program perlu memiliki mekanisme penanganan error? Jelaskan dampaknya jika error tidak ditangani dengan baik!

**Jawaban:**
Program butuh mekanisme penanganan error (exception handling) supaya kalau ada masalah yang tidak terduga saat dijalankan—seperti salah input dari user, file hilang, atau koneksi terputus—program tidak langsung berhenti mendadak (crash). Dengan penanganan error, program bisa menangkap masalah tersebut dan memberikan respon yang sesuai.

Jika error tidak ditangani dengan baik:
* Program bakal langsung crash dan terhenti di tengah jalan.
* User akan melihat pesan error teknis dari interpreter yang membingungkan dan tidak ramah pengguna.
* Berisiko kehilangan data, misalnya data tidak tersimpan ke database karena prosesnya terputus secara mendadak.

---

## 2. Keuntungan Penggunaan Custom Exception
**Pertanyaan:** Jelaskan keuntungan penggunaan custom exception dibandingkan hanya menggunakan exception bawaan Python!

**Jawaban:**
Menggunakan *custom exception* (exception buatan sendiri) punya beberapa keuntungan:
* **Lebih spesifik dan relevan:** Nama error bisa disesuaikan dengan logika aplikasi kita. Misalnya membuat `SaldoTidakMencukupiError`, yang jauh lebih jelas konteksnya dibanding hanya pakai `ValueError` bawaan Python.
* **Mempermudah debugging:** Saat terjadi error, developer lain yang membaca kode atau log error bisa lebih cepat paham letak masalahnya.
* **Penanganan error lebih rapi:** Kita bisa menangkap dan menangani jenis error tertentu secara khusus pada blok `try-except`.

---

## 3. Cara Kerja Blok Try, Except, dan Finally
**Pertanyaan:** Jelaskan cara kerja blok try, except, dan finally dalam penanganan error pada Python!

**Jawaban:**
* **`try`**: Blok berisi kode program yang ingin diuji atau diperkirakan berpotensi menghasilkan error. Jika terjadi error di dalam blok ini, eksekusinya langsung dihentikan lalu dialihkan ke blok `except`.
* **`except`**: Blok yang bertugas menangkap dan menangani error yang muncul dari blok `try`. Di dalamnya berisi perintah yang harus dilakukan saat error terjadi agar program tidak crash.
* **`finally`**: Blok kode yang akan **selalu dieksekusi** paling akhir, tidak peduli apakah terjadi error atau tidak. Biasanya dipakai untuk penutupan atau pembersihan resource, seperti menutup file atau koneksi database.