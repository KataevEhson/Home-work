from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    context = {
        'name': 'Ehson',
        'age': 14
    }
    return render(request, 'index.html', context)


def winter(request):
    context = {
        'about_winter': """Winter is the coldest season of the year. It comes after autumn and before spring. The days are short, and the nights are long. In many places, snow covers the ground, trees, and houses.

People wear warm coats, hats, scarves, and gloves. Children enjoy playing in the snow, making snowmen, and throwing snowballs. Many people also like skiing, ice skating, and sledding.

During winter, some animals sleep for a long time to save energy. Others look for food or stay in warm shelters. Many trees lose their leaves, but pine trees stay green.

On cold evenings, people enjoy staying at home, drinking hot chocolate, and watching films with their families. Winter is a wonderful season for snowy adventures and cosy moments.""",
    }
    return render(request, 'index1.html', context)


def spring(request):
    info = {
        'about_spring' :"""
Spring is one of the four seasons of the year. It comes after winter and before summer. In spring, the weather gets warmer, and the days become longer. The snow melts, and fresh green grass begins to grow.

Trees get new leaves, and flowers bloom in gardens and parks. We can see many colourful flowers, such as tulips and daffodils. Birds sing and build nests. Bees and butterflies fly from flower to flower.

Spring weather can change quickly. Some days are warm and sunny, while others are cool and rainy. Rain helps plants and trees grow. After the rain, we can sometimes see a beautiful rainbow in the sky.

People enjoy spending time outside in spring. They walk in parks, ride bicycles, play sports, and have picnics with friends and family. Many people also plant flowers and vegetables in their gardens.

Spring is a season of new life, bright colours, and fresh beginnings.
""",
        'author': 'Ehson',
    }
    return render(request, 'index2.html', info)


def summer(request):
    info = {
        'about_summer' : """Summer is the warmest season of the year. It comes after spring and before autumn. The days are long, and the nights are short. The sun shines brightly, and the weather is often hot and sunny.

In summer, trees are full of green leaves, and flowers bloom in gardens. Many fruits and vegetables become ready to eat. People enjoy watermelon, strawberries, cherries, and ice cream.

Children often have a long break from school. They spend time with friends, ride bicycles, and play outside. Many families go on holiday to the beach, the mountains, or the countryside.

Swimming, camping, and having picnics are popular summer activities. On hot days, it is important to drink plenty of water, wear sunscreen, and take breaks in the shade.

Summer is a wonderful season for outdoor adventures, relaxation, and spending time with family and friends.

      """
    
        }
    return render(request, 'index3.html', info)


def autumn(request):
    info = {
        'about_autumn' : """ Autumn comes after summer and before winter. The weather gets cooler, and the days become shorter
        Leaves turn yellow, orange, and red before falling from the trees. People enjoy walks in parks and warm drinks on cool evenings"""
    }
    return render(request, 'index4.html', info)
