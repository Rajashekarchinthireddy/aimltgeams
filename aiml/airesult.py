from numpy import random as rs
Team_leaders=['soumya(Team_lead-1)','Mona(Team_lead-2)','Abhiram(Team_lead-3)','shivani(Team_lead-4)','anirudh(Team_lead-5)','sahitha(Team_lead-6)','harshini(Team_lead-7)','vathsalya(Team_lead-8)','krishna teja(Team_lead-9)','laxman(Team_lead-10)','vivek(Team_lead-11)','varshitha(Team_lead-12)','srivalli(Team_lead-13)','spandana(Team_lead-14)']
Batch_1=['Akansha','Balaram','srija','p.sumanth','Akhil','sriya','vimala','bhaskar','harshitha','D,Gayathri','J.Sahiyhya','Syed Inayath','Shiza','Rajashekar']
Batch_2=['sai tharun','shiva','sai teja','sidharth','venky','saivenkat','anusha','akash','mukesh','praharsha','manorath','surya','dileep','narender',]
Batch_3=['vishnu','gathri','A.sumath','saketh','vaishnav','nouman','ravi teja','vishal','vinayak','nehal','jyotsna','sridhar','rahul','praneeth']
def batches_count():
    print("ALL BATCHES COUNT IS FOLLOWING:-")
    print("\n")
    print(" total Team leaders:-",len(Team_leaders))
    print("batch_1 total members:-",len(Batch_1))
    print("batch_2 total members:-",len(Batch_2))
    print("batch_3 total members:-",len(Batch_3))
def batch_detail():
    print("BATCHES ARE MADE ACCORDING TO CANDIDATES CGPA AND BACKLOGS")
    print("\n")
    print('TEAM-LEADERS BATCH  consist of following members:-')
    print("\n")
    for i in Team_leaders:
     print(i)
    print("\n")
    print('BATCH_1  consist of following members:-')
    print("\n")
    for i in Batch_1:
     print(i)
    print("\n")
    print('BATCH_2  consist of following members:-')
    print("\n")
    for i in Batch_2:
     print(i)
    print("\n")
    print('BATCH_3  consist of following members:-')
    print("\n")
    for i in Batch_3:
     print(i)
def making_teams():
  soumya_team=['SOUMYA(Team_lead-1)']
  mona_team=['MONA(Team_lead-1)']
  abhiram_team=['ABHIRAM(Team_lead-1)']
  shivani_team=['SHIVANI(Team_lead-1)']
  anirudh_team=['ANIRUDH(Team_lead-1)']
  sahithi_team=['SAHITHI(Team_lead-1)']
  harshini_team=['HARSHINI(Team_lead-1)']
  vathsalya_team=['VATHSALYA(Team_lead-1)']
  krishna_team=['KRISHNA TEJA(Team_lead-1)']
  laxman_team=['LAXMAN(Team_lead-1)']
  vivek_team=['VIVEK(Team_lead-1)']
  varshitha_team=['VARSHITHA(Team_lead-1)']
  srivalli_team=['SRIVALLI(Team_lead-1)']
  spandana_team=['SPANDANA(Team_lead-1)']
  Batch1copy=Batch_1
  Batch2copy=Batch_2
  Batch3copy=Batch_3
  leaders=['soumya_team','mona_team','abhiram_team','shivani_team','anirudh_team','sahithi_team','harshini_team','vathsalya_team','krishna_team','laxman_team','vivek_team','varshitha_team','srivalli_team','spandana_team']
  soumya_team=['soumya(Lead-1)']
  mona_team=['mona(Lead-2)']
  abhiram_team=['abhiram(Lead-3)']
  shivani_team=['shivani(Lead-4)']
  anirudh_team=['anirudh(Lead-5)']
  sahithi_team=['sahithi(Lead-6)']
  harshini_team=['harshini(Lead-7)']
  vathsalya_team=['vathsalya(Lead-8)']
  krishna_team=['krishna(Lead-9)']
  laxman_team=['laxman(Lead-10)']
  vivek_team=['vivek(Lead-11)']
  varshitha_team=['varshitha(Lead-12)']
  srivalli_team=['srivalli(Lead-13)']
  spandana_team=['spandana(Lead-14)']
  Heads=[soumya_team,mona_team,abhiram_team,shivani_team,anirudh_team,sahithi_team,harshini_team,vathsalya_team,krishna_team,laxman_team,vivek_team,varshitha_team,srivalli_team,spandana_team]
  Tails=['soumya_team','mona_team','abhiram_team','shivani_team','anirudh_team','sahithi_team','harshini_team','vathsalya_team','krishna_team','laxman_team','vivek_team','varshitha_team','srivalli_team','spandana_team']
  batch1copy=Batch_1
  batch2copy=Batch_2
  batch3copy=Batch_3
  for i in range(0,14):
    a=rs.choice(batch1copy)
    b=rs.choice(batch2copy)
    c=rs.choice(batch3copy)
    Heads[i].append(a)
    Heads[i].append(b)
    Heads[i].append(c)
    batch1copy.remove(a)
    batch2copy.remove(b)
    batch3copy.remove(c)
  for i in range(0,14):
    print('Team members of',Tails[i],'are:-')
    print('\n')
    for j in Heads[i]:
      print(j)
    print('\n')
while(1):
  print('MENU:-')
  print("1.to know batches count")
  print('2.to know batches details')
  print('3.to make teams')
  choice=int(input("enter your choice"))
  if(choice==1):
    batches_count()
  elif(choice==2):
    batch_detail()
  elif(choice==3):
    making_teams()
  else:
    print("enter valid choice")