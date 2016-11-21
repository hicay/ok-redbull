import pyautogui, time

class Phone:

   def __init__(self, _pid, _x, _y):
      self.pid = _pid
      self.x = _x
      self.y = _y

   def displayPoints(self):
      print("X : ", self.x,  ", Y: ", self.y)


counter = 2
inputArray = []
def count():
    global counter
    global inputArray
    inputArray.append(input())
    print("array uzunlugu ", len(inputArray))
    if(len(inputArray) == counter) :
        pyautogui.moveTo(1080, 384)
        pyautogui.click()
        for idx in range(0, len(inputArray)):
            pyautogui.moveTo(phoneList[int(inputArray[idx])-1].x, phoneList[int(inputArray[idx])-1].y)
            pyautogui.click()
            print("Phone ", int(inputArray[idx]) , " Clicked")
        inputArray = []
        counter += 1
        pyautogui.moveTo(537, 367)
        pyautogui.click()


if __name__ == "__main__":
    phoneList = []
    phoneList.append(Phone(1, 948, 530))
    phoneList.append(Phone(2, 1072, 519))
    phoneList.append(Phone(3, 1215, 518))
    phoneList.append(Phone(4, 1403, 514))
    phoneList.append(Phone(5, 1493, 537))
    print(pyautogui.position())
    while True:
        count()


        # nums = input('phones : ')
        # pyautogui.moveTo(1080, 384)
        # pyautogui.click()
        # for idx in range(0, len(nums)):
        #     pyautogui.moveTo(phoneList[int(nums[idx])-1].x, phoneList[int(nums[idx])-1].y)
        #     pyautogui.click()
        #     print("Phone ", int(nums[idx]) , " Clicked")
        # pyautogui.moveTo(537, 367)
        # pyautogui.click()




        # pyautogui.moveTo(p1.x, p1.y)
        # time.sleep(2)
        # pyautogui.moveTo(p2.x, p2.y)
        # time.sleep(2)
        # pyautogui.moveTo(p3.x, p3.y)
        # time.sleep(2)
        # pyautogui.moveTo(p4.x, p4.y)
        # time.sleep(2)
        # pyautogui.moveTo(p5.x, p5.y)
        # time.sleep(2)

    #click(10,10)
