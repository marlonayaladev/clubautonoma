#include <iostream>

//namespace = haces un espacio como def en python donde puedes reutilizar las variables
//siempre fuera del main

namespace primero
{
    int x=888888;
} 


int main() {
    using namespace primero; //usando namespace, ya no es necesario llevarlo
    using std::cout; //usando cout, ya no es necesario escribir "std:: cout <<", porque ya lo estas usando

/*pongo double porque cuando se quiere cambiar el numero directamente desde el code y cambia el numero por un 
decimal, agarra el decimal, pero si lo pones como int no agarra el decimal solo el numero entero 
double es mejor que float al mostrar mas decimales*/
    double a = 1.5;
    double b = 2;
    double c = 3;

    double resultado = a+b+c;

//booleanos ("bool")

    bool falso = false;
    bool verdadero = true;

//string para letras 

    std::string nombre = "Marlon";

//COUT -> mostrar algo en pantalla
    std::cout << resultado << std::endl;
    std::cout << nombre << std::endl;
    std::cout << "X en el namespace es -> " << primero::x;
   

    return 0;
}