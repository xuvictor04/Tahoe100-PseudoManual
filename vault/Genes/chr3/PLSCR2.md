---
symbol: "PLSCR2"
type: "gene"
col: 8771
ensembl_id: "ENSG00000163746"
name: "phospholipid scramblase 2"
location: "3q24"
module: 37
arm: "+"
pooled_cpm: 12.34
n_lines_expressing: 44
n_dd_up: 18
n_dd_down: 17
n_dd_up_clean: 16
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 11
direction_downstream: 15
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# PLSCR2

*phospholipid scramblase 2* — 3q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.65× (z +19.9, q 0e+00, up in 37 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.527× (z -7.4, q 8e-11, down in 28 of 41 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00880]] (+0.75, fdr 1e-05), [[MCF2]] (+0.74, fdr 1e-05), [[IMPA1P1]] (+0.73, fdr 7e-06); moves opposite to [[ELP1]] (-0.60, fdr 3e-04), [[CEP131]] (-0.59, fdr 6e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[PLEKHS1]] → it (grade B ⚠); 15 go from it, the strongest it → [[TBCE]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8771.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.65×** | +19.9 | 0e+00 | 37/39 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **8.17×** | +16.5 | 0e+00 | 31/35 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **5.69×** | +13.6 | 5e-40 | 33/37 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.75×** | +10.8 | 6e-25 | 27/39 (LoVo, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.41×** | +10.1 | 4e-22 | 32/42 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.73×** | +9.9 | 3e-21 | 20/27 (C32, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.62×** | +7.6 | 3e-12 | 23/32 (J82, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.94×** | +5.1 | 2e-05 | 22/40 (A498, A549, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **3.19×** | +4.9 | 5e-05 | 17/41 (LoVo, COLO 205, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +4.2 | 0.001 | 18/41 (HS-578T, CHP-212, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Gefitinib (drug)]] 5 µM |  | **1.59×** | +3.8 | 0.007 | 14/42 (LoVo, COLO 205, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.007 | 17/42 (A498, hTERT-HPNE, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +3.7 | 0.007 | 14/41 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +3.7 | 0.007 | 13/41 (AsPC-1, A549, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.61×** | +3.7 | 0.007 | 14/39 (LoVo, A498, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.069 | 13/40 (LoVo, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +3.0 | 0.078 | 15/40 (LoVo, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8771.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.527×** | -7.4 | 8e-11 | 28/41 (COLO 205, BT-474, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.603×** | -5.9 | 1e-06 | 27/41 (CHP-212, COLO 205, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.274×** | -5.5 | 6e-06 | 21/35 (COLO 205, KATO III, …) | top dose only | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.634×** | -5.3 | 2e-05 | 21/41 (BT-474, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.530×** | -5.2 | 2e-05 | 21/40 (KATO III, COLO 205, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.306×** | -5.1 | 4e-05 | 19/39 (COLO 205, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.546×** | -5.0 | 6e-05 | 23/40 (NCI-H1573, HS-578T, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.557×** | -4.8 | 1e-04 | 23/38 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.679×** | -4.5 | 5e-04 | 20/42 (CHP-212, SHP-77, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.587×** | -4.4 | 8e-04 | 16/40 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.400×** | -3.9 | 0.005 | 10/41 (KATO III, BT-474, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.606×** | -3.9 | 0.005 | 16/39 (NCI-H1573, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.637×** | -3.7 | 0.010 | 18/38 (NCI-H1792, BT-474, …) | rises with dose |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.437×** | -3.5 | 0.016 | 13/35 (BT-474, C32, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.681×** | -3.1 | 0.062 | 15/41 (COLO 205, AsPC-1, …) | inconsistent across doses |  |
| [[Fumaric acid (drug)]] 5 µM |  | **0.684×** | -3.0 | 0.092 | 9/40 (H4, NCI-H1573, …) | top dose only | plate-row cell shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8771. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 9.11 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +13.7) | — |
| [[C32 (line)]] | wt | 13.6 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 33.5× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 19.8× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 15.2 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 91.0× (z +14.5) | — |
| [[LoVo (line)]] | wt | 25.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 23.7× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 4.07 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.35× (z +12.0) | — |
| [[COLO 205 (line)]] | alt | 173 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.292× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 7.36 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 3.72 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +12.0) | — |
| [[NCI-H2347 (line)]] | alt | 8.26 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +12.2) | — |
| [[Panc 03.27 (line)]] | alt | 11.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.88× (z +10.6) | — |
| [[A498 (line)]] | wt | 26.6 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.73× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 47.4 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0214× (z -11.4) |
| [[KATO III (line)]] | alt | 18.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0269× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 5.59 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.67× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 31.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0947× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 5.43 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +10.0) | [[Apalutamide (drug)]] 5 µM 0.0822× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 17.0 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 26.3× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 9.43 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.65× (z +9.7) | [[Silodosin (drug)]] 5 µM 0.0672× (z -9.4) |
| [[A549 (line)]] | wt | 8.12 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 17.3× (z +8.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 9.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.4× (z +12.8) | — |
| [[CHP-212 (line)]] | wt | 41.7 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 5 µM 0.136× (z -9.3) |
| [[H4 (line)]] | wt | 8.02 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 28.9× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 11.6 | 1 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0622× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 8.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.85× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 4.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.07× (z +11.4) | — |
| [[SW 900 (line)]] | alt | 17.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0382× (z -9.5) |
| [[SW1417 (line)]] | alt | 4.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.63× (z +9.7) | — |
| [[A-427 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.75 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8771), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00880]] | +0.75 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[MCF2]] | +0.74 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[IMPA1P1]] | +0.73 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[LINC02955]] | +0.73 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[LINC02936]] | +0.71 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[PXDNL]] | +0.70 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[CASS4]] | +0.70 | +0.71 / +0.39 | both halves | 5e-05 |  |
| [[ST8SIA5]] | +0.69 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[HSD17B3]] | +0.69 | +0.71 / +0.43 | both halves | 4e-05 |  |
| [[SLC26A7]] | +0.68 | +0.71 / +0.43 | both halves | 3e-05 |  |
| [[FBXO39]] | +0.68 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[CORIN]] | +0.68 | +0.69 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELP1]] | -0.60 | -0.58 / -0.27 | both halves | 3e-04 |  |
| [[CEP131]] | -0.59 | -0.52 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 8, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHS1]] | B | PLEKHS1 activity raises PLSCR2's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 1.83× lower at baseline in the lines without PLEKHS1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PLSCR2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FBXO39]] | B | FBXO39 activity raises PLSCR2's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 1.72× lower at baseline in the lines without FBXO39 | 0.034 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[LINC02889]] | B | LINC02889 activity raises PLSCR2's level | lines that do not express LINC02889 (12) vs lines expressing it (38) | 2.24× lower at baseline in the lines without LINC02889 | 0.051 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, SAMD5, ENSG00000226640; maybe low, not absent |
| [[TNFSF14]] | B | TNFSF14 activity raises PLSCR2's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 1.73× lower at baseline in the lines without TNFSF14 | 0.054 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[CTSS]] | B | CTSS activity raises PLSCR2's level | lines that do not express CTSS (15) vs lines expressing it (35) | 1.92× lower at baseline in the lines without CTSS | 0.054 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[NRIR]] | B | NRIR activity raises PLSCR2's level | lines that do not express NRIR (14) vs lines expressing it (36) | 2.12× lower at baseline in the lines without NRIR | 0.070 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[TTC6]] | B | TTC6 activity raises PLSCR2's level | lines that do not express TTC6 (15) vs lines expressing it (35) | 1.67× lower at baseline in the lines without TTC6 | 0.088 | ⚠ within organs, on part of the lines; also absent: SLC27A2, FOXA1, LIMCH1; maybe low, not absent |
| [[SLC2A9]] | C | SLC2A9 activity raises PLSCR2's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 2.76× lower at baseline in the lines without SLC2A9 | 0.022 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent; co-absent with the target |
| [[CEMIP2]] | C | CEMIP2 activity raises PLSCR2's level | lines that do not express CEMIP2 (4) vs lines expressing it (46) | 3.73× lower at baseline in the lines without CEMIP2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KIFC3, SMARCA2, PLSCR2; maybe low, not absent; co-absent with the target; its own permutation p |
| [[CA3]] | C | CA3 activity raises PLSCR2's level | lines that do not express CA3 (10) vs lines expressing it (40) | 2.22× lower at baseline in the lines without CA3 | 0.081 | ⚠ within organs, on part of the lines; also absent: CA13, NAALADL2, PLSCR2; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 11, C 4. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBCE]] | B | PLSCR2 activity lowers TBCE's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 1.31× higher at baseline in the lines without PLSCR2 | 0.021 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent |
| [[PMAIP1]] | B | PLSCR2 activity raises PMAIP1's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 2.83× lower at baseline in the lines without PLSCR2 | 0.023 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent |
| [[MOB3B]] | B | PLSCR2 activity raises MOB3B's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 2.73× lower at baseline in the lines without PLSCR2 | 0.028 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent |
| [[TTC6]] | B | PLSCR2 activity raises TTC6's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 1.78× lower at baseline in the lines without PLSCR2 | 0.046 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent |
| cells under [[Tofacitinib (drug)]] 0.05 µM | B | PLSCR2 activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express PLSCR2 (6) vs lines expressing it (42) | the lines without PLSCR2: 0.75× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent |
| [[RCC1]] | B | PLSCR2 activity lowers RCC1's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 2.00× higher at baseline in the lines without PLSCR2 | 0.063 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent |
| [[BRD7]] | B | PLSCR2 activity lowers BRD7's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 1.46× higher at baseline in the lines without PLSCR2 | 0.077 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent |
| [[IMPA1P1]] | B | PLSCR2 activity raises IMPA1P1's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 1.65× lower at baseline in the lines without PLSCR2 | 0.079 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent |
| [[LINC02889]] | B | PLSCR2 activity raises LINC02889's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 2.29× lower at baseline in the lines without PLSCR2 | 0.089 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent |
| cells under [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM | B | PLSCR2 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express PLSCR2 (6) vs lines expressing it (42) | the lines without PLSCR2: 1.23× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent |
| cells under [[Pralsetinib (drug)]] 0.05 µM | B | PLSCR2 activity lowers the cells' numbers under Pralsetinib 0.05 µM (makes them more sensitive) | lines that do not express PLSCR2 (6) vs lines expressing it (42) | the lines without PLSCR2: 1.24× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent |
| [[CA3]] | C | PLSCR2 activity raises CA3's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 4.69× lower at baseline in the lines without PLSCR2 | 0.002 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.605). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.6, -14.0); signed map (19.6, 2.4). **Vector** length 115, 28.7% of its response variance represented; |z| ≥ 3 in 1,268 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.5 | +19.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +16.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +13.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.4 | +10.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.4 | +5.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.5 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +3.8 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.5 | -4.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.5 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.0 | -5.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.1 | -7.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.0 | -3.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.7 | -5.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.6 | -4.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.4 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | phospholipid scramblase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q24 — chr3:146,391,421-146,495,991 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phospholipid scramblases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRY7](https://www.uniprot.org/uniprotkb/Q9NRY7) (Phospholipid scramblase 2):

> May catalyze calcium-induced ATP-independent rapid bidirectional and non-specific movement of phospholipids (lipid scrambling or lipid flip-flop) between the inner and outer leaflet of the plasma membrane.; [Isoform 1]: Has no phospholipid scramblase activity, due to the lack of a N-terminal proline-rich domain.

**Summary**, from NCBI Gene [57047](https://www.ncbi.nlm.nih.gov/gene/57047):

> This gene encodes a member of the phospholipid scramblase family. Phospholipid scramblases are membrane proteins that mediate calcium-dependent, non-specific movement of plasma membrane phospholipids and phosphatidylserine exposure. The encoded protein contains a low affinity calcium binding motif and may play a role in blood coagulation and apoptosis. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:16494](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16494) · Entrez [57047](https://www.ncbi.nlm.nih.gov/gene/57047) · UniProt [Q9NRY7](https://www.uniprot.org/uniprotkb/Q9NRY7) · Ensembl [ENSG00000163746](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163746)

## Data

Gene col 8771: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8771); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8771, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8771]; `tensor/DDL_lfc|DDL_z.npy` [8771]; `embed/gene_vectors.npy` [8771]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8771 or target_col == 8771). Every well: [[PLSCR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLSCR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
