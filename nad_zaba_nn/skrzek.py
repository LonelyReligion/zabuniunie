import gymnasium as gym
import numpy #moze do generowania seeda?
import siecneuronowa as zaba

def run():
    env = gym.make("ALE/Frogger-v5", render_mode="human", obs_type="rgb")
    #render_module: human, rgb_array, ansi, rgb_array_list, ansi_list 
    print(env.observation_space)
    obs, info = env.reset()
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

    siec = zaba.siec(dane_wejsciowe=obs.shape, dane_wyjsciowe = 5) #5 (od 0) to liczba akcji jakie moze wykonać zaba

    #trzeba jakoś ten model wytrenować
    #jakimi danymi? - zapytac prowadzacego 
    #czy można w takich sposób w tym programie użyć sieci neuronowej
    #jezeli tak to czy uzyc tensorflow czy pytorch
    #jakie dane wejsciowe dla sieci: czy całe obs czy wyjscie z szukajaut()
    #jak polaczyc ta siec neuronowa z algorytmem genetycznym
    #czy wyjscie z sieci neuronowej lepiej zeby bylo konkretną już akcją żaby czy prawdopodobienstwem
    #x_train_tf =
    #y_train_tf =
    #siec.train(x_train_tf, y_train_tf, epochs=10)

    while(not terminated and not truncated): #na potrzeby testu, jedna zaba do smierci lub znudzenia;)
        i+=1
        if i % 6 <= 3:
            #action = zabcia.pobierz_akcje(env, szukajaut(obs, zaba_x, zaba_y));
            action = siec.predict(obs)
        else:
            #konieczne, poniewaz symulujemy przyciski - jesli akcja sie powtorzy zostanie wykonanana tylko raz 
            #mogloby to zaburzyc proces uczenia sie imo
            action = 0
        obs, reward, terminated, truncated, info = env.step(action)
 

    env.close()

if __name__ == '__main__':
    run()