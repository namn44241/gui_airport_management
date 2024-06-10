CREATE DATABASE QuanLiSanBay
USE QuanLiSanBay

CREATE TABLE KhachHang (
	MaKH NCHAR(8) NOT NULL PRIMARY KEY,
	SDT VARCHAR (10) CHECK (SDT LIKE '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'), 
	HoDem NVARCHAR(30), 
	Ten NVARCHAR(20),
	DiaChi NVARCHAR(80)
);

CREATE TABLE NhanVien (
	MaNV NCHAR(8) NOT NULL PRIMARY KEY ,
	DiaChi NVARCHAR (80) NOT NULL,
	HoDem NVARCHAR(30) ,
    SDT VARCHAR (10) CHECK (SDT LIKE '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
	Ten NVARCHAR (20),
    Luong DECIMAL(18, 2),
    LoaiNV NVARCHAR(40) DEFAULT 'Tiếp viên'
);


CREATE TABLE LoaiMayBay (
	MaLoai INT NOT NULL ,
	HangSanXuat NVARCHAR (80),
	PRIMARY KEY (MaLoai),
)

CREATE TABLE MayBay (
    SoHieu NCHAR(10) PRIMARY KEY,
    MaLoai INT,
	SoGheNgoi INT ,
    FOREIGN KEY (MaLoai) REFERENCES LoaiMayBay(MaLoai)
);

CREATE TABLE ChuyenBay (
	MaChuyenBay NCHAR(8) NOT NULL PRIMARY KEY ,
	TenSanBayDi NVARCHAR(50),
	TenSanBayDen NVARCHAR(50),
	GioDi DATETIME ,
	GioDen DATETIME , 
)


CREATE TABLE LichBay (
    NgayDi DATE,
    MaChuyenBay NCHAR(8),
    SoHieu  NCHAR(10),
    MaLoai INT,
    PRIMARY KEY (NgayDi, MaChuyenBay),
    FOREIGN KEY (MaChuyenBay) REFERENCES ChuyenBay(MaChuyenBay),
    FOREIGN KEY (SoHieu) REFERENCES MayBay(SoHieu),
    FOREIGN KEY (MaLoai) REFERENCES LoaiMayBay(MaLoai)
);

CREATE TABLE DatCho (
    MaKH NCHAR(8),
    NgayDi DATE,
    MaChuyenBay NCHAR(8),
    PRIMARY KEY (MAKH, NgayDi, MaChuyenBay),
    FOREIGN KEY (MAKH) REFERENCES KhachHang(MAKH),
    FOREIGN KEY (NgayDi, MaChuyenBay) REFERENCES LichBay(NgayDi, MaChuyenBay)
);

CREATE TABLE PhanCong (
    MaNV NCHAR(8),
    NgayDi DATE,
    MaChuyenBay NCHAR(8),
    PRIMARY KEY (MaNV, NgayDi, MaChuyenBay),
    FOREIGN KEY (MaNV) REFERENCES NhanVien(MaNV),
    FOREIGN KEY (NgayDi, MaChuyenBay) REFERENCES LICHBAY(NgayDi, MaChuyenBay)
);

-- Tạo bảng quản lý admin
CREATE TABLE Admins (
    UserName NVARCHAR(50) NOT NULL PRIMARY KEY,
    PasswordHash CHAR(32) NOT NULL
);

-- Hàm để mã hóa mật khẩu bằng MD5
CREATE FUNCTION dbo.HashPassword (@password NVARCHAR(255))
RETURNS CHAR(32)
AS
BEGIN
    RETURN CONVERT(CHAR(32), HASHBYTES('MD5', @password), 2)
END;

-- Ví dụ cách thêm tài khoản admin với mật khẩu được mã hóa bằng MD5
INSERT INTO Admins (UserName, PasswordHash)
VALUES 
('admin', dbo.HashPassword('yourpassword'));

