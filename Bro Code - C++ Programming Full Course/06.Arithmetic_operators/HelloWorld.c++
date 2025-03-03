#include <iostream>

int main()
{
    // arithmetic operators = return the result of a specific
    //                        arithmetic operation (+ - * /)

    //parenthesis
    //multiplication & division
    //addition & subtraction

    int students = 20;
    int alunos;
    alunos = 6 - (5 + 4) * 3 / 2;

    //students = students + 1;
    //students+=1;
    students++;

    //students = students - 1;
    //students-=1;
    students--;

    //students = students / 3;
    students/=3;

    int remainder = students % 2;

    std::cout << students << '\n';
    std::cout << alunos << '\n';

    return 0;
}