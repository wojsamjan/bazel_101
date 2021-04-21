load("@rules_proto//proto:defs.bzl", "proto_library")
load("@com_github_grpc_grpc//bazel:python_rules.bzl", "py_grpc_library", "py_proto_library")

proto_library(
    name = "fakeperson_proto",
    srcs = ["fakeperson.proto"],
)

py_proto_library(
    name = "fakeperson_py_proto",
    deps = [":fakeperson_proto"],
)

py_grpc_library(
    name = "fakeperson_py_grpc",
    srcs = [":fakeperson_proto"],
    deps = [":fakeperson_py_proto"],
)

load("@py_deps//:requirements.bzl", "requirement")
py_binary(
    name = "fakeperson_server",
    srcs = ["fakeperson_server.py"],
    deps = [
        requirement("requests"),
        ":fakeperson_py_grpc"
    ],
)

py_binary(
    name = "fakeperson_client",
    srcs = ["fakeperson_client.py"],
    deps = [":fakeperson_py_grpc"],
)

py_test(
    name = "fakeperson_test",
    srcs = ["fakeperson_test.py"],
    deps = [
        requirement("pytest"),
        ":fakeperson_server",
        ":fakeperson_py_grpc"
    ],
)
