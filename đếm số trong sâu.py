def demsotrongsau(s,n):
    length_s=len(s)#độ dài chuỗi s
    length_n=len(n)#độ dài chuỗi n
    cnt=0#biến đếm
    i=0#chỉ số bđ duyệt
    while i<=length_s-length_n+1:#chạy để y k vượt quá các ký tự trong sâu
        if s[i:length_n+i]==n:#kiểm tra trong chuỗi con từ i đến i + length_n
            cnt+=1# nếu tìm thấy thì tăng số đếm lên 1
            i+=length_n#tăng i lên length_n để bỏ qua chuỗi con vừa tìm thấy
        else:
            i+=1# k thấy thì tăng lên 1 tìm vị trí tiếp theo
    return cnt
for i in range(int(input())):
    a=input()
    n=input()
    print(demsotrongsau(a,n))