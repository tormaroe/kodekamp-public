<Query Kind="Program" />

void Main()
{
	string alphabeth = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ .";
	int columns = 6;
	int rows = 5;
	
	var rnd = new Random();
	for(int row = 0; row < rows; row++)
	{
		for(int digit = 0; digit < columns * 6; digit++)
		{
			if (digit > 0 && digit % 6 == 0)
				Console.Write("-");
			Console.Write(alphabeth[rnd.Next(0, alphabeth.Length)]);
		}
		Console.WriteLine();
	}
}