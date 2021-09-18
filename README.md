- clone code về PC
- trong terminal cd đến thư mục mytest
- mở MySQL tạo một CSDL rỗng với tên :django,không cần tạo bất cứ bảng gì vì làm theo kiểu code first
có hai bảng là User được kế thừa từ User model của django,bảng Todo
NOTE : THÊM THÔNG TIN USER PASSWORD CỦA DATABASE VÀO TRONG FILE settings.py
- thực thi lệnh : python manage.py makemigrations sau đó gõ python manage.py migrate
- tạo một tài khoản super user vào trang admin để dễ dàng xem kết quả với lệnh : python manage.py createsuperuser
- deploy ở local host bằng lệnh :python manage.py runserver
Test các API ở POST MAN
API 1 : - nhập url : http://127.0.0.1:8000/register/ chọn method POST
        - ở phần body chọn kiểu dữ liệu JSON rồi nhập theo format :
           {
               "username":"",
               "email":"",
               "password":"",
               "re_password":""
           }
API 2 : - nhập url : http://127.0.0.1:8000/login/api/token/ ,chọn method POST
        - ở phần body chọn kiểu dữ liệu JSON rồi nhập theo format :
          {"username": "", "password": ""}
         kết quả sẽ trả về một chuỗi token để có thể xác thực các API ở các yêu cầu tiếp theo
API 3 : - nhập url : http://127.0.0.1:8000/addtodo/ , chọn method POST
        - vào Headers , thêm mục Authorization ở cột KEY,thêm vào VALUE : Bearer <chuỗi token nhận được khi login thành công>
        - ở phần body chọn kiểu dữ liệu JSON rồi nhập theo format :
          {"title":"",
            "description":"",
            "user_id":"",
            "date_complete":"",
            "status":""}
API 4 : - nhập url : http://127.0.0.1:8000/updatetodo/<id> ,chọn method PATCH với id = id của record cần update
        - cũng thêm Headers như API 3
        - ở phần body chọn kiểu dữ liệu JSON rồi nhập theo format :
            {"title":"",
            "description":"",
            "user_id":"",
            "date_complete":"",
            "status":""}
API 5 : - nhập url :http://127.0.0.1:8000/removetodo/<id> ,chọn method DELETE với id = id của record cần delete
        - thêm headers như trên

API 6 : - nhập url :http://127.0.0.1:8000/getalltodo/ chọn method GET
        - thêm Headers như các mục trên
API 7 : -nhập url :http://127.0.0.1:8000/getonetodo/<id> , chọn method GET với id = id của record cần lấy
        -  thêm Headers như các mục trên
API 8 : - http://127.0.0.1:8000/getalluser/ ,chọn method GET
          -  thêm Headers như các mục trên
API 9: không có hướng giải quyết
Đã băm mật khẩu!      