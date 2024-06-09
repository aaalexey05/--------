using System;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main()
        {
            for(int i = 1; i < 5; i++){
                switch(i){
                    case 1:
                        System.Console.WriteLine("В ветви case 1");
                        goto case 3;
                    case 2:
                        System.Console.WriteLine("В ветви case 2");
                        goto case 1;
                    case 3:
                        System.Console.WriteLine("В ветви case 3");
                        goto default;
                    default:
                        System.Console.WriteLine("В ветви default");
                        break;
                }
                System.Console.WriteLine();
            }

        }
    }
}






