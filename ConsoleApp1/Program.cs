using System;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main()
        {
            int i;
            for(i = -5; i <= 5; i++) {
                System.Console.Write($"Check {i} :");

                if(i < 0) System.Console.WriteLine("-n");
                else System.Console.WriteLine("+n");
            }
        }
    }
}





