using System;
using System.Threading;
using System.IO;
using System.Formats.Asn1;
using System.Data;
using System.IO.Compression;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main()
        {
            int[] numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
            int sum = 0;

            System.Console.Write("Numbers: ");
            for(int i = 0; i < numbers.Length; i++)
            {
                System.Console.Write(numbers[i] + " ");
                sum += i;
            }
            System.Console.WriteLine($"\nSum = {sum}");
        }

    }
}

