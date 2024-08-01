using System;
using System.Threading;
using System.IO;
using System.Formats.Asn1;
using System.Data;
using System.IO.Compression;
using System.Runtime.CompilerServices;

namespace ConsoleApp1
{
    internal class Rect
    {
        public int Width;
        public int Height;

        public Rect(int w, int h)
        {
            this.Width = w;
            this.Height = h;
        }

        public int Area()
        {
            return this.Width * this.Height;
        }
    }

    class ThreeDMatrix
    {
        static void Main()
        {
            
        }
    }
}