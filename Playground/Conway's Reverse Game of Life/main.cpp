#include<iostream>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<unistd.h>
using namespace std;

typedef struct{
    int dna[25][25];
    int fitness=0;
}GENE;

#include<random>
template<class Genotype>class Genetic_Algorithm{

    public:

    std::mt19937 mt;            // メルセンヌ・ツイスタの32ビット版
    //std::random_device rnd;     // 非決定的な乱数生成器

    vector<Genotype>individuals[2];//世代 偶奇
    Genotype ideal;//評価の基準

    int population_size;//1世代の個体数
    int generation=0;//現在の世代

    //public:

    Genetic_Algorithm(int population_size):population_size(population_size)
    {
        individuals[0]=vector<Genotype>(population_size);
        individuals[1]=vector<Genotype>(population_size);
    }

    Genotype operator[](int individual_No){return this->individuals[generation%2][individual_No];}


    int fitness(Genotype individual){
        ////////////////////
        int dna_[2][25][25];
        for(int i=0;i<25*25;i++)dna_[0][i/25][i%25]=individual.dna[i/25][i%25];

        const int alive=1,dead=0;
        int d8[10]={1,1,1,0,-1,-1,-1,0,1,1};//0-7 2-9

        for(int step=0;step<ideal.fitness;step++){
            for(int i=0;i<25;i++){
                for(int j=0;j<25;j++){
                    int alive_cnt=0;
                    for(int k=0;k<8;k++){
                        int h=i+d8[k],w=j+d8[k+2];
                        //if(!(0<=h&&h<H&&0<=w&&w<W))continue;
                        h=(h+25)%25;w=(w+25)%25;
                        alive_cnt+=(dna_[step%2][h][w]==alive);
                    }
                    switch(dna_[step%2][i][j]){
                        case alive:dna_[!(step%2)][i][j]=((alive_cnt==2||alive_cnt==3)?alive:dead);break;
                        case dead:dna_[!(step%2)][i][j]=(alive_cnt==3?alive:dead);break;
                    }
                }
            }
        }



        int cnt=0;
        for(int i=0;i<25*25;i++){
            cnt+=(dna_[ideal.fitness%2][i/25][i%25]!=ideal.dna[i/25][i%25]);
        }
        return cnt;
        ////////////////////
    }

    void evaluation(){
        int current=generation%2,next=current^1;

        for(Genotype& x:individuals[current])x.fitness=fitness(x);

        sort(individuals[current].begin(),individuals[current].end(),
        [](const Genotype& a,const Genotype& b){return a.fitness<b.fitness;});
    }

    void initialize(int Seed){
        mt.seed(Seed);
        std::uniform_int_distribution<> rand_int(0,100);//integer [L,R]
        ////////////////////
        for(auto& x:individuals[0]){
            for(int i=0;i<25*25;i++){
                x.dna[i/25][i%25]=(rand_int(mt)>50?1:0);
            }
        }
        for(int i=0;i<25*25;i++){
            individuals[0][0].dna[i/25][i%25]=0;
        }
        
        evaluation();
        ////////////////////
        return;
    }

    Genotype crossover(Genotype a,Genotype b){
        Genotype child;
        std::uniform_int_distribution<> rand_int(0,20);//integer [L,R]

        ////////////////

        #define CROSSOVER_RATE 0.8 //交叉の確率
        for(int i=0;i<25*25;i++){
            child.dna[i/25][i%25]=(rand_int(mt)>50?a.dna[i/25][i%25]:b.dna[i/25][i%25]);
        }

        // for(int i=0;i<25*25;i++){
        //     child.dna[i/25][i%25]=(i<(25*25)/2?a.dna[i/25][i%25]:b.dna[i/25][i%25]);
        // }

        ////////////////
        return child;
    }

    void mutation(Genotype& g){
        const int mutation_rate=1; //突然変異の確率
        std::uniform_int_distribution<> rand_int(0,100);//integer [L,R]
        ////////////////
        for(int i=0;i<25*25;i++){
            g.dna[i/25][i%25]^=(rand_int(mt)<mutation_rate?ideal.dna[i/25][i%25]:!ideal.dna[i/25][i%25]);
        }
        ////////////////
        return;
    }

    void next_generation(){
        int No=0;
        int current=generation%2,next=current^1;
        
        //エリート選択
        const int elite_reproduction=3;
        for(;No<elite_reproduction;No++){
            individuals[next][No]=individuals[current][No];
        }
        // //突然変異を加えるエリート
        for(;No<elite_reproduction*2;No++){
            individuals[next][No]=individuals[current][No-elite_reproduction];
        }
        std::uniform_int_distribution<> rand_int(0,population_size-1);//integer [L,R]
        //交叉
        for(;No<population_size;No++){
            int a=rand_int(mt),b=rand_int(mt);
            individuals[next][No]=crossover(individuals[current][a],individuals[current][b]);
        }
        //突然変異 最良個体を除く
        for(int i=1;i<population_size;i++){
            mutation(individuals[next][i]);
        }
        generation++;
        evaluation();
        return;
    }

    Genotype run(int Seed,int max_generation){
        //initialize(Seed);

        for(generation=0;generation<max_generation;){
            printf("\033[%d;%dH",(30)+1,(0)*2+1);
            cout<<individuals[generation%2][0].fitness<<endl;
            next_generation();
            //for(int i=0;i<population_size;i++)cout<<individuals[generation%2][i].fitness<<" \n"[i==population_size-1];
            if(individuals[generation%2][0].fitness==0){cout<<"ok"<<endl;break;}
           //if(generation>max_generation&&individuals[generation%2][0].fitness<20)break;
        }
        return individuals[generation%2][0];
    }
};

