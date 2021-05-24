
import chevron


def test_template():
    # print(chevron.render("this is {{name}}, {{#start}} age is {{value}}{{/start}}",
    #                      data={
    #                          "name": "zhangsan",
    #                          "start": True,
    #                          "value": 18
    #
    #                      }))

    # print(chevron.render("this is {{name}}, {{#start}} age is {{value}}{{/start}}",
    #                      data={
    #                          "name": "zhangsan",
    #                          "start": False,
    #                          "value": 18
    #
    #                      }))

    # print(chevron.render("this is {{name}}, {{#start}} age is {{value}}{{/start}}",
    #                      data={
    #                          "name": "zhangsan",
    #                          "start": [1,2,3],
    #                          "value": 18
    #                      }))

    print(chevron.render("this is {{name}}, {{#start}} age is {{value}}{{/start}}",
                         data={
                             "name": "zhangsan",
                             "start": [{"value": 18}, {"value": 18}, {"value": 18}
                                       ]
                         }))




