---
symbol: "IVNS1ABP"
type: "gene"
col: 3820
ensembl_id: "ENSG00000116679"
name: "influenza virus NS1A binding protein"
location: "1q25.3"
module: 12
arm: "-"
pooled_cpm: 83.44
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# IVNS1ABP

*influenza virus NS1A binding protein* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.58× (z +8.7, q 2e-15, up in 37 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (NCI-H2347 3.47×, AsPC-1 2.89×, PANC-1 2.12×, Panc 03.27 2.28×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (C32 2.94×, J82 2.13×, NCI-H1573 2.06×, RPMI-7951 2.16×, …).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.582× (z -7.0, q 1e-09, down in 34 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.681× (z -5.2, q 4e-05, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL15]] (+0.60, fdr 1e-05), [[PRPS2]] (+0.57, fdr 1e-05), [[PTDSS1]] (+0.57, fdr 1e-05); moves opposite to [[PPP6R2]] (-0.55, fdr 1e-05), [[RNFT1]] (-0.55, fdr 2e-05), [[SNX6]] (-0.55, fdr 2e-05).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SPRY4-AS1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3820.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (NCI-H2347 3.47×, AsPC-1 2.89×, PANC-1 2.12×, Panc 03.27 2.28×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (C32 2.94×, J82 2.13×, NCI-H1573 2.06×, RPMI-7951 2.16×, …).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +8.7 | 2e-15 | 37/49 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +4.5 | 0.002 | 24/48 (C32, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +4.3 | 0.003 | 28/48 (C32, NCI-H1792, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3820.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.582×** | -7.0 | 1e-09 | 34/42 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.669×** | -5.4 | 2e-05 | 30/48 (NCI-H2347, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.681×** | -5.2 | 4e-05 | 34/48 (A-172, RKO, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.684×** | -4.9 | 1e-04 | 30/48 (NCI-H460, Hs 766T, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.700×** | -4.8 | 2e-04 | 36/48 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.706×** | -4.7 | 2e-04 | 35/48 (RKO, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.724×** | -4.4 | 0.001 | 31/49 (NCI-H460, A-427, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.742×** | -4.3 | 0.001 | 31/48 (NCI-H460, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.727×** | -4.3 | 0.001 | 28/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.715×** | -4.2 | 0.002 | 26/45 (J82, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.733×** | -4.0 | 0.003 | 27/47 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.765×** | -3.6 | 0.014 | 24/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.776×** | -3.4 | 0.027 | 23/48 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.802×** | -3.3 | 0.043 | 25/50 (NCI-H460, A-427, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.786×** | -3.3 | 0.043 | 26/48 (KATO III, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.792×** | -3.1 | 0.058 | 22/48 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.793×** | -3.1 | 0.058 | 25/48 (hTERT-HPNE, RKO, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.849× | -3.1 | 0.063 | 16/48 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.851× | -3.1 | 0.065 | 21/48 (A498, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3820. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 91.8 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.388× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 97.3 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +18.5) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 79.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.3) | [[Harringtonine (drug)]] 0.5 µM 0.374× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 49.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -10.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 92.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -10.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.628× (z -15.1) ⚠ position not correctable |
| [[C32 (line)]] | wt | 259 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +14.2) | — |
| [[CFPAC-1 (line)]] | alt | 118 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.3) | — |
| [[H4 (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -8.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 74.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 84.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -8.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 75.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.350× (z -9.9) |
| [[LS 180 (line)]] | wt | 82.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.358× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 66.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 58.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 57.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +11.4) | — |
| [[RKO (line)]] | wt | 103 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.330× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 81.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 46.4 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0953× (z -9.0) ⚠ toxic |
| [[SW 900 (line)]] | alt | 82.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +10.0) | — |
| [[A-427 (line)]] | wt | 72.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 81.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 116 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 88.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 140 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 62.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 73.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 76.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 63.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 73.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3820), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL15]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 | same gene group |
| [[PRPS2]] | +0.57 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[PTDSS1]] | +0.57 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[EXTL2]] | +0.55 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[NASP]] | +0.53 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[TPP2]] | +0.53 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[IPO4]] | +0.53 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[NHSL1]] | +0.52 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[SUV39H2]] | +0.52 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[EGR3]] | +0.51 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[ADAMTSL4-AS2]] | +0.51 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[NSUN2]] | +0.51 | +0.45 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP6R2]] | -0.55 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[RNFT1]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[SNX6]] | -0.55 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[ITSN2]] | -0.53 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[TRIP4]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[AP3S2]] | -0.52 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[TRAPPC3]] | -0.52 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[UBA3]] | -0.52 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[NCOA6]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[CEBPZOS]] | -0.51 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[XPA]] | -0.51 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[CENATAC]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPRY4-AS1]] | C | SPRY4-AS1 activity lowers IVNS1ABP's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 1.41× higher at baseline in the lines without SPRY4-AS1 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.329). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-31.8, -37.7); signed map (-31.3, -45.4). **Vector** length 126, 37.1% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.0 | +8.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.3 | +1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +4.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +0.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | +2.2 | +2.5 |
|  | [[EX229 (drug)]] 0.05 µM |  | +2.2 | +1.5 |
|  | [[Malotilate (drug)]] 0.05 µM |  | +2.1 | +1.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.6 | -4.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.4 | -3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.4 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.1 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.0 | -4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.0 | -4.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | influenza virus NS1A binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:185,296,388-185,317,273 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NS1-BP, HSPC068, NS-1, KIAA0850, ND1, KLHL39, ARA3 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6Y0](https://www.uniprot.org/uniprotkb/Q9Y6Y0) (Influenza virus NS1A-binding protein):

> Involved in many cell functions, including pre-mRNA splicing, the aryl hydrocarbon receptor (AHR) pathway, F-actin organization and protein ubiquitination. Plays a role in the dynamic organization of the actin skeleton as a stabilizer of actin filaments by association with F-actin through Kelch repeats (By similarity). Protects cells from cell death induced by actin destabilization (By similarity). Functions as modifier of the AHR/Aryl hydrocarbon receptor pathway increasing the concentration …

**Summary**, from NCBI Gene [10625](https://www.ncbi.nlm.nih.gov/gene/10625):

> Predicted to enable ubiquitin-like ligase-substrate adaptor activity. Involved in RNA splicing; negative regulation of protein ubiquitination; and response to virus. Located in cytosol. Implicated in immunodeficiency 70. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16951](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16951) · Entrez [10625](https://www.ncbi.nlm.nih.gov/gene/10625) · UniProt [Q9Y6Y0](https://www.uniprot.org/uniprotkb/Q9Y6Y0) · Ensembl [ENSG00000116679](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116679)

## Data

Gene col 3820: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3820); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3820, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3820]; `tensor/DDL_lfc|DDL_z.npy` [3820]; `embed/gene_vectors.npy` [3820]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3820 or target_col == 3820). Every well: [[IVNS1ABP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IVNS1ABP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
