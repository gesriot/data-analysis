package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strconv"

	"github.com/360EntSecGroup-Skylar/excelize"
)

func main() {
	root := os.Args[1]  // путь к папке передается аргументом командной строки
	err := filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		if !info.IsDir() && filepath.Base(path) == "weights_B.xlsx" {
			xlFile, err := excelize.OpenFile(path)
			if err != nil {
				fmt.Printf("Не удалось открыть файл: %v\n", err)
				return err
			}

			cells := []string{"AG371", "AH371", "AI371"}
			for _, cell := range cells {
				value := xlFile.GetCellValue("Sheet1", cell)
				_, err := strconv.ParseFloat(value, 64)
				if err != nil {
					fmt.Printf("Ошибка в файле %s: значение ячейки %s не является числом\n", path, cell)
					return nil
				}
				fmt.Printf("%s\t", value)
			}
			fmt.Println()
		}
		return nil
	})

	if err != nil {
		fmt.Printf("Ошибка при обходе директории: %v\n", err)
	}
}
