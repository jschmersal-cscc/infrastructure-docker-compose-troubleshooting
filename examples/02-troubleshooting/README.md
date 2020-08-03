# Docker troubleshooting

While Docker is pretty straightforward, there are still some tools of the trade that you should know.  For these examples, build the `infra-example-3-03:0.3`, by running the [build.sh](build.sh) script.
```
[jschmersal1@WFIL011 03-troubleshooting]$ ./build.sh 
Sending build context to Docker daemon  31.23kB
Step 1/4 : FROM alpine
 ---> a24bb4013296
Step 2/4 : RUN mkdir /app
 ---> Running in 4e43ae17e799
Removing intermediate container 4e43ae17e799
 ---> 95e1d4a0f85e
Step 3/4 : COPY . /app
 ---> ed1bbf0a1dbf
Step 4/4 : CMD /app/run-it.sh
 ---> Running in 9938afd71afd
Removing intermediate container 9938afd71afd
 ---> d4cee17ccbc6
Successfully built d4cee17ccbc6
Successfully tagged infra-example-3-03:0.3
```


## Docker inspect
We've used a `docker inspect` command earlier in the examples, but I didn't explain it.  Running 
`docker inspect` on a container gives you a lot of information about the container from a docker
point of view.

Let's start your just-built `infra-example-3-03:0.3` container: `docker run --rm --name ex-3-03 -d infra-example-3-03:0.3`.

Now, let's run `docker inspect ex-3-03` and check out the output:
```
[jschmersal1@WFIL011 03-troubleshooting]$ docker inspect ex-3-03
[
    {
        "Id": "e2ced5f1c5370503df7260dcdff09720bcd6a578b37d510e1ff33296b5779ed6",
        "Created": "2020-08-03T20:17:59.345802435Z",
        "Path": "/bin/sh",
        "Args": [
            "-c",
            "/app/run-it.sh"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 16642,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2020-08-03T20:17:59.795380682Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:d4cee17ccbc6a524f9705abbd0b2e7409d2dd2f65267bde225d8ea377c739e60",
        "ResolvConfPath": "/var/lib/docker/containers/e2ced5f1c5370503df7260dcdff09720bcd6a578b37d510e1ff33296b5779ed6/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/e2ced5f1c5370503df7260dcdff09720bcd6a578b37d510e1ff33296b5779ed6/hostname",
        "HostsPath": "/var/lib/docker/containers/e2ced5f1c5370503df7260dcdff09720bcd6a578b37d510e1ff33296b5779ed6/hosts",
        "LogPath": "/var/lib/docker/containers/e2ced5f1c5370503df7260dcdff09720bcd6a578b37d510e1ff33296b5779ed6/e2ced5f1c5370503df7260dcdff09720bcd6a578b37d510e1ff33296b5779ed6-json.log",
        "Name": "/ex-3-03",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": true,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "Capabilities": null,
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/d14471f63be1592116e7a117a172fbdbfd959f4d0e07e1fd2fe78a9f0284324e-init/diff:/var/lib/docker/overlay2/30ad0804018e09c4f29ef1fa3b5521b10893029c6925bae7b0af96d495cf2947/diff:/var/lib/docker/overlay2/fec1112514b22002f03a548fd147c1ac11c0130148dbc8af81b9cfeb8b624f37/diff:/var/lib/docker/overlay2/973a101a487ce10750bd4c25f3f9d32592af8ecd99ce04ca3141bcc7960ff81f/diff",
                "MergedDir": "/var/lib/docker/overlay2/d14471f63be1592116e7a117a172fbdbfd959f4d0e07e1fd2fe78a9f0284324e/merged",
                "UpperDir": "/var/lib/docker/overlay2/d14471f63be1592116e7a117a172fbdbfd959f4d0e07e1fd2fe78a9f0284324e/diff",
                "WorkDir": "/var/lib/docker/overlay2/d14471f63be1592116e7a117a172fbdbfd959f4d0e07e1fd2fe78a9f0284324e/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "e2ced5f1c537",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "/app/run-it.sh"
            ],
            "Image": "infra-example-3-03:0.3",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "a8d6e81b464643e5b9fd8157e283b9816970dd6dbcdf26b4f27076e89c0dc4aa",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/a8d6e81b4646",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "390d9578bd89b25c090aabb3a74cef8230095214bbe39a2076364d899b5984ea",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "0c5a8dc1e9ad48dec536c3209aaf6235faf89d277ba92168930eeeb7851ff47a",
                    "EndpointID": "390d9578bd89b25c090aabb3a74cef8230095214bbe39a2076364d899b5984ea",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]
```

As you can see, there's a whole bunch of JSON-formatted output.  Notice some of the juicy parts: `State`, `HostConfig`, `Config`, `NetworkSettings`.

