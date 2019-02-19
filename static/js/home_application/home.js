var student_data = []

var mytable=$('#table')





mytable.bootstrapTable({
    //striped: true,          // 显示条纹表格
   // pagination: true,       // 显示表格分页组件
   // pageList: [1, 3, 5],    // 设置每页显示数据条数框
    //pageSize: 3,            // 页面默认每页显示数据条数
    //pageNumber: 1,          // 设置首页页码
    columns: [{
        field: 'id',
        title: '主键id',
        align: 'center',
        visible: false
    },{
        field: 'stuId',
        title: '学号',
        align: 'center',

    }, {
        field: 'name',
        title: '姓名',
        align: 'center',

    }, {
        field: 'age',
        title: '年龄',
        align: 'center',

    },{
        field: 'gender',
        title: '性别',
        align: 'center',

    },{
        field: 'operation',
        title: '操作',
        formatter: btnGroup,    //自定义方法，添加按钮组
        events: {               //注册按钮组事件

            'click #editUser': function (event, value, row, index) {
                $("#aaa").val(row.id)
                $("#bbb").val(row.stuId)
                $("#ccc").val(row.name)
                $("#ddd").val(row.age)
                $("#eee").val(row.gender)

            },
            'click #delUser': function (event, value, row, index) {
                alert(row.id)
            }
        }
    }


    ]
})

function btnGroup() {   //自定义方法，添加操作按钮
    let html ="<button data-toggle=\"modal\" data-target=\"#myModal\" id='editUser' class='king-btn king-warning' style='cursor: pointer;'>编辑</button>&emsp;" +
                        "<button id='delUser' class='king-btn king-danger' style='cursor: pointer;'>删除</button>"

    return html;
};


function search_student() {
    var name_info = $("#nameid").val();
    $.post(site_url + 'search_student/', {
        'name_info': name_info
    }, function (res) {
        if (res.result) {
            console.log(res.student)
            mytable.bootstrapTable('load',res.student);  //根据Json动态加载Table
        }
    }, 'json');

}
