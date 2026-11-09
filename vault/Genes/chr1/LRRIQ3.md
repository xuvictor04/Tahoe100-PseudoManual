---
symbol: "LRRIQ3"
type: "gene"
col: 8546
ensembl_id: "ENSG00000162620"
name: "leucine rich repeats and IQ motif containing 3"
location: "1p31.1"
module: 10
arm: "+"
pooled_cpm: 2.54
n_lines_expressing: 46
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 9
direction_downstream: 21
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# LRRIQ3

*leucine rich repeats and IQ motif containing 3* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.97× (z +12.0, q 3e-30, up in 22 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.344× (z -8.3, q 8e-14, down in 30 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRB1]] (+0.73, fdr 7e-06), [[APPBP2-DT]] (+0.71, fdr 7e-06), [[DPH6-DT]] (+0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 21 go from it, the strongest it → [[RAPGEF4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8546.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.97×** | +12.0 | 3e-30 | 22/27 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.47×** | +9.7 | 1e-19 | 7/12 (SW480, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.93×** | +8.0 | 2e-13 | 1/3 (HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.85×** | +7.5 | 7e-12 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.96×** | +7.4 | 1e-11 | 16/37 (CFPAC-1, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.51×** | +6.9 | 5e-10 | 11/20 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +5.1 | 3e-05 | 10/29 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +4.6 | 3e-04 | 10/38 (A498, SHP-77, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +4.4 | 6e-04 | 10/34 (NCI-H2030, C32, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.69×** | +4.1 | 0.002 | 12/39 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +3.9 | 0.004 | 6/30 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +3.8 | 0.006 | 7/39 (A498, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.62×** | +3.7 | 0.008 | 6/36 (NCI-H2030, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.58×** | +3.6 | 0.015 | 5/34 (CFPAC-1, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.017 | 3/39 (NCI-H2030, C-33 A, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.093 | 3/37 (NCI-H2030, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8546.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.344×** | -8.3 | 8e-14 | 30/38 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.513×** | -5.2 | 7e-05 | 17/40 (A-172, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.531×** | -4.9 | 2e-04 | 19/38 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.537×** | -4.8 | 2e-04 | 17/40 (RKO, SW 900, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.601×** | -3.9 | 0.010 | 14/36 (J82, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.617×** | -3.7 | 0.018 | 16/33 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.647×** | -3.4 | 0.063 | 14/33 (CFPAC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.660×** | -3.2 | 0.096 | 14/40 (PANC-1, SHP-77, …) | inconsistent across doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | 0.673× | -3.1 | 0.14 | 10/37 (PANC-1, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8546. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 4.35 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0459× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 4.70 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0550× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 3.52 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0686× (z -9.2) |
| [[A-172 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.888 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.810 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.762 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.949 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.589 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.752 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.868 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8546), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRB1]] | +0.73 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[APPBP2-DT]] | +0.71 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[DPH6-DT]] | +0.71 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[EIF1B-AS1]] | +0.70 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[AHI1-DT]] | +0.70 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[LRIG2-DT]] | +0.70 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[MAMDC2-AS1]] | +0.69 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[KLHDC1]] | +0.69 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[USP38-DT]] | +0.69 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[FAM227B]] | +0.69 | +0.75 / +0.55 | both halves | 1e-05 | STRING 734 |
| [[ZBED5-AS1]] | +0.67 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[GAS2]] | +0.67 | +0.68 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LRRIQ3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.1% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[FBXO15]] | B | FBXO15 activity raises LRRIQ3's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 1.72× lower at baseline in the lines without FBXO15 | 0.009 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[ANKRD20A21P]] | B | ANKRD20A21P activity raises LRRIQ3's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.52× lower at baseline in the lines without ANKRD20A21P | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[CRB1]] | B | CRB1 activity raises LRRIQ3's level | lines that do not express CRB1 (6) vs lines expressing it (44) | 1.56× lower at baseline in the lines without CRB1 | 0.036 | ⚠ within organs, on part of the lines; also absent: DNAI1, RBFOX1, RHBDL3; maybe low, not absent |
| [[SYT9-AS1]] | B | SYT9-AS1 activity raises LRRIQ3's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 1.33× lower at baseline in the lines without SYT9-AS1 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LRRC63]] | B | LRRC63 activity raises LRRIQ3's level | lines that do not express LRRC63 (25) vs lines expressing it (25) | 1.70× lower at baseline in the lines without LRRC63 | 0.060 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, STAC, CRLF2 |
| [[HOXD8]] | B | HOXD8 activity raises LRRIQ3's level | lines that do not express HOXD8 (20) vs lines expressing it (30) | 1.59× lower at baseline in the lines without HOXD8 | 0.070 | ⚠ within organs, on part of the lines; also absent: SHANK1, LHX2, COL4A3 |
| [[LINC00466]] | B | LINC00466 activity raises LRRIQ3's level | lines that do not express LINC00466 (15) vs lines expressing it (35) | 1.46× lower at baseline in the lines without LINC00466 | 0.082 | ⚠ within organs, on part of the lines; also absent: FAM124A, NTN1, SSPOP; maybe low, not absent |
| [[DUSP19]] | C | DUSP19 activity raises LRRIQ3's level | lines that do not express DUSP19 (3) vs lines expressing it (47) | 1.78× lower at baseline in the lines without DUSP19 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 0, C 21. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAPGEF4]] | C | LRRIQ3 activity raises RAPGEF4's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 2.18× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |
| [[EPM2A-DT]] | C | LRRIQ3 activity raises EPM2A-DT's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 2.07× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent |
| [[TTC30A]] | C | LRRIQ3 activity raises TTC30A's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 2.04× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |
| [[PRDX6-AS1]] | C | LRRIQ3 activity raises PRDX6-AS1's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 2.02× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |
| [[COPS8-DT]] | C | LRRIQ3 activity raises COPS8-DT's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.97× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |
| [[CCDC30]] | C | LRRIQ3 activity raises CCDC30's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.90× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; co-absent with the target; its own permutation p |
| [[KRBA2]] | C | LRRIQ3 activity raises KRBA2's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.85× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |
| [[FAM227B]] | C | LRRIQ3 activity raises FAM227B's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.77× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |
| [[DUSP19]] | C | LRRIQ3 activity raises DUSP19's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.69× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |
| [[ATP6V0D1-DT]] | C | LRRIQ3 activity raises ATP6V0D1-DT's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.57× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |
| [[CHKB-DT]] | C | LRRIQ3 activity raises CHKB-DT's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.50× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent |
| [[SRP14-DT]] | C | LRRIQ3 activity raises SRP14-DT's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.42× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.734). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.4, 19.6); signed map (31.3, -8.8). **Vector** length 40.7, 5.16% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +7.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.5 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -8.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.8 | -4.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +1.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -3.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.0 | -2.0 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeats and IQ motif containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:74,026,015-74,198,187 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC22773; previously LRRC44 |
| Matched by | ensembl_id |

UniProt [A6PVS8](https://www.uniprot.org/uniprotkb/A6PVS8) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28318](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28318) · Entrez [127255](https://www.ncbi.nlm.nih.gov/gene/127255) · UniProt [A6PVS8](https://www.uniprot.org/uniprotkb/A6PVS8) · Ensembl [ENSG00000162620](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162620)

## Data

Gene col 8546: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8546); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8546, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8546]; `tensor/DDL_lfc|DDL_z.npy` [8546]; `embed/gene_vectors.npy` [8546]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8546 or target_col == 8546). Every well: [[LRRIQ3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRIQ3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
