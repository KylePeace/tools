

/***st_test.xls***/
export interface st_test_row 
{

	/***id***/
	id :number;

	/***des***/
	title :string;

	/***int类型***/
	option :number;

	/***测试list***/
	test_list :any[];

	/***测试int_list2***/
	test_int_list2 :number[];

	/***测试str_list***/
	test_str_list :string[];

	/***测试item***/
	test_item :{itemId:number, itemNum:number};

	/***测试item_list***/
	test_item_list :{itemId:number, itemNum:number}[];

	/***测试float***/
	test_float :number;

	/***测试float_list***/
	test_float_list :number[];

	/***测试test_str***/
	test_str :string;

	/***测试int_list***/
	test_int_list :number[];

	/***int二维数组***/
	test_int_list_list :number[];

	/***str二维数组***/
	str_list_list :string[];

}


