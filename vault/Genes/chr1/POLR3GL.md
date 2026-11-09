---
symbol: "POLR3GL"
type: "gene"
col: 4297
ensembl_id: "ENSG00000121851"
name: "RNA polymerase III subunit GL"
location: "1q21.1"
module: 106
arm: "+"
pooled_cpm: 14.15
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# POLR3GL

*RNA polymerase III subunit GL* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +7.0, q 2e-09, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.306× (z -10.0, q 7e-21, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM7-AS2]] (+0.62, fdr 1e-05), [[PHF21A]] (+0.60, fdr 1e-05), [[CLPX]] (+0.58, fdr 1e-05); moves opposite to [[TBILA]] (-0.49, fdr 8e-05), [[LRP8]] (-0.49, fdr 3e-05), [[RNF32-AS1]] (-0.49, fdr 0.001, ⚠ one half only (not replicated)), [[SLC19A1]] (-0.48, fdr 3e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GRAMD2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4297.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +7.0 | 2e-09 | 35/47 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.88×** | +5.4 | 2e-05 | 30/36 (HEC-1-A, A-172, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.5 | 0.001 | 27/42 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.63×** | +4.0 | 0.008 | 25/45 (A498, C-33 A, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.58×** | +3.9 | 0.009 | 23/47 (SW 900, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.60×** | +3.9 | 0.010 | 15/25 (J82, PANC-1, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +3.8 | 0.011 | 27/42 (HOP62, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.55×** | +3.8 | 0.011 | 24/47 (A498, J82, …) | all doses, flat | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.33×** | +3.5 | 0.034 | 18/48 (RKO, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.44×** | +3.2 | 0.088 | 19/47 (A-172, A498, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4297.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.306×** | -10.0 | 7e-21 | 46/47 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.331×** | -9.4 | 2e-18 | 42/47 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.406×** | -7.6 | 5e-12 | 38/46 (SHP-77, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.470×** | -6.4 | 3e-08 | 34/46 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.530×** | -5.4 | 9e-06 | 33/47 (NCI-H460, SNU-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.308×** | -5.0 | 4e-05 | 31/45 (A-427, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.568×** | -4.8 | 2e-04 | 31/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.565×** | -4.5 | 4e-04 | 26/47 (SNU-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.636×** | -3.8 | 0.009 | 21/47 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.643×** | -3.7 | 0.011 | 23/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.628×** | -3.7 | 0.011 | 21/47 (LOX-IMVI, SW1417, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.424×** | -3.7 | 0.011 | 25/48 (HCT15, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.647×** | -3.7 | 0.011 | 24/46 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.430×** | -3.6 | 0.012 | 20/36 (SW 900, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.675×** | -3.2 | 0.054 | 19/42 (NCI-H23, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.685×** | -3.2 | 0.054 | 18/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.775×** | -3.0 | 0.087 | 20/47 (A549, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Pentagastrin (drug)]] 5 µM |  | **0.777×** | -3.0 | 0.092 | 16/48 (LS 180, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4297. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 21.0 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -12.1) |
| [[SW480 (line)]] | alt | 17.0 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.162× (z -11.5) |
| [[A-427 (line)]] | wt | 20.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.196× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -8.5) |
| [[SHP-77 (line)]] | alt | 24.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.189× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0668× (z -10.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 20.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -10.6) |
| [[PANC-1 (line)]] | alt | 21.9 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.216× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0745× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 40.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -10.3) |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0671× (z -12.5) |
| [[A-172 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4297), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM7-AS2]] | +0.62 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[PHF21A]] | +0.60 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[CLPX]] | +0.58 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[PAPOLG]] | +0.57 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[CEPT1]] | +0.57 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[SCAND1]] | +0.57 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[ANKRA2]] | +0.56 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[KLF9]] | +0.56 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ILF3-DT]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[ARF5]] | +0.55 | +0.30 / +0.60 | both halves | 2e-04 |  |
| [[MRPS31]] | +0.55 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[ATP5IF1]] | +0.55 | +0.42 / +0.61 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBILA]] | -0.49 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[LRP8]] | -0.49 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[RNF32-AS1]] | -0.49 | -0.16 / -0.57 | ⚠ one half (not replicated) | 0.001 |  |
| [[SLC19A1]] | -0.48 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[HNRNPAB]] | -0.47 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[PSMD1]] | -0.47 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[SMG1P3]] | -0.47 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[EIF5A]] | -0.46 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[TTL]] | -0.46 | -0.37 / -0.39 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRAMD2B]] | B | GRAMD2B activity lowers POLR3GL's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 1.32× higher at baseline in the lines without GRAMD2B | 0.092 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.493). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.5, -25.9); signed map (-6.8, 7.7). **Vector** length 63.0, 12.8% of its response variance represented; |z| ≥ 3 in 847 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +7.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.9 | +2.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.8 | +2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.7 | +0.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | -4.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.4 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -10.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase III subunit GL |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.1 — chr1:145,964,690-145,978,848 (+) |
| Ensembl biotype | protein_coding |
| Also known as | flj32422, MGC3200 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 10 pathways, smallest: RNA Polymerase III Chain Elongation; RNA Polymerase III Transcription Termination; RNA Polymerase III Transcription Initiation From Type 2 Promoter |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BT43](https://www.uniprot.org/uniprotkb/Q9BT43) (DNA-directed RNA polymerase III subunit RPC7-like):

> DNA-dependent RNA polymerase catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. Specific peripheric component of RNA polymerase III which synthesizes small RNAs, such as 5S rRNA and tRNAs.

**Summary**, from NCBI Gene [84265](https://www.ncbi.nlm.nih.gov/gene/84265):

> Predicted to enable chromatin binding activity. Involved in transcription by RNA polymerase III. Located in nucleus. Part of RNA polymerase III complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28466](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28466) · Entrez [84265](https://www.ncbi.nlm.nih.gov/gene/84265) · UniProt [Q9BT43](https://www.uniprot.org/uniprotkb/Q9BT43) · Ensembl [ENSG00000121851](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121851)

## Data

Gene col 4297: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4297); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4297, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4297]; `tensor/DDL_lfc|DDL_z.npy` [4297]; `embed/gene_vectors.npy` [4297]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4297 or target_col == 4297). Every well: [[POLR3GL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR3GL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
