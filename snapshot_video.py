import cv2
import argparse
from tqdm import tqdm

"""----------------------------- Demo options -----------------------------"""
parser = argparse.ArgumentParser(description='Video to fewer images')
parser.add_argument('--vid', type=str, required=True,help='the video file name with path to be processed')
parser.add_argument('--jump', type=str,help='Take a snapshot of the vide at nth frame',default = 10)
args = parser.parse_args()


video_name = args.vid
jump = int(args.jump)
print(video_name)
cap = cv2.VideoCapture(video_name)

#may be can use this flag 
TotalFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))




counter = 0 #Start from frame 0 and traverse till end
pbar = tqdm(total = TotalFrames+ jump )
while(counter <= TotalFrames):
    #frame_no = (counter /(TotalFrames))
    #print("counter value initialized ",counter)
    cap.set(cv2.CAP_PROP_POS_FRAMES,counter)
    ret, frame = cap.read()
    
    if ret == True:
#        print('frame number being read ',cv2.CAP_PROP_POS_FRAMES)
#        print('True counter value ',counter)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#Cut the video extension to have the name of the video
        my_video_name = video_name.split(".")[0]
        cv2.imwrite(my_video_name+'_frame_'+str(counter)+'.jpg',gray)

    pbar.update(jump)
    counter =counter + jump
pbar.close()
#print(counter)
