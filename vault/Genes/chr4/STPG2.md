---
symbol: "STPG2"
type: "gene"
col: 8635
ensembl_id: "ENSG00000163116"
name: "sperm tail PG-rich repeat containing 2"
location: "4q22.3-q23"
module: 10
arm: "+"
pooled_cpm: 14.44
n_lines_expressing: 45
n_dd_up: 34
n_dd_down: 15
n_dd_up_clean: 30
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# STPG2

*sperm tail PG-rich repeat containing 2* — 4q22.3-q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.95× (z +13.5, q 1e-38, up in 26 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.502× (z -6.1, q 6e-07, down in 24 of 41 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.548× (z -5.3, q 2e-05, down in 22 of 41 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM232]] (+0.76, fdr 7e-06), [[CHODL]] (+0.74, fdr 1e-05), [[MAMDC2-AS1]] (+0.73, fdr 1e-05); moves opposite to [[NBPF3]] (-0.60, fdr 9e-05), [[ANKS6]] (-0.58, fdr 5e-05), [[FAM118A]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GRIP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8635.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.95×** | +13.5 | 1e-38 | 26/37 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.86×** | +7.7 | 4e-12 | 24/42 (HEC-1-A, A498, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.08×** | +6.5 | 2e-08 | 25/41 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +5.9 | 4e-07 | 16/38 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +5.9 | 6e-07 | 14/28 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +5.5 | 3e-06 | 19/36 (HEC-1-A, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.90×** | +5.4 | 5e-06 | 26/39 (HOP62, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +5.3 | 6e-06 | 16/39 (C32, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +5.2 | 1e-05 | 4/15 (HT-29, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +5.0 | 3e-05 | 8/21 (SW1417, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.73×** | +4.8 | 7e-05 | 22/41 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.50×** | +4.8 | 7e-05 | 17/43 (LoVo, SK-MEL-2, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.68×** | +4.6 | 2e-04 | 15/41 (SK-MEL-2, NCI-H2030, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.51×** | +4.2 | 9e-04 | 16/41 (LoVo, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.40×** | +4.2 | 9e-04 | 17/43 (A-427, LS 180, …) | top dose only | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM |  | **1.66×** | +4.1 | 0.002 | 16/43 (SK-MEL-2, LoVo, …) | all doses, flat | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.58×** | +3.9 | 0.004 | 18/39 (CFPAC-1, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.38×** | +3.8 | 0.004 | 20/41 (SK-MEL-2, A498, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **2.24×** | +3.7 | 0.006 | 14/41 (SK-MEL-2, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8635.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.502×** | -6.1 | 6e-07 | 24/41 (COLO 205, NCI-H23, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.531×** | -5.6 | 7e-06 | 22/42 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.548×** | -5.3 | 2e-05 | 22/41 (Panc 03.27, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.605×** | -4.4 | 0.001 | 17/42 (NCI-H23, NCI-H1792, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.594×** | -4.3 | 0.002 | 21/39 (Panc 03.27, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.625×** | -4.2 | 0.003 | 16/42 (Panc 03.27, SHP-77, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.641×** | -3.9 | 0.007 | 19/40 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.734×** | -3.9 | 0.008 | 12/41 (C32, HT-29, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.546×** | -3.8 | 0.008 | 15/43 (NCI-H23, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.672×** | -3.5 | 0.025 | 17/42 (NCI-H1573, COLO 205, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.684×** | -3.4 | 0.040 | 14/42 (SK-MEL-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.676×** | -3.3 | 0.043 | 17/42 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.683×** | -3.2 | 0.054 | 14/41 (A-427, NCI-H23, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.704×** | -3.1 | 0.075 | 15/40 (NCI-H23, Panc 03.27, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.518×** | -3.0 | 0.090 | 7/39 (NCI-H23, LOX-IMVI, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8635. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 82.0 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0831× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -10.6) |
| [[A-427 (line)]] | wt | 14.1 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0378× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.165× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 19.2 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0858× (z -11.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.154× (z -8.8) |
| [[COLO 205 (line)]] | alt | 26.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0691× (z -11.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.161× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 32.7 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.135× (z -9.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A498 (line)]] | wt | 42.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -12.3) |
| [[C32 (line)]] | wt | 5.66 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.10× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 5.17 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.10× (z +12.8) | — |
| [[NCI-H1573 (line)]] | alt | 55.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0919× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 3.92 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +8.5) | [[Pimozide (drug)]] 0.5 µM 0.0639× (z -11.8) ⚠ transcription drop |
| [[NCI-H460 (line)]] | wt | 4.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +8.7) | — |
| [[RKO (line)]] | wt | 5.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.50× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 89.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -10.9) |
| [[A-172 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.54 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8635), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM232]] | +0.76 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[CHODL]] | +0.74 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[MAMDC2-AS1]] | +0.73 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[PKN2-AS1]] | +0.73 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[TAFA2]] | +0.73 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[FBXO38-DT]] | +0.73 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[CFAP418-AS1]] | +0.73 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[GAS2]] | +0.72 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[IQCH-AS1]] | +0.71 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[EIF1B-AS1]] | +0.71 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | +0.71 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[UNC79]] | +0.70 | +0.72 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF3]] | -0.60 | -0.56 / -0.36 | both halves | 9e-05 |  |
| [[ANKS6]] | -0.58 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[FAM118A]] | -0.58 | -0.50 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIP1]] | B | GRIP1 activity raises STPG2's level | lines that do not express GRIP1 (13) vs lines expressing it (37) | 2.49× lower at baseline in the lines without GRIP1 | 0.011 | ⚠ within organs, on part of the lines; also absent: PAX9; maybe low, not absent |
| [[LINC00886]] | B | LINC00886 activity raises STPG2's level | lines that do not express LINC00886 (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without LINC00886 | 0.033 | ⚠ within organs, on part of the lines; also absent: RASEF; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers STPG2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ST8SIA6-AS1]] | B | ST8SIA6-AS1 activity raises STPG2's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 1.95× lower at baseline in the lines without ST8SIA6-AS1 | 0.087 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267 |
| [[LINC01905]] | B | LINC01905 activity raises STPG2's level | lines that do not express LINC01905 (35) vs lines expressing it (15) | 1.85× lower at baseline in the lines without LINC01905 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000267327, ENSG00000267284, SLC25A24P1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.751). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (8.5, 16.3); signed map (29.3, -10.0). **Vector** length 88.8, 19.7% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.1 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.3 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.0 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.8 | +5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +3.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.7 | -3.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -3.5 | -4.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | -2.9 | -2.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.1 | -3.8 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -0.5 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | sperm tail PG-rich repeat containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.3-q23 — chr4:97,184,093-98,143,476 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC46496; previously C4orf37 |
| Matched by | ensembl_id |

UniProt [Q8N412](https://www.uniprot.org/uniprotkb/Q8N412) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28712](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28712) · Entrez [285555](https://www.ncbi.nlm.nih.gov/gene/285555) · UniProt [Q8N412](https://www.uniprot.org/uniprotkb/Q8N412) · Ensembl [ENSG00000163116](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163116)

## Data

Gene col 8635: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8635); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8635, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8635]; `tensor/DDL_lfc|DDL_z.npy` [8635]; `embed/gene_vectors.npy` [8635]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8635 or target_col == 8635). Every well: [[STPG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STPG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
