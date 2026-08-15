# Veracia Eval Report — Veritarach holdout

Dataset: 47 case(s)

## Summary

| Metric | Value |
| --- | --- |
| confusion_matrix | {'tp': 1, 'fp': 0, 'tn': 23, 'fn': 23} |
| precision | 1.0 |
| recall | 0.041666666666666664 |
| f1 | 0.07999999999999999 |
| false_positive_rate | 0.0 |

## Failures (worst 10)

| Input | Expected | Actual | Confidence |
| --- | --- | --- | --- |
| 'Expect overcast skies through the morning with the fog burning off by early afternoon, giving way to...' | 'ai_generated' | 'human_written' | 0.9893821477890015 |
| "The keeper had counted the flashes since dusk, one every eleven seconds, the same rhythm he'd been l..." | 'ai_generated' | 'human_written' | 0.9918599724769592 |
| 'The home team pulled away in the fourth quarter behind a 14-2 run, turning a three-point deficit int...' | 'ai_generated' | 'human_written' | 0.9932010769844055 |
| 'Voters in the district re-elected the incumbent by a narrow margin Tuesday night, with turnout runni...' | 'ai_generated' | 'human_written' | 0.9941149353981018 |
| "First weeks at a new job are always a little disorienting, and that's normal, not a sign you're behi..." | 'ai_generated' | 'human_written' | 0.9957758784294128 |
| "Composting in a city apartment is more doable than people assume -- you don't need a backyard, just ..." | 'ai_generated' | 'human_written' | 0.9959970712661743 |
| "We landed in Kyoto in late October, right as the maples along the Philosopher's Path were starting t..." | 'ai_generated' | 'human_written' | 0.9969090819358826 |
| 'This keyboard has a satisfying amount of travel on each key without feeling mushy, and the low-profi...' | 'ai_generated' | 'human_written' | 0.9985108971595764 |
| 'A REST API is just a set of rules for how two programs talk to each other over HTTP. You send a requ...' | 'ai_generated' | 'human_written' | 0.9987319111824036 |
| 'Vaccines work by showing your immune system a harmless preview of a threat -- a weakened or inactiva...' | 'ai_generated' | 'human_written' | 0.9988840222358704 |

## Full Results

