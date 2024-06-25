using System;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            System.Console.WriteLine("Hello");
            System.Console.WriteLine("You here?");
            WriteError("Нет соединения", ConsoleColor.DarkRed);
            System.Console.WriteLine("Hmmm...");
            WriteError("Нет соединения с сервером", ConsoleColor.Blue, symbol: '@');
        }


    static void WriteError(string textError, ConsoleColor color = ConsoleColor.Red, char symbol = '!')
    {
        ConsoleColor defaultColor = Console.ForegroundColor;
        Console.ForegroundColor = color;
        System.Console.WriteLine(textError + symbol);
        Console.ForegroundColor = defaultColor;
    }
    }
}