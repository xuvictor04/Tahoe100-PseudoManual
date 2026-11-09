---
symbol: "DMTN"
type: "gene"
col: 8198
ensembl_id: "ENSG00000158856"
name: "dematin actin binding protein"
location: "8p21.3"
module: 27
arm: "+"
pooled_cpm: 7.17
n_lines_expressing: 36
n_dd_up: 6
n_dd_down: 24
n_dd_up_clean: 0
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 4
direction_downstream: 27
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# DMTN

*dematin actin binding protein* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.09× (z +13.2, q 8e-37, up in 5 of 10 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 5.24×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.333× (z -13.4, q 6e-38, down in 30 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP1G2]] (+0.64, fdr 9e-06), [[LPIN3]] (+0.61, fdr 2e-05), [[NEIL1]] (+0.61, fdr 2e-05); moves opposite to [[GLIS3]] (-0.49, fdr 4e-05), [[HS3ST3A1]] (-0.48, fdr 1e-04), [[DNAAF9]] (-0.48, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[DSCAML1]] → it (grade B ⚠); 27 go from it, the strongest it → [[TSHZ3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8198.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 5.24×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.09×** | +13.2 | 8e-37 | 5/10 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.32×** | +10.2 | 4e-22 | 13/20 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +7.8 | 1e-12 | 4/12 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.28×** | +4.2 | 0.004 | 6/33 (LoVo, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.1 | 0.004 | 2/34 (MIA PaCa-2, NCI-H23) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +3.5 | 0.046 | 6/22 (LS 180, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.3 | 0.082 | 0/15 | top dose only | noisy plate (z scaled) |
| [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | 1.30× | +3.1 | 0.12 | 6/31 (A549, HepG2/C3A, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 1.29× | +3.1 | 0.13 | 6/30 (HCT15, HT-29, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.29× | +3.1 | 0.13 | 6/33 (A549, LoVo, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8198.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.333×** | -13.4 | 6e-38 | 30/33 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.392×** | -11.4 | 1e-27 | 30/34 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.527×** | -11.0 | 6e-26 | 22/29 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.429×** | -10.3 | 1e-22 | 24/34 (LoVo, SW480, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.443×** | -9.9 | 6e-21 | 21/30 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.431×** | -9.8 | 7e-21 | 24/33 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.450×** | -9.7 | 3e-20 | 24/29 (HepG2/C3A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.463×** | -9.4 | 6e-19 | 27/34 (LoVo, SW48, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.627×** | -8.0 | 7e-14 | 23/29 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.591×** | -6.4 | 9e-09 | 15/32 (NCI-H1792, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~23% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.645×** | -5.3 | 5e-06 | 10/33 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.445×** | -5.1 | 1e-05 | 16/31 (LoVo, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.680×** | -4.7 | 1e-04 | 14/31 (A-172, HCT15, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.704×** | -4.3 | 8e-04 | 18/30 (RKO, NCI-H23, …) | two highest doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.706×** | -4.2 | 9e-04 | 12/34 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.787×** | -4.1 | 0.001 | 11/34 (HEC-1-A, NCI-H1792, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.760×** | -3.3 | 0.027 | 8/33 (A549, MIA PaCa-2, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.597×** | -3.3 | 0.030 | 6/28 (LS 180, KATO III, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8198. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 28.8 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -13.6) |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0840× (z -12.8) |
| [[SW480 (line)]] | alt | 13.8 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0931× (z -16.1) |
| [[LoVo (line)]] | wt | 14.5 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.24× (z +10.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.0639× (z -17.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.153× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 0 | 5 | — | [[Harringtonine (drug)]] 5 µM 0.0348× (z -15.7) |
| [[HCT15 (line)]] | alt | 15.4 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -9.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.133× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 40.6 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.112× (z -12.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.168× (z -10.2) |
| [[SW48 (line)]] | wt | 15.0 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0777× (z -10.7) |
| [[A-172 (line)]] | wt | 7.39 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -10.0) |
| [[A549 (line)]] | wt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 6.40 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -9.7) |
| [[COLO 205 (line)]] | alt | 7.51 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0749× (z -8.5) |
| [[HT-29 (line)]] | alt | 3.34 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -10.6) |
| [[KATO III (line)]] | alt | 10.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 5.44 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0881× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 5.06 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0891× (z -8.6) |
| [[RKO (line)]] | wt | 9.39 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.118× (z -9.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.756 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.963 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8198), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP1G2]] | +0.64 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[LPIN3]] | +0.61 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[NEIL1]] | +0.61 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[ERBB2]] | +0.59 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[SORL1]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[SLC44A3]] | +0.57 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[EPS8L3]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[EVPL]] | +0.55 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[B3GAT1-DT]] | +0.55 | +0.37 / +0.54 | both halves | 8e-05 |  |
| [[MIR3936HG]] | +0.55 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[LINC02058]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[SLC44A3-AS1]] | +0.54 | +0.51 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLIS3]] | -0.49 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[HS3ST3A1]] | -0.48 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[DNAAF9]] | -0.48 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[DDX50]] | -0.47 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[NAV1]] | -0.46 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[PCBP3]] | -0.45 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[DYNLT1]] | -0.45 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[ABL1]] | -0.45 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[TSHZ3]] | -0.45 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[MSX2]] | -0.45 | -0.47 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSCAML1]] | B | DSCAML1 activity raises DMTN's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 2.41× lower at baseline in the lines without DSCAML1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[NOXA1]] | B | NOXA1 activity raises DMTN's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 2.53× lower at baseline in the lines without NOXA1 | 0.093 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[EVPL]] | C | EVPL activity raises DMTN's level | lines that do not express EVPL (16) vs lines expressing it (34) | 2.58× lower at baseline in the lines without EVPL | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: PTK6, MYO5C, SFN; co-absent with the target |
| [[SCNN1A]] | C | SCNN1A activity raises DMTN's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 2.30× lower at baseline in the lines without SCNN1A | 0.060 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 25, C 2. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSHZ3]] | B | DMTN activity lowers TSHZ3's level | lines that do not express DMTN (14) vs lines expressing it (36) | 4.54× higher at baseline in the lines without DMTN | 0.007 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[WNT5A]] | B | DMTN activity lowers WNT5A's level | lines that do not express DMTN (14) vs lines expressing it (36) | 6.23× higher at baseline in the lines without DMTN | 0.011 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[SLC44A3]] | B | DMTN activity raises SLC44A3's level | lines that do not express DMTN (14) vs lines expressing it (36) | 2.77× lower at baseline in the lines without DMTN | 0.013 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[PLXNB1]] | B | DMTN activity raises PLXNB1's level | lines that do not express DMTN (14) vs lines expressing it (36) | 2.01× lower at baseline in the lines without DMTN | 0.014 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[TMEM184A]] | B | DMTN activity raises TMEM184A's level | lines that do not express DMTN (14) vs lines expressing it (36) | 2.50× lower at baseline in the lines without DMTN | 0.016 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[ERBB3]] | B | DMTN activity raises ERBB3's level | lines that do not express DMTN (14) vs lines expressing it (36) | 4.52× lower at baseline in the lines without DMTN | 0.031 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[LRP5]] | B | DMTN activity raises LRP5's level | lines that do not express DMTN (14) vs lines expressing it (36) | 2.49× lower at baseline in the lines without DMTN | 0.032 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[HSD3B7]] | B | DMTN activity raises HSD3B7's level | lines that do not express DMTN (14) vs lines expressing it (36) | 1.70× lower at baseline in the lines without DMTN | 0.033 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[SLC44A3-AS1]] | B | DMTN activity raises SLC44A3-AS1's level | lines that do not express DMTN (14) vs lines expressing it (36) | 2.85× lower at baseline in the lines without DMTN | 0.039 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[ABL1]] | B | DMTN activity weakens ABL1's drug response | lines that do not express DMTN (14) vs lines expressing it (36) | the lines without DMTN respond 1.45× as strongly (z diff -1.93); strongest at Panobinostat 0.5 µM: 0.56x vs 0.87x (z diff -3.9) | 0.046 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent; artifact flags |
| [[PRR16]] | B | DMTN activity lowers PRR16's level | lines that do not express DMTN (14) vs lines expressing it (36) | 4.25× higher at baseline in the lines without DMTN | 0.053 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[PSD4]] | B | DMTN activity raises PSD4's level | lines that do not express DMTN (14) vs lines expressing it (36) | 2.38× lower at baseline in the lines without DMTN | 0.057 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.512). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.8, 30.5); signed map (39.1, -14.0). **Vector** length 57.0, 9.89% of its response variance represented; |z| ≥ 3 in 807 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +7.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.0 | +4.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.6 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | -1.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -6.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.4 | -9.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.1 | -5.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.0 | -1.6 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -0.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | dematin actin binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:22,048,995-22,082,527 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DMT; previously EPB49 |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 2 pathways, smallest: Miscellaneous transport and binding events; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08495](https://www.uniprot.org/uniprotkb/Q08495) (Dematin):

> Membrane-cytoskeleton-associated protein with F-actin-binding activity that induces F-actin bundles formation and stabilization. Its F-actin-bundling activity is reversibly regulated upon its phosphorylation by the cAMP-dependent protein kinase A (PKA). Binds to the erythrocyte membrane glucose transporter-1 SLC2A1/GLUT1, and hence stabilizes and attaches the spectrin-actin network to the erythrocytic plasma membrane. Plays a role in maintaining the functional integrity of PKA-activated …

**Summary**, from NCBI Gene [2039](https://www.ncbi.nlm.nih.gov/gene/2039):

> The protein encoded by this gene is an actin binding and bundling protein that plays a structural role in erythrocytes, by stabilizing and attaching the spectrin/actin cytoskeleton to the erythrocyte membrane in a phosphorylation-dependent manner. This protein contains a core domain in the N-terminus, and a headpiece domain in the C-terminus that binds F-actin. When purified from erythrocytes, this protein exists as a trimer composed of two 48 kDa polypeptides and a 52 kDa polypeptide. The …

**Accessions** — [HGNC:3382](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3382) · Entrez [2039](https://www.ncbi.nlm.nih.gov/gene/2039) · UniProt [Q08495](https://www.uniprot.org/uniprotkb/Q08495) · Ensembl [ENSG00000158856](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158856)

## Data

Gene col 8198: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8198); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8198, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8198]; `tensor/DDL_lfc|DDL_z.npy` [8198]; `embed/gene_vectors.npy` [8198]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8198 or target_col == 8198). Every well: [[DMTN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DMTN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
