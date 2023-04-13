from django.shortcuts import render


def test(request):
    return render(request, template_name="main/advertisement.html",
                  context={"title": "Название объявления", "price": 1000, "rating": 5,
                           "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur elementum, libero et interdum faucibus, erat massa consectetur arcu, in viverra mi ligula egestas lectus. Proin id augue eros. Fusce placerat finibus mattis. Ut et ex porttitor, pulvinar nulla ut, vestibulum ex. Nulla vel libero nec justo vestibulum vestibulum non nec odio. Nulla dolor erat, lobortis in nunc vel, cursus vehicula nunc. Aliquam a tellus lacus. Quisque pulvinar aliquam orci eget vehicula.",
                           "phone_number": "+7 323 204 20 20", "email": "hahahahaha@mail.ru"})
