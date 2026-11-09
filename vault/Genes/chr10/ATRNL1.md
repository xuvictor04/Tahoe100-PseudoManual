---
symbol: "ATRNL1"
type: "gene"
col: 2854
ensembl_id: "ENSG00000107518"
name: "attractin like 1"
location: "10q25.3"
module: 9
arm: "+"
pooled_cpm: 17.71
n_lines_expressing: 29
n_dd_up: 38
n_dd_down: 14
n_dd_up_clean: 32
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 21
direction_downstream: 13
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ATRNL1

*attractin like 1* — 10q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.49× (z +23.0, q 0e+00, up in 24 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.561× (z -7.5, q 4e-11, down in 21 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMCN1]] (+0.70, fdr 7e-06), [[CDH18]] (+0.65, fdr 1e-05), [[LDB2]] (+0.65, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[GXYLT2]] → it (grade B ⚠); 13 go from it, the strongest it → [[NREP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2854.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.49×** | +23.0 | 0e+00 | 24/26 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +15.6 | 0e+00 | 11/26 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.87×** | +13.7 | 3e-40 | 23/26 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.43×** | +10.8 | 4e-25 | 22/26 (A498, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.19×** | +10.2 | 2e-22 | 18/26 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +8.6 | 1e-15 | 13/25 (NCI-H2030, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +8.5 | 1e-15 | 4/19 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +8.3 | 6e-15 | 15/26 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +7.5 | 3e-12 | 4/22 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.76×** | +7.3 | 1e-11 | 18/26 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.75×** | +7.3 | 2e-11 | 7/26 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.67×** | +6.7 | 1e-09 | 20/27 (A498, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.60×** | +5.9 | 2e-07 | 20/26 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.0 | 2e-05 | 7/27 (J82, A498, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.47×** | +4.8 | 6e-05 | 7/25 (HS-578T, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +4.4 | 3e-04 | 6/26 (A-172, NCI-H23, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 5e-04 | 12/26 (A-172, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.28×** | +4.3 | 5e-04 | 15/26 (A498, A-172, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2854.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.561×** | -7.5 | 4e-11 | 21/26 (PANC-1, C32, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.611×** | -6.4 | 6e-08 | 22/26 (C-33 A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.625×** | -5.7 | 2e-06 | 16/26 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.633×** | -5.5 | 4e-06 | 16/26 (C-33 A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.482×** | -4.9 | 9e-05 | 15/25 (C-33 A, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.677×** | -4.9 | 1e-04 | 9/26 (NCI-H460, SW 900, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.770×** | -4.8 | 2e-04 | 14/26 (CFPAC-1, CHP-212, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.694×** | -4.7 | 2e-04 | 14/26 (CHP-212, C32, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.744×** | -3.8 | 0.008 | 20/26 (NCI-H2030, PANC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.755×** | -3.6 | 0.016 | 18/26 (CHP-212, PANC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.748×** | -3.6 | 0.016 | 13/26 (CHP-212, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.774×** | -3.3 | 0.045 | 10/26 (NCI-H23, SW 900, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.781×** | -3.2 | 0.061 | 11/26 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.790×** | -3.0 | 0.098 | 9/26 (CHP-212, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2854. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 83.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -9.9) |
| [[CHP-212 (line)]] | wt | 262 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 17.3 | 3 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.77× (z +10.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.145× (z -9.3) ⚠ cell-cycle shift, explains ~23% of this change |
| [[PANC-1 (line)]] | alt | 47.1 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.210× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.255× (z -9.8) |
| [[A-172 (line)]] | wt | 20.6 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.88× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.149× (z -9.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 26.1 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.98× (z +11.2) | [[Docetaxel (drug)]] 0.05 µM 0.202× (z -9.3) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 30.3 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 4.08× (z +11.7) | — |
| [[A498 (line)]] | wt | 17.1 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.54× (z +13.3) | — |
| [[A549 (line)]] | wt | 5.19 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 8.72× (z +10.0) | — |
| [[LoVo (line)]] | wt | 8.68 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.67× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 8.28 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 7.60× (z +11.4) | [[Belumosudil (drug)]] 5 µM 0.0941× (z -9.1) |
| [[SW 900 (line)]] | alt | 63.9 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.145× (z -11.1) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 6.70 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.46× (z +11.9) | — |
| [[A-427 (line)]] | wt | 5.39 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.32× (z +9.2) | — |
| [[H4 (line)]] | wt | 30.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0586× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LOX-IMVI (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.168× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 7.42 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.74× (z +11.0) | — |
| [[AN3 CA (line)]] | alt | 106 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.72 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.79 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2854), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMCN1]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[CDH18]] | +0.65 | +0.55 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[LDB2]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[NREP]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ARHGAP28]] | +0.63 | +0.58 / +0.65 | both halves | 8e-06 | **novel candidate** |
| [[UNC5C]] | +0.63 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[CDH12]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[SORCS1]] | +0.60 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[MPDZ]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[MMP16]] | +0.60 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[CNTN4]] | +0.60 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[ST6GALNAC3]] | +0.59 | +0.61 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 8, C 13. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GXYLT2]] | B | GXYLT2 activity raises ATRNL1's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 2.89× lower at baseline in the lines without GXYLT2 | 0.016 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[TOP2A]] | B | TOP2A activity lowers ATRNL1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PRKD1]] | B | PRKD1 activity raises ATRNL1's level | lines that do not express PRKD1 (13) vs lines expressing it (37) | 3.68× lower at baseline in the lines without PRKD1 | 0.047 | ⚠ within organs, on part of the lines; also absent: SPART, KCTD16, DMD |
| [[TMEM178B]] | B | TMEM178B activity raises ATRNL1's level | lines that do not express TMEM178B (22) vs lines expressing it (28) | 1.86× lower at baseline in the lines without TMEM178B | 0.049 | ⚠ within organs, on part of the lines; also absent: NTRK3, SPOCK1, POU3F2 |
| [[NREP]] | B | NREP activity raises ATRNL1's level | lines that do not express NREP (13) vs lines expressing it (37) | 3.53× lower at baseline in the lines without NREP | 0.054 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16 |
| [[LRRC7]] | B | LRRC7 activity raises ATRNL1's level | lines that do not express LRRC7 (15) vs lines expressing it (35) | 3.33× lower at baseline in the lines without LRRC7 | 0.060 | ⚠ within organs, on part of the lines; also absent: RNF150, MAP2, KCTD16; maybe low, not absent |
| [[SDC2]] | B | SDC2 activity raises ATRNL1's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 2.81× lower at baseline in the lines without SDC2 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH |
| [[EML1]] | B | EML1 activity raises ATRNL1's level | lines that do not express EML1 (13) vs lines expressing it (37) | 3.80× lower at baseline in the lines without EML1 | 0.093 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FGF2, PYGO1 |
| [[NEGR1]] | C | NEGR1 activity raises ATRNL1's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 4.10× lower at baseline in the lines without NEGR1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[ANKS1B]] | C | ANKS1B activity raises ATRNL1's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 3.65× lower at baseline in the lines without ANKS1B | 0.012 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3; co-absent with the target |
| [[CAMK4]] | C | CAMK4 activity raises ATRNL1's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 3.48× lower at baseline in the lines without CAMK4 | 0.023 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12; co-absent with the target |
| [[NLGN1]] | C | NLGN1 activity raises ATRNL1's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 2.28× lower at baseline in the lines without NLGN1 | 0.045 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 4, C 9. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NREP]] | B | ATRNL1 activity raises NREP's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 3.23× lower at baseline in the lines without ATRNL1 | 0.043 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent |
| [[JAZF1]] | B | ATRNL1 activity raises JAZF1's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 2.37× lower at baseline in the lines without ATRNL1 | 0.058 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent |
| [[ADIRF]] | B | ATRNL1 activity lowers ADIRF's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 2.66× higher at baseline in the lines without ATRNL1 | 0.078 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent |
| [[PCDHGA2]] | B | ATRNL1 activity raises PCDHGA2's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 2.28× lower at baseline in the lines without ATRNL1 | 0.091 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent |
| [[CAMK4]] | C | ATRNL1 activity raises CAMK4's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 4.82× lower at baseline in the lines without ATRNL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent; co-absent with the target |
| [[NLGN1]] | C | ATRNL1 activity raises NLGN1's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 5.04× lower at baseline in the lines without ATRNL1 | 0.017 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent; co-absent with the target |
| [[NEGR1]] | C | ATRNL1 activity raises NEGR1's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 3.71× lower at baseline in the lines without ATRNL1 | 0.021 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent; co-absent with the target |
| [[MPDZ]] | C | ATRNL1 activity raises MPDZ's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 5.95× lower at baseline in the lines without ATRNL1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent; co-absent with the target |
| [[ANKS1B]] | C | ATRNL1 activity raises ANKS1B's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 3.00× lower at baseline in the lines without ATRNL1 | 0.040 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent; co-absent with the target |
| [[GHR]] | C | ATRNL1 activity raises GHR's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 3.12× lower at baseline in the lines without ATRNL1 | 0.046 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent; co-absent with the target |
| [[NKAIN3]] | C | ATRNL1 activity raises NKAIN3's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 2.50× lower at baseline in the lines without ATRNL1 | 0.051 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent; co-absent with the target |
| [[MMP16]] | C | ATRNL1 activity raises MMP16's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 4.20× lower at baseline in the lines without ATRNL1 | 0.052 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.659). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.6, 30.2); signed map (36.8, 33.8). **Vector** length 70.2, 17.8% of its response variance represented; |z| ≥ 3 in 809 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.0 | +23.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.9 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.5 | +13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.4 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.0 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +4.2 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -3.2 | -5.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -0.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | +0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -7.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -0.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -0.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.9 | -0.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | attractin like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.3 — chr10:115,093,365-115,948,999 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0534, FLJ45344, ALP |
| Gene groups (HGNC) | C-type lectin domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VV63](https://www.uniprot.org/uniprotkb/Q5VV63) (Attractin-like protein 1):

> Substrate-recognition component of a membrane-tethered ubiquitin ligase complex that acts as a negative regulator of melanocortin receptor signaling by mediating ubiquitination of MC1R and MC4R. Within the complex, MEGF8 both recognizes MC1R and MC4R and recruits the cytoplasmic E3 ubiquitin ligase MGRN1.

**Summary**, from NCBI Gene [26033](https://www.ncbi.nlm.nih.gov/gene/26033):

> Predicted to enable Notch binding activity. Predicted to act upstream of or within G protein-coupled receptor signaling pathway. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29063](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29063) · Entrez [26033](https://www.ncbi.nlm.nih.gov/gene/26033) · UniProt [Q5VV63](https://www.uniprot.org/uniprotkb/Q5VV63) · Ensembl [ENSG00000107518](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107518)

## Data

Gene col 2854: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2854); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2854, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2854]; `tensor/DDL_lfc|DDL_z.npy` [2854]; `embed/gene_vectors.npy` [2854]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2854 or target_col == 2854). Every well: [[ATRNL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATRNL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
