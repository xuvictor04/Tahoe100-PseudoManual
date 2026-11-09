---
symbol: "FAM110C"
type: "gene"
col: 11571
ensembl_id: "ENSG00000184731"
name: "family with sequence similarity 110 member C"
location: "2p25.3"
module: 34
arm: "+"
pooled_cpm: 19.67
n_lines_expressing: 24
n_dd_up: 14
n_dd_down: 24
n_dd_up_clean: 11
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 25
direction_downstream: 39
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# FAM110C

*family with sequence similarity 110 member C* — 2p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.68× (z +6.8, q 7e-09, up in 14 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.615× (z -6.3, q 1e-07, down in 17 of 22 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.676× (z -5.1, q 4e-05, down in 14 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GJB3]] (+0.59, fdr 1e-05), [[CDCP1]] (+0.58, fdr 1e-05), [[FAM83B]] (+0.58, fdr 1e-05); moves opposite to [[B9D2]] (-0.51, fdr 3e-04), [[PRRT2]] (-0.49, fdr 5e-05), [[PAXBP1]] (-0.49, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 39 go from it, the strongest it → [[ITGA6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11571.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.68×** | +6.8 | 7e-09 | 14/22 (A-427, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.89×** | +6.4 | 5e-08 | 5/14 (AsPC-1, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.32×** | +5.2 | 5e-05 | 8/22 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +4.9 | 2e-04 | 7/22 (NCI-H1573, A-427, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.45×** | +4.5 | 6e-04 | 11/22 (A-427, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +4.1 | 0.003 | 2/16 (AsPC-1, Hs 766T) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bexarotene (drug)]] 0.05 µM |  | **1.35×** | +4.0 | 0.006 | 7/22 (KATO III, A-427, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.007 | 10/22 (SW480, KATO III, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.8 | 0.010 | 2/19 (NCI-H460, LoVo) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.030 | 7/22 (SW480, AsPC-1, …) | rises with dose |  |
| [[Bexarotene (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.033 | 5/22 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.034 | 2/22 (HCT15, A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.19× | +3.3 | 0.043 | 3/22 (Hs 766T, LS 180, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.046 | 9/22 (NCI-H1573, HEC-1-A, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.047 | 10/22 (NCI-H1573, CFPAC-1, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11571.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.615×** | -6.3 | 1e-07 | 17/22 (CFPAC-1, NCI-H1573, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.629×** | -5.8 | 2e-06 | 15/21 (A-427, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.675×** | -5.1 | 4e-05 | 14/22 (CFPAC-1, NCI-H1573, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.676×** | -5.1 | 4e-05 | 14/22 (LS 180, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.666×** | -5.1 | 4e-05 | 13/22 (NCI-H1573, NCI-H2030, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.680×** | -5.0 | 4e-05 | 12/22 (CFPAC-1, NCI-H2030, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.771×** | -4.8 | 1e-04 | 19/22 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.701×** | -4.6 | 2e-04 | 16/22 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.702×** | -4.3 | 0.001 | 6/22 (AsPC-1, NCI-H2030, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.707×** | -4.2 | 0.002 | 8/23 (AsPC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.794×** | -4.2 | 0.002 | 8/22 (NCI-H2030, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.782×** | -4.1 | 0.002 | 12/22 (AsPC-1, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **0.725×** | -4.0 | 0.002 | 16/22 (HepG2/C3A, CFPAC-1, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.736×** | -4.0 | 0.003 | 11/22 (CFPAC-1, NCI-H1573, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.741×** | -3.9 | 0.003 | 10/22 (NCI-H23, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.739×** | -3.7 | 0.007 | 8/22 (SW48, AsPC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.755×** | -3.5 | 0.013 | 9/22 (NCI-H1573, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.776×** | -3.3 | 0.025 | 9/22 (NCI-H2030, NCI-H1573, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.804×** | -3.3 | 0.026 | 10/22 (AsPC-1, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.845× | -3.1 | 0.048 | 9/22 (AsPC-1, NCI-H2030, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.796×** | -3.0 | 0.067 | 8/23 (NCI-H2030, NCI-H1573, …) | all doses, flat |  |
| [[Sildenafil (drug)]] 5 µM |  | **0.791×** | -2.9 | 0.071 | 1/22 (AsPC-1) | rises with dose | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11571. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 177 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0654× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 62.9 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -11.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.286× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 123 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.215× (z -9.4) |
| [[A-427 (line)]] | wt | 56.4 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 5.14× (z +10.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -10.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 65.1 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -19.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 41.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0659× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 52.3 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.102× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~51% of this change |
| [[HCT15 (line)]] | alt | 13.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.106× (z -8.5) |
| [[BT-474 (line)]] | alt | 34.6 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.106× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 35.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -11.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 18.4 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -9.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW480 (line)]] | alt | 13.0 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.297× (z -9.1) ⚠ cell-cycle shift, explains ~50% of this change |
| [[COLO 205 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0891× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[KATO III (line)]] | alt | 8.71 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -8.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 5.80 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.163× (z -8.5) |
| [[A-172 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.00 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.80 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11571), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GJB3]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[CDCP1]] | +0.58 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[FAM83B]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[PLEK2]] | +0.57 | +0.57 / +0.49 | both halves | 2e-05 |  |
| [[PTK6]] | +0.56 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[LAMC2]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SCEL]] | +0.55 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[SDR16C5]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[FERMT1]] | +0.55 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[PTK2B]] | +0.54 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[ANXA5]] | +0.54 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[LINC00659]] | +0.54 | +0.47 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B9D2]] | -0.51 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[PRRT2]] | -0.49 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[PAXBP1]] | -0.49 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[GTF2I]] | -0.42 | -0.38 / -0.27 | both halves | 3e-04 |  |
| [[SUMO2]] | -0.42 | -0.29 / -0.37 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 1, C 24. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises FAM110C's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[SH2D3A]] | C | SH2D3A activity raises FAM110C's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 5.90× lower at baseline in the lines without SH2D3A | 7e-04 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3; co-absent with the target |
| [[FAM83B]] | C | FAM83B activity raises FAM110C's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 4.65× lower at baseline in the lines without FAM83B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14; co-absent with the target |
| [[LAMA3]] | C | LAMA3 activity raises FAM110C's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 4.98× lower at baseline in the lines without LAMA3 | 0.002 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B; co-absent with the target |
| [[KIAA0040]] | C | KIAA0040 activity raises FAM110C's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 4.15× lower at baseline in the lines without KIAA0040 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1; co-absent with the target |
| [[C1orf116]] | C | C1orf116 activity raises FAM110C's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 4.92× lower at baseline in the lines without C1orf116 | 0.005 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[LINC00659]] | C | LINC00659 activity raises FAM110C's level | lines that do not express LINC00659 (26) vs lines expressing it (24) | 4.44× lower at baseline in the lines without LINC00659 | 0.005 | ⚠ within organs, on part of the lines; also absent: KLK6, TRIM15, ENSG00000225680; co-absent with the target |
| [[ARHGEF5]], [[ARHGEF34P]] | C | ARHGEF5, ARHGEF34P activity raises FAM110C's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 4.54× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent with the target; co-absent genes |
| [[B3GNT3]] | C | B3GNT3 activity raises FAM110C's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 4.43× lower at baseline in the lines without B3GNT3 | 0.008 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises FAM110C's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 4.13× lower at baseline in the lines without ATP2C2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[PRKG2-AS1]] | C | PRKG2-AS1 activity raises FAM110C's level | lines that do not express PRKG2-AS1 (23) vs lines expressing it (27) | 3.42× lower at baseline in the lines without PRKG2-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent; co-absent with the target |
| [[MST1R]] | C | MST1R activity raises FAM110C's level | lines that do not express MST1R (24) vs lines expressing it (26) | 4.62× lower at baseline in the lines without MST1R | 0.019 | ⚠ within organs, on part of the lines; also absent: SLC52A3, SPINT1, MAP7; co-absent with the target |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 12, C 27. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA6]] | B | FAM110C activity raises ITGA6's level | lines that do not express FAM110C (26) vs lines expressing it (24) | 3.45× lower at baseline in the lines without FAM110C | 6e-04 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |
| [[PTK2B]] | B | FAM110C activity raises PTK2B's level | lines that do not express FAM110C (26) vs lines expressing it (24) | 2.86× lower at baseline in the lines without FAM110C | 0.008 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |
| [[FHDC1]] | B | FAM110C activity raises FHDC1's level | lines that do not express FAM110C (26) vs lines expressing it (24) | 1.96× lower at baseline in the lines without FAM110C | 0.011 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |
| [[CSPP1]] | B | FAM110C activity lowers CSPP1's level | lines that do not express FAM110C (26) vs lines expressing it (24) | 1.35× higher at baseline in the lines without FAM110C | 0.021 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |
| [[EPHA2]] | B | FAM110C activity raises EPHA2's level | lines that do not express FAM110C (26) vs lines expressing it (24) | 3.35× lower at baseline in the lines without FAM110C | 0.027 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |
| [[RAPGEF3]] | B | FAM110C activity raises RAPGEF3's level | lines that do not express FAM110C (26) vs lines expressing it (24) | 1.70× lower at baseline in the lines without FAM110C | 0.028 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |
| [[SOWAHC]] | B | FAM110C activity raises SOWAHC's level | lines that do not express FAM110C (26) vs lines expressing it (24) | 1.60× lower at baseline in the lines without FAM110C | 0.039 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |
| [[TLDC2]] | B | FAM110C activity raises TLDC2's level | lines that do not express FAM110C (26) vs lines expressing it (24) | 2.02× lower at baseline in the lines without FAM110C | 0.051 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |
| [[SCAT1]] | B | FAM110C activity raises SCAT1's level | lines that do not express FAM110C (26) vs lines expressing it (24) | 1.97× lower at baseline in the lines without FAM110C | 0.064 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |
| cells under [[Sodium Salicylate (drug)]] 0.5 µM | B | FAM110C activity raises the cells' numbers under Sodium Salicylate 0.5 µM (protects the cells) | lines that do not express FAM110C (26) vs lines expressing it (22) | the lines without FAM110C: 0.86× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |
| [[GALE]] | B | FAM110C activity raises GALE's level | lines that do not express FAM110C (26) vs lines expressing it (24) | 1.58× lower at baseline in the lines without FAM110C | 0.082 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |
| [[TMC6]] | B | FAM110C activity raises TMC6's level | lines that do not express FAM110C (26) vs lines expressing it (24) | 3.27× lower at baseline in the lines without FAM110C | 0.089 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.536). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.2, 54.0); signed map (2.0, 37.5). **Vector** length 74.0, 20.5% of its response variance represented; |z| ≥ 3 in 682 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.4 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +4.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.6 | +3.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.1 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.6 | -5.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change | -2.5 | -2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -3.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.3 | -3.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.0 | -4.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.9 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 110 member C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.3 — chr2:38,814-46,870 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q1W6H9](https://www.uniprot.org/uniprotkb/Q1W6H9) (Protein FAM110C):

> May play a role in microtubule organization. May play a role in cell spreading and cell migration of epithelial cells; the function may involve the AKT1 signaling pathway.

**Summary**, from NCBI Gene [642273](https://www.ncbi.nlm.nih.gov/gene/642273):

> Enables alpha-tubulin binding activity. Involved in positive regulation of cell migration; positive regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction; and regulation of cell projection assembly. Located in cell cortex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33340](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33340) · Entrez [642273](https://www.ncbi.nlm.nih.gov/gene/642273) · UniProt [Q1W6H9](https://www.uniprot.org/uniprotkb/Q1W6H9) · Ensembl [ENSG00000184731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184731)

## Data

Gene col 11571: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11571); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11571, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11571]; `tensor/DDL_lfc|DDL_z.npy` [11571]; `embed/gene_vectors.npy` [11571]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11571 or target_col == 11571). Every well: [[FAM110C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM110C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
