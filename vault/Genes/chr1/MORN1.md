---
symbol: "MORN1"
type: "gene"
col: 3768
ensembl_id: "ENSG00000116151"
name: "MORN repeat containing 1"
location: "1p36.32"
module: 15
arm: "+"
pooled_cpm: 12.64
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 23
n_dd_up_clean: 8
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# MORN1

*MORN repeat containing 1* — 1p36.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.59× (z +8.2, q 1e-13, up in 36 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.511× (z -8.4, q 3e-14, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RABL2B]] (+0.64, fdr 7e-06), [[RABL2A]] (+0.62, fdr 1e-05), [[PSKH1]] (+0.60, fdr 1e-05); moves opposite to [[SNRNP48]] (-0.58, fdr 4e-05), [[CCDC112]] (-0.57, fdr 8e-05), [[BLVRA]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[CCDC191]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3768.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +8.2 | 1e-13 | 36/46 (NCI-H1792, RKO, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +6.6 | 1e-08 | 27/44 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +6.1 | 1e-07 | 17/30 (BT-474, A498, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.54×** | +5.4 | 9e-06 | 24/48 (HepG2/C3A, PANC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.50×** | +5.1 | 5e-05 | 20/48 (AsPC-1, SW480, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.013 | 16/48 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.34×** | +3.6 | 0.024 | 13/47 (HepG2/C3A, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.32×** | +3.5 | 0.031 | 7/46 (NCI-H1792, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.32×** | +3.4 | 0.038 | 11/47 (BT-474, RKO, …) | rises with dose | position effect removed |
| [[Arbutin (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.043 | 7/47 (J82, NCI-H1573, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.043 | 10/46 (HCT15, SK-MEL-2, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.069 | 12/47 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.069 | 5/48 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +3.1 | 0.069 | 8/48 (NCI-H23, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3768.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.511×** | -8.4 | 3e-14 | 33/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.545×** | -7.6 | 1e-11 | 31/44 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.531×** | -7.5 | 1e-11 | 25/41 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.568×** | -7.1 | 2e-10 | 30/47 (J82, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.589×** | -6.6 | 4e-09 | 26/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.398×** | -6.0 | 2e-07 | 24/42 (MIA PaCa-2, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.621×** | -5.9 | 2e-07 | 20/46 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.737×** | -5.4 | 5e-06 | 27/48 (BT-474, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.651×** | -5.4 | 5e-06 | 24/47 (NCI-H23, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.446×** | -5.3 | 7e-06 | 22/47 (HepG2/C3A, J82, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.687×** | -4.7 | 1e-04 | 22/47 (LoVo, SHP-77, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.678×** | -4.6 | 2e-04 | 21/46 (Hs 766T, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.508×** | -4.4 | 4e-04 | 14/34 (NCI-H1573, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.722×** | -4.1 | 0.002 | 18/46 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.731×** | -3.9 | 0.003 | 17/48 (BT-474, LoVo, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.803×** | -3.9 | 0.004 | 20/48 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.746×** | -3.5 | 0.016 | 15/47 (NCI-H460, CFPAC-1, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.763×** | -3.4 | 0.022 | 18/44 (hTERT-HPNE, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3768. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 30.0 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0650× (z -17.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.276× (z -8.6) |
| [[SW480 (line)]] | alt | 16.8 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.190× (z -12.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -9.8) |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 2 | — | [[Vandetanib (drug)]] 0.5 µM 0.0827× (z -11.2) |
| [[COLO 205 (line)]] | alt | 19.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0721× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.112× (z -10.0) |
| [[J82 (line)]] | alt | 16.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.219× (z -9.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 12.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -9.3) |
| [[A-427 (line)]] | wt | 16.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -12.8) ⚠ cell-cycle shift, explains ~83% of this change |
| [[AsPC-1 (line)]] | alt | 4.72 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.05 µM 0.0628× (z -10.0) |
| [[C-33 A (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.160× (z -9.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 39.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -8.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -8.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 8.70 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0682× (z -16.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0867× (z -8.7) |
| [[SW 900 (line)]] | alt | 6.48 | 0 | 1 | — | [[Rosiglitazone (drug)]] 5 µM 0.0904× (z -8.6) |
| [[A-172 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3768), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABL2B]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[RABL2A]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[PSKH1]] | +0.60 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[LENG8-AS1]] | +0.56 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[PACRGL]] | +0.56 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[WDR90]] | +0.55 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[ACAD9]] | +0.55 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[SP2]] | +0.54 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[ALG8]] | +0.54 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[XNDC1N]] | +0.54 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[PSME3IP1]] | +0.54 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[IPO4]] | +0.52 | +0.44 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRNP48]] | -0.58 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[CCDC112]] | -0.57 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[BLVRA]] | -0.52 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[MGST3]] | -0.52 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[MAST1]] | -0.52 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[TENT4B]] | -0.50 | -0.28 / -0.41 | both halves | 3e-04 |  |
| [[SNX3]] | -0.50 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[FADS3]] | -0.48 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[UBR2]] | -0.47 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[SH3PXD2B]] | -0.47 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ABHD6]] | -0.47 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[PRKAG2]] | -0.47 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MORN1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC191]] | C | MORN1's natural level strengthens CCDC191's drug response | MORN1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.25; direction not clear | 0.042 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[OARD1]] | C | MORN1's natural level strengthens OARD1's drug response | MORN1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.23; direction not clear | 0.076 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.312). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-7.3, 17.7); signed map (28.1, -20.3). **Vector** length 67.4, 11.4% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.8 | -0.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.6 | +1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | +1.2 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.5 | -5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.7 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -6.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.7 | +0.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -2.9 | -4.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | MORN repeat containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.32 — chr1:2,321,253-2,391,707 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13941 |
| Gene groups (HGNC) | MORN repeat containing |
| Matched by | ensembl_id |

UniProt [Q5T089](https://www.uniprot.org/uniprotkb/Q5T089) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25852](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25852) · Entrez [79906](https://www.ncbi.nlm.nih.gov/gene/79906) · UniProt [Q5T089](https://www.uniprot.org/uniprotkb/Q5T089) · Ensembl [ENSG00000116151](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116151)

## Data

Gene col 3768: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3768); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3768, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3768]; `tensor/DDL_lfc|DDL_z.npy` [3768]; `embed/gene_vectors.npy` [3768]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3768 or target_col == 3768). Every well: [[MORN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MORN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
