# Veracia Eval Report — Veritarach cross-model generalization

Dataset: 100 case(s)

## Summary

| Metric | Value |
| --- | --- |
| confusion_matrix | {'tp': 62, 'fp': 0, 'tn': 0, 'fn': 38} |
| precision | 1.0 |
| recall | 0.62 |
| f1 | 0.7654320987654321 |
| false_positive_rate | 0.0 |
| accuracy | 0.62 |
| baseline_accuracy | 0.5106382978723404 |
| accuracy_delta | 0.10936170212765961 |

## Failures (worst 10)

| Input | Expected | Actual | Confidence |
| --- | --- | --- | --- |
| 'To support monarch butterfly migration, consider planting milkweed in your garden, as this is their ...' | 'ai_generated' | 'human_written' | 0.5088624358177185 |
| 'Beneath the gleaming surface of the sleek, high-tech device lay the heart of its power: a small, cyl...' | 'ai_generated' | 'human_written' | 0.5528717637062073 |
| 'Leaves change color in autumn due to the reduction of chlorophyll production in response to shorter ...' | 'ai_generated' | 'human_written' | 0.6438797116279602 |
| 'Weather refers to short-term atmospheric conditions at a specific place and time, including variable...' | 'ai_generated' | 'human_written' | 0.7220152616500854 |
| 'A thermostat regulates temperature through a simple yet effective mechanism. Located in your heating...' | 'ai_generated' | 'human_written' | 0.7434774041175842 |
| 'In the quiet hum of the Smith household, the thermostat sat silently in the wall, an unassuming sent...' | 'ai_generated' | 'human_written' | 0.823290228843689 |
| 'A lighthouse functions as a navigational aid, guiding mariners safely through treacherous coastal wa...' | 'ai_generated' | 'human_written' | 0.8275513052940369 |
| 'Hey there! So, you’ve ever wondered why bread rises when you bake it? It all has to do with yeast, t...' | 'ai_generated' | 'human_written' | 0.8684216141700745 |
| 'In the bustling city, where honking horns and chattering crowds drowned out serenity, Max sought ref...' | 'ai_generated' | 'human_written' | 0.8788111805915833 |
| 'In the small coastal town of Bayview, Clara watched as the brisk autumn air turned to a balmy summer...' | 'ai_generated' | 'human_written' | 0.9209885001182556 |

## Full Results

