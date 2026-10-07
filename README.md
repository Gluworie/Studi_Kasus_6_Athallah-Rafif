# Studi_Kasus_6_Athallah-Rafif<br>

Sistem Manajemen Inventaris Barang<br>
<img width="221" height="66" alt="image" src="https://github.com/user-attachments/assets/e24f92bf-9887-47da-aab4-28d5b9182d34" /><br>
Import Library<br>
<br>
Paling atas ada import json dan import os, ini wajib soalnya programnya main-main sama file. JSON buat baca-tulis data, OS buat ngecek apakah file udah ada atau belum.<br>
<img width="1028" height="35" alt="image" src="https://github.com/user-attachments/assets/2766b44c-2d74-40c5-8ba9-b504d6ca1aae" /><br>
NAMA_FILE<br>
<br>
NAMA_FILE itu cuma variabel nyimpen path ke file JSON-nya biar gampang diubah kalau mau. Di program ini path-nya:<br>
C:\Users\Rapip\Downloads\KULIAH\PRAKTIKUM\Praktikum DDP\STUDI KASUS 6\Studkas6.json<br>
<img width="553" height="176" alt="image" src="https://github.com/user-attachments/assets/8faa8a56-765b-4940-8b2f-ed15866c9dd0" /><br>
Fungsi baca_data()<br>
<br>
Tugasnya buka file JSON terus ubah isinya jadi list Python yang bisa dipakai. Kalau filenya belum pernah ada, dia bakal balikin list kosong aja biar gak error pas run pertama kali. cara kerjanya:<br>
<br>
1.Ngecek apakah file ada dengan os.path.exists()<br>
2.Kalau ada, buka file terus parse JSON pake json.load()<br>
3.Kalau gak ada, balikin list kosong []<br>
<img width="551" height="86" alt="image" src="https://github.com/user-attachments/assets/6bbef4dd-e279-408e-bc64-52ba451760f3" /><br>
Fungsi simpan_data()<br>
<br>
Kebalikannya dari baca_data(). Dia nulis ulang semua data ke file dalam format JSON. Nah ini bagian yang bikin data gak ilang walau programnya ditutup terus dibuka lagi. Prosesnya:<br>
<br>
1.Buka file dengan mode write (timpa yang lama)<br>
2.Pakai json.dump() buat ubah list Python jadi JSON terus simpan ke file<br>
3.indent=2 itu biar JSON-nya rapih dan mudah dibaca<br>
<img width="1287" height="272" alt="image" src="https://github.com/user-attachments/assets/663a379e-072f-4815-8579-9a524574b1a4" /><br>
Fungsi tampilkan_barang()<br>
<br>
Manggil baca_data() dulu buat ambil semua data barang dari file. Abis itu di-loop pake for biar tiap barang keprint satu-satu dengan nomor urut. Kalau belum ada barang (list kosong), dia akan bilang "belum ada barang di gudang".
<img width="768" height="362" alt="image" src="https://github.com/user-attachments/assets/d6568eb5-0778-4d6a-aa78-b2a6178b42a3" /><br>
Fungsi tambah_barang()<br>
<br>
Nanya input ke user: nama barang, jumlah stok, sama harga satuan. Terus semua input itu dibungkus jadi dictionary (objek) dengan key nama, stok, dan harga. Setelah itu dictionary baru itu ditempel ke data lama pake append(), baru deh semua data disimpen ulang ke file pake simpan_data() biar perubahan gak ilang.<br>
<img width="631" height="386" alt="image" src="https://github.com/user-attachments/assets/fc5c9309-41ae-4189-8912-e6d3aaa053eb" /><br>
Menu Utama (while True)<br>
<br>
Bagian paling bawah itu menunya, pake while True biar program terus looping dan nanya user mau pilih apa:<br>
<br>
Pilihan 1: Lihat data barang (manggil tampilkan_barang())<br>
Pilihan 2: Tambah barang baru (manggil tambah_barang())<br>
Pilihan 3: Keluar (pakai break buat keluar dari loop)<br>
Program bakal terus nanya sampe user ketik 3, baru deh break dan program ditutup.<br>
<img width="1176" height="938" alt="image" src="https://github.com/user-attachments/assets/cce7a733-d89f-4cc9-a2f0-f0eae03d4da9" /><br>
Dalam hasil output disini dicoba:<br>
1. Lihat data barang > belum ada barang di gudang > 2. Tambah barang baru > Menambahkan "Aqua" > Jumlah Stok "100" > Dan Harga Baranng "4000" > 1. Lihat data barang (lagi) > Melihat Data Barang Yang Di Tambahkan > 3. Keluar<br>
<br>
<img width="483" height="339" alt="image" src="https://github.com/user-attachments/assets/4570404b-6332-4e90-a9c8-77e1bda21dce" /><br>
Isi file JSON yang sudah ditambah data barang baru, barang punya tiga informasi: nama barang, jumlah stok, dan harga satuan.<br>
Terimakasih
