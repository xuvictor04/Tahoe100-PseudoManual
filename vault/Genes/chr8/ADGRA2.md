---
symbol: "ADGRA2"
type: "gene"
col: 319
ensembl_id: "ENSG00000020181"
name: "adhesion G protein-coupled receptor A2"
location: "8p11.23"
module: 62
arm: "+"
pooled_cpm: 2.76
n_lines_expressing: 39
n_dd_up: 25
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 9
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# ADGRA2

*adhesion G protein-coupled receptor A2* — 8p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.69× (z +14.7, q 0e+00, up in 27 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.457× (z -7.5, q 4e-11, down in 18 of 33 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.116×); [[Digitoxin (drug)]] 5 µM in 1 line (CHP-212 0.0578×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (LoVo 0.0768×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF423]] (+0.66, fdr 1e-05), [[ADAMTS7]] (+0.66, fdr 1e-05), [[GRIP2]] (+0.64, fdr 4e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[RTN4RL1]] → it (grade B ⚠); 9 go from it, the strongest it → [[GLIPR2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 319.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.69×** | +14.7 | 0e+00 | 27/36 (Panc 03.27, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.69×** | +13.3 | 6e-38 | 13/21 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.42×** | +11.9 | 3e-30 | 24/35 (A-172, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.41×** | +11.7 | 3e-29 | 24/34 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.24×** | +11.2 | 8e-27 | 23/33 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.87×** | +10.0 | 1e-21 | 4/10 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.93×** | +9.8 | 7e-21 | 1/5 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.97×** | +9.1 | 7e-18 | 14/25 (LoVo, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.35×** | +8.1 | 3e-14 | 22/35 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +6.7 | 1e-09 | 1/5 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.98×** | +6.5 | 4e-09 | 12/27 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.95×** | +6.1 | 5e-08 | 6/12 (LoVo, A498, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.85×** | +5.6 | 9e-07 | 11/21 (A498, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.82×** | +5.1 | 1e-05 | 6/29 (A-172, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.62×** | +4.6 | 2e-04 | 10/34 (A-172, SNU-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.2 | 0.001 | 6/35 (LOX-IMVI, A-172, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.007 | 6/28 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.014 | 5/23 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.057 | 3/36 (A-172, CHP-212, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.39×** | +2.9 | 0.095 | 3/17 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 319.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.116×); [[Digitoxin (drug)]] 5 µM in 1 line (CHP-212 0.0578×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (LoVo 0.0768×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.457×** | -7.5 | 4e-11 | 18/33 (C-33 A, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.620×** | -4.4 | 0.003 | 12/29 (LoVo, CHP-212, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.637×** | -4.3 | 0.003 | 11/34 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 319. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 38.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -11.0) |
| [[LoVo (line)]] | wt | 3.19 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.03× (z +9.0) | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0768× (z -9.2) |
| [[A498 (line)]] | wt | 4.75 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.59× (z +8.8) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[A549 (line)]] | wt | 2.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 0.930 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +8.7) | — |
| [[A-172 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.911 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.809 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.968 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.560 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.539 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.876 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.704 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.788 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 319), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF423]] | +0.66 | +0.57 / +0.72 | both halves | 1e-05 | **novel candidate** |
| [[ADAMTS7]] | +0.66 | +0.54 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[GRIP2]] | +0.64 | +0.42 / +0.70 | both halves | 4e-05 | **novel candidate** |
| [[AK1]] | +0.60 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[ZNF536]] | +0.59 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[APLP1]] | +0.58 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[MIR3659HG]] | +0.58 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[DACH2]] | +0.56 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[INKA2]] | +0.54 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[PARD6G]] | +0.54 | +0.32 / +0.65 | both halves | 2e-04 |  |
| [[PDZD4]] | +0.54 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[NBEAP1]] | +0.53 | +0.44 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RTN4RL1]] | B | RTN4RL1 activity raises ADGRA2's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 2.31× lower at baseline in the lines without RTN4RL1 | 0.027 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ADGRA2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SYT11]] | B | SYT11 activity raises ADGRA2's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 2.23× lower at baseline in the lines without SYT11 | 0.033 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1 |
| [[LINC02384]] | B | LINC02384 activity raises ADGRA2's level | lines that do not express LINC02384 (26) vs lines expressing it (24) | 2.37× lower at baseline in the lines without LINC02384 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000259929, ENSG00000277693, FAM230C; maybe low, not absent |
| [[GAS6]] | B | GAS6 activity raises ADGRA2's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 1.83× lower at baseline in the lines without GAS6 | 0.083 | ⚠ within organs, on part of the lines |
| [[GLIS1]] | B | GLIS1 activity raises ADGRA2's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 1.81× lower at baseline in the lines without GLIS1 | 0.0995 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent |
| [[ADAMTS7]] | C | ADAMTS7 activity raises ADGRA2's level | lines that do not express ADAMTS7 (17) vs lines expressing it (33) | 2.45× lower at baseline in the lines without ADAMTS7 | 0.038 | ⚠ within organs, on part of the lines; also absent: VASH1, FHL1, ANTXR1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLIPR2]] | B | ADGRA2 activity raises GLIPR2's level | lines that do not express ADGRA2 (11) vs lines expressing it (39) | 2.62× lower at baseline in the lines without ADGRA2 | 0.032 | ⚠ within organs, on part of the lines; also absent: CERCAM, SPEG, STARD9; maybe low, not absent |
| [[GRIN2C]] | B | ADGRA2 activity raises GRIN2C's level | lines that do not express ADGRA2 (11) vs lines expressing it (39) | 1.92× lower at baseline in the lines without ADGRA2 | 0.034 | ⚠ within organs, on part of the lines; also absent: CERCAM, SPEG, STARD9; maybe low, not absent |
| [[GAS6]] | B | ADGRA2 activity raises GAS6's level | lines that do not express ADGRA2 (11) vs lines expressing it (39) | 1.32× lower at baseline in the lines without ADGRA2 | 0.036 | ⚠ within organs, on part of the lines; also absent: CERCAM, SPEG, STARD9; maybe low, not absent |
| [[FDXR]] | B | ADGRA2 activity raises FDXR's level | lines that do not express ADGRA2 (11) vs lines expressing it (39) | 1.58× lower at baseline in the lines without ADGRA2 | 0.060 | ⚠ within organs, on part of the lines; also absent: CERCAM, SPEG, STARD9; maybe low, not absent |
| [[IRF4]] | B | ADGRA2 activity lowers IRF4's level | lines that do not express ADGRA2 (11) vs lines expressing it (39) | 1.22× higher at baseline in the lines without ADGRA2 | 0.061 | ⚠ within organs, on part of the lines; also absent: CERCAM, SPEG, STARD9; maybe low, not absent |
| [[SEPTIN3]] | B | ADGRA2 activity raises SEPTIN3's level | lines that do not express ADGRA2 (11) vs lines expressing it (39) | 2.10× lower at baseline in the lines without ADGRA2 | 0.064 | ⚠ within organs, on part of the lines; also absent: CERCAM, SPEG, STARD9; maybe low, not absent |
| [[CAMK2B]] | B | ADGRA2 activity raises CAMK2B's level | lines that do not express ADGRA2 (11) vs lines expressing it (39) | 1.86× lower at baseline in the lines without ADGRA2 | 0.068 | ⚠ within organs, on part of the lines; also absent: CERCAM, SPEG, STARD9; maybe low, not absent |
| [[NPTXR]] | B | ADGRA2 activity raises NPTXR's level | lines that do not express ADGRA2 (11) vs lines expressing it (39) | 2.18× lower at baseline in the lines without ADGRA2 | 0.0998 | ⚠ within organs, on part of the lines; also absent: CERCAM, SPEG, STARD9; maybe low, not absent |
| [[ADAMTS7]] | C | ADGRA2 activity raises ADAMTS7's level | lines that do not express ADGRA2 (11) vs lines expressing it (39) | 2.19× lower at baseline in the lines without ADGRA2 | 0.080 | ⚠ within organs, on part of the lines; also absent: CERCAM, SPEG, STARD9; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.522). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.0, 37.8); signed map (44.6, -23.8). **Vector** length 44.6, 6.18% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +11.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +6.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +0.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -4.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -2.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.7 | -4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -7.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -0.4 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.1 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.23 — chr8:37,784,191-37,844,896 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TEM5, DKFZp434C211, DKFZp434J0911, KIAA1531, FLJ14390; previously GPR124 |
| Gene groups (HGNC) | Immunoglobulin like domain containing; Adhesion G protein-coupled receptors, subfamily A |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PE1](https://www.uniprot.org/uniprotkb/Q96PE1) (Adhesion G protein-coupled receptor A2):

> Endothelial receptor which functions together with RECK to enable brain endothelial cells to selectively respond to Wnt7 signals (WNT7A or WNT7B). Plays a key role in Wnt7-specific responses, such as endothelial cell sprouting and migration in the forebrain and neural tube, and establishment of the blood-brain barrier (By similarity). Acts as a Wnt7-specific coactivator of canonical Wnt signaling: required to deliver RECK-bound Wnt7 to frizzled by assembling a higher-order …

**Summary**, from NCBI Gene [25960](https://www.ncbi.nlm.nih.gov/gene/25960):

> Predicted to enable G protein-coupled receptor activity. Involved in canonical Wnt signaling pathway. Located in plasma membrane. Part of Wnt signalosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17849](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17849) · Entrez [25960](https://www.ncbi.nlm.nih.gov/gene/25960) · UniProt [Q96PE1](https://www.uniprot.org/uniprotkb/Q96PE1) · Ensembl [ENSG00000020181](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000020181)

## Data

Gene col 319: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 319); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 319, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 319]; `tensor/DDL_lfc|DDL_z.npy` [319]; `embed/gene_vectors.npy` [319]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 319 or target_col == 319). Every well: [[ADGRA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
