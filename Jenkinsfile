pipeline {
    agent {
        node {
            label 'docker-ckbase-ubuntu'
        }
    }

    stages {
        stage('Build') {
            steps {
                script {
                    def BRANCH_NAME = env.GIT_BRANCH.replaceAll("origin/", "")
                    currentBuild.displayName = "#${currentBuild.number}_${BRANCH_NAME}"

                    env.IMAGE_TAG = env.GIT_COMMIT.substring(0, 7)
                }

                echo "Building image for ${env.GIT_BRANCH}"

                sh "echo \"[build]\" > __deploy_info.txt"
                sh "echo \"time=\$(date)\" >> __deploy_info.txt"
                sh "echo \"revision=\$(git rev-parse HEAD)\" >> __deploy_info.txt"
                sh "echo \"branch=${env.GIT_BRANCH}\" >> __deploy_info.txt"

                sh "docker build --tag asergio:weddingbook-${env.IMAGE_TAG} ."
            }
        }

        stage ('Push image') {
            when {
                expression {
                    env.GIT_BRANCH =~ /^master$|^release\/.*$/
                }
            }

            steps {
                script {
                    REGISTRY_ID = env.GIT_BRANCH =~ /^master$/ ? '988207228673' : '889859566884'
                    REGISTRY_URL = "${REGISTRY_ID}.dkr.ecr.eu-west-1.amazonaws.com"
                    IMAGE_VERSION = env.GIT_BRANCH =~ /^master$/ ? 'latest' : 'preprod'
                }
                echo "Pushing image to registry ${IMAGE_VERSION}:${env.IMAGE_TAG}"

                sh 'echo StrictHostKeyChecking=no >> ~/.ssh/config'

                sh "docker tag asergio:weddingbook-${env.IMAGE_TAG} ${REGISTRY_URL}/asergio:weddingbook-${env.IMAGE_TAG}"
                sh "docker push ${REGISTRY_URL}/asergio:weddingbook-${env.IMAGE_TAG}"

                sh "docker tag ${REGISTRY_URL}/asergio:weddingbook-${env.IMAGE_TAG} ${REGISTRY_URL}/asergio:weddingbook-${IMAGE_VERSION}"
                sh "docker push ${REGISTRY_URL}/asergio:weddingbook-${IMAGE_VERSION}"
            }
        }
    }
}