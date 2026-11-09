---
symbol: "RPH3AL"
type: "gene"
col: 11161
ensembl_id: "ENSG00000181031"
name: "rabphilin 3A like (without C2 domains)"
location: "17p13.3"
module: 31
arm: "+"
pooled_cpm: 64.2
n_lines_expressing: 40
n_dd_up: 0
n_dd_down: 38
n_dd_up_clean: 0
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 6
direction_downstream: 9
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# RPH3AL

*rabphilin 3A like (without C2 domains)* — 17p13.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.322× (z -20.2, q 0e+00, down in 37 of 37 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNS4]] (+0.61, fdr 1e-05), [[LINC02320]] (+0.59, fdr 1e-05), [[PDE9A]] (+0.54, fdr 2e-05); moves opposite to [[ZNF521]] (-0.49, fdr 6e-05), [[KLF7]] (-0.45, fdr 4e-05), [[APBB1IP]] (-0.43, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LINC02320]] → it (grade B ⚠); 9 go from it, the strongest it → [[KIF13B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11161.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 0.5 µM |  | 1.31× | +3.4 | 0.40 | 18/38 (C-33 A, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.28× | +3.0 | 0.46 | 14/37 (BT-474, NCI-H1573, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11161.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.322×** | -20.2 | 0e+00 | 37/37 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.295×** | -15.4 | 0e+00 | 37/38 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.313×** | -14.1 | 7e-43 | 32/37 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.464×** | -13.7 | 2e-40 | 34/39 (SHP-77, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.342×** | -13.5 | 1e-39 | 35/37 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.344×** | -13.5 | 2e-39 | 36/37 (HEC-1-A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.362×** | -12.8 | 9e-36 | 36/38 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.371×** | -12.5 | 5e-34 | 32/37 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.374×** | -12.4 | 2e-33 | 36/38 (SHP-77, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.375×** | -12.4 | 2e-33 | 33/37 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.411×** | -10.8 | 2e-25 | 31/36 (H4, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.440×** | -10.4 | 2e-23 | 34/37 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.249×** | -9.2 | 2e-18 | 35/39 (LS 180, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.654×** | -7.6 | 2e-12 | 29/38 (SNU-1, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.569×** | -6.8 | 3e-10 | 25/36 (SHP-77, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.381×** | -6.4 | 7e-09 | 24/36 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.636×** | -5.7 | 3e-07 | 27/37 (HT-29, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.671×** | -5.0 | 1e-05 | 26/37 (HCT15, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.512×** | -4.4 | 2e-04 | 20/38 (H4, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11161. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 254 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0610× (z -26.2) |
| [[SW480 (line)]] | alt | 113 | 0 | 16 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0860× (z -22.1) |
| [[SHP-77 (line)]] | alt | 351 | 0 | 12 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -22.3) |
| [[HEC-1-A (line)]] | alt | 99.4 | 0 | 11 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -16.6) |
| [[NCI-H23 (line)]] | alt | 48.9 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -20.4) |
| [[SW 900 (line)]] | alt | 157 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -19.6) |
| [[HOP62 (line)]] | alt | 51.7 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -17.9) |
| [[LoVo (line)]] | wt | 60.4 | 0 | 10 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -16.9) |
| [[KATO III (line)]] | alt | 68.9 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0612× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -13.7) |
| [[A-172 (line)]] | wt | 34.0 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -16.8) |
| [[A549 (line)]] | wt | 196 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -19.5) |
| [[COLO 205 (line)]] | alt | 83.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -15.0) |
| [[HepG2_C3A (line)]] | wt | 83.5 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -14.0) |
| [[LS 180 (line)]] | wt | 92.6 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.144× (z -14.6) |
| [[NCI-H1792 (line)]] | alt | 83.7 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -17.7) |
| [[C-33 A (line)]] | alt | 52.3 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0973× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -10.8) |
| [[H4 (line)]] | wt | 62.0 | 0 | 6 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0603× (z -17.8) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.143× (z -12.8) |
| [[A-427 (line)]] | wt | 34.6 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.255× (z -11.0) |
| [[BT-474 (line)]] | alt | 43.0 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.111× (z -13.6) |
| [[HCT15 (line)]] | alt | 93.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0985× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -12.4) |
| [[HT-29 (line)]] | alt | 61.1 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -14.2) |
| [[A498 (line)]] | wt | 42.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -19.3) |
| [[Hs 766T (line)]] | wt | 38.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 29.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 36.2 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 21.2 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0258× (z -20.1) |
| [[NCI-H1573 (line)]] | alt | 18.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 20.2 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.126× (z -11.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.201× (z -9.0) |
| [[SNU-1 (line)]] | wt | 31.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -9.7) |
| [[SW48 (line)]] | wt | 40.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 32.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -12.6) |
| [[RKO (line)]] | wt | 29.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -16.4) |
| [[SW1417 (line)]] | alt | 18.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -9.1) |
| [[AN3 CA (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.18 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.7 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.69 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.5 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.0 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11161), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNS4]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[LINC02320]] | +0.59 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[PDE9A]] | +0.54 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[LAMA5]] | +0.53 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[ITPK1]] | +0.52 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[CASC19]] | +0.52 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[ITGB4]] | +0.51 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[GPR35]] | +0.51 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[B3GNT3]] | +0.51 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[DIO3OS]] | +0.50 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[ARHGEF16]] | +0.50 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[MST1R]] | +0.50 | +0.49 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF521]] | -0.49 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[KLF7]] | -0.45 | -0.41 / -0.40 | both halves | 4e-05 |  |
| [[APBB1IP]] | -0.43 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[SLC66A3]] | -0.42 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[SLC30A4]] | -0.42 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[ARL10]] | -0.42 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[PPP2R3A]] | -0.41 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[SLC41A2]] | -0.41 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[HCFC1R1]] | -0.41 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[CCL28]] | -0.41 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[CERT1]] | -0.40 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[COL1A2]] | -0.39 | -0.44 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02320]] | B | LINC02320 activity raises RPH3AL's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 2.51× lower at baseline in the lines without LINC02320 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[CHN2]] | B | CHN2 activity raises RPH3AL's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 1.89× lower at baseline in the lines without CHN2 | 0.020 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[TRPM2-AS]] | B | TRPM2-AS activity raises RPH3AL's level | lines that do not express TRPM2-AS (29) vs lines expressing it (21) | 2.42× lower at baseline in the lines without TRPM2-AS | 0.020 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1 |
| [[DSCAML1]] | B | DSCAML1 activity raises RPH3AL's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 2.33× lower at baseline in the lines without DSCAML1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[COL1A2]] | B | COL1A2 activity lowers RPH3AL's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 2.72× higher at baseline in the lines without COL1A2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5 |
| [[HR]] | B | HR activity raises RPH3AL's level | lines that do not express HR (23) vs lines expressing it (27) | 1.80× lower at baseline in the lines without HR | 0.079 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF13B]] | B | RPH3AL activity raises KIF13B's level | lines that do not express RPH3AL (10) vs lines expressing it (40) | 2.33× lower at baseline in the lines without RPH3AL | 0.027 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, PATJ; maybe low, not absent |
| [[LINC02320]] | B | RPH3AL activity raises LINC02320's level | lines that do not express RPH3AL (10) vs lines expressing it (40) | 3.09× lower at baseline in the lines without RPH3AL | 0.028 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, PATJ; maybe low, not absent |
| [[COL1A2]] | B | RPH3AL activity lowers COL1A2's level | lines that do not express RPH3AL (10) vs lines expressing it (40) | 10.30× higher at baseline in the lines without RPH3AL | 0.030 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, PATJ; maybe low, not absent |
| [[ITGB4]] | B | RPH3AL activity raises ITGB4's level | lines that do not express RPH3AL (10) vs lines expressing it (40) | 5.24× lower at baseline in the lines without RPH3AL | 0.030 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, PATJ; maybe low, not absent |
| [[GSAP]] | B | RPH3AL activity raises GSAP's level | lines that do not express RPH3AL (10) vs lines expressing it (40) | 1.83× lower at baseline in the lines without RPH3AL | 0.064 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, PATJ; maybe low, not absent |
| [[MALL]] | B | RPH3AL activity raises MALL's level | lines that do not express RPH3AL (10) vs lines expressing it (40) | 3.36× lower at baseline in the lines without RPH3AL | 0.066 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, PATJ; maybe low, not absent |
| [[PSD4]] | B | RPH3AL activity raises PSD4's level | lines that do not express RPH3AL (10) vs lines expressing it (40) | 2.35× lower at baseline in the lines without RPH3AL | 0.088 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, PATJ; maybe low, not absent |
| [[DLG3]] | B | RPH3AL activity raises DLG3's level | lines that do not express RPH3AL (10) vs lines expressing it (40) | 2.90× lower at baseline in the lines without RPH3AL | 0.088 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, PATJ; maybe low, not absent |
| [[HCFC1R1]] | B | RPH3AL activity lowers HCFC1R1's level | lines that do not express RPH3AL (10) vs lines expressing it (40) | 1.26× higher at baseline in the lines without RPH3AL | 0.093 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, PATJ; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.419). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.1, 50.0); signed map (5.6, 37.6). **Vector** length 82.8, 23.1% of its response variance represented; |z| ≥ 3 in 1,133 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.5 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | -3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +0.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -3.3 | -7.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -0.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -0.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.1 | -0.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.0 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | rabphilin 3A like (without C2 domains) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:212,389-386,254 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Noc2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNE2](https://www.uniprot.org/uniprotkb/Q9UNE2) (Rab effector Noc2):

> Rab GTPase effector involved in the late steps of regulated exocytosis, both in endocrine and exocrine cells (By similarity). Acts as a potential RAB3B effector protein in epithelial cells.

**Summary**, from NCBI Gene [9501](https://www.ncbi.nlm.nih.gov/gene/9501):

> The protein encoded by this gene plays a direct regulatory role in calcium-ion-dependent exocytosis in both endocrine and exocrine cells and plays a key role in insulin secretion by pancreatic cells. This gene is likely a tumor suppressor. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:10296](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10296) · Entrez [9501](https://www.ncbi.nlm.nih.gov/gene/9501) · UniProt [Q9UNE2](https://www.uniprot.org/uniprotkb/Q9UNE2) · Ensembl [ENSG00000181031](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181031)

## Data

Gene col 11161: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11161); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11161, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11161]; `tensor/DDL_lfc|DDL_z.npy` [11161]; `embed/gene_vectors.npy` [11161]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11161 or target_col == 11161). Every well: [[RPH3AL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPH3AL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
