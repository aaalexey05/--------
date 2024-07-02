using System;
using System.Threading;
using System.IO;
using System.Formats.Asn1;
using System.Data;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main()
        {

        }

        class Building
        {
            public int Floors;  //количество этажей
            public int Area;  //общая площадь здания
            public int Occupants;  //количество жильцов
        }

        class BuildingDemo
        {
            static void Maim()
            {
                Building house = new Building();
                Building office = new Building();

                int areaPP;

                house.Occupants = 4;
                house.Area = 2500;
                house.Floors = 2;

                office.Occupants = 25;
                office.Area = 4200;
                office.Floors = 3;

                areaPP = house.Area / house.Occupants;

                System.Console.WriteLine("Дом имеет:\n " +
                                        house.Floors + " этажа/n " +
                                        house.Occupants + " жильца\n " +
                                        house.Area + " кв. фунтов общей площади,из них\n " +
                                        areaPP + " приходится на одного человека");

                areaPP = office.Area / office.Occupants;
                System.Console.WriteLine("Офис имеет:\n " +
                                        office.Floors + " этажа/n " +
                                        office.Occupants + " жильца\n " +
                                        office.Area + " кв. фунтов общей площади,из них\n " +
                                        areaPP + " приходится на одного человека");
            }
        }
    }
}
