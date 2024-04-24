import gymnasium as gym
import numpy #moze do generowania seeda?
import zaba_agent

def run():
    env = gym.make("ALE/Frogger-v5", render_mode="human", obs_type="rgb")
    #render_module: human, rgb_array, ansi, rgb_array_list, ansi_list 
    print(env.observation_space)
    state = env.reset()
    print(state)
    terminated = False
    truncated = False
    #1 rzeka/lad 
    #5 rzeka
    #stop
    #pięć pasów
    #stop
    #wykorzystac same 0 w state[0] do okreslania dlugosci pól:3!
    i = 0;
    zabcia = zaba_agent.zaba_agent()
    while(not terminated and not truncated): #na potrzeby testu, jedna zaba do smierci lub znudzenia;)
        i+=1
        if i % 2 == 1:
            action = zabcia.pobierz_akcje(state[0])
        else:
            #konieczne, poniewaz symulujemy przyciski - jesli akcja sie powtorzy zostanie wykonanana tylko raz 
            #mogloby to zaburzyc proces uczenia sie imo
            action = 0
        new_state, reward, terminated, truncated, _ = env.step(action)
        state = new_state
    env.close()

if __name__ == '__main__':
    run()