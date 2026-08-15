# Veracia Eval Report — Veritarach adversarial robustness

Dataset: 18 case(s)

## Summary

| Metric | Value |
| --- | --- |
| confusion_matrix | {'tp': 15, 'fp': 0, 'tn': 0, 'fn': 3} |
| precision | 1.0 |
| recall | 0.8333333333333334 |
| f1 | 0.9090909090909091 |
| false_positive_rate | 0.0 |
| pre_accuracy | 1.0 |
| post_accuracy | 0.8333333333333334 |
| avg_confidence_delta | -0.009177254305945503 |

## Failures (worst 10)

| Input | Expected | Actual | Confidence |
| --- | --- | --- | --- |
| 'A small balcony or raised bed with containers will yield more than anticipated. Begin with hardy pla...' | 'ai_generated' | 'human_written' | 0.5050123333930969 |
| 'A REST API is a collection of guidelines determining how two applications communicate using HTTP. Yo...' | 'ai_generated' | 'human_written' | 0.5125977993011475 |
| 'Begin by generously salting your pasta water to achieve a briny flavor reminiscent of the ocean. As ...' | 'ai_generated' | 'human_written' | 0.6738423109054565 |
| "There's an odd ease in acknowledging you won't complete the entire list, recognizing that the object..." | 'ai_generated' | 'ai_generated' | 0.5045701265335083 |
| 'Vaccines function by introducing your immune system a safe sample of an invader -- like a diminished...' | 'ai_generated' | 'ai_generated' | 0.5132429003715515 |
| "Your initial creation will likely appear unattractive, and that's perfectly acceptable—no one's firs..." | 'ai_generated' | 'ai_generated' | 0.514758288860321 |
| 'Adopted her at eight, already gray around the muzzle, since older dogs are less likely to be selecte...' | 'ai_generated' | 'ai_generated' | 0.5158265233039856 |
| 'The central idea is straightforward: a research vessel receives an unexpected signal from under the ...' | 'ai_generated' | 'ai_generated' | 0.5240628123283386 |
| 'The enigma features a classic locked-room scenario and several potential suspects who each have some...' | 'ai_generated' | 'ai_generated' | 0.5328353047370911 |
| 'Tuesday night saw voters in the district narrowly re-elect the incumbent with a turnout significantl...' | 'ai_generated' | 'ai_generated' | 0.5453714728355408 |

## Full Results

| Input | Expected | Actual | Confidence |
| --- | --- | --- | --- |
| 'A REST API is a collection of guidelines determining how two applications communicate using HTTP. Yo...' | 'ai_generated' | 'human_written' | 0.5125977993011475 |
| "In late October, we arrived in Kyoto as the maples along the Philosopher's Path were beginning to ch..." | 'ai_generated' | 'ai_generated' | 0.6058018803596497 |
| "The keyboard features a pleasurable key travel that isn't overly soft, and its low-profile switches ..." | 'ai_generated' | 'ai_generated' | 0.6026267409324646 |
| 'Begin by generously salting your pasta water to achieve a briny flavor reminiscent of the ocean. As ...' | 'ai_generated' | 'human_written' | 0.6738423109054565 |
| "During the initial weeks at a new job, it's common to feel a bit lost; this isn't an indication of f..." | 'ai_generated' | 'ai_generated' | 0.5924448370933533 |
| 'Tuesday night saw voters in the district narrowly re-elect the incumbent with a turnout significantl...' | 'ai_generated' | 'ai_generated' | 0.5453714728355408 |
| 'The central idea is straightforward: a research vessel receives an unexpected signal from under the ...' | 'ai_generated' | 'ai_generated' | 0.5240628123283386 |
| 'In the fourth quarter, the home team expanded their lead with a 14-2 run, transforming a three-point...' | 'ai_generated' | 'ai_generated' | 0.62081378698349 |
| 'Contrary to popular belief, composting in an urban apartment is achievable -- you just need a compac...' | 'ai_generated' | 'ai_generated' | 0.6258500218391418 |
| "There's an odd ease in acknowledging you won't complete the entire list, recognizing that the object..." | 'ai_generated' | 'ai_generated' | 0.5045701265335083 |
| 'He had kept track of the flashes since dusk, at a steady rate of one every eleven seconds, a rhythm ...' | 'ai_generated' | 'ai_generated' | 0.5889726281166077 |
| 'The enigma features a classic locked-room scenario and several potential suspects who each have some...' | 'ai_generated' | 'ai_generated' | 0.5328353047370911 |
| "Your initial creation will likely appear unattractive, and that's perfectly acceptable—no one's firs..." | 'ai_generated' | 'ai_generated' | 0.514758288860321 |
| 'Vaccines function by introducing your immune system a safe sample of an invader -- like a diminished...' | 'ai_generated' | 'ai_generated' | 0.5132429003715515 |
| 'The broth is perfectly balanced and takes a full day to perfect. The noodles have just the right amo...' | 'ai_generated' | 'ai_generated' | 0.6079961657524109 |
| 'A small balcony or raised bed with containers will yield more than anticipated. Begin with hardy pla...' | 'ai_generated' | 'human_written' | 0.5050123333930969 |
| 'Adopted her at eight, already gray around the muzzle, since older dogs are less likely to be selecte...' | 'ai_generated' | 'ai_generated' | 0.5158265233039856 |
| 'Interest accumulates on both the principal amount and the previously earned interest. This causes th...' | 'ai_generated' | 'ai_generated' | 0.617573618888855 |
