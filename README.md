# Douyin Lite

Ứng dụng Windows nội bộ, chỉ gồm hai chức năng:

- Mở Chrome để đăng nhập Douyin và xuất `cookies.txt`.
- Tải một hoặc nhiều video Douyin theo link, hỗ trợ chất lượng cao nhất và H.264.

Không bao gồm Whisper, OpenAI, GPT hoặc các model AI.

## Tải bản Windows

File chạy sẵn nằm tại `dist/DouyinLite.exe`.

## Cách sử dụng

1. Mở `DouyinLite.exe`.
2. Bấm **Mở Chrome để đăng nhập**.
3. Đăng nhập hoặc xác minh trên Douyin.
4. Quay lại ứng dụng và bấm **Lưu cookie và đóng Chrome**.
5. Dán link Douyin, mỗi link một dòng, rồi bấm **TẢI VIDEO**.

Dữ liệu cá nhân được lưu cục bộ tại `Documents\DouyinLite` và không được đưa vào repository.

## Build

```powershell
python -m PyInstaller --noconfirm --clean DouyinLite.spec
```

Ứng dụng yêu cầu Windows và Google Chrome. File EXE là gói một file tạo bằng PyInstaller; đây không phải cơ chế chống dịch ngược tuyệt đối.
