import telebot
from datetime import datetime
from telebot import types

bot = telebot.TeleBot('7472721745:AAFhZYYesr88ykIcaG0AdHLVKb904np4xE8')

questions_and_answers = {
    1: "Apa manfaat utama dari ubi cilembu?",
    2: "Bagaimana cara terbaik memasak ubi cilembu?",
    3: "Berapa porsi ubi cilembu yang pas sebagai pengganti nasi?",
    4: "Bisakah ubi cilembu dijadikan makanan untuk diet?",
    5: "Apa saja kandungan gizi dalam ubi cilembu?",
    6: "Olahan ubi cilembu apa yang simpel dan enak?",
    7: "Apa tips untuk menjual ubi cilembu dan produknya?",
    8: "Bagaimana cara menanam ubi cilembu agar rasanya manis?",
    9: "Apa yang harus dilakukan jika tanaman ubi terserang hama?",
    10: "Bagaimana cara membuat akun e-commerce?"
}

answers = {
    1: """
    <b>Manfaat Ubi Cilembu untuk Kesehatan:</b>
    • Mencegah kekurangan vitamin A.
    • Mengurangi risiko diabetes.
    • Mengandung anti-inflamasi untuk mencegah peradangan usus.
    • Membantu mengelola stres.
    • Meningkatkan kesehatan rambut dan kulit.
    • Baik untuk sistem pencernaan.
    """,
    2: """
    <b>Cara Memasak Ubi Cilembu:</b>
    <b>a. Panggang di Oven:</b>
    • Panaskan oven pada suhu 200°C.
    • Cuci ubi hingga bersih dan letakkan di loyang.
    • Panggang selama 45-60 menit hingga kulitnya mengeriput dan bagian dalam lembut.
    
    <b>b. Kukus:</b>
    • Cuci ubi, potong sesuai selera, dan kukus selama 30-45 menit hingga lembut.
    
    <b>c. Bakar:</b>
    • Cuci ubi dan tusuk dengan garpu, bakar di atas bara api selama 30-45 menit hingga matang.
    
    <b>Tips:</b>
    • Tambahkan garam atau mentega setelah matang.
    • Ubi panggang atau bakar sering kali mengeluarkan cairan manis.
    """,
    3: """
    <b>Apakah Ubi Cilembu Bisa Digunakan Sebagai Pengganti Diet?</b>
    • Ubi Cilembu rendah kalori dan tinggi serat, cocok untuk diet penurunan berat badan.
    • Kaya vitamin dan mineral, serta memiliki indeks glikemik rendah.
    • Konsumsi sebagai bagian dari diet beragam dan seimbang, dengan porsi yang diperhatikan.
    • Gunakan sebagai pengganti karbohidrat, dikombinasikan dengan protein, dan olah dengan cara sehat.
    """,
    4: """
    <b>Manfaat Ubi Cilembu untuk Diet:</b>
    • Rendah Kalori dan tinggi serat.
    • Kaya vitamin A, C, dan mineral.
    • Indeks glikemik rendah untuk kestabilan gula darah.
    
    <b>Pertimbangan:</b>
    • Variasi dan keseimbangan dalam diet penting.
    • Perhatikan porsi konsumsi.
    
    <b>Saran Penggunaan:</b>
    • Sebagai pengganti nasi atau roti.
    • Kombinasikan dengan protein.
    • Olah dengan cara sehat seperti memanggang atau mengukus.
    """,
    5: """
    <b>Kandungan Nutrisi Ubi Cilembu:</b>
    • Karbohidrat: Sumber energi.
    • Serat: Menjaga kesehatan pencernaan.
    • Vitamin A: Untuk kesehatan mata.
    • Vitamin C: Meningkatkan sistem kekebalan tubuh.
    • Vitamin B Kompleks: Untuk metabolisme energi.
    • Mineral: Kalium, mangan, dan magnesium.
    • Antioksidan dan gula alami.
    
    <b>Manfaat Kesehatan:</b>
    • Mengatur gula darah.
    • Mendukung kesehatan mata.
    • Memperkuat sistem kekebalan tubuh.
    """,
    6: """
    <b>Olahan Ubi Cilembu:</b>
    1. <b>Ubi Cilembu Panggang Madu:</b> Panggang irisan ubi dengan madu dan garam.
    2. <b>Ubi Cilembu Goreng:</b> Goreng potongan ubi hingga kuning keemasan.
    3. <b>Puding Ubi Cilembu:</b> Campur ubi halus dengan santan dan agar-agar, lalu dinginkan.
    4. <b>Ubi Cilembu Rebus:</b> Rebus ubi hingga empuk.
    5. <b>Sup Krim Ubi Cilembu:</b> Tumis bawang, masukkan ubi dan kaldu, lalu blender halus.
    6. <b>Salad Ubi Cilembu:</b> Campur ubi panggang dengan sayuran hijau dan kacang, siram dressing balsamic.
    """,
    7: """
    <b>Tips Menjual Ubi Cilembu:</b>
    1. <b>Kenali Produk:</b> Pastikan kualitas dan beragam olahan.
    2. <b>Penetapan Harga:</b> Tentukan harga kompetitif dan tawarkan promosi.
    3. <b>Branding dan Kemasan:</b> Desain kemasan menarik dan informatif.
    4. <b>Pemasaran dan Promosi:</b> Gunakan media sosial dan kolaborasi.
    5. <b>Tempat Penjualan:</b> Jual offline di pasar atau online melalui platform e-commerce.
    6. <b>Pelayanan Pelanggan:</b> Responsif dan terima feedback.
    7. <b>Inovasi Produk:</b> Kembangkan varian baru dan produk musiman.
    """,
    8: """
    <b>Cara Menanam Ubi Cilembu:</b>
    1. <b>Pemilihan Bibit:</b> Pilih bibit atau stek sehat dengan mata tunas.
    2. <b>Persiapan Lahan:</b> Tanam di tanah gembur dengan pH 5,5-6,5.
    3. <b>Penanaman:</b> Tanam stek pada jarak 30-40 cm dan kedalaman 10-15 cm.
    4. <b>Perawatan:</b> Siram teratur, beri pupuk organik, dan siangi gulma.
    5. <b>Pengendalian Hama dan Penyakit:</b> Gunakan pestisida organik dan observasi rutin.
    6. <b>Pemanenan:</b> Panen setelah 3-4 bulan saat daun menguning.
    7. <b>Tips Tambahan:</b> Pilih lokasi dengan sinar matahari penuh dan rotasi tanaman.
    """,
    9: """
    <b>Pengendalian Hama pada Ubi Cilembu:</b>
    1. <b>Identifikasi Hama:</b> Kenali jenis hama dan gejala serangan.
    2. <b>Pengendalian Mekanis:</b> Pemeriksaan rutin, pemangkasan, dan pengumpulan manual.
    3. <b>Penggunaan Pestisida Organik:</b> Gunakan neem oil, sabun insektisida, atau minyak atsiri.
    4. <b>Penggunaan Pestisida Kimia (Jika Diperlukan):</b> Pilih dengan hati-hati dan ikuti instruksi.
    5. <b>Pengendalian Hayati:</b> Manfaatkan musuh alami dan jamur entomopatogenik.
    6. <b>Pengelolaan Lingkungan:</b> Terapkan rotasi tanaman, pengaturan jarak tanam, dan sanitasi.
    7. <b>Pencegahan:</b> Tanam tanaman pendamping dan gunakan mulsa.
    8. <b>Pemantauan Lanjutan:</b> Monitoring rutin dan catat hasil.
    """,
    10: """
    <b>Cara Membuat Akun E-Commerce:</b>
    1. Daftar akun seller melalui “Buka Toko” di aplikasi atau “Mulai Berjualan” di situs.
    2. Tambahkan informasi toko.
    3. Pilih jasa kirim yang ingin Anda sediakan.
    4. Unggah foto dan daftar produk.
    5. Tambahkan detail rekening bank untuk penarikan penghasilan.
    """
}