| Input | Expected | Actual | Confidence |
| --- | --- | --- | --- |
| 'As no objection was made to the young people’s engagement with their aunt, and all Mr. Collins’s scr...' | 'human_written' | 'human_written' | 0.9998873472213745 |
| 'Mr. Wickham’s society was of material service in dispelling the gloom which the late perverse occurr...' | 'human_written' | 'human_written' | 0.9999768733978271 |
| 'The extravagance and general profligacy which he scrupled not to lay to Mr. Wickham’s charge exceedi...' | 'human_written' | 'human_written' | 0.999982476234436 |
| 'In this room they were received by Miss Darcy, who was sitting there with Mrs. Hurst and Miss Bingle...' | 'human_written' | 'human_written' | 0.9999523162841797 |
| '“Well, and so, just as the carriage came to the door, my uncle was called away upon business to that...' | 'human_written' | 'human_written' | 0.9998055100440979 |
| '“It is simplicity itself,” said he; “my eyes tell me that on the inside of your left shoe, just wher...' | 'human_written' | 'human_written' | 0.9999754428863525 |
| 'What a time it seemed! From comparing notes afterwards it was but an hour and a quarter, yet it appe...' | 'human_written' | 'human_written' | 0.9867510199546814 |
| '“Well, obviously it could not have been meant for the son. The son, as far as he knew, was in Bristo...' | 'human_written' | 'human_written' | 0.9982084035873413 |
| 'He picked it up and gazed at it in the peculiar introspective fashion which was characteristic of hi...' | 'human_written' | 'human_written' | 0.9998729228973389 |
| '“I had come to these conclusions before ever I had entered his room. An inspection of his chair show...' | 'human_written' | 'human_written' | 0.9997072815895081 |
| '“Seeing that my client was anxious to leave, I said no more but, calling for my cashier, I ordered h...' | 'human_written' | 'human_written' | 0.9999083280563354 |
| 'These visions faded when I perused, for the first time, those poets whose effusions entranced my sou...' | 'human_written' | 'human_written' | 0.9999774694442749 |
| 'I see by your eagerness and the wonder and hope which your eyes express, my friend, that you expect ...' | 'human_written' | 'human_written' | 0.9999722242355347 |
| '“Why do you call to my remembrance,” I rejoined, “circumstances of which I shudder to reflect, that ...' | 'human_written' | 'human_written' | 0.9998262524604797 |
| '“I endeavoured to crush these fears and to fortify myself for the trial which in a few months I reso...' | 'human_written' | 'human_written' | 0.9995891451835632 |
| 'We left Edinburgh in a week, passing through Coupar, St. Andrew’s, and along the banks of the Tay, t...' | 'human_written' | 'human_written' | 0.9998482465744019 |
| 'In the meantime I took every precaution to defend my person in case the fiend should openly attack m...' | 'human_written' | 'human_written' | 0.9995701909065247 |
| 'In this book a number of dialects are used, to wit: the Missouri negro dialect; the extremest form o...' | 'human_written' | 'human_written' | 0.9999891519546509 |
| '“But I didn’ have no luck. When we ’uz mos’ down to de head er de islan’ a man begin to come aft wid...' | 'human_written' | 'human_written' | 0.9999383687973022 |
| 'The candle was on the floor, and there they all was, looking at me, and me at them, for about a quar...' | 'human_written' | 'human_written' | 0.9999268054962158 |
| 'So somebody started on a run. I walked down street a ways and stopped. In about five or ten minutes ...' | 'human_written' | 'human_written' | 0.9998953342437744 |
| 'So he laughed again; and so did everybody else, except three or four, or maybe half a dozen. One of ...' | 'human_written' | 'human_written' | 0.9995211362838745 |
| '“Many makes it out of iron-rust and tears; but that’s the common sort and women; the best authoritie...' | 'human_written' | 'human_written' | 0.9999793767929077 |
| 'A REST API is just a set of rules for how two programs talk to each other over HTTP. You send a requ...' | 'ai_generated' | 'human_written' | 0.9987319111824036 |
| "We landed in Kyoto in late October, right as the maples along the Philosopher's Path were starting t..." | 'ai_generated' | 'human_written' | 0.9969090819358826 |
| 'This keyboard has a satisfying amount of travel on each key without feeling mushy, and the low-profi...' | 'ai_generated' | 'human_written' | 0.9985108971595764 |
| 'Start by salting your pasta water more than feels reasonable -- it should taste like the sea. While ...' | 'ai_generated' | 'human_written' | 0.9996007084846497 |
| "First weeks at a new job are always a little disorienting, and that's normal, not a sign you're behi..." | 'ai_generated' | 'human_written' | 0.9957758784294128 |
| 'Voters in the district re-elected the incumbent by a narrow margin Tuesday night, with turnout runni...' | 'ai_generated' | 'human_written' | 0.9941149353981018 |
| "Most people don't drink as much water as they think they do, and thirst alone is a poor early signal..." | 'ai_generated' | 'human_written' | 0.9994872808456421 |
| 'Movable type predates Gutenberg by centuries -- Bi Sheng was experimenting with it in China around 1...' | 'ai_generated' | 'human_written' | 0.9999884366989136 |
| "Thanks for reaching out, and I'm sorry for the delay on order #48291. I checked with our fulfillment..." | 'ai_generated' | 'human_written' | 0.9999816417694092 |
| "The premise is simple enough: a research vessel picks up a signal from beneath the ice that shouldn'..." | 'ai_generated' | 'human_written' | 0.9996278285980225 |
| 'The home team pulled away in the fourth quarter behind a 14-2 run, turning a three-point deficit int...' | 'ai_generated' | 'human_written' | 0.9932010769844055 |
| "Composting in a city apartment is more doable than people assume -- you don't need a backyard, just ..." | 'ai_generated' | 'human_written' | 0.9959970712661743 |
| "There's a strange comfort in realizing you'll never get through the whole list, that the goal was ne..." | 'ai_generated' | 'human_written' | 0.9998310804367065 |
| "To reset your password, go to the sign-in page and click 'Forgot password' below the login form. You..." | 'ai_generated' | 'ai_generated' | 0.6906321048736572 |
| "The keeper had counted the flashes since dusk, one every eleven seconds, the same rhythm he'd been l..." | 'ai_generated' | 'human_written' | 0.9918599724769592 |
| 'Expect overcast skies through the morning with the fog burning off by early afternoon, giving way to...' | 'ai_generated' | 'human_written' | 0.9893821477890015 |
| 'The mystery itself is fairly conventional -- a locked room, a handful of suspects each with somethin...' | 'ai_generated' | 'human_written' | 0.9992282390594482 |
| "Hi all -- just a quick note that Thursday's 2pm sync is moving to Friday at 10am instead, same room...." | 'ai_generated' | 'human_written' | 0.9999922513961792 |
| "The first project you build will be ugly and that's fine -- everyone's is. What actually matters at ..." | 'ai_generated' | 'human_written' | 0.9994181394577026 |
| 'Vaccines work by showing your immune system a harmless preview of a threat -- a weakened or inactiva...' | 'ai_generated' | 'human_written' | 0.9988840222358704 |
| 'The broth here is the kind that takes a full day to get right, rich without tipping into heavy, and ...' | 'ai_generated' | 'human_written' | 0.9999537467956543 |
| "You don't need a big yard to start growing your own food -- a few containers on a balcony or a small..." | 'ai_generated' | 'human_written' | 0.9998412132263184 |
| 'We adopted her at eight, already gray around the muzzle, because the shelter said older dogs rarely ...' | 'ai_generated' | 'human_written' | 0.9998993873596191 |
| 'Compound interest is just interest that gets calculated on both your original amount and whatever in...' | 'ai_generated' | 'human_written' | 0.9996656179428101 |
