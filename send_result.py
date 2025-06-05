import shutil
import os
import time
import subprocess

# 복사할 파일 경로 (원본 파일)
source_file = '/workspace/NGPRDL/NGPDRL-gpu/logavg.txt'   # 원본 파일 경로로 변경하세요
# 복사한 파일이 저장될 경로 (저장소 내부 경로)
dest_file = './logavg.txt'  # 복사할 경로로 변경하세요
# git 저장소 경로
repo_dir = './'  # 로컬 저장소 디렉토리로 변경하세요

# 커밋 메시지 템플릿
commit_message = 'Auto commit: updated at ' + time.strftime('%Y-%m-%d %H:%M:%S')

while True:
    # 1️⃣ 파일 복사
    shutil.copy2(source_file, dest_file)
    print(f'파일 복사 완료: {source_file} -> {dest_file}')

    # 2️⃣ git add
    subprocess.run(['git', 'add', '.'], cwd=repo_dir)
    # 3️⃣ git commit
    subprocess.run(['git', 'commit', '-m', commit_message], cwd=repo_dir)
    # 4️⃣ git push
    subprocess.run(['git', 'push', 'origin', 'main'], cwd=repo_dir)
    print(f'커밋 및 푸쉬 완료: {commit_message}')

    # 1시간 대기
    time.sleep(3600)
