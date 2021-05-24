{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template\n",
    "from flask_pymongo import PyMongo\n",
    "import scrape_mars"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mission_to_mars\"\n",
    "mongo = PyMongo(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\")\n",
    "def index():\n",
    "    mars_info_dict = mongo.db.mars_info_dict.find_one()\n",
    "    return render_template(\"index.html\", mars_info_dict=mars_info_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "    mars_info_dict = scrape_mars.scrape()\n",
    "    mongo.db.mars_info_dict.update({}, mars_info_dict, upsert=True)\n",
    "    return redirect(\"/\", code=302)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [24/May/2021 17:15:25] \"\u001b[35m\u001b[1mGET / HTTP/1.1\u001b[0m\" 500 -\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 2464, in __call__\n",
      "    return self.wsgi_app(environ, start_response)\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 2450, in wsgi_app\n",
      "    response = self.handle_exception(e)\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 1867, in handle_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 2447, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 1952, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 1821, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 1950, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 1936, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"<ipython-input-19-2b231701e662>\", line 4, in index\n",
      "    \n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\templating.py\", line 138, in render_template\n",
      "    ctx.app.jinja_env.get_or_select_template(template_name_or_list),\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\jinja2\\environment.py\", line 930, in get_or_select_template\n",
      "    return self.get_template(template_name_or_list, parent, globals)\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\jinja2\\environment.py\", line 883, in get_template\n",
      "    return self._load_template(name, self.make_globals(globals))\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\jinja2\\environment.py\", line 857, in _load_template\n",
      "    template = self.loader.load(self, name, globals)\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\jinja2\\loaders.py\", line 115, in load\n",
      "    source, filename, uptodate = self.get_source(environment, name)\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\templating.py\", line 60, in get_source\n",
      "    return self._get_source_fast(environment, template)\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\templating.py\", line 89, in _get_source_fast\n",
      "    raise TemplateNotFound(template)\n",
      "jinja2.exceptions.TemplateNotFound: index.html\n",
      "127.0.0.1 - - [24/May/2021 17:15:25] \"\u001b[37mGET /?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [24/May/2021 17:15:25] \"\u001b[37mGET /?__debugger__=yes&cmd=resource&f=jquery.js HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [24/May/2021 17:15:25] \"\u001b[37mGET /?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [24/May/2021 17:15:25] \"\u001b[37mGET /?__debugger__=yes&cmd=resource&f=ubuntu.ttf HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [24/May/2021 17:15:25] \"\u001b[37mGET /?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [24/May/2021 17:15:25] \"\u001b[37mGET /?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [24/May/2021 17:15:26] \"\u001b[35m\u001b[1mGET / HTTP/1.1\u001b[0m\" 500 -\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 2464, in __call__\n",
      "    return self.wsgi_app(environ, start_response)\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 2450, in wsgi_app\n",
      "    response = self.handle_exception(e)\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 1867, in handle_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 2447, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 1952, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 1821, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 1950, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 1936, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"<ipython-input-19-2b231701e662>\", line 4, in index\n",
      "    \n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\templating.py\", line 138, in render_template\n",
      "    ctx.app.jinja_env.get_or_select_template(template_name_or_list),\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\jinja2\\environment.py\", line 930, in get_or_select_template\n",
      "    return self.get_template(template_name_or_list, parent, globals)\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\jinja2\\environment.py\", line 883, in get_template\n",
      "    return self._load_template(name, self.make_globals(globals))\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\jinja2\\environment.py\", line 857, in _load_template\n",
      "    template = self.loader.load(self, name, globals)\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\jinja2\\loaders.py\", line 115, in load\n",
      "    source, filename, uptodate = self.get_source(environment, name)\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\templating.py\", line 60, in get_source\n",
      "    return self._get_source_fast(environment, template)\n",
      "  File \"C:\\Users\\caleb\\anaconda3\\Lib\\site-packages\\flask\\templating.py\", line 89, in _get_source_fast\n",
      "    raise TemplateNotFound(template)\n",
      "jinja2.exceptions.TemplateNotFound: index.html\n",
      "127.0.0.1 - - [24/May/2021 17:15:26] \"\u001b[37mGET /?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [24/May/2021 17:15:26] \"\u001b[37mGET /?__debugger__=yes&cmd=resource&f=jquery.js HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [24/May/2021 17:15:26] \"\u001b[37mGET /?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [24/May/2021 17:15:26] \"\u001b[37mGET /?__debugger__=yes&cmd=resource&f=ubuntu.ttf HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [24/May/2021 17:15:26] \"\u001b[37mGET /?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True, use_reloader=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
