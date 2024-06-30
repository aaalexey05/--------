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
            bool isOpen = true;

            Table[] tables = {new Table(1, 3), new Table(2, 4), new Table(3, 10)};
        
            while(isOpen)
            {
                System.Console.WriteLine("Администрирование кафе.\n");

                for(int i = 0; i < tables.Length; i++){
                    tables[i].ShowInfo();
                }
                    
                System.Console.Write("\nВведите номер стола: ");
                int wishTable = Convert.ToInt32(Console.ReadLine()) - 1;
                System.Console.Write("\nВведите количество мест для брони: ");
                int disaredPlaces = Convert.ToInt32(Console.ReadLine());


                bool isReservationCompleted = tables[wishTable].Reserve(disaredPlaces);

                if(isReservationCompleted)
                {
                    System.Console.WriteLine("Бронь прошла успешно!");
                }
                else
                {
                    System.Console.WriteLine("Бронь не прошла. Недостаточно мест.");
                }

                System.Console.ReadKey();
                Console.Clear();
            }
        }
    }

    class Table{
        public int Number;
        public int MaxPlaces;
        public int FreePlaces;

        public Table(int number, int maxPlaces){
            Number = number;
            MaxPlaces = maxPlaces;
            FreePlaces = maxPlaces;
        }

        public void ShowInfo(){
            System.Console.WriteLine($"Стол: {Number}. Свободно мест: {FreePlaces} из {MaxPlaces}");
        }

        public bool Reserve(int places)
        {
            if(FreePlaces >= places)
            {
                FreePlaces -= places;
                return true;
            }
            else
            {
                return false;
            }
        }
    }
}
