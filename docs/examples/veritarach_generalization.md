# Veracia Eval Report — Veritarach cross-model generalization

Dataset: 100 case(s)

## Summary

| Metric | Value |
| --- | --- |
| confusion_matrix | {'tp': 8, 'fp': 0, 'tn': 0, 'fn': 92} |
| precision | 1.0 |
| recall | 0.08 |
| f1 | 0.14814814814814814 |
| false_positive_rate | 0.0 |
| accuracy | 0.08 |
| baseline_accuracy | 0.5319148936170213 |
| accuracy_delta | -0.45191489361702125 |

## Failures (worst 10)

| Input | Expected | Actual | Confidence |
| --- | --- | --- | --- |
| 'Cyclists adeptly maintain balance while moving through a combination of skilled maneuvers and inhere...' | 'ai_generated' | 'human_written' | 0.5452656149864197 |
| 'Monarch butterflies (Danaus plexippus) are renowned for their extraordinary migration patterns, one ...' | 'ai_generated' | 'human_written' | 0.6141840219497681 |
| "Coffee's history dates back to ancient Ethiopia, where legend has it that a goat herder named Kaldi ..." | 'ai_generated' | 'human_written' | 0.6202760338783264 |
| 'In the dim glow of his workshop, Johannes Gutenberg hunched over a wooden block, carving not merely ...' | 'ai_generated' | 'human_written' | 0.6347848176956177 |
| 'The bicycle, an iconic mode of transport, traces its roots back to the 1817 "Draisine" or "Running m...' | 'ai_generated' | 'human_written' | 0.6348422765731812 |
| 'In the shadowy corners of ancient Yemen, a mysterious bean thrummed with vitality, a divine secret p...' | 'ai_generated' | 'human_written' | 0.635437548160553 |
| "Hey there! Ever wonder how noise-cancelling headphones magically block out the world's sounds? It al..." | 'ai_generated' | 'human_written' | 0.6374077200889587 |
| 'Beneath the cobblestone streets of 19th-century Paris, whispers spoke of an invention that would rev...' | 'ai_generated' | 'human_written' | 0.6392475366592407 |
| 'Hey there! So, you’ve ever wondered why bread rises when you bake it? It all has to do with yeast, t...' | 'ai_generated' | 'human_written' | 0.6404328346252441 |
| 'The history of tea dates back thousands of years, originating in ancient China around 2737 BCE. Empe...' | 'ai_generated' | 'human_written' | 0.6429441571235657 |

## Full Results

