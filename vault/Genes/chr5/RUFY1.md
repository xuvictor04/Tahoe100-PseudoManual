---
symbol: "RUFY1"
type: "gene"
col: 10750
ensembl_id: "ENSG00000176783"
name: "RUN and FYVE domain containing 1"
location: "5q35.3"
module: 28
arm: "+"
pooled_cpm: 56.9
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# RUFY1

*RUN and FYVE domain containing 1* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.39× (z +12.2, q 2e-31, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.840× (z -6.4, q 5e-08, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM254]] (+0.65, fdr 7e-06), [[SETDB1]] (+0.64, fdr 7e-06), [[LSM14A]] (+0.64, fdr 7e-06); moves opposite to [[SDC1]] (-0.59, fdr 1e-05), [[MED12L]] (-0.55, fdr 3e-05), [[LINC02458]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10750.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +12.2 | 2e-31 | 30/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +8.4 | 1e-14 | 25/48 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.26×** | +5.9 | 4e-07 | 23/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +5.9 | 4e-07 | 26/48 (LoVo, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +5.8 | 8e-07 | 24/47 (SW1417, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.22×** | +5.2 | 2e-05 | 21/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.22×** | +5.1 | 3e-05 | 20/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.18× | +4.3 | 0.001 | 15/48 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +4.1 | 0.002 | 11/48 (COLO 205, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.0 | 0.004 | 19/48 (KATO III, LoVo, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.17× | +4.0 | 0.004 | 16/48 (LoVo, A-172, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.09× | +3.0 | 0.11 | 13/48 (AsPC-1, A498, …) | all doses, flat | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10750.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.840× | -6.4 | 5e-08 | 21/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.841× | -6.4 | 5e-08 | 21/49 (H4, CHP-212, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.807×** | -5.6 | 4e-06 | 23/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.808×** | -5.5 | 4e-06 | 25/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.830×** | -4.8 | 1e-04 | 22/48 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.707×** | -4.7 | 2e-04 | 22/48 (LS 180, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | 0.834× | -4.4 | 9e-04 | 20/44 (C-33 A, HOP62, …) | inconsistent across doses | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.846× | -4.3 | 0.001 | 17/48 (NCI-H23, A-172, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.848× | -4.1 | 0.002 | 15/49 (LOX-IMVI, H4, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.868× | -3.6 | 0.021 | 14/48 (HS-578T, SNU-1, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.837× | -3.3 | 0.049 | 16/48 (H4, MIA PaCa-2, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.884× | -3.1 | 0.096 | 8/47 (NCI-H23, HOP62, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.889× | -3.1 | 0.096 | 10/48 (H4, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10750. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 45.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 58.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +11.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.532× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 60.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.466× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 52.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.453× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 63.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.1) | — |
| [[A498 (line)]] | wt | 50.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 76.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 76.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[H4 (line)]] | wt | 79.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -8.7) ⚠ cell-cycle shift, explains ~16% of this change |
| [[HEC-1-A (line)]] | alt | 75.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +9.2) | — |
| [[J82 (line)]] | alt | 47.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +8.7) | — |
| [[LoVo (line)]] | wt | 59.5 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.25× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 54.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 51.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.396× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SK-MEL-2 (line)]] | alt | 61.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.381× (z -10.2) |
| [[SW480 (line)]] | alt | 57.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +9.1) | — |
| [[A-172 (line)]] | wt | 88.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10750), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM254]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[SETDB1]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[LSM14A]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[PHC3]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[BBS1]] | +0.61 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[TIMM9]] | +0.60 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[TAB1]] | +0.59 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[RBM5]] | +0.59 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[XPA]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[STAT5B]] | +0.58 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[CIAO3]] | +0.58 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[TRMT10B]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDC1]] | -0.59 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[MED12L]] | -0.55 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[LINC02458]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[EPB41L2]] | -0.52 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[FSCN2]] | -0.50 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[STK24]] | -0.50 | -0.56 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises RUFY1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[MED12L]] | B | MED12L activity raises RUFY1's level | lines that do not express MED12L (18) vs lines expressing it (32) | 1.22× lower at baseline in the lines without MED12L | 0.098 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.504). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.9, 4.8); signed map (-4.1, -8.5). **Vector** length 104, 23.6% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +12.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.0 | +8.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.8 | +5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +2.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.3 | +4.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.8 | +2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.3 | -6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.8 | -5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -6.6 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -4.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | -4.9 | -5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -4.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | RUN and FYVE domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:179,550,554-179,610,012 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22251, ZFYVE12, RABIP4 |
| Gene groups (HGNC) | Zinc fingers FYVE-type; RUN domain containing |
| Reactome | 4 pathways, smallest: Synthesis of PIPs at the plasma membrane; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96T51](https://www.uniprot.org/uniprotkb/Q96T51) (RUN and FYVE domain-containing protein 1):

> Activating adapter involved in cargo sorting from early/recycling endosomes. Regulates retrieval of proteins from endosomes to the trans-Golgi network through interaction with the dynein-dynactin complex. Dual effector of RAB4B and RAB14, mediates a cooperative interaction allowing endosomal tethering and fusion. Binds phospholipid vesicles containing phosphatidylinositol 3-phosphate and participates in early endosomal trafficking. In oocytes, self-assembles to form a protein matrix which hold …

**Summary**, from NCBI Gene [80230](https://www.ncbi.nlm.nih.gov/gene/80230):

> This gene encodes a protein that contains a RUN domain and a FYVE-type zinc finger domain. The encoded protein binds to phosphatidylinositol-3-phosphate (PI3P) and plays a role in early endosomal trafficking, tethering and fusion through interactions with small GTPases including Rab4, Rab5 and Rab14. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:19760](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19760) · Entrez [80230](https://www.ncbi.nlm.nih.gov/gene/80230) · UniProt [Q96T51](https://www.uniprot.org/uniprotkb/Q96T51) · Ensembl [ENSG00000176783](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176783)

## Data

Gene col 10750: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10750); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10750, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10750]; `tensor/DDL_lfc|DDL_z.npy` [10750]; `embed/gene_vectors.npy` [10750]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10750 or target_col == 10750). Every well: [[RUFY1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RUFY1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
