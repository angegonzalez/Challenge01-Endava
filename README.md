## Endava Challenge 01
For _development_ and _testing_ trainees

**Solution by**: Angel Mateo Gonzalez Bejarano

2023, Endava.

### Challenge statement
Endava  has  always  been  known  for  throwing  epic  parties  and  the  next  one  will  not  be  the exception.
For the next event a series of challenges are planned for all the guests, and there is  a  big  surprise, 
the  dance  floor  will  look  like  a  square  matrix!
For this  reason,  PDR  has designed a very interesting game called Longest
Endavans Line Dance which consists of the following rules: 

1. There can only be one Endavan for each position on the dance floor.

2. In this game, the ages of the Endavans are important, so PDR has designed a banner with this information,
   and this must be carried all the time.

3. The winners of the game will be those who manage to create the longest line dance, considering the following
   rules defined by PDR:
   
   1. No matter the age of the first person
   2. The next person must be one year younger or older
   3. The next person should be located to the right or down

I solved this challenge using a DFS approach and combine that with the DP approach to provide a better solution
in terms of time complexity.