from viewflow import flow
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from viewflow import frontend

from .models import CRProcess

@frontend.register
class CRFlow(Flow):
    process_class = CRProcess

    start = (
        flow.Start(
            CreateProcessView,
            fields=["orderid","title","vendor","product_name","severity","cr_type","affected_device","start_time","end_time"]
        ).Permission(
            auto_create=True
        ).Next(this.l1_approve)
    )

    l1_approve = (
        flow.View(
            UpdateProcessView,
            fields=["l1_approve"]
        ).Permission(
            auto_create=True
        ).Next(this.check_l1_approve)
    )

    check_l1_approve = (
        flow.If(lambda activation: activation.process.l1_approve)
        .Then(this.send)
        .Else(this.end)
    )

    send = (
        flow.Handler(
            this.send_to_l2
        ).Next(this.l2_approve)
    )

    l2_approve = (
        flow.View(
            UpdateProcessView,
            fields=["l2_approve"]
        ).Permission(
            auto_create=True
        ).Next(this.check_l2_approve)
    )

    check_l2_approve = (
        flow.If(lambda activation: activation.process.l2_approve)
        .Then(this.send)
        .Else(this.end)
    )

    send = (
        flow.Handler(
            this.send_to_close
        ).Next(this.end)
    )

    end = flow.End()

    def send_to_l2(self, activation):
        print(activation.process.orderid)
    
    def send_to_close(self, activation):
        print(activation.process.orderid)