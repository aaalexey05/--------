using System;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main()
        {
            bool isOpen = true;
           string [,] books = {
            {"Александ Пушкин", "Михаил Лермонтов", "Сергей Есенин"},
            {"Роберт Мартин", "Джесси Шелл", "Сергей Тепляков"},
            {"Стивен Кинг", "Говард Лавкрафт", "Брем Стокер"}
           };
        
            while (isOpen)
            {
                System.Console.WriteLine("\nВесь список авторов:\n");
                for (int i = 0; i < books.GetLength(0); i++)
                {
                    for(int j = 0; j < books.GetLength(1); j++)
                    {
                        System.Console.Write(books[i,j] + " | ");
                    }
                    System.Console.WriteLine();
                }

                System.Console.WriteLine("\nБиблиотека");
                System.Console.WriteLine("\n1 - узнать имя автора по индексу книги.\n\n2 - найти книгу по автору.\n\n3 - выйти из программы");
                System.Console.Write("\nВыберите пункт меню: ");

                switch(Convert.ToInt32(Console.ReadLine())){
                    case 1:
                        int line, column;
                        System.Console.WriteLine("Введите номер полки: ");
                        line = Convert.ToInt32(Console.ReadLine()) - 1;
                        System.Console.WriteLine("Введите номер столбца: ");
                        column = Convert.ToInt32(Console.ReadLine()) - 1;
                        System.Console.WriteLine("Это автор " + books[line, column]);
                        break;
                    case 2:
                        string author;
                        System.Console.Write("Введите автора: ");
                        author = Console.ReadLine();
                        for (int i = 0; i < books.GetLength(0); i++)
                        {
                            for (int j = 0; j < books.GetLength(1); j++)
                            {
                                if (author == books[i, j])
                                {
                                    System.Console.Write($"Автор {books[i ,j]} находится по адресу: полка {i + 1}, место {j + 1}.");
                                }
                            }
                        }
                        break;
                    case 3:
                        isOpen = false;
                        break;
                    default:
                        System.Console.WriteLine("Ошибка! Данный пункт отсутсвует в программе, попробуйте снова!");
                        break;
                }

                if(isOpen)
                {
                    System.Console.WriteLine("\nНажмите любую клавишу для продолжения...");
                }
                Console.ReadKey();
                System.Console.Clear();
            }

        }

    }
}







