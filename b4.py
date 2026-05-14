class Sach:
    def __init__(self, ma_sach, ten_sach, tac_gia):
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
        self.trang_thai = "Sẵn sàng"

    def hien_thi(self):
        print(f"Mã sách: {self.ma_sach}")
        print(f"Tên sách: {self.ten_sach}")
        print(f"Tác giả: {self.tac_gia}")
        print(f"Trạng thái: {self.trang_thai}")
        print("-" * 40)