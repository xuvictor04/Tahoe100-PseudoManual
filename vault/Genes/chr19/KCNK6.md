---
symbol: "KCNK6"
type: "gene"
col: 1796
ensembl_id: "ENSG00000099337"
name: "potassium two pore domain channel subfamily K member 6"
location: "19q13.2"
module: 41
arm: "+"
pooled_cpm: 35.85
n_lines_expressing: 38
n_dd_up: 2
n_dd_down: 38
n_dd_up_clean: 2
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 5
direction_downstream: 17
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# KCNK6

*potassium two pore domain channel subfamily K member 6* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 2.13× (z +7.2, q 4e-10, up in 28 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (SW480 4.53×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 3.50×; ⚠ cell-cycle shift, explains ~33% of this change).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.241× (z -18.9, q 0e+00, down in 34 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACBD3]] (+0.66, fdr 1e-05), [[RABGEF1]] (+0.66, fdr 7e-06), [[PHKG1]] (+0.65, fdr 1e-05); moves opposite to [[CAPRIN1]] (-0.65, fdr 1e-05), [[NONO]] (-0.62, fdr 4e-05), [[NELFCD]] (-0.61, fdr 1e-04).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[KCNK1]] → it (grade B ⚠); 17 go from it, the strongest it → [[RAB5A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1796.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (SW480 4.53×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 3.50×; ⚠ cell-cycle shift, explains ~33% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.13×** | +7.2 | 4e-10 | 28/35 (SW480, SW48, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.87×** | +3.6 | 0.075 | 20/34 (SW480, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sodium Salicylate (drug)]] 5 µM |  | 1.29× | +3.4 | 0.11 | 19/36 (HCT15, J82, …) | top dose only | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.46× | +3.4 | 0.11 | 17/36 (KATO III, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | 1.72× | +3.2 | 0.18 | 15/35 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1796.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.241×** | -18.9 | 0e+00 | 34/36 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.203×** | -14.4 | 2e-44 | 36/36 (Panc 03.27, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.266×** | -12.4 | 3e-33 | 30/36 (HT-29, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.329×** | -10.4 | 3e-23 | 32/36 (HT-29, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.370×** | -9.3 | 1e-18 | 33/36 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.374×** | -9.2 | 3e-18 | 34/36 (hTERT-HPNE, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.426×** | -8.0 | 1e-13 | 31/35 (hTERT-HPNE, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.205×** | -7.8 | 6e-13 | 34/37 (HT-29, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.511×** | -6.3 | 2e-08 | 27/36 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.636×** | -6.0 | 1e-07 | 24/36 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.297×** | -6.0 | 1e-07 | 28/35 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.545×** | -5.7 | 7e-07 | 23/34 (HOP62, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.549×** | -5.6 | 9e-07 | 25/35 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.622×** | -4.4 | 4e-04 | 22/36 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.418×** | -4.3 | 7e-04 | 24/36 (HT-29, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.634×** | -4.0 | 0.002 | 18/36 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.740×** | -4.0 | 0.003 | 21/36 (hTERT-HPNE, SNU-423, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.642×** | -3.9 | 0.003 | 18/35 (BT-474, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.59 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1796. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 49.9 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -16.0) |
| [[HOP62 (line)]] | alt | 22.4 | 0 | 10 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0751× (z -14.3) |
| [[HS-578T (line)]] | alt | 21.9 | 0 | 9 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0772× (z -13.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.0835× (z -13.0) |
| [[KATO III (line)]] | alt | 124 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -19.7) |
| [[HT-29 (line)]] | alt | 99.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -15.8) |
| [[MIA PaCa-2 (line)]] | alt | 54.7 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0675× (z -13.3) |
| [[RKO (line)]] | wt | 37.4 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -16.9) |
| [[SW480 (line)]] | alt | 34.7 | 1 | 5 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.53× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.150× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 61.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -22.5) |
| [[COLO 205 (line)]] | alt | 93.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -16.7) |
| [[Hs 766T (line)]] | wt | 66.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -15.3) |
| [[LoVo (line)]] | wt | 121 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.144× (z -13.5) |
| [[NCI-H2347 (line)]] | alt | 41.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -18.9) |
| [[Panc 03.27 (line)]] | alt | 63.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0804× (z -25.9) |
| [[PANC-1 (line)]] | alt | 31.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -16.0) |
| [[BT-474 (line)]] | alt | 37.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -16.9) |
| [[LS 180 (line)]] | wt | 47.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -14.4) |
| [[NCI-H1573 (line)]] | alt | 45.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 18.8 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0271× (z -16.1) |
| [[SNU-423 (line)]] | alt | 18.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -12.8) |
| [[SW 900 (line)]] | alt | 17.7 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0615× (z -12.5) |
| [[A549 (line)]] | wt | 20.3 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +9.3) ⚠ cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -14.4) |
| [[AsPC-1 (line)]] | alt | 95.9 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.294× (z -9.7) |
| [[HCT15 (line)]] | alt | 76.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.137× (z -12.6) |
| [[J82 (line)]] | alt | 12.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0948× (z -10.5) |
| [[A498 (line)]] | wt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -15.5) |
| [[SW1417 (line)]] | alt | 33.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -11.7) |
| [[SW48 (line)]] | wt | 56.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -9.1) |
| [[A-172 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.08 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.84 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.96 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.24 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.51 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.03 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1796), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACBD3]] | +0.66 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[RABGEF1]] | +0.66 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[PHKG1]] | +0.65 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[SRP54]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ARID3A]] | +0.62 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[ZNF841]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[ATG101]] | +0.62 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[TINCR]] | +0.62 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[HM13]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[RAB5A]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[SPTY2D1]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[PGM3]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPRIN1]] | -0.65 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[NONO]] | -0.62 | -0.42 / -0.69 | both halves | 4e-05 |  |
| [[NELFCD]] | -0.61 | -0.34 / -0.71 | both halves | 1e-04 |  |
| [[XRCC6]] | -0.59 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[MBTPS2]] | -0.59 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[HNRNPK]] | -0.58 | -0.43 / -0.61 | both halves | 4e-05 |  |
| [[EWSR1]] | -0.57 | -0.40 / -0.66 | both halves | 4e-05 |  |
| [[EXOSC10]] | -0.57 | -0.34 / -0.63 | both halves | 1e-04 |  |
| [[ZMYND11]] | -0.57 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[CBX5]] | -0.57 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[COPS6]] | -0.56 | -0.38 / -0.59 | both halves | 7e-05 |  |
| [[SRP9]] | -0.56 | -0.25 / -0.63 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNK1]] | B | KCNK1 activity raises KCNK6's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 3.31× lower at baseline in the lines without KCNK1 | 0.023 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[S100A14]] | B | S100A14 activity raises KCNK6's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 3.19× lower at baseline in the lines without S100A14 | 0.040 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |
| [[PRSS8]] | B | PRSS8 activity raises KCNK6's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 3.11× lower at baseline in the lines without PRSS8 | 0.080 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[GALNT3]] | B | GALNT3 activity raises KCNK6's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 3.24× lower at baseline in the lines without GALNT3 | 0.089 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity raises KCNK6's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 1.38× lower at baseline in the lines without TMEM92-AS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB5A]] | B | KCNK6 activity raises RAB5A's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 1.39× lower at baseline in the lines without KCNK6 | 0.008 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[HLA-F-AS1]] | B | KCNK6 activity raises HLA-F-AS1's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 2.10× lower at baseline in the lines without KCNK6 | 0.026 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[PTP4A1]] | B | KCNK6 activity lowers PTP4A1's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 1.83× higher at baseline in the lines without KCNK6 | 0.031 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[KCNK1]] | B | KCNK6 activity raises KCNK1's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 4.49× lower at baseline in the lines without KCNK6 | 0.037 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[SMARCD1]] | B | KCNK6 activity lowers SMARCD1's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 1.36× higher at baseline in the lines without KCNK6 | 0.050 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[PDXK]] | B | KCNK6 activity raises PDXK's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 1.62× lower at baseline in the lines without KCNK6 | 0.060 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[NHLRC2]] | B | KCNK6 activity lowers NHLRC2's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 1.30× higher at baseline in the lines without KCNK6 | 0.060 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[DEDD2]] | B | KCNK6 activity raises DEDD2's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 1.54× lower at baseline in the lines without KCNK6 | 0.063 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[BET1L]] | B | KCNK6 activity raises BET1L's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without KCNK6 | 0.077 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[APEX1]] | B | KCNK6 activity lowers APEX1's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 1.30× higher at baseline in the lines without KCNK6 | 0.078 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[GALNT3]] | B | KCNK6 activity raises GALNT3's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 4.27× lower at baseline in the lines without KCNK6 | 0.078 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[LINC02649]] | B | KCNK6 activity raises LINC02649's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 1.97× lower at baseline in the lines without KCNK6 | 0.079 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.537). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (19.3, -36.8); signed map (-17.5, 17.2). **Vector** length 104, 32.9% of its response variance represented; |z| ≥ 3 in 916 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.2 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +0.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.6 | -6.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.9 | +3.4 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -3.9 | -2.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.8 | -7.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -6.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.2 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.1 | -9.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -6.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | potassium two pore domain channel subfamily K member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,319,845-38,332,076 (+) |
| Ensembl biotype | protein_coding |
| Also known as | K2p6.1, TWIK-2 |
| Gene groups (HGNC) | Potassium two pore domain channel subfamily K |
| Reactome | 6 pathways, smallest: Tandem pore domain potassium channels; Phase 4 - resting membrane potential; Potassium Channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y257](https://www.uniprot.org/uniprotkb/Q9Y257) (Potassium channel subfamily K member 6):

> K(+) channel that conducts outward rectifying currents at the membranes of the endolysosomal system. Active in lysosomes where it regulates lysosome numbers and size. In macrophages, enables K(+) efflux coupled to ATP-induced NLRP3 inflammasome activation upon bacterial infection. Cooperates with ATP-gated P2RX7 channels to activate NLRP3 inflammasome, with P2RX7 conducting Ca(2+) and Na(+) influx that sets the membrane potential for K(+) efflux (By similarity).; [Isoform 2]: Does not display …

**Summary**, from NCBI Gene [9424](https://www.ncbi.nlm.nih.gov/gene/9424):

> This gene encodes one of the members of the superfamily of potassium channel proteins containing two pore-forming P domains. This channel protein, considered an open rectifier, is widely expressed. It is stimulated by arachidonic acid, and inhibited by internal acidification and volatile anaesthetics. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6281](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6281) · Entrez [9424](https://www.ncbi.nlm.nih.gov/gene/9424) · UniProt [Q9Y257](https://www.uniprot.org/uniprotkb/Q9Y257) · Ensembl [ENSG00000099337](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099337)

## Data

Gene col 1796: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1796); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1796, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1796]; `tensor/DDL_lfc|DDL_z.npy` [1796]; `embed/gene_vectors.npy` [1796]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1796 or target_col == 1796). Every well: [[KCNK6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNK6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
