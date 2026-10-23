from django.templatetags.static import static
# App/context_processors.py

def global_context(request):
    """
    Single optimized context processor that merges all global data
    instead of loading 100+ small processors.
    """


# features data

    features = [
        {
            'icon' : 'ri-stack-line', 
            'title' : 'Scalability',
            'desc' : 'One disadvantage of Lorum Ipsum is that in Latin frequently than others',
            'class' : 'bg-slate-50 dark:bg-slate-800 lg:order-1 md:order-1 order-1',
            'data' : '.1s',
        },
        {
            'icon' : 'ri-hourglass-line', 
            'title' : 'Time Efficiency',
            'desc' : 'One disadvantage of Lorum Ipsum is that in Latin frequently than others',
            'class' : 'bg-white dark:bg-slate-900 lg:order-2 md:order-2 order-2',
            'data' : '.2s',
        },
        {
            'icon' : 'ri-git-merge-line', 
            'title' : 'Live Collaboration',
            'desc' : 'One disadvantage of Lorum Ipsum is that in Latin frequently than others',
            'class' : 'bg-slate-50 dark:bg-slate-800 lg:order-3 md:order-4 order-3',
            'data' : '.3s',
        },
        {
            'icon' : 'ri-stackshare-line', 
            'title' : 'Secure Sharing',
            'desc' : 'One disadvantage of Lorum Ipsum is that in Latin frequently than others',
            'class' : 'bg-white dark:bg-slate-900 lg:order-4 md:order-3 order-4',
            'data' : '.4s',
        },
        {
            'icon' : 'ri-smartphone-line', 
            'title' : 'Mobile-friendly',
            'desc' : 'One disadvantage of Lorum Ipsum is that in Latin frequently than others',
            'class' : 'bg-slate-50 dark:bg-slate-800 lg:order-6 md:order-5 order-5',
            'data' : '.5s',
        },
        {
            'icon' : 'ri-file-edit-line', 
            'title' : 'Editor Auto-completion',
            'desc' : 'One disadvantage of Lorum Ipsum is that in Latin frequently than others',
            'class' : 'bg-white dark:bg-slate-900 lg:order-5 md:order-6 order-6',
            'data' : '.6s',
        },
        {
            'icon' : 'ri-merge-cells-horizontal', 
            'title' : 'Smart Integrations',
            'desc' : 'One disadvantage of Lorum Ipsum is that in Latin frequently than others',
            'class' : 'bg-slate-50 dark:bg-slate-800 lg:order-8 md:order-8 order-7',
            'data' : '.7s',
        },
        {
            'icon' : 'ri-bar-chart-box-ai-line', 
            'title' : 'Higher Conversion Rate',
            'desc' : 'One disadvantage of Lorum Ipsum is that in Latin frequently than others',
            'class' : 'bg-white dark:bg-slate-900 lg:order-7 md:order-7 order-8',
            'data' : '.8s',
        }
    ]


# portfolios data

    portfolios = [
        {
            'id' : 1,
            'img' : static('app/images/portfolio/1.jpg'), 
            'title' : 'Mockup Collection',
            'name' : 'Abstract',
            'groups' : '["branding"]',
            'data' : '.1s',
        },
        {
            'id' : 2,
            'img' : static('app/images/portfolio/2.jpg'), 
            'title' : 'Iphone mockup',
            'name' : 'Abstract',
            'groups' : '["designing"]',
            'data' : '.2s',
        },
        {
            'id' : 3,
            'img' : static('app/images/portfolio/3.jpg'), 
            'title' : 'Abstract images',
            'name' : 'Abstract',
            'groups' : '["photography"]',
            'data' : '.3s',
        },
        {
            'id' : 4,
            'img' : static('app/images/portfolio/4.jpg'), 
            'title' : 'Yellow bg with Books',
            'name' : 'Abstract',
            'groups' : '["development"]',
            'data' : '.4s',
        },
        {
            'id' : 5,
            'img' : static('app/images/portfolio/5.jpg'), 
            'title' : 'Company V-card',
            'name' : 'Abstract',
            'groups' : '["branding"]',
            'data' : '.5s',
        },
        {
            'id' : 6,
            'img' : static('app/images/portfolio/6.jpg'), 
            'title' : 'Coffee cup',
            'name' : 'Abstract',
            'groups' : '["branding"]',
            'data' : '.6s',
        },
        {
            'id' : 7,
            'img' : static('app/images/portfolio/7.jpg'), 
            'title' : 'Deep Sea Phantasy',
            'name' : 'Abstract',
            'groups' : '["development"]',
            'data' : '.7s',
        },
        {
            'id' : 8,
            'img' : static('app/images/portfolio/8.jpg'), 
            'title' : 'Color Abstract Painting',
            'name' : 'Abstract',
            'groups' : '["branding"]',
            'data' : '.8s',
        },
        {
            'id' : 9,
            'img' : static('app/images/portfolio/9.jpg'), 
            'title' : 'Liquid Forest Princess',
            'name' : 'Abstract',
            'groups' : '["branding"]',
            'data' : '.9s',
        }
    ]


