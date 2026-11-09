---
symbol: "CCDC180"
type: "gene"
col: 12469
ensembl_id: "ENSG00000197816"
name: "coiled-coil domain containing 180"
location: "9q22.33"
module: 17
arm: "+"
pooled_cpm: 7.26
n_lines_expressing: 42
n_dd_up: 4
n_dd_down: 28
n_dd_up_clean: 4
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# CCDC180

*coiled-coil domain containing 180* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.42× (z +4.9, q 5e-04, up in 18 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.234× (z -14.3, q 2e-43, down in 36 of 39 measured lines).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUGT1P4-STRA6LP-CCDC180]] (+0.79, fdr 7e-06, ⚠ same locus), [[STRA6LP]] (+0.65, fdr 1e-05, ⚠ same locus), [[SUGT1P4-STRA6LP]] (+0.61, fdr 1e-05, ⚠ same locus), [[HNRNPDL]] (+0.57, fdr 3e-05), [[ZNF177]] (+0.53, fdr 3e-05), [[ODAD4]] (+0.51, fdr 8e-05); moves opposite to [[EMSY]] (-0.50, fdr 3e-05), [[DNASE1]] (-0.47, fdr 0.001, ⚠ one half only (not replicated)), [[BANP]] (-0.47, fdr 2e-04), [[GTPBP10]] (-0.47, fdr 2e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[SUGT1P4-STRA6LP]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12469.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +4.9 | 5e-04 | 18/40 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.2 | 0.008 | 5/40 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.042 | 14/39 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.042 | 8/38 (NCI-H1573, NCI-H23, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.46×** | +3.6 | 0.042 | 11/37 (NCI-H460, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.35× | +3.0 | 0.25 | 11/38 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12469.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.234×** | -14.3 | 2e-43 | 36/39 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.282×** | -12.5 | 3e-33 | 33/38 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.349×** | -10.4 | 7e-23 | 30/39 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.374×** | -9.7 | 6e-20 | 28/37 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.542×** | -8.5 | 2e-15 | 26/38 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.218×** | -7.8 | 5e-13 | 30/38 (HEC-1-A, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.455×** | -7.7 | 8e-13 | 27/38 (RPMI-7951, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.476×** | -7.3 | 2e-11 | 25/38 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.257×** | -7.0 | 2e-10 | 24/35 (BT-474, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.527×** | -6.3 | 2e-08 | 26/38 (RPMI-7951, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.527×** | -5.9 | 2e-07 | 20/39 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.575×** | -5.4 | 3e-06 | 21/36 (RPMI-7951, SNU-423, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.571×** | -5.1 | 2e-05 | 19/38 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.605×** | -4.6 | 1e-04 | 18/37 (HOP62, SW 1271, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.546×** | -4.6 | 1e-04 | 18/38 (NCI-H23, SNU-423, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.640×** | -4.4 | 4e-04 | 17/38 (A549, PANC-1, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.581×** | -4.2 | 0.001 | 18/37 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.741×** | -4.1 | 0.001 | 16/40 (A-172, Panc 03.27, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.645×** | -4.1 | 0.001 | 15/37 (SNU-423, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.766×** | -3.7 | 0.007 | 13/40 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12469. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 20.0 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0267× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.121× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 17.1 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0174× (z -17.9) |
| [[HOP62 (line)]] | alt | 13.4 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0857× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 7.31 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0506× (z -11.9) |
| [[A549 (line)]] | wt | 7.80 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -11.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0883× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 16.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0575× (z -15.7) |
| [[A498 (line)]] | wt | 8.68 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0547× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 3.29 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0328× (z -14.2) |
| [[PANC-1 (line)]] | alt | 7.99 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.148× (z -11.9) |
| [[A-172 (line)]] | wt | 11.8 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.269× (z -8.9) |
| [[C32 (line)]] | wt | 5.32 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0492× (z -9.7) |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -9.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 10.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0629× (z -8.6) |
| [[J82 (line)]] | alt | 5.52 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0505× (z -11.0) |
| [[LoVo (line)]] | wt | 4.72 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 3.84 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0843× (z -9.0) |
| [[SHP-77 (line)]] | alt | 7.64 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0844× (z -8.8) |
| [[SNU-1 (line)]] | wt | 30.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.151× (z -8.9) |
| [[SW 900 (line)]] | alt | 7.28 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0291× (z -12.3) |
| [[A-427 (line)]] | wt | 0.482 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.707 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.611 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.699 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12469), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 8 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUGT1P4-STRA6LP-CCDC180]] | +0.79 | +0.71 / +0.77 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[STRA6LP]] | +0.65 | +0.51 / +0.65 | both halves | 1e-05 | ⚠ same locus (11.5 kb, same strand: neighbours can correlate without regulation) |
| [[SUGT1P4-STRA6LP]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 | ⚠ same locus (10.0 kb, same strand: neighbours can correlate without regulation) |
| [[HNRNPDL]] | +0.57 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[ZNF177]] | +0.53 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[ODAD4]] | +0.51 | +0.56 / +0.37 | both halves | 8e-05 |  |
| [[ANKRD24]] | +0.48 | +0.37 / +0.41 | both halves | 7e-05 |  |
| [[MOCS1]] | +0.47 | +0.23 / +0.44 | both halves | 5e-04 |  |
| [[PTCH2]] | +0.46 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[SF1]] | +0.46 | +0.38 / +0.39 | both halves | 7e-05 |  |
| [[ACACB]] | +0.46 | +0.28 / +0.48 | both halves | 3e-04 |  |
| [[ZNF527]] | +0.46 | +0.33 / +0.43 | both halves | 1e-04 |  |
| [[HLTF]] | +0.45 | +0.30 / +0.41 | both halves | 2e-04 |  |
| [[LRRCC1]] | +0.45 | +0.33 / +0.33 | both halves | 1e-04 |  |
| [[EIF4A2]] | +0.44 | +0.42 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMSY]] | -0.50 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[DNASE1]] | -0.47 | -0.15 / -0.53 | ⚠ one half (not replicated) | 0.001 |  |
| [[BANP]] | -0.47 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[GTPBP10]] | -0.47 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[BMT2]] | -0.47 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[R3HCC1L]] | -0.47 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[TMEM11-DT]] | -0.46 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[NRSN2-AS1]] | -0.45 | -0.21 / -0.37 | both halves | 7e-04 |  |
| [[SAP30L-AS1]] | -0.44 | -0.26 / -0.29 | both halves | 4e-04 |  |
| [[CCNO-DT]] | -0.44 | -0.28 / -0.29 | both halves | 3e-04 |  |
| [[ATP6V1E1]] | -0.43 | -0.26 / -0.38 | both halves | 4e-04 |  |
| [[AK4]] | -0.43 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[VPS13B-DT]] | -0.43 | -0.24 / -0.31 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CCDC180's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CCDC180's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[NQO1]] | B | NQO1 activity lowers CCDC180's level | lines that do not express NQO1 (5) vs lines expressing it (45) | 2.46× higher at baseline in the lines without NQO1 | 0.078 | ⚠ within organs, on part of the lines |
| [[C13orf46]] | B | C13orf46 activity raises CCDC180's level | lines that do not express C13orf46 (11) vs lines expressing it (39) | 1.50× lower at baseline in the lines without C13orf46 | 0.088 | ⚠ within organs, on part of the lines; also absent: RASA3, COL27A1, PRR5L |
| [[STRA6LP]], [[SUGT1P4-STRA6LP]], [[SUGT1P4-STRA6LP-CCDC180]] | C | STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 activity raises CCDC180's level | lines that do not express STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 (9) vs lines expressing them (41) | 5.07× lower at baseline in the lines without STRA6LP, SUGT1P4-STRA6LP, SUGT1P4-STRA6LP-CCDC180 | 5e-04 | ⚠ within organs, on part of the lines; also absent: CCDC180; co-absent with the target; co-absent genes |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SUGT1P4-STRA6LP]] | C | CCDC180 activity raises SUGT1P4-STRA6LP's level | lines that do not express CCDC180 (8) vs lines expressing it (42) | 4.27× lower at baseline in the lines without CCDC180 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: STRA6LP; co-absent with the target |
| [[STRA6LP]] | C | CCDC180 activity raises STRA6LP's level | lines that do not express CCDC180 (8) vs lines expressing it (42) | 3.43× lower at baseline in the lines without CCDC180 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: STRA6LP; co-absent with the target |
| [[SUGT1P4-STRA6LP-CCDC180]] | C | CCDC180 activity raises SUGT1P4-STRA6LP-CCDC180's level | lines that do not express CCDC180 (8) vs lines expressing it (42) | 3.44× lower at baseline in the lines without CCDC180 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: STRA6LP; co-absent with the target |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.350). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-4.5, -4.2); signed map (-25.9, -14.5). **Vector** length 53.8, 8.18% of its response variance represented; |z| ≥ 3 in 1,036 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +1.8 | +3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.4 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.1 | +0.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.1 | +4.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +0.7 | +2.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +0.7 | +2.2 |
|  | [[Cinacalcet (drug)]] 5 µM |  | +0.6 | +1.5 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +0.6 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -4.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -7.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 180 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:97,307,304-97,378,751 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434I2420, BDAG1, FAP76, CFAP76; previously KIAA1529, C9orf174 |
| Gene groups (HGNC) | Cilia and flagella associated |
| Matched by | ensembl_id |

UniProt [Q9P1Z9](https://www.uniprot.org/uniprotkb/Q9P1Z9) carries no function annotation.

**Summary**, from NCBI Gene [100499483](https://www.ncbi.nlm.nih.gov/gene/100499483):

> The protein encoded by this gene contains a coiled-coil domain. Alternative splicing results in multiple transcript variants encoding different isoforms. A single nucleotide polymorphism (SNP) in this gene has been associated with increased susceptibility to Behcet's Disease (PMID: 19442274). [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:29303](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29303) · Entrez [100499483](https://www.ncbi.nlm.nih.gov/gene/100499483) · UniProt [Q9P1Z9](https://www.uniprot.org/uniprotkb/Q9P1Z9) · Ensembl [ENSG00000197816](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197816)

## Data

Gene col 12469: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12469); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12469, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12469]; `tensor/DDL_lfc|DDL_z.npy` [12469]; `embed/gene_vectors.npy` [12469]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12469 or target_col == 12469). Every well: [[CCDC180 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC180.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
