using System;

namespace RzutUkośny
{
    public class Physics
    {
        private double dt = 0.01;
        private int gx = 0;
        private int gy = -10;
        private double k = 0.5;
        private double scale = 3;
        
        private Object O = new Object()
        {
            Vpx = 10,
            Vpy = 10,
            Sx = 0,
            Sy = 0,
            M = 50
        };
        
        private double DVy;
        private double Vy;
        private double Vya;
        private double DSy;
        private double Sy; 
        
        private double DVx;
        private double Vx;
        private double Vxa;
        private double DSx;
        private double Sx;

        private void FillArray(string[,] array)
        {
            for (int i = 0; i < array.GetLength(0); i++)
            {
                for (int j = 0; j < array.GetLength(1); j++)
                {
                    array[i, j] = " ";
                }
            }
        }

        private double EulerImprovedMethodSx(int counter)
        {
            if (counter == 0)
            {
                Vx += O.Vpx;
                Vxa = Vx + gx * dt / 2;
                DSx = Vxa * dt;
                Sx = O.Sx;
                return 0;
            }
            DVx = gx * dt;
            Vx += DVx;
            Vxa = Vx + gx * dt / 2;
            Sx += DSx;
            DSx = Vxa * dt;
            return Sx*scale;
        }
        private double EulerImprovedMethodSy(int counter)
        {
            if (counter == 0)
            {
                Vy += O.Vpy;
                Vya = Vy + gy * dt / 2;
                DSy = Vya * dt;
                Sy = O.Sy;
                return 0;
            }
            DVy = gy * dt;
            Vy += DVy;
            Vya = Vy + gy * dt / 2;
            Sy += DSy;
            DSy = Vya * dt;
            return Sy*scale;
        }

        private double EulerMethodSy(int counter)
        {
            if (counter == 0)
            {
                Vy += O.Vpy;
                DSy = Vy * dt;
                Sy = O.Sy;
                return 0;
            }
            DVy = gy * dt;
            Vy += DVy;
            Sy += DSy;
            DSy = Vy * dt;
            return Sy*scale;
        }
        
        private double EulerMethodSx(int counter)
        {
            if (counter == 0)
            {
                Vx += O.Vpx;
                DSx = Vx * dt;
                Sx = O.Sx;
                return 0;
            }
            DVx = gx * dt;
            Vx += DVx;
            Sx += DSx;
            DSx = Vx * dt;
            return Sx*scale;
        }

        public void DrawGraph(string[,] graph)
        {
            FillArray(graph);
            double time = 0;
            
            int counter = 0;
            while (time <= 2)
            {
                graph[16 -(int)EulerImprovedMethodSy(counter), 60 -(int)EulerImprovedMethodSx(counter)] = "*";
                //graph[(int)Math.Round(EulerMethodSy(counter), MidpointRounding.AwayFromZero), (int)Math.Round(EulerMethodSx(counter), MidpointRounding.AwayFromZero)] = "*";
                time += dt;
                counter++;
            }
            time = 0;
            counter = 0;
            Sx = 0;
            Sy = 0;
            Vx = 0;
            Vy = 0;
            DSx = 0;
            DSy = 0;
            DVx = 0;
            DVy = 0;

            while (time <= 2)
            {
                graph[16 -(int)EulerMethodSy(counter), 130 -(int)EulerMethodSx(counter)] = "*";
                time += dt;
                counter++;
            }

            for (int i = 0; i < graph.GetLength(0); i++)
            {
                for (int j = 0; j < graph.GetLength(1); j++)
                {
                    Console.Write(graph[i, j]);
                }
                Console.WriteLine();
            }
        }
    }
}