| Input | Expected | Actual | Confidence |
| --- | --- | --- | --- |
| 'The history of tea dates back thousands of years, originating in ancient China around 2737 BCE. Empe...' | 'ai_generated' | 'ai_generated' | 0.9707021713256836 |
| "Hey there! Ever wondered about tea's story? Tea's been around since the ancient Chinese dynasties, b..." | 'ai_generated' | 'human_written' | 0.9896384477615356 |
| 'In ancient China, legend whispers of Emperor Shen Nong, who chanced upon a mystical leaf falling int...' | 'ai_generated' | 'human_written' | 0.9962299466133118 |
| 'Sure, here are a few practical tips related to the history of tea:\n\n1. **Explore Different Types**: ...' | 'ai_generated' | 'ai_generated' | 0.9999871253967285 |
| "Originating in ancient China around 2737 BC, tea's journey began with Emperor Shen Nong who discover..." | 'ai_generated' | 'ai_generated' | 0.9691916704177856 |
| 'Bicycles maintain balance through a combination of rider input, wheel geometry, and physical forces....' | 'ai_generated' | 'human_written' | 0.9946473240852356 |
| "Hey there!\n\nEver wondered how bikes stay upright while you pedal? It's all about balance! Here's the..." | 'ai_generated' | 'ai_generated' | 0.9971168041229248 |
| 'Beneath the gentle sway of the willow tree, Mia balanced her bicycle on the cobblestone path, feelin...' | 'ai_generated' | 'ai_generated' | 0.9996507167816162 |
| 'Bicycles maintain balance while moving through a combination of several mechanisms:\n\n1. **Center of ...' | 'ai_generated' | 'ai_generated' | 0.999987006187439 |
| 'Cyclists adeptly maintain balance while moving through a combination of skilled maneuvers and inhere...' | 'ai_generated' | 'human_written' | 0.9948073029518127 |
| 'Leaves change color in autumn due to the reduction of chlorophyll production in the fall season. As ...' | 'ai_generated' | 'human_written' | 0.9827554821968079 |
| 'Hey there! Ever wonder why leaves turn all sorts of colors in the fall? It’s all thanks to some clev...' | 'ai_generated' | 'ai_generated' | 0.9998339414596558 |
| 'In the heart of Maplewood Forest, leaves once green now donned shades of amber, gold, and crimson, a...' | 'ai_generated' | 'ai_generated' | 0.9956845045089722 |
| 'Leaves change color in autumn due to the reduction of chlorophyll production in response to shorter ...' | 'ai_generated' | 'human_written' | 0.6438797116279602 |
| 'As autumn arrives, leaves undergo a stunning transformation. This natural phenomenon is driven by th...' | 'ai_generated' | 'ai_generated' | 0.9995487332344055 |
| 'Weather refers to the short-term conditions of the atmosphere at a specific time and place, includin...' | 'ai_generated' | 'human_written' | 0.97095787525177 |
| 'Hey there! Quick note on weather vs climate. Weather is what you experience day-to-day, like sunshin...' | 'ai_generated' | 'human_written' | 0.9998890161514282 |
| 'In the small coastal town of Bayview, Clara watched as the brisk autumn air turned to a balmy summer...' | 'ai_generated' | 'human_written' | 0.9209885001182556 |
| 'Understanding the difference between weather and climate is crucial for various fields. Here are a f...' | 'ai_generated' | 'ai_generated' | 0.9999814033508301 |
| 'Weather refers to short-term atmospheric conditions at a specific place and time, including variable...' | 'ai_generated' | 'human_written' | 0.7220152616500854 |
| 'A lighthouse functions as a navigational aid, guiding mariners safely through treacherous coastal wa...' | 'ai_generated' | 'human_written' | 0.8275513052940369 |
| "Hey there!\n\nSo, you've ever wondered how a lighthouse works? It's pretty cool! Basically, it uses a ..." | 'ai_generated' | 'ai_generated' | 0.9997753500938416 |
| 'High atop a jagged cliff stood the lighthouse, its beacon a steadfast sentinel against the restless ...' | 'ai_generated' | 'ai_generated' | 0.9970032572746277 |
| 'A lighthouse functions to guide ships safely by emitting a bright light visible over long distances....' | 'ai_generated' | 'ai_generated' | 0.9999864101409912 |
| 'Lighthouses serve as a beacon of hope and guidance for sailors navigating treacherous waters. At the...' | 'ai_generated' | 'human_written' | 0.9651514291763306 |
| 'The invention of the printing press, attributed to Johannes Gutenberg in the mid-15th century, revol...' | 'ai_generated' | 'ai_generated' | 0.9950122237205505 |
| 'Hey there! So, have you ever wondered who invented the printing press? Well, it was Johannes Gutenbe...' | 'ai_generated' | 'ai_generated' | 0.9997223019599915 |
| 'In the dim glow of his workshop, Johannes Gutenberg hunched over a wooden block, carving not merely ...' | 'ai_generated' | 'human_written' | 0.9498687386512756 |
| 'The invention of the printing press by Johannes Gutenberg in the 15th century revolutionized the dis...' | 'ai_generated' | 'ai_generated' | 0.9999822378158569 |
| 'In the mid-15th century, Johannes Gutenberg revolutionized the spread of knowledge with the inventio...' | 'ai_generated' | 'ai_generated' | 0.8956960439682007 |
| 'Bread rises due to the fermentation process induced by yeast, a type of fungus. When yeast is added ...' | 'ai_generated' | 'ai_generated' | 0.9995561242103577 |
| 'Hey there! So, you’ve ever wondered why bread rises when you bake it? It all has to do with yeast, t...' | 'ai_generated' | 'human_written' | 0.8684216141700745 |
| 'In the quiet corner of an old bakery, Sarah watched with childlike wonder as the dough slowly transf...' | 'ai_generated' | 'ai_generated' | 0.9997518658638 |
| 'Bread rises due to the action of yeast. Here are a few practical tips to help your bread rise effect...' | 'ai_generated' | 'ai_generated' | 0.9999872446060181 |
| 'Bread rises due to yeast fermentation, a process transforming dough into fluffy loaves. Yeast, a sin...' | 'ai_generated' | 'human_written' | 0.9984326958656311 |
| 'Noise-cancelling headphones utilize active noise control technology to reduce unwanted ambient sound...' | 'ai_generated' | 'ai_generated' | 0.9998388290405273 |
| "Hey there! Ever wonder how noise-cancelling headphones magically block out the world's sounds? It al..." | 'ai_generated' | 'ai_generated' | 0.9866999387741089 |
| 'In the bustling city, where honking horns and chattering crowds drowned out serenity, Max sought ref...' | 'ai_generated' | 'human_written' | 0.8788111805915833 |
| '1. **Active Noise Control:** Noise-cancelling headphones use microphones to pick up ambient sounds, ...' | 'ai_generated' | 'ai_generated' | 0.9999879598617554 |
| 'Innovations in personal audio technology have led to the development of noise-cancelling headphones....' | 'ai_generated' | 'ai_generated' | 0.9991856217384338 |
| 'Monarch butterflies (Danaus plexippus) are renowned for their extraordinary migration patterns, one ...' | 'ai_generated' | 'human_written' | 0.9764269590377808 |
| 'Hey there! Just wanted to share a fascinating bit about monarch butterflies. These incredible little...' | 'ai_generated' | 'ai_generated' | 0.9957284331321716 |
| 'The air buzzed with a peculiar warmth as thousands of monarch butterflies unfurled their wings again...' | 'ai_generated' | 'human_written' | 0.9407777190208435 |
| 'To support monarch butterfly migration, consider planting milkweed in your garden, as this is their ...' | 'ai_generated' | 'human_written' | 0.5088624358177185 |
| 'Monarch butterflies, known for their remarkable annual migration, traverse thousands of miles from N...' | 'ai_generated' | 'ai_generated' | 0.9996976852416992 |
| 'A thermostat regulates temperature through a feedback loop mechanism. Inside the thermostat, a senso...' | 'ai_generated' | 'human_written' | 0.9944919347763062 |
| 'Hey there! 🛋️ Ever wondered how a thermostat keeps your room cozy or cool? It’s all about balancing ...' | 'ai_generated' | 'ai_generated' | 0.9883455038070679 |
| 'In the quiet hum of the Smith household, the thermostat sat silently in the wall, an unassuming sent...' | 'ai_generated' | 'human_written' | 0.823290228843689 |
| 'A thermostat regulates temperature by maintaining a desired setpoint through a feedback loop. Here a...' | 'ai_generated' | 'ai_generated' | 0.9999837875366211 |
| 'A thermostat regulates temperature through a simple yet effective mechanism. Located in your heating...' | 'ai_generated' | 'human_written' | 0.7434774041175842 |
| 'Chess is a strategic board game with a history that dates back to the 6th century in India. Known in...' | 'ai_generated' | 'ai_generated' | 0.9999196529388428 |
| "Hey! Did you know chess has such an ancient origin? It's believed to have started in India around 6t..." | 'ai_generated' | 'ai_generated' | 0.9986603260040283 |
| 'In the ancient Indian subcontinent, beneath the shadowed banyan tree of a wise sage named Dhanna, th...' | 'ai_generated' | 'human_written' | 0.9927916526794434 |
| 'Sure! Here are a few practical tips related to the origin of chess:\n\n1. **Historical Research:** Del...' | 'ai_generated' | 'ai_generated' | 0.9999874830245972 |
| 'Originating in the 6th century in India, chess began as a game called Chaturanga. Its name evolved a...' | 'ai_generated' | 'ai_generated' | 0.8564285635948181 |
| "The sky appears blue due to Rayleigh scattering, which occurs when sunlight enters Earth's atmospher..." | 'ai_generated' | 'ai_generated' | 0.9997640252113342 |
| "Hey there! So, why is the sky blue? It's all about light and tiny particles in the air. Sunlight loo..." | 'ai_generated' | 'ai_generated' | 0.9996016621589661 |
| 'The azure expanse above stretched endlessly, its cerulean hue a comforting blanket of peace. On this...' | 'ai_generated' | 'ai_generated' | 0.9528117775917053 |
| 'Sure! Here are a few practical tips to understand why the sky is blue:\n\n1. **Rayleigh Scattering**: ...' | 'ai_generated' | 'ai_generated' | 0.9999876022338867 |
| "Sky's Blue Explained: The sky appears blue due to Rayleigh scattering. As sunlight passes through Ea..." | 'ai_generated' | 'ai_generated' | 0.9977360963821411 |
| 'Composting is a natural process that transforms organic waste into nutrient-rich soil amendment. In ...' | 'ai_generated' | 'ai_generated' | 0.9957369565963745 |
| 'Hey there! 🌿 Ever wondered what happens to kitchen scraps and yard waste in your compost bin? Compos...' | 'ai_generated' | 'ai_generated' | 0.9993528723716736 |
| 'In the tranquil town of Evergreen, nestled beneath the golden canopy, there thrived a hidden world b...' | 'ai_generated' | 'human_written' | 0.9855002760887146 |
| 'Composting is a natural process that breaks down organic materials into rich soil. Here are a few pr...' | 'ai_generated' | 'ai_generated' | 0.9997835755348206 |
| 'Compost is a rich, nutrient-filled organic material produced through the natural decay of plant and ...' | 'ai_generated' | 'ai_generated' | 0.9995958209037781 |
| 'The bicycle, a pivotal mode of personal transportation, emerged in the 19th century. Its invention i...' | 'ai_generated' | 'human_written' | 0.999910831451416 |
| 'Hey there! Did you know that the bicycle has been around for quite a while? It all started back in t...' | 'ai_generated' | 'human_written' | 0.9937263131141663 |
| 'Beneath the cobblestone streets of 19th-century Paris, whispers spoke of an invention that would rev...' | 'ai_generated' | 'human_written' | 0.9905188679695129 |
| '1. **Understand its origins**: The first crude bicycle, called the "Draisine" or "running machine," ...' | 'ai_generated' | 'ai_generated' | 0.9999856948852539 |
| 'The bicycle, an iconic mode of transport, traces its roots back to the 1817 "Draisine" or "Running m...' | 'ai_generated' | 'human_written' | 0.9921513795852661 |
| 'Tides are the rhythmic rise and fall of sea levels caused primarily by the gravitational pull of the...' | 'ai_generated' | 'human_written' | 0.9773001670837402 |
| "Hey! 🌕 Did you know tides happen because of the moon? Well, it's all about gravity. The moon pulls o..." | 'ai_generated' | 'human_written' | 0.990422248840332 |
| 'Beneath the silvery glow of the moon, the sea whispered secrets to the shore. Waves danced rhythmica...' | 'ai_generated' | 'human_written' | 0.9842239618301392 |
| 'Understanding tides caused by the moon involves recognizing several key principles. Firstly, remembe...' | 'ai_generated' | 'human_written' | 0.961389422416687 |
| "Recent observations confirm that the Moon's gravitational pull is the primary force behind Earth's t..." | 'ai_generated' | 'human_written' | 0.982393741607666 |
| 'Cats purr for various reasons that are largely beneficial to their health and well-being. Primarily,...' | 'ai_generated' | 'ai_generated' | 0.9999432563781738 |
| "Hey there!\n\nEver wonder why cats purr? Well, it's pretty cool. Cats purr for a bunch of reasons. Som..." | 'ai_generated' | 'ai_generated' | 0.9999632835388184 |
| 'Whiskers twitched against the soft velvet of an old armchair as Luna, the gentle giant of the househ...' | 'ai_generated' | 'ai_generated' | 0.9994797110557556 |
| 'Cats purr for a variety of reasons, often related to their comfort and well-being. Here are some pra...' | 'ai_generated' | 'ai_generated' | 0.9999879598617554 |
| 'Cats purr for various reasons, both beneficial and mysterious. Primarily, purring occurs when cats f...' | 'ai_generated' | 'ai_generated' | 0.9917652010917664 |
| 'A battery stores energy through electrochemical processes involving chemical reactions between its c...' | 'ai_generated' | 'ai_generated' | 0.999066174030304 |
| 'Hey there! So, how a battery stores energy is pretty cool. Think of it like a tiny battery factory. ...' | 'ai_generated' | 'ai_generated' | 0.996147632598877 |
| 'Beneath the gleaming surface of the sleek, high-tech device lay the heart of its power: a small, cyl...' | 'ai_generated' | 'human_written' | 0.5528717637062073 |
| 'A battery stores energy through chemical reactions between its components, typically involving a pos...' | 'ai_generated' | 'ai_generated' | 0.9999876022338867 |
| 'A battery stores energy through electrochemical reactions between its components. Inside a battery, ...' | 'ai_generated' | 'ai_generated' | 0.9965938925743103 |
| 'Bread-making in a bakery begins with mixing ingredients like flour, water, yeast, and salt. This mix...' | 'ai_generated' | 'ai_generated' | 0.995298445224762 |
| 'Hey there! 🍞 Just wanted to share the cool steps we take to make fresh bread in the bakery. First, w...' | 'ai_generated' | 'human_written' | 0.9977906942367554 |
| 'In the heart of downtown, the warm glow of "Bread & Butter" bakery welcomed patrons into its cozy em...' | 'ai_generated' | 'ai_generated' | 0.9936113953590393 |
| '1. **Kneading**: Flour, water, yeast, and salt are mixed together. The dough is kneaded to develop g...' | 'ai_generated' | 'ai_generated' | 0.9999899864196777 |
| 'Bread-making in a bakery is a process rooted in tradition but guided by modern techniques. Bakers be...' | 'ai_generated' | 'ai_generated' | 0.7203114032745361 |
| "Coffee's history dates back to ancient Ethiopia, where legend has it that a goat herder named Kaldi ..." | 'ai_generated' | 'human_written' | 0.9574493169784546 |
| 'Hey there! So, coffee has a fascinating history. It all started in ancient Ethiopia where legend say...' | 'ai_generated' | 'ai_generated' | 0.9971004128456116 |
| 'In the shadowy corners of ancient Yemen, a mysterious bean thrummed with vitality, a divine secret p...' | 'ai_generated' | 'human_written' | 0.9861722588539124 |
| '1. **Explore Historical Origins**: Coffee’s journey began in ancient Ethiopia around 850 AD, where l...' | 'ai_generated' | 'ai_generated' | 0.9999785423278809 |
| 'Coffee, a beloved global beverage, traces its origins back to Ethiopia in the 9th century, where leg...' | 'ai_generated' | 'human_written' | 0.9814358353614807 |
| 'A violin produces sound through the vibration of its strings. When a player draws a bow across these...' | 'ai_generated' | 'ai_generated' | 0.9999285936355591 |
| "Hey there! So, here's how a violin makes its magic: It's all about the strings, right? When you pluc..." | 'ai_generated' | 'ai_generated' | 0.996557354927063 |
| 'Amidst the quiet hum of an ancient library, a lone violin rested upon a mahogany stand, its glossy f...' | 'ai_generated' | 'ai_generated' | 0.9990639090538025 |
| '1. Pluck the strings: Sound production starts when you pluck the strings with your fingers. The stri...' | 'ai_generated' | 'ai_generated' | 0.9998117089271545 |
| 'A violin produces sound through the vibration of its strings when plucked or bowed. The strings are ...' | 'ai_generated' | 'ai_generated' | 0.9998476505279541 |
