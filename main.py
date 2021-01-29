import pygame
from pygame.locals import *
import random
import time

class RandomNum:
    def __init__(self,w,hw):
        self.num=str(random.randint(0,9))
        self.x=random.randint(0,w-128)
        self.y=random.randint(0,hw-128)
    def changeNum(self,w,hw):
        self.num=str(random.randint(0,9))
        self.x=random.randint(0,w-128)
        self.y=random.randint(0,hw-128)
    def displayNum(self,screen):
        img=pygame.image.load(self.num+".png")
        screen.blit(img,(self.x,self.y))
    
class App:
    """Create a single-window app with multiple scenes."""

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        pygame.display.set_caption("Remember Everything")
        gameicon=pygame.image.load('book.png')
        pygame.display.set_icon(gameicon)
        self.start=0
        self.bg=Color('pink')
        self.screen = pygame.display.set_mode((1200, 630))
        self.x ,self.y=(1200,630)
        self.Num=RandomNum(self.x,self.y)
        self.num_arr=""
        self.printed_num=5
        self.counter_number=0
        self.running = True
        self.activeScene2=False
        self.activeScene3=False
        self.answer=[""]
        self.index=0
        self.score=0
        self.dk=2
        self.sn=0
        self.input=True
        self.send_button=pygame.Rect(self.x//2-140,500,280,110)
        self.button_color=(3,80,111)
        

    def run(self):
        """Run the main event loop."""
        
        self.Menu()
        play_again_button=Rect(self.x//2-250, self.y//2+85, 500, 200)
        play_again_color=(148, 87, 114)
        self.start=time.time()
        flag=False
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if self.activeScene2:
                    if event.type ==KEYDOWN:
                        if event.key==K_BACKSPACE :
                            self.answer[self.index]=self.answer[self.index][:-1]
   
                            
                        elif self.input and event.unicode>='0' and event.unicode<='9':
                            if len(self.answer[self.index])%25 == 0 and len(self.answer[self.index])!=0:
                                self.index+=1
                                self.answer.append("")
                            self.answer[self.index]+=event.unicode
                            
                    if event.type==pygame.MOUSEMOTION:
                        if self.send_button.collidepoint(event.pos):
                            self.button_color=(17,138,191)
                        else:
                            self.button_color=(3,80,111)
                    if (event.type==pygame.MOUSEBUTTONDOWN and self.send_button.collidepoint(event.pos)) or (event.type==pygame.KEYDOWN and (event.key==K_KP_ENTER or event.key==K_RETURN)):

                        if self.answer[self.index] == self.num_arr:
                            self.activeScene2=False
                            self.score+=1
                        else:
                            self.activeScene3=True
                            
                        self.answer.clear()
                        self.answer=[""]
                        self.index=0
                        self.input=True
                        self.num_arr=""
                        self.start=time.time()
                        self.dk=2
                        self.sn=0
                        
                            
                            
                            
                        
                if self.activeScene3 and flag:
                    if event.type==pygame.MOUSEMOTION:
                        if play_again_button.collidepoint(event.pos):
                            play_again_color=(60, 66, 82)
                        else:
                            play_again_color=(148, 87, 114)
                    if event.type==pygame.MOUSEBUTTONDOWN and  play_again_button.collidepoint(event.pos):
                        self.activeScene3=False
                        self.activeScene2=False
                        self.counter_number=0
                        self.printed_num=5
                        self.start=time.time() 
                        flag=False
                        self.score=0
                            
            img=pygame.image.load("denme.png")
            self.screen.blit(img,(0,0))                   
                
            if self.activeScene3:
                self.displayScene3(play_again_color,play_again_button)
                flag=True 
            elif self.activeScene2:
                self.displayScene2()
                self.activeScene2=True
            elif self.isScene1():
                self.displayScene1()
                
            
            font=pygame.font.Font(None,50)
            surface=font.render("SCORE : "+ str(self.score),True,(255,255,255))
            self.screen.blit(surface,(10,10))
            
            pygame.display.update()

        pygame.quit()
      
    def displayScene1(self):
        # img=pygame.image.load("denme.png")
        # self.screen.blit(img,(0,0))
        self.Num.displayNum(self.screen)
        if time.time()-self.start>1 : #İMPORTANT 
            self.start=time.time()
            self.counter_number+=1
            self.num_arr+=self.Num.num                
            self.Num.changeNum(self.x,self.y)
            
    def displayScene2(self):
        # rect = Rect(0, self.y//2-150, 1200, 300)
        # pygame.draw.rect(self.screen, (0,0,0), rect)
        font=pygame.font.Font(None,100)
        a=0
        
        leng=0
        for answers in self.answer:
            leng+=len(answers)
        if leng ==len(self.num_arr):
            self.input=False
        else:
            self.input=True
           
           
               
        for answers in self.answer:
            surface=font.render(answers,True,(255,255,255))
            rect = Rect(0, self.y//2-150+a, 1200, 100)
            pygame.draw.rect(self.screen,(102, 160, 171), rect)
            self.screen.blit(surface,((self.x//2)-(len(answers))*19,self.y//2+a-150+25))
            a+=100
        
        font_time=pygame.font.Font(None,60)
        surface_font=font_time.render("TIME: "+ str(self.dk).zfill(2)+ ':' + str(self.sn).zfill(2),True,(148, 87, 114))
        self.screen.blit(surface_font,(950,15))
        send_font=pygame.font.Font(None,125)
        send_sur=send_font.render("SEND",True,(255,255,255))

        pygame.draw.rect(self.screen,self.button_color,self.send_button)
        self.screen.blit(send_sur,(self.x//2-125+10,500+15))
        
        
        
        
        if self.dk==0 and self.sn==0:
            self.activeScene3=True
            self.dk=2
            self.sn=0
        
        
        if time.time()-self.start>1 : #İMPORTANT 
            self.start=time.time()
            self.Clock()
            
        
        
    def displayScene3(self,play_again_color,play_again_button):
        # self.screen.fill(Color('purple'))
        font=pygame.font.Font(None,250)
        surface=font.render("GAME  OVER",True,(255,255,255))
        self.screen.blit(surface,(70,100)) 
        play_again_font=pygame.font.Font(None,100)
        play_surface=play_again_font.render("PLAY AGAİN",True,(255,255,255)) 
        pygame.draw.rect(self.screen, play_again_color, play_again_button)
        self.screen.blit(play_surface,(self.x//2-250+45, self.y//2+85+60)) 
        
    def isScene1(self):
        if self.printed_num== self.counter_number:
            self.counter_number=0
            self.printed_num +=1
            self.activeScene2=True
            return False
        return True    

    def Clock(self):
        if self.sn-1<0:
            self.sn=59
            self.dk-=1
        else:
            self.sn-=1

    def Menu(self):
        run=True
        start_color=(59, 98, 132)
        start_button=pygame.Rect(self.x//2-250,400,500,170)
        while run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False 
                    pygame.quit() 
                if event.type==pygame.MOUSEMOTION:
                    if start_button.collidepoint(event.pos):
                        start_color=(3,80,111)
                    else:
                        start_color=(59, 98, 132)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(event.pos):
                        run=False
                        
            head_img=pygame.image.load('back.png')
            self.screen.blit(head_img,(0,0))
            
            
            pygame.draw.rect(self.screen,start_color,start_button)
            
            send_font=pygame.font.Font(None,125)
            send_sur=send_font.render("START",True,(255,255,255))
            self.screen.blit(send_sur,(self.x//2-250+110,400+50))
            pygame.display.update()


if __name__ == '__main__':
    app=App()
    app.run()