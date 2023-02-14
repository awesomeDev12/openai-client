# Open AI client

First clone the project

```
git clone https://github.com/awesomeDev12/openai-client.git ~/Desktop/openai-client/

```


To create a desktop entry

```
touch ~/.local/share/applications/OpenAIClient.desktop
xdg-open ~/.local/share/applications/OpenAIClient.desktop
```

And fill it with
```
[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec=bash -c "cd $(xdg-user-dir DESKTOP) && ./openai-client/launch.sh"
Name=OpenAI client
Comment=OpenAI client for Desktop
Icon=$(xdg-user-dir DESKTOP)/openai-client/images/icons/desktop_icon.jpg
```

Fill it with

```ini
`cat OpenAIClient.desktop`


Fill it with


`![alt text](/OpenAIClient.desktop)`



To add your API key

1. Go to Settings -> Edit Settings -> API
2. Paste or Type your API key 
3. Click on Save



For developers

To run 
```
bash launch.sh
```
or 
```
python main.py
```
