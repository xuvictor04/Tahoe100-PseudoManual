---
symbol: "RWDD2B"
type: "gene"
col: 7962
ensembl_id: "ENSG00000156253"
name: "RWD domain containing 2B"
location: "21q21.3"
module: 68
arm: "+"
pooled_cpm: 8.43
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 10
n_dd_up_clean: 19
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# RWDD2B

*RWD domain containing 2B* — 21q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.27× (z +15.8, q 0e+00, up in 41 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.507× (z -6.4, q 9e-08, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (73 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 27 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LACTB2]] (+0.74, fdr 1e-05), [[SMIM19]] (+0.73, fdr 2e-05), [[TMEM35B]] (+0.73, fdr 7e-06); moves opposite to [[SLC27A1]] (-0.67, fdr 5e-04), [[CABLES2]] (-0.67, fdr 6e-04), [[GNAI2]] (-0.66, fdr 2e-04).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7962.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.27×** | +15.8 | 0e+00 | 41/42 (CFPAC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.75×** | +12.4 | 4e-33 | 30/31 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.55×** | +11.5 | 3e-28 | 14/14 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.34×** | +10.9 | 1e-25 | 34/36 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.05×** | +9.7 | 3e-20 | 20/22 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.72×** | +9.0 | 1e-17 | 32/41 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.65×** | +8.8 | 1e-16 | 38/41 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.91×** | +8.6 | 4e-16 | 35/46 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.13×** | +7.1 | 7e-11 | 33/45 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.08×** | +6.6 | 2e-09 | 27/44 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.64×** | +6.6 | 3e-09 | 30/47 (A498, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.62×** | +6.4 | 6e-09 | 29/43 (HEC-1-A, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +6.3 | 1e-08 | 27/41 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.71×** | +5.1 | 2e-05 | 23/45 (A-172, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.66×** | +4.8 | 7e-05 | 25/46 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.65×** | +4.7 | 8e-05 | 21/45 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.62×** | +4.5 | 2e-04 | 23/45 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.58×** | +4.1 | 0.001 | 18/45 (HS-578T, NCI-H23, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.53×** | +3.7 | 0.006 | 17/41 (SW480, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belzutifan (drug)]] 5 µM |  | **2.03×** | +3.5 | 0.015 | 12/36 (SW480, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7962.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.507×** | -6.4 | 9e-08 | 31/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.523×** | -6.1 | 3e-07 | 27/45 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.595×** | -4.9 | 2e-04 | 24/44 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.597×** | -4.9 | 2e-04 | 26/43 (A-427, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.377×** | -4.8 | 2e-04 | 25/41 (NCI-H1573, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.429×** | -4.2 | 0.003 | 19/44 (MIA PaCa-2, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.652×** | -4.0 | 0.005 | 18/44 (C-33 A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.638×** | -4.0 | 0.005 | 21/46 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.690×** | -3.3 | 0.060 | 18/43 (PANC-1, SW1417, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.713×** | -3.2 | 0.080 | 18/46 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7962. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.73 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +9.9) | [[Digitoxin (drug)]] 0.5 µM 0.172× (z -10.7) |
| [[SW480 (line)]] | alt | 14.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 2 | — | [[Ixazomib (drug)]] 0.05 µM 0.0976× (z -9.8) |
| [[SNU-423 (line)]] | alt | 7.46 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +10.0) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.123× (z -9.2) |
| [[A-427 (line)]] | wt | 9.73 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 8.19 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +9.1) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 6.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.47× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 9.13 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0660× (z -9.0) |
| [[C32 (line)]] | wt | 7.05 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0740× (z -8.5) ⚠ cell-cycle shift, explains ~22% of this change |
| [[CFPAC-1 (line)]] | alt | 9.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.88× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +11.5) | — |
| [[HOP62 (line)]] | alt | 7.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 8.55 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0780× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 6.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.81× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 12.3 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.86× (z +8.9) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 7.36 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0795× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 5.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 11.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +8.8) | — |
| [[RKO (line)]] | wt | 7.27 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.5 µM 0.0449× (z -11.9) |
| [[SK-MEL-2 (line)]] | alt | 6.50 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0634× (z -9.9) |
| [[A-172 (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7962), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 21 of them with an alert (⚠; 21 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LACTB2]] | +0.74 | +0.78 / +0.52 | both halves | 1e-05 |  |
| [[SMIM19]] | +0.73 | +0.74 / +0.47 | both halves | 2e-05 |  |
| [[TMEM35B]] | +0.73 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[PHYH]] | +0.72 | +0.75 / +0.45 | both halves | 3e-05 |  |
| [[TRAM2-AS1]] | +0.72 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[DHRS4-AS1]] | +0.71 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[WAC-AS1]] | +0.71 | +0.72 / +0.41 | both halves | 4e-05 |  |
| [[C17orf75]] | +0.70 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[FAIM]] | +0.69 | +0.59 / +0.36 | both halves | 9e-05 |  |
| [[PPCS]] | +0.68 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[SDSL]] | +0.68 | +0.77 / +0.47 | both halves | 2e-05 |  |
| [[THAP2]] | +0.68 | +0.70 / +0.29 | both halves | 2e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A1]] | -0.67 | -0.66 / -0.23 | both halves | 5e-04 |  |
| [[CABLES2]] | -0.67 | -0.60 / -0.21 | both halves | 6e-04 |  |
| [[GNAI2]] | -0.66 | -0.54 / -0.29 | both halves | 2e-04 |  |
| [[TPST2]] | -0.64 | -0.67 / -0.41 | both halves | 4e-05 |  |
| [[MAST3]] | -0.64 | -0.63 / -0.12 | ⚠ one half (not replicated) | 0.002 |  |
| [[RAB40B]] | -0.62 | -0.60 / -0.30 | both halves | 2e-04 |  |
| [[KANK2]] | -0.62 | -0.54 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[PHKA2]] | -0.62 | -0.63 / -0.32 | both halves | 1e-04 |  |
| [[PBX4]] | -0.62 | -0.61 / -0.21 | both halves | 6e-04 |  |
| [[TCF3]] | -0.62 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[PCMT1]] | -0.62 | -0.64 / -0.11 | ⚠ one half (not replicated) | 0.002 |  |
| [[SLC25A42]] | -0.61 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[GALNS]] | -0.60 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[NPHP4]] | -0.60 | -0.54 / -0.23 | both halves | 5e-04 |  |
| [[SAMD4B]] | -0.60 | -0.49 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RWDD2B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises RWDD2B's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[OGFRL1]] | B | OGFRL1 activity raises RWDD2B's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 1.17× lower at baseline in the lines without OGFRL1 | 0.085 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1 |
| [[LHFPL6]] | B | LHFPL6 activity raises RWDD2B's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.20× lower at baseline in the lines without LHFPL6 | 0.087 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.714). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (2.0, 13.4); signed map (22.0, -15.0). **Vector** length 83.1, 17.8% of its response variance represented; |z| ≥ 3 in 989 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +15.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +9.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +8.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.6 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +8.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +5.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.0 | +2.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -0.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -2.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | -0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -4.8 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +0.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | RWD domain containing 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.3 — chr21:29,004,384-29,019,360 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GL011; previously C21orf6 |
| Gene groups (HGNC) | RWD domain containing |
| Matched by | ensembl_id |

UniProt [P57060](https://www.uniprot.org/uniprotkb/P57060) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:1302](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1302) · Entrez [10069](https://www.ncbi.nlm.nih.gov/gene/10069) · UniProt [P57060](https://www.uniprot.org/uniprotkb/P57060) · Ensembl [ENSG00000156253](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156253)

## Data

Gene col 7962: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7962); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7962, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7962]; `tensor/DDL_lfc|DDL_z.npy` [7962]; `embed/gene_vectors.npy` [7962]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7962 or target_col == 7962). Every well: [[RWDD2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RWDD2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
