# Veracia Eval Report — Veritarach holdout

Dataset: 47 case(s)

## Summary

| Metric | Value |
| --- | --- |
| confusion_matrix | {'tp': 18, 'fp': 16, 'tn': 7, 'fn': 6} |
| precision | 0.5294117647058824 |
| recall | 0.75 |
| f1 | 0.6206896551724139 |
| false_positive_rate | 0.6956521739130435 |

## Failures (worst 10)

| Input | Expected | Actual | Confidence |
| --- | --- | --- | --- |
| "Thanks for reaching out, and I'm sorry for the delay on order #48291. I checked with our fulfillment..." | 'ai_generated' | 'human_written' | 0.503282904624939 |
| 'The candle was on the floor, and there they all was, looking at me, and me at them, for about a quar...' | 'human_written' | 'ai_generated' | 0.5072978138923645 |
| '“It is simplicity itself,” said he; “my eyes tell me that on the inside of your left shoe, just wher...' | 'human_written' | 'ai_generated' | 0.5129734873771667 |
| "Hi all -- just a quick note that Thursday's 2pm sync is moving to Friday at 10am instead, same room...." | 'ai_generated' | 'human_written' | 0.514866054058075 |
| "Most people don't drink as much water as they think they do, and thirst alone is a poor early signal..." | 'ai_generated' | 'human_written' | 0.5158207416534424 |
| 'Movable type predates Gutenberg by centuries -- Bi Sheng was experimenting with it in China around 1...' | 'ai_generated' | 'human_written' | 0.5173494815826416 |
| 'So somebody started on a run. I walked down street a ways and stopped. In about five or ten minutes ...' | 'human_written' | 'ai_generated' | 0.5295332670211792 |
| 'He picked it up and gazed at it in the peculiar introspective fashion which was characteristic of hi...' | 'human_written' | 'ai_generated' | 0.5328669548034668 |
| '“Why do you call to my remembrance,” I rejoined, “circumstances of which I shudder to reflect, that ...' | 'human_written' | 'ai_generated' | 0.5497629642486572 |
| '“Well, and so, just as the carriage came to the door, my uncle was called away upon business to that...' | 'human_written' | 'ai_generated' | 0.5537606477737427 |

## Full Results

