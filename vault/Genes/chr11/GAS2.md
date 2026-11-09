---
symbol: "GAS2"
type: "gene"
col: 7328
ensembl_id: "ENSG00000148935"
name: "growth arrest specific 2"
location: "11p14.3"
module: 10
arm: "+"
pooled_cpm: 3.76
n_lines_expressing: 49
n_dd_up: 32
n_dd_down: 14
n_dd_up_clean: 26
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# GAS2

*growth arrest specific 2* — 11p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.25× (z +14.9, q 0e+00, up in 24 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.425× (z -7.7, q 1e-11, down in 23 of 46 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.545× (z -5.4, q 1e-05, down in 21 of 42 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHI1-DT]] (+0.79, fdr 7e-06), [[ZRANB2-DT]] (+0.73, fdr 1e-05), [[STPG2]] (+0.72, fdr 1e-05); moves opposite to [[EPN2]] (-0.65, fdr 3e-04), [[TMEM184B]] (-0.62, fdr 1e-04), [[ATG16L2]] (-0.61, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7328.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.25×** | +14.9 | 0e+00 | 24/29 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.97×** | +8.5 | 4e-15 | 16/45 (COLO 205, A498, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +8.5 | 4e-15 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **2.38×** | +7.7 | 1e-12 | 24/45 (COLO 205, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.40×** | +7.2 | 6e-11 | 2/7 (HOP62, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +6.9 | 5e-10 | 8/18 (HepG2/C3A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +6.5 | 9e-09 | 13/26 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.8 | 6e-07 | 14/46 (A498, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.80×** | +5.2 | 1e-05 | 15/46 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.51×** | +5.0 | 3e-05 | 9/44 (SW480, C32, …) | all doses, flat |  |
| [[Afatinib (drug)]] 5 µM |  | **1.84×** | +4.8 | 9e-05 | 11/44 (CFPAC-1, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.64×** | +4.8 | 9e-05 | 13/43 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +4.7 | 1e-04 | 8/32 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.60×** | +4.5 | 3e-04 | 11/46 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.64×** | +4.4 | 4e-04 | 8/46 (LOX-IMVI, A498, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.68×** | +3.9 | 0.003 | 11/39 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.61×** | +3.8 | 0.005 | 6/39 (SW480, NCI-H1573, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.60×** | +3.7 | 0.006 | 10/31 (SW480, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.35×** | +3.7 | 0.007 | 8/44 (SW480, C32, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7328.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.425×** | -7.7 | 1e-11 | 23/46 (SHP-77, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.473×** | -5.7 | 3e-06 | 22/45 (BT-474, KATO III, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.545×** | -5.4 | 1e-05 | 21/42 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.585×** | -4.8 | 2e-04 | 17/45 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.718×** | -4.2 | 0.003 | 16/32 (NCI-H1573, COLO 205, …) | top dose only | composition shift |
| [[Artesunate (drug)]] 5 µM |  | **0.735×** | -3.9 | 0.008 | 12/46 (A549, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.603×** | -3.9 | 0.008 | 11/29 (NCI-H1573, BT-474, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.654×** | -3.6 | 0.022 | 13/37 (SHP-77, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.646×** | -3.5 | 0.027 | 11/41 (COLO 205, NCI-H1573, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.634×** | -3.5 | 0.027 | 16/39 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.493×** | -3.3 | 0.047 | 15/38 (SK-MEL-2, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.694×** | -3.3 | 0.049 | 10/45 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.657×** | -3.2 | 0.055 | 13/42 (SHP-77, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.672×** | -3.1 | 0.091 | 11/43 (SK-MEL-2, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7328. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.27 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.0534× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change · without an alert: [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0459× (z -11.3) |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0705× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[COLO 205 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0874× (z -8.6) |
| [[J82 (line)]] | alt | 3.13 | 0 | 1 | — | [[Vandetanib (drug)]] 0.05 µM 0.0692× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 8.66 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0689× (z -17.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7328), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHI1-DT]] | +0.79 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[ZRANB2-DT]] | +0.73 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[STPG2]] | +0.72 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[CFAP418-AS1]] | +0.72 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[UFL1-AS1]] | +0.71 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[SATB1-AS1]] | +0.71 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[HOTAIR]] | +0.71 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[MAMDC2-AS1]] | +0.70 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[CDNF]] | +0.70 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[IDNK]] | +0.70 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[TAFA2]] | +0.69 | +0.64 / +0.35 | both halves | 1e-04 |  |
| [[LRIG2-DT]] | +0.69 | +0.63 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPN2]] | -0.65 | -0.58 / -0.27 | both halves | 3e-04 |  |
| [[TMEM184B]] | -0.62 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[ATG16L2]] | -0.61 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[GNAI2]] | -0.61 | -0.48 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[CIB1]] | -0.61 | -0.61 / -0.24 | both halves | 4e-04 |  |
| [[ZFYVE28]] | -0.60 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[EHD4]] | -0.59 | -0.52 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GAS2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SUCLG2-DT]] | B | SUCLG2-DT activity lowers GAS2's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 1.60× higher at baseline in the lines without SUCLG2-DT | 0.056 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[C11orf52]] | B | C11orf52 activity raises GAS2's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 1.48× lower at baseline in the lines without C11orf52 | 0.059 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[CRPPA]] | B | CRPPA activity lowers GAS2's level | lines that do not express CRPPA (5) vs lines expressing it (45) | 2.34× higher at baseline in the lines without CRPPA | 0.089 | ⚠ within organs, on part of the lines; also absent: TBL1X, NLGN2; maybe low, not absent; its own permutation p |
| [[C10orf95-AS1]] | C | C10orf95-AS1 activity raises GAS2's level | lines that do not express C10orf95-AS1 (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without C10orf95-AS1 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CHD7, NRTN, ENSG00000256673; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.734). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.9, 17.3); signed map (29.6, -9.7). **Vector** length 60.4, 9.60% of its response variance represented; |z| ≥ 3 in 1,032 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +6.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.2 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +7.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +4.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.0 | -4.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.5 | -3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.5 | -5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -2.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -0.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -2.9 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.4 | -1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -2.7 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | growth arrest specific 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p14.3 — chr11:22,625,509-22,813,001 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 5 pathways, smallest: Caspase-mediated cleavage of cytoskeletal proteins; Apoptotic cleavage of cellular proteins; Apoptotic execution phase |
| Matched by | ensembl_id |

**Function**, from UniProt [O43903](https://www.uniprot.org/uniprotkb/O43903) (Growth arrest-specific protein 2):

> Required to maintain microtubule bundles in inner ear supporting cells, affording them with mechanical stiffness to transmit sound energy through the cochlea.

**Summary**, from NCBI Gene [2620](https://www.ncbi.nlm.nih.gov/gene/2620):

> The protein encoded by this gene is a caspase-3 substrate that plays a role in regulating microfilament and cell shape changes during apoptosis. It can also modulate cell susceptibility to p53-dependent apoptosis by inhibiting calpain activity. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:4167](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4167) · Entrez [2620](https://www.ncbi.nlm.nih.gov/gene/2620) · UniProt [O43903](https://www.uniprot.org/uniprotkb/O43903) · Ensembl [ENSG00000148935](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148935)

## Data

Gene col 7328: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7328); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7328, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7328]; `tensor/DDL_lfc|DDL_z.npy` [7328]; `embed/gene_vectors.npy` [7328]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7328 or target_col == 7328). Every well: [[GAS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
