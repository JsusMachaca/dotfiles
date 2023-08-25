call plug#begin('~/.config/nvim/plugged')
	
	Plug 'sheerun/vim-polyglot'
	Plug 'jiangmiao/auto-pairs'

	Plug 'Yggdroot/indentLine'
	
	Plug 'alvan/vim-closetag'

	Plug 'mhinz/vim-signify'
  
	Plug 'scrooloose/NERDTree'    

	" Intellisense
  Plug 'neoclide/coc.nvim', {'branch': 'release'}

	"Icons
	Plug 'ryanoasis/vim-devicons'

	" Themes / Airline
	Plug 'vim-airline/vim-airline'
	Plug 'vim-airline/vim-airline-themes'
	Plug 'dracula/vim', {'as': 'dracula'}
	Plug 'tomasiser/vim-code-dark'
	Plug 'joshdick/onedark.vim'
call plug#end()
