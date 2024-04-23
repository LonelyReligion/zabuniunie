import gymnasium as gym
import numpy

def run():
    env = gym.make("ALE/Frogger-v5", render_mode="human")
    #render_module: human, rgb_array, ansi, rgb_array_list, ansi_list 
    print(env.observation_space)

    #low high shape(x, y i rgb:)) dtype
    #coś, x, y, rgb
    state = env.reset()
    terminated = False
    truncated = False
    #1 rzeka/lad
    #5 rzeka
    #stop
    #pięć pasów
    #stop
    i = 0;
    while(not terminated and not truncated): #na potrzeby testu, jedna zaba do smierci lub znudzenia;)
        i+=1
        if i % 2 == 1:
            action = 1 #env.action_space.sample()
        else:
            #konieczne, poniewaz symulujemy przyciski - jesli akcja sie powtorzy zostanie wykonanana tylko raz 
            #mogloby to zaburzyc proces uczenia sie imo
            action = 0
        new_state, reward, terminated, truncated, _ = env.step(action)
        state = new_state
        if terminated or truncated:
            state = env.reset()
    env.close()

if __name__ == '__main__':
    run()