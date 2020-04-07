import datetime
import json
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

leads = [
{
    "Id": 0,
    "Title": "Template", 
    "Author": "Template", 
    "Date": "1/1/2020",
    "Text": "Loren Ipsum", 
    "LeadCharCount": 11,
    "LeadTypes":
        [
            {
                "Type": "hiddenfact",
                "marked_as_deleted": False
            },
            {
                "Type": "timepeg",
                "marked_as_deleted": False
            },
            {
                "Type": "haveyoueverwondered",
                "marked_as_deleted": False
            },
            {
                "Type": "question",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://images.app.goo.gl/zBZTtEtC91xVoXE76",
    "Link": "Template URL"
},
{
    "Id": 1,
    "Title": "Cool bit of 20th Century urban archaeology",
    "Author": "Mark Wallace",
    "Date": "3/27/2019",
    "Text": "Geeky thread warning. Or, if you’re like me, a cool bit of 20th Century urban archaeology. Check out this shop in Kingston. What’s unusual about it (aside from its no-doubt-excellent nails service)?",
    "LeadCharCount": 198,
    "LeadTypes":
        [
            {
                "Type": "hiddenfact",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://pbs.twimg.com/media/D2p7sn8X0AA2Eyh?format=jpg&name=large",
    "Link": "https://twitter.com/wallaceme/status/1110836282480082944"
},
{
    "Id": 2,
    "Title": "What is a VPN?",
    "Author": "Katy Gero",
    "Date": "4/4/2019",
    "Text": "@alex_calderwoo and I are trying our hand at writing #tweetorials, here's our first one: The recent repeal of #NetNeutrality may have got you wondering-- do you need a #VPN? What even _is_ a VPN? Is it really like a condom for your computer?",
    "LeadCharCount": 243,
    "LeadTypes":
        [
            {
                "Type": "timepeg",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://i.pcmag.com/imagery/articles/06u6ziELpyaxdO8kDuUmPsH-15.fit_scale.size_2698x1517.v1569488323.jpg",
    "Link": "https://twitter.com/katyilonka/status/1113907133882482689"
},
{
    "Id": 3,
    "Title": "Why do my fingers get all wrinkly when I take a bath?", 
    "Author": "Tony Breu", 
    "Date": "7/11/2018",
    "Text": "1/ 'Why do my fingers get all wrinkly when I take a bath?' This was the question my 3-year-old daughter asked me recently after bath time. I thought for a minute, then realized I didn't have a clue. The explanation is so much cooler than I had expected...", 
    "LeadCharCount": 259,
    "LeadTypes":
        [
            {
                "Type": "haveyoueverwondered",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://pbs.twimg.com/media/Dh2_WfPVQAAEtyR?format=jpg&name=4096x4096",
    "Link": "https://twitter.com/tony_breu/status/1017179836320710657"
},
{
    "Id": 4,
    "Title": "Do butterflies remember being caterpillars?", 
    "Author": "Jennifer Harrison", 
    "Date": "8/21/2017",
    "Text": "Do butterflies remember being caterpillars? Someone recently asked me if butterflies remember being caterpillars. We don't know for sure, but here's an intriguing study that suggests they might.", 
    "LeadCharCount": 194,
    "LeadTypes":
        [
            {
                "Type": "haveyoueverwondered",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://media.mnn.com/assets/images/2019/08/caterpillar.jpg.1440x960_q100_crop-scale_upscale.jpg",
    "Link": "https://twitter.com/i/moments/899757563935432706"
},
{
    "Id": 5,
    "Title": "A thread about dung beetles", 
    "Author": "Jennifer Harrison", 
    "Date": "8/15/2017",
    "Text": "A thread about dung beetles. After billions of years of evolution, all living things are pretty spectacular. Someone gave me dung beetles as an example of a rubbish animal. *rolls up sleeves*", 
    "LeadCharCount": 190,
    "LeadTypes":
        [
            {
                "Type": "hiddenfact",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://pbs.twimg.com/media/DHNXhEpXUAIgofy?format=jpg&name=medium",
    "Link": "https://twitter.com/i/moments/899757563935432706"
},
{
    "Id": 6,
    "Title": "what is 'oppo research'?", 
    "Author": "Yashar Ali", 
    "Date": "2/6/2019",
    "Text": "1. All this talk about opposition research tonight is driving me nuts because so many people are getting it wrong (not Kyle). This is an area I know well, I got my training as a oppo researcher many years ago, I have also commissioned, disseminated, and received a ton of research", 
    "LeadCharCount": 280,
    "LeadTypes":
        [
            {
                "Type": "timepeg",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://am13.mediaite.com/med/cnt/uploads/2018/10/GettyImages-1052056706.jpg",
    "Link": "https://twitter.com/yashar/status/1093381319428530176"
},
{
    "Id": 7,
    "Title": "why enterprise software sucks", 
    "Author": "Arvind Narayanan", 
    "Date": "10/11/2019",
    "Text": "My university just announced that it’s dumping Blackboard, and there was much rejoicing. Why is Blackboard universally reviled? There’s a standard story of why 'enterprise software' sucks. If you’ll bear with me, I think this is best appreciated by talking about… baby clothes!", 
    "LeadCharCount": 278,
    "LeadTypes":
        [
            {
                "Type": "haveyoueverwondered",
                "marked_as_deleted": False
            },
            {
                "Type": "timepeg",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://upload.wikimedia.org/wikipedia/commons/6/6c/Blackboard_Logo_StdReg.png",
    "Link": "https://twitter.com/random_walker/status/1182635589604171776"
},
{
    "Id": 8,
    "Title": "how are the fires in California impacted by climate change?", 
    "Author": "Meehan Crist", 
    "Date": "11/21/2019",
    "Text": "I’ve been watched the landscape of my childhood burn with an aching heart, and wondering how much climate change is to blame. Turns out human activity is a major driver of California’s wildfires, but not just in the ways you might imagine. (pic: Noah Berger) 1/10", 
    "LeadCharCount": 263,
    "LeadTypes":
        [
            {
                "Type": "timepeg",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://pbs.twimg.com/media/EJ55WKqWoAg1Ma2?format=jpg&name=900x900",
    "Link": "https://twitter.com/meehancrist/status/1197527975379505152"
},
{
    "Id": 9,
    "Title": "a wacky problem for AI ethicists", 
    "Author": "Jonathan Stray", 
    "Date": "8/29/2019",
    "Text": "THREAD on a wacky problem that AI ethics theorists should be aware of. Consider a coin flip bet: Heads you get 1.5 times your current wealth. Tails you get 0.6. Should you take it? Expected value is 1/2*0.6 + 1/2*1.5 = 1.05 times your wealth. So take it right? Not quite...", 
    "LeadCharCount": 277,
    "LeadTypes":
        [
            {
                "Type": "hiddenfact",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://pbs.twimg.com/media/EDLLc6jUcAICX9X?format=jpg&name=large",
    "Link": "https://twitter.com/jonathanstray/status/1167217965638406144"
},
{
    "Id": 10,
    "Title": "everyone has an accent", 
    "Author": "Kevin B. McGowan", 
    "Date": "3/26/2019",
    "Text": "Sometimes you might hear a linguist like me say 'everyone has an accent' and I think what you probably believe we mean is something like 'everyone but me/you/people like X has an accent'.  That's not it *at all*. 1/", 
    "LeadCharCount": 216,
    "LeadTypes":
        [
            {
                "Type": "hiddenfact",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://www.wikihow.com/images/5/51/Speak-With-a-Bostonian-Accent-Step-10.jpg",
    "Link": "https://twitter.com/kbmcgowan/status/1110549232229011456"
},
{
    "Id": 11,
    "Title": "steroids and white blood cell counts", 
    "Author": "Tony Breu", 
    "Date": "10/20/2018",
    "Text": "1/ How do steroids cause an increase in the white blood cell (WBC) count (i.e., leukocytosis)? And, how do steroids tamp down inflammation if it appears that there are more WBCs in the blood after they are administered? Seems like a paradox in need of a thread.", 
    "LeadCharCount": 264,
    "LeadTypes":
        [
            {
                "Type": "question",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://pbs.twimg.com/media/Dp6TTtNUUAICljt?format=jpg&name=large",
    "Link": "https://twitter.com/tony_breu/status/1053671032140251136"
},
{
    "Id": 12,
    "Title": "the relativity of simultaneity", 
    "Author": "Jennifer Harrison", 
    "Date": "8/19/2017",
    "Text": "Time is relative. Lunchtime doubly so. Here's an explainer on a phenomenon that shook my entire understanding of the universe. It has bad drawings.", 
    "LeadCharCount": 147,
    "LeadTypes":
        [
            {
                "Type": "hiddenfact",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://pbs.twimg.com/media/DHlcjZiXgAARxYn?format=jpg&name=4096x4096",
    "Link": "https://twitter.com/i/moments/899752815391801346"
},
{
    "Id": 13,
    "Title": "Are your friends more popular than you", 
    "Author": "Ana-Andreea S", 
    "Date": "1/1/2020",
    "Text": "Are your friends more popular than you? If you check out your Twitter friends, you might find out that, on average, they have more friends than you! Don’t worry---this is the Friendship Paradox... (1/n)", 
    "LeadCharCount": 11,
    "LeadTypes":
        [
            {
                "Type": "haveyoueverwondered",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://miro.medium.com/max/2408/0*8T9WFQKlf147X7FE.jpg",
    "Link": "Template URL"
},
{
    "Id": 14,
    "Title": "What deep sea mud could reveal about climate change", 
    "Author": "Ingrid", 
    "Date": "1/1/2020",
    "Text": "Deep sea mud could reveal the future of climate change - Here’s how:", 
    "LeadCharCount": 11,
    "LeadTypes":
        [
            {
                "Type": "simplestatement",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://joybileefarm.com/wp-content/uploads/2014/01/Dead-Sea-Mud.jpg",
    "Link": "Template URL"
},
{
    "Id": 15,
    "Title": "Hurricane Sandy Remembrance", 
    "Author": "Jonathan L", 
    "Date": "10/1/2020",
    "Text": "On this anniversary of Sandy, let’s look back: Sandy was one of only # NYC hurricanes during the last century. This is below average for the last millennium. Does this mean climate change isn’t affecting hurricanes? And does it matter how many hurricanes we had 500 years ago?", 
    "LeadCharCount": 11,
    "LeadTypes":
        [
            {
                "Type": "timepeg",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Sandy_Oct_25_2012_0320Z.png",
    "Link": "Template URL"
},
{
    "Id": 16,
    "Title": "Animal Responses", 
    "Author": "Adam J Calhoun", 
    "Date": "7/3/2019",
    "Text": "Animals will respond differently to the same inputs when they are hungry/sated, attentive/bored, etc. But how do we know what state the animal is in? In this preprint with @jpillowtime @MurthyLab, we show how you can do that automatically! 👇", 
    "LeadCharCount": 241,
    "LeadTypes":
        [
            {
                "Type": "haveyoueverwondered",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://pbs.twimg.com/media/D-judCUWsAAUvQV?format=png&name=900x900",
    "Link": "https://twitter.com/neuroecology/status/1146428513920126976"
},
{
    "Id": 17,
    "Title": "Too much money in politics", 
    "Author": "Juan C", 
    "Date": "10/1/2020",
    "Text": "By and large, Americans agree that there’s too much money in politics. Most likely, over $2 billion will be spent on the 2020 presidential election. Short of passing legislation (which right now seems infeasible), is there anything we can do about this? I think we can! (THREAD)", 
    "LeadCharCount": 11,
    "LeadTypes":
        [
            {
                "Type": "hiddenfact",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://www.livingroomconversations.org/wp-content/uploads/2018/09/money_in_politics.jpg",
    "Link": "Template URL"
},
{
    "Id": 18,
    "Title": "Why should you confess your feelings?", 
    "Author": "Arianna V", 
    "Date": "10/1/2020",
    "Text": "Why should you confess your feelings to the one you love? There is a science behind. NOTE: this is actually the lead tweet for the first draft. I decided to use this one because I thought it was more effective at drawing me in. For reference, here's the revised lead: When you finally get a chance to sit with your loved one at a romantic bar, would you hope Cupid to launch his golden arrow? If so, you should set up the bow by confessing your feelings first, as there is a science behind.", 
    "LeadCharCount": 11,
    "LeadTypes":
        [
            {
                "Type": "haveyoueverwondered",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://miro.medium.com/max/5400/1*VcHVCyRSAOF3V6Ldi0iXOQ.jpeg",
    "Link": "Template URL"
},
{
    "Id": 19,
    "Title": "Boulders in Central Park", 
    "Author": "Carly P", 
    "Date": "10/1/2020",
    "Text": "Did you know that there are boulders in central park from Canada? Who brought them here? Turns out, glaciers did. Only about 20 thousand years ago New York was under a mile thick of ice because... ", 
    "LeadCharCount": 11,
    "LeadTypes":
        [
            {
                "Type": "haveyoueverwondered",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://i.redd.it/g4qg63e21fc21.jpg",
    "Link": "Template URL"
},
{
    "Id": 20,
    "Title": "Air pollution in India", 
    "Author": "Emily F", 
    "Date": "10/1/2020",
    "Text": "I’m sure you’ve heard a lot about air pollution in India in the news. Most people know that air pollution is bad. But why is it so bad for our health?", 
    "LeadCharCount": 11,
    "LeadTypes":
        [
            {
                "Type": "hiddenfact",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://www.aljazeera.com/mritems/Images/2019/6/11/07cec803024a4b458764328abb33d4fc_18.jpg",
    "Link": "Template URL"
},
{
    "Id": 21,
    "Title": "Organism survivng in deep freeze", 
    "Author": "Dr. Jacquelyn Gill", 
    "Date": "7/9/2019",
    "Text": "Okay, so: I was understandably incredulous to read this. 41,000 years is unheard of in terms of an organism surviving deep freeze, by orders of magnitude. So, I went to the source.", 
    "LeadCharCount": 180,
    "LeadTypes":
        [
            {
                "Type": "hiddenfact",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://ichef.bbci.co.uk/news/976/cpsprodpb/125E3/production/_93553257_ap_fox.jpg",
    "Link": "https://twitter.com/JacquelynGill/status/1148770899065266176"
},
{
    "Id": 22,
    "Title": "Why Johnson was impeached", 
    "Author": "Michael Harriot", 
    "Date": "12/11/2019",
    "Text": "Everyone's talking about impeachment and Clinton & Johnson as the only presidents ever impeached. But most people don't know WHY Johnson was impeached. So let me tell you the story about how not impeaching a racist president is a BIG reason why white supremacy lingers in America", 
    "LeadCharCount": 278,
    "LeadTypes":
        [
            {
                "Type": "haveyoueverwondered",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://cdn.britannica.com/43/78243-050-F9B7D2BD/Lyndon-B-Johnson-1963.jpg",
    "Link": "https://twitter.com/michaelharriot/status/1204924987100073984"
},
{
    "Id": 23,
    "Title": "Animations", 
    "Author": "Henrique M", 
    "Date": "10/1/2020",
    "Text": "POLL: Which of the following animations looks real? POLL: Now, which would you expect to see in the movies or cartoons?", 
    "LeadCharCount": 11,
    "LeadTypes":
        [
            {
                "Type": "poll",
                "marked_as_deleted": False
            },
            {
                "Type": "hiddenfact",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://smartslider3.com/wp-content/uploads/2017/12/animatedslider-780x410.png",
    "Link": "Template URL"
},
{
    "Id": 24,
    "Title": "Puzzle", 
    "Author": "Laura G", 
    "Date": "10/1/2020",
    "Text": "Imagine two olympic sized swimming pools connected by...a paper towel tube. Now imagine you start to heat one pool. What happens to the other?", 
    "LeadCharCount": 11,
    "LeadTypes":
        [
            {
                "Type": "hiddenfact",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://www.liveabout.com/thmb/hQYsUyZZvgMrDwIjTmZqEXafiyE=/2667x2000/smart/filters:no_upscale()/RioOlympicsswimmingpool-GettyImages-519838356-59c09963054ad90011cf5247.jpg",
    "Link": "Template URL"
},
{
    "Id": 25,
    "Title": "Memory Safety", 
    "Author": "Mohamed H", 
    "Date": "10/1/2020",
    "Text": "The lack of memory safety is a very serious problem. Why do we think so? Thread 1/n", 
    "LeadCharCount": 11,
    "LeadTypes":
        [
            {
                "Type": "haveyoueverwondered",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://i.ytimg.com/vi/P5BVSGse454/maxresdefault.jpg",
    "Link": "Template URL"
},
{
    "Id": 26,
    "Title": "Why pre-ordering books is important", 
    "Author": "Andrea Bartz", 
    "Date": "11/5/2019",
    "Text": "You have probably heard me stating that preordering a book from an independent bookseller is the most impactful thing you can do if you're going to buy an author's book. Lately some of you wonderful people have asked for more detail, so I thought I'd explain! [THREAD]", 
    "LeadCharCount": 267,
    "LeadTypes":
        [
            {
                "Type": "timpeg",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://elearningindustry.com/wp-content/uploads/2016/05/top-10-books-every-college-student-read-e1464023124869.jpeg",
    "Link": "https://twitter.com/andibartz/status/1191786513476079616"
},
{
    "Id": 27,
    "Title": "Why college rankings are bullshit", 
    "Author": "herr_naphta", 
    "Date": "11/6/2019",
    "Text": "Jesus Christ this is dark: colleges buy low-scoring SAT names from the College Board, and then *encourage students to apply knowing they will reject them* to boost their selectivity rating. One of a million kinds of perfectly legal ways poor people are fucked over every day.", 
    "LeadCharCount": 275,
    "LeadTypes":
        [
            {
                "Type": "simplestatement",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://snworksceo.imgix.net/dtc/a7ed8659-b35b-4b9a-a962-a9c27b635503.sized-1000x1000.jpg?w=1000",
    "Link": "https://www.wsj.com/articles/for-sale-sat-takers-names-colleges-buy-student-data-and-boost-exclusivity-11572976621?width=10&height=5"
},
{
    "Id": 28,
    "Title": "Death row story with options", 
    "Author": "ProPublica", 
    "Date": "10/1/2020",
    "Text": "In FL, a man sits on death row. He could be executed as early as Jan. 2020. The key witness in his case is a con artist, convicted child predator and “jailhouse snitch” named Paul Skalnik — who’s offered info on 40+ defendants. Would you believe him? Let’s review the evidence:", 
    "LeadCharCount": 279,
    "LeadTypes":
        [
            {
                "Type": "haveyoueverwondered",
                "marked_as_deleted": False
            },
            {
                "Type": "hiddenfact",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://dmn-dallas-news-prod.cdn.arcpublishing.com/resizer/FjbxoYZpExrSQ_oUFn0qUWf0Sco=/1660x934/smart/filters:no_upscale()/arc-anglerfish-arc2-prod-dmn.s3.amazonaws.com/public/ZUJTE6EABJFS5NBHZHI7XHWW2A.JPG",
    "Link": "Template URL"
},
{
    "Id": 29,
    "Title": "Why washing your hands works", 
    "Author": "Karen Fleming", 
    "Date": "2/28/2020",
    "Text": "PSA for non-science folks: Wonder why everyone is emphasizing hand washing? Sounds banal, but soap really IS an amazing weapon that we all have in our homes. This is because coronavirus is an 'enveloped' virus, which means that it has an outer lipid membrane layer. 1/3", 
    "LeadCharCount": 270,
    "LeadTypes":
        [
            {
                "Type": "haveyoueverwondered",
                "marked_as_deleted": False
            },
            {
                "Type": "hiddenfact",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://thenypost.files.wordpress.com/2020/02/coronavirus-hands-wash.jpg?quality=80&strip=all",
    "Link": "https://twitter.com/KarenFlemingPhD/status/1233451607385202688"
},
{
    "Id": 30,
    "Title": "Pink ponds in SF Bay", 
    "Author": "Christina Toms", 
    "Date": "11/27/2019",
    "Text": "Flight attendant: 'What are those weird pink ponds in San Francisco Bay?' Me: *crashes up the aisle and grabs the loudspeaker microphone* 'SO TIDAL WETLANDS IN THE BAY FORMED ROUGHLY 2 TO 5 THOUSAND YEARS AGO AS POST-ICE AGE RATES OF SEA LEVEL RISE SLOWED AND STABILIZED...'", 
    "LeadCharCount": 275,
    "LeadTypes":
        [
            {
                "Type": "haveyoueverwondered",
                "marked_as_deleted": False
            },
            {
                "Type": "humor",
                "marked_as_deleted": False
            }
        ],
    "Image": "https://pbs.twimg.com/media/EKeBuGbU0AAVCs-?format=jpg&name=large",
    "Link": "https://twitter.com/ChristinaToms/status/1199909280184356866",
}
]

filtered = []

def searchforword(arr, searchWord):
    searchWord = searchWord.lower()
    for key in arr:
        if searchWord in key["Title"].lower() or searchWord in key["Text"].lower() or searchWord in key["Author"].lower() or searchWord in key["LeadTypes"][0] or searchWord in key["LeadTypes"]:
            filtered.append(key)
    
    return filtered

@app.route('/')
def search():
    return render_template('searchpage.html', leads=leads) 

@app.route('/searchbykeyword', methods=['GET', 'POST'])
def searchbykeyword():
    filtered.clear()
    searchword = request.get_json()
    searchforword(leads, searchword)
    return jsonify(filtered=filtered)

@app.route('/getthismany', methods=['GET', 'POST'])
def gethismany():
    filtered.clear()
    num = request.get_json()
    first = int(len(leads))-(num-1)
    last = int(len(leads))-1
    for x in range(first, last):
        filtered.append(leads[x])

    return jsonify(filtered=filtered)

@app.route('/view/<id>', methods=['GET', 'POST'])
def view(id):
    tweet = leads[int(id)]
    return render_template('templatepage.html', tweet=tweet)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/createtweet', methods=['GET', 'POST'])
def createtweet():
    newtweet = request.get_json()
    length = len(leads)
    newtweet["Id"] = length
    leads.append(newtweet)
    link = "view/" + str(length)
    return jsonify(link=link)

#@app.route('/edit/<id>', methods=['GET', 'POST'])
#def edit(id):
    #title = leads[int(id)]["Title"]
    #print("392")
    #return render_template('editpage.html', id=id)

@app.route('/edit_Title', methods=['GET','POST'])
def edit_Title():
    data = request.get_json()
    title = data[0]
    index = data[1]
    leads[int(index)]["Title"] = title
    #print(leads[int(index)])
    return jsonify('')

@app.route('/edit_Author', methods=['GET','POST'])
def edit_Lead():
    data = request.get_json()
    author = data[0]
    index = data[1]
    leads[int(index)]["Author"] = author
    #print(leads[int(index)])
    return jsonify('')

#@app.route('/deleteitem', methods=['GET', 'POST'])
#def deleteitem():
#    id = request.get_json()
#    leads.remove(leads[int(id)])
#    if len(leads) != 0:
#        for x in range(0, len(leads)):
#            leads[x]["Id"] = x
#    else:
#        print("there are no more entries left! please add some")   
#    return jsonify(leads=leads)

@app.route('/deleteleadtype', methods=['GET', 'POST'])
def deleteleadtype():
    content = request.get_json()
    index = content[0]
    id = content[1]
    leads[id]["LeadTypes"][int(index)]["marked_as_deleted"] = True
    return jsonify('')

@app.route('/undodeleteleadtype', methods=['GET', 'POST'])
def undodeleteleadtype():
    content = request.get_json()
    index = content[0]
    id = content[1]
    leads[id]["LeadTypes"][int(index)]["marked_as_deleted"] = False
    typetoreturn = leads[id]["LeadTypes"][int(index)]["Type"]
    return jsonify(typetoreturn = typetoreturn)

@app.route('/getnondeleted', methods=['GET', 'POST'])
def getnondeleted():
    index = request.get_json()
    result = leads[index]["LeadTypes"]
    return jsonify(result=result)

def savetweets():
    ts = datetime.datetime.now().timestamp()
    o = "./backup/" + repr(ts) + ".txt"
    out_file = open(o, "w")
    out_file.write(json.dumps(leads))
    out_file.close()
    
if __name__ == '__main__':
   app.run(debug = True)
