---
symbol: "CNTNAP3"
type: "gene"
col: 2799
ensembl_id: "ENSG00000106714"
name: "contactin associated protein family member 3"
location: "9p12"
module: 196
arm: "+"
pooled_cpm: 14.77
n_lines_expressing: 25
n_dd_up: 8
n_dd_down: 23
n_dd_up_clean: 5
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 10
direction_downstream: 12
tags: ["gene", "module/196"]
generated_by: "tahoemap"
---

# CNTNAP3

*contactin associated protein family member 3* — 9p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.49× (z +8.2, q 1e-13, up in 5 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.59× (z +6.1, q 2e-07, up in 7 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.461× (z -7.3, q 2e-10, down in 19 of 22 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTNAP3B]] (+0.81, fdr 7e-06), [[CNTNAP3C]] (+0.75, fdr 7e-06), [[CNTNAP3P2]] (+0.65, fdr 7e-06); moves opposite to [[CERS5]] (-0.43, fdr 5e-05), [[VPS39]] (-0.37, fdr 2e-04), [[VIPAS39]] (-0.36, fdr 2e-04).
> It is in [[Module 196]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ANKRD29]] → it (grade B ⚠); 12 go from it, the strongest it → [[DPY19L2P2-1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2799.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.49×** | +8.2 | 1e-13 | 5/13 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.27×** | +7.7 | 4e-12 | 4/17 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +6.1 | 2e-07 | 7/22 (SW480, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +4.9 | 2e-04 | 4/16 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.58×** | +4.3 | 0.002 | 12/22 (NCI-H1792, C-33 A, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.020 | 14/22 (NCI-H1792, CFPAC-1, …) | two highest doses |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.42×** | +3.3 | 0.075 | 7/22 (SW 900, Hs 766T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.094 | 4/22 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2799.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.461×** | -7.3 | 2e-10 | 19/22 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.557×** | -5.5 | 1e-05 | 16/19 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.683×** | -5.1 | 7e-05 | 16/20 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.594×** | -4.9 | 1e-04 | 18/22 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.596×** | -4.9 | 1e-04 | 17/22 (PANC-1, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.602×** | -4.8 | 2e-04 | 17/22 (Hs 766T, A549, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.619×** | -4.5 | 5e-04 | 15/22 (Hs 766T, A549, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.629×** | -4.1 | 0.003 | 18/22 (NCI-H2030, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.663×** | -3.9 | 0.007 | 8/22 (SNU-423, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.678×** | -3.7 | 0.015 | 16/22 (Hs 766T, A549, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.683×** | -3.6 | 0.017 | 12/22 (C32, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.687×** | -3.5 | 0.020 | 15/22 (PANC-1, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.490×** | -3.5 | 0.020 | 11/21 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.770×** | -3.5 | 0.020 | 12/22 (Panc 03.27, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.695×** | -3.4 | 0.023 | 12/22 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.704×** | -3.3 | 0.034 | 16/22 (A549, H4, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.706×** | -3.3 | 0.035 | 6/22 (NCI-H2030, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2799. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 74.9 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0536× (z -22.6) |
| [[Hs 766T (line)]] | wt | 195 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -17.7) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0937× (z -15.2) |
| [[PANC-1 (line)]] | alt | 16.8 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -16.8) |
| [[NCI-H2030 (line)]] | alt | 44.7 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -14.6) |
| [[A-427 (line)]] | wt | 14.8 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0896× (z -13.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.102× (z -12.8) |
| [[C32 (line)]] | wt | 33.9 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -15.6) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.150× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 16.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -13.4) |
| [[Panc 03.27 (line)]] | alt | 13.4 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.148× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 31.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -13.4) |
| [[NCI-H23 (line)]] | alt | 6.15 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0937× (z -8.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Docetaxel (Trihydrate) (drug)]] 0.05 µM 0.0793× (z -8.8) |
| [[SNU-423 (line)]] | alt | 16.3 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -11.9) ⚠ cell-cycle shift, explains ~58% of this change |
| [[C-33 A (line)]] | alt | 21.5 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0589× (z -13.0) |
| [[H4 (line)]] | wt | 11.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0764× (z -8.9) |
| [[SW 900 (line)]] | alt | 28.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0857× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 9.06 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.08× (z +8.5) | — |
| [[A-172 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.51 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2799), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTNAP3B]] | +0.81 | +0.77 / +0.78 | both halves | 7e-06 | same gene group; STRING 605 |
| [[CNTNAP3C]] | +0.75 | +0.71 / +0.69 | both halves | 7e-06 | same gene group |
| [[CNTNAP3P2]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[TIMD4]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[HAVCR1]] | +0.53 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[LRRK2]] | +0.50 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[GCAWKR]] | +0.50 | +0.48 / +0.37 | both halves | 9e-05 |  |
| [[ARHGAP26]] | +0.49 | +0.50 / +0.38 | both halves | 6e-05 |  |
| [[LINC01239]] | +0.49 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[ANKRD29]] | +0.49 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[GUCY1B2]] | +0.47 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[ELOVL2]] | +0.46 | +0.50 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CERS5]] | -0.43 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[VPS39]] | -0.37 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[VIPAS39]] | -0.36 | -0.34 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD29]] | B | ANKRD29 activity raises CNTNAP3's level | lines that do not express ANKRD29 (19) vs lines expressing it (31) | 2.13× lower at baseline in the lines without ANKRD29 | 0.060 | ⚠ within organs, on part of the lines; also absent: NHS, PI3, GPR37 |
| [[SOHLH2]] | B | SOHLH2 activity lowers CNTNAP3's level | lines that do not express SOHLH2 (21) vs lines expressing it (29) | 1.50× higher at baseline in the lines without SOHLH2 | 0.084 | ⚠ within organs, on part of the lines; also absent: PRR16, LINC00839, GUCY1B1 |
| [[PIEZO2]] | B | PIEZO2 activity raises CNTNAP3's level | lines that do not express PIEZO2 (30) vs lines expressing it (20) | 1.69× lower at baseline in the lines without PIEZO2 | 0.090 | ⚠ within organs, on part of the lines; also absent: AMPH, COLEC12, ANKRD30B |
| [[DPY19L2P2-1]] | B | DPY19L2P2-1 activity raises CNTNAP3's level | lines that do not express DPY19L2P2-1 (17) vs lines expressing it (33) | 2.20× lower at baseline in the lines without DPY19L2P2-1 | 0.097 | ⚠ within organs, on part of the lines; also absent: RNF182, ENSG00000234405, FGF2 |
| [[CNTNAP3C]] | C | CNTNAP3C activity raises CNTNAP3's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 4.69× lower at baseline in the lines without CNTNAP3C | 2e-04 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA; co-absent with the target |
| [[CNTNAP3B]] | C | CNTNAP3B activity raises CNTNAP3's level | lines that do not express CNTNAP3B (22) vs lines expressing it (28) | 3.98× lower at baseline in the lines without CNTNAP3B | 0.004 | ⚠ within organs, on part of the lines; also absent: CNTNAP3P2, CNTNAP3, CNTNAP3C; co-absent with the target |
| [[CNTNAP3P2]] | C | CNTNAP3P2 activity raises CNTNAP3's level | lines that do not express CNTNAP3P2 (19) vs lines expressing it (31) | 3.35× lower at baseline in the lines without CNTNAP3P2 | 0.006 | ⚠ within organs, on part of the lines; also absent: CNTNAP3B, CNTNAP3, CNTNAP3C; co-absent with the target |
| [[ADAMTSL3]] | C | ADAMTSL3 activity raises CNTNAP3's level | lines that do not express ADAMTSL3 (29) vs lines expressing it (21) | 2.75× lower at baseline in the lines without ADAMTSL3 | 0.017 | ⚠ within organs, on part of the lines; also absent: ANOS1, NTRK3, PSG4; maybe low, not absent; co-absent with the target |
| [[ITGB3]] | C | ITGB3 activity raises CNTNAP3's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 2.83× lower at baseline in the lines without ITGB3 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130; co-absent with the target |
| [[BICC1]] | C | BICC1 activity raises CNTNAP3's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 2.28× lower at baseline in the lines without BICC1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 4, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPY19L2P2-1]] | B | CNTNAP3 activity raises DPY19L2P2-1's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 1.62× lower at baseline in the lines without CNTNAP3 | 0.066 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2 |
| [[DPY19L2P2]] | B | CNTNAP3 activity raises DPY19L2P2's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 1.40× lower at baseline in the lines without CNTNAP3 | 0.081 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2 |
| [[ARNT2]] | B | CNTNAP3 activity raises ARNT2's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 1.76× lower at baseline in the lines without CNTNAP3 | 0.081 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2 |
| [[LRRC36]] | B | CNTNAP3 activity raises LRRC36's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 1.59× lower at baseline in the lines without CNTNAP3 | 0.097 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2 |
| [[CNTNAP3P2]] | C | CNTNAP3 activity raises CNTNAP3P2's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 3.44× lower at baseline in the lines without CNTNAP3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2; co-absent with the target |
| [[CNTNAP3C]] | C | CNTNAP3 activity raises CNTNAP3C's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 2.32× lower at baseline in the lines without CNTNAP3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2; co-absent with the target |
| [[CNTNAP3B]] | C | CNTNAP3 activity raises CNTNAP3B's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 4.51× lower at baseline in the lines without CNTNAP3 | 0.002 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2; co-absent with the target |
| [[BICC1]] | C | CNTNAP3 activity raises BICC1's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 3.24× lower at baseline in the lines without CNTNAP3 | 0.036 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2; co-absent with the target |
| [[NR5A2]] | C | CNTNAP3 activity raises NR5A2's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 3.17× lower at baseline in the lines without CNTNAP3 | 0.040 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2; co-absent with the target |
| [[GCAWKR]] | C | CNTNAP3 activity raises GCAWKR's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 1.64× lower at baseline in the lines without CNTNAP3 | 0.043 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2; co-absent with the target |
| [[L3MBTL4]] | C | CNTNAP3 activity raises L3MBTL4's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 2.44× lower at baseline in the lines without CNTNAP3 | 0.057 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2; co-absent with the target |
| [[ITGB3]] | C | CNTNAP3 activity raises ITGB3's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 3.54× lower at baseline in the lines without CNTNAP3 | 0.074 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2; co-absent with the target |

