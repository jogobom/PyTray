from behave import given, then
from assertpy import assert_that
from models.tuples import Tuple, Point, Vector


@given('a <- tuple({x}, {y}, {z}, {w})')
def step_impl(context, x, y, z, w):  # noqa: F811
    context.a = Tuple(x, y, z, w)


@then('a.x = {x}')
def step_impl(context, x):  # noqa: F811
    assert_that(context.a.x).is_close_to(float(x), 1e-6)


@then('a.y = {y}')
def step_impl(context, y):  # noqa: F811
    assert_that(context.a.y).is_close_to(float(y), 1e-6)


@then('a.z = {z}')
def step_impl(context, z):  # noqa: F811
    assert_that(context.a.z).is_close_to(float(z), 1e-6)


@then('a.w = {w}')
def step_impl(context, w):  # noqa: F811
    assert_that(context.a.w).is_close_to(float(w), 1e-6)


@then('a is a point')
def step_impl(context):  # noqa: F811
    assert_that(context.a.w).is_close_to(1.0, 1e-6)


@then('a is not a vector')
def step_impl(context):  # noqa: F811
    assert_that(context.a.w).is_not_equal_to(0)


@then('a is not a point')
def step_impl(context):  # noqa: F811
    assert_that(context.a.w).is_not_close_to(1.0, 1e-6)


@then('a is a vector')
def step_impl(context):  # noqa: F811
    assert_that(context.a.w).is_equal_to(0)


@given('p <- point({x}, {y}, {z})')
def step_impl(context, x, y, z):  # noqa: F811
    context.p = Point(x, y, z)


@then('p = tuple({x}, {y}, {z}, {w})')
def step_impl(context, x, y, z, w):  # noqa: F811
    assert context.p == Tuple(x, y, z, w)


@given('v <- vector({x}, {y}, {z})')
def step_impl(context, x, y, z):  # noqa: F811
    context.v = Vector(x, y, z)


@then('v = tuple({x}, {y}, {z}, {w})')
def step_impl(context, x, y, z, w):  # noqa: F811
    assert context.v == Tuple(x, y, z, w)
