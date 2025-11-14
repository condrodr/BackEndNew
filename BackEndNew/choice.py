## Jika choice ada di Tabel (urut dari atas) sebelumnya maka akan direuse diselanjutnya 
## SEMUA PENGAJUAN DAN PERUBAHAN DISINI HARUS PERSETUJUAN DIREKTUR, MANAGER TIDAK BERHAK MERUBAH OPSI CHOICE

## CHOICES di Customer ##

choice_kategori_outlet = [
    ('2W','2W'),
    ('4W','4W'),
    ('6W','6W'),
    ('2W4W','2W4W'),
    ('4W6W','4W6W'),
    ('2W6W','2W6W'),
    ('2W4W6W','2W4W6W'),
    ('Pabrik','Pabrik'),
    ('Tambang','Tambang'),
    ('Alat Berat','Alat Berat'),
    ('Sub Contractor','Sub Contractor'),
    ('Crusher','Crusher'),
    ('Kapal Tangker','Kapal Tangker'),
    ('Kapal Nelayan','Kapal Nelayan'),
    ('Pembangkit','Pembangkit'),
    ('PO Bus','PO Bus'),
    ('Trucking','Trucking'),
    ('Logistik','Logistik'),
    ('Perkebunan','Perkebunan'),
    ('Peternakan','Peternakan'),
    ('Pengolahan','Pengolahan'),
    ('Industri Lain','Industri Lain')
]


choice_level_outlet = [
    ('kecil','kecil'),
    ('sedang','sedang'),
    ('besar','besar'),
    ('sangat besar','sangat besar')
]

choice_tipe_outlet = [
    ('kelilingan','kelilingan'),
    ('toko','toko'),
    ('bengkel','bengkel'),
    ('spbu','spbu'),
    ('bengkel own channel','bengkel own channel'),
    ('industri','industri'),
    ('KAM','KAM'),
    ('atpm','atpm')
]

choice_bentuk_usaha_outlet = [
    ('PT','PT'),
    ('CV','CV'),
    ('Koperasi','Koperasi'),
    ('Yayasan','Yayasan'),
    ('UD','UD'),
    ('BUMN','BUMN'),
    ('BUMD','BUMD'),
    ('Perorangan','Perorangan')
]

choice_lebar_muka_jalan = [
    ('lebih kecil dari 4m','lebih kecil dari 4m'),
    ('4m sampai 8m','4m sampai 8m'),
    ('lebih dari 8m','lebih dari 8m'),
]

choice_tipe_lokasi_outlet = [
    ('R1','R1'),
    ('R2','R2'),
    ('R3','R3'),
    ('R4','R4')
]

choice_kondisi_outlet = [
    ('terawat','terawat'),
    ('kurang terawat','kurang terawat'),
    ('tidak terawat','tidak terawat')
]

choice_oli_dominan = [
    ('Shell Motor','Shell Motor'),
    ('Shell Mobil','Shell Mobil'),
    ('Pertamina','Pertamina'),
    ('MPX','MPX'),
    ('Federal','Federal'),
    ('Evalube','Evalube'),
    ('Merek Lain','Merek Lain')
]

choice_bisnis_fokus_outlet = [
    ('ban','ban'), 
    ('oli','oli'),
    ('aki','aki'),
    ('sparepart','sparepart'),
    ('bisnis lain','bisnis lain')
]


choice_estimasi_nilai_stok = [
    ('dibawah 5 juta','dibawah 5 juta'),
    ('5-20 juta','5-20 juta'),
    ('diatas 20 juta','diatas 20 juta')
]

choice_cluster_outlet = [
    ('Industri','Industri'),
    ('KAM','KAM'),
    ('cikebu','cikebu'),
    ('babawopa','babawopa'),
    ('temapur','temapur'),
    ('DIY','DIY'),
    ('Luar Cluster','Luar Cluster')
]

choice_divisi_kantor = [
    ('Pelumas','Pelumas'), 
    ('LPG NPSO','LPG NPSO'),
    ('LPG PSO','LPG PSO'),
    ('Minyak Inmar','Minyak Inmar'),
    ('Customer Goods','Customer Goods')
]

choice_perusahaan_kantor = [
    ('PT. Gelora Putra Perkasa','PT. Gelora Putra Perkasa'),
    ('PT. Gelora Portalindo','PT. Gelora Portalindo'),
    ('PT. Buana Rahayu','PT Buana Rahayu'),
    ('PT. Sochi Jaya Sentosa','PT. Sochi Jaya Sentosa'),
    ('PT. Serayu Mitra Jaya','PT. Serayu Mitra Jaya')
]