## Where it sits

- **Module**: [[Module 196]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.630). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.7, 28.7); signed map (19.8, 58.7). **Vector** length 72.8, 21.1% of its response variance represented; |z| ≥ 3 in 717 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +3.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | +4.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | +1.3 | +2.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -7.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.3 | -4.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -3.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -3.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | contactin associated protein family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p12 — chr9:39,064,710-39,288,315 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CASPR3, KIAA1714, FLJ14195, CNTNAP3A |
| Gene groups (HGNC) | Contactin associated protein family |
| Matched by | ensembl_id |

UniProt [Q9BZ76](https://www.uniprot.org/uniprotkb/Q9BZ76) carries no function annotation.

**Summary**, from NCBI Gene [79937](https://www.ncbi.nlm.nih.gov/gene/79937):

> The protein encoded by this gene belongs to the NCP family of cell-recognition molecules. This family represents a distinct subgroup of the neurexins. NCP proteins mediate neuron-glial interactions in vertebrates and glial-glial contact in invertebrates. The protein encoded by this gene may play a role in cell recognition within the nervous system. Alternatively spliced transcript variants encoding different isoforms have been described but their biological nature has not been determined. …

**Accessions** — [HGNC:13834](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13834) · Entrez [79937](https://www.ncbi.nlm.nih.gov/gene/79937) · UniProt [Q9BZ76](https://www.uniprot.org/uniprotkb/Q9BZ76) · Ensembl [ENSG00000106714](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106714)

## Data

Gene col 2799: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2799); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2799, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2799]; `tensor/DDL_lfc|DDL_z.npy` [2799]; `embed/gene_vectors.npy` [2799]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2799 or target_col == 2799). Every well: [[CNTNAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNTNAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
