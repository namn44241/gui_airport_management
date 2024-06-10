---- Nhập dữ liệu khách hàng
-- Thêm 15 bản ghi vào bảng "KhachHang"
USE [QuanLiSanBay]

-- Ví dụ cách thêm tài khoản admin với mật khẩu được mã hóa bằng MD5
INSERT INTO Admins (UserName, PasswordHash)
VALUES 
('1', dbo.HashPassword('1'));


INSERT INTO KhachHang (MaKH, SDT, HoDem, TEN, DiaChi) VALUES
('KH000001', '0123456789', N'Nguyễn', N'Văn A', N'123 Đường ABC, Quận 1, Thành phố Hồ Chí Minh'),
('KH000002', '0987654321', N'Trần', N'Thị B', N'456 Đường XYZ, Quận 2, Thành phố Hồ Chí Minh'),
('KH000003', '0369852147', N'Lê', N'Đình C', N'789 Đường KLM, Quận 3, Thành phố Hồ Chí Minh'),
('KH000004', '0543219876', N'Phạm', N'Duy D', N'321 Đường DEF, Quận 4, Thành phố Hồ Chí Minh'),
('KH000005', '0798654321', N'Hoàng', N'Thị E', N'654 Đường MNO, Quận 5, Thành phố Hồ Chí Minh'),
('KH000006', '0234567890', N'Võ', N'Văn F', N'987 Đường GHI, Quận 6, Thành phố Hồ Chí Minh'),
('KH000007', '0456789123', N'Đặng', N'Thị G', N'159 Đường JKL, Quận 7, Thành phố Hồ Chí Minh'),
('KH000008', '0789456123', N'Trần', N'Văn H', N'753 Đường QRS, Quận 8, Thành phố Hồ Chí Minh'),
('KH000009', '0632147859', N'Nguyễn', N'Thị I', N'852 Đường TUV, Quận 9, Thành phố Hồ Chí Minh'),
('KH000010', '0978563412', N'Phan', N'Văn K', N'147 Đường WXY, Quận 10, Thành phố Hồ Chí Minh'),
('KH000011', '0365987412', N'Trần', N'Thị L', N'258 Đường ZAB, Quận 11, Thành phố Hồ Chí Minh'),
('KH000012', '0876543210', N'Hoàng', N'Văn M', N'369 Đường CDE, Quận 12, Thành phố Hồ Chí Minh'),
('KH000013', '0321456987', N'Lê', N'Thị N', N'951 Đường FGH, Quận Gò Vấp, Thành phố Hồ Chí Minh'),
('KH000014', '0798641235', N'Võ', N'Văn O', N'753 Đường IJK, Quận Bình Thạnh, Thành phố Hồ Chí Minh'),
('KH000015', '0978652143', N'Nguyễn', N'Thị P', N'246 Đường LMN, Quận Tân Bình, Thành phố Hồ Chí Minh')
-----------------------
INSERT INTO NhanVien (MaNV, DiaChi, HoDem, SDT, Ten, LUONG, LOAINV) VALUES
('NV000001', N'123 Đường ABC, Quận 1, Thành phố Hồ Chí Minh', N'Nguyễn', '0123456789', N'Văn A', 15000000.00, 'Tiếp viên'),
('NV000002', N'456 Đường XYZ, Quận 2, Thành phố Hồ Chí Minh', N'Trần', '0987654321', N'Thị B', 18000000.00, 'Phi công'),
('NV000003', N'789 Đường KLM, Quận 3, Thành phố Hồ Chí Minh', N'Lê', '0369852147', N'Đình C', 17000000.00, 'Tiếp viên'),
('NV000004', N'321 Đường DEF, Quận 4, Thành phố Hồ Chí Minh', N'Phạm', '0543219876', N'Duy D', 16000000.00, 'Phi công'),
('NV000005', N'654 Đường MNO, Quận 5, Thành phố Hồ Chí Minh', N'Hoàng', '0798654321', N'Thị E', 14000000.00, 'Tiếp viên'),
('NV000006', N'987 Đường GHI, Quận 6, Thành phố Hồ Chí Minh', N'Võ', '0234567890', N'Văn F', 19000000.00, 'Phi công'),
('NV000007', N'159 Đường JKL, Quận 7, Thành phố Hồ Chí Minh', N'Đặng', '0456789123', N'Thị G', 17000000.00, 'Tiếp viên'),
('NV000008', N'753 Đường QRS, Quận 8, Thành phố Hồ Chí Minh', N'Trần', '0789456123', N'Văn H', 16000000.00, 'Phi công'),
('NV000009', N'852 Đường TUV, Quận 9, Thành phố Hồ Chí Minh', N'Nguyễn', '0632147859', N'Thị I', 18000000.00, 'Tiếp viên'),
('NV000010', N'147 Đường WXY, Quận 10, Thành phố Hồ Chí Minh', N'Phan', '0978563412', N'Văn K', 20000000.00, 'Phi công'),
('NV000011', N'258 Đường ZAB, Quận 11, Thành phố Hồ Chí Minh', N'Trần', '0365987412', N'Thị L', 16000000.00, 'Tiếp viên'),
('NV000012', N'369 Đường CDE, Quận 12, Thành phố Hồ Chí Minh', N'Hoàng', '0876543210', N'Văn M', 18000000.00, 'Phi công'),
('NV000013', N'951 Đường FGH, Quận Gò Vấp, Thành phố Hồ Chí Minh', N'Lê', '0321456987', N'Thị N', 17000000.00, 'Tiếp viên'),
('NV000014', N'753 Đường IJK, Quận Bình Thạnh, Thành phố Hồ Chí Minh', N'Võ', '0798641235', N'Văn O', 19000000.00, 'Phi công'),
('NV000015', N'246 Đường LMN, Quận Tân Bình, Thành phố Hồ Chí Minh', N'Nguyễn', '0978652143', N'Thị P', 16000000.00, 'Tiếp viên');
------------------------------
-- Thêm 15 bản ghi vào bảng "LoaiMayBay" cho các loại máy bay của Việt Nam
INSERT INTO LoaiMayBay (MaLoai, HangSanXuat) VALUES
(16, 'Vietnam Airlines'),
(17, 'VietJet Air'),
(18, 'Bamboo Airways'),
(19, 'VASCO - Vietnam Air Services Company'),
(20, 'Jetstar Pacific Airlines'),
(21, 'Vietnam Helicopter Corporation (VNH)'),
(22, 'Vietnam Helicopters'),
(23, 'Vietnam Helicopter Corporation (VNH)'),
(24, 'Vietnam Peoples Air Force (VPAF)'),
(25, 'Vietnam Airlines Engineering Company (VAECO)'),
(26, 'Vietnam Aircraft Leasing Company (VALC)'),
(27, 'Vietnam Airlines Flight Training Center (VAFTC)'),
(28, 'Vietnam Air Traffic Management Corporation (VATM)'),
(29, 'Vietnam Airlines Caterers (VAC)'),
(30, 'Vietnam Airlines Ground Services (VIAGS)');