| Input | Expected | Actual | Confidence |
| --- | --- | --- | --- |
| 'The history of tea dates back thousands of years, originating in ancient China around 2737 BCE. Empe...' | 'ai_generated' | 'human_written' | 0.6429441571235657 |
| "Hey there! Ever wondered about tea's story? Tea's been around since the ancient Chinese dynasties, b..." | 'ai_generated' | 'ai_generated' | 0.6290984153747559 |
| 'In ancient China, legend whispers of Emperor Shen Nong, who chanced upon a mystical leaf falling int...' | 'ai_generated' | 'ai_generated' | 0.628883957862854 |
| 'Sure, here are a few practical tips related to the history of tea:\n\n1. **Explore Different Types**: ...' | 'ai_generated' | 'human_written' | 0.6961119174957275 |
| "Originating in ancient China around 2737 BC, tea's journey began with Emperor Shen Nong who discover..." | 'ai_generated' | 'human_written' | 0.6915765404701233 |
| 'Bicycles maintain balance through a combination of rider input, wheel geometry, and physical forces....' | 'ai_generated' | 'human_written' | 0.6826361417770386 |
| "Hey there!\n\nEver wondered how bikes stay upright while you pedal? It's all about balance! Here's the..." | 'ai_generated' | 'human_written' | 0.689298152923584 |
| 'Beneath the gentle sway of the willow tree, Mia balanced her bicycle on the cobblestone path, feelin...' | 'ai_generated' | 'human_written' | 0.6941609978675842 |
| 'Bicycles maintain balance while moving through a combination of several mechanisms:\n\n1. **Center of ...' | 'ai_generated' | 'human_written' | 0.6966054439544678 |
| 'Cyclists adeptly maintain balance while moving through a combination of skilled maneuvers and inhere...' | 'ai_generated' | 'human_written' | 0.5452656149864197 |
| 'Leaves change color in autumn due to the reduction of chlorophyll production in the fall season. As ...' | 'ai_generated' | 'human_written' | 0.6896008849143982 |
| 'Hey there! Ever wonder why leaves turn all sorts of colors in the fall? It’s all thanks to some clev...' | 'ai_generated' | 'human_written' | 0.6930723190307617 |
| 'In the heart of Maplewood Forest, leaves once green now donned shades of amber, gold, and crimson, a...' | 'ai_generated' | 'human_written' | 0.6756308674812317 |
| 'Leaves change color in autumn due to the reduction of chlorophyll production in response to shorter ...' | 'ai_generated' | 'human_written' | 0.694513201713562 |
| 'As autumn arrives, leaves undergo a stunning transformation. This natural phenomenon is driven by th...' | 'ai_generated' | 'human_written' | 0.6931342482566833 |
| 'Weather refers to the short-term conditions of the atmosphere at a specific time and place, includin...' | 'ai_generated' | 'human_written' | 0.6858476400375366 |
| 'Hey there! Quick note on weather vs climate. Weather is what you experience day-to-day, like sunshin...' | 'ai_generated' | 'ai_generated' | 0.618942141532898 |
| 'In the small coastal town of Bayview, Clara watched as the brisk autumn air turned to a balmy summer...' | 'ai_generated' | 'human_written' | 0.6819189786911011 |
| 'Understanding the difference between weather and climate is crucial for various fields. Here are a f...' | 'ai_generated' | 'human_written' | 0.7007483243942261 |
| 'Weather refers to short-term atmospheric conditions at a specific place and time, including variable...' | 'ai_generated' | 'human_written' | 0.6834036111831665 |
| 'A lighthouse functions as a navigational aid, guiding mariners safely through treacherous coastal wa...' | 'ai_generated' | 'human_written' | 0.6907638311386108 |
| "Hey there!\n\nSo, you've ever wondered how a lighthouse works? It's pretty cool! Basically, it uses a ..." | 'ai_generated' | 'human_written' | 0.6991970539093018 |
| 'High atop a jagged cliff stood the lighthouse, its beacon a steadfast sentinel against the restless ...' | 'ai_generated' | 'human_written' | 0.6791099905967712 |
| 'A lighthouse functions to guide ships safely by emitting a bright light visible over long distances....' | 'ai_generated' | 'human_written' | 0.6972777843475342 |
| 'Lighthouses serve as a beacon of hope and guidance for sailors navigating treacherous waters. At the...' | 'ai_generated' | 'human_written' | 0.6881812214851379 |
| 'The invention of the printing press, attributed to Johannes Gutenberg in the mid-15th century, revol...' | 'ai_generated' | 'human_written' | 0.6759657859802246 |
| 'Hey there! So, have you ever wondered who invented the printing press? Well, it was Johannes Gutenbe...' | 'ai_generated' | 'human_written' | 0.6900256276130676 |
| 'In the dim glow of his workshop, Johannes Gutenberg hunched over a wooden block, carving not merely ...' | 'ai_generated' | 'human_written' | 0.6347848176956177 |
| 'The invention of the printing press by Johannes Gutenberg in the 15th century revolutionized the dis...' | 'ai_generated' | 'human_written' | 0.697365403175354 |
| 'In the mid-15th century, Johannes Gutenberg revolutionized the spread of knowledge with the inventio...' | 'ai_generated' | 'human_written' | 0.684782862663269 |
| 'Bread rises due to the fermentation process induced by yeast, a type of fungus. When yeast is added ...' | 'ai_generated' | 'human_written' | 0.7000171542167664 |
| 'Hey there! So, you’ve ever wondered why bread rises when you bake it? It all has to do with yeast, t...' | 'ai_generated' | 'human_written' | 0.6404328346252441 |
| 'In the quiet corner of an old bakery, Sarah watched with childlike wonder as the dough slowly transf...' | 'ai_generated' | 'human_written' | 0.6976996660232544 |
| 'Bread rises due to the action of yeast. Here are a few practical tips to help your bread rise effect...' | 'ai_generated' | 'human_written' | 0.6982472538948059 |
| 'Bread rises due to yeast fermentation, a process transforming dough into fluffy loaves. Yeast, a sin...' | 'ai_generated' | 'ai_generated' | 0.5181543827056885 |
| 'Noise-cancelling headphones utilize active noise control technology to reduce unwanted ambient sound...' | 'ai_generated' | 'human_written' | 0.6945803761482239 |
| "Hey there! Ever wonder how noise-cancelling headphones magically block out the world's sounds? It al..." | 'ai_generated' | 'human_written' | 0.6374077200889587 |
| 'In the bustling city, where honking horns and chattering crowds drowned out serenity, Max sought ref...' | 'ai_generated' | 'human_written' | 0.6868180632591248 |
| '1. **Active Noise Control:** Noise-cancelling headphones use microphones to pick up ambient sounds, ...' | 'ai_generated' | 'human_written' | 0.6993093490600586 |
| 'Innovations in personal audio technology have led to the development of noise-cancelling headphones....' | 'ai_generated' | 'human_written' | 0.6965318918228149 |
| 'Monarch butterflies (Danaus plexippus) are renowned for their extraordinary migration patterns, one ...' | 'ai_generated' | 'human_written' | 0.6141840219497681 |
| 'Hey there! Just wanted to share a fascinating bit about monarch butterflies. These incredible little...' | 'ai_generated' | 'human_written' | 0.6959482431411743 |
| 'The air buzzed with a peculiar warmth as thousands of monarch butterflies unfurled their wings again...' | 'ai_generated' | 'human_written' | 0.6715376377105713 |
| 'To support monarch butterfly migration, consider planting milkweed in your garden, as this is their ...' | 'ai_generated' | 'human_written' | 0.673291027545929 |
| 'Monarch butterflies, known for their remarkable annual migration, traverse thousands of miles from N...' | 'ai_generated' | 'human_written' | 0.6909944415092468 |
| 'A thermostat regulates temperature through a feedback loop mechanism. Inside the thermostat, a senso...' | 'ai_generated' | 'human_written' | 0.6771323680877686 |
| 'Hey there! 🛋️ Ever wondered how a thermostat keeps your room cozy or cool? It’s all about balancing ...' | 'ai_generated' | 'human_written' | 0.6972372531890869 |
| 'In the quiet hum of the Smith household, the thermostat sat silently in the wall, an unassuming sent...' | 'ai_generated' | 'human_written' | 0.6688873171806335 |
| 'A thermostat regulates temperature by maintaining a desired setpoint through a feedback loop. Here a...' | 'ai_generated' | 'human_written' | 0.6977428793907166 |
| 'A thermostat regulates temperature through a simple yet effective mechanism. Located in your heating...' | 'ai_generated' | 'human_written' | 0.6956390142440796 |
| 'Chess is a strategic board game with a history that dates back to the 6th century in India. Known in...' | 'ai_generated' | 'human_written' | 0.6918096542358398 |
| "Hey! Did you know chess has such an ancient origin? It's believed to have started in India around 6t..." | 'ai_generated' | 'human_written' | 0.6822406649589539 |
| 'In the ancient Indian subcontinent, beneath the shadowed banyan tree of a wise sage named Dhanna, th...' | 'ai_generated' | 'ai_generated' | 0.641549289226532 |
| 'Sure! Here are a few practical tips related to the origin of chess:\n\n1. **Historical Research:** Del...' | 'ai_generated' | 'human_written' | 0.6975938677787781 |
| 'Originating in the 6th century in India, chess began as a game called Chaturanga. Its name evolved a...' | 'ai_generated' | 'human_written' | 0.6515392065048218 |
| "The sky appears blue due to Rayleigh scattering, which occurs when sunlight enters Earth's atmospher..." | 'ai_generated' | 'human_written' | 0.6967047452926636 |
| "Hey there! So, why is the sky blue? It's all about light and tiny particles in the air. Sunlight loo..." | 'ai_generated' | 'human_written' | 0.6943334341049194 |
| 'The azure expanse above stretched endlessly, its cerulean hue a comforting blanket of peace. On this...' | 'ai_generated' | 'human_written' | 0.6933374404907227 |
| 'Sure! Here are a few practical tips to understand why the sky is blue:\n\n1. **Rayleigh Scattering**: ...' | 'ai_generated' | 'human_written' | 0.6973819732666016 |
| "Sky's Blue Explained: The sky appears blue due to Rayleigh scattering. As sunlight passes through Ea..." | 'ai_generated' | 'human_written' | 0.6982293725013733 |
| 'Composting is a natural process that transforms organic waste into nutrient-rich soil amendment. In ...' | 'ai_generated' | 'human_written' | 0.6883949041366577 |
| 'Hey there! 🌿 Ever wondered what happens to kitchen scraps and yard waste in your compost bin? Compos...' | 'ai_generated' | 'human_written' | 0.681244969367981 |
| 'In the tranquil town of Evergreen, nestled beneath the golden canopy, there thrived a hidden world b...' | 'ai_generated' | 'human_written' | 0.6541795134544373 |
| 'Composting is a natural process that breaks down organic materials into rich soil. Here are a few pr...' | 'ai_generated' | 'human_written' | 0.6956592202186584 |
| 'Compost is a rich, nutrient-filled organic material produced through the natural decay of plant and ...' | 'ai_generated' | 'human_written' | 0.6915465593338013 |
| 'The bicycle, a pivotal mode of personal transportation, emerged in the 19th century. Its invention i...' | 'ai_generated' | 'ai_generated' | 0.6324286460876465 |
| 'Hey there! Did you know that the bicycle has been around for quite a while? It all started back in t...' | 'ai_generated' | 'ai_generated' | 0.6468189358711243 |
| 'Beneath the cobblestone streets of 19th-century Paris, whispers spoke of an invention that would rev...' | 'ai_generated' | 'human_written' | 0.6392475366592407 |
| '1. **Understand its origins**: The first crude bicycle, called the "Draisine" or "running machine," ...' | 'ai_generated' | 'human_written' | 0.6987374424934387 |
| 'The bicycle, an iconic mode of transport, traces its roots back to the 1817 "Draisine" or "Running m...' | 'ai_generated' | 'human_written' | 0.6348422765731812 |
| 'Tides are the rhythmic rise and fall of sea levels caused primarily by the gravitational pull of the...' | 'ai_generated' | 'human_written' | 0.683968722820282 |
| "Hey! 🌕 Did you know tides happen because of the moon? Well, it's all about gravity. The moon pulls o..." | 'ai_generated' | 'human_written' | 0.682273268699646 |
| 'Beneath the silvery glow of the moon, the sea whispered secrets to the shore. Waves danced rhythmica...' | 'ai_generated' | 'human_written' | 0.6795312166213989 |
| 'Understanding tides caused by the moon involves recognizing several key principles. Firstly, remembe...' | 'ai_generated' | 'human_written' | 0.6883561611175537 |
| "Recent observations confirm that the Moon's gravitational pull is the primary force behind Earth's t..." | 'ai_generated' | 'human_written' | 0.6879996061325073 |
| 'Cats purr for various reasons that are largely beneficial to their health and well-being. Primarily,...' | 'ai_generated' | 'human_written' | 0.6957736015319824 |
| "Hey there!\n\nEver wonder why cats purr? Well, it's pretty cool. Cats purr for a bunch of reasons. Som..." | 'ai_generated' | 'human_written' | 0.6983128786087036 |
| 'Whiskers twitched against the soft velvet of an old armchair as Luna, the gentle giant of the househ...' | 'ai_generated' | 'human_written' | 0.6885708570480347 |
| 'Cats purr for a variety of reasons, often related to their comfort and well-being. Here are some pra...' | 'ai_generated' | 'human_written' | 0.6979550123214722 |
| 'Cats purr for various reasons, both beneficial and mysterious. Primarily, purring occurs when cats f...' | 'ai_generated' | 'human_written' | 0.6972919702529907 |
| 'A battery stores energy through electrochemical processes involving chemical reactions between its c...' | 'ai_generated' | 'human_written' | 0.6954941153526306 |
| 'Hey there! So, how a battery stores energy is pretty cool. Think of it like a tiny battery factory. ...' | 'ai_generated' | 'human_written' | 0.7003400325775146 |
| 'Beneath the gleaming surface of the sleek, high-tech device lay the heart of its power: a small, cyl...' | 'ai_generated' | 'human_written' | 0.6871795058250427 |
| 'A battery stores energy through chemical reactions between its components, typically involving a pos...' | 'ai_generated' | 'human_written' | 0.6981710195541382 |
| 'A battery stores energy through electrochemical reactions between its components. Inside a battery, ...' | 'ai_generated' | 'human_written' | 0.6881855130195618 |
| 'Bread-making in a bakery begins with mixing ingredients like flour, water, yeast, and salt. This mix...' | 'ai_generated' | 'human_written' | 0.6979288458824158 |
| 'Hey there! 🍞 Just wanted to share the cool steps we take to make fresh bread in the bakery. First, w...' | 'ai_generated' | 'human_written' | 0.6916176080703735 |
| 'In the heart of downtown, the warm glow of "Bread & Butter" bakery welcomed patrons into its cozy em...' | 'ai_generated' | 'human_written' | 0.6684018969535828 |
| '1. **Kneading**: Flour, water, yeast, and salt are mixed together. The dough is kneaded to develop g...' | 'ai_generated' | 'human_written' | 0.695877730846405 |
| 'Bread-making in a bakery is a process rooted in tradition but guided by modern techniques. Bakers be...' | 'ai_generated' | 'human_written' | 0.6946293711662292 |
| "Coffee's history dates back to ancient Ethiopia, where legend has it that a goat herder named Kaldi ..." | 'ai_generated' | 'human_written' | 0.6202760338783264 |
| 'Hey there! So, coffee has a fascinating history. It all started in ancient Ethiopia where legend say...' | 'ai_generated' | 'human_written' | 0.6884711384773254 |
| 'In the shadowy corners of ancient Yemen, a mysterious bean thrummed with vitality, a divine secret p...' | 'ai_generated' | 'human_written' | 0.635437548160553 |
| '1. **Explore Historical Origins**: Coffee’s journey began in ancient Ethiopia around 850 AD, where l...' | 'ai_generated' | 'human_written' | 0.6927895545959473 |
| 'Coffee, a beloved global beverage, traces its origins back to Ethiopia in the 9th century, where leg...' | 'ai_generated' | 'ai_generated' | 0.5435705184936523 |
| 'A violin produces sound through the vibration of its strings. When a player draws a bow across these...' | 'ai_generated' | 'human_written' | 0.697587788105011 |
| "Hey there! So, here's how a violin makes its magic: It's all about the strings, right? When you pluc..." | 'ai_generated' | 'human_written' | 0.6921188235282898 |
| 'Amidst the quiet hum of an ancient library, a lone violin rested upon a mahogany stand, its glossy f...' | 'ai_generated' | 'human_written' | 0.680546760559082 |
| '1. Pluck the strings: Sound production starts when you pluck the strings with your fingers. The stri...' | 'ai_generated' | 'human_written' | 0.6977706551551819 |
| 'A violin produces sound through the vibration of its strings when plucked or bowed. The strings are ...' | 'ai_generated' | 'human_written' | 0.6999732255935669 |
