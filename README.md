# health-support-chatbot

This is a <a href="https://rasa.com/">Rasa</a> powered health support chatbot

### To run the bot
- Install rasa by following the steps given <a href="https://rasa.com/docs/rasa/installation/">here</a>🔗
- Create a `data.json` jsut outside the directory and enter the data in the format given below
```
{
    "ortho":{
        "Ravis":{
            "info":"MBBS",
            "slots":"32"
        },
        "Ravi":{
            "info":"MBBS",
            "slots":"14"
        }        
    }
}
```
- Open a terminal and run ``` rasa run actions ```
- Open andother terminal and run ```rasa shell ```
- Type you query in the terminal
  - You can view the various hospital deparments available
  - Check the nearby hospitals, doctors and OP slots available as per given in the `data.json` file.
  - Check the symptoms and preventive measures for common diseases
  - _i.e. covid, diabetes cough diarrhea common-cold chiken-pox, flu, malaria, pneumonia, cholera, dengue, typhoid_
