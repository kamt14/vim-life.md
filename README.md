# 📓 Vim life.txt
Este un archivo de texto para tomar tus apuntes y notas, etc. Está hecho usando vim y vimWiki he inspirado en [LinuxChad](https://www.youtube.com/watch?v=EUCneUnGjv8&t=160s) puedes usarlo y mejorarlo.
Con ayuda de vim + vimWiki he implementado una forma fácil de llevar tus notas, calendario, etc.
Esta es una pequeña versión, espero en un futuro seguir actualizando.

## 📑 Requisitos
- vim
- vimWiki

## 🖥️ Formato
El siguiente formato tiene el index.wiki donde están todos los atajos a lo necesario para llevar tus notas.

life.txt

- 📬 Inbox
- 📆 Calendario
- 📓 ToDo
- 💻 Proyectos
- 📈 Futuro
- 📝 Notas

## Calendario
El calendar tiene las siguientes funciones para ser automatico.

- Añade fechas.
- Archiva días pasados.
- Implementa tareas recurrentes.

## 🚦 Instalación
1. Crear una carpeta para vimWiki

```
mkdir ~/wiki
```

2. Pegar todos los archivos a /wiki
3. Configurar ~/.vimrc

```
" To set default directory, and default format to markdown
let g:vimwiki_global_ext = 0
let g:vimwiki_key_mappings = { 'table_mappings':0 }
let g:vimwiki_list = [{
      \ 'path':'~/wiki/',
      \ 'syntax':'markdown',
      \ 'template_path':'~/wiki/template/',
      \ 'template_default':'default',
      \ 'ext':'.md',
      \ 'path_html':'~/wiki/site_html/',
      \ 'custom_wiki2html':'vimwiki_markdown',
      \ 'template_ext':'.tpl'}]

" Grupo de autocomandos para manejar Calendar.wiki
augroup CalendarManager
  autocmd!
  autocmd BufReadPost ~/wiki/Calendar.md 0r! python3 ~/wiki/calendar_manager.py
augroup END
```

> [!IMPORTANT]
> Esta configuración es necesaria para que no exista conflictos si estas usando **UltiSnippets**.


