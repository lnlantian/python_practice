##BluePrint（蓝图）的概念说白了就是路由组，所有注册到该蓝图上的路由都使用同一个前缀。\
##这样方便了管理，不同的功能可以放在一个模块（比如admin模块）中实现，更加解耦。

# 定义一个蓝图
simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

# 绑定视图函数
@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
        

        # 在主模块中注册路由
app = Flask(__name__)
app.register_blueprint(simple_page)

#### 源码实现分析

1、 调用 blueprint.register()
def register_blueprint(self, blueprint, **options):
   	...	
	blueprint.register(self, options, first_registration)

2、 register 注册
# blueprints.py
def register(self, app, options, first_registration=False):
	
    ...
    state = self.make_setup_state(app, options, first_registration)
    
    ...
    for deferred in self.deferred_functions:   ###deferred_functions 延迟函数
        deferred(state)
3、 返回一个Blue_setup_state类
def make_setup_state(self, app, options, first_registration=False):
    return BlueprintSetupState(self, app, options, first_registration)

##  app.register_blueprint 注册蓝图之后，会激活Buleprint类中的register方法，\
##在register方法中循环调用 deferred_functions 中的函数来执行，这段代码的功能就是将蓝图中定义的路由都添加到路由组中。

4、 继续分析
@simple_page.route('/', defaults={'page': 'index'})

5、 route 装饰器
def route(self, rule, **options):
    def decorator(f):
        self.add_url_rule(rule, f.__name__, f, **options)
        return f
    return decorator

6、route方法是个装饰器，实际上调用了 add_url_rule 方法：
def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
    self.record(lambda s: s.add_url_rule(rule, endpoint, view_func, **options))
        
def record(self, func):
	....
    self.deferred_functions.append(func)
    
    ##在record方法中，将func添加到了deferred_functions列表中，而add_url_rule中调用了record方法
    
7、 
state = self.make_setup_state(app, options, first_registration)    
...
for deferred in self.deferred_functions:
    deferred(state)

8、 def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
    self.app.add_url_rule(rule, '%s.%s' % (self.blueprint.name, endpoint),view_func, defaults=defaults, **options)

9、 state
# state 是 BlueprintSetupState 实例
BlueprintSetupState -> state

# deferred_functions 里面是蓝图路由的lambda
lambda s: s.add_url_rule -> deferred_functions

for deferred in self.deferred_functions:
    deferred(state)
    
意思就是 lambda 中的 s 被赋值为 state ，然后state.add_url_rule,
这样就执行了app.add_url_rule

## 蓝图代码分析链接：https://juejin.im/post/5e36a881518825262f54b3cc
