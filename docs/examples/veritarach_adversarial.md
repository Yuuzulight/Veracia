# Veracia Eval Report — Veritarach adversarial robustness

Dataset: 18 case(s)

## Summary

| Metric | Value |
| --- | --- |
| confusion_matrix | {'tp': 0, 'fp': 0, 'tn': 0, 'fn': 18} |
| precision | 0.0 |
| recall | 0.0 |
| f1 | 0.0 |
| false_positive_rate | 0.0 |
| pre_accuracy | 1.0 |
| post_accuracy | 0.0 |
| avg_confidence_delta | 0.42168224851290387 |

## Failures (worst 10)

| Input | Expected | Actual | Confidence |
| --- | --- | --- | --- |
| 'Begin by generously salting your pasta water to achieve a briny flavor reminiscent of the ocean. As ...' | 'ai_generated' | 'human_written' | 0.9912712574005127 |
| 'He had kept track of the flashes since dusk, at a steady rate of one every eleven seconds, a rhythm ...' | 'ai_generated' | 'human_written' | 0.9929666519165039 |
| 'In the fourth quarter, the home team expanded their lead with a 14-2 run, transforming a three-point...' | 'ai_generated' | 'human_written' | 0.9939385652542114 |
| 'Interest accumulates on both the principal amount and the previously earned interest. This causes th...' | 'ai_generated' | 'human_written' | 0.9962778687477112 |
| 'The enigma features a classic locked-room scenario and several potential suspects who each have some...' | 'ai_generated' | 'human_written' | 0.9967185854911804 |
| 'Contrary to popular belief, composting in an urban apartment is achievable -- you just need a compac...' | 'ai_generated' | 'human_written' | 0.9969077706336975 |
| "In late October, we arrived in Kyoto as the maples along the Philosopher's Path were beginning to ch..." | 'ai_generated' | 'human_written' | 0.9977420568466187 |
| 'The central idea is straightforward: a research vessel receives an unexpected signal from under the ...' | 'ai_generated' | 'human_written' | 0.9983943104743958 |
| 'Vaccines function by introducing your immune system a safe sample of an invader -- like a diminished...' | 'ai_generated' | 'human_written' | 0.9986475110054016 |
| 'Tuesday night saw voters in the district narrowly re-elect the incumbent with a turnout significantl...' | 'ai_generated' | 'human_written' | 0.9986904263496399 |

## Full Results

| Input | Expected | Actual | Confidence |
| --- | --- | --- | --- |
| 'A REST API is a collection of guidelines determining how two applications communicate using HTTP. Yo...' | 'ai_generated' | 'human_written' | 0.9999885559082031 |
| "In late October, we arrived in Kyoto as the maples along the Philosopher's Path were beginning to ch..." | 'ai_generated' | 'human_written' | 0.9977420568466187 |
| "The keyboard features a pleasurable key travel that isn't overly soft, and its low-profile switches ..." | 'ai_generated' | 'human_written' | 0.9998524188995361 |
| 'Begin by generously salting your pasta water to achieve a briny flavor reminiscent of the ocean. As ...' | 'ai_generated' | 'human_written' | 0.9912712574005127 |
| "During the initial weeks at a new job, it's common to feel a bit lost; this isn't an indication of f..." | 'ai_generated' | 'human_written' | 0.9995280504226685 |
| 'Tuesday night saw voters in the district narrowly re-elect the incumbent with a turnout significantl...' | 'ai_generated' | 'human_written' | 0.9986904263496399 |
| 'The central idea is straightforward: a research vessel receives an unexpected signal from under the ...' | 'ai_generated' | 'human_written' | 0.9983943104743958 |
| 'In the fourth quarter, the home team expanded their lead with a 14-2 run, transforming a three-point...' | 'ai_generated' | 'human_written' | 0.9939385652542114 |
| 'Contrary to popular belief, composting in an urban apartment is achievable -- you just need a compac...' | 'ai_generated' | 'human_written' | 0.9969077706336975 |
| "There's an odd ease in acknowledging you won't complete the entire list, recognizing that the object..." | 'ai_generated' | 'human_written' | 0.9998989105224609 |
| 'He had kept track of the flashes since dusk, at a steady rate of one every eleven seconds, a rhythm ...' | 'ai_generated' | 'human_written' | 0.9929666519165039 |
| 'The enigma features a classic locked-room scenario and several potential suspects who each have some...' | 'ai_generated' | 'human_written' | 0.9967185854911804 |
| "Your initial creation will likely appear unattractive, and that's perfectly acceptable—no one's firs..." | 'ai_generated' | 'human_written' | 0.9999475479125977 |
| 'Vaccines function by introducing your immune system a safe sample of an invader -- like a diminished...' | 'ai_generated' | 'human_written' | 0.9986475110054016 |
| 'The broth is perfectly balanced and takes a full day to perfect. The noodles have just the right amo...' | 'ai_generated' | 'human_written' | 0.9990004897117615 |
| 'A small balcony or raised bed with containers will yield more than anticipated. Begin with hardy pla...' | 'ai_generated' | 'human_written' | 0.9999804496765137 |
| 'Adopted her at eight, already gray around the muzzle, since older dogs are less likely to be selecte...' | 'ai_generated' | 'human_written' | 0.9999191761016846 |
| 'Interest accumulates on both the principal amount and the previously earned interest. This causes th...' | 'ai_generated' | 'human_written' | 0.9962778687477112 |
