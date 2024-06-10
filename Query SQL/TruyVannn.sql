--Thực hiện các truy vấn sử dụng các câu lệnh đã học (bao gồm INSERT, DELETE, UPDATE, SELECT).
--Mỗi câu lệnh tối thiểu 5 ví dụ khác nhau.
--Riêng phần câu lệnh select thực hiện lấy dữ liệu từ 1, 2, 3 bảng 
--có liên quan và có sử dụng mệnh đề group by, having.


-- I : INSERT
INSERT INTO KHACHHANG 
VALUES 
('KH000099', '0632970859', N'Phạm Đức', N'A', N'852 Đường TUV, Quận 19, Thành phố Bắc Ninh')

INSERT INTO KHACHHANG 
VALUES 
('KH000199', '0632888859', N'Nguyễn Đức', N'b', N'883 Đường TkUV, Quận 129, Thành phố Hải Dương')

INSERT INTO NHANVIEN 
VALUES
('NV000299', N'123 Đường CHS, Quận 11, Thành phố Hồ Chí Minh', N'Nguyễn Văn', '0223456789', N' A', 15000000.00, 'Tiếp viên');

INSERT INTO LoaiMayBay(MaLoai, HangSanXuat) 
VALUES
(31, 'VietJet Plus');

INSERT INTO MayBay 
VALUES ('VJ0011', 31,200);

INSERT INTO ChuyenBay
VALUES 
('CB000044', N'Sân Bay Nội Bài', N'Sân Bay Điện Biên', '2024-04-30 11:00:00', '2024-04-30 13:00:00')

INSERT INTO LichBay (NgayDi, MaChuyenBay, SoHieu, MaLoai) 
VALUES
('2024-04-30', 'CB000044', 'VA2292',19)

INSERT INTO DatCho (MaKH, NgayDi, MaChuyenBay)
VALUES
('KH000199', '2024-04-30', 'CB000044')

INSERT INTO DatCho (MaKH, NgayDi, MaChuyenBay)
VALUES
('KH000002', '2024-04-30', 'CB000044')

-- II : UPDATE
-- Ví Dụ 1 : cập nhật lại thông tinh sđt của 1 khách hàng có mã khách hàng là KH000006
UPDATE KhachHang
SET SDT = '0234562312'
WHERE MaKH = 'KH000006'

-- Ví Dụ 2 : Cập nhật lại giờ bay do thời tiết xấu
UPDATE ChuyenBay
SET GioDi = '2024-04-30 14:30:00'
WHERE MaChuyenBay = 'CB000007'

-- Ví dụ 3 : Thay đổi giờ đến do thời tiết xấu
UPDATE ChuyenBay
SET GioDi = '2024-04-30 18:30:00'
WHERE MaChuyenBay = 'CB000009'

-- Ví dụ 4 : cập nhật lại lương nhân viên
UPDATE NhanVien
SET Luong = 13000000
WHERE MANV = 'NV000002';

-- Ví dụ 5 : cập nhật lại hãng máy bay
UPDATE LoaiMayBay
SET HangSanXuat = 'Jetstar '
WHERE MaLoai = 20

-- Ví dụ 6 : Tăng lương 4% cho toàn bộ nhân viên

UPDATE NhanVien
SET Luong = Luong*1.04


--- III : SELECT 
-- Ví dụ 1 : Hãy liệt kê ra các hành khách đặt vé nhiều hơn 1 lần
SELECT  K.Ten , K.DiaChi , K.SDT,
		 COUNT(K.MaKH) AS "Số lần đặt vé"
FROM KhachHang K , DatCho D 
WHERE  K.MaKH = D.MaKH
GROUP BY K.DiaChi , K.Ten , K.SDT 
HAVING COUNT(K.MaKH) > 1
ORDER BY K.Ten


-- Ví dụ 2 : Từ lịch bay hãy show ra những hãng máy bay 
-- Kể cả máy bay chưa có người đặt chỗ 
SELECT DISTINCT(L.MaLoai)  ,L.SoHieu ,LMB.HangSanXuat , L.MaLoai
FROM LichBay L
RIGHT JOIN LoaiMayBay LMB
ON L.MaLoai = LMB.MaLoai

-- Ví dụ 3 : Tổng số Chuyến bay trong 1 ngày nhiều hơn 5 chuyến 
SELECT L.NgayDi  ,COUNT(*) "Tổng số chuyến bay trong một ngày "
FROM LichBay L 
GROUP BY L.NgayDi 
HAVING COUNT(*)  > 5


-- Ví dụ 4 : Hãy chỉ ra nhân viên có số lương cao nhất trong sân bay
SELECT TOP 1 *
FROM NhanVien N 
ORDER BY N.Luong DESC

-- Ví dụ 5 :- Tổng số chuyến bay theo từng loại máy bay nhiều hơn 1 lần bay
SELECT LMB.HangSanXuat, COUNT(MaChuyenBay) AS "Tổng Chuyến Bay"
FROM MayBay M , LoaiMayBay LMB , LICHBAY LB
WHERE M.MALOAI = LMB.MALOAI
	  AND M.SoHieu = LB.SoHieu
GROUP BY LMB.HangSanXuat
HAVING COUNT(MaChuyenBay) > 1 


--- DELETE

DELETE FROM DATCHO 
WHERE MaKH IN (SELECT MaKH FROM KHACHHANG WHERE SDT = '0123456789');

DELETE FROM KHACHHANG
WHERE SDT = '0123456789';

DELETE FROM DATCHO 
WHERE MaKH = 'KH000003' AND MaChuyenBay = 'CB000003';

DELETE FROM DATCHO
WHERE MaKH = 'KH000002';

DELETE FROM PhanCong
WHERE MaNV = 'NV000006';


