HƯỚNG DẪN CÀI ĐẶT VÀ CHẠY CHƯƠNG TRÌNH “CHAT-CLIENT”
I.	CÀI ĐẶT PYTHON
Python là một ngôn ngữ lập trình được ra đời khoảng năm 1990, ngôn ngữ này dùng cơ chế tạo kiểu động và cấp phát bộ nhớ tự động, do vậy nó giống như ruby, Smalltalk, ... Python là một dự án mở do tổ chức PSF bao trọn gói.
Theo những người đã và đang làm việc trên ngôn ngữ này thì đây là một ngôn ngữ sáng sủa, gọn và có cấu trúc rõ ràng nên thuận tiện cho người mới học lập trình. Ban đầu ngôn ngữ này được phát triển trên hệ điều hành UNIX, nhưng dần về sau thì nó được lấn sang các hệ điều hành khác như LINUX, WINDOW.
Về cấu trúc cú pháp ngôn ngữ Python cũng có những điểm tựa như các ngôn ngữ khác như C, C++, PHP, nên nếu bạn đang là một lập trình viên phát triển ứng dụng trên các ngôn ngữ đó thì việc tìm hiểu Python hoàn toàn đơn giản.
Đề tài: “Chat Client” được xây dựng trên ngôn ngữ Python. Đề tài nhằm giải quyết việc liên lạc kết nối và chia sẻ dữ liệu giữa các máy tính và laptop trong cùng một mang LAN.
Máy của người sử dụng sẽ được kết nối với một máy chủ (Server). Từ máy chủ này sẽ kết nối các máy người dùng lại với nhau. Khi một trong số những người sử dụng có nhu cầu liên lạc với nhóm sẽ viết tin hoặc chia sẻ file sưc liệu. Nội dung sẽ được đưa lên máy Chủ, từ đây máy chủ sẽ đưa nội dung đi tất cả các máy người dùng khác đã được kết nối nhóm.

  
1- Download Python
Trước hết bạn cần truy cập vào địa chỉ dưới đây để download Python:
•	https://www.python.org/downloads/
Các bạn lưu ý: chọn đúng phiên bản 2.7.x. Ở đây mình sẽ chọn phiên bản 2.7.13
 <img src='/img2/cdpt1.png'>
<img src='/img2/cdpt2.png'>
Sau khi download bạn có 1 file:
 <img src='/img2/cdpt3.png'>
2- Cài đặt Python
Trước hết bạn cần giải nén file mà bạn vừa download được ở bước trên.
 


 
Mở "Terminal" và CD vào thư mục mà bạn có được sau khi giải nén ở bước trên.

 

Đăng nhập vào với quyền ADMIN:

	sudo su

 
Cài đặt:
	./configure
 
Lệnh "./configure" đã thực hiện xong.
 

Thực hiện tiếp lệnh "make" để tạo các file.

	make
 


 
OK, tới đây bạn đã cài đặt xong Python, bạn cần kiểm tra lại. Chạy lệnh "python" để làm việc với Python:
 
Thực thi một vài đoạn mã Python:
 
Như thế là chúng ta đã cài đặt xong Python phiên bản 2.7.12 để có thể phát triển và ứng dụng phần mềm: Chat client của chúng tôi. Chúc các bạn thành công!
 
II.	CÀI ĐẶT ỨNG DỤNG “CHAT-CLIENT”
-	Tải chương trìnhTrên Linux: https://github.com/TCU1/ChatClientServer_Python
Sau khi chương trình đã được tải về, đưa thư mục về Thư mục thích hợp. Ở đây chúng tôi lưu thư mục tại Desktop.

-	Khởi động:
ở cửa sổ terminal: cd /root/Desktop/ChatClientServer_Python
-	Cú pháp chạy server (Đối với máy làm Server): python server.py

 



-	Cú pháp chạy client (Đối với máy client): python client.py <server> <cổng>

 
 
-	Sau khi đã kết nối thành công, các bạn tiến hành nhập tên NickName mà bạn muốn sử dụng để nói chuyện với mọi người.

 

-	Lúc này các bạn đã có thể nói chuyện với mọi người rồi, chúc các bạn thành công.

 

Nếu có bất kỳ vấn đề gì thắc mắc hoặc cần hỗ trợ về ứng dụng “Chat-Client” vui lòng liên hệ: 
Trịnh Văn Bình email: binhboibac.dhttll@gmail.com hoặc kênh truyền thông của ứng dụng: https://www.facebook.com/itplussln/ 
Xin chân thành cảm ơn!

