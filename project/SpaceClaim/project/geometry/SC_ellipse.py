def extrude_ellipse(a, b, c, name_3D_object, center_coordinate={"OX": 0, "OY": 0, "OZ": 0}):
    center = Point.Create(center_coordinate["OX"], center_coordinate["OY"], center_coordinate["OZ"])

    c1 = CurveSegment.Create(Ellipse.Create(Frame.Create(center, Direction.DirX, Direction.DirY), a, b),
                             Interval.Create(0, math.pi))
    c2 = CurveSegment.Create(Ellipse.Create(Frame.Create(center, Direction.DirX, Direction.DirZ), a, c),
                             Interval.Create(0, math.pi))
    c3 = CurveSegment.Create(Ellipse.Create(Frame.Create(center, Direction.DirY, Direction.DirZ), b, c),
                             Interval.Create(0, math.pi / 2))

    pt = Window.ActiveWindow.Document.MainPart

    profile1 = List[ITrimmedCurve]([c1])
    profile2 = List[ITrimmedCurve]([c2])
    guides = List[ITrimmedCurve]([c3])
    profiles = List[ICollection[ITrimmedCurve]]([profile1, profile2])
    b = Body.LoftProfiles(None, profiles, None, guides)

    matrixXZ = SpaceClaim.Api.V19.Unsupported.MatrixMethods.GetMirror(
        Plane.Create(Frame.Create(center, Direction.DirX, Direction.DirZ)))
    matrixXY = SpaceClaim.Api.V19.Unsupported.MatrixMethods.GetMirror(
        Plane.Create(Frame.Create(center, Direction.DirX, Direction.DirY)))

    b2 = b.Copy()
    b2.Transform(matrixXZ)
    b.Unite(List[Body]([b2]))
    b2 = b.Copy()
    b2.Transform(matrixXY)
    b.Unite(List[Body]([b2]))

    DesignBody.Create(pt, name_3D_object, b)


def execute_ellipse(a, b, c, center_coordinate={"OX": 0, "OY": 0, "OZ": 0}):
    extrude_ellipse(a, b, c, "execute", center_coordinate)

    targets = BodySelection.Create(GetRootPart().Bodies[0])

    tools = BodySelection.Create(GetRootPart().Bodies[1])

    options = MakeSolidsOptions()

    result = Combine.Intersect(targets, tools, options)

    selection = BodySelection.Create(GetRootPart().Bodies[2])

    result = Combine.RemoveRegions(selection)

    selection = BodySelection.Create(GetRootPart().Bodies[1])

    result = Delete.Execute(selection)