-- Thêm 15 bản ghi vào bảng "MayBay"
INSERT INTO MayBay (SoHieu, MaLoai, SoGheNgoi) VALUES
('VA2222', 16, 150),
('VJ0001', 17, 180),
('BA0003',18, 200),
('VA2292',19, 190),
('JP0012',20, 160),
('VNH0002', 21, 170),
('VH2221',22, 180),
('VNH0011', 23, 170),
('VPAF00', 24, 150),
('VAECO2', 25, 160),
('VALC009', 26, 180),
('VAFTC05', 27, 190),
('VATM08',28, 200),
('VAC003', 29, 180),
('VIAGS02', 30, 170);


-- Thêm 15 dòng dữ liệu vào bảng ChuyenBay với một sân bay cố định ở điểm đến hoặc đi
INSERT INTO ChuyenBay (MaChuyenBay, TenSanBayDi, TenSanBayDen, GioDi, GioDen) VALUES
    ('CB000001', N'Sân Bay Nội Bài', N'Sân bay Tân Sơn Nhất', '2024-04-11 08:00:00', '2024-04-11 10:00:00'),
    ('CB000002', N'Sân Bay Nội Bài', N'Sân bay Đà Nẵng', '2024-04-30 09:00:00', '2024-04-30 11:00:00'),
    ('CB000003', N'Sân Bay Nội Bài', N'Sân Bay Hải Phòng', '2024-04-30 10:00:00', '2024-04-30 12:00:00'),
    ('CB000004', N'Sân Bay Nội Bài', N'Sân Bay Điện Biên', '2024-06-30 11:00:00', '2024-06-30 13:00:00'),
    ('CB000005', N'Sân Bay Nội Bài', N'Sân bay Đà Nẵng', '2024-04-03 12:00:00', '2024-04-03 14:00:00'),
    ('CB000006', N'Sân bay Đà Nẵng', N'Sân Bay Nội Bài', '2024-04-30 13:00:00', '2024-04-30 15:00:00'),
    ('CB000007', N'Sân Bay Nội Bài', N'San Bay Sài Gòn', '2024-04-30 14:00:00', '2024-04-30 16:00:00'),
    ('CB000008', N'Sân Bay Nội Bài', N'Sân Bay Cần Thơ', '2024-04-30 15:00:00', '2024-04-30 17:00:00'),
    ('CB000009', N'Sân Bay Buôn Ma Thuật', N'Sân Bay Nội Bài', '2024-04-30 16:00:00', '2024-04-30 18:00:00'),
    ('CB000010', N'Sân Bay Nội Bài', N'Sân Bay Buôn Ma Thuật', '2024-04-30 17:00:00', '2024-04-30 19:00:00'),
    ('CB000011', N'Sân Bay Nội Bài', N'Sân Bay Nội Bài', '2024-05-22 18:00:00', '2024-05-22 20:00:00'),
    ('CB000012', N'Sân Bay Nội Bài', N'Sân bay Tân Sơn Nhất', '2024-04-30 19:00:00', '2024-04-30 21:00:00'),
    ('CB000013', N'Sân Bay Nội Bài', N'Sân Bay Hải Phòng', '2024-04-30 20:00:00', '2024-04-30 22:00:00'),
    ('CB000014', N'Sân Bay Điện Biên', N'Sân Bay Nội Bài', '2024-04-30 21:00:00', '2024-04-30 23:00:00'),
    ('CB000015', N'Sân Bay Nội Bài', N'Sân Bay Điện Biên', '2024-04-30 22:00:00', '2024-05-01 00:00:00')