| Input | Expected | Actual | Confidence |
| --- | --- | --- | --- |
| 'As no objection was made to the young people’s engagement with their aunt, and all Mr. Collins’s scr...' | 'human_written' | 'ai_generated' | 0.5620331168174744 |
| 'Mr. Wickham’s society was of material service in dispelling the gloom which the late perverse occurr...' | 'human_written' | 'human_written' | 0.5185528993606567 |
| 'The extravagance and general profligacy which he scrupled not to lay to Mr. Wickham’s charge exceedi...' | 'human_written' | 'human_written' | 0.5209155678749084 |
| 'In this room they were received by Miss Darcy, who was sitting there with Mrs. Hurst and Miss Bingle...' | 'human_written' | 'ai_generated' | 0.5580864548683167 |
| '“Well, and so, just as the carriage came to the door, my uncle was called away upon business to that...' | 'human_written' | 'ai_generated' | 0.5537606477737427 |
| '“It is simplicity itself,” said he; “my eyes tell me that on the inside of your left shoe, just wher...' | 'human_written' | 'ai_generated' | 0.5129734873771667 |
| 'What a time it seemed! From comparing notes afterwards it was but an hour and a quarter, yet it appe...' | 'human_written' | 'ai_generated' | 0.6444137096405029 |
| '“Well, obviously it could not have been meant for the son. The son, as far as he knew, was in Bristo...' | 'human_written' | 'ai_generated' | 0.5873115658760071 |
| 'He picked it up and gazed at it in the peculiar introspective fashion which was characteristic of hi...' | 'human_written' | 'ai_generated' | 0.5328669548034668 |
| '“I had come to these conclusions before ever I had entered his room. An inspection of his chair show...' | 'human_written' | 'ai_generated' | 0.575579047203064 |
| '“Seeing that my client was anxious to leave, I said no more but, calling for my cashier, I ordered h...' | 'human_written' | 'ai_generated' | 0.5665427446365356 |
| 'These visions faded when I perused, for the first time, those poets whose effusions entranced my sou...' | 'human_written' | 'human_written' | 0.5345621705055237 |
| 'I see by your eagerness and the wonder and hope which your eyes express, my friend, that you expect ...' | 'human_written' | 'human_written' | 0.5182079076766968 |
| '“Why do you call to my remembrance,” I rejoined, “circumstances of which I shudder to reflect, that ...' | 'human_written' | 'ai_generated' | 0.5497629642486572 |
| '“I endeavoured to crush these fears and to fortify myself for the trial which in a few months I reso...' | 'human_written' | 'ai_generated' | 0.579755425453186 |
| 'We left Edinburgh in a week, passing through Coupar, St. Andrew’s, and along the banks of the Tay, t...' | 'human_written' | 'ai_generated' | 0.5727803111076355 |
| 'In the meantime I took every precaution to defend my person in case the fiend should openly attack m...' | 'human_written' | 'ai_generated' | 0.5762614011764526 |
| 'In this book a number of dialects are used, to wit: the Missouri negro dialect; the extremest form o...' | 'human_written' | 'human_written' | 0.5305771827697754 |
| '“But I didn’ have no luck. When we ’uz mos’ down to de head er de islan’ a man begin to come aft wid...' | 'human_written' | 'human_written' | 0.5027108192443848 |
| 'The candle was on the floor, and there they all was, looking at me, and me at them, for about a quar...' | 'human_written' | 'ai_generated' | 0.5072978138923645 |
| 'So somebody started on a run. I walked down street a ways and stopped. In about five or ten minutes ...' | 'human_written' | 'ai_generated' | 0.5295332670211792 |
| 'So he laughed again; and so did everybody else, except three or four, or maybe half a dozen. One of ...' | 'human_written' | 'ai_generated' | 0.5715658664703369 |
| '“Many makes it out of iron-rust and tears; but that’s the common sort and women; the best authoritie...' | 'human_written' | 'human_written' | 0.5070557594299316 |
| 'A REST API is just a set of rules for how two programs talk to each other over HTTP. You send a requ...' | 'ai_generated' | 'ai_generated' | 0.5852073431015015 |
| "We landed in Kyoto in late October, right as the maples along the Philosopher's Path were starting t..." | 'ai_generated' | 'ai_generated' | 0.6162669658660889 |
| 'This keyboard has a satisfying amount of travel on each key without feeling mushy, and the low-profi...' | 'ai_generated' | 'ai_generated' | 0.571526825428009 |
| 'Start by salting your pasta water more than feels reasonable -- it should taste like the sea. While ...' | 'ai_generated' | 'ai_generated' | 0.6122464537620544 |
| "First weeks at a new job are always a little disorienting, and that's normal, not a sign you're behi..." | 'ai_generated' | 'ai_generated' | 0.6078881621360779 |
| 'Voters in the district re-elected the incumbent by a narrow margin Tuesday night, with turnout runni...' | 'ai_generated' | 'ai_generated' | 0.6060222387313843 |
| "Most people don't drink as much water as they think they do, and thirst alone is a poor early signal..." | 'ai_generated' | 'human_written' | 0.5158207416534424 |
| 'Movable type predates Gutenberg by centuries -- Bi Sheng was experimenting with it in China around 1...' | 'ai_generated' | 'human_written' | 0.5173494815826416 |
| "Thanks for reaching out, and I'm sorry for the delay on order #48291. I checked with our fulfillment..." | 'ai_generated' | 'human_written' | 0.503282904624939 |
| "The premise is simple enough: a research vessel picks up a signal from beneath the ice that shouldn'..." | 'ai_generated' | 'ai_generated' | 0.5855409502983093 |
| 'The home team pulled away in the fourth quarter behind a 14-2 run, turning a three-point deficit int...' | 'ai_generated' | 'ai_generated' | 0.6349866390228271 |
| "Composting in a city apartment is more doable than people assume -- you don't need a backyard, just ..." | 'ai_generated' | 'ai_generated' | 0.6016952991485596 |
| "There's a strange comfort in realizing you'll never get through the whole list, that the goal was ne..." | 'ai_generated' | 'ai_generated' | 0.5398021340370178 |
| "To reset your password, go to the sign-in page and click 'Forgot password' below the login form. You..." | 'ai_generated' | 'human_written' | 0.6943260431289673 |
| "The keeper had counted the flashes since dusk, one every eleven seconds, the same rhythm he'd been l..." | 'ai_generated' | 'ai_generated' | 0.6154762506484985 |
| 'Expect overcast skies through the morning with the fog burning off by early afternoon, giving way to...' | 'ai_generated' | 'human_written' | 0.668365478515625 |
| 'The mystery itself is fairly conventional -- a locked room, a handful of suspects each with somethin...' | 'ai_generated' | 'ai_generated' | 0.578141450881958 |
| "Hi all -- just a quick note that Thursday's 2pm sync is moving to Friday at 10am instead, same room...." | 'ai_generated' | 'human_written' | 0.514866054058075 |
| "The first project you build will be ugly and that's fine -- everyone's is. What actually matters at ..." | 'ai_generated' | 'ai_generated' | 0.6414727568626404 |
| 'Vaccines work by showing your immune system a harmless preview of a threat -- a weakened or inactiva...' | 'ai_generated' | 'ai_generated' | 0.5548138618469238 |
| 'The broth here is the kind that takes a full day to get right, rich without tipping into heavy, and ...' | 'ai_generated' | 'ai_generated' | 0.5043124556541443 |
| "You don't need a big yard to start growing your own food -- a few containers on a balcony or a small..." | 'ai_generated' | 'ai_generated' | 0.5097981691360474 |
| 'We adopted her at eight, already gray around the muzzle, because the shelter said older dogs rarely ...' | 'ai_generated' | 'ai_generated' | 0.5023539662361145 |
| 'Compound interest is just interest that gets calculated on both your original amount and whatever in...' | 'ai_generated' | 'ai_generated' | 0.501838207244873 |
