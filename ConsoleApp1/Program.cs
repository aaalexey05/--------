using System;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main()
        {
            int[,] array3 = new int[4,4];

            Random rand = new Random();
            
            for(int i=0; i<array3.GetLength(0); i++){
                for(int j = 0; j < array3.GetLength(1); j++) {
                    array3[i, j] = rand.Next(0, 101);
                    System.Console.Write(array3[i, j] + " "); 
                }
                System.Console.WriteLine();
            }
        }
    }
}






