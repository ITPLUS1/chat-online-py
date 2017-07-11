<h2>Phần 3:Mô hình triển khai ứng dụng và chuẩn lập trình:</h2>

<br>Người thực hiện: Nguyễn đình thái
<br>Ngày: 12/07/2017

<h3>Mô hình triển khai</h3>
Triển khai theo mô hình 2 lớp
Presentation Layers
Lớp này làm nhiệm vụ giao tiếp với người dùng cuối để thu thập dữ liệu và hiển thị kết quả/dữ liệu thông qua các thành phần trong giao diện người sử dụng.

Business Logic Layer

Đây là layer xử lý chính các dữ liệu trước khi được đưa lên hiển thị trên màn hình hoặc xử lý các dữ liệu.
Đây là nơi đê kiểm tra ràng buộc, các yêu cầu nghiệp vụ, tính toán, xử lý các yêu cầu và lựa chọn kết quả trả về cho Presentation Layers.

Cách vận hành của mô hình

Yêu cầu được xử lý tuần tự qua các layer như hình.
- Đầu tiên User giao tiếp với Presentation Layers (GUI) để gửi đi thông tin và yêu cầu. Tại layer này, các thông tin sẽ được kiểm tra, nếu OK chúng sẽ được chuyển xuống Business Logic Layer (BLL).

- Tại BLL, các thông tin sẽ được nhào nặn, tính toán theo đúng yêu cầu đã gửi, BLL sẽ gửi trả kết quả về GUI
<img src='/img/2_TIER.png'>


<h3>chuẩn lập trình</h3>
xem chi tiết tại <a href="http://csc.edu.vn/lap-trinh-di-dong/tin-tuc/Tin-dao-tao-LTDD/10-dieu-nen-biet-ve-phong-cach-viet-code-Python-Theo-tieu-chuan-PEP8-776
">đây </a>