# partners data

    partners = [
        {
            'img' : static('app/images/client/Amazon.svg'), 
            'data' : '.1s',
        },
        {
            'img' : static('app/images/client/Behance.svg'), 
            'data' : '.2s',
        },
        {
            'img' : static('app/images/client/ClickUp.svg'), 
            'data' : '.3s',
        },
        {
            'img' : static('app/images/client/Deezer.svg'), 
            'data' : '.4s',
        },
        {
            'img' : static('app/images/client/Evernote.svg'), 
            'data' : '.5s',
        },
        {
            'img' : static('app/images/client/Grammarly.svg'), 
            'data' : '.6s',
        },
        {
            'img' : static('app/images/client/google-ad.svg'), 
            'data' : '.7s',
        },
        {
            'img' : static('app/images/client/Asana.svg'), 
            'data' : '.8s',
        },
        {
            'img' : static('app/images/client/BeReal.svg'), 
            'data' : '.9s',
        },
        {
            'img' : static('app/images/client/Copper.svg'), 
            'data' : '1s',
        }
    ]


# reviews data

    reviews = [
        {
            'img' : static('app/images/client/01.jpg'), 
            'name' : 'Thomas Israel',
            'title' : 'User',
            'desc' : "I didn't know a thing about icon design until I read this book. Now I can create any icon I need in no time. Great resource!",
        },
        {
            'img' : static('app/images/client/02.jpg'), 
            'name' : 'Carli Oliver',
            'title' : 'User',
            'desc' : "The best part about this template is every time I pay my employees, my bank balance doesn't go down like it used to. Looking forward to spending this extra cash when I figure out why my card is being declined.",
        },
        {
            'img' : static('app/images/client/03.jpg'), 
            'name' : 'Barbara McIntosh',
            'title' : 'User',
            'desc' : "I used to have to remit tax to the EU and with this template I somehow don't have to do that anymore. Nervous to travel there now though.",
        },
        {
            'img' : static('app/images/client/04.jpg'), 
            'name' : 'Jill Webb',
            'title' : 'User',
            'desc' : "I'm trying to get a hold of someone in support, I'm in a lot of trouble right now and they are saying it has something to do with my books. Please get back to me right away.",
        },
        {
            'img' : static('app/images/client/05.jpg'), 
            'name' : 'Janisha Doll',
            'title' : 'User',
            'desc' : "There are so many things I had to do with my old software that I just don't do at all with this template. Suspicious but I can't say I don't love it.",
        },
        {
            'img' : static('app/images/client/06.jpg'), 
            'name' : 'Calvin Carlo',
            'title' : 'User',
            'desc' : "This is the fourth email I've sent to your support team. I am literally being held in jail for tax fraud. Please answer your damn emails, this is important.",
        }
    ]


# counters data

    counters = [
        {
            'icon' : 'ri-service-line',
            'target' : '1548',
            'number' : '1010',
            'symbol' : '+',
            'title' : 'Happy Clients',
            'data' : '.1s',
        },
        {
            'icon' : 'ri-earth-line',
            'target' : '12',
            'number' : '2',
            'symbol' : '+',
            'title' : 'Countries',
            'data' : '.2s',
        },
        {
            'icon' : 'ri-time-line',
            'target' : '145',
            'number' : '0',
            'symbol' : 'K',
            'title' : 'Hours',
            'data' : '.3s',
        },
        {
            'icon' : 'ri-group-2-line',
            'target' : '8',
            'number' : '0',
            'symbol' : '+',
            'title' : 'Team Members',
            'data' : '.4s',
        }
    ]


