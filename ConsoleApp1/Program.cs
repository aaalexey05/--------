using System;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main()
        {
            for(int i = 0; i <= 3; i++) {
                System.Console.WriteLine("Подсчёт во внешнем цикле: " + i);
                System.Console.Write("Подсчёт во внутреннем цикле: ");

                int t = 0;
                while(t < 100) {
                    if (t == 10) break;
                    System.Console.Write(t + " ");
                    t++;
                }
                System.Console.WriteLine();
            }
            System.Console.WriteLine("Все циклы завершены.");
        }
    }
}