-- Thêm 15 dòng dữ liệu vào bảng LichBay
INSERT INTO LichBay (NgayDi, MaChuyenBay, SoHieu, MaLoai) VALUES
    ('2024-04-11', 'CB000001', 'VA2222', 16),
    ('2024-04-30', 'CB000002', 'VJ0001', 17),
    ('2024-04-30', 'CB000003', 'BA0003',18),
    ('2024-06-30', 'CB000004', 'VA2292',19),
    ('2024-04-03', 'CB000005', 'JP0012',20),
    ('2024-04-30', 'CB000006', 'VNH0002', 21),
    ('2024-04-30', 'CB000007', 'VH2221',22),
    ('2024-04-30', 'CB000008', 'VNH0011', 23),
    ('2024-04-30', 'CB000009', 'VPAF00', 24),
    ('2024-04-30', 'CB000010', 'VAECO2', 25),
    ('2024-05-22', 'CB000011', 'VALC009', 26),
    ('2024-04-30', 'CB000012', 'VAFTC05', 27),
    ('2024-04-30', 'CB000013', 'VATM08',28),
    ('2024-04-30', 'CB000014', 'VAC003', 29),
    ('2024-04-30', 'CB000015', 'VIAGS02', 30);

-- Thêm 15 dòng dữ liệu vào bảng DatCho
INSERT INTO DatCho (MaKH, NgayDi, MaChuyenBay) VALUES
    ('KH000001', '2024-04-11', 'CB000001'),
    ('KH000002', '2024-04-30', 'CB000002'),
    ('KH000003', '2024-04-30', 'CB000003'),
    ('KH000004', '2024-06-30', 'CB000004'),
    ('KH000005', '2024-04-03', 'CB000005'),
    ('KH000006', '2024-04-30', 'CB000006'),
    ('KH000007', '2024-04-30', 'CB000007'),
    ('KH000008', '2024-04-30', 'CB000008'),
    ('KH000009', '2024-04-30', 'CB000009'),
    ('KH000010', '2024-04-30', 'CB000010'),
    ('KH000011', '2024-05-22', 'CB000011'),
    ('KH000012', '2024-04-30', 'CB000012'),
    ('KH000013', '2024-04-30', 'CB000013'),
    ('KH000014', '2024-04-30', 'CB000014'),
    ('KH000015', '2024-04-30', 'CB000015');




-- Thêm 15 dòng dữ liệu vào bảng PhanCong
INSERT INTO PhanCong (MaNV, NgayDi, MaChuyenBay) VALUES
('NV000001', '2024-04-11', 'CB000001'),
('NV000002', '2024-04-30', 'CB000002'),
('NV000003', '2024-04-30', 'CB000003'),
('NV000004', '2024-06-30', 'CB000004'),
('NV000005', '2024-04-03', 'CB000005'),
('NV000006', '2024-04-30', 'CB000006'),
('NV000007', '2024-04-30', 'CB000007'),
('NV000008', '2024-04-30', 'CB000008'),
('NV000009', '2024-04-30', 'CB000009'),
('NV000010', '2024-04-30', 'CB000010'),
('NV000011', '2024-05-22', 'CB000011'),
('NV000012', '2024-04-30', 'CB000012'),
('NV000013', '2024-04-30', 'CB000013'),
('NV000014', '2024-04-30', 'CB000014'),
('NV000015', '2024-04-30', 'CB000015');