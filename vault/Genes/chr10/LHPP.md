---
symbol: "LHPP"
type: "gene"
col: 2897
ensembl_id: "ENSG00000107902"
name: "phospholysine phosphohistidine inorganic pyrophosphate phosphatase"
location: "10q26.13"
module: 80
arm: "+"
pooled_cpm: 14.56
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 37
n_dd_up_clean: 7
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# LHPP

*phospholysine phosphohistidine inorganic pyrophosphate phosphatase* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.44× (z +4.8, q 0.001, up in 10 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.05 µM: 1.21× (z +3.6, q 0.044, up in 14 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.294× (z -23.6, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAF7]] (+0.64, fdr 1e-05), [[DTWD2]] (+0.62, fdr 1e-05), [[SMARCD3]] (+0.61, fdr 3e-05); moves opposite to [[ZNF341-AS1]] (-0.58, fdr 3e-05), [[C14orf119]] (-0.58, fdr 1e-05), [[EIF3J-DT]] (-0.57, fdr 9e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[WWOX]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2897.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +4.8 | 0.001 | 10/21 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.044 | 14/48 (NCI-H1573, PANC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.044 | 13/45 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.044 | 13/48 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.050 | 20/48 (KATO III, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.072 | 10/47 (NCI-H23, HS-578T, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.078 | 17/47 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.18× | +3.3 | 0.078 | 7/48 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.086 | 14/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 1.17× | +3.0 | 0.14 | 5/48 (NCI-H460, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2897.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.294×** | -23.6 | 0e+00 | 46/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.303×** | -16.3 | 0e+00 | 43/47 (NCI-H23, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.350×** | -13.8 | 7e-41 | 43/47 (NCI-H23, SNU-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.382×** | -13.1 | 4e-37 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.400×** | -12.5 | 9e-34 | 40/45 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.440×** | -11.2 | 5e-27 | 35/48 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.453×** | -10.8 | 3e-25 | 42/47 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.584×** | -10.4 | 3e-23 | 36/47 (COLO 205, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.522×** | -8.9 | 5e-17 | 33/47 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.527×** | -8.4 | 3e-15 | 31/45 (NCI-H23, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.540×** | -8.1 | 4e-14 | 29/42 (A549, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.660×** | -8.0 | 7e-14 | 28/48 (SNU-1, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.568×** | -7.7 | 5e-13 | 27/47 (HT-29, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.734×** | -5.9 | 1e-07 | 32/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.649×** | -5.9 | 2e-07 | 26/47 (MIA PaCa-2, SNU-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.459×** | -5.5 | 1e-06 | 27/48 (A-427, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.666×** | -5.5 | 1e-06 | 23/47 (NCI-H2030, NCI-H23, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2897. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 20.7 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -24.7) |
| [[HT-29 (line)]] | alt | 18.1 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -19.9) |
| [[C32 (line)]] | wt | 18.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -15.7) |
| [[LS 180 (line)]] | wt | 21.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -16.5) |
| [[NCI-H23 (line)]] | alt | 29.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0780× (z -18.3) |
| [[Panc 03.27 (line)]] | alt | 13.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -13.2) |
| [[SNU-1 (line)]] | wt | 25.6 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0469× (z -13.9) |
| [[SW480 (line)]] | alt | 19.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -14.8) |
| [[A-427 (line)]] | wt | 24.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -14.7) |
| [[COLO 205 (line)]] | alt | 16.5 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0859× (z -16.8) |
| [[LoVo (line)]] | wt | 11.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -13.9) |
| [[MIA PaCa-2 (line)]] | alt | 17.4 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -13.8) |
| [[A549 (line)]] | wt | 10.2 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0693× (z -12.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0866× (z -11.6) |
| [[C-33 A (line)]] | alt | 28.0 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0960× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 18.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 8.03 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -15.3) |
| [[SW48 (line)]] | wt | 24.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -12.3) |
| [[A498 (line)]] | wt | 12.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -15.3) |
| [[H4 (line)]] | wt | 13.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0956× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.120× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0691× (z -10.9) |
| [[SNU-423 (line)]] | alt | 11.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 22.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -9.6) |
| [[HOP62 (line)]] | alt | 9.05 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -9.6) |
| [[Hs 766T (line)]] | wt | 7.05 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -9.3) |
| [[HS-578T (line)]] | alt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -10.5) |
| [[J82 (line)]] | alt | 12.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -15.8) |
| [[LOX-IMVI (line)]] | wt | 5.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0828× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 17.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0643× (z -24.0) |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -11.6) |
| [[SW1417 (line)]] | alt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -12.8) |
| [[A-172 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2897), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAF7]] | +0.64 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[DTWD2]] | +0.62 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[SMARCD3]] | +0.61 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[LSM12]] | +0.61 | +0.69 / +0.46 | both halves | 2e-05 |  |
| [[COPG2]] | +0.60 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[ABCA2]] | +0.59 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[SPATA6]] | +0.58 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[NDRG3]] | +0.58 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[POLD2]] | +0.57 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[CEP131]] | +0.57 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[LRRC28]] | +0.56 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[TBCD]] | +0.56 | +0.42 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF341-AS1]] | -0.58 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[C14orf119]] | -0.58 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[EIF3J-DT]] | -0.57 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[PDCD7]] | -0.56 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[IRX5]] | -0.55 | -0.52 / -0.37 | both halves | 7e-05 |  |
| [[BCL10-AS1]] | -0.55 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[PBDC1]] | -0.53 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[ZSWIM3]] | -0.53 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[LINC01829]] | -0.53 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[RRP8]] | -0.53 | -0.52 / -0.18 | ⚠ one half (not replicated) | 0.001 |  |
| [[MSX1]] | -0.53 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[REST]] | -0.53 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[ZNF585A]] | -0.53 | -0.46 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WWOX]] | B | WWOX activity raises LHPP's level | lines that do not express WWOX (5) vs lines expressing it (45) | 2.15× lower at baseline in the lines without WWOX | 0.012 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers LHPP's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds |
| [[MSX1]] | B | MSX1 activity raises LHPP's level | lines that do not express MSX1 (6) vs lines expressing it (44) | 1.84× lower at baseline in the lines without MSX1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ANAPC1P4, WDR35, TMCC2; maybe low, not absent |
| [[WWOX]] | B | WWOX activity strengthens LHPP's drug response | lines that do not express WWOX (5) vs lines expressing it (43) | the lines without WWOX respond 0.58× as strongly (z diff +2.38); strongest at Homoharringtonine 0.5 µM: 0.47x vs 0.26x (z diff +3.9) | 0.055 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises LHPP's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF563]] | B | ZNF563 activity raises LHPP's level | lines that do not express ZNF563 (9) vs lines expressing it (41) | 1.42× lower at baseline in the lines without ZNF563 | 0.062 | ⚠ within organs, on part of the lines; also absent: ZNF442, ZNF433, ENSG00000269755 |
| [[MAP2K2]] | B | MAP2K2 activity lowers LHPP's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction -0.537). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-27.8, -15.2); signed map (-43.0, -23.2). **Vector** length 71.1, 14.3% of its response variance represented; |z| ≥ 3 in 1,275 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.8 | +1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +4.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.2 | +3.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.2 | +3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.2 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.1 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.0 | -8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -16.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -8.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -5.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -5.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | phospholysine phosphohistidine inorganic pyrophosphate phosphatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:124,461,823-124,617,888 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HDHD2B |
| Gene groups (HGNC) | HAD Asp-based non-protein phosphatases; Haloacid dehalogenase like hydrolase domain containing |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 1 pathways, smallest: Pyrophosphate hydrolysis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H008](https://www.uniprot.org/uniprotkb/Q9H008) (Phospholysine phosphohistidine inorganic pyrophosphate phosphatase):

> Phosphatase that hydrolyzes imidodiphosphate, 3-phosphohistidine and 6-phospholysine. Has broad substrate specificity and can also hydrolyze inorganic diphosphate, but with lower efficiency (By similarity).

**Summary**, from NCBI Gene [64077](https://www.ncbi.nlm.nih.gov/gene/64077):

> Enables inorganic diphosphate phosphatase activity and protein homodimerization activity. Involved in phosphate-containing compound metabolic process. Located in cytosol and nuclear speck. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30042](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30042) · Entrez [64077](https://www.ncbi.nlm.nih.gov/gene/64077) · UniProt [Q9H008](https://www.uniprot.org/uniprotkb/Q9H008) · Ensembl [ENSG00000107902](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107902)

## Data

Gene col 2897: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2897); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2897, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2897]; `tensor/DDL_lfc|DDL_z.npy` [2897]; `embed/gene_vectors.npy` [2897]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2897 or target_col == 2897). Every well: [[LHPP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LHPP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
