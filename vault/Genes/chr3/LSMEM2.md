---
symbol: "LSMEM2"
type: "gene"
col: 11044
ensembl_id: "ENSG00000179564"
name: "leucine rich single-pass membrane protein 2"
location: "3p21.31"
module: 47
arm: "+"
pooled_cpm: 4.82
n_lines_expressing: 42
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 25
direction_downstream: 37
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# LSMEM2

*leucine rich single-pass membrane protein 2* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.14× (z +9.4, q 2e-18, up in 15 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.571× (z -4.9, q 5e-04, down in 18 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA3B]] (+0.72, fdr 7e-06, ⚠ read-through risk), [[PHYHD1]] (+0.71, fdr 7e-06), [[FAM83E]] (+0.71, fdr 7e-06), [[SEMA4A]] (+0.70, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[SEMA3B]] → it (grade B ⚠); 37 go from it, the strongest it → [[SLC22A20P]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11044.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +9.4 | 2e-18 | 15/31 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +8.2 | 8e-14 | 5/9 (HOP62, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.33×** | +7.4 | 2e-11 | 6/18 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +5.6 | 3e-06 | 5/11 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.4 | 1e-03 | 6/31 (A549, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +4.2 | 0.002 | 8/30 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Filgotinib (drug)]] 5 µM |  | 1.44× | +3.2 | 0.11 | 4/39 (SW1417, HT-29, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.42× | +3.1 | 0.15 | 6/28 (A-172, HCT15, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11044.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.571×** | -4.9 | 5e-04 | 18/33 (SW48, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.593×** | -4.6 | 0.001 | 22/37 (BT-474, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.598×** | -4.5 | 0.001 | 17/39 (AsPC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.615×** | -4.3 | 0.003 | 14/39 (SW48, RPMI-7951, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **0.628×** | -3.7 | 0.027 | 16/38 (KATO III, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.757×** | -3.4 | 0.053 | 12/37 (AsPC-1, LoVo, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.668×** | -3.4 | 0.053 | 14/33 (LoVo, HCT15, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.662×** | -3.3 | 0.058 | 8/38 (SNU-423, SW48, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.767×** | -3.3 | 0.062 | 16/38 (HT-29, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.691×** | -3.2 | 0.066 | 10/37 (HT-29, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.502×** | -3.2 | 0.079 | 7/27 (SW48, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.710× | -3.0 | 0.12 | 9/37 (AsPC-1, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11044. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 68.0 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0579× (z -13.4) |
| [[BT-474 (line)]] | alt | 7.30 | 0 | 4 | — | [[Digitoxin (drug)]] 0.5 µM 0.0416× (z -9.4) |
| [[HT-29 (line)]] | alt | 8.94 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.126× (z -10.7) |
| [[A-172 (line)]] | wt | 4.34 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 5 µM 0.0799× (z -8.5) |
| [[C32 (line)]] | wt | 3.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 5.72 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0534× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 4.72 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.106× (z -8.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[KATO III (line)]] | alt | 3.50 | 0 | 1 | — | [[Flutamide (drug)]] 5 µM 0.0502× (z -9.0) |
| [[LoVo (line)]] | wt | 11.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0716× (z -11.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 4.64 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0576× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 4.18 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0523× (z -10.7) |
| [[SW480 (line)]] | alt | 8.69 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.253× (z -10.1) |
| [[A-427 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.979 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.955 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.960 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11044), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA3B]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 1.5 kb 3′ of SEMA3B on the same strand (can correlate by spillover, not regulation) |
| [[PHYHD1]] | +0.71 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[FAM83E]] | +0.71 | +0.64 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SEMA4A]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[ARHGAP27]] | +0.68 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.68 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[C19orf38]] | +0.67 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[GP6]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[MROH3P]] | +0.67 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[GPRC5D-AS1]] | +0.66 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[UCKL1-AS1]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[LMO7DN]] | +0.65 | +0.58 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 25, C 0. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA3B]] | B | SEMA3B activity raises LSMEM2's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.74× lower at baseline in the lines without SEMA3B | 2e-04 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[TNNT2]] | B | TNNT2 activity raises LSMEM2's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.49× lower at baseline in the lines without TNNT2 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[MROH3P]] | B | MROH3P activity raises LSMEM2's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 2.15× lower at baseline in the lines without MROH3P | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[KRT16]] | B | KRT16 activity raises LSMEM2's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 2.27× lower at baseline in the lines without KRT16 | 0.004 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[LEMD1]] | B | LEMD1 activity raises LSMEM2's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 2.11× lower at baseline in the lines without LEMD1 | 0.004 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[SULT2B1]] | B | SULT2B1 activity raises LSMEM2's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 2.07× lower at baseline in the lines without SULT2B1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[TMPRSS4]] | B | TMPRSS4 activity raises LSMEM2's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 2.32× lower at baseline in the lines without TMPRSS4 | 0.010 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[C1orf116]] | B | C1orf116 activity raises LSMEM2's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 2.31× lower at baseline in the lines without C1orf116 | 0.013 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[ANO1]] | B | ANO1 activity raises LSMEM2's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 2.05× lower at baseline in the lines without ANO1 | 0.014 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[CRYBG2]] | B | CRYBG2 activity raises LSMEM2's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 1.76× lower at baseline in the lines without CRYBG2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[CLDN4]] | B | CLDN4 activity raises LSMEM2's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 1.97× lower at baseline in the lines without CLDN4 | 0.016 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[LINC01610]] | B | LINC01610 activity raises LSMEM2's level | lines that do not express LINC01610 (45) vs lines expressing it (5) | 1.55× lower at baseline in the lines without LINC01610 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC00879, LINC02099 |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 37, C 0. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC22A20P]] | B | LSMEM2 activity raises SLC22A20P's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 2.06× lower at baseline in the lines without LSMEM2 | 0.005 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[POU2F2]] | B | LSMEM2 activity raises POU2F2's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 2.39× lower at baseline in the lines without LSMEM2 | 0.012 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[ITPKC]] | B | LSMEM2 activity raises ITPKC's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 1.98× lower at baseline in the lines without LSMEM2 | 0.013 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[LINC00672]] | B | LSMEM2 activity raises LINC00672's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 1.65× lower at baseline in the lines without LSMEM2 | 0.013 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[ARHGAP27]] | B | LSMEM2 activity raises ARHGAP27's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 2.02× lower at baseline in the lines without LSMEM2 | 0.016 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[MISP]] | B | LSMEM2 activity raises MISP's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 3.14× lower at baseline in the lines without LSMEM2 | 0.018 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[SEMA4A]] | B | LSMEM2 activity raises SEMA4A's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 2.95× lower at baseline in the lines without LSMEM2 | 0.019 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[PYGM]] | B | LSMEM2 activity raises PYGM's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 1.63× lower at baseline in the lines without LSMEM2 | 0.019 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | B | LSMEM2 activity raises ARHGAP27P1-BPTFP1-KPNA2P3's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 1.52× lower at baseline in the lines without LSMEM2 | 0.026 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[UNC13D]] | B | LSMEM2 activity raises UNC13D's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 2.78× lower at baseline in the lines without LSMEM2 | 0.028 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[FSCN2]] | B | LSMEM2 activity raises FSCN2's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 1.77× lower at baseline in the lines without LSMEM2 | 0.031 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[SH2D4B]] | B | LSMEM2 activity raises SH2D4B's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 1.71× lower at baseline in the lines without LSMEM2 | 0.032 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.5, -18.1); signed map (14.3, 13.9). **Vector** length 78.5, 15.2% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +4.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.1 | +2.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.4 | -4.5 |
|  | [[NG25 (drug)]] 5 µM |  | -3.2 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -4.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -3.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.0 | -2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich single-pass membrane protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:50,279,087-50,288,114 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38608; previously C3orf45 |
| Matched by | ensembl_id |

UniProt [Q8N112](https://www.uniprot.org/uniprotkb/Q8N112) carries no function annotation.

**Summary**, from NCBI Gene [132228](https://www.ncbi.nlm.nih.gov/gene/132228):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26781](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26781) · Entrez [132228](https://www.ncbi.nlm.nih.gov/gene/132228) · UniProt [Q8N112](https://www.uniprot.org/uniprotkb/Q8N112) · Ensembl [ENSG00000179564](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179564)

## Data

Gene col 11044: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11044); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11044, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11044]; `tensor/DDL_lfc|DDL_z.npy` [11044]; `embed/gene_vectors.npy` [11044]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11044 or target_col == 11044). Every well: [[LSMEM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSMEM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
