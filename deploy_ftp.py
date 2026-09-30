import os
import sys
import ftplib

FTP_HOST = "82.25.121.163"
FTP_USER = "u384964548.2ndpaytech"
FTP_PASS = "57c2R*!Uk>A0"

def upload_directory(ftp, local_dir, remote_dir=""):
    print(f"📁 Syncing directory: {local_dir} -> {remote_dir or '/'}")
    for item in sorted(os.listdir(local_dir)):
        local_path = os.path.join(local_dir, item)
        remote_path = f"{remote_dir}/{item}" if remote_dir else item

        if os.path.isdir(local_path):
            try:
                ftp.mkd(remote_path)
                print(f"  + Created remote dir: {remote_path}")
            except ftplib.error_perm:
                pass # Already exists
            upload_directory(ftp, local_path, remote_path)
        else:
            print(f"  ↑ Uploading {remote_path} ({os.path.getsize(local_path):,} bytes)...", end="", flush=True)
            with open(local_path, "rb") as f:
                ftp.storbinary(f"STOR {remote_path}", f)
            print(" Done.")

def main():
    print("=" * 60)
    print("🚀 Connecting to Hostinger FTP (srv876 / 82.25.121.163)...")
    print("=" * 60)
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, 21, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.set_pasv(True)
    print(f"✅ Successfully logged in as {FTP_USER}!")

    local_dist = os.path.abspath("dist_production/public_html")
    if not os.path.exists(local_dist):
        print(f"❌ Error: {local_dist} does not exist!")
        sys.exit(1)

    upload_directory(ftp, local_dist)

    # Also upload the zip file as a backup
    zip_path = os.path.abspath("2ndpaytech-public_html.zip")
    if os.path.exists(zip_path):
        print(f"  ↑ Uploading 2ndpaytech-public_html.zip ({os.path.getsize(zip_path):,} bytes)...", end="", flush=True)
        with open(zip_path, "rb") as f:
            ftp.storbinary("STOR 2ndpaytech-public_html.zip", f)
        print(" Done.")

    ftp.quit()
    print("=" * 60)
    print("🎉 DEPLOYMENT COMPLETE!")
    print("=" * 60)

if __name__ == "__main__":
    main()
