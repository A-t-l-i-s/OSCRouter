#include<require.hpp>





int main(int argC, char* argV[]){
	{
		// Allocate vars
		char exePath[MAX_PATH];
		uint16_t exePathSize;
		
		// Get path
		GetModuleFileName(NULL, exePath, MAX_PATH);
		
		// Get path size
		exePathSize = strlen(exePath);

		// Initialize program path 
		char programPath[exePathSize];


		char c;
		bool found = false;

		for (uint16_t i = 0; i < exePathSize; i++){
			// Get exe path character
			c = exePath[exePathSize - i - 1];

			// Reset program path
			programPath[i] = 0;

			if (c == '/' || c == '\\'){
				c = '\\';
				found = true;
			}

			if (found){
				programPath[exePathSize - i - 1] = c;
			}
		}


		// Change to correct directory
		chdir(programPath);


		// Get binary directory and size
		char* binPath = strcat(programPath, "bin");
		uint16_t binPathSize = strlen(binPath);


		// Allocate bin path wide char
		wchar_t binPathW[binPathSize];

		// Convert to wide character
		mbstowcs(binPathW, binPath, binPathSize);
		uint16_t binPathWSize = wcslen(binPathW);

		// Add dll directory
		AddDllDirectory(
			binPathW
		);
	}


	{
		// Create python pre config
		PyPreConfig config;
		PyPreConfig_InitIsolatedConfig(&config);

		// Config
		config.allocator = PYMEM_ALLOCATOR_DEFAULT;
		config.configure_locale = false;
		config.coerce_c_locale = false;
		config.coerce_c_locale_warn = false;
		config.dev_mode = false;
		config.isolated = true;
		config.legacy_windows_fs_encoding = false;
		config.parse_argv = false;
		config.use_environment = false;
		config.utf8_mode = false;


		// Pre initialize python
		Py_PreInitialize(&config);
	}


	{
		// Create python config
		PyConfig config;
		PyConfig_InitPythonConfig(&config);

		// Config
		config.write_bytecode = false;
		config.optimization_level = 0;
		config.program_name = (wchar_t*)L"OSCRouter";
		
		config.home = (wchar_t*)L".";
		config.pythonpath_env = (wchar_t*)L".";
		config.platlibdir = (wchar_t*)L"bin";
		
		config.safe_path = true;
		config.parse_argv = false;
		config.site_import = false;
		config.buffered_stdio = false;
		config.use_environment = false;
		config.user_site_directory = false;

		// Prefix
		config.prefix = (wchar_t*)L".";

		// Parse args to python
		PyConfig_SetBytesArgv(&config, argC, argV);


		// Logging
		// config.verbose = true;
		// config.tracemalloc = true;


		// Add module search paths
		PyWideStringList_Append(&config.module_search_paths, L".");
		PyWideStringList_Append(&config.module_search_paths, L"bin");
		PyWideStringList_Append(&config.module_search_paths, L"lib.zip");

		// Prevent module paths from override
		config.module_search_paths_set = true;


		// Initialize python
		Py_InitializeFromConfig(&config);
	}


	{
		// File name constant
		const char* fileName = "main.py";

		// Create py string of filename
		PyObject* filenameObj = Py_BuildValue("s", fileName);

		// Open file
		FILE* file = _Py_fopen_obj(filenameObj, "rb");

		// Compile file
		PyRun_SimpleFile(file, fileName);

		// Close file
		fclose(file);
	}


	// De-Initialize python
	Py_Finalize();


	return 0x01;
}


