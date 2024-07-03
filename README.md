# Vim life.txt
Este un archivo de texto para tomar tus apuntes y notas, etc. Está hecho usando vim y vimWiki he inspirado en [LinuxChad](https://www.youtube.com/watch?v=EUCneUnGjv8&t=160s) puedes usarlo y mejorarlo.

## Requisitos
- vim
- vimWiki

## Instalación
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


