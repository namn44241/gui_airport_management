# README

## Mô tả chi tiết
Đây là một cơ sở dữ liệu (CSDL) được sử dụng để quản lý thông tin các chuyến bay của một sân bay, bao gồm:

- Quản lý thông tin khách hàng
- Quản lý thông tin nhân viên
- Quản lý thông tin máy bay
- Quản lý thông tin loại máy bay
- Quản lý thông tin chuyến bay
- Quản lý thông tin lịch bay
- Quản lý thông tin đặt chỗ
- Quản lý thông tin khả năng
- Quản lý thông tin phân công

## Mục đích
- Lưu trữ thông tin về các chuyến bay, bao gồm thông tin về các chuyến bay hiện tại, lịch sử các chuyến bay, thông tin về các hãng hàng không, máy bay và sân bay.
- Cung cấp khả năng tìm kiếm, cập nhật và xóa thông tin về các chuyến bay.
- Hỗ trợ quản lý sắp xếp lịch trình chuyến bay, kiểm tra tình trạng của các chuyến bay và thống kê thông tin liên quan đến các chuyến bay.

## Yêu cầu
- **Quản lý thông tin chuyến bay**: Lưu trữ thông tin về các chuyến bay như mã chuyến bay, sân bay đi, sân bay đến, giờ đi, giờ đến, loại máy bay.
- **Quản lý thông tin sân bay**: Lưu trữ thông tin về các sân bay như mã sân bay, tên sân bay, địa điểm, quốc gia.
- **Quản lý thông tin hãng hàng không**: Lưu trữ thông tin về các hãng hàng không như mã hãng hàng không, tên hãng hàng không, quốc gia.
- **Quản lý thông tin máy bay**: Lưu trữ thông tin về các máy bay như mã máy bay, tên máy bay, số lượng ghế.

## Quy trình xử lý bên trong hệ thống
- **Thêm chuyến bay mới**: Nhập thông tin về chuyến bay bao gồm mã chuyến bay, điểm khởi hành, điểm đến, thời gian khởi hành, thời gian đến và liên kết với các thông tin khác như sân bay, hãng hàng không và máy bay tương ứng.
- **Cập nhật thông tin chuyến bay**: Cho phép cập nhật thông tin về chuyến bay như thời gian khởi hành, thời gian đến hoặc điểm đến.
- **Xóa chuyến bay**: Loại bỏ thông tin về chuyến bay khỏi CSDL khi chuyến bay đã hoàn thành hoặc bị hủy bỏ.
- **Tìm kiếm chuyến bay**: Cung cấp chức năng tìm kiếm chuyến bay dựa trên các tiêu chí như điểm khởi hành, điểm đến hoặc thời gian khởi hành.

## Các trường hợp dữ liệu cần thiết
- **KhachHang** (MaKH, DiaChi, TenKH, SDT)
- **NhanVien** (DiaChi, SDT, MaNV, TenNV, Luong, LoaiNV)
- **LoaiMayBay** (MaLoai, HangSX)
- **MayBay** (SoHieu, SoGheNgoi)
- **ChuyenBay** (MaCB, TenSBDen, TenSBDi, GioDi, GioDen)
- **LichBay** (NgayDi, MaChuyenBay, SoHieu, MaLoai)
- **DatCho** (MaKH, NgayDi, MaChuyenBay)
- **PhanCong** (MaNV, NgayDi, MaChuyenBay)

## Thiết kế mô hình thực thể liên kết

### Mô tả qua về sơ đồ ERD
- Lược đồ E-R gồm 6 tập thực thể mạnh.
- Mỗi chuyến bay có thể có 1 lịch bay, một lịch bay cụ thể chỉ sử dụng một máy bay. Giả sử mỗi chuyến bay chỉ được bố trí tối đa một lần cho một ngày.
- Mỗi máy bay chỉ thuộc 1 loại máy bay và 1 loại máy bay có thể có nhiều máy bay.
- Mỗi khách hàng có thể đặt chỗ theo lịch bay của hãng hàng không đưa ra. Giả sử mỗi khách hàng chỉ được phép đặt tối đa một chỗ trên một chuyến bay vào một ngày cụ thể và một lịch bay sẽ được đăng kí bởi nhiều khách hàng.
- Các nhân viên được phân công vào một hay nhiều lịch bay, một lịch bay sẽ cần nhiều nhân viên.
- Một loại máy bay sẽ được sử dụng cho nhiều lịch bay.
