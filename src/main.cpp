#include<require.hpp>





int main(int argC, const char* argV[]){
	{
		// Create new path
		const wchar_t* binPath = L"./bin";

		// Alocate new path
		wchar_t binPath_[MAX_PATH];

		// Get absolute path
		_wfullpath(
			binPath_,
			binPath,
			MAX_PATH
		);

		// Add dll directory
		AddDllDirectory(
			binPath_
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
		config.program_name = (wchar_t*)programName;
		
		config.home = NULL;
		config.platlibdir = (wchar_t*)L"bin";
		
		config.site_import = false;
		config.buffered_stdio = false;
		config.user_site_directory = false;


		// Logging
		// config.verbose = true;
		// config.tracemalloc = true;


		// Add module search paths
		PyWideStringList_Append(&config.module_search_paths, L"bin");
		PyWideStringList_Append(&config.module_search_paths, L"lib");
		PyWideStringList_Append(&config.module_search_paths, L"lib.zip");

		// Prevent module paths from override
		config.module_search_paths_set = true;


		// Initialize python
		Py_InitializeFromConfig(&config);
	}


	{
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


