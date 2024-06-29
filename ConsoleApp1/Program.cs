using System;

namespace ConsoleApp1
{
        class Building {
            public int Floors;
            public int Area;
            public int Occupant;
        }

        class DemoBuilding{
            static void Main(){
                Building house = new Building();
                int areaPP;

                house.Occupant = 4;
                house.Area = 2500;
                house.Floors = 2;

                areaPP = house.Area / house.Occupant;

                System.Console.WriteLine("Дом имеет:\n " + 
                house.Floors + " этажа\n  " + 
                house.Occupant + " жильца\n  " + 
                house.Area + " кв. фунтов общей площади, из них\n " + 
                areaPP + " приходится на одного человека");
        }
    }
}
