import cv2
import sys
import pytesseract
import re
import glob
import os
import fpdf



if __name__ == '__main__':

  '''if len(sys.argv) < 2:
    print('Usage: python ocr_simple.py image.jpg')
    sys.exit(1)'''
  reload(sys)
  sys.setdefaultencoding('utf8')
  #vip=input("enter a video path")
  vidcap=cv2.VideoCapture("/Users/gouryrajsrinivas/Desktop/untitled folder/vid.mp4")
  try:
    if not os.path.exists('data1'):
          os.makedirs('data1')
  except OSError:
    print("error")
  def getFrame(sec):
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image=vidcap.read()
        if hasFrames:
              name='./data1/'+str(sec)+'.jpg'
              cv2.imwrite(name,image)
        return hasFrames
  sec=0
  frameRate=20.0
  success=getFrame(sec)
  while success:
    sec=sec+frameRate
    sec=round(sec,2)
    success=getFrame(sec)
  vidcap.release()
  cv2.destroyAllWindows()      
  
  
  s=[0,0]
  c=0
for imPath in glob.glob("/Users/gouryrajsrinivas/Desktop/untitled folder/data/*.jpg"):
      
   config = ('-l eng --oem 1 --psm 3')
   result=" "

  # Read image from disk
   im = cv2.imread(imPath, cv2.IMREAD_COLOR)
  
   im = im[60:500, 30:1200] 
   result=" "
  #cv2.imshow("cropped", crop_img)
  
  # Run tesseract OCR on image
   text = pytesseract.image_to_string(im, config=config)
   if c==0:
        
     temp=str(text)
     s[0]=temp
     c=c+1
     #print("vam")
     continue
   if c==1:
     temp2=str(text)
     s[1]=temp2
     #print("2")
   if c>1:
      s[0]=s[1]
      s[1]=str(text)
      #print("3")
   #for k in s[0].split("\n"):
   m1=re.sub(r"[^a-zA-Z0-9]"," ",s[0])
   m2=re.sub(r"[^a-zA-Z0-9]"," ",s[1])
   #print(m1)
   d1=m1.split(" ")
   d2=m2.split(" ")  
   t1=list(filter(None,d1))
   t2=list(filter(None,d2))
       #d1=g1.remove(" ")
   #for j in g2:
         
       #d2=g2.remove(" ") 
   #d1=re.findall("[a-z A-Z 0-9]{1,20}",s[0])
   #d2=re.findall("[a-z A-Z 0-9]{1,20}",s[1])
   #print(t1)
   #print(t2)
   l1=len(t1)
   l2=len(t2)
   v=c
   c=c+1
   if l1<l2:
        
         rs=" "
         result=" "
         for i in range(l1,l2):
               dat=t2[i]+" "
               rs+=dat
               #print(rs) 
         #print(rs)
         #print(s[1])        
         result=s[0]+rs
         res_lines=result.split("\n");
         #res_lines=unicode(res_lines,"utf-8")
         if v!=1:
                
              pdf = fpdf.FPDF(format='A4')
              pdf.add_page()
              pdf.set_font("Arial", size=12)
              for w in res_lines:
                 if type(w) == unicode:
                     w =  input.decode('utf-8')
                    # return input
            
                 pdf.cell(200, 10, txt=w, ln=1, align="C")
              pdf.output("simple_demo.pdf")
              print(result)
               
         
             #print(result)
             #print(v)
             #print("............................................................................")

   

            

  