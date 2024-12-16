

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


/***装备表.xls***/
export interface st_equip_row 
{

	/***装备id***/
	id :number;

	/***装备icon***/
	icon :string;

	/***装备名字***/
	name :string;

	/***装备描述***/
	desc :string;

	/***装备位置
1.武器
2.护甲
3.帽子***/
	pos :number;

	/***装备固定属性***/
	fixedAttr :number[];

	/***白绿蓝紫橙红品质特性0没有
(待定)***/
	quality :number;

	/***随机属性最大个数个数
平均随机***/
	randMaxNum :number;

	/***随机属性池***/
	randPool :number;

	/***枪械baseId
枪械表（待定）***/
	gunBaseId :number;

}


/***装备表.xls***/
export interface st_equip_pool_row 
{

	/***奖池id***/
	id :number;

	/***属性权重
属性id,权重|属性id,权重***/
	weight :number[];

}


/***装备表.xls***/
export interface st_attri_range_row 
{

	/***属性id***/
	id :number;

	/***最大范围***/
	max :number;

	/***最小范围***/
	min :number;

}


/***装备表.xls***/
export interface st_equip_lv_row 
{

	/***等级id***/
	id :number;

	/***消耗(升到下一级)***/
	cost :{itemId:number, itemNum:number}[];

}


/***装备表.xls***/
export interface st_equip_quailty_row 
{

	/***消耗***/
	cost :{itemId:number, itemNum:number}[];

}


/***装备表.xls***/
export interface st_equip_effect_row 
{

	/***品质类型***/
	id :number;

	/***描述***/
	desc :string;

	/***类型
1.属性提升
2.结算金币增加
3.增加无人机***/
	type :number;

	/***参数1***/
	param1 :string;

	/***参数2***/
	param2 :string;

}


