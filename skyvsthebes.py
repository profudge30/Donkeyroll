import random

def main ():
    
    thebe3 = (264,46,47,54,70,49,80,129,75,130,53,76,51,129,53)
    thebe2 = (100,43,41,108,50,71,41,119,45,114,45,60,47,143,80)
    thebe1 = (64,76,66,168,49,49,42,68,42,76,47,162,74,88,76)

    sky3 = (120,112,40,64,49,42,179,51,48,59,78,44,58,91,60)
    sky2 = (44,168,47,50,75,72,61,37,193,49,73,84,47,43,109)
    sky1 = (62,120,72,92,145,93,42,62,40,192,102,76,91,102,50)


    ronde1 = (73,120,73,82,92,95,91,53,52,173,53,252,52,186,76)
    ronde2 = (102,140,55,92,76,80,54,48,145,93,56,197,72,52,62)
    ronde3 = (142,93,72,152,92,88,129,145,53,77,82,206,90,74,57)

    skyup1 = (73,138,68,84,51,67,45,50,100,156,105,72,45,55,48)
    skyup2 = (198,82,116,81,76,132,72,84,44,82,158,91,42,148,210)
    skyup3 = (117,72,148,144,94,88,54,115,158,157,72,59,108,69,70)


    runs = {thebe3: 'Thebe3', thebe2: 'Thebe2', thebe1: 'Thebe1', sky3: 'Sky3', sky2: 'Sky2', sky1: 'Sky1', ronde1: 'Ronde1', ronde2: 'Ronde2', ronde3: 'Ronde3',
            skyup1: 'Skyup1', skyup2: 'Skyup2', skyup3: 'Skyup3'}
    thbsavg=0
    skyavg=0
    skyavg2=0
    skyupavg=0
    rndavg=0
    print('Testing the damage difference between +9 Thebes Edoryu and +2 Edoryu of Blue Sky')
    print('\n')

    topdamage = []
    skyswing = []
    bonus = []
    for run in runs:
        max = 0
        counter=0
        for swing in run:
            counter+=1
            tmp=swing
            if (runs[run][0:2] == 'Th'):
                thbsavg+=swing
            elif (runs[run][0:2] == 'Ro'):
                rndavg+=swing
            elif (runs[run][3:4] == 'u'):
                print(runs[run][3:4])
                skyupavg+=swing
            else:
                #mltplr = random.uniform(1.0, 1.3)
                #swing *= mltplr
                skyavg+=swing
                '''if tmp > max:
                    max = tmp
                    maxbonus = mltplr
        if max > 0:
            bonus.append(maxbonus)
            skyswing.append(max * maxbonus)
            topdamage.append(max)
        print(f'{runs[run]} Swing Count: {counter}')
    print('\nHighest dammage in the set, including the multiplier:')
    for i, x in enumerate(topdamage):
        print(f'Sky trial {-i + 3}: Bonus - {int(skyswing[i])} , x{bonus[i]:.2f} || Without - {x}')'''

        

        
    print('\n')
    #print('Random 1-75% increase: ')
    print(f'Average damage of sky over 15 swings: {(skyavg) / 3:.2f} \nAverage damage of Ronde over 15 swings: {(rndavg) / 3:.2f}\nAverage damage of thebes over 15 swings: {(thbsavg) / 3:.2f}\nAverage damage of skyup over 15 swings: {(skyupavg) / 3:.2f}')
    print('\n')
    print(f'Average damage of sky per swing: {(skyavg) / 45:.2f} \nAverage damage of Ronde per swing: {(rndavg) / 45:.2f}\nAverage damage of thebes per swing: {(thbsavg) / 45:.2f}\nAverage damage of skyup per swing: {(skyupavg) / 45:.2f}')


    print(f'\nHighest damage in the amplified set: {int(max)}')
#mathematical thinking comp sci check and see ifyou are locked out of any of the content.

main()
