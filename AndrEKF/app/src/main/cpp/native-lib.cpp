#include <jni.h>
#include <string>
#include <fstream>
#include "main_closed_loop_float.h"
extern "C" JNIEXPORT jstring

JNICALL
Java_com_example_andrekf_MainActivity_stringFromJNI(
        JNIEnv *env,
        jobject /* this */) {
    std::string hello = "success!";
    main1();
    /*
    std::string dir = "/storage/emulated/0/Android/data/com.example.andrekf/files/zop.txt";
    std::string buf = "whatever";
    std::ifstream myfile(dir);
    if (!myfile.is_open()) {
        std::ofstream os(dir.c_str(), std::ios::trunc);
        os.write(buf.c_str(), buf.length());
        os.close();

    }

    FILE* file = fopen("/storage/emulated/0/Android/data/com.example.andrekf/files/zop.txt","w");
    if (file != NULL)
    {
        fputs("HELLO WORLD!\n", file);
        fclose(file);
    }
*/
    return env->NewStringUTF(hello.c_str());


    //return env->NewStringUTF(main1().c_str());

}

