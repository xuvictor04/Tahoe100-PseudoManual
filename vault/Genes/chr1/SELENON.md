---
symbol: "SELENON"
type: "gene"
col: 8517
ensembl_id: "ENSG00000162430"
name: "selenoprotein N"
location: "1p36.11"
module: 50
arm: "+"
pooled_cpm: 17.72
n_lines_expressing: 48
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# SELENON

*selenoprotein N* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.02× (z +16.4, q 0e+00, up in 26 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.36× (z +4.7, q 3e-04, up in 20 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.379× (z -21.2, q 0e+00, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTSZ]] (+0.80, fdr 7e-06), [[NAGA]] (+0.76, fdr 7e-06), [[FKBP9]] (+0.75, fdr 7e-06); moves opposite to [[CCDC174]] (-0.71, fdr 7e-06), [[NSRP1]] (-0.68, fdr 7e-06), [[ATF4]] (-0.67, fdr 7e-06).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LGALS3BP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8517.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.02×** | +16.4 | 0e+00 | 26/30 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.00×** | +15.0 | 0e+00 | 39/40 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.46×** | +12.9 | 2e-35 | 30/37 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +4.7 | 3e-04 | 17/43 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +4.7 | 3e-04 | 20/46 (NCI-H1792, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.5 | 6e-04 | 19/46 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.30×** | +4.0 | 0.004 | 9/46 (C32, H4, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.6 | 0.020 | 16/45 (LOX-IMVI, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.2 | 0.077 | 9/28 (HEC-1-A, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Pentoxifylline (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.096 | 2/45 (hTERT-HPNE, SW480) | inconsistent across doses | position effect removed |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.23× | +3.1 | 0.11 | 4/44 (A-427, C-33 A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, none with an alert; shown: the 15 strongest. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8517.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.379×** | -21.2 | 0e+00 | 42/46 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.324×** | -17.4 | 0e+00 | 37/44 (RPMI-7951, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.368×** | -14.9 | 0e+00 | 41/46 (J82, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.526×** | -8.8 | 3e-16 | 33/46 (AN3 CA, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.590×** | -7.9 | 4e-13 | 35/44 (NCI-H460, PANC-1, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.672×** | -6.2 | 7e-08 | 23/45 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.674×** | -6.1 | 9e-08 | 24/46 (LS 180, C32, …) | two highest doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.685×** | -5.2 | 2e-05 | 24/45 (CHP-212, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.732×** | -4.8 | 9e-05 | 21/46 (C-33 A, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.726×** | -4.7 | 2e-04 | 21/45 (SW1417, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.763×** | -4.2 | 0.001 | 18/45 (LS 180, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.840× | -3.8 | 0.006 | 11/45 (C-33 A, SHP-77, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.780×** | -3.6 | 0.017 | 18/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.852× | -3.5 | 0.017 | 13/46 (RPMI-7951, C-33 A, …) | rises with dose | position effect removed |
| [[Hexylresorcinol (drug)]] 5 µM |  | 0.854× | -3.5 | 0.019 | 3/46 (RPMI-7951, C-33 A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8517. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -20.5) |
| [[PANC-1 (line)]] | alt | 18.8 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -17.4) |
| [[LoVo (line)]] | wt | 17.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.34× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -13.6) |
| [[A-172 (line)]] | wt | 25.6 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.112× (z -17.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.329× (z -12.9) |
| [[HOP62 (line)]] | alt | 18.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.08× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -12.7) |
| [[J82 (line)]] | alt | 26.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -18.1) |
| [[RKO (line)]] | wt | 38.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0644× (z -28.8) |
| [[A-427 (line)]] | wt | 26.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -12.8) |
| [[A549 (line)]] | wt | 14.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.98× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -10.6) |
| [[AN3 CA (line)]] | alt | 46.2 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0771× (z -10.2) |
| [[H4 (line)]] | wt | 25.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0592× (z -13.9) |
| [[HEC-1-A (line)]] | alt | 18.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -10.4) |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -12.4) |
| [[LS 180 (line)]] | wt | 12.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -13.0) |
| [[SW480 (line)]] | alt | 11.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.89× (z +9.7) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 52.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.217× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 13.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -8.6) |
| [[HS-578T (line)]] | alt | 17.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -12.6) |
| [[hTERT-HPNE (line)]] | wt | 24.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -10.8) |
| [[KATO III (line)]] | alt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 23.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.117× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 24.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.226× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 9.71 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 18.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0435× (z -16.2) |
| [[A498 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8517), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSZ]] | +0.80 | +0.78 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[NAGA]] | +0.76 | +0.78 / +0.73 | both halves | 7e-06 |  |
| [[FKBP9]] | +0.75 | +0.72 / +0.72 | both halves | 7e-06 | same gene group |
| [[AKT1]] | +0.74 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[POMGNT1]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 | STRING 432 |
| [[PPT1]] | +0.73 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[CNPY3]] | +0.73 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[LAMP1]] | +0.72 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[PRKCSH]] | +0.70 | +0.71 / +0.59 | both halves | 7e-06 | same gene group |
| [[MAN2B2]] | +0.70 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[CRTAP]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[CDK16]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC174]] | -0.71 | -0.71 / -0.66 | both halves | 7e-06 |  |
| [[NSRP1]] | -0.68 | -0.70 / -0.63 | both halves | 7e-06 |  |
| [[ATF4]] | -0.67 | -0.60 / -0.71 | both halves | 7e-06 |  |
| [[NKAP]] | -0.66 | -0.68 / -0.57 | both halves | 9e-06 |  |
| [[ZNF503]] | -0.64 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[RBMX2]] | -0.64 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[SNW1]] | -0.63 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[MED19]] | -0.62 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[MRPS18C]] | -0.62 | -0.58 / -0.63 | both halves | 8e-06 |  |
| [[NRBF2]] | -0.62 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.62 | -0.61 / -0.62 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[C1orf131]] | -0.62 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[PPIG]] | -0.61 | -0.64 / -0.57 | both halves | 8e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALS3BP]] | B | LGALS3BP activity lowers SELENON's level | lines that do not express LGALS3BP (7) vs lines expressing it (43) | 2.06× higher at baseline in the lines without LGALS3BP | 0.035 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[GAS6]] | B | GAS6 activity raises SELENON's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 1.32× lower at baseline in the lines without GAS6 | 0.048 | ⚠ within organs, on part of the lines |
| [[CERCAM]] | B | CERCAM activity raises SELENON's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 1.85× lower at baseline in the lines without CERCAM | 0.054 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[CRTAP]] | C | CRTAP activity raises SELENON's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 2.61× lower at baseline in the lines without CRTAP | 0.033 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.844). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.3, -23.5); signed map (-25.5, -37.9). **Vector** length 98.9, 22.8% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Extracellular matrix organization* (reactome, mean cos +0.54 to 12); *Degradation of the extracellular matrix* (reactome, mean cos +0.51 to 7); *epithelial mesenchymal transition* (hallmark, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.1 | +16.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.9 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.2 | +15.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.9 | +3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.9 | +4.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +3.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.8 | +2.4 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.7 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.6 | -17.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.5 | -14.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.8 | -8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -21.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -6.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -3.6 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | selenoprotein N |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:25,800,193-25,818,221 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SELN, RSS; previously RSMD1, MDRS1, SEPN1 |
| Gene groups (HGNC) | EF-hand domain containing; Selenoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZV5](https://www.uniprot.org/uniprotkb/Q9NZV5) (Selenoprotein N):

> [Isoform 2]: Plays an important role in cell protection against oxidative stress and in the regulation of redox-related calcium homeostasis. Regulates the calcium level of the ER by protecting the calcium pump ATP2A2 against the oxidoreductase ERO1A-mediated oxidative damage. Within the ER, ERO1A activity increases the concentration of H(2)O(2), which attacks the luminal thiols in ATP2A2 and thus leads to cysteinyl sulfenic acid formation (-SOH) and SEPN1 reduces the SOH back to free thiol …

**Summary**, from NCBI Gene [57190](https://www.ncbi.nlm.nih.gov/gene/57190):

> This gene encodes a glycoprotein that is localized in the endoplasmic reticulum. It plays an important role in cell protection against oxidative stress, and in the regulation of redox-related calcium homeostasis. Mutations in this gene are associated with early onset muscle disorders, referred to as SEPN1-related myopathy. SEPN1-related myopathy consists of 4 autosomal recessive disorders, originally thought to be separate entities: rigid spine muscular dystrophy (RSMD1), the classical form of …

**Accessions** — [HGNC:15999](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15999) · Entrez [57190](https://www.ncbi.nlm.nih.gov/gene/57190) · UniProt [Q9NZV5](https://www.uniprot.org/uniprotkb/Q9NZV5) · Ensembl [ENSG00000162430](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162430)

## Data

Gene col 8517: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8517); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8517, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8517]; `tensor/DDL_lfc|DDL_z.npy` [8517]; `embed/gene_vectors.npy` [8517]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8517 or target_col == 8517). Every well: [[SELENON — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SELENON.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
