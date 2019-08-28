package main

import (
	"go/ast"
	"go/parser"
	"go/token"
	"log"
	"os"
)

func main() {
	if len(os.Args) < 2 {
		log.Printf("Usage:\n\t./main filename\n")
		return
	}
	filename := os.Args[1]
	fset := token.NewFileSet()
	node, err := parser.ParseFile(fset, filename, nil, parser.ParseComments)
	if err != nil {
		log.Fatal(err)
	}
	for _, v := range node.Imports {
		log.Printf("value:%s\n", v.Path.Value)
	}
	log.Printf("comments:\n")
	for _, v := range node.Comments {
		log.Printf("comments:%s\n", v.Text())
	}

	log.Printf("functions:\n")
	for _, v := range node.Decls {
		if fn, ok := v.(*ast.FuncDecl); ok {
			log.Printf("function name:%s\n", fn.Name.Name)
		}
	}

	ast.Inspect(node, func(n ast.Node) bool {
		fn, ok := n.(*ast.FuncDecl)
		if !ok {
			return true
		}
		log.Printf("function is exported, function name:%s, position:%v, line:%d, filename:%s\n",
			fn.Name.Name, fset.Position(fn.Pos()), fset.Position(fn.Pos()).Line, fset.Position(fn.Pos()).Filename)
		return true
	})
}

func test() {
	return
}
