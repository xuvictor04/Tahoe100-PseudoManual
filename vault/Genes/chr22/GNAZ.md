---
symbol: "GNAZ"
type: "gene"
col: 4867
ensembl_id: "ENSG00000128266"
name: "G protein subunit alpha z"
location: "22q11.22-q11.23"
module: 132
arm: "+"
pooled_cpm: 3.55
n_lines_expressing: 40
n_dd_up: 11
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 15
direction_downstream: 68
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# GNAZ

*G protein subunit alpha z* — 22q11.22-q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.09× (z +7.3, q 2e-10, up in 20 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.341× (z -15.0, q 0e+00, down in 25 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHANK3]] (+0.77, fdr 7e-06), [[SEMA4F]] (+0.73, fdr 7e-06), [[BRSK2]] (+0.72, fdr 7e-06); moves opposite to [[THAP2]] (-0.62, fdr 3e-05), [[ASH1L]] (-0.61, fdr 3e-05), [[GGPS1]] (-0.61, fdr 2e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[LAMC3]] → it (grade B ⚠); 68 go from it, the strongest it → [[USP31]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4867.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.09×** | +7.3 | 2e-10 | 20/34 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +6.1 | 2e-07 | 15/34 (SW1417, PANC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +5.4 | 1e-05 | 8/16 (SW1417, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +5.3 | 2e-05 | 16/37 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +5.1 | 3e-05 | 12/37 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +5.1 | 4e-05 | 3/4 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +4.8 | 2e-04 | 8/29 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +4.7 | 2e-04 | 14/37 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +4.3 | 1e-03 | 7/32 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.94×** | +3.4 | 0.036 | 4/34 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.041 | 6/29 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.38× | +3.1 | 0.11 | 8/29 (A-172, HOP62, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4867.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.341×** | -15.0 | 0e+00 | 25/30 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.347×** | -10.0 | 3e-21 | 23/33 (A-427, HS-578T, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.524×** | -9.0 | 4e-17 | 22/28 (HS-578T, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.413×** | -8.7 | 4e-16 | 18/26 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.465×** | -7.5 | 5e-12 | 22/37 (HS-578T, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.490×** | -7.0 | 2e-10 | 22/25 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.493×** | -7.0 | 3e-10 | 20/36 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.563×** | -5.7 | 1e-06 | 17/35 (A-427, A549, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.595×** | -5.1 | 2e-05 | 19/31 (HS-578T, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.447×** | -4.1 | 0.002 | 10/32 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.678×** | -3.8 | 0.007 | 10/36 (SNU-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.697×** | -3.6 | 0.018 | 14/33 (SW480, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4867. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 6.61 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -11.5) |
| [[A-172 (line)]] | wt | 5.14 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0992× (z -13.0) |
| [[C32 (line)]] | wt | 5.57 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0302× (z -16.3) |
| [[NCI-H2030 (line)]] | alt | 5.50 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -9.1) |
| [[A-427 (line)]] | wt | 8.86 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0895× (z -11.1) |
| [[A498 (line)]] | wt | 2.18 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 19.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -8.6) |
| [[HOP62 (line)]] | alt | 1.82 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 6.69 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 2.19 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0742× (z -9.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[PANC-1 (line)]] | alt | 2.97 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -10.1) |
| [[SW48 (line)]] | wt | 8.19 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0487× (z -12.5) |
| [[SW480 (line)]] | alt | 3.17 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.121× (z -8.8) |
| [[A549 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.324 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.710 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.881 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.725 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.850 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4867), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHANK3]] | +0.77 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[SEMA4F]] | +0.73 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[BRSK2]] | +0.72 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[RIMS3]] | +0.70 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[AIF1L]] | +0.69 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[SDC3]] | +0.69 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[SEPTIN5]] | +0.69 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[NBEAL2]] | +0.68 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[GPRIN1]] | +0.68 | +0.54 / +0.60 | both halves | 1e-05 | STRING 776 |
| [[WASF3]] | +0.67 | +0.55 / +0.57 | both halves | 1e-05 | pathway: Leishmania infection |
| [[METAP1]] | +0.67 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[TMOD2]] | +0.66 | +0.60 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP2]] | -0.62 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[ASH1L]] | -0.61 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[GGPS1]] | -0.61 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[LINC01004]] | -0.60 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[LINC02307]] | -0.59 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[METTL6]] | -0.59 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[TRIP11]] | -0.59 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[HELQ]] | -0.59 | -0.53 / -0.37 | both halves | 7e-05 |  |
| [[TBCE-1]] | -0.58 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[CCDC90B-AS1]] | -0.58 | -0.49 / -0.27 | both halves | 3e-04 |  |
| [[PDCD7]] | -0.58 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[GTF2IRD2]] | -0.58 | -0.50 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 14, C 1. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMC3]] | B | LAMC3 activity raises GNAZ's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.85× lower at baseline in the lines without LAMC3 | 0.010 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[SLC4A3]] | B | SLC4A3 activity raises GNAZ's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 2.00× lower at baseline in the lines without SLC4A3 | 0.012 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[BRSK2]] | B | BRSK2 activity raises GNAZ's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.80× lower at baseline in the lines without BRSK2 | 0.026 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[FSD1]] | B | FSD1 activity raises GNAZ's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 1.93× lower at baseline in the lines without FSD1 | 0.031 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[NT5M]] | B | NT5M activity raises GNAZ's level | lines that do not express NT5M (7) vs lines expressing it (43) | 2.49× lower at baseline in the lines without NT5M | 0.034 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[MCOLN2]] | B | MCOLN2 activity raises GNAZ's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.57× lower at baseline in the lines without MCOLN2 | 0.038 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[PDZD4]] | B | PDZD4 activity raises GNAZ's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 1.65× lower at baseline in the lines without PDZD4 | 0.042 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[JAM3]] | B | JAM3 activity raises GNAZ's level | lines that do not express JAM3 (23) vs lines expressing it (27) | 1.64× lower at baseline in the lines without JAM3 | 0.050 | ⚠ within organs, on part of the lines; also absent: NPTX1, NOVA2, GDNF-AS1 |
| [[SEPTIN5]] | B | SEPTIN5 activity raises GNAZ's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.62× lower at baseline in the lines without SEPTIN5 | 0.058 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[THRB]] | B | THRB activity lowers GNAZ's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.86× higher at baseline in the lines without THRB | 0.058 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[CBX2]] | B | CBX2 activity raises GNAZ's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 2.89× lower at baseline in the lines without CBX2 | 0.065 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers GNAZ's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*68 arrows, 68 of them with an alert ⚠; grade A 0, B 66, C 2. Shown: the 12 strongest; 56 more arrows (56 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[USP31]] | B | GNAZ activity raises USP31's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.45× lower at baseline in the lines without GNAZ | 0.001 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[NT5M]] | B | GNAZ activity raises NT5M's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.48× lower at baseline in the lines without GNAZ | 0.002 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[BRSK2]] | B | GNAZ activity raises BRSK2's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.21× lower at baseline in the lines without GNAZ | 0.002 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[FAM78B]] | B | GNAZ activity raises FAM78B's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 3.52× lower at baseline in the lines without GNAZ | 0.004 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[STX2]] | B | GNAZ activity raises STX2's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.16× lower at baseline in the lines without GNAZ | 0.004 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[TTC7B]] | B | GNAZ activity raises TTC7B's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.88× lower at baseline in the lines without GNAZ | 0.004 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[ABCA3]] | B | GNAZ activity raises ABCA3's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.55× lower at baseline in the lines without GNAZ | 0.005 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[GARNL3]] | B | GNAZ activity raises GARNL3's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.71× lower at baseline in the lines without GNAZ | 0.007 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[INPP4A]] | B | GNAZ activity raises INPP4A's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.75× lower at baseline in the lines without GNAZ | 0.008 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[MAPK12]] | B | GNAZ activity raises MAPK12's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.72× lower at baseline in the lines without GNAZ | 0.009 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[MCOLN2]] | B | GNAZ activity raises MCOLN2's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.63× lower at baseline in the lines without GNAZ | 0.009 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[CHST10]] | B | GNAZ activity raises CHST10's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.84× lower at baseline in the lines without GNAZ | 0.010 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.857). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.4, 40.9); signed map (-39.8, -7.6). **Vector** length 56.9, 9.14% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.2 | +5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +7.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.8 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +6.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.3 | +5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.4 | +0.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.3 | +1.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.0 | -10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -15.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -9.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -3.6 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit alpha z |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.22-q11.23 — chr22:23,070,519-23,125,032 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | G protein subunits alpha, group i |
| Reactome | 11 pathways, smallest: ADORA2B mediated anti-inflammatory cytokines production; GPER1 signaling; G alpha (z) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P19086](https://www.uniprot.org/uniprotkb/P19086) (Guanine nucleotide-binding protein G(z) subunit alpha):

> Guanine nucleotide-binding proteins (G proteins) are involved as modulators or transducers in various transmembrane signaling systems.

**Summary**, from NCBI Gene [2781](https://www.ncbi.nlm.nih.gov/gene/2781):

> The protein encoded by this gene is a member of a G protein subfamily that mediates signal transduction in pertussis toxin-insensitive systms. This encoded protein may play a role in maintaining the ionic balance of perilymphatic and endolymphatic cochlear fluids. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4395](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4395) · Entrez [2781](https://www.ncbi.nlm.nih.gov/gene/2781) · UniProt [P19086](https://www.uniprot.org/uniprotkb/P19086) · Ensembl [ENSG00000128266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128266)

## Data

Gene col 4867: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4867); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4867, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4867]; `tensor/DDL_lfc|DDL_z.npy` [4867]; `embed/gene_vectors.npy` [4867]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4867 or target_col == 4867). Every well: [[GNAZ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNAZ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
