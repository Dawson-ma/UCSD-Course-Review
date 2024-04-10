# Instruction
編輯團隊的編輯指南  
如果你希望透過 Pull Request 來貢獻也歡迎參照[模板](/Template/README.md)撰寫評論喔！

## Steps
### 自動更新
Auto-Generate .md檔
1. 將[專案](https://github.com/Dawson-ma/UCSD-Course-Review/tree/main) pull 到本地端
2. 將[表單](https://docs.google.com/spreadsheets/d/1EvdOwx-ZwcU8SWFJwOivjJcNdeiZMCG_Az6764Enf8U/edit?usp=sharing)下載並放到剛剛 pull 下來專案中```./raw``` 資料夾中並取名```UCSDCourseReview.csv```
3. 開啟 Terminal 並到[```./AutoGenerate```](https://github.com/Dawson-ma/UCSD-Course-Review/tree/main/AutoGenerate)
4. 執行 ```AutoGenerate.py```
5. 該程式會自動產生所有相關資料夾、 README.md 與 SUMMARY.md。(課程科系碼與課號如包含"/"將無法自動生成，需手動更新，建議是直接在表單中修改好。如有人填CSE158/258，將其分開成CSE158與CSE258兩個獨立回覆但內容一樣）
6. 將檔案剪下並複製到根目錄 (替換掉原本的檔案)
7. git add .
8. git commit -m update
9. git push origin main

### 手動更新
#### 要更新的課程已經有所屬.md檔 (假設要更新ECE143，但ECE/ECE100-199已經有ECE143.md)
1. 點開該.md檔
2. 點擊右上角編輯
3. 根據 Template 資料夾下的[模板](/Template/README.md)撰寫評論
4. 完成後右上角 Commit changes...
5. 彈出一個視窗後按右下角 Commit changes
6. 等待約3至5分鐘，就可以在[這裡](https://dawson-ma.github.io/UCSD-Course-Review/)看到更改成功

#### 要更新的課程沒有所屬.md檔 (假設要更新ECE201，但ECE/ECE200+下並沒有ECE201.md)
1. 到想要新增評價的課程資料夾下 (如ECE200+)
2. 按右上角 Add file -> Create new file
3. 取名為 科系課號.md (如ECE201.md)
3. 根據 Template 資料夾下的[模板](/Template/README.md)撰寫評論
4. 完成後右上角 Commit changes...
5. 彈出一個視窗後按右下角 Commit changes
6. 到該層資料夾 README.md 檔 (如到ECE200+/README.md)
7. 點擊右上角編輯
8. 將```* [科系 課號 課名](/科系/科系課號分類/科系課號.md)``` 放至適當位置 (如將```* [ECE 285 Introduction to Visual Learning](/ECE/ECE200+/ECE285VL.md)``` 放到檔案最下面)
9. 完成後右上角 Commit changes...
10. 彈出一個視窗後按右下角 Commit changes
11. 到該科系資料夾 README.md 檔 (如到ECE/README.md)
12. 將步驟8所打的資訊放到適合位置
13. 完成後右上角 Commit changes...
14. 彈出一個視窗後按右下角 Commit changes
15. 到主頁[SUMMARY.md](/SUMMARY.md)
16. 將步驟8所打的資訊放到適合位置
17. 完成後右上角 Commit changes...
18. 彈出一個視窗後按右下角 Commit changes
19. 等待約3至5分鐘，就可以在[這裡](https://dawson-ma.github.io/UCSD-Course-Review/)看到更改成功

## Troubleshooting
歡迎大家將遇到的問題與解決方法寫在這裡，以後遇到相同的問題能夠更快速解決！  
可以在[這裡](https://github.com/Dawson-ma/UCSD-Course-Review/actions)看是否有成功Build和Deploy。

1. 更新後沒有正常顯示  
檢查是否照著上面步驟Commit，特別注意當自己創建.md檔需要在「科系分類資料夾」(e.g. ECE200+)、「科系」(e.g. ECE)、「[SUMMARY.md](/SUMMARY.md)」三個地方都更新才會正常顯示，且要注意縮排！
2. [Action](https://github.com/Dawson-ma/UCSD-Course-Review/actions)中的 Gitbook Action Build 一直失敗  
如果是刪除檔案，失敗是正常的。  
如果點進去看log發現找不到Token，可能是Token過期了，請跟Repository 擁有者聯絡更新Token。 (下次Token過期日:2025/4/8)