choice_rute_kunjungan = [
    ('0','0'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('belum ada','belum ada')
]

choice_tipe_promo = [
    ('single produk','single produk'), 
    ('by merek','by merek'),
    ('by submerek','by submerek'),
    ('by tiersegmen','by tiersegmen'),
    ('by usersegmen','by usersegmen'),
    ('by kategori','by kategori'),
    ('by klasifikasi','by klasifikasi'),
    ('by spek','by spek'),
    ('by produsen','by produsen'),
    ('by jenis','by jenis'),
    ('all produk','all produk')
]

## CHOICES di Produk ##
choice_kemasan = [
    ('Dus','Dus'),
    ('Botol','Botol'),
    ('Drum','Drum'),
    ('Pail','Pail'),
    ('Pcs','Pcs'),
    ('Ikat','Ikat')
]

choice_isi_pack = [
    (0,0),
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (8,8),
    (10,10),
    (12,12),
    (15,15),
    (20,20),
    (24,24),
    (25,25),
    (30,30),
    (32,32),
    (35,35),
    (48,48),
    (50,50),
    (56,56),
    (60,60),
    (70,70),
    (100,100),
    (150,150),
    (180,180),
    (200,200)
]

choice_volume_pcs = [
    (0,0),
    (0.05,0.05),
    (0.07,0.07),
    (0.12,0.12),
    (0.15,0.15),
    (0.16,0.16),
    (0.3,0.3),
    (0.4,0.4),
    (0.5,0.5),
    (0.65,0.65),
    (0.7,0.7),
    (0.8,0.8),
    (1.0,1.0),
    (1.2,1.2),
    (3.5,3.5),
    (4.0,4.0),
    (5.0,5.0),
    (10.0,10.0),
    (16.0,16.0),
    (18.0,18.0),
    (20.0,20.0),
    (178.0,178.0),
    (200.0,200.0),
    (209.0,209.0)
]

choice_merek = [
    ('Enduro','Enduro'),('Fastron','Fastron'),('Mesran','Mesran'),('Meditran','Meditran'),
    ('Prima XP','Prima XP'),('Rored','Rored'),('Pertamina','Pertamina'),('Gemuk Pertamina','Gemuk Pertamina'),
    ('Masri','Masri'),('Medripal','Medripal'),('Kompen','Kompen'),('Turalik','Turalik'),('Trafolube','Trafolube'),
    ('Turbolube','Turbolube'),('Salyx','Salyx'),('Translik','Translik'),('Enviro','Enviro'),
    ('Diloka','Diloka'),('Gandar','Gandar'),('GC Lube','GC Lube'),('NG Lube','NG Lube'),('Knito','Knito'),
    ('Sebana','Sebana'),('Silinap','Silinap'),('Steelo','Steelo'),('Termo','Termo'),('MPX','MPX'),
    ('Federal','Federal'),('Mobil','Mobil'),('SPX','SPX'),('Advance','Advance'),('Helix','Helix'),
    ('Evalube','Evalube'),('Idemitsu','Idemitsu'),('Top1','Top1'),('Rimula','Rimula'),('Castrol','Castrol'),
    ('Orange','Orange'),('Jumbo','Jumbo'),('Ban AHM', 'Ban AHM'),('Aki Yuasa', 'Aki Yuasa'),('Aki GS','Aki GS'),('Agip','Agip'),
    ('Repsol','Repsol'),('Yamalube','Yamalube'),('Ban IRC','Ban IRC'),('Busi NGK','Busi NGK'),
    ('Megacool','Megacool'),('Busi Champion','Busi Champion'),('Motul','Motul'),('Unnoco','Unnoco'),
    ('Treebond','Treebond'),('Ban Kingland','Ban Kingland'),('TMO','TMO'),('Fortag','Fortag'),
    ('Prestone','Prestone')
]

choice_submerek = [
    ('Enduro Racing', 'Enduro Racing'), ('Enduro Matic', 'Enduro Matic'), ('Enduro Matic S', 'Enduro Matic S'),
    ('Enduro Matic G', 'Enduro Matic G'), ('Enduro Gear Matic', 'Enduro Gear Matic'), ('Enduro Matic V', 'Enduro Matic V'),
    ('Enduro Sport', 'Enduro Sport'), ('Enduro 4T', 'Enduro 4T'), ('Prima XP 10W-40', 'Prima XP 10W-40'),
    ('Prima XP 20W-50', 'Prima XP 20W-50'), ('Mesran 40', 'Mesran 40'), ('Mesran B40', 'Mesran B40'),
    ('Mesrania 2T', 'Mesrania 2T'), ('Mesran Marine', 'Mesran Marine'), ('Fastron Gold', 'Fastron Gold'),
    ('Fastron Techno', 'Fastron Techno'), ('Fastron Diesel', 'Fastron Diesel'), ('Fastron EcoGreen', 'Fastron EcoGreen'),
    ('Fastron Platinum', 'Fastron Platinum'), ('Coolant', 'Coolant'), ('ATF', 'ATF'), ('Break Fluid', 'Break Fluid'),
    ('Gemuk SGX', 'Gemuk SGX'), ('Gemuk EPX', 'Gemuk EPX'), ('Enviro', 'Enviro'), ('Diloka', 'Diloka'),
    ('Gandar', 'Gandar'), ('GC Lube M', 'GC Lube M'), ('GC Lube Syn', 'GC Lube Syn'), ('Knito', 'Knito'),
    ('NG Lube', 'NG Lube'), ('Maxcool NC', 'Maxcool NC'), ('Maxcool SM', 'Maxcool SM'), ('Maxcool Syn', 'Maxcool Syn'),
    ('Maxcool WS', 'Maxcool WS'), ('Rinsol', 'Rinsol'), ('Rubbsol', 'Rubbsol'), ('Rusguard', 'Rusguard'),
    ('Slideway', 'Slideway'), ('Refro', 'Refro'), ('Sebana P', 'Sebana P'), ('Silinap', 'Silinap'),
    ('Spreeze', 'Spreeze'), ('Steelo', 'Steelo'), ('Termo', 'Termo'), ('Termo XT', 'Termo XT'),
    ('Trafolube', 'Trafolube'), ('Meditran SC', 'Meditran SC'), ('Meditran S40', 'Meditran S40'),
    ('Meditran SX Bio', 'Meditran SX Bio'), ('Meditran SX', 'Meditran SX'), ('Mesran', 'Mesran'),
    ('Mesran Super', 'Mesran Super'), ('Mesran Super Motor', 'Mesran Super Motor'), ('Rored EPA', 'Rored EPA'),
    ('Rored HDA', 'Rored HDA'), ('Rored MTF', 'Rored MTF'), ('Gemuk HDX-2', 'Gemuk HDX-2'), ('Gemuk LI CX-2', 'Gemuk LI CX-2'),
    ('Gemuk Super EPX-2', 'Gemuk Super EPX-2'), ('Gemuk Super HDX-2', 'Gemuk Super HDX-2'), ('Gemuk WR-NL', 'Gemuk WR-NL'),
    ('Gemuk X-NL2', 'Gemuk X-NL2'), ('Gemuk X-NL3', 'Gemuk X-NL3'), ('Kompen', 'Kompen'), ('Masri FLG', 'Masri FLG'),
    ('Masri RG', 'Masri RG'), ('Masri SMG', 'Masri SMG'), ('Masri Syn', 'Masri Syn'), ('Meditran', 'Meditran'),
    ('Meditran E', 'Meditran E'), ('Meditran GEO', 'Meditran GEO'), ('Meditran P', 'Meditran P'), ('Meditran S', 'Meditran S'),
    ('Meditran SMX', 'Meditran SMX'), ('Meditran SV', 'Meditran SV'), ('Meditran SXV', 'Meditran SXV'), ('Medripal', 'Medripal'),
    ('Salyx', 'Salyx'), ('Salyx C', 'Salyx C'), ('Salyx DF', 'Salyx DF'), ('Translik', 'Translik'),
    ('Turalik', 'Turalik'), ('Turalik C', 'Turalik C'), ('Turalik CX', 'Turalik CX'), ('Turalik T', 'Turalik T'),
    ('Turalik V', 'Turalik V'), ('Turalik XT', 'Turalik XT'), ('Turbolube', 'Turbolube'), ('Turbolube XT', 'Turbolube XT'),
    ('AHM Chainlube', 'AHM Chainlube'), ('AHM Gear', 'AHM Gear'), ('Brake Fluid', 'Brake Fluid'),
    ('AHM Coolant', 'AHM Coolant'), ('Fortag Chain Lube', 'Fortag Chain Lube'), ('Carb Cleaner 2B', 'Carb Cleaner 2B'),
    ('Carb Cleaner', 'Carb Cleaner'), ('Prestone Rem', 'Prestone Rem'), ('TMO', 'TMO'), ('Yamaha YTZ', 'Yamaha YTZ'),
    ('AHM Ban K59 A12', 'AHM Ban K59 A12'), ('AHM Ban K59 A72', 'AHM Ban K59 A72'), ('AHM Ban KVB', 'AHM Ban KVB'),
    ('AHM Ban K93', 'AHM Ban K93'), ('AHM Ban KOJ', 'AHM Ban KOJ'), ('AHM Ban KOW', 'AHM Ban KOW'),
    ('AHM Ban KPH', 'AHM Ban KPH'), ('AHM Ban KTM', 'AHM Ban KTM'), ('AHM Ban KWW', 'AHM Ban KWW'),
    ('Alfabatt', 'Alfabatt'), ('AHM Bearing', 'AHM Bearing'), ('Busi AHM U20', 'Busi AHM U20'), ('Busi AHM U22', 'Busi AHM U22'),
    ('AHM Filter Udara', 'AHM Filter Udara'), ('AHM Gearset', 'AHM Gearset'), ('IRC BD Ring 17', 'IRC BD Ring 17'),
    ('IRC BD Ring 18', 'IRC BD Ring 18'), ('IRC BD Ring 14', 'IRC BD Ring 14'), ('IRC BL Ring 12 TL', 'IRC BL Ring 12 TL'),
    ('IRC BL Ring 17', 'IRC BL Ring 17'), ('IRC BL Ring 18', 'IRC BL Ring 18'), ('IRC BL Ring 13 TL', 'IRC BL Ring 13 TL'),
    ('IRC BL Ring 19', 'IRC BL Ring 19'), ('IRC BL Ring 20', 'IRC BL Ring 20'), ('IRC BL Ring 21', 'IRC BL Ring 21'),
    ('IRC BL Ring 22', 'IRC BL Ring 22'), ('IRC BL Ring 23', 'IRC BL Ring 23'), ('IRC BL Ring 24', 'IRC BL Ring 24'),
    ('IRC BL Ring 25', 'IRC BL Ring 25'), ('IRC BL Ring 14', 'IRC BL Ring 14'), ('IRC BL Ring 14 TL', 'IRC BL Ring 14 TL'),
    ('IRC BL Ring 16', 'IRC BL Ring 16'), ('AHM Kabel Speedo', 'AHM Kabel Speedo'), ('AHM Kampas Rem', 'AHM Kampas Rem'),
    ('King Jaguar BL Ring 14', 'King Jaguar BL Ring 14'), ('King Jaguar BL Ring 17', 'King Jaguar BL Ring 17'),
    ('King Tiger BL Ring 14', 'King Tiger BL Ring 14'), ('AHM Lampu KFV', 'AHM Lampu KFV'), ('AHM Oil Seal', 'AHM Oil Seal'),
    ('AHM Pelindung Knalpot', 'AHM Pelindung Knalpot'), ('AHM Rantai Keteng', 'AHM Rantai Keteng'), ('AHM Roller', 'AHM Roller'),
    ('AHM Rumah Roller', 'AHM Rumah Roller'), ('AHM Seal Shock', 'AHM Seal Shock'), ('AHM Shockbeker Assy', 'AHM Shockbeker Assy'),
    ('AHM Vanbelt', 'AHM Vanbelt'), ('Agip 2T', 'Agip 2T'), ('MPX1', 'MPX1'), ('MPX2', 'MPX2'),
    ('MPX3', 'MPX3'), ('Castrol Active', 'Castrol Active'), ('Castrol Active Matic', 'Castrol Active Matic'),
    ('Castrol 2T', 'Castrol 2T'), ('Castrol 4T', 'Castrol 4T'), ('Castrol Magnatec', 'Castrol Magnatec'),
    ('Castrol Power', 'Castrol Power'), ('Evalube 2T', 'Evalube 2T'), ('Evalube 2T Pro', 'Evalube 2T Pro'),
    ('Evalube 4T', 'Evalube 4T'), ('Federal Flick', 'Federal Flick'), ('Federal Gear', 'Federal Gear'),
    ('Federal Matic Orange', 'Federal Matic Orange'), ('Federal Ultratec', 'Federal Ultratec'), ('Federal XX', 'Federal XX'),
    ('Idemitsu 2T', 'Idemitsu 2T'), ('Motul 3100', 'Motul 3100'), ('Motul 510', 'Motul 510'),
    ('Motul 5100', 'Motul 5100'), ('Motul Scooter', 'Motul Scooter'), ('Jumbo Rem', 'Jumbo Rem'),
    ('Jumbo Shock', 'Jumbo Shock'), ('Orange Tropical', 'Orange Tropical'), ('Repsol MXR3', 'Repsol MXR3'),
    ('Repsol MXR Matic', 'Repsol MXR Matic'), ('Shell 2TSX', 'Shell 2TSX'), ('Shell AX3', 'Shell AX3'),
    ('Shell AX5', 'Shell AX5'), ('Shell AX5 Sc', 'Shell AX5 Sc'), ('Shell AX7', 'Shell AX7'),
    ('Shell AX7 Sc', 'Shell AX7 Sc'), ('Shell HX3', 'Shell HX3'), ('Shell HX5', 'Shell HX5'),
    ('Shell HX6', 'Shell HX6'), ('Shell HX7', 'Shell HX7'), ('Shell HX8', 'Shell HX8'),
    ('Shell RX4', 'Shell RX4'), ('Shell RX4 LDP', 'Shell RX4 LDP'), ('SPX1', 'SPX1'),
    ('SPX2', 'SPX2'), ('Top1', 'Top1'), ('Unoco Coolant', 'Unoco Coolant'),
    ('Yamalube Matic', 'Yamalube Matic'), ('Yamalube Silver', 'Yamalube Silver'), ('Yamalube Sport', 'Yamalube Sport'),
    ('Yamalube Super Matic', 'Yamalube Super Matic'), ('GS GM5Z', 'GS GM5Z'), ('GS GTZ5S', 'GS GTZ5S'),
    ('GS GTZ6V', 'GS GTZ6V'), ('Yuasa YB5LB', 'Yuasa YB5LB'), ('Yuasa YTZ5V', 'Yuasa YTZ5V'),
    ('Yuasa YTZ6V', 'Yuasa YTZ6V'), ('Champion RG4HC', 'Champion RG4HC'), ('Champion Z9Y', 'Champion Z9Y'),
    ('NGK-BP7ES', 'NGK-BP7ES'), ('NGK-BP7HS', 'NGK-BP7HS'), ('NGK-BP8ES', 'NGK-BP8ES'),
    ('NGK-BP8HS', 'NGK-BP8HS'), ('NGK-C7HSA', 'NGK-C7HSA'), ('NGK-CPR6EA', 'NGK-CPR6EA'),
    ('NGK-D6HSA', 'NGK-D6HSA'), ('NGK-D8EA', 'NGK-D8EA'), ('TREEBOND', 'TREEBOND'),
    ('NGK-DP8EA', 'NGK-DP8EA'), ('NGK-T5999', 'NGK-T5999'), ('NGK-T6000', 'NGK-T6000'),
    ('Yamaha YTZ Kering', 'Yamaha YTZ Kering')
]

choice_tier = [
    ('Very High Tier','Very High Tier'),
    ('High Tier','High Tier'),
    ('Middle Tier','Middle Tier'),
    ('Low Tier','Low Tier'),
    ('Very Low Tier','Very Low Tier')
]

choice_user = [
    ('2W','2W'),
    ('4W','4W'),
    ('6W','6W'),
    ('Industrial','Industrial')
]


choice_kategori = [
    ('Ban','Ban'),
    ('Oli','Oli'),
    ('Aki','Aki'),
    ('Busi','Busi'),
    ('Sparepart','Sparepart')
]

choice_klasifikasi = [
    ('Retail','Retail'),
    ('Industri','Industri')
]


choice_user = [
    ('2W','2W'),
    ('4W','4W'),
    ('6W','6W'),
    ('Industrial','Industrial')
]

choice_urgency = [
    ('2W','2W'),
    ('4W','4W'),
    ('6W','6W'),
    ('Industrial','Industrial')
]

choice_jenis_penjualan = [
    ('Purchase Order','Purchase Order'),
    ('Tokopedia','Tokopedia'),
    ('Blibli','Blibli'),
    ('Power','Power'),
    ('Pembelian di Kantor','Pembelian di Kantor')
]

choice_detail_lokasi = [
    ('L1','L1'),
    ('L2','L2'),
    ('L3','L3')

]

choice_faktur = [
    ('Print Faktur','Print Faktur'),
    ('Faktur tidak Print','Faktur tidak Print'),
    ('Tanpa Faktur','Tanpa Faktur'),
    ('Gunggung','Gunggung'),
    ('Offline Req Gunggung','Offline Req Gunggung')
]
choice_kantor = [
    ('Cilacap','Cilacap'),
    ('Jogja','Jogja'),
    ('Purwokerto','Purwokerto'),
    ('Magelang','Magelang'),
    ('Wonosobo','Wonosobo'),
    ('Klaten','Klaten'),
    ('Kebumen','Kebumen'),
    ('Purworejo','Purworejo')
]

choice_nama_salesman = [
    ('Supervisor Cikebu','Supervisor Cikebu'),
    ('Supervisor Babawopa','Supervisor Babawopa'),
    ('Supervisor Temapur','Supervisor Temapur'),
    ('Supervisor DIY','Supervisor DIY'),
    ('Sales Cilacap Barat','Sales Cilacap Barat'),
    ('Sales Cilacap Timur','Sales Cilacap Timur'),
    ('Sales Kebumen ','Sales Kebumen'),
    ('Sales Wonosobo','Sales Wonosobo'),
    (f'Sales Banjarnegara Purbalingga','Sales Banjarnegara Purbalingga'),
    ('Sales Banyumas','Sales Banyumas'),
    ('Sales Magelang','Sales Magelang'),
    ('Sales Purworejo','Sales Purworejo'),
    ('Sales Jogja Barat Daya','Sales Jogja Barat Daya'),
    ('Sales Jogja Barat Laut','Sales Jogja Barat Laut'),
    ('Sales Jogja Tenggara','Sales Jogja Tenggara'),
    ('Sales Jogja Timur Laut','Sales Jogja Timur Laut'),
    ('Sales Jogja Kota','Sales Jogja Kota'),
    ('Kantor DIY','Kantor DIY'),
    ('Kantor Cikebu','Kantor Cikebu'),
    ('Kantor Babawopa','Kantor Babawopa'),
    ('Kantor Temapur','Kantor Temapur'),
    ('Sales Industry Barat','Sales Industry Barat'),
    ('Sales Industry Timur','Sales Industry Timur'),
    ('Sales Industry Tengah','Sales Industry Tengah'),
     ] 

choice_produsen = [
    ('Pertamina', 'Pertamina'), ('Exxon Federal', 'Exxon Federal'), ('Honda AHM', 'Honda AHM'), 
    ('Yamaha', 'Yamaha'), ('Repsol', 'Repsol'), ('Shell', 'Shell'), ('Castrol', 'Castrol'), 
    ('Idemitsu', 'Idemitsu'), ('Orange Oil', 'Orange Oil'), ('Motul', 'Motul'), ('United', 'United'), 
    ('Top1', 'Top1'), ('WGI Evalube', 'WGI Evalube'), ('Agip', 'Agip'), ('Gajah Tunggal', 'Gajah Tunggal'), 
    ('NGK', 'NGK'), ('Yuasa', 'Yuasa'), ('Megacool', 'Megacool'), ('AHM', 'AHM'), 
    ('Jumbo', 'Jumbo'), ('Prestone', 'Prestone'), ('Toyota TMO', 'Toyota TMO'), ('Ecco', 'Ecco'), 
    ('GS', 'GS'), ('Champion', 'Champion'), ('Kingland', 'Kingland'), ('Treebond Inc', 'Treebond Inc')
]

choice_jenis = [
    ('Fast Moving','Fast Moving'),
    ('Slow Moving','Slow Moving')
]

choice_debit_kredit = [
    ('debit','debit'),
    ('kredit','kredit')
]

choice_tipe_akun = [
    ('Aset', 'Aset'),
    ('Hutang', 'Hutang'),
    ('Modal', 'Pendapatan'),
    ('Pengeluaran', 'Pengeluaran')
]

choice_lokasi_kas = [
    ('BCA 0963024441','BCA 0963024441'), 
    ('BCA 0969003777','BCA 0969003777'),
    ('MANDIRI 1390009064423','MANDIRI 1390009064423'),
    ('MANDIRI 1370013051525','MANDIRI 1370013051525'),
    ('MANDIRI 1800004861086','MANDIRI 1800004861086'),
    ('MANDIRI 1800100827023','MANDIRI 1800100827023'),
    ('BRI 010601001118309','BRI 010601001118309'),
    ('Kas Pusat','Kas Pusat'),
    ('Kas DIY','Kas DIY'),
    ('Kas Purwokerto','Kas Purwokerto'),
    ('Kas Magelang','Kas Magelang'),
    ('Kas Kebumen','Kas Kebumen'),
    ('Kas Wonosobo','Kas Wonosobo'),
    ('Kas Klaten','Kas Klaten'),
    ('Kas Cilacap','Kas Cilacap'),
    ('Kas Purworejo','Kas Purworejo'),
    ('Kas Doku','Kas Doku')
]

choice_kategori_action = [
    ('Aset', 'Aset'),
    ('Hutang', 'Hutang'),
    ('Modal', 'Modal'),
    ('Pengeluaran', 'Pengeluaran'),
    ('Pendapatan', 'Pendapatan'),
    ('Biaya','Biaya')
]

choice_jenis_transaksi = [
    ('Terima Hutangan dari Bank','Terima Hutangan dari Bank'),
    ('Bayar Hutang ke Bank','Bayar Hutang ke Bank'),
    ('Pengeluaran Biaya','Pengeluaran Biaya'),
    ('Pengeluaran Pajak','Pengeluaran Pajak'),
    ('Terima Hutangan dari Owner','Terima Hutangan dari Owner'),
    ('Bayar Hutang ke Owner','Bayar Hutang ke Owner'),
    ('Beli Asset Kendaraan','Beli Asset Kendaraan'),
    ('Beli Asset Elektronik','Beli Asset Elektronik'),
    ('Prive ke Owner','Prive ke Owner'),
    ('Beli Asset Tanah','Beli Asset Tanah'),
    ('Beli Asset Bangunan','Beli Asset Bangunan'),
    ('Penjualan Asset','Penjualan Asset'),
    #Jual Asset belum ada, Jurnal Beli Investasi dan Jual (PPN seperti apa)
]

choice_biaya = [
    'biaya solar', #ops kirim
    'biaya bensin', #ops kirim
    'biaya HSK supir', #ops kirim
    'biaya kiriman motor', #ops kirim
    'biaya admin tebusan', #ops kirim
    'biaya bongkar muat', #ops kirim
    'biaya operasional gudang', #ops kirim
    'biaya kiriman expedisi', #ops kirim
    'biaya kiriman tak terduga', #ops kirim
    'biaya administrasi bunga bank', #ops kantor
    'biaya administrasi bank harian', #ops kantor
    'biaya ATK', #ops kantor
    'biaya uang catering makan kantor', #ops kantor
    'biaya percetakan', #ops kantor
    'biaya umum', #ops kantor
    'biaya fax dan foto copy', #ops kantor
    'biaya HSK admin', #ops kantor
    'biaya perbaikan perangkat lunak', #ops kantor
    'biaya iuran', #ops kantor
    'biaya listrik', #ops kantor
    'biaya maintenance', #ops kantor
    'biaya perawatan peralatan kantor', #ops kantor
    'biaya pembelian materai', #ops kantor
    'biaya pengiriman paket dan surat menyurat', #ops kantor
    'biaya PDAM', #ops kantor
    'biaya prive', #ops kantor
    'biaya pulsa CS', #ops kantor
    'biaya pulsa kantor', #ops kantor 
    'biaya internet', #ops kantor
    'biaya tagihan telepon', #ops kantor
    'biaya BPJS', #gaji
    'biaya uang cuti', #gaji
    'biaya fee transaksi', #gaji
    'biaya gaji karyawan', #gaji
    'biaya honorarium', #gaji
    'biaya reward karyawan', #gaji
    'biaya lembur', #gaji
    'biaya upah pekerja paruh waktu', #gaji
    'biaya jaminan sosial lain', #gaji
    'biaya operasional manager', #ops sales
    'biaya operasional salesman', #ops sales
    'biaya operasional supervisor', #ops sales
    'biaya pulsa salesman', #ops sales
    'biaya ban kendaraan', #perawatan kendaraan
    'biaya KIR kendaraan', #perawatan kendaraan
    'biaya perbaikan viar', #perawatan kendaraan
    'biaya servis dan ganti oli', #perawatan kendaraan
    'biaya sparepart kendaraan', #perawatan kendaraan
    'biaya perbaikan truk', #perawatan kendaraan
    'biaya terpal', #perawatan kendaraan
    'biaya pemeliharaan gedung', #perawatan kantor
    'biaya perjalanan dinas manager', #biaya perjalanan
    'biaya perjalanan umum', #biaya perjalanan
    'biaya handling', #ops kirim
    'biaya buy back', #promosi
    'biaya cash back', #promosi
    'biaya event promo', #promosi
    'biaya ongkir kapal', #ops kirim
    'biaya promosi', #promosi
    'biaya tak terduga', #promosi
    'biaya asuransi gudang', #asuransi
    'biaya asuransi kendaraan', #asuransi
    'biaya asuransi lain-lain', #asuransi
    'biaya sewa', #ops kantor 
    'biaya pengadaan merchandise', #promosi
    'biaya pengadaan seragam', #ops kantor
    'Pengeluaran PPH Pasal 21', #pajak
    'Pengeluaran PPH Pasal 25', #pajak
    'Pengeluaran PPH Pasal 29', #pajak
    'Pengeluaran PPH Pasal 22', #pajak
    'Pengeluaran PPH Pasal 23', #pajak
    'Pengeluaran PPH Sewa', #pajak
    'Pengeluaran PPN KMS', #pajak
    'Pengeluraran PPN',
    'Pengeluaran Pajak Deviden', #pajak
    'Pengeluaran Pajak Bumi dan Bangunan', #pajak
    'Pengeluaran PPH Badan Pasal 17', #pajak
    'Pengeluaran Pajak Kendaraan Bermotor', #pajak
    'beli kendaraan',
    'beli peralatan elektronik',
    'beli tanah',
    'beli bangunan',
    'Terima Pokok Hutangan Owner',
    'Bayar Pokok Hutang ke Owner',
    'Terima Pokok Hutangan Bank',
    'Bayar Pokok Hutang ke Bank',
    'setor ke BCA',
    'setor ke Mandiri',
    'setor ke Kas Pusat',
    'setor ke BRI',
    'setor ke Niaga',
    'Lain-Lain'
]

choice_bentuk_kas = [
    ('Bank Mandiri','Bank Mandiri'), 
    ('Bank BCA','Bank BCA'),
    ('Bank BRI','Bank BRI'),
    ('Bank Niaga','Bank Niaga'),
    ('Kas Tunai','Kas Tunai')
]

choice_jenis_lokasi = [
    ('Gudang Pcs','Gudang Pcs'), 
    ('Gudang Dus','Gudang Dus'),
    ('Gudang Palet','Gudang Palet')
]

choice_jenis_bg = [
    ('Bank Mandiri','Bank Mandiri'), 
    ('Bank BCA','Bank BCA'),
    ('Jasa','Jasa'),
    ('Bank BNI','Bank BNI'),
    ('Bank BRI','Bank BRI'),
    ('Bank Niaga','Bank Niaga'),
    ('Bank Permata','Bank Permata'),
    ('Lain-Lain','Lain-Lain'),
]
choice_penyimpanan_bg = [
    ('Cilacap','Cilacap'), 
    ('Jogja','Jogja'),
    ('Purwokerto','Purwokerto'),
    ('Magelang','Magelang'),
    ('Wonosobo','Wonosobo'),
    ('Klaten','Klaten'),
    ('Kebumen','Kebumen'),
    ('Purworejo','Purworejo'),
]
choice_kantor_cabang = [
    ('Cilacap','Cilacap'), 
    ('Jogja','Jogja'),
    ('Purwokerto','Purwokerto'),
    ('Magelang','Magelang'),
    ('Wonosobo','Wonosobo'),
    ('Klaten','Klaten'),
    ('Kebumen','Kebumen'),
    ('Purworejo','Purworejo'),
]
choice_macam_kas= [
    ('Bank Mandiri','Bank Mandiri'), 
    ('Bank BCA','Bank BCA'),
    ('Bank BRI','Bank BRI'),
    ('Bank Niaga','Bank Niaga'),
    ('Kas Tunai','Kas Tunai'),
    ('Kas Pusat','Kas Pusat'),
    ('Kas DIY','Kas DIY'),
    ('Kas Purwokerto','Kas Purwokerto'),
    ('Kas Magelang','Kas Magelang'),
    ('Kas Kebumen','Kas Kebumen'),
    ('Kas Wonosobo','Kas Wonosobo'),
    ('Kas Klaten','Kas Klaten'),
    ('Kas Cilacap','Kas Cilacap'),
    ('Kas Purworejo','Kas Purworejo'),
    # ('Kas Di Sales','Kas Di Sales'),
    # ('Kas Di Sales Cilacap Barat','Kas Di Sales Cilacap Barat'),
    ('Sales Cilacap Barat','Sales Cilacap Barat'),
    ('Sales Cilacap Timur','Sales Cilacap Timur'),
    ('Sales Kebumen ','Sales Kebumen'),
    ('Sales Wonosobo','Sales Wonosobo'),
    ('Sales Banjarnegara Purbalingga','Sales Banjarnegara Purbalingga'),
    ('Sales Banyumas','Sales Banyumas'),
    ('Sales Magelang','Sales Magelang'),
    ('Sales Purworejo','Sales Purworejo'),
    ('Sales Jogja Barat Daya','Sales Jogja Barat Daya'),
    ('Sales Jogja Barat Laut','Sales Jogja Barat Laut'),
    ('Sales Jogja Tenggara','Sales Jogja Tenggara'),
    ('Sales Jogja Timur Laut','Sales Jogja Timur Laut'),
    ('Sales Jogja Kota','Sales Jogja Kota'),
    ('Sales Industry Barat','Sales Industry Barat'),
    ('Sales Industry Timur','Sales Industry Timur'),
    ('Sales Industry Tengah','Sales Industry Tengah'),
]

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_all_choices(request):
    data = {
        "kategori_outlet": [val for val, _ in choice_kategori_outlet],
        "kategori": [val for val, _ in choice_kategori],
        "cluster_outlet": [val for val, _ in choice_cluster_outlet],
        "detail_lokasi": [val for val, _ in choice_detail_lokasi],
        "divisi_kantor": [val for val, _ in choice_divisi_kantor],
        "faktur": [val for val, _ in choice_faktur],
        "isi_pack": [val for val, _ in choice_isi_pack],
        "perusahaan_kantor": [val for val, _ in choice_perusahaan_kantor],
        "jenis": [val for val, _ in choice_jenis],
        "jenis_penjualan": [val for val, _ in choice_jenis_penjualan],
        "merek": [val for val, _ in choice_merek],
        "produsen": [val for val, _ in choice_produsen],
        "kemasan": [val for val, _ in choice_kemasan],
        "nama_salesman": [val for val, _ in choice_nama_salesman],
        "level_outlet": [val for val, _ in choice_level_outlet],
        "oli_dominan": [val for val, _ in choice_oli_dominan],
        "submerek": [val for val, _ in choice_submerek],
        "tier": [val for val, _ in choice_tier],
        "klasifikasi": [val for val, _ in choice_klasifikasi],
        "rute_kunjungan": [val for val, _ in choice_rute_kunjungan],
        "volume_pcs": [val for val, _ in choice_volume_pcs],
        "tipe_lokasi_outlet": [val for val, _ in choice_tipe_lokasi_outlet],
        "debit_kredit": [val for val, _ in choice_debit_kredit],
        "tipe_akun": [val for val, _ in choice_tipe_akun],
        "kategori_action": [val for val, _ in choice_kategori_action],
        "lokasi_kas": [val for val, _ in choice_lokasi_kas],
        "bentuk_kas": [val for val, _ in choice_bentuk_kas],
        "jenis_transaksi": [val for val, _ in choice_jenis_transaksi],
        "jenis_bg": [val for val, _ in choice_jenis_bg],
        "penyimpanan_bg": [val for val, _ in choice_penyimpanan_bg],
        "kantor_cabang": [val for val, _ in choice_kantor_cabang],
        "macam_kas": [val for val, _ in choice_macam_kas],
        "biaya": choice_biaya
        # bisa tambah lagi pilihan lainnya di sini
    }
    return Response(data)

