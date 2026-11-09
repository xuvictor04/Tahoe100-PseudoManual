---
symbol: "KBTBD11"
type: "gene"
col: 10733
ensembl_id: "ENSG00000176595"
name: "kelch repeat and BTB domain containing 11"
location: "8p23.3"
module: 4
arm: "+"
pooled_cpm: 4.47
n_lines_expressing: 38
n_dd_up: 6
n_dd_down: 18
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# KBTBD11

*kelch repeat and BTB domain containing 11* — 8p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.05× (z +8.3, q 7e-14, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.67× (z +6.2, q 2e-07, up in 17 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.433× (z -14.3, q 2e-43, down in 22 of 30 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XK]] (+0.68, fdr 1e-05), [[LINC01357]] (+0.64, fdr 9e-06), [[ASIC1]] (+0.63, fdr 1e-05); moves opposite to [[ARID4A]] (-0.49, fdr 4e-05), [[DYNC2I1]] (-0.49, fdr 9e-05), [[ANKHD1]] (-0.48, fdr 1e-04).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[BTNL9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10733.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +8.3 | 7e-14 | 3/4 (CFPAC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +6.2 | 2e-07 | 17/32 (NCI-H2347, LS 180, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.023 | 5/28 (PANC-1, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +3.7 | 0.033 | 6/20 (AsPC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.23×** | +3.6 | 0.042 | 3/35 (A549, LoVo, …) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.081 | 10/34 (NCI-H2347, H4, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.29× | +3.0 | 0.20 | 1/34 (NCI-H2347) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10733.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.433×** | -14.3 | 2e-43 | 22/30 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.575×** | -6.4 | 4e-08 | 17/32 (A549, NCI-H1792, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.599×** | -6.2 | 1e-07 | 18/35 (SW 900, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.594×** | -6.0 | 2e-07 | 14/27 (RKO, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.668×** | -4.9 | 1e-04 | 11/34 (A549, SW 900, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.671×** | -4.8 | 1e-04 | 13/30 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.677×** | -4.7 | 2e-04 | 15/34 (SW48, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.764×** | -4.6 | 3e-04 | 11/27 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.700×** | -4.3 | 0.001 | 13/34 (LOX-IMVI, HCT15, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.703×** | -4.1 | 0.002 | 14/31 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.534×** | -3.9 | 0.004 | 9/28 (A-427, A-172, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.538×** | -3.9 | 0.004 | 11/31 (LS 180, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.724×** | -3.9 | 0.004 | 11/32 (NCI-H23, SW 900, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM |  | **0.765×** | -3.2 | 0.050 | 4/34 (H4, Hs 766T, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.771×** | -3.1 | 0.065 | 2/34 (PANC-1, A549) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.777×** | -3.0 | 0.077 | 13/34 (LOX-IMVI, SK-MEL-2, …) | two highest doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.705×** | -3.0 | 0.085 | 9/29 (NCI-H460, CFPAC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10733. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 15.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0831× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 9.19 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -9.5) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 6.40 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0644× (z -13.6) |
| [[A-172 (line)]] | wt | 4.91 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -8.5) |
| [[A549 (line)]] | wt | 8.89 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -10.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 2.16 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0880× (z -9.7) |
| [[LoVo (line)]] | wt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -14.6) |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 7.60 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0661× (z -11.3) |
| [[SW48 (line)]] | wt | 27.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -8.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.653 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.539 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.940 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10733), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XK]] | +0.68 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[LINC01357]] | +0.64 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[ASIC1]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[MCOLN2]] | +0.59 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[SLC19A1]] | +0.58 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[BTNL9]] | +0.57 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[SPTBN2]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ZC3HAV1L]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[RAB4A-AS1]] | +0.55 | +0.38 / +0.54 | both halves | 7e-05 |  |
| [[KIAA1549]] | +0.54 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[MAT2A]] | +0.54 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[SORD]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID4A]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[DYNC2I1]] | -0.49 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[ANKHD1]] | -0.48 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[GPS2]] | -0.46 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[ZMYM5]] | -0.46 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[GPATCH1]] | -0.46 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[BBOF1]] | -0.45 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[LRRC37A2]] | -0.45 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[NUDT16L1]] | -0.45 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[MED19]] | -0.45 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[DNAL4]] | -0.44 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[SUCLG1]] | -0.44 | -0.38 / -0.48 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BTNL9]] | B | BTNL9 activity raises KBTBD11's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 2.36× lower at baseline in the lines without BTNL9 | 0.007 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |
| [[XK]] | B | XK activity raises KBTBD11's level | lines that do not express XK (18) vs lines expressing it (32) | 1.95× lower at baseline in the lines without XK | 0.022 | ⚠ within organs, on part of the lines; also absent: SAMD12, MARVELD2, BTC; maybe low, not absent |
| [[SPTBN2]] | C | SPTBN2 activity raises KBTBD11's level | lines that do not express SPTBN2 (9) vs lines expressing it (41) | 2.74× lower at baseline in the lines without SPTBN2 | 0.018 | ⚠ within organs, on part of the lines; also absent: CCDC88C, HID1, ASS1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.415). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (0.9, 42.4); signed map (-6.0, -57.3). **Vector** length 45.6, 6.10% of its response variance represented; |z| ≥ 3 in 826 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.2 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +2.6 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.6 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.9 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.9 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.8 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.8 | -6.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.1 | -4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -1.0 | -6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -1.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Rucaparib (phosphate) (drug)]] 5 µM |  | -0.7 | -2.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.7 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | -0.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -0.6 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | kelch repeat and BTB domain containing 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.3 — chr8:1,973,677-2,006,936 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0711, KLHDC7C |
| Gene groups (HGNC) | BTB domain containing |
| Matched by | ensembl_id |

UniProt [O94819](https://www.uniprot.org/uniprotkb/O94819) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:29104](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29104) · Entrez [9920](https://www.ncbi.nlm.nih.gov/gene/9920) · UniProt [O94819](https://www.uniprot.org/uniprotkb/O94819) · Ensembl [ENSG00000176595](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176595)

## Data

Gene col 10733: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10733); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10733, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10733]; `tensor/DDL_lfc|DDL_z.npy` [10733]; `embed/gene_vectors.npy` [10733]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10733 or target_col == 10733). Every well: [[KBTBD11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KBTBD11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
