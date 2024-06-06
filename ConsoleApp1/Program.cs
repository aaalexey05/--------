using System;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main()
        {
            int[,] array;
            int[,] array2 = new int[2, 3];

            int[,] array3 = {
                {2, 3, 4}, 
                {4, 5, 1}, 
                {7, 8, 9}
                };

            int[,] array4 = new int[2, 3] {
                {9, 8, 7}, 
                {6, 5, 4}};

            System.Console.WriteLine(array4[0,0]);

        }
    }
}






