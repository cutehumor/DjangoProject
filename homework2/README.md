在本作业中，分别设计了两个模板HTML。

[collect_interests.html](templates/collect_interests.html)

[show_interests.html](templates/show_interests.html)

---

在`collect_interests.html`中，创建了一个标题，用于指示用户在这个表单中输入他们的兴趣爱好，使用`GET`方法提交表单。同时创建了一个文本输入框，用于输入兴趣爱好，`name="interests"`定义了这个输入框的名称，当表单提交时，输入框中的内容将被作为名为`interests` 的GET请求参数发送到服务器。设计了一个提交按钮，用户点击这个按钮后，表单中的数据将被提交到服务器，`value="Submit"` 定义了按钮上显示的文本。

```
<h2>Enter your interests:</h2>
    <form action="{% url 'show_interests' %}" method="get">
        <input type="text" name="interests">
        <br>
        <input type="submit" value="Submit">
    </form>
```

---

在`show_interests.html`中就很简单了，直接显示刚刚收集到的数据就好了。

```
<h2>Your interests:</h2>
    <p>{{ interests }}</p>
```

