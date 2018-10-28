import pickle
import numpy as np

pipeline = pickle.load(open('../model.pkl', 'rb'))


example = {
    'period': 9.48,
    'impact': .146,
    'duration': 2.9575,
    'depth': 615.8,
    'prad': 2.26,
    'teq': 793,
    'insol': 93.59,
    'model_snr': 35.8
}

def predict_planet(features):
    X = np.array([features['period'], features['impact'], features['duration'], features['depth'], features['prad'],
                features['teq'], features['insol'], features['model_snr']]).reshape(1, -1)

    prob_planet = pipeline.predict_proba(X)[0, 1]

    result = {'prediction': int(prob_planet > 0.5),
              'prob_planet': prob_planet
    }

    return result

if __name__ == '__main__':
    print(predict_planet(example))