---
symbol: "EXO5-DT"
type: "gene"
col: 14180
ensembl_id: "ENSG00000238287"
name: "EXO5 divergent transcript"
location: "1p34.2"
module: 129
arm: "+"
pooled_cpm: 7.71
n_lines_expressing: 42
n_dd_up: 9
n_dd_down: 22
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/129"]
generated_by: "tahoemap"
---

# EXO5-DT

*EXO5 divergent transcript* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.65× (z +7.5, q 3e-11, up in 28 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.233× (z -15.4, q 0e+00, down in 35 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF112]] (+0.67, fdr 1e-05), [[ZNF790-AS1]] (+0.66, fdr 1e-05), [[ZNF559]] (+0.64, fdr 1e-05); moves opposite to [[RFX3]] (-0.55, fdr 4e-05), [[EIF4G2]] (-0.55, fdr 9e-05), [[GPAA1]] (-0.54, fdr 4e-05).
> It is in [[Module 129]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CERS4]] → it (grade B ⚠); 1 goes from it, the strongest it → [[DDX19B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14180.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +7.5 | 3e-11 | 28/38 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.95×** | +7.1 | 4e-10 | 25/38 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.83×** | +5.2 | 3e-05 | 20/39 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +5.0 | 9e-05 | 21/39 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.31×** | +4.0 | 0.006 | 16/38 (A498, RKO, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.006 | 16/39 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.035 | 13/39 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.079 | 10/39 (PANC-1, LoVo, …) | rises with dose |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.35×** | +3.2 | 0.079 | 4/39 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.34× | +3.1 | 0.11 | 8/39 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.33× | +3.0 | 0.12 | 7/38 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14180.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.233×** | -15.4 | 0e+00 | 35/39 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.342×** | -10.9 | 3e-25 | 31/38 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.375×** | -10.4 | 6e-23 | 29/37 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.430×** | -8.6 | 2e-15 | 21/30 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.397×** | -8.0 | 2e-13 | 29/39 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.237×** | -8.0 | 2e-13 | 29/38 (PANC-1, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.491×** | -7.5 | 5e-12 | 23/38 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.619×** | -7.2 | 6e-11 | 25/36 (SNU-423, A498, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.582×** | -5.7 | 7e-07 | 20/36 (A498, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.393×** | -5.2 | 1e-05 | 18/34 (Panc 03.27, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.604×** | -4.9 | 4e-05 | 10/18 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.597×** | -4.4 | 4e-04 | 16/37 (PANC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.659×** | -4.4 | 5e-04 | 15/39 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.752×** | -4.2 | 9e-04 | 16/38 (NCI-H2347, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **0.703×** | -3.7 | 0.008 | 16/29 (PANC-1, CFPAC-1, …) | inconsistent across doses | composition shift |
| [[Allopurinol (drug)]] 0.05 µM |  | **0.712×** | -3.6 | 0.012 | 8/39 (NCI-H1573, C32, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.716×** | -3.5 | 0.014 | 12/39 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.693×** | -3.2 | 0.048 | 13/38 (HS-578T, NCI-H661, …) | rises with dose | noisy plate (z scaled) |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.742×** | -3.1 | 0.048 | 11/39 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.729×** | -3.1 | 0.048 | 14/37 (J82, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artemether (drug)]] 0.05 µM |  | **0.746×** | -3.1 | 0.055 | 3/39 (PANC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Gefitinib (drug)]] 5 µM |  | **0.749×** | -3.0 | 0.059 | 8/39 (NCI-H460, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14180. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 18.7 | 0 | 8 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0943× (z -18.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.153× (z -15.4) |
| [[J82 (line)]] | alt | 11.0 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 4.65 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0459× (z -11.4) |
| [[A498 (line)]] | wt | 4.97 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0685× (z -11.6) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.132× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 11.3 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0974× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 16.3 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.122× (z -11.4) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 7.99 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0805× (z -15.2) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0806× (z -10.3) |
| [[SW480 (line)]] | alt | 9.04 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -11.7) |
| [[HOP62 (line)]] | alt | 7.42 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 8.60 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -8.9) ⚠ cell-cycle shift, explains ~64% of this change |
| [[SW 900 (line)]] | alt | 6.84 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.0618× (z -9.1) |
| [[BT-474 (line)]] | alt | 7.17 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -8.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0897× (z -9.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 6.17 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0600× (z -10.3) |
| [[LoVo (line)]] | wt | 4.55 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -8.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -10.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 6.80 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0381× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.120× (z -8.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.886 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.978 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.876 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14180), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF112]] | +0.67 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[ZNF790-AS1]] | +0.66 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[ZNF559]] | +0.64 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[ZNF212]] | +0.63 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[SNRNP35]] | +0.63 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[ZNF786]] | +0.61 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[TRIP4]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[TDG]] | +0.60 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | +0.59 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[MED9]] | +0.59 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ZNF322]] | +0.58 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[SNU13]] | +0.58 | +0.42 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFX3]] | -0.55 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[EIF4G2]] | -0.55 | -0.36 / -0.60 | both halves | 9e-05 |  |
| [[GPAA1]] | -0.54 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[CNOT1]] | -0.53 | -0.37 / -0.61 | both halves | 8e-05 |  |
| [[PTBP1]] | -0.53 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[FOSB]] | -0.53 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[ATP11C]] | -0.53 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[SLC12A2]] | -0.51 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[LNPEP]] | -0.51 | -0.28 / -0.58 | both halves | 3e-04 |  |
| [[WNK1]] | -0.50 | -0.24 / -0.57 | both halves | 5e-04 |  |
| [[CYB5D1]] | -0.50 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[MBNL3]] | -0.50 | -0.28 / -0.45 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CERS4]] | B | CERS4 activity raises EXO5-DT's level | lines that do not express CERS4 (17) vs lines expressing it (33) | 2.23× lower at baseline in the lines without CERS4 | 0.041 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, PCSK1N, CHST10 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers EXO5-DT's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers EXO5-DT's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDX19B]] | B | EXO5-DT activity raises DDX19B's level | lines that do not express EXO5-DT (8) vs lines expressing it (42) | 1.44× lower at baseline in the lines without EXO5-DT | 0.092 | ⚠ within organs, on part of the lines; also absent: EXO5, LARP6, ENSG00000290399 |

## Where it sits

- **Module**: [[Module 129]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.668). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-30.6, -4.4); signed map (-16.5, -17.0). **Vector** length 63.0, 11.9% of its response variance represented; |z| ≥ 3 in 785 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.5 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +7.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.6 | +2.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +2.4 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | -0.2 |
|  | [[Carbamazepine (drug)]] 0.5 µM |  | +1.5 | +2.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | +1.4 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | -3.2 | -3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.0 | -0.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -10.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.8 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.4 | -0.9 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.4 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | EXO5 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p34.2 — chr1:40,493,157-40,508,661 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55647](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55647) · Entrez [105378672](https://www.ncbi.nlm.nih.gov/gene/105378672) · Ensembl [ENSG00000238287](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000238287)

## Data

Gene col 14180: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14180); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14180, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14180]; `tensor/DDL_lfc|DDL_z.npy` [14180]; `embed/gene_vectors.npy` [14180]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14180 or target_col == 14180). Every well: [[EXO5-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXO5-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
