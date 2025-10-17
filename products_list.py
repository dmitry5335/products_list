from http.server import BaseHTTPRequestHandler, HTTPServer

cars = {
    1: ['Лада Веста', '750000', 'Надежный седан для повседневных поездок'],
    2: ['Hyundai Solaris', '950000', 'Популярный автомобиль с хорошей комплектацией'],
    3: ['Kia Rio', '920000', 'Стильный городской автомобиль с экономичным расходом'],
    4: ['Volkswagen Polo', '1100000', 'Немецкое качество и комфорт'],
    5: ['Toyota Camry', '2500000', 'Представительский седан бизнес-класса']
}

site_title = "<h1>Автосалон</h1>"

class MyCarDealershipHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path

        if path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            response = site_title
            response += "<h2>Наши автомобили:</h2>"
            response += "<ul>"
            for car_id, car_info in cars.items():
                response += f'<li><a href="/car/{car_id}">{car_info[0]}</a></li>'
            response += "</ul>"

            self.wfile.write(response.encode('utf-8'))

        elif path.startswith('/car/'):
            try:
                car_id_str = path[len('/car/'):]
                car_id = int(car_id_str)
                if car_id in cars:
                    car_info = cars[car_id]
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html; charset=utf-8')
                    self.end_headers()

                    response = f"<h1>{car_info[0]}</h1>"
                    response += f"<p>Цена: {car_info[1]} руб.</p>"
                    response += f"<p>Описание: {car_info[2]}</p>"
                    response += '<p><a href="/">Назад к списку автомобилей</a></p>'

                    self.wfile.write(response.encode('utf-8'))
                else:
                    self.send_error(404, "Автомобиль не найден")
            except ValueError:
                self.send_error(400, "Неверный ID автомобиля")
        else:
            self.send_error(404, "Страница не найдена")  


def run(http_server=HTTPServer, handler=BaseHTTPRequestHandler):
    httpd = http_server(('', 8000), handler)
    print("Сервер запущен на http://localhost:8000")
    httpd.serve_forever()

if __name__ == "__main__":
    run(HTTPServer, MyCarDealershipHandler)