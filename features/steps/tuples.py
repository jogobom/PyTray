from behave import given, then
from assertpy import assert_that
from models.tuples import Tuple, Point, Vector


@given('a <- tuple({x}, {y}, {z}, {w})')
def given_a_tuple(context, x, y, z, w):
    context.a = Tuple(x, y, z, w)


@then('a.x = {x}')
def then_tuple_has_x_value(context, x):
    assert_that(context.a.x).is_close_to(float(x), 1e-6)


@then('a.y = {y}')
def then_tuple_has_y_value(context, y):
    assert_that(context.a.y).is_close_to(float(y), 1e-6)


@then('a.z = {z}')
def then_tuple_has_z_value(context, z):
    assert_that(context.a.z).is_close_to(float(z), 1e-6)


@then('a.w = {w}')
def then_tuple_has_w_value(context, w):
    assert_that(context.a.w).is_close_to(float(w), 1e-6)


@then('a is a point')
def then_a_is_a_point(context):
    assert_that(context.a.w).is_close_to(1.0, 1e-6)


@then('a is not a vector')
def then_a_not_a_vector(context):
    assert_that(context.a.w).is_not_equal_to(0)


@then('a is not a point')
def then_a_is_not_a_point(context):
    assert_that(context.a.w).is_not_close_to(1.0, 1e-6)


@then('a is a vector')
def then_a_is_a_vector(context):
    assert_that(context.a.w).is_equal_to(0)


@given('p <- point({x}, {y}, {z})')
def given_a_point(context, x, y, z):
    context.p = Point(x, y, z)


@then('p = tuple({x}, {y}, {z}, {w})')
def then_p_is_a_tuple_of(context, x, y, z, w):
    assert context.p == Tuple(x, y, z, w)


@given('v <- vector({x}, {y}, {z})')
def given_a_vector(context, x, y, z):
    context.v = Vector(x, y, z)


@then('v = tuple({x}, {y}, {z}, {w})')
def then_v_is_a_tuple_of(context, x, y, z, w):
    assert context.v == Tuple(x, y, z, w)
