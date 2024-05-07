import gymnasium as gym
import numpy #moze do generowania seeda?
import zaba_agent

def capture_screen(env):
    screen = env.render()

    #screen_array = jakiś sposób na użycie tego obrazu
    #do stworzenia array z obrazu (może z pomocą numpy)

def run():
    env = gym.make("ALE/Frogger-v5", render_mode="human", obs_type="rgb")
    #render_module: human, rgb_array, ansi, rgb_array_list, ansi_list 
    print(env.observation_space)
    state = env.reset()
    print(state)
    terminated = False
    truncated = False
    # kolor ramki: [82, 126, 45]
    # kolor żaby: [110, 156, 66]
    # kolory aut: fioletowe [164, 89, 208], różowe [198, 89, 179], zielone [82, 126, 45], 
    # pomarańczowe [195, 144, 61], białe [236,136,136]
    # kolory liści: brązowe [144, 72, 17], niebieskie [66, 114, 194]
    # kolory kłód: [105, 105, 15]

    # 13 wysokosc
    # 8 + 1 + 8 = 19 szerokosc
    i = 0
    zabcia = zaba_agent.zaba_agent()
    while(not terminated and not truncated): #na potrzeby testu, jedna zaba do smierci lub znudzenia;)
        capture_screen(env)
        i+=1
        if i % 6 <= 3:
            action = zabcia.pobierz_akcje(env ,state[0])
        else:
            #konieczne, poniewaz symulujemy przyciski - jesli akcja sie powtorzy zostanie wykonanana tylko raz 
            #mogloby to zaburzyc proces uczenia sie imo
            action = 0
        new_state, reward, terminated, truncated, _ = env.step(action)
        state = new_state
 

    env.close()

if __name__ == '__main__':
    run()