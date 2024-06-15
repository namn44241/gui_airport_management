from flask import Flask, render_template, request, redirect, url_for, render_template_string, jsonify, session
import pyodbc
import os
from datetime import datetime

app = Flask(__name__)
app.static_folder = 'static' 
app.secret_key = os.urandom(24)

# Thông tin kết nối
dsn = 'QuanLiSanBay'
cnxn = pyodbc.connect(f'DSN={dsn}')
cursor = cnxn.cursor()
                           
@app.route('/test_connection')
def test_connection():
    try:
        query = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES"
        cursor.execute(query)
        tables = cursor.fetchall()
        return f"Kết nối thành công! Danh sách các bảng: {tables}"
    except Exception as e:
        return f"Kết nối thất bại: {str(e)}"
    
@app.route('/')
def login():
    if 'username' in session:
        return redirect(url_for('admin'))  # Chuyển hướng nếu đã đăng nhập
    
    # Hiển thị form đăng nhập nếu chưa đăng nhập
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Đăng nhập</title>
        <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    </head>
    <body onload="showLoginDialog()">
        <script>
            function showLoginDialog() {
                Swal.fire({
                    title: 'Đăng nhập',
                    html: `
                        <input id="username" class="swal2-input" placeholder="Tài khoản">
                        <input id="password" type="password" class="swal2-input" placeholder="Mật khẩu">
                    `,
                    confirmButtonText: 'Đăng nhập',
                    preConfirm: () => {
                        const username = document.getElementById('username').value;
                        const password = document.getElementById('password').value;
                        if (!username || !password) {
                            Swal.showValidationMessage('Vui lòng nhập tài khoản và mật khẩu.');
                        }
                        return { username, password };
                    },
                    allowOutsideClick: false
                }).then((result) => {
                    if (result.isConfirmed) {
                        const { username, password } = result.value;
                        window.location.href = `/auth?username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`;
                    }
                });
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

    
@app.route('/auth')
def auth():
    username = request.args.get('username')
    password = request.args.get('password')
    
    query = "SELECT UserName FROM Admins WHERE UserName = ? AND PasswordHash = dbo.HashPassword(?)"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        user_name = result[0]
        session['username'] = user_name  
        return redirect(url_for('admin', username=user_name))
    else:
        error_msg = "Tài khoản hoặc mật khẩu không đúng"
        return render_template_string("<script>alert('{}'); window.location.href = '/';</script>".format(error_msg))
    

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/admin')
def admin():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session.get('username')

    # Hiển thị nút đăng xuất
    html = f"""
    <h2>Xin chào {username}</h2>
    <a href="{url_for('logout')}">Đăng xuất</a>
    <script>
        var confirmLogout = confirm("Bạn có muốn đăng xuất?");
        if (confirmLogout) {{
            window.location.href = "{url_for('logout')}";
        }}
    </script>
    """

    flight_info = []
    plane_info = []
    booking_info = []
    aircraft_info = []
    customer_info = []
    employee_info = []
    schedule_info = []
    assignment_info = []
    customer_list = []
    flight_list = []


    # Lấy danh sách chuyến bay từ cơ sở dữ liệu
    query = "SELECT MaChuyenBay, TenSanBayDi, TenSanBayDen, GioDi, GioDen FROM ChuyenBay"
    cursor.execute(query)
    flight_info = [row for row in cursor.fetchall()]

    query = "SELECT MAX(MaChuyenBay) FROM ChuyenBay"
    cursor.execute(query)
    max_flight_id = cursor.fetchone()[0]

    if max_flight_id:
        max_id_num = int(max_flight_id[2:])
        next_id_num = max_id_num + 1
        next_flight_id = f"CB{next_id_num:06d}"
    else:
        next_flight_id = "CB000001"

    # Lấy danh sách loại máy bay từ cơ sở dữ liệu
    query = "SELECT MaLoai, HangSanXuat FROM LoaiMayBay"
    cursor.execute(query)
    aircraft_info = [dict(MaLoai=row[0], HangSanXuat=row[1]) for row in cursor.fetchall()]

    query = "SELECT MAX (MaLoai) FROM LoaiMayBay"
    cursor.execute(query)
    max_plane_type_id = cursor.fetchone()[0]

    if max_plane_type_id:
         # Chuyển đổi max_plane_type_id thành chuỗi
        max_plane_type_id_str = str(max_plane_type_id)
        next_id_num = int(max_plane_type_id_str) + 1
        next_plane_type_id = f"{next_id_num:02d}"
    else:
        next_plane_type_id = "01"

    # Lấy danh sách thông tin đặt chỗ và thông tin chuyến bay
    query = """
    SELECT dc.MaKH, dc.NgayDi, cb.MaChuyenBay, cb.GioDi, cb.GioDen, cb.TenSanBayDi, cb.TenSanBayDen
    FROM DatCho dc
    JOIN ChuyenBay cb ON dc.MaChuyenBay = cb.MaChuyenBay
    """
    cursor.execute(query)
    booking_info = cursor.fetchall()

    # Lấy thông tin đầy đủ về khách hàng từ cơ sở dữ liệu
    query = "SELECT MaKH, SDT, HoDem, Ten, DiaChi FROM KhachHang"
    cursor.execute(query)
    customer_info = [row for row in cursor.fetchall()]

    query = "SELECT MAX(MaKH) FROM KhachHang"
    cursor.execute(query)
    max_customer_id = cursor.fetchone()[0]

    if max_customer_id:
        # Lấy phần số từ ký tự thứ 3 của max_customer_id
        max_id_num = int(max_customer_id[2:])
        next_id_num = max_id_num + 1
        next_customer_id = f"KH{next_id_num:06d}"
    else:
        next_customer_id = "KH000001"

    # Lấy danh sách máy bay từ cơ sở dữ liệu
    query = "SELECT SoHieu, MayBay.MaLoai, SoGheNgoi FROM MayBay JOIN LoaiMayBay ON MayBay.MaLoai = LoaiMayBay.MaLoai"
    cursor.execute(query)
    plane_info = [dict(SoHieu=row[0], MaLoai=row[1], SoGheNgoi=row[2]) for row in cursor.fetchall()]

    # Lấy thông tin đầy đủ về nhân viên từ cơ sở dữ liệu
    query = "SELECT MaNV, HoDem, Ten, SDT, DiaChi, Luong, LoaiNV FROM NhanVien"
    cursor.execute(query)
    employee_info = [row for row in cursor.fetchall()]

    query = "SELECT MAX(MaNV) FROM NhanVien"
    cursor.execute(query)
    max_employee_id = cursor.fetchone()[0]

    if max_employee_id:
        max_id_num = int(max_employee_id[2:])
        next_id_num = max_id_num + 1
        next_employee_id = f"NV{next_id_num:06d}"
    else:
        next_employee_id = "NV000001"

    # Lấy thông tin lịch bay từ cơ sở dữ liệu
    query = "SELECT * FROM LichBay"
    cursor.execute(query)
    schedule_rows = cursor.fetchall()

    # Lấy thông tin phân công từ cơ sở dữ liệu
    query = "SELECT KhachHang.MaKH, DatCho.NgayDi, DatCho.MaChuyenBay FROM DatCho JOIN KhachHang ON DatCho.MaKH = KhachHang.MaKH"
    cursor.execute(query)
    assignment_info = [row for row in cursor.fetchall()]

    # Thống kê số lượng
    stats = {
        'khach_hang': cursor.execute("SELECT COUNT(*) FROM KhachHang").fetchone()[0],
        'nhan_vien': cursor.execute("SELECT COUNT(*) FROM NhanVien").fetchone()[0],
        'loai_may_bay': cursor.execute("SELECT COUNT(*) FROM LoaiMayBay").fetchone()[0],
        'may_bay': cursor.execute("SELECT COUNT(*) FROM MayBay").fetchone()[0],
        'chuyen_bay': cursor.execute("SELECT COUNT(*) FROM ChuyenBay").fetchone()[0],
        'lich_bay': cursor.execute("SELECT COUNT(*) FROM LichBay").fetchone()[0],
        'dat_cho': cursor.execute("SELECT COUNT(*) FROM DatCho").fetchone()[0],
        'phan_cong': cursor.execute("SELECT COUNT(*) FROM PhanCong").fetchone()[0]
    }

    # API loai_may_bay_stats
    cursor.execute("SELECT HangSanXuat, COUNT(*) FROM LoaiMayBay GROUP BY HangSanXuat")
    loai_may_bay_stats = cursor.fetchall()
    stats['loai_may_bay_stats'] = {
        'labels': [s[0] for s in loai_may_bay_stats],
        'data': [s[1] for s in loai_may_bay_stats]
    }

    # API top_chuyen_bay
    query = """
    SELECT TOP 5 ChuyenBay.MaChuyenBay, ChuyenBay.TenSanBayDi, ChuyenBay.TenSanBayDen, COUNT(DatCho.MaKH) as total_bookings
    FROM ChuyenBay 
    JOIN LichBay ON LichBay.MaChuyenBay = ChuyenBay.MaChuyenBay
    JOIN DatCho ON DatCho.MaChuyenBay = LichBay.MaChuyenBay AND DatCho.NgayDi = LichBay.NgayDi
    GROUP BY ChuyenBay.MaChuyenBay, ChuyenBay.TenSanBayDi, ChuyenBay.TenSanBayDen
    ORDER BY total_bookings DESC
    """
    cursor.execute(query)
    top_flights = cursor.fetchall()
    stats['top_chuyen_bay'] = {
        'labels': [f"{f[0]} ({f[1]} -> {f[2]})" for f in top_flights],
        'data': [f[3] for f in top_flights]
    }

    # API nhan_vien_theo_loai
    cursor.execute("SELECT LoaiNV, COUNT(*) FROM NhanVien GROUP BY LoaiNV")
    nhan_vien_stats = cursor.fetchall()
    stats['nhan_vien_theo_loai'] = {
        'labels': [s[0] for s in nhan_vien_stats],
        'data': [s[1] for s in nhan_vien_stats]
    }

    return render_template('admin.html',
                           username=username,
                           flight_info=flight_info,
                           plane_info=plane_info,
                           booking_info=booking_info,
                           aircraft_info=aircraft_info,
                           customer_info=customer_info,
                           employee_info=employee_info,
                           schedule_info=schedule_rows,
                           assignment_info=assignment_info,
                           customer_list=customer_list,
                           flight_list=flight_list,
                           next_customer_id=next_customer_id,
                           next_employee_id=next_employee_id,
                           next_plane_type_id=next_plane_type_id,
                           next_flight_id=next_flight_id,
                           stats= stats)


@app.route('/them_cb', methods=['POST'])
def them_cb():
    flight_id = request.form['flight-id']
    departure_airport = request.form['departure-airport']
    arrival_airport = request.form['arrival-airport']
    departure_time = datetime.strptime(request.form['departure-time'], "%Y-%m-%dT%H:%M")
    arrival_time = datetime.strptime(request.form['arrival-time'], "%Y-%m-%dT%H:%M")

    query = "INSERT INTO ChuyenBay (MaChuyenBay, TenSanBayDi, TenSanBayDen, GioDi, GioDen) VALUES (?, ?, ?, ?, ?)"
    values = (flight_id, departure_airport, arrival_airport, departure_time, arrival_time)
    cursor.execute(query, values)
    cnxn.commit()
    return redirect(url_for('admin'))

@app.route('/sua_cb', methods=['POST'])
def sua_cb():
    flight_id = request.form['flight-id']
    departure_airport = request.form['departure-airport']
    arrival_airport = request.form['arrival-airport']
    departure_time = datetime.strptime(request.form['departure-time'], "%Y-%m-%dT%H:%M")
    arrival_time = datetime.strptime(request.form['arrival-time'], "%Y-%m-%dT%H:%M")
    query = "UPDATE ChuyenBay SET TenSanBayDi = ?, TenSanBayDen = ?, GioDi = ?, GioDen = ? WHERE MaChuyenBay = ?"
    values = (departure_airport, arrival_airport, departure_time, arrival_time, flight_id)
    cursor.execute(query, values)
    cnxn.commit()
    return redirect(url_for('admin'))

@app.route('/xoa_cb/<flight_id>', methods=['POST'])
def xoa_cb(flight_id):
    query = "DELETE FROM ChuyenBay WHERE MaChuyenBay = ?"
    cursor.execute(query, (flight_id,))
    cnxn.commit()
    return redirect(url_for('admin'))

### Các hàm xử lý cho quản lý LOẠI MÁY BAY

@app.route('/them_loai_mb', methods=['POST'])
def them_loai_mb():
    plane_type_id = request.form['plane-type-id']
    manufacturer = request.form['manufacturer']
    query = "INSERT INTO LoaiMayBay (MaLoai, HangSanXuat) VALUES (?, ?)"
    values = (plane_type_id, manufacturer)
    cursor.execute(query, values)
    cnxn.commit()
    return redirect(url_for('admin', section='aircraft-types'))

@app.route('/sua_loai_mb', methods=['POST'])
def sua_loai_mb():
    plane_type_id = request.form['plane-type-id']
    manufacturer = request.form['manufacturer']
    query = "UPDATE LoaiMayBay SET HangSanXuat = ? WHERE MaLoai = ?"
    values = (manufacturer, plane_type_id)
    cursor.execute(query, values)
    cnxn.commit()
    return redirect(url_for('admin', section='aircraft-types'))

@app.route('/xoa_loai_mb/<plane_type_id>', methods=['POST'])
def xoa_loai_mb(plane_type_id):
    query = "DELETE FROM LoaiMayBay WHERE MaLoai = ?"
    cursor.execute(query, (plane_type_id,))
    cnxn.commit()
    return redirect(url_for('admin', section='aircraft-types'))


### Các hàm xử lý cho quản lý ĐẶT CHỖ

# Hàm kiểm tra tồn tại khách hàng
def check_customer_exists(customer_id):
    query = "SELECT COUNT(*) FROM KhachHang WHERE MaKH = ?"
    cursor.execute(query, (customer_id,))
    count = cursor.fetchone()[0]
    return count > 0

# Hàm kiểm tra tồn tại chuyến bay
def check_flight_exists(flight_id):
    query = "SELECT COUNT(*) FROM ChuyenBay WHERE MaChuyenBay = ?"
    cursor.execute(query, (flight_id,))
    count = cursor.fetchone()[0]
    return count > 0

# Hàm kiểm tra tồn tại lịch bay
def check_flight_schedule_exists(flight_id, departure_date):
    query = "SELECT COUNT(*) FROM LichBay WHERE MaChuyenBay = ? AND NgayDi = ?"
    cursor.execute(query, (flight_id, departure_date))
    count = cursor.fetchone()[0]
    return count > 0

def get_flight_dates(flight_id):
    query = "SELECT NgayDi FROM LichBay WHERE MaChuyenBay = ?"
    cursor.execute(query, (flight_id,))
    result = cursor.fetchall()
    flight_dates = [row[0] for row in result]
    return flight_dates
    
def check_flight_schedule_exists(flight_id, departure_date):
    query = "SELECT COUNT(*) FROM LichBay WHERE MaChuyenBay = ? AND NgayDi = ?"
    cursor.execute(query, (flight_id, departure_date))
    return cursor.fetchone()[0] > 0


@app.route('/get_flight_details', methods=['GET'])
def get_flight_details():
    flight_id = request.args.get('flight_id')

    # Truy vấn SQL để lấy thông tin giờ đi và giờ đến từ bảng ChuyenBay
    query = """
    SELECT GioDi, GioDen
    FROM ChuyenBay
    WHERE MaChuyenBay = ?
    """
    cursor.execute(query, (flight_id,))
    flight_info = cursor.fetchone()

    if flight_info:
        departure_time = flight_info[0].isoformat()
        arrival_time = flight_info[1].isoformat()
        flight_details = {
            'departure_time': departure_time,
            'arrival_time': arrival_time
        }
        return jsonify(flight_details)
    else:
        return jsonify({'error': 'Mã chuyến bay không hợp lệ'}), 404

@app.route('/them_dat_cho', methods=['POST'])
def them_dat_cho():
    customer_id = request.form['customer-id']
    flight_id = request.form['flight-id']

    # Kiểm tra xem MaKH có tồn tại trong bảng KhachHang hay không
    if not check_customer_exists(customer_id):
        error_message = "Mã khách hàng không hợp lệ. Vui lòng nhập lại."
        return render_template('admin.html', error_message=error_message)

    # Kiểm tra xem MaChuyenBay có tồn tại trong bảng ChuyenBay hay không
    if not check_flight_exists(flight_id):
        error_message = "Mã chuyến bay không hợp lệ. Vui lòng nhập lại."
        return render_template('admin.html', error_message=error_message)

    # Lấy thông tin GioDi và GioDen từ bảng ChuyenBay
    query = "SELECT GioDi, GioDen FROM ChuyenBay WHERE MaChuyenBay = ?"
    cursor.execute(query, (flight_id,))
    flight_info = cursor.fetchone()

    if flight_info:
        giodi, gioden = flight_info

        # Thực hiện thêm thông tin đặt chỗ vào cơ sở dữ liệu
        query = "INSERT INTO DatCho (MaKH, MaChuyenBay, GioDi, GioDen) VALUES (?, ?, ?, ?)"
        values = (customer_id, flight_id, giodi, gioden)
        cursor.execute(query, values)
        cnxn.commit()
        return redirect(url_for('admin'))
    else:
        error_message = "Không tìm thấy thông tin chuyến bay. Vui lòng kiểm tra lại."
        return render_template('admin.html', error_message=error_message)

@app.route('/sua_dat_cho', methods=['POST'])
def sua_dat_cho():
    customer_id = request.form['customer-id']
    flight_id = request.form['flight-id']

    # Kiểm tra xem MaKH có tồn tại trong bảng KhachHang hay không
    if not check_customer_exists(customer_id):
        error_message = "Mã khách hàng không hợp lệ. Vui lòng nhập lại."
        return render_template('admin.html', error_message=error_message)

    # Kiểm tra xem MaChuyenBay có tồn tại trong bảng ChuyenBay hay không
    if not check_flight_exists(flight_id):
        error_message = "Mã chuyến bay không hợp lệ. Vui lòng nhập lại."
        return render_template('admin.html', error_message=error_message)

    # Lấy thông tin GioDi và GioDen từ bảng ChuyenBay
    query = "SELECT GioDi, GioDen FROM ChuyenBay WHERE MaChuyenBay = ?"
    cursor.execute(query, (flight_id,))
    flight_info = cursor.fetchone()

    if flight_info:
        giodi, gioden = flight_info

        query = "UPDATE DatCho SET MaChuyenBay = ?, GioDi = ?, GioDen = ? WHERE MaKH = ?"
        values = (flight_id, giodi, gioden, customer_id)
        cursor.execute(query, values)
        cnxn.commit()
        return redirect(url_for('admin'))
    else:
        error_message = "Không tìm thấy thông tin chuyến bay. Vui lòng kiểm tra lại."
        return render_template('admin.html', error_message=error_message)

@app.route('/xoa_dat_cho', methods=['POST'])
def xoa_dat_cho():
    customer_id = request.form['customer-id']
    flight_id = request.form['flight-id']
    departure_datetime = request.form['departure-datetime']

    # Thực hiện xóa thông tin đặt chỗ từ cơ sở dữ liệu
    query = "DELETE FROM DatCho WHERE MaKH = ? AND MaChuyenBay = ? AND GioDi = ?"
    values = (customer_id, flight_id, departure_datetime)
    cursor.execute(query, values)
    cnxn.commit()

    return redirect(url_for('admin'))

### Các hàm xử lý cho quản lý MÁY BAY

@app.route('/them_mb', methods=['POST'])
def them_mb():
    plane_id = request.form['plane-id']
    plane_type_id = request.form['plane-type-id']
    seat_quantity = request.form['seat-quantity']

    query = "INSERT INTO MayBay (SoHieu, MaLoai, SoGheNgoi) VALUES (?, ?, ?)"
    values = (plane_id, plane_type_id, seat_quantity)
    cursor.execute(query, values)
    cnxn.commit()
    return redirect(url_for('admin'))

@app.route('/sua_mb', methods=['POST'])
def sua_mb():
    plane_id = request.form['plane-id']
    plane_type_id = request.form['plane-type-id']
    seat_quantity = request.form['seat-quantity']

    query = "UPDATE MayBay SET MaLoai = ?, SoGheNgoi = ? WHERE SoHieu = ?"
    values = (plane_type_id, seat_quantity, plane_id)
    cursor.execute(query, values)
    cnxn.commit()
    return redirect(url_for('admin'))

@app.route('/xoa_mb/<plane_id>', methods=['POST'])
def xoa_mb(plane_id):
    query = "DELETE FROM MayBay WHERE SoHieu = ?"
    cursor.execute(query, (plane_id,))
    cnxn.commit()
    return redirect(url_for('admin'))

### Các hàm xử lý cho quản lý KHÁCH HÀNG

@app.route('/them_kh', methods=['POST'])
def them_kh():
    customer_id = request.form['customer-id']
    customer_phone = request.form['customer-phone']
    customer_last_name = request.form['customer-last-name']
    customer_first_name = request.form['customer-first-name']
    customer_address = request.form['customer-address']
    query = "INSERT INTO KhachHang (MaKH, SDT, HoDem, Ten, DiaChi) VALUES (?, ?, ?, ?, ?)"
    values = (customer_id, customer_phone, customer_last_name, customer_first_name, customer_address)
    cursor.execute(query, values)
    cnxn.commit()
    return redirect(url_for('admin'))

@app.route('/sua_kh', methods=['POST'])
def sua_kh():
    customer_id = request.form['customer-id']
    customer_phone = request.form['customer-phone']
    customer_last_name = request.form['customer-last-name']
    customer_first_name = request.form['customer-first-name']
    customer_address = request.form['customer-address']
    query = "UPDATE KhachHang SET SDT = ?, HoDem = ?, Ten = ?, DiaChi = ? WHERE MaKH = ?"
    values = (customer_phone, customer_last_name, customer_first_name, customer_address, customer_id)
    cursor.execute(query, values)
    cnxn.commit()
    return redirect(url_for('admin'))

@app.route('/xoa_kh/<customer_id>', methods=['POST'])
def xoa_kh(customer_id):
    query = "DELETE FROM KhachHang WHERE MaKH = ?"
    cursor.execute(query, (customer_id,))
    cnxn.commit()
    return redirect(url_for('admin'))

### Các hàm xử lý cho quản lý NHÂN VIÊN


@app.route('/them_nv', methods=['POST'])
def them_nv():
    employee_id = request.form['employee-id']
    employee_last_name = request.form['employee-last-name']
    employee_first_name = request.form['employee-first-name']
    employee_phone = request.form['employee-phone']
    employee_address = request.form['employee-address']
    employee_salary = request.form['employee-salary']
    employee_type = request.form['employee-type']

    query = "INSERT INTO NhanVien (MaNV, HoDem, Ten, SDT, DiaChi, Luong, LoaiNV) VALUES (?, ?, ?, ?, ?, ?, ?)"
    values = (employee_id, employee_last_name, employee_first_name, employee_phone, employee_address, employee_salary, employee_type)
    cursor.execute(query, values)
    cnxn.commit()
    return redirect(url_for('admin'))

@app.route('/sua_nv/<employee_id>', methods=['POST'])
def sua_nv(employee_id):
    employee_last_name = request.form['employee-last-name']
    employee_first_name = request.form['employee-first-name']
    employee_phone = request.form['employee-phone']
    employee_address = request.form['employee-address']
    employee_salary = request.form['employee-salary']
    employee_type = request.form['employee-type']

    query = "UPDATE NhanVien SET HoDem = ?, Ten = ?, SDT = ?, DiaChi = ?, Luong = ?, LoaiNV = ? WHERE MaNV = ?"
    values = (employee_last_name, employee_first_name, employee_phone, employee_address, employee_salary, employee_type, employee_id)
    cursor.execute(query, values)
    cnxn.commit()
    return redirect(url_for('admin'))

@app.route('/xoa_nv/<employee_id>', methods=['POST'])
def xoa_nv(employee_id):
    query = "DELETE FROM NhanVien WHERE MaNV = ?"
    cursor.execute(query, (employee_id,))
    cnxn.commit()
    return redirect(url_for('admin')) 


### Các hàm xử lý cho quản lý LỊCH BAY


@app.route('/them_lich', methods=['POST'])
def them_lich():
    flight_id = request.form['flight-id']
    aircraft_id = request.form['aircraft-id']
    aircraft_type_id = request.form['aircraft-type-id']
    departure_date = request.form['departure-date']

    query = "INSERT INTO LichBay (NgayDi, MaChuyenBay, SoHieu, MaLoai) VALUES (?, ?, ?, ?)"
    values = (departure_date, flight_id, aircraft_id, aircraft_type_id)
    cursor.execute(query, values)
    cnxn.commit()
    return redirect(url_for('admin'))

@app.route('/sua_lich', methods=['POST'])
def sua_lich():
    schedule_id = request.form['schedule-id']
    flight_id = request.form['flight-id']
    aircraft_id = request.form['aircraft-id']
    aircraft_type_id = request.form['aircraft-type-id']
    departure_date = request.form['departure-date']

    query = "UPDATE LichBay SET MaChuyenBay = ?, SoHieu = ?, MaLoai = ?, NgayDi = ? WHERE MaChuyenBay = ?"
    values = (flight_id, aircraft_id, aircraft_type_id, departure_date, schedule_id)
    cursor.execute(query, values)
    cnxn.commit()
    return redirect(url_for('admin'))

@app.route('/xoa_lich', methods=['POST'])
def xoa_lich():
       flight_id = request.form['flight-id']
       aircraft_id = request.form['aircraft-id']  # Lấy giá trị từ form
       departure_date = request.form['departure-date'] 
       query = "DELETE FROM LichBay WHERE NgayDi = ? AND MaChuyenBay = ? AND SoHieu = ?"
       values = (departure_date, flight_id, aircraft_id)
       cursor.execute(query, values)
       cnxn.commit()
       return redirect(url_for('admin'))


### Các hàm xử lý cho quản lý PHÂN CÔNG
   

@app.route('/them_phan_cong', methods=['POST'])
def them_phan_cong():
    customer_id = request.form['customer-id']
    flight_id = request.form['schedule-id'] 

    # Lấy ngày đi từ danh sách chuyến bay (giả sử bạn có hàm lấy ngày đi)
    departure_date = get_departure_date(flight_id)

    query = "INSERT INTO DatCho (MaKH, NgayDi, MaChuyenBay) VALUES (?, ?, ?)"
    values = (customer_id, departure_date, flight_id)
    cursor.execute(query, values)  # Cung cấp đầy đủ 3 tham số
    conn.commit()

    return redirect(url_for('admin'))

@app.route('/sua_phan_cong/<customer_id>/<departure_date>/<flight_id>', methods=['GET', 'POST'])
def sua_phan_cong(customer_id, departure_date, flight_id):
         if request.method == 'GET':
             # Lấy thông tin phân công hiện tại để hiển thị trong form sửa
             query = "SELECT * FROM DatCho WHERE MaKH = ? AND NgayDi = ? AND MaChuyenBay = ?"
             cursor.execute(query, (customer_id, departure_date, flight_id))
             assignment_info = cursor.fetchone()
             if assignment_info is None:
                 return 'Phân công không tồn tại'  # Xử lý trường hợp phân công không tồn tại
 
             # Lấy danh sách khách hàng và chuyến bay để hiển thị trong form
             customer_info = get_customer_info()  # Hàm lấy danh sách khách hàng
             flight_info = get_flight_info()  # Hàm lấy danh sách chuyến bay
             return render_template('sua_phan_cong.html', assignment_info=assignment_info, customer_info=customer_info, flight_info=flight_info)
         elif request.method == 'POST':
             # Lấy dữ liệu từ form sửa
             new_customer_id = request.form['new-customer-id']
             new_departure_date = request.form['new-departure-date']
             new_flight_id = request.form['new-flight-id']
 
             # Cập nhật thông tin phân công trong database
             query = "UPDATE DatCho SET MaKH = ?, NgayDi = ?, MaChuyenBay = ? WHERE MaKH = ? AND NgayDi = ? AND MaChuyenBay = ?"
             values = (new_customer_id, new_departure_date, new_flight_id, customer_id, departure_date, flight_id)
             cursor.execute(query, values)
             conn.commit()
             return redirect(url_for('admin')) 

@app.route('/xoa_phan_cong/<customer_id>/<departure_date>/<flight_id>', methods=['POST'])
def xoa_phan_cong(customer_id, departure_date, flight_id):
    query = "DELETE FROM DatCho WHERE MaKH = ? AND NgayDi = ? AND MaChuyenBay = ?"
    cursor.execute(query, (customer_id, departure_date, flight_id))
    conn.commit()
    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(debug=True)