# blogs data

    blogs = [
        {
            'id' : 1,
            'img' : static('app/images/blogs/1.jpg'), 
            'title' : 'Design your apps in your own way',
            'desc' : 'The phrasal sequence of the is now so that many campaign and benefit',
            'data' : '.1s',
        },
        {
            'id' : 2,
            'img' : static('app/images/blogs/2.jpg'), 
            'title' : 'How apps is changing the IT world',
            'desc' : 'The phrasal sequence of the is now so that many campaign and benefit',
            'data' : '.2s',
        },
        {
            'id' : 3,
            'img' : static('app/images/blogs/3.jpg'), 
            'title' : 'Smartest Applications for Business',
            'desc' : 'The phrasal sequence of the is now so that many campaign and benefit',
            'data' : '.3s',
        },
        {
            'id' : 4,
            'img' : static('app/images/blogs/4.jpg'), 
            'title' : 'Mobile Marketing, Its Synthes and 2027 Offer Prognosis',
            'desc' : 'The phrasal sequence of the is now so that many campaign and benefit',
            'data' : '.4s',
        },
        {
            'id' : 5,
            'img' : static('app/images/blogs/5.jpg'), 
            'title' : 'Stop Worrying About Deadlines! We Got You Covered',
            'desc' : 'The phrasal sequence of the is now so that many campaign and benefit',
            'data' : '.5s',
        },
        {
            'id' : 6,
            'img' : static('app/images/blogs/6.jpg'), 
            'title' : 'Change Your Strategy: Find a Business Consultant',
            'desc' : 'The phrasal sequence of the is now so that many campaign and benefit',
            'data' : '.6s',
        },
        {
            'id' : 7,
            'img' : static('app/images/blogs/7.jpg'), 
            'title' : 'Everything About Financial Modeling',
            'desc' : 'The phrasal sequence of the is now so that many campaign and benefit',
            'data' : '.7s',
        },
        {
            'id' : 8,
            'img' : static('app/images/blogs/8.jpg'), 
            'title' : 'On the other hand we provide denounce',
            'desc' : 'The phrasal sequence of the is now so that many campaign and benefit',
            'data' : '.8s',
        },
        {
            'id' : 9,
            'img' : static('app/images/blogs/9.jpg'), 
            'title' : 'Organization of accounting at the enterprise',
            'desc' : 'The phrasal sequence of the is now so that many campaign and benefit',
            'data' : '.9s',
        }
    ]


# posts data

    posts = [
        {
            'img' : static('app/images/blogs/6.jpg'), 
            'title' : 'Consultant Business',
            'date' : '11th September 2027',
        },
        {
            'img' : static('app/images/blogs/7.jpg'), 
            'title' : 'Grow Your Business',
            'date' : '11th September 2027',
        },
        {
            'img' : static('app/images/blogs/8.jpg'), 
            'title' : 'Look On The Glorious Balance',
            'date' : '11th September 2027',
        }
    ]


# teams data

    teams = [
        {
            'img' : static('app/images/client/01.jpg'),  
            'name' : 'Ramon Gibson',
            'title' : 'C.E.O.',
            'data' : '.1s',
        },
        {
            'img' : static('app/images/client/02.jpg'),  
            'name' : 'Megan Cade',
            'title' : 'Engineer',
            'data' : '.2s',
        },
        {
            'img' : static('app/images/client/03.jpg'),  
            'name' : 'Stella Robinson',
            'title' : 'Engineer',
            'data' : '.3s',
        },
        {
            'img' : static('app/images/client/04.jpg'),  
            'name' : 'Paul Phelan',
            'title' : 'Engineer',
            'data' : '.4s',
        },
        {
            'img' : static('app/images/client/05.jpg'),  
            'name' : 'Nancy Hall',
            'title' : 'Engineer',
            'data' : '.5s',
        },
        {
            'img' : static('app/images/client/06.jpg'),  
            'name' : 'Wendy Buckley',
            'title' : 'Engineer',
            'data' : '.6s',
        },
        {
            'img' : static('app/images/client/07.jpg'),  
            'name' : 'Wendy Buckley',
            'title' : 'Engineer',
            'data' : '.7s',
        },
        {
            'img' : static('app/images/client/08.jpg'),  
            'name' : 'Wendy Buckley',
            'title' : 'Engineer',
            'data' : '.8s',
        }
    ]


    return {
        "features": features,
        "portfolios": portfolios,
        "partners": partners,
        "reviews": reviews,
        "counters": counters,
        "blogs": blogs,
        "posts": posts,
        "teams": teams,
    }


def site_config(request):
    """
    Provides site-wide configuration like site name, copyright info.
    """
    return {
        'site_name': 'Pixind',
        'copyright_year': 2026,
    }


def brand_settings(request):
    """
    Injects the singleton BrandSettings into every template as `brand`.
    """
    from .models import BrandSettings
    return {"brand": BrandSettings.load()}