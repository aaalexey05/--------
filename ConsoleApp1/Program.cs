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
        static void Main(string[] args)
        {
            Table[] tables = {new Table(1, 4), new Table(2, 3), new Table(3, 10)};
        }
    }

    class Table
    {
        public int Number;
        public int MaxPlaces;
        public int FreePlaces;


        public Table(int number, int maxPlaces)
        {
            Number = number;
            MaxPlaces = maxPlaces;
            FreePlaces = maxPlaces;
        }

        public void ShowInfo(){
            System.Console.WriteLine($"Стол: {Number}. Свободно мест: {FreePlaces} из {MaxPlaces}.");
        }
    }
}
