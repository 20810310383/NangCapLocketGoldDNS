import os
from dotenv import load_dotenv
load_dotenv()

# BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
# NEXTDNS_KEY = os.environ.get("NEXTDNS_KEY", "")

BOT_TOKEN   = os.getenv("BOT_TOKEN")
NEXTDNS_KEY = os.getenv("NEXTDNS_KEY")

TOKEN_SETS = [
    {
        "fetch_token": os.getenv("FETCH_TOKEN"),
        "app_transaction": os.getenv("APP_TRANSACTION"),
        "hash_params": "",
        "hash_headers": "",
        "is_sandbox": False,
    },
]

ADMIN_ID    = int(os.getenv("ADMIN_ID", 8373929944))

NUM_WORKERS = 2
DONATE_PHOTO = ""

E_LOADING = '<tg-emoji emoji-id="5350752364246606166">✍️</tg-emoji>'
E_LIMIT   = '<tg-emoji emoji-id="5424857974784925603">🚫</tg-emoji>'
E_SUCCESS = '<tg-emoji emoji-id="5260463209562776385">✅</tg-emoji>'
E_ERROR   = '<tg-emoji emoji-id="5318840353510408444">🔴</tg-emoji>'
E_TIP     = '<tg-emoji emoji-id="4968003407315993509">💡</tg-emoji>'
E_MENU    = '<tg-emoji emoji-id="5449601904147440135">👑</tg-emoji>'

E_USER    = '<tg-emoji emoji-id="5974048815789903111">👤</tg-emoji>'
E_ID      = '<tg-emoji emoji-id="5974526806995242353">🆔</tg-emoji>'
E_TAG     = '<tg-emoji emoji-id="5240228673738527951">🏷️</tg-emoji>'
E_STAT    = '<tg-emoji emoji-id="4967519884192777037">📊</tg-emoji>'
E_GLOBE   = '<tg-emoji emoji-id="5231489647946768652">🌐</tg-emoji>'
E_SOS     = '<tg-emoji emoji-id="6301027265899661025">🆘</tg-emoji>'
E_SHIELD  = '<tg-emoji emoji-id="5352888345972187597">🛡️</tg-emoji>'
E_CALENDAR = '<tg-emoji emoji-id="5413879192267805083">📅</tg-emoji>'
E_IOS     = '<tg-emoji emoji-id="5350556204500263431">🍏</tg-emoji>'
E_ANDROID = '<tg-emoji emoji-id="5303145396254563405">🤖</tg-emoji>'


DEFAULT_LANG = "VI"

