#include <vector>
using namespace std;

vector<int> find_first_n_version1( int n )
{
    vector<int> primes;
    primes.emplace_back(2);

    int counter = 3;
    while( primes.size() < n )
    {
        bool prime = true;

        for( int i=3; i<counter; ++i )
            if( counter % i == 0 )
                prime = false;

        if( prime )
            primes.emplace_back(counter);

        counter += 1;
    }

    return primes;
}

vector<int> find_first_n_version2( int n )
{
    vector<int> primes;

    int counter = 2;
    while( primes.size() < n )
    {
        bool prime = true;
        int half = counter/2;

        for( int i=0; prime && i<primes.size() && primes[i]<=half; ++i )
            if( counter % primes[i] == 0 )
                prime = false;

        if( prime )
            primes.emplace_back(counter);

        counter += 1;
    }

    return primes;
}

int main()
{
    int primesToFind = 1000;

    find_first_n_version1( primesToFind );
    find_first_n_version2( primesToFind );

    return 0;
}
