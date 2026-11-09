---
symbol: "MGME1"
type: "gene"
col: 4685
ensembl_id: "ENSG00000125871"
name: "mitochondrial genome maintenance exonuclease 1"
location: "20p11.23"
module: 91
arm: "+"
pooled_cpm: 31.66
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# MGME1

*mitochondrial genome maintenance exonuclease 1* — 20p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +9.8, q 5e-20, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.655× (z -6.8, q 5e-09, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF24]] (+0.71, fdr 7e-06), [[FAM111A]] (+0.66, fdr 1e-05), [[BRCA1]] (+0.66, fdr 7e-06); moves opposite to [[ST6GALNAC4]] (-0.62, fdr 4e-05), [[ST6GALNAC6]] (-0.61, fdr 5e-05), [[STX7]] (-0.59, fdr 3e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ZNF876P]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4685.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +9.8 | 5e-20 | 37/48 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +7.4 | 3e-11 | 32/48 (A549, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +7.4 | 3e-11 | 36/48 (SW480, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.49×** | +6.2 | 8e-08 | 32/47 (HT-29, KATO III, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.41×** | +5.3 | 1e-05 | 30/48 (RKO, H4, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.0 | 6e-05 | 24/48 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.37×** | +4.9 | 9e-05 | 24/47 (NCI-H460, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.7 | 2e-04 | 22/47 (RKO, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +4.6 | 2e-04 | 24/48 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.32×** | +4.4 | 5e-04 | 18/47 (A549, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.27×** | +3.8 | 0.007 | 19/48 (RKO, HEC-1-A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.008 | 20/48 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.26×** | +3.8 | 0.008 | 19/48 (NCI-H1573, HEC-1-A, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.27×** | +3.7 | 0.008 | 21/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.26×** | +3.7 | 0.008 | 19/47 (RPMI-7951, LoVo, …) | rises with dose | composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.012 | 14/48 (COLO 205, KATO III, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.055 | 13/48 (A549, A-172, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.056 | 15/48 (A549, KATO III, …) | two highest doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.14× | +3.0 | 0.072 | 12/48 (SW480, A549, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.20×** | +2.9 | 0.072 | 11/48 (LOX-IMVI, LoVo, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 1.14× | +2.9 | 0.081 | 10/48 (A498, SK-MEL-2, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +2.8 | 0.097 | 8/48 (RKO, SW480, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4685.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.655×** | -6.8 | 5e-09 | 36/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.758×** | -6.3 | 8e-08 | 29/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.690×** | -6.0 | 4e-07 | 25/48 (PANC-1, J82, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.693×** | -5.9 | 5e-07 | 25/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.697×** | -5.8 | 7e-07 | 32/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.695×** | -4.2 | 0.003 | 21/48 (SW480, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.784×** | -3.9 | 0.007 | 23/48 (LS 180, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.844× | -3.9 | 0.008 | 17/48 (RKO, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.782×** | -3.7 | 0.012 | 21/48 (KATO III, A498, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **0.799×** | -3.6 | 0.016 | 17/48 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.813×** | -3.2 | 0.067 | 20/47 (C-33 A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.689×** | -3.1 | 0.076 | 13/48 (A498, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.824×** | -3.1 | 0.076 | 9/48 (A498, J82, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.829× | -3.0 | 0.10 | 17/48 (COLO 205, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4685. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 55.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0834× (z -24.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.528× (z -9.1) |
| [[SW480 (line)]] | alt | 47.6 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.413× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 31.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 35.9 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0852× (z -10.0) ⚠ toxic |
| [[C-33 A (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.176× (z -10.8) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 57.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.423× (z -8.5) |
| [[HOP62 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.124× (z -8.5) ⚠ toxic |
| [[HS-578T (line)]] | alt | 23.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 34.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.0) | — |
| [[A-172 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4685), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF24]] | +0.71 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[FAM111A]] | +0.66 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[BRCA1]] | +0.66 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[BRCA2]] | +0.65 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[RMI1]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[RMI2]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[GEN1]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[ESCO2]] | +0.64 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ZNF724]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CENPP]] | +0.64 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[RBM15]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[MASTL]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC4]] | -0.62 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[ST6GALNAC6]] | -0.61 | -0.63 / -0.40 | both halves | 5e-05 |  |
| [[STX7]] | -0.59 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[USP35]] | -0.58 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[RIMS3]] | -0.56 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[WASF3]] | -0.54 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[ANKRD27]] | -0.54 | -0.53 / -0.29 | both halves | 2e-04 |  |
| [[HSPA5]] | -0.54 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[SGTB]] | -0.54 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[SH3PXD2B]] | -0.54 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[TPD52]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[CDA]] | -0.52 | -0.49 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF876P]] | B | ZNF876P activity raises MGME1's level | lines that do not express ZNF876P (17) vs lines expressing it (33) | 1.32× lower at baseline in the lines without ZNF876P | 0.015 | ⚠ within organs, on part of the lines; also absent: ZNF718, PAX8 |
| [[TOP2A]] | B | TOP2A activity lowers MGME1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP1]] | B | TOP1 activity lowers MGME1's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GPR19]] | B | GPR19 activity raises MGME1's level | lines that do not express GPR19 (6) vs lines expressing it (44) | 1.31× lower at baseline in the lines without GPR19 | 0.060 | ⚠ within organs, on part of the lines; also absent: DBNDD1, GPR137B, ERO1B; maybe low, not absent; its own permutation p |
| [[RIMS3]] | B | RIMS3 activity raises MGME1's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 1.30× lower at baseline in the lines without RIMS3 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.756). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-41.5, -47.5); signed map (-42.9, -48.1). **Vector** length 121, 32.8% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.60 to 5); *Resolution of D-loop Structures through Holliday Junction Intermediates* (reactome, mean cos +0.62 to 4); *Resolution of D-Loop Structures* (reactome, mean cos +0.62 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +7.0 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +5.6 | +4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +5.3 | +6.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +5.2 | +3.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.9 | +2.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.8 | +2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.7 | +1.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.1 | -6.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.5 | -6.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.3 | -5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.1 | -5.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.0 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -3.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.4 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial genome maintenance exonuclease 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.23 — chr20:17,969,018-17,991,122 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA504H3.4, DDK1; previously C20orf72 |
| Gene groups (HGNC) | Exonucleases |
| Reactome | 2 pathways, smallest: Strand-asynchronous mitochondrial DNA replication; DNA Replication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQP7](https://www.uniprot.org/uniprotkb/Q9BQP7) (Mitochondrial genome maintenance exonuclease 1):

> Metal-dependent single-stranded DNA (ssDNA) exonuclease involved in mitochondrial genome maintenance. Has preference for 5'-3' exonuclease activity but is also capable of endonuclease activity on linear substrates. Necessary for maintenance of proper 7S DNA levels. Probably involved in mitochondrial DNA (mtDNA) repair, possibly via the processing of displaced DNA containing Okazaki fragments during RNA-primed DNA synthesis on the lagging strand or via processing of DNA flaps during long-patch …

**Summary**, from NCBI Gene [92667](https://www.ncbi.nlm.nih.gov/gene/92667):

> The protein encoded by this gene is a nuclear-encoded mitochondrial protein necessary for the maintenance of mitochondrial genome synthesis. The encoded protein is a RecB-type exonuclease and primarily cleaves single-stranded DNA. Defects in this gene have been associated with mitochondrial DNA depletion syndrome-11. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2015]

**Accessions** — [HGNC:16205](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16205) · Entrez [92667](https://www.ncbi.nlm.nih.gov/gene/92667) · UniProt [Q9BQP7](https://www.uniprot.org/uniprotkb/Q9BQP7) · Ensembl [ENSG00000125871](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125871)

## Data

Gene col 4685: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4685); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4685, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4685]; `tensor/DDL_lfc|DDL_z.npy` [4685]; `embed/gene_vectors.npy` [4685]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4685 or target_col == 4685). Every well: [[MGME1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MGME1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
