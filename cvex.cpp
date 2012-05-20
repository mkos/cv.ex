#include <iostream>
#include <opencv2/highgui/highgui_c.h>

int main( int argc, char** argv ) {

	if (argc < 2) {
	
		std::cout << "usage: cvex <picture>" << std::endl;
	
	}
	else {

		IplImage* img = cvLoadImage( argv[1] );
		cvNamedWindow( "Example1", CV_WINDOW_AUTOSIZE );
		cvShowImage( "Example1", img );
		cvWaitKey(0);
		cvReleaseImage( &img );
		cvDestroyWindow( "Example1" );
		
		std::cout << "end of the test" << std::endl;
	
	}
    
	return 0;
}