However, there's a _lot_ of information there.  If you want to see more targeted information you can either `grep` the results, or (preferrably), you can run `docker inspect` with the format option
and provide a [Go template](https://golang.org/pkg/text/template/) that filters the results for you.

In this example, I wan to look at the second (zero-based) environment variable: `docker inspect --format '{{ index .Config.Env 1 }}' ex-3-03`
```
[jschmersal1@WFIL011 03-troubleshooting]$ docker inspect --format '{{ index .Config.Env 1 }}' ex-3-03
MY_ENV_VAR=foo
```

## Docker logs
Docker logs lets you see the stdout and stderr for your docker containers:
```
[jschmersal1@WFIL011 03-troubleshooting]$ docker logs ex-3-03
The current time is Mon Aug  3 20:29:40 UTC 2020
The current time is Mon Aug  3 20:29:45 UTC 2020
The current time is Mon Aug  3 20:29:50 UTC 2020
The current time is Mon Aug  3 20:29:55 UTC 2020
The current time is Mon Aug  3 20:30:00 UTC 2020
The current time is Mon Aug  3 20:30:05 UTC 2020
The current time is Mon Aug  3 20:30:10 UTC 2020
The current time is Mon Aug  3 20:30:15 UTC 2020
The current time is Mon Aug  3 20:30:20 UTC 2020
The current time is Mon Aug  3 20:30:25 UTC 2020
...
```

It has some handy options to make your log spelunking easier.  Some commonly used options:

### Since (--since)
If you let your docker container run for a while, the logs will start to become overwhelming.  The `--since` option lets you specify a timeframe and only show logs that have happened after that time.  For example, `docker logs --since 2m ex-3-03` shows you logs in the last two minutes:
```
[jschmersal1@WFIL011 03-troubleshooting]$ docker logs --since 2m ex-3-03 
The current time is Tue Aug  4 14:09:09 UTC 2020
The current time is Tue Aug  4 14:09:14 UTC 2020
The current time is Tue Aug  4 14:09:19 UTC 2020
The current time is Tue Aug  4 14:09:24 UTC 2020
The current time is Tue Aug  4 14:09:29 UTC 2020
The current time is Tue Aug  4 14:09:34 UTC 2020
The current time is Tue Aug  4 14:09:39 UTC 2020
The current time is Tue Aug  4 14:09:44 UTC 2020
The current time is Tue Aug  4 14:09:49 UTC 2020
The current time is Tue Aug  4 14:09:54 UTC 2020
The current time is Tue Aug  4 14:09:59 UTC 2020
The current time is Tue Aug  4 14:10:04 UTC 2020
The current time is Tue Aug  4 14:10:09 UTC 2020
The current time is Tue Aug  4 14:10:14 UTC 2020
The current time is Tue Aug  4 14:10:19 UTC 2020
The current time is Tue Aug  4 14:10:24 UTC 2020
The current time is Tue Aug  4 14:10:29 UTC 2020
The current time is Tue Aug  4 14:10:34 UTC 2020
The current time is Tue Aug  4 14:10:39 UTC 2020
The current time is Tue Aug  4 14:10:44 UTC 2020
The current time is Tue Aug  4 14:10:49 UTC 2020
The current time is Tue Aug  4 14:10:54 UTC 2020
The current time is Tue Aug  4 14:10:59 UTC 2020
The current time is Tue Aug  4 14:11:04 UTC 2020
```

### Follow (--follow, -f)
The follow option (`--follow` or `-f`) is useful if you want to see the logging happen live to 
your screen.  Enter `docker logs -f ex-3-03` and wait for about 10 seconds and you will see new
logs printed to your terminal.

## Docker ps
We have touched on `docker ps` already, so you know it's a handy tool for seeing containers on
the system.  Just know that by default only _running_ containers are shown.  Also note that 
`docker ps` outputs the exposed ports to the screen, which is quite helpful.

Finally, `docker ps` has a useful `-f` (or `--filter`) option, which lets you specify attributes
of the containers you want to filter the output down to.  The 
[docker ps command page](https://docs.docker.com/engine/reference/commandline/ps/) gives the full
list of attributes you can filter by, but the most common by far is `status`.  You will very 
frequently see scripts with a line similar to `docker ps --filter status=exited -q` along with
further processing of the resulting container IDs.

## Docker exec (get into a running container)
The last troubleshooting option might be the most useful.  There is a container still running on
your system (`ex-3-03`), and you can see that it's running and view its logs.  However, something
doesn't seem quite right.  It would be handy to be able to "join" the container and open a terminal
within the container.  The `docker exec` command lets you run a command _inside_ a running container.

For example, we can run an `sh` session inside the container (as long as `sh` is available within the container, and any Linux-based container will have it).  Try it out with: `docker exec -it ex-3-03 sh`.  This instructs docker to run the `sh` command inside the `ex-3-03` container, and to have that `sh` terminal use my terminal's input as its standard input (remember the `-it` options?).

```
[jschmersal1@WFIL011 03-troubleshooting]$ docker exec -it ex-3-03 sh
/ # ls
app    dev    home   media  opt    root   sbin   sys    usr
bin    etc    lib    mnt    proc   run    srv    tmp    var
/ # ls /app
Dockerfile  README.md   build.sh    run-it.sh
/ # cat /app/run-it.sh 
while true
do
  echo "The current time is $(date)"
  sleep 5
done
/ # env
HOSTNAME=1d52b9a98348
SHLVL=1
HOME=/root
TERM=xterm
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
MY_ENV_VAR=foo
PWD=/
/ # ps
PID   USER     TIME  COMMAND
    1 root      0:03 {busybox} ash /app/run-it.sh
27306 root      0:00 sh
27324 root      0:00 sleep 5
27325 root      0:00 ps
/ # whoami
root
/ # exit
```

This is an invaluable tool.  As you can see I was able to interact with the running container.

_Note_: the biggest negative here is that the container needs to be running.  Frequently you would
like to get inside your stopped containers (for example, to troubleshoot why they didn't start up
correctly).  To do so, check out this [Stack Overflow answer](https://stackoverflow.com/questions/32353055/how-to-start-a-stopped-docker-container-with-a-different-command).
