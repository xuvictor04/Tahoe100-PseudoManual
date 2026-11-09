---
symbol: "INTS6L"
type: "gene"
col: 9111
ensembl_id: "ENSG00000165359"
name: "integrator complex subunit 6 like"
location: "Xq26.3"
module: 4
arm: "-"
pooled_cpm: 45.29
n_lines_expressing: 40
n_dd_up: 5
n_dd_down: 39
n_dd_up_clean: 4
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# INTS6L

*integrator complex subunit 6 like* — Xq26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +9.4, q 2e-18, up in 30 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.362× (z -15.1, q 0e+00, down in 34 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.615× (z -7.0, q 5e-10, down in 30 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2B]] (+0.67, fdr 7e-06), [[POLR2A]] (+0.66, fdr 7e-06), [[KLHL15]] (+0.64, fdr 1e-05); moves opposite to [[DIS3L2]] (-0.61, fdr 1e-05), [[TMEM33]] (-0.59, fdr 1e-05), [[CCDC91]] (-0.59, fdr 1e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SYNJ1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9111.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +9.4 | 2e-18 | 30/38 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +7.9 | 6e-13 | 23/38 (AsPC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +6.8 | 2e-09 | 28/38 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.4 | 1e-05 | 23/38 (NCI-H460, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.34×** | +4.3 | 0.002 | 17/38 (J82, NCI-H2347, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.37× | +3.2 | 0.15 | 13/38 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.24× | +3.1 | 0.16 | 13/38 (SK-MEL-2, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9111.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.362×** | -15.1 | 0e+00 | 34/38 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.368×** | -14.3 | 5e-44 | 26/31 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.380×** | -13.3 | 5e-38 | 26/35 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.615×** | -7.0 | 5e-10 | 30/38 (SNU-423, PANC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.638×** | -6.7 | 3e-09 | 27/38 (CFPAC-1, HOP62, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.641×** | -6.6 | 3e-09 | 25/37 (HCT15, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.684×** | -5.6 | 1e-06 | 23/38 (AsPC-1, RPMI-7951, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.692×** | -5.5 | 3e-06 | 26/38 (CFPAC-1, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.700×** | -5.3 | 7e-06 | 26/38 (Panc 03.27, AsPC-1, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.509×** | -5.3 | 8e-06 | 24/37 (RPMI-7951, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.612×** | -5.0 | 4e-05 | 25/38 (COLO 205, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.733×** | -4.6 | 2e-04 | 19/38 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.807×** | -4.5 | 3e-04 | 21/38 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.742×** | -4.4 | 4e-04 | 24/37 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.730×** | -4.4 | 4e-04 | 24/38 (SNU-423, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.739×** | -4.3 | 5e-04 | 20/37 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.588×** | -4.1 | 0.001 | 17/39 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.762×** | -4.0 | 0.002 | 18/38 (HCT15, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 5 µM |  | **0.608×** | -3.9 | 0.003 | 16/34 (H4, NCI-H460, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9111. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 59.5 | 2 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.320× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 40.7 | 4 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -12.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 71.2 | 2 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.345× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 81.9 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.0937× (z -22.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 94.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.371× (z -8.6) |
| [[HCT15 (line)]] | alt | 116 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.346× (z -10.8) |
| [[HOP62 (line)]] | alt | 84.0 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.142× (z -17.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 31.5 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.124× (z -15.0) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 48.8 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -15.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 79.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -16.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 35.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.38× (z +9.6) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -10.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 57.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Pralsetinib (drug)]] 5 µM 0.110× (z -8.9) |
| [[A498 (line)]] | wt | 70.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -13.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 74.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -15.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +8.8) | — |
| [[C32 (line)]] | wt | 25.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -11.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 48.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -12.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 19.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.209× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 49.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -8.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 39.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 60.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.317× (z -10.1) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 37.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -8.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -9.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 98.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0498× (z -25.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 66.2 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0919× (z -8.8) |
| [[SW1417 (line)]] | alt | 18.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.37× (z +12.6) | — |
| [[SW480 (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.321× (z -8.8) ⚠ transcription drop |
| [[A-427 (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.42 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.94 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.30 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.78 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 61.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.41 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9111), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2B]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[POLR2A]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[KLHL15]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[GAD1]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[PMS2P4-1]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[IRF3]] | +0.58 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[HLA-A]] | +0.57 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[TOB2]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[KATNA1]] | +0.56 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[CHCHD7]] | +0.56 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[SLC15A2]] | +0.56 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[SPAG4]] | +0.56 | +0.33 / +0.55 | both halves | 1e-04 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIS3L2]] | -0.61 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.59 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[CCDC91]] | -0.59 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[RBM45]] | -0.58 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[USP14]] | -0.58 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[KPNA1]] | -0.58 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[VPS50]] | -0.58 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[TALDO1]] | -0.57 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[COG2]] | -0.56 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[CHCHD6]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[SNX19]] | -0.56 | -0.58 / -0.57 | both halves | 9e-06 |  |
| [[NAA25]] | -0.55 | -0.64 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers INTS6L's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZFP69]] | B | ZFP69 activity raises INTS6L's level | lines that do not express ZFP69 (7) vs lines expressing it (43) | 4.14× lower at baseline in the lines without ZFP69 | 0.026 | ⚠ within organs, on part of the lines; also absent: FBXL2, ETV1, KIF3C; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYNJ1]] | B | INTS6L activity raises SYNJ1's level | lines that do not express INTS6L (10) vs lines expressing it (40) | 1.45× lower at baseline in the lines without INTS6L | 0.082 | ⚠ within organs, on part of the lines; also absent: LINC02454, FRMD6, CHST11 |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (3.0, -30.3); signed map (2.8, 15.2). **Vector** length 105, 28.0% of its response variance represented; |z| ≥ 3 in 957 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +9.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +5.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +6.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.8 | +3.2 |
|  | [[EX229 (drug)]] 0.05 µM |  | +2.2 | +2.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | +0.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +2.4 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -5.0 | -7.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.7 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.7 | -5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.6 | -13.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -6.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | integrator complex subunit 6 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.3 — chrX:135,520,659-135,582,510 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ41215; previously DDX26B |
| Gene groups (HGNC) | Integrator complex |
| Matched by | ensembl_id |

UniProt [Q5JSJ4](https://www.uniprot.org/uniprotkb/Q5JSJ4) carries no function annotation.

**Summary**, from NCBI Gene [203522](https://www.ncbi.nlm.nih.gov/gene/203522):

> Predicted to enable protein-macromolecule adaptor activity. Predicted to be involved in snRNA 3'-end processing. Located in centrosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27334](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27334) · Entrez [203522](https://www.ncbi.nlm.nih.gov/gene/203522) · UniProt [Q5JSJ4](https://www.uniprot.org/uniprotkb/Q5JSJ4) · Ensembl [ENSG00000165359](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165359)

## Data

Gene col 9111: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9111); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9111, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9111]; `tensor/DDL_lfc|DDL_z.npy` [9111]; `embed/gene_vectors.npy` [9111]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9111 or target_col == 9111). Every well: [[INTS6L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INTS6L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
