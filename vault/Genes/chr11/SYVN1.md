---
symbol: "SYVN1"
type: "gene"
col: 8496
ensembl_id: "ENSG00000162298"
name: "synoviolin 1"
location: "11q13.1"
module: 40
arm: "+"
pooled_cpm: 21.29
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 13
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# SYVN1

*synoviolin 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +9.1, q 8e-17, up in 35 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A549 3.73×, NCI-H460 3.12×, SW480 2.52×).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.547× (z -6.9, q 2e-09, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YIPF2]] (+0.77, fdr 7e-06), [[ARFGAP1]] (+0.77, fdr 7e-06), [[BET1L]] (+0.75, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[EIF2AK3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8496.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A549 3.73×, NCI-H460 3.12×, SW480 2.52×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +9.1 | 8e-17 | 35/47 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +4.0 | 0.015 | 24/44 (RPMI-7951, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.5 | 0.075 | 1/48 (HS-578T) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | 1.30× | +3.1 | 0.20 | 17/48 (LOX-IMVI, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | 1.30× | +3.1 | 0.20 | 13/48 (SHP-77, NCI-H1573, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8496.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.547×** | -6.9 | 2e-09 | 33/47 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.622×** | -5.7 | 3e-06 | 28/37 (AsPC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.659×** | -4.8 | 3e-04 | 22/33 (LS 180, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.740×** | -4.4 | 0.002 | 21/47 (A498, HS-578T, …) | inconsistent across doses | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.704×** | -4.2 | 0.003 | 24/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.544×** | -3.8 | 0.013 | 20/48 (NCI-H1792, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.741×** | -3.6 | 0.025 | 22/46 (BT-474, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.743×** | -3.6 | 0.025 | 21/48 (HOP62, A-172, …) | inconsistent across doses | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.755×** | -3.4 | 0.043 | 19/45 (SW480, KATO III, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.756×** | -3.4 | 0.043 | 19/48 (HT-29, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **0.741×** | -3.3 | 0.043 | 17/34 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Berbamine (drug)]] 0.05 µM |  | **0.759×** | -3.3 | 0.043 | 17/48 (SW 1088, LS 180, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.769×** | -3.2 | 0.069 | 17/48 (COLO 205, SW 1088, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8496. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 20.1 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.191× (z -12.3) |
| [[A549 (line)]] | wt | 16.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[HS-578T (line)]] | alt | 34.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -10.9) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.239× (z -9.2) |
| [[A-172 (line)]] | wt | 15.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -9.1) ⚠ cell-cycle shift, explains ~52% of this change |
| [[AsPC-1 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.243× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[H4 (line)]] | wt | 27.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -8.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 45.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 33.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 19.5 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0293× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 11.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 18.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.309× (z -9.2) |
| [[SNU-1 (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.110× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.260× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 19.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +8.9) | — |
| [[A-427 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8496), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIPF2]] | +0.77 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[ARFGAP1]] | +0.77 | +0.77 / +0.72 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation |
| [[BET1L]] | +0.75 | +0.73 / +0.73 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 486 |
| [[MOGS]] | +0.71 | +0.73 / +0.66 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SURF4]] | +0.70 | +0.72 / +0.67 | both halves | 7e-06 | STRING 455 |
| [[MGAT1]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC61A1]] | +0.70 | +0.77 / +0.61 | both halves | 7e-06 | STRING 900 |
| [[C2CD2L]] | +0.69 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[NDEL1]] | +0.69 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[CDK2AP2]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[GMPPA]] | +0.68 | +0.72 / +0.62 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[OSBPL2]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EIF2AK3]] | C | SYVN1's natural level strengthens EIF2AK3's drug response | SYVN1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.43; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Belzutifan (drug)]] 5 µM | C | SYVN1's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | SYVN1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.60 | 0.465 over the table, 0.076 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.652). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (10.2, -30.7); signed map (-50.1, 5.0). **Vector** length 105, 25.6% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +9.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +5.1 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.8 | +1.5 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.8 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | -0.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.9 | -6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -3.6 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -2.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.7 | -3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | synoviolin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,121,780-65,134,532 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HRD1, DER3 |
| Gene groups (HGNC) | Ring finger proteins; MicroRNA protein coding host genes; RING finger E3 ubiquitin protein ligases |
| Reactome | 14 pathways, smallest: ER Quality Control Compartment (ERQC); Calnexin/calreticulin cycle; N-glycan trimming in the ER and Calnexin/Calreticulin cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86TM6](https://www.uniprot.org/uniprotkb/Q86TM6) (E3 ubiquitin-protein ligase synoviolin):

> E3 ubiquitin-protein ligase which accepts ubiquitin specifically from endoplasmic reticulum-associated UBC7 E2 ligase and transfers it to substrates, promoting their degradation. Component of the endoplasmic reticulum quality control (ERQC) system also called ER-associated degradation (ERAD) involved in ubiquitin-dependent degradation of misfolded endoplasmic reticulum proteins. Also promotes the degradation of normal but naturally short-lived proteins such as SGK. Protects cells from ER …

**Summary**, from NCBI Gene [84447](https://www.ncbi.nlm.nih.gov/gene/84447):

> This gene encodes a protein involved in endoplasmic reticulum (ER)-associated degradation. The encoded protein removes unfolded proteins, accumulated during ER stress, by retrograde transport to the cytosol from the ER. This protein also uses the ubiquitin-proteasome system for additional degradation of unfolded proteins. Sequence analysis identified two transcript variants that encode different isoforms. [provided by RefSeq, May 2011]

**Accessions** — [HGNC:20738](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20738) · Entrez [84447](https://www.ncbi.nlm.nih.gov/gene/84447) · UniProt [Q86TM6](https://www.uniprot.org/uniprotkb/Q86TM6) · Ensembl [ENSG00000162298](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162298)

## Data

Gene col 8496: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8496); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8496, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8496]; `tensor/DDL_lfc|DDL_z.npy` [8496]; `embed/gene_vectors.npy` [8496]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8496 or target_col == 8496). Every well: [[SYVN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYVN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
