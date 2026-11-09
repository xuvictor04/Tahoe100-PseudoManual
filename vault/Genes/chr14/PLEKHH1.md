---
symbol: "PLEKHH1"
type: "gene"
col: 614
ensembl_id: "ENSG00000054690"
name: "pleckstrin homology, MyTH4 and FERM domain containing H1"
location: "14q24.1"
module: 34
arm: "+"
pooled_cpm: 26.05
n_lines_expressing: 46
n_dd_up: 0
n_dd_down: 26
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PLEKHH1

*pleckstrin homology, MyTH4 and FERM domain containing H1* — 14q24.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.384× (z -16.5, q 0e+00, down in 39 of 43 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.440× (z -10.0, q 2e-21, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FERMT1]] (+0.56, fdr 1e-05), [[SLC25A15]] (+0.52, fdr 4e-05), [[RELT]] (+0.50, fdr 3e-05); moves opposite to [[ZBTB20]] (-0.55, fdr 4e-05), [[GABARAP]] (-0.54, fdr 3e-05, ⚠ GABARAP in the vector space only through flagged drug-doses), [[ID3]] (-0.53, fdr 3e-05), [[TNS3]] (-0.51, fdr 4e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → cells under [[Cobimetinib (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 614.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.28× | +3.0 | 0.98 | 16/43 (SW480, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 614.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.384×** | -16.5 | 0e+00 | 39/43 (A549, NCI-H23, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.393×** | -11.0 | 1e-25 | 38/43 (MIA PaCa-2, NCI-H1792, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.440×** | -10.0 | 2e-21 | 31/43 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.445×** | -9.9 | 5e-21 | 28/43 (NCI-H1792, A549, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.462×** | -9.4 | 4e-19 | 32/43 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.471×** | -9.2 | 3e-18 | 33/43 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.505×** | -8.4 | 5e-15 | 31/43 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.512×** | -8.2 | 2e-14 | 35/42 (NCI-H460, NCI-H1792, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.500×** | -8.1 | 2e-14 | 32/40 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.297×** | -7.8 | 5e-13 | 35/44 (NCI-H1792, CFPAC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.572×** | -6.8 | 5e-10 | 29/43 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.581×** | -6.6 | 1e-09 | 29/43 (NCI-H460, PANC-1, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.595×** | -6.4 | 9e-09 | 33/43 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.628×** | -5.7 | 5e-07 | 30/43 (NCI-H460, SNU-1, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.636×** | -5.5 | 1e-06 | 23/43 (NCI-H460, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.449×** | -5.1 | 1e-05 | 25/41 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.665×** | -3.6 | 0.010 | 19/41 (AsPC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.751×** | -3.3 | 0.024 | 17/43 (CFPAC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.777×** | -3.1 | 0.047 | 16/44 (C32, AsPC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.777×** | -3.0 | 0.065 | 16/43 (A549, BT-474, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.840× | -3.0 | 0.066 | 16/44 (NCI-H460, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 614. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 63.4 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0394× (z -23.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -12.2) |
| [[LS 180 (line)]] | wt | 83.7 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -16.3) |
| [[NCI-H460 (line)]] | wt | 21.3 | 0 | 10 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.349× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 38.9 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0586× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.219× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 52.5 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.260× (z -10.0) |
| [[LoVo (line)]] | wt | 71.8 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -15.7) |
| [[RKO (line)]] | wt | 39.7 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -11.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.275× (z -8.7) |
| [[KATO III (line)]] | alt | 30.5 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 37.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -18.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.278× (z -9.3) |
| [[SNU-1 (line)]] | wt | 37.0 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.145× (z -10.3) |
| [[SW48 (line)]] | wt | 48.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.237× (z -8.6) |
| [[A549 (line)]] | wt | 23.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0980× (z -22.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -9.2) |
| [[C-33 A (line)]] | alt | 48.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.152× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 34.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -14.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.310× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 44.8 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.143× (z -14.0) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 41.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.224× (z -10.8) |
| [[SNU-423 (line)]] | alt | 16.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -15.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[BT-474 (line)]] | alt | 27.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -11.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.258× (z -8.8) |
| [[J82 (line)]] | alt | 6.96 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.129× (z -9.3) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 36.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -14.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -11.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 52.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -9.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 17.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -8.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[AN3 CA (line)]] | alt | 51.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -9.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HCT15 (line)]] | alt | 37.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -9.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HepG2_C3A (line)]] | wt | 22.2 | 0 | 1 | — | [[Mifepristone (drug)]] 0.05 µM 0.159× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 1 | — | [[Sonidegib (drug)]] 0.5 µM 0.0645× (z -8.5) |
| [[A-172 (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.83 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.08 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 614), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FERMT1]] | +0.56 | +0.57 / +0.52 | both halves | 1e-05 | same gene group |
| [[SLC25A15]] | +0.52 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[RELT]] | +0.50 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[SMYD2]] | +0.50 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[DENR]] | +0.50 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[MALL]] | +0.48 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[POC1B]] | +0.48 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[TMEM181]] | +0.48 | +0.37 / +0.52 | both halves | 9e-05 |  |
| [[PYGL]] | +0.48 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[SRPK1]] | +0.47 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[POLR3G]] | +0.47 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[SLC25A19]] | +0.47 | +0.32 / +0.46 | both halves | 1e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB20]] | -0.55 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[GABARAP]] ⚠ | -0.54 | -0.44 / -0.50 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ID3]] | -0.53 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[TNS3]] | -0.51 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[IFT22]] | -0.49 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ING3]] | -0.48 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[BBS9]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[SELENOP]] | -0.47 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[XRN1]] | -0.46 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[NPHP1]] | -0.46 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[IQCK]] | -0.46 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[YY1]] | -0.45 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[WBP2NL]] | -0.45 | -0.42 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Cobimetinib (drug)]] 0.5 µM | C | PLEKHH1 activity raises the cells' numbers under Cobimetinib 0.5 µM (protects the cells) | lines that do not express PLEKHH1 (4) vs lines expressing it (44) | the lines without PLEKHH1: 0.74× the cells of the other lines | 0.069 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: BMP8B, E2F8, RIMKLA |
| cells under [[Sunitinib (drug)]] 5 µM | C | PLEKHH1 activity raises the cells' numbers under Sunitinib 5 µM (protects the cells) | lines that do not express PLEKHH1 (4) vs lines expressing it (44) | the lines without PLEKHH1: 0.70× the cells of the other lines | 0.076 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: BMP8B, E2F8, RIMKLA |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.415). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.5, -45.8); signed map (-23.4, 46.3). **Vector** length 92.2, 22.8% of its response variance represented; |z| ≥ 3 in 1,075 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.0 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | -0.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | +1.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.0 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.7 | +1.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +2.0 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.6 | -8.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.5 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.4 | -3.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.3 | -1.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -3.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology, MyTH4 and FERM domain containing H1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.1 — chr14:67,533,290-67,589,612 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1200 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; FERM domain containing |
| Matched by | ensembl_id |

UniProt [Q9ULM0](https://www.uniprot.org/uniprotkb/Q9ULM0) carries no function annotation.

**Summary**, from NCBI Gene [57475](https://www.ncbi.nlm.nih.gov/gene/57475):

> Predicted to be located in cytoskeleton. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17733](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17733) · Entrez [57475](https://www.ncbi.nlm.nih.gov/gene/57475) · UniProt [Q9ULM0](https://www.uniprot.org/uniprotkb/Q9ULM0) · Ensembl [ENSG00000054690](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000054690)

## Data

Gene col 614: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 614); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 614, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 614]; `tensor/DDL_lfc|DDL_z.npy` [614]; `embed/gene_vectors.npy` [614]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 614 or target_col == 614). Every well: [[PLEKHH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