TEXTS = {
   "VI": {
        "welcome": f"{E_SUCCESS} <b>HỆ THỐNG KÍCH HOẠT LOCKET GOLD</b>\n\nChào mừng bạn! Chúng tôi cung cấp giải pháp nâng cấp tài khoản Locket chuyên nghiệp và ổn định nhất hiện nay.",
        "menu_msg": f"{E_MENU} <b>BẢNG ĐIỀU KHIỂN DỊCH VỤ</b>\n\nVui lòng chọn các tính năng bên dưới để bắt đầu quy trình nâng cấp tài khoản của bạn.",
        "btn_input": "🔑 Nâng Cấp Gold Ngay",
        "btn_lang": "🌐 Đổi ngôn ngữ",
        "prompt_input": f"{E_LOADING} <b>YÊU CẦU CUNG CẤP:</b>\nVui lòng gửi <b>Username</b> hoặc <b>Link Locket</b> của bạn để hệ thống nhận diện mục tiêu:",
        "lang_select": "🌐 Vui lòng chọn ngôn ngữ hiển thị:",
        "lang_set": f"{E_SUCCESS} Đã thiết lập ngôn ngữ: Tiếng Việt",
        "help_msg": (
            f"<b>{E_MENU} HƯỚNG DẪN SỬ DỤNG:</b>\n\n"
            f"🚀 <b>Bắt đầu:</b> Nhấn 'Nâng Cấp Gold Ngay'\n"
            f"🆔 <b>Định danh:</b> Gửi ID hoặc Link Locket cá nhân.\n"
            f"⚡ <b>Xử lý:</b> Chờ hệ thống nạp gói cước (3-5 giây).\n"
            f"🛡️ <b>Bảo vệ:</b> Cài đặt DNS chống thu hồi (Bắt buộc).\n\n"
            f"<i>Nếu gặp sự cố, vui lòng liên hệ Admin để được hỗ trợ tức thì.</i>"
        ),
        "resolving": f"{E_LOADING} <b>Đang truy vấn ID người dùng từ Database...</b>",
        "not_found": f"{E_ERROR} <b>LỖI:</b> Tài khoản không tồn tại hoặc sai định dạng. Vui lòng thử lại!",
        "limit_reached": f"{E_LIMIT} <b>THÔNG BÁO:</b> Bạn đã dùng hết hạn mức miễn phí trong ngày (5/5).",
        "queue_almost": f"{E_LOADING} <b>SẮP ĐẾN LƯỢT:</b>\nHàng chờ đang xử lý, bạn ở vị trí số <b>2</b>. Vui lòng không thoát!",
        "admin_noti_sent": f"{E_SUCCESS} Thông báo hệ thống đã được gửi đi.",
        "admin_reset": f"{E_SUCCESS} Đã khôi phục lượt dùng cho User {{}}.",
        "admin_only": f"{E_ERROR} Bạn không có quyền truy cập lệnh này.",
        "checking_status": f"{E_LOADING} <b>Đang kiểm tra quyền lợi gói cước...</b>",
        "free_status": "Standard (Chưa Nâng Cấp)",
        "gold_active": f"{E_SUCCESS} <b>TRẠNG THÁI: GOLD MEMBER</b> (Hết hạn: {{}})",
        "user_info_title": f"{E_USER} <b>HỒ SƠ NGƯỜI DÙNG</b>",
        "btn_upgrade": "🚀 XÁC NHẬN NÂNG CẤP",
        "queued": f"{E_LOADING} <b>ĐÃ GHI DANH VÀO HÀNG CHỜ</b>\nĐối tượng: <code>{{0}}</code>\nThứ tự: <b>#{{1}}</b> (Ước tính: {{2}} lượt tiếp theo)...",
        "processing": (
            f"{E_LOADING} <b>⚡ KHỞI CHẠY TIẾN TRÌNH EXPLOIT...</b>\n"
            f"<pre>"
            f"[*] Target:  {{}}\n"
            f"[*] Method:  Cloud_Injection_v3.0\n"
            f"[>] Action:  Syncing Premium Receipt...\n"
            f"[>] Status:  Bypassing Apple Store Kit...\n"
            f"[?] Waiting: Finalizing Response..."
            f"</pre>"
        ),
        "success_title": f"{E_SUCCESS} <b>XÁC NHẬN: NÂNG CẤP THÀNH CÔNG!</b>",
        "generating_dns": f"{E_SHIELD} Đang khởi tạo cấu hình Anti-Revoke cá nhân...",
        "fail_title": f"{E_ERROR} <b>LỖI: Tiến trình bị gián đoạn</b>",
        "dns_msg": (
            f"{E_SHIELD} <b>BƯỚC QUAN TRỌNG ĐỂ DUY TRÌ GOLD</b>:\n\n"
            f"Để gói Gold <b>KHÔNG BỊ MẤT</b> khi thoát ứng dụng, bạn cần cài đặt Profile bảo vệ sau đây:\n\n"
            f"{E_IOS} <b>Dành cho iPhone</b>: <a href='{{}}'><b>[NHẤN VÀO ĐÂY ĐỂ CÀI]</b></a>\n"
            f"(Yêu cầu dùng <b>Safari</b> -> Cho phép -> Vào Cài đặt để duyệt Profile)\n\n"
            f"{E_ANDROID} <b>Dành cho Android</b>: <code>{{}}.dns.nextdns.io</code>\n"
            f"(Cài đặt → Mạng → Private DNS)\n\n"
            f"{E_TIP} <b>CẢNH BÁO:</b> Hệ thống sẽ không chịu trách nhiệm nếu bạn không cài DNS này!"
        )
    },
    "EN": {
        "welcome": f"{E_SUCCESS} <b>Locket Gold Activator</b>\n\nWelcome! Please select your language or use the menu below.",
        "menu_msg": f"{E_MENU} <b>Control Panel</b>\n\n👇 Click the button below to enter Username.",
        "btn_input": "🔑 Input Locket User",
        "btn_lang": "🌐 Change Language",
        "prompt_input": f"{E_LOADING} Please enter your <b>Username</b> or <b>Locket Link</b> in the reply below:",
        "lang_select": "🌐 Please select language:",
        "lang_set": f"{E_SUCCESS} Language set: English",
        "help_msg": (
            f"<b>{E_MENU} Commands:</b>\n\n"
            f"/start - Main Menu\n"
            f"/setlang - Change Language\n"
            f"/help - Show this help\n\n"
            f"<b>{E_TIP} How to use:</b>\n"
            f"1. Click '🔑 Input Locket User'\n"
            f"2. Enter Username or Link\n"
            f"3. Bot will activate Gold."
        ),
        "resolving": f"{E_LOADING} <b>Resolving UID...</b>",
        "not_found": f"{E_ERROR} User not found.",
        "limit_reached": f"{E_LIMIT} Daily limit reached (5/5).",
        "queue_almost": f"{E_LOADING} <b>Almost your turn!</b>\n<b>2 people</b> ahead of you. Get ready! 🚀",
        "admin_noti_sent": f"{E_SUCCESS} Notification sent to all users.",
        "admin_reset": f"{E_SUCCESS} Usage reset for user {{}}.",
        "admin_only": f"{E_ERROR} You don't have permission.",
        "checking_status": f"{E_LOADING} <b>Checking Entitlements...</b>",
        "free_status": "Free (Inactive)",
        "gold_active": f"{E_SUCCESS} <b>Gold Active</b> (Exp: {{}})",
        "user_info_title": f"{E_USER} <b>User Information</b>",
        "btn_upgrade": "🚀 ACTIVATE NOW",
        "queued": f"{E_LOADING} <b>Added to Queue</b>\nTarget: <code>{{0}}</code>\nPosition: <b>#{{1}}</b> ({{2}} people ahead)...",
        "processing": (
            f"{E_LOADING} <b>⚡ SYSTEM EXPLOIT RUNNING...</b>\n"
            f"<pre>"
            f"[*] Target:  {{}}\n"
            f"[*] Method:  RevenueCat_Bypass_v2\n"
            f"[>] Action:  Injecting Malicious Receipt\n"
            f"[>] Status:  Bypassing Validation...\n"
            f"[?] Waiting: Server Response..."
            f"</pre>"
        ),
        "success_title": f"{E_SUCCESS} <b>ACTIVATION SUCCESSFUL</b>",
        "generating_dns": f"{E_SHIELD} Generating Anti-Revoke DNS...",
        "fail_title": f"{E_ERROR} <b>Activation Failed</b>",
        "dns_msg": (
            f"{E_SHIELD} <b>IMPORTANT INSTRUCTIONS</b>:\n"
            f"1️⃣ Check Locket App for <b>Gold</b> status.\n"
            f"2️⃣ If active, <b>INSTALL DNS IMMEDIATELY</b> (within 45s):\n\n"
            f"{E_IOS} <b>iOS</b>: <a href='{{}}'>Click to Install</a>\n"
            f"(Open link in <b>Safari</b> -> Allow -> Install Profile)\n\n"
            f"{E_ANDROID} <b>Android</b>: <code>{{}}.dns.nextdns.io</code>\n"
            f"(Settings → Network → Private DNS)\n\n"
            f"{E_TIP} <b>Note</b>: DNS is required to keep Gold active!"
        )
    }
}

def T(key, lang=None):
    if not lang:
        lang = DEFAULT_LANG
    return TEXTS.get(lang, TEXTS["VI"]).get(key, key)
