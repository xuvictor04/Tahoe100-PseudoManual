---
symbol: "PLEKHA2"
type: "gene"
col: 9812
ensembl_id: "ENSG00000169499"
name: "pleckstrin homology domain containing A2"
location: "8p11.22"
module: 164
arm: "+"
pooled_cpm: 104.58
n_lines_expressing: 45
n_dd_up: 3
n_dd_down: 36
n_dd_up_clean: 3
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# PLEKHA2

*pleckstrin homology domain containing A2* — 8p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Dimethyl fumarate (drug)]] 5 µM: 1.31× (z +4.8, q 0.001, up in 30 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.180× (z -44.1, q 0e+00, down in 42 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YEATS2]] (+0.71, fdr 7e-06), [[PFKFB4]] (+0.70, fdr 7e-06), [[INSIG2]] (+0.69, fdr 1e-05); moves opposite to [[REEP3]] (-0.58, fdr 2e-05), [[ARAP2]] (-0.54, fdr 5e-05), [[DDX5]] (-0.53, fdr 4e-05).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[KDM3A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9812.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.31×** | +4.8 | 0.001 | 30/44 (A-172, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.28×** | +4.3 | 0.004 | 25/43 (HEC-1-A, AsPC-1, …) | top dose only | plate-row cell shift |
| [[Fumaric acid (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.044 | 20/44 (HEC-1-A, hTERT-HPNE, …) | top dose only | plate-row cell shift |
| [[NG25 (drug)]] 5 µM |  | 1.40× | +3.2 | 0.21 | 18/42 (A498, SW 900, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.22 | 18/43 (AsPC-1, HS-578T, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.24 | 12/43 (CFPAC-1, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9812.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.180×** | -44.1 | 0e+00 | 42/43 (NCI-H1792, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.140×** | -35.8 | 0e+00 | 43/43 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.157×** | -32.8 | 0e+00 | 43/43 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.189×** | -30.3 | 0e+00 | 43/43 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.227×** | -26.0 | 0e+00 | 42/43 (AsPC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.388×** | -24.3 | 0e+00 | 42/44 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.281×** | -23.1 | 0e+00 | 42/43 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.386×** | -17.3 | 0e+00 | 35/44 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.413×** | -16.1 | 0e+00 | 42/43 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.406×** | -15.8 | 0e+00 | 32/39 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.444×** | -13.7 | 1e-40 | 36/41 (CFPAC-1, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.459×** | -13.6 | 1e-40 | 43/43 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.461×** | -13.5 | 4e-40 | 36/42 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.467×** | -13.3 | 6e-39 | 37/42 (Hs 766T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.518×** | -11.5 | 6e-29 | 39/45 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.541×** | -10.9 | 4e-26 | 41/43 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.568×** | -10.3 | 3e-23 | 40/43 (CFPAC-1, H4, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.722×** | -8.4 | 2e-15 | 33/43 (LoVo, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.629×** | -8.2 | 7e-15 | 39/43 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.728×** | -8.1 | 1e-14 | 31/43 (HOP62, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9812. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 185 | 0 | 19 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0933× (z -41.1) |
| [[LOX-IMVI (line)]] | wt | 167 | 0 | 18 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0699× (z -40.4) |
| [[C32 (line)]] | wt | 104 | 0 | 17 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0647× (z -39.0) |
| [[NCI-H2347 (line)]] | alt | 114 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0652× (z -40.7) |
| [[NCI-H460 (line)]] | wt | 52.2 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -28.8) |
| [[HEC-1-A (line)]] | alt | 154 | 0 | 16 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -31.5) |
| [[MIA PaCa-2 (line)]] | alt | 127 | 0 | 16 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0743× (z -40.2) |
| [[RPMI-7951 (line)]] | alt | 154 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0648× (z -41.8) |
| [[A-172 (line)]] | wt | 221 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0943× (z -40.5) |
| [[Hs 766T (line)]] | wt | 126 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -31.9) |
| [[SW 900 (line)]] | alt | 99.8 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0917× (z -33.4) |
| [[H4 (line)]] | wt | 160 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -20.7) |
| [[NCI-H1573 (line)]] | alt | 53.6 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -28.8) |
| [[J82 (line)]] | alt | 186 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -30.1) |
| [[NCI-H1792 (line)]] | alt | 167 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0796× (z -44.8) |
| [[AsPC-1 (line)]] | alt | 113 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0985× (z -33.7) |
| [[BT-474 (line)]] | alt | 39.5 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -24.7) |
| [[LoVo (line)]] | wt | 70.8 | 1 (1 ⚠) | 11 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.01× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -37.6) |
| [[LS 180 (line)]] | wt | 160 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -25.0) |
| [[Panc 03.27 (line)]] | alt | 166 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -31.8) |
| [[SW480 (line)]] | alt | 118 | 0 | 12 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.124× (z -28.8) |
| [[HOP62 (line)]] | alt | 194 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -22.5) |
| [[HS-578T (line)]] | alt | 84.1 | 0 | 11 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -19.3) |
| [[hTERT-HPNE (line)]] | wt | 152 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -23.8) |
| [[SNU-423 (line)]] | alt | 83.4 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -23.5) |
| [[KATO III (line)]] | alt | 127 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -29.6) |
| [[A498 (line)]] | wt | 147 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -22.6) |
| [[A549 (line)]] | wt | 65.9 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -21.5) |
| [[AN3 CA (line)]] | alt | 142 | 0 | 8 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0468× (z -19.2) |
| [[HepG2_C3A (line)]] | wt | 97.6 | 0 | 8 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.155× (z -14.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.171× (z -14.0) |
| [[NCI-H2030 (line)]] | alt | 46.5 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -23.9) |
| [[RKO (line)]] | wt | 130 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -18.2) |
| [[COLO 205 (line)]] | alt | 64.2 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -25.2) |
| [[HCT15 (line)]] | alt | 170 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -19.3) |
| [[SK-MEL-2 (line)]] | alt | 57.5 | 0 | 7 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.115× (z -15.9) |
| [[SW1417 (line)]] | alt | 57.2 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -17.9) |
| [[SW48 (line)]] | wt | 85.0 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -13.0) |
| [[CHP-212 (line)]] | wt | 180 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -13.6) |
| [[A-427 (line)]] | wt | 40.0 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.261× (z -12.1) |
| [[HT-29 (line)]] | alt | 27.6 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.0997× (z -17.3) |
| [[SW 1088 (line)]] | alt | 143 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0575× (z -11.7) |
| [[C-33 A (line)]] | alt | 35.1 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.208× (z -9.4) |
| [[NCI-H596 (line)]] | alt | 105 | 1 | 0 | [[Fulvestrant (drug)]] 5 µM 2.70× (z +8.5) | — |
| [[NCI-H2122 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.3 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.4 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 25.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.45 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 15.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9812), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YEATS2]] | +0.71 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[PFKFB4]] | +0.70 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.69 | +0.77 / +0.56 | both halves | 1e-05 |  |
| [[SNAPC3]] | +0.69 | +0.74 / +0.58 | both halves | 8e-06 |  |
| [[CABIN1]] | +0.68 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[HERC3]] | +0.67 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[PEX3]] | +0.67 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[PDK3]] | +0.66 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[WDR45B]] | +0.66 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[GYS1]] | +0.65 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[VDAC3]] | +0.65 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[LNPK]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REEP3]] | -0.58 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[ARAP2]] | -0.54 | -0.59 / -0.39 | both halves | 5e-05 | same gene group |
| [[DDX5]] | -0.53 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[SRGAP1]] | -0.53 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[UGGT2]] | -0.52 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[NUTM2A-AS1]] | -0.52 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[ATE1]] | -0.51 | -0.45 / -0.37 | both halves | 7e-05 |  |
| [[LINC00342]] | -0.50 | -0.40 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PLEKHA2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RAB20]] | B | RAB20 activity raises PLEKHA2's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 2.31× lower at baseline in the lines without RAB20 | 0.062 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KDM3A]] | C | PLEKHA2 activity raises KDM3A's level | lines that do not express PLEKHA2 (4) vs lines expressing it (45) | 1.35× lower at baseline in the lines without PLEKHA2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: LSMEM2, ENSG00000285868; maybe low, not absent |
| [[PMS2CL]] | C | PLEKHA2 activity lowers PMS2CL's level | lines that do not express PLEKHA2 (4) vs lines expressing it (45) | 1.53× higher at baseline in the lines without PLEKHA2 | 0.086 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: LSMEM2, ENSG00000285868; maybe low, not absent |
| [[ALG9]] | C | PLEKHA2 activity lowers ALG9's level | lines that do not express PLEKHA2 (4) vs lines expressing it (45) | 1.84× higher at baseline in the lines without PLEKHA2 | 0.091 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: LSMEM2, ENSG00000285868; maybe low, not absent |
| [[FAM216A]] | C | PLEKHA2 activity lowers FAM216A's level | lines that do not express PLEKHA2 (4) vs lines expressing it (45) | 2.95× higher at baseline in the lines without PLEKHA2 | 0.093 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: LSMEM2, ENSG00000285868; maybe low, not absent |
| [[ARL6]] | C | PLEKHA2 activity lowers ARL6's level | lines that do not express PLEKHA2 (4) vs lines expressing it (45) | 2.30× higher at baseline in the lines without PLEKHA2 | 0.098 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: LSMEM2, ENSG00000285868; maybe low, not absent |

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.802). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.0, -16.9); signed map (-37.1, 23.7). **Vector** length 97.1, 33.6% of its response variance represented; |z| ≥ 3 in 1,557 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +6.2 | -35.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.2 | -32.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.8 | -30.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.2 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +2.1 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +3.1 | +3.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.0 | +0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.8 | -0.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -5.3 | -8.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.3 | -13.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.3 | -7.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -4.0 | -2.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.4 | -2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -4.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology domain containing A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.22 — chr8:38,901,235-38,973,912 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAPP2 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Reactome | 4 pathways, smallest: Synthesis of PIPs at the plasma membrane; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HB19](https://www.uniprot.org/uniprotkb/Q9HB19) (Pleckstrin homology domain-containing family A member 2):

> Binds specifically to phosphatidylinositol 3,4-diphosphate (PtdIns3,4P2), but not to other phosphoinositides. May recruit other proteins to the plasma membrane (By similarity).

**Summary**, from NCBI Gene [59339](https://www.ncbi.nlm.nih.gov/gene/59339):

> Enables fibronectin binding activity; laminin binding activity; and phosphatidylinositol-3,4-bisphosphate binding activity. Involved in positive regulation of cell-matrix adhesion. Located in cytoplasm and membrane. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14336](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14336) · Entrez [59339](https://www.ncbi.nlm.nih.gov/gene/59339) · UniProt [Q9HB19](https://www.uniprot.org/uniprotkb/Q9HB19) · Ensembl [ENSG00000169499](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169499)

## Data

Gene col 9812: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9812); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9812, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9812]; `tensor/DDL_lfc|DDL_z.npy` [9812]; `embed/gene_vectors.npy` [9812]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9812 or target_col == 9812). Every well: [[PLEKHA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
