---
symbol: "TMEM158"
type: "gene"
col: 14656
ensembl_id: "ENSG00000249992"
name: "transmembrane protein 158"
location: "3p21.31"
module: 81
arm: "+"
pooled_cpm: 39.65
n_lines_expressing: 31
n_dd_up: 3
n_dd_down: 44
n_dd_up_clean: 1
n_dd_down_clean: 37
in_vector_space: true
direction_upstream: 19
direction_downstream: 28
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# TMEM158

*transmembrane protein 158* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.28× (z +5.0, q 4e-04, up in 20 of 27 measured lines) ⚠ toxic. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 2.71× (z +3.5, q 0.082, up in 24 of 29 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 1 line (RKO 5.39×).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (7 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.234× (z -8.7, q 2e-15, down in 27 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STC1]] (+0.79, fdr 7e-06), [[BCL2A1]] (+0.77, fdr 7e-06), [[ANTXR2]] (+0.72, fdr 7e-06); moves opposite to [[ALDH3B1]] (-0.61, fdr 1e-05), [[MGST1]] (-0.60, fdr 2e-05), [[PDLIM1]] (-0.60, fdr 1e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[MMP1]] → it (grade B ⚠); 28 go from it, the strongest it → [[ENTPD7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14656.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 1 line (RKO 5.39×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +5.0 | 4e-04 | 20/27 (AsPC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.76×** | +3.6 | 0.082 | 14/29 (Hs 766T, NCI-H1792, …) | top dose only | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **2.71×** | +3.5 | 0.082 | 24/29 (C32, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.45× | +3.3 | 0.11 | 15/29 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.72× | +3.3 | 0.11 | 18/29 (Hs 766T, Panc 03.27, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 1.44× | +3.3 | 0.11 | 19/29 (C32, AsPC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | 1.83× | +3.1 | 0.14 | 11/26 (A-172, NCI-H1792, …) | inconsistent across doses | composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 2.40× | +3.1 | 0.14 | 19/29 (RKO, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~76% of this change | 1.61× | +3.0 | 0.16 | 15/29 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14656.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.234×** | -8.7 | 2e-15 | 27/28 (A-172, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.252×** | -7.7 | 4e-12 | 29/29 (A-172, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.310×** | -7.0 | 4e-10 | 27/29 (HS-578T, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.450×** | -6.9 | 6e-10 | 29/29 (C32, NCI-H2347, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.340×** | -6.7 | 2e-09 | 27/29 (HS-578T, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.328×** | -6.4 | 1e-08 | 28/29 (C32, NCI-H2347, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.360×** | -5.8 | 7e-07 | 26/29 (A-172, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.458×** | -5.7 | 7e-07 | 27/29 (HS-578T, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.438×** | -5.6 | 1e-06 | 25/29 (C32, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.419×** | -5.4 | 4e-06 | 26/29 (HS-578T, H4, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.357×** | -5.2 | 8e-06 | 25/28 (NCI-H460, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **0.554×** | -5.2 | 9e-06 | 23/29 (RPMI-7951, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.407×** | -5.2 | 9e-06 | 22/28 (HS-578T, H4, …) | all doses, flat | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.451×** | -5.0 | 3e-05 | 23/29 (HS-578T, H4, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.572×** | -4.8 | 6e-05 | 22/29 (NCI-H2347, NCI-H460, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.443×** | -4.8 | 6e-05 | 24/29 (SW 1271, C32, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.83 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14656. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 320 | 0 | 20 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -15.0) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.0647× (z -14.9) |
| [[A-172 (line)]] | wt | 109 | 0 | 10 (4 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0510× (z -15.2) |
| [[C32 (line)]] | wt | 127 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -12.2) |
| [[H4 (line)]] | wt | 75.5 | 0 | 8 (2 ⚠) | — | [[Clobetasol propionate (drug)]] 5 µM 0.0635× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 165 | 0 | 7 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0831× (z -11.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.112× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 38.6 | 0 | 5 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0865× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 234 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0970× (z -17.5) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.195× (z -8.7) |
| [[SNU-1 (line)]] | wt | 90.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -12.6) ⚠ position correction uncertain · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.245× (z -9.7) |
| [[SW 1088 (line)]] | alt | 441 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0965× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0540× (z -10.0) |
| [[SW 1271 (line)]] | alt | 84.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0308× (z -14.8) ⚠ position correction uncertain · without an alert: [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.0390× (z -9.2) |
| [[A549 (line)]] | wt | 44.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.158× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 56.4 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.0584× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 27.3 | 0 | 2 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.408× (z -13.1) ⚠ position not correctable |
| [[J82 (line)]] | alt | 51.0 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0770× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -9.7) ⚠ position correction uncertain |
| [[NCI-H1792 (line)]] | alt | 52.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -12.1) ⚠ position correction uncertain |
| [[NCI-H2030 (line)]] | alt | 27.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -9.4) ⚠ position correction uncertain |
| [[NCI-H23 (line)]] | alt | 11.6 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0916× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 30.4 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.109× (z -8.9) |
| [[RKO (line)]] | wt | 13.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.39× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0387× (z -10.6) |
| [[A-427 (line)]] | wt | 4.30 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.99 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.47 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.43 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.75 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.08 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.34 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.06 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.12 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.94 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14656), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STC1]] | +0.79 | +0.79 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[BCL2A1]] | +0.77 | +0.70 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[ANTXR2]] | +0.72 | +0.76 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[LRRC8C]] | +0.71 | +0.69 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[RAC2]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[PLAUR]] | +0.68 | +0.67 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[CSNK1E]] | +0.68 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[MMP1]] | +0.68 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[PKIA]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[TM4SF1]] | +0.64 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[KCNN4]] | +0.64 | +0.66 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[SIPA1L3]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH3B1]] | -0.61 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[MGST1]] | -0.60 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[PDLIM1]] | -0.60 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[TMTC1]] | -0.58 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[STOM]] | -0.58 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[NNMT]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[MAP2]] | -0.55 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[ROS1]] | -0.55 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[HECTD1]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[GSR]] | -0.52 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[MYOF]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 11, C 8. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP1]] | B | MMP1 activity raises TMEM158's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 4.16× lower at baseline in the lines without MMP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[GDNF]] | B | GDNF activity raises TMEM158's level | lines that do not express GDNF (38) vs lines expressing it (12) | 5.01× lower at baseline in the lines without GDNF | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9 |
| [[ABHD17C]] | B | ABHD17C activity raises TMEM158's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 2.80× lower at baseline in the lines without ABHD17C | 0.055 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[SLC1A1]] | B | SLC1A1 activity raises TMEM158's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 2.13× lower at baseline in the lines without SLC1A1 | 0.058 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[PTGS2]] | B | PTGS2 activity raises TMEM158's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 3.24× lower at baseline in the lines without PTGS2 | 0.062 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[DPF3]] | B | DPF3 activity raises TMEM158's level | lines that do not express DPF3 (13) vs lines expressing it (37) | 2.18× lower at baseline in the lines without DPF3 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, RNF152, RORA; maybe low, not absent |
| [[LINC02454]] | B | LINC02454 activity raises TMEM158's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 3.13× lower at baseline in the lines without LINC02454 | 0.071 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[SLC46A3]] | B | SLC46A3 activity raises TMEM158's level | lines that do not express SLC46A3 (11) vs lines expressing it (39) | 3.27× lower at baseline in the lines without SLC46A3 | 0.086 | ⚠ within organs, on part of the lines; also absent: PLCE1, CLCF1 |
| [[SERPIND1]] | B | SERPIND1 activity raises TMEM158's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 2.21× lower at baseline in the lines without SERPIND1 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers TMEM158's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.7% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[ULBP2]] | B | ULBP2 activity raises TMEM158's level | lines that do not express ULBP2 (9) vs lines expressing it (41) | 3.29× lower at baseline in the lines without ULBP2 | 0.099 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[COL13A1]] | C | COL13A1 activity raises TMEM158's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 5.54× lower at baseline in the lines without COL13A1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38; co-absent with the target |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 20, C 8. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENTPD7]] | B | TMEM158 activity raises ENTPD7's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 2.20× lower at baseline in the lines without TMEM158 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[STX1A]] | B | TMEM158 activity raises STX1A's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 2.48× lower at baseline in the lines without TMEM158 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[EFL1]] | B | TMEM158 activity raises EFL1's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 1.36× lower at baseline in the lines without TMEM158 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[WWTR1]] | B | TMEM158 activity raises WWTR1's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 3.20× lower at baseline in the lines without TMEM158 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[NUMB]] | B | TMEM158 activity raises NUMB's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 1.41× lower at baseline in the lines without TMEM158 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[ARSJ]] | B | TMEM158 activity raises ARSJ's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 3.15× lower at baseline in the lines without TMEM158 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[CSNK1E]] | B | TMEM158 activity raises CSNK1E's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 1.73× lower at baseline in the lines without TMEM158 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[TIMP1]] | B | TMEM158 activity raises TIMP1's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 2.26× lower at baseline in the lines without TMEM158 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[TPBG]] | B | TMEM158 activity raises TPBG's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 2.38× lower at baseline in the lines without TMEM158 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[SMTN]] | B | TMEM158 activity raises SMTN's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 1.47× lower at baseline in the lines without TMEM158 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[UPP1]] | B | TMEM158 activity raises UPP1's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without TMEM158 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[PYGL]] | B | TMEM158 activity raises PYGL's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 2.28× lower at baseline in the lines without TMEM158 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.800). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.9, 3.7); signed map (3.3, 47.7). **Vector** length 136, 50.3% of its response variance represented; |z| ≥ 3 in 1,136 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +2.8 | +2.4 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.4 | +3.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.4 | -7.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.2 | -5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.7 | -7.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -5.4 | -6.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.3 | -4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.3 | -8.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 158 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:45,224,466-45,226,287 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RIS1, p40BBp |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WZ71](https://www.uniprot.org/uniprotkb/Q8WZ71) (Transmembrane protein 158):

> Receptor for brain injury-derived neurotrophic peptide (BINP), a synthetic 13-mer peptide.

**Summary**, from NCBI Gene [25907](https://www.ncbi.nlm.nih.gov/gene/25907):

> Constitutive activation of the Ras pathway triggers an irreversible proliferation arrest reminiscent of replicative senescence. Transcription of this gene is upregulated in response to activation of the Ras pathway, but not under other conditions that induce senescence. The encoded protein is similar to a rat cell surface receptor proposed to function in a neuronal survival pathway. An allelic polymorphism in this gene results in both functional and non-functional (frameshifted) alleles; the …

**Accessions** — [HGNC:30293](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30293) · Entrez [25907](https://www.ncbi.nlm.nih.gov/gene/25907) · UniProt [Q8WZ71](https://www.uniprot.org/uniprotkb/Q8WZ71) · Ensembl [ENSG00000249992](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249992)

## Data

Gene col 14656: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14656); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14656, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14656]; `tensor/DDL_lfc|DDL_z.npy` [14656]; `embed/gene_vectors.npy` [14656]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14656 or target_col == 14656). Every well: [[TMEM158 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM158.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
