BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "jenis" (
	"id_jenis"	TEXT NOT NULL UNIQUE,
	"jenis"	TEXT NOT NULL UNIQUE,
	"harga"	INTEGER NOT NULL,
	PRIMARY KEY("id_jenis")
);
CREATE TABLE IF NOT EXISTS "pelanggan" (
	"id_pelanggan"	INTEGER NOT NULL UNIQUE,
	"firstname_pelanggan"	TEXT NOT NULL UNIQUE,
	"lastname__pelanggan"	INTEGER,
	"nohp_pelanggan"	TEXT NOT NULL,
	"email_pelanggan"	TEXT,
	PRIMARY KEY("id_pelanggan" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "pegawai" (
	"id_pegawai"	TEXT NOT NULL UNIQUE,
	"firstname_pegawai"	TEXT NOT NULL UNIQUE,
	"lastname_pegawai"	INTEGER,
	"nohp_pegawai"	TEXT NOT NULL,
	"email_pegawai"	TEXT,
	PRIMARY KEY("id_pegawai")
);
CREATE TABLE IF NOT EXISTS "transaksi" (
	"idtransaksi"	INTEGER NOT NULL UNIQUE,
	"id_pegawai"	INTEGER NOT NULL,
	"id_pelanggan"	INTEGER NOT NULL,
	"tglterima"	NUMERIC NOT NULL,
	"tglselesai"	NUMERIC NOT NULL,
	"totalpakaian"	INTEGER NOT NULL,
	"id_jenis"	TEXT NOT NULL,
	"jumlahberatjenis"	INTEGER NOT NULL,
	FOREIGN KEY("id_pegawai") REFERENCES "pegawai"("id_pegawai"),
	FOREIGN KEY("id_jenis") REFERENCES "jenis"("id_jenis"),
	FOREIGN KEY("id_pelanggan") REFERENCES "pelanggan"("id_pelanggan"),
	PRIMARY KEY("idtransaksi")
);
INSERT INTO "jenis" VALUES ('jenis01','Cuci Kering',6000);
INSERT INTO "jenis" VALUES ('jenis03','Cuci Setrika',7000);
INSERT INTO "jenis" VALUES ('jenis02','Setrika',6000);
INSERT INTO "pelanggan" VALUES (2,'Rani',NULL,'08xxxxxxxxxx','rani@gmail.com');
INSERT INTO "pegawai" VALUES ('pegawai01','Tanjiro',NULL,'081112222233',NULL);
COMMIT;
