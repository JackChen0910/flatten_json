import copy

# 没有考虑同一级dict内含有多个list的情况
# 默认list内都是dict
class JsonParser:
    # class JsonDickParser:
    #     def __init__(self):

    def __init__(self):
        self._sep = '_'
        pass

    # 在dict中与到嵌套dict
    # prefix为key的名称
    # 直接接触嵌套
    # data: key:value
    #       value可能为list,dict,和普通值
    def dict2dict(self, prefix, data):
        result_dict = {}
        for k in data:
            result_dict[prefix + self._sep + k] = data[k]
        return result_dict

    # 在dict中与到嵌套list
    # prefix为前置最近一个dict的非list信息
    # 复制多行dict，将list元素放置
    # data 必定为list,内部元素必定为dict
    def dict2list(self, prefix, data):
        result_list = []
        for i in data:
            i_d = {}
            for k in i:
                i_d[prefix + self._sep + k] = i[k]
            result_list.append(i_d)
        return result_list

    # json_data 必定为list
    # 返回值 list
    def parse_forward(self, json_data):
        assert type(json_data) == list
        stop = 1  # 没有嵌套的dict和list就停下来
        result = []
        while stop == 1:
            stop = 0  # 初始化
            for json_data_i in json_data:  # 检查每一行数据
                assert type(json_data_i) == dict
                list_key = None
                for i in list(json_data_i):  # 对于一行数据的每一个key:value
                    if type(json_data_i[i]) == dict:  # 如果value是一个dict
                        stop = 1  # 继续
                        d = self.dict2dict(i, json_data_i[i])  # dict中含有dict
                        json_data_i.pop(i)
                        json_data_i.update(d)
                    elif type(json_data_i[i]) == list:  # 如果value是一个list
                        list_key = i  # 记录下来，先不操作，保证每一个属性的key已经改过了
                        stop = 1  # 继续
                    else:
                        # 是一个普通的数据，不用处理
                        pass
                # 如果这行数据已经没有任何list,直接保存
                if list_key is None:
                    result.append(copy.deepcopy(json_data_i))
                # 检查完所有的key:value，再对列表操作，保证每一个属性的key已经改过了
                else:
                    l = self.dict2list(list_key, json_data_i[list_key])
                    json_data_i.pop(list_key)
                    for data in l:
                        r = copy.deepcopy(json_data_i)
                        r.update(data)
                        result.append(r)
            json_data = result
            result = []
        return json_data

