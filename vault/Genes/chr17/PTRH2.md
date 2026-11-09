---
symbol: "PTRH2"
type: "gene"
col: 6507
ensembl_id: "ENSG00000141378"
name: "peptidyl-tRNA hydrolase 2"
location: "17q23.1"
module: 33
arm: "+"
pooled_cpm: 56.74
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# PTRH2

*peptidyl-tRNA hydrolase 2* — 17q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.97× (z +13.5, q 7e-39, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.813× (z -7.0, q 2e-09, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (A-427 0.357×, CHP-212 0.216×, C-33 A 0.393×, SW480 0.609×, …); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW48 0.108×, NCI-H23 0.222×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.353×, SNU-1 0.217×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (H4 0.258×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EARS2]] (+0.74, fdr 7e-06), [[PMM2]] (+0.65, fdr 7e-06), [[CTU1]] (+0.61, fdr 7e-06); moves opposite to [[ILK]] (-0.48, fdr 5e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6507.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.97×** | +13.5 | 7e-39 | 47/49 (CFPAC-1, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.19×** | +9.8 | 5e-20 | 32/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +9.2 | 6e-18 | 41/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +7.2 | 1e-10 | 30/48 (Panc 03.27, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +6.8 | 8e-10 | 29/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +6.8 | 1e-09 | 33/48 (NCI-H2030, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +5.9 | 4e-07 | 26/48 (NCI-H2347, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +5.8 | 4e-07 | 28/47 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.57×** | +5.6 | 2e-06 | 26/48 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change | **1.24×** | +4.9 | 4e-05 | 19/43 (NCI-H460, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.48×** | +4.8 | 7e-05 | 22/48 (NCI-H1573, HCT15, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +4.8 | 8e-05 | 22/47 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +4.6 | 2e-04 | 21/48 (SK-MEL-2, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.31×** | +4.5 | 2e-04 | 23/48 (A549, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.43×** | +4.4 | 3e-04 | 17/48 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.41×** | +4.3 | 7e-04 | 16/48 (NCI-H460, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.002 | 16/48 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.009 | 9/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6507.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (A-427 0.357×, CHP-212 0.216×, C-33 A 0.393×, SW480 0.609×, …); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW48 0.108×, NCI-H23 0.222×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.353×, SNU-1 0.217×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (H4 0.258×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.813×** | -7.0 | 2e-09 | 26/48 (A-427, CHP-212, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.847× | -3.9 | 0.017 | 16/48 (PANC-1, SW1417, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.890× | -3.9 | 0.017 | 8/48 (SK-MEL-2, BT-474, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.854× | -3.8 | 0.023 | 15/48 (RKO, J82, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.896× | -3.7 | 0.023 | 13/48 (A-427, LOX-IMVI, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.861× | -3.6 | 0.034 | 14/47 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.891× | -3.4 | 0.057 | 13/48 (SW480, CHP-212, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.772×** | -3.2 | 0.090 | 9/48 (A-427, SW1417, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.870× | -3.1 | 0.12 | 11/47 (SW480, SNU-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.898× | -3.1 | 0.12 | 11/48 (SW480, A-427, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | 0.887× | -3.0 | 0.12 | 13/48 (SW480, SW48, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6507. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 107 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -17.7) |
| [[SW48 (line)]] | wt | 76.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.403× (z -10.2) |
| [[CHP-212 (line)]] | wt | 126 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -15.4) |
| [[HEC-1-A (line)]] | alt | 53.7 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.48× (z +10.3) | — |
| [[SNU-1 (line)]] | wt | 64.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -11.2) |
| [[BT-474 (line)]] | alt | 179 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.581× (z -9.1) |
| [[C-33 A (line)]] | alt | 73.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 49.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.98× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 49.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.88× (z +8.9) | — |
| [[H4 (line)]] | wt | 85.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.258× (z -10.1) |
| [[HOP62 (line)]] | alt | 38.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +8.9) ⚠ cell-cycle shift, explains ~10% of this change | — |
| [[NCI-H1573 (line)]] | alt | 36.2 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.73× (z +8.9) ⚠ toxic | — |
| [[NCI-H23 (line)]] | alt | 64.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change |
| [[NCI-H661 (line)]] | alt | 44.7 | 0 | 1 | — | [[γ-Oryzanol (drug)]] 0.5 µM 0.0860× (z -8.8) |
| [[SW1417 (line)]] | alt | 63.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.546× (z -9.6) |
| [[SW480 (line)]] | alt | 69.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.609× (z -10.5) |
| [[A-172 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 58.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 56.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 104 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 72.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6507), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EARS2]] | +0.74 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[PMM2]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[CTU1]] | +0.61 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[PRPF40B]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[TSR1]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[TRNT1]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ALG3]] | +0.60 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[SNRPE]] | +0.60 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[NAA20]] | +0.60 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[GTPBP4]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RABEPK]] | +0.59 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[YRDC]] | +0.59 | +0.60 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ILK]] | -0.48 | -0.40 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.511). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.4, -30.8); signed map (-14.3, -56.8). **Vector** length 108, 27.2% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.0 | +9.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +13.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.4 | +9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.7 | +5.8 |
|  | [[EX229 (drug)]] 5 µM |  | +3.8 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.7 | +4.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.6 | +5.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -7.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -2.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change | -3.0 | +4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -3.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.4 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -3.1 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.9 | -0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | peptidyl-tRNA hydrolase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.1 — chr17:59,674,636-59,707,626 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BIT1, CGI-147, PTH2, CFAP37 |
| Gene groups (HGNC) | Cilia and flagella associated |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 2 pathways, smallest: Ub-specific processing proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3E5](https://www.uniprot.org/uniprotkb/Q9Y3E5) (Peptidyl-tRNA hydrolase 2, mitochondrial):

> Peptidyl-tRNA hydrolase which releases tRNAs from the ribosome during protein synthesis. Promotes caspase-independent apoptosis by regulating the function of two transcriptional regulators, AES and TLE1.

**Summary**, from NCBI Gene [51651](https://www.ncbi.nlm.nih.gov/gene/51651):

> The protein encoded by this gene is a mitochondrial protein with two putative domains, an N-terminal mitochondrial localization sequence, and a UPF0099 domain. In vitro assays suggest that this protein possesses peptidyl-tRNA hydrolase activity, to release the peptidyl moiety from tRNA, thereby preventing the accumulation of dissociated peptidyl-tRNA that could reduce the efficiency of translation. This protein also plays a role regulating cell survival and death. It promotes survival as part …

**Accessions** — [HGNC:24265](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24265) · Entrez [51651](https://www.ncbi.nlm.nih.gov/gene/51651) · UniProt [Q9Y3E5](https://www.uniprot.org/uniprotkb/Q9Y3E5) · Ensembl [ENSG00000141378](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141378)

## Data

Gene col 6507: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6507); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6507, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6507]; `tensor/DDL_lfc|DDL_z.npy` [6507]; `embed/gene_vectors.npy` [6507]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6507 or target_col == 6507). Every well: [[PTRH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTRH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
