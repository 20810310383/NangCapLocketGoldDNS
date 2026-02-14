# 🚀 Locket Gold Activator Bot (Professional Edition)

Hệ thống tự động kích hoạt Locket Gold chuyên nghiệp, tích hợp giải pháp chống thu hồi (Anti-Revoke) qua NextDNS API.

---

## 🛠️ Hướng Dẫn Cài Đặt

### Điều kiện cần thiết

- **Python 3.9+**
- **Telegram Bot Token**: Lấy từ [@BotFather](https://t.me/BotFather)
- **NextDNS API Key**: Lấy tại mục Account trên [my.nextdns.io](https://my.nextdns.io/account)

### Cài đặt nhanh (One-click Setup)

Chúng tôi cung cấp script tự động để khởi tạo môi trường ảo và cài đặt thư viện hỗ trợ.

```bash
# 1. Tải mã nguồn về máy
git clone [https://github.com/20810310383/NangCapLocketGoldDNS](https://github.com/20810310383/NangCapLocketGoldDNS)
cd NangCapLocketGoldDNS

# 2. Cấp quyền và chạy script cài đặt
chmod +x run.sh
./run.sh

# app/config.py

# 1. Thông tin định danh hệ thống
BOT_TOKEN   = "DIEN_TOKEN_BOT_CUA_BAN"
NEXTDNS_KEY = "DIEN_API_KEY_NEXTDNS"
ADMIN_ID    = 8373929944  # Thay bằng ID Telegram của bạn để làm Admin

# 2. Cấu hình Worker
# Đặt số lượng Worker bằng với số lượng Token Sets bạn có.
NUM_WORKERS = 2

# 3. Biên lai gốc (Gói tin bắt được từ máy đã mua Gold)
TOKEN_SETS = [
    {
        "fetch_token": "ey...",      # RevenueCat Fetch Token
        "app_transaction": "ey...",  # Apple Receipt Transaction
        "is_sandbox": False          # Luôn để False để chạy chính thức
    },
    # Bạn có thể thêm nhiều bộ token khác để tăng tốc độ xử lý...
]

```

Lệnh --- Mô tả chi tiết
/start --- Khởi động Bot và mở Menu điều khiển chính.
/setlang --- Thay đổi ngôn ngữ (Tiếng Việt 🇻🇳 / Tiếng Anh 🇺🇸).
/help --- Xem hướng dẫn sử dụng và cách cài đặt DNS.
Gửi trực tiếp,username,Gửi Username hoặc Link Locket để bắt đầu nâng cấp.