# Start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    gif = open(r'C:\Users\riant\Documents\ITEBOT\Welcome.gif', 'rb')
    bot.send_animation(message.chat.id, gif, caption="Halo! Selamat datang di ITEBOT, bantuan apa yang diperlukan? ⸜(｡˃ ᵕ ˂ )⸝♡")
    gif.close()
    bot.reply_to(message, "Gunakan /help untuk melihat perintah yang tersedia. ᵔ ᵕ ᵔ")

# Help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "/start - Memulai ITEBOT\n"
        "/help - Menampilkan layanan yang tersedia\n"
        "/info - Menampilkan informasi bot\n"
        "/status - Menampilkan status bot\n"
        "/time - Menampilkan waktu saat ini\n"
        "/ask - Ajukan pertanyaan kepada bot\n"
        "/about - Mengenal lebih jauh tentang creator\n"
        "/contact - Untuk pertanyaan lain hubungi kontak berikut\n"
    )
    bot.reply_to(message, help_text)

# Info
@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "Bot ini dibuat oleh kelompok 2 sebagai akses informasi Desa Cilembu yang merupakan implementasi proyek kuliah Pancasila ITB.")

# Status 
@bot.message_handler(commands=['status'])
def send_status(message):
    bot.reply_to(message, "Bot sedang online")

# Time 
@bot.message_handler(commands=['time'])
def send_time(message):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    bot.reply_to(message, f"Waktu saat ini adalah : {current_time}")

# About
@bot.message_handler(commands=['about'])
def send_about(message):
    about_image = open(r'C:\Users\riant\Documents\ITEBOT\About.jpg', 'rb')
    caption = (
        "Nama Anggota / Fakultas / Universitas:\n"
        "\n"
        "1. Yavie Azka Putra Araly / STEI-K / ITB\n"
        "2. Aldyto Rafif Abhinaya / STEI-K / ITB\n"
        "3. Riantama Putra / STEI-K / ITB\n"
        "4. Zahra Aulia / STEI-R / ITB\n"
    )
    bot.send_photo(message.chat.id, about_image, caption=caption)
    about_image.close()

# Contact
@bot.message_handler(commands=['contact'])
def send_contact(message):
    bot.reply_to(message, "https://t.me/zahraula")

# Ask
@bot.message_handler(commands=['ask'])
def ask_question(message):
    markup = types.InlineKeyboardMarkup()
    for number, question in questions_and_answers.items():
        markup.add(types.InlineKeyboardButton(text=question, callback_data=f"answer_{number}"))
    bot.send_message(message.chat.id, "Pilih pertanyaan untuk melihat jawabannya:", reply_markup=markup)

# Handle callback query when a button is clicked
@bot.callback_query_handler(func=lambda call: call.data.startswith('answer_'))
def handle_question_answer(call):
    question_number = int(call.data.split('_')[1])
    answer_text = answers.get(question_number, "Maaf, tidak ada jawaban untuk pertanyaan ini.")
    send_long_message(call.message.chat.id, answer_text, parse_mode='HTML')

# Long message handler
def send_long_message(chat_id, text, parse_mode=None):
    MAX_MESSAGE_LENGTH = 4096
    while len(text) > MAX_MESSAGE_LENGTH:
        split_pos = text.rfind(' ', 0, MAX_MESSAGE_LENGTH)
        if split_pos == -1:
            split_pos = MAX_MESSAGE_LENGTH
        bot.send_message(chat_id, text[:split_pos], parse_mode=parse_mode)
        text = text[split_pos:].lstrip()
    bot.send_message(chat_id, text, parse_mode=parse_mode)

# Error handling
@bot.message_handler(func=lambda message: True)
def unknown_command(message):
    bot.reply_to(message, "Maaf, Saya tidak bisa mengenali perintah tersebut (╥﹏╥). Gunakan /help untuk melihat perintah yang tersedia.")

print("Bot is running...")

# Keep the bot running
bot.polling()