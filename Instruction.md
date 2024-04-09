# Instruction
編輯團隊的編輯指南  
如果你希望透過 Pull Request 來貢獻也歡迎參照[模板](/Template/README.md)撰寫評論喔！

## Steps
### 要更新的課程已經有所屬.md檔 (假設要更新ECE143，但ECE/ECE100-199已經有ECE143.md)
1. 點開該.md檔
2. 根據 Template 資料夾下的[模板](/Template/README.md)撰寫評論
3. 完成後右上角 Commit changes...
4. 彈出一個視窗後按右下角 Commit changes
5. 等待約3至5分鐘，就可以在[這裡](https://dawson-ma.github.io/UCSD-Course-Review/)看到更改成功

### 要更新的課程沒有所屬.md檔 (假設要更新ECE201，但ECE/ECE200+下並沒有ECE201.md)
1. 到想要新增評價的課程資料夾下 (如ECE200+)
2. 按右上角 Add file -> Create new file
3. 取名為 科系課號.md (如ECE201.md)
3. 根據 Template 資料夾下的[模板](/Template/README.md)撰寫評論
4. 完成後右上角 Commit changes...
5. 彈出一個視窗後按右下角 Commit changes
6. 到該層資料夾 README.md 檔 (如到ECE200+/README.md)
7. 點擊右上角編輯
8. 將```* [科系 課號 課名](/科系/科系課號分類/科系課號.md)``` 夾到適當位置 (如將```* [ECE 285 Introduction to Visual Learning](/ECE/ECE200+/ECE285VL.md)``` 放到檔案最下面)
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
