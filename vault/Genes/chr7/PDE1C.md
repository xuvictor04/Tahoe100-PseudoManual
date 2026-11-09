---
symbol: "PDE1C"
type: "gene"
col: 7827
ensembl_id: "ENSG00000154678"
name: "phosphodiesterase 1C"
location: "7p14.3"
module: 19
arm: "+"
pooled_cpm: 28.65
n_lines_expressing: 24
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 15
direction_downstream: 3
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# PDE1C

*phosphodiesterase 1C* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.16× (z +23.9, q 0e+00, up in 7 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.652× (z -6.3, q 2e-07, down in 13 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIMS1]] (+0.69, fdr 7e-06), [[KCNK2]] (+0.69, fdr 7e-06), [[LINC02742]] (+0.68, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[GYG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7827.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.16×** | +23.9 | 0e+00 | 7/20 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.24×** | +16.7 | 0e+00 | 13/22 (NCI-H1573, LS 180, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +15.1 | 0e+00 | 6/13 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.77×** | +15.0 | 0e+00 | 11/17 (Panc 03.27, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.63×** | +13.1 | 3e-37 | 7/16 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.25×** | +11.9 | 1e-30 | 10/21 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +9.7 | 2e-20 | 6/22 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +9.0 | 1e-17 | 10/21 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.77×** | +8.4 | 3e-15 | 5/22 (SK-MEL-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +7.5 | 3e-12 | 3/21 (SK-MEL-2, SW480, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.1 | 2e-05 | 6/22 (SW1417, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +4.6 | 2e-04 | 9/22 (NCI-H1573, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.3 | 6e-04 | 4/12 (SNU-423, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.005 | 9/22 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.012 | 1/20 (SW480) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.024 | 3/22 (SNU-423, RPMI-7951, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.027 | 3/22 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Afatinib (drug)]] 0.05 µM |  | 1.16× | +2.9 | 0.098 | 1/21 (SK-MEL-2) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7827.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.652×** | -6.3 | 2e-07 | 13/21 (NCI-H460, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.744×** | -4.4 | 0.004 | 7/22 (SW 1088, A-172, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.754×** | -3.8 | 0.019 | 1/22 (NCI-H460) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.772×** | -3.8 | 0.019 | 9/22 (MIA PaCa-2, H4, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.792×** | -3.4 | 0.067 | 8/21 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.784×** | -3.3 | 0.074 | 2/22 (SW 1271, NCI-H1573) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 0.5 µM |  | **0.799×** | -3.3 | 0.074 | 5/19 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.787×** | -3.3 | 0.079 | 2/22 (H4, SW 1271) | inconsistent across doses | position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | 0.810× | -3.1 | 0.12 | 5/22 (A549, J82, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.815× | -3.0 | 0.14 | 4/20 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7827. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 231 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -14.8) |
| [[J82 (line)]] | alt | 108 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -13.4) |
| [[SHP-77 (line)]] | alt | 82.8 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.165× (z -12.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 7.51 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +16.7) | [[Roxadustat (drug)]] 0.05 µM 0.0858× (z -10.1) |
| [[SW480 (line)]] | alt | 9.62 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.10× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 9.42 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.78× (z +10.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.146× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 10.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 8.55 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.19× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.74× (z +8.7) ⚠ position not correctable | — |
| [[SK-MEL-2 (line)]] | alt | 8.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +8.5) | — |
| [[A-172 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.05 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.64 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 64.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.06 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.29 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.33 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.28 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.95 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.33 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.58 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.84 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.51 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.42 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.30 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7827), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIMS1]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[KCNK2]] | +0.69 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[LINC02742]] | +0.68 | +0.53 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[ESM1]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[LINC01035]] | +0.65 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[RAB3C]] | +0.64 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[COL4A6]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[DPP10]] | +0.62 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[LSAMP]] | +0.62 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CNTN1]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[PAX7]] | +0.61 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[PDCD1LG2]] | +0.61 | +0.49 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 4, C 11. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PDE1C's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PTN]] | B | PTN activity raises PDE1C's level | lines that do not express PTN (28) vs lines expressing it (22) | 2.14× lower at baseline in the lines without PTN | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC |
| [[ALPK2]] | B | ALPK2 activity raises PDE1C's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 3.00× lower at baseline in the lines without ALPK2 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4 |
| [[PALMD]] | B | PALMD activity raises PDE1C's level | lines that do not express PALMD (27) vs lines expressing it (23) | 2.06× lower at baseline in the lines without PALMD | 0.099 | ⚠ within organs, on part of the lines; also absent: GPRC5B, FAM110B, SHISAL1; maybe low, not absent |
| [[LINC02994]] | C | LINC02994 activity raises PDE1C's level | lines that do not express LINC02994 (33) vs lines expressing it (17) | 3.49× lower at baseline in the lines without LINC02994 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000234352, ANKRD30B, ENSG00000287598; co-absent with the target |
| [[FRMPD4]] | C | FRMPD4 activity raises PDE1C's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 3.11× lower at baseline in the lines without FRMPD4 | 0.041 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3; co-absent with the target |
| [[UNC5D]] | C | UNC5D activity raises PDE1C's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 3.37× lower at baseline in the lines without UNC5D | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11; co-absent with the target |
| [[TCF4]] | C | TCF4 activity raises PDE1C's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 3.10× lower at baseline in the lines without TCF4 | 0.046 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[GLP2R]] | C | GLP2R activity raises PDE1C's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 5.14× lower at baseline in the lines without GLP2R | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054; co-absent with the target |
| [[PDE1A]] | C | PDE1A activity raises PDE1C's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 3.72× lower at baseline in the lines without PDE1A | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |
| [[SCARA5]] | C | SCARA5 activity raises PDE1C's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 3.12× lower at baseline in the lines without SCARA5 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[TBXT]] | C | TBXT activity raises PDE1C's level | lines that do not express TBXT (47) vs lines expressing it (3) | 6.95× lower at baseline in the lines without TBXT | 0.069 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GYG2]] | B | PDE1C activity raises GYG2's level | lines that do not express PDE1C (26) vs lines expressing it (24) | 1.73× lower at baseline in the lines without PDE1C | 0.069 | ⚠ within organs, on part of the lines; also absent: NTRK3, LINC02211, LINC02945 |
| [[RNF182]] | B | PDE1C activity strengthens RNF182's drug response | lines that do not express PDE1C (12) vs lines expressing it (12) | the lines without PDE1C respond 0.81× as strongly (z diff +0.20); strongest at Harringtonine 0.5 µM: 0.97x vs 0.53x (z diff +2.4) | 0.086 | ⚠ within organs, on part of the lines; also absent: NTRK3, LINC02211, LINC02945; target measured in part of the lines; both ways; artifact flags |
| [[CCDC9B]] | B | PDE1C activity raises CCDC9B's level | lines that do not express PDE1C (26) vs lines expressing it (24) | 1.66× lower at baseline in the lines without PDE1C | 0.098 | ⚠ within organs, on part of the lines; also absent: NTRK3, LINC02211, LINC02945 |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.6, 34.9); signed map (42.1, 46.1). **Vector** length 64.5, 16.6% of its response variance represented; |z| ≥ 3 in 657 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.51 to 18).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.6 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.4 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.1 | +13.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +23.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +16.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +11.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +5.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.9 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -3.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -6.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -3.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 1C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:31,751,179-32,428,131 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Hcam3 |
| Gene groups (HGNC) | Phosphodiesterases |
| Reactome | 12 pathways, smallest: Cam-PDE 1 activation; CaM pathway; Calmodulin induced events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14123](https://www.uniprot.org/uniprotkb/Q14123) (Dual specificity calcium/calmodulin-dependent 3',5'-cyclic nucleotide phosphodiesterase 1C):

> Calmodulin-dependent cyclic nucleotide phosphodiesterase with a dual specificity for the second messengers cAMP and cGMP, which are key regulators of many important physiological processes. Has a high affinity for both cAMP and cGMP. Modulates the amplitude and duration of the cAMP signal in sensory cilia in response to odorant stimulation, hence contributing to the generation of action potentials. Regulates smooth muscle cell proliferation. Regulates the stability of growth factor receptors, …

**Summary**, from NCBI Gene [5137](https://www.ncbi.nlm.nih.gov/gene/5137):

> This gene encodes an enzyme that belongs to the 3'5'-cyclic nucleotide phosphodiesterase family. Members of this family catalyze hydrolysis of the cyclic nucleotides, cyclic adenosine monophosphate and cyclic guanosine monophosphate, to the corresponding nucleoside 5'-monophosphates. The enzyme encoded by this gene regulates proliferation and migration of vascular smooth muscle cells, and neointimal hyperplasia. This enzyme also plays a role in pathological vascular remodeling by regulating the …

**Accessions** — [HGNC:8776](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8776) · Entrez [5137](https://www.ncbi.nlm.nih.gov/gene/5137) · UniProt [Q14123](https://www.uniprot.org/uniprotkb/Q14123) · Ensembl [ENSG00000154678](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154678)

## Data

Gene col 7827: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7827); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7827, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7827]; `tensor/DDL_lfc|DDL_z.npy` [7827]; `embed/gene_vectors.npy` [7827]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7827 or target_col == 7827). Every well: [[PDE1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