#include"visualize.h"
using namespace vis;
void printlife(GENE life,int H,int W,int h,int w){
    setcursol(h,w);
    attribute(attr(BOLD));
    attribute(attr(REVERSE));
    for(int i=0;i<H;i++){
        for(int j=0;j<W;j++){
            charcolor(color(life.dna[i][j]));
            //printf("  ");
            printf(" %d",life.dna[i][j]);
        }
        newline();
        setcursol(cursol_h,w);
    }
    attribute(attr(RESET));
    return;
}

int main(int argc,char** argv){

    string str;
    ifstream test("test.csv");
    getline(test, str);
    ifstream sample("sample_submission.csv");
    getline(sample, str);

    if(!test){
        cerr << "Error: test file not opened." << endl;
        return 1;
    }
    if(!sample){
        cerr << "Error: sample file not opened." << endl;
        return 1;
    }

    ofstream out("submission.csv", ios::out);
    out<<"id,";
    for(int i=0;i<25*25;i++)out<<"start_"<<i<<",\n"[i+1==25*25];

    for(int No=0;No<50000;No++){
        getline(test, str);
        replace(str.begin(), str.end(), ',', ' ');
        stringstream buf(str);
        int id,delta;buf>>id>>delta;
        //cout<<"id:"<<id<<endl<<"delta:"<<delta<<endl;

        Genetic_Algorithm<GENE>GA(20);
        GA.ideal.fitness=delta;

        for(int i=0;i<25*25;i++)buf>>GA.ideal.dna[i/25][i%25];

        GA.initialize(0);
        getline(sample, str);
        replace(str.begin(), str.end(), ',', ' ');
        stringstream buf2(str);
        buf2>>id;

        for(int i=0;i<25*25;i++)buf2>>GA.individuals[0][0].dna[i/25][i%25];

        GA.run(0,200);

        cout<<id<<" "<<delta<<" "<<GA[0].fitness<<endl;

        out<<id<<",";
        for(int i=0;i<25*25;i++)out<<GA[0].dna[i/25][i%25]<<",\n"[i+1==25*25];

        // printlife(GA.ideal,25,25,0,30);

        // printf("\033[2J");
        // printlife(GA[0],25,25,0,0);
        // printf("%d\n",GA[0].fitness);
        //return 0;
    }
    return 0;
}
