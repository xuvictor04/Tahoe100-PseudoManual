---
symbol: "IMPA2"
type: "gene"
col: 6512
ensembl_id: "ENSG00000141401"
name: "inositol monophosphatase 2"
location: "18p11.21"
module: 11
arm: "-"
pooled_cpm: 13.63
n_lines_expressing: 46
n_dd_up: 18
n_dd_down: 20
n_dd_up_clean: 15
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# IMPA2

*inositol monophosphatase 2* — 18p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.36× (z +16.3, q 0e+00, up in 34 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.357× (z -19.5, q 0e+00, down in 37 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAM15]] (+0.67, fdr 7e-06), [[GLB1L2]] (+0.57, fdr 1e-05), [[PCLAF]] (+0.57, fdr 1e-05); moves opposite to [[PDRG1]] (-0.62, fdr 1e-05), [[GSPT2]] (-0.60, fdr 1e-05), [[DCTN6]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 2 go from it, the strongest it → [[MFSD14B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6512.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +16.3 | 0e+00 | 34/41 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +11.3 | 2e-27 | 22/24 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.23×** | +10.8 | 1e-24 | 34/43 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +9.4 | 1e-18 | 21/33 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +9.3 | 2e-18 | 20/27 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +8.1 | 5e-14 | 31/43 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.83×** | +7.6 | 3e-12 | 29/42 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.5 | 5e-09 | 22/40 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +6.0 | 1e-07 | 23/41 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +5.8 | 4e-07 | 23/43 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.37×** | +4.9 | 5e-05 | 15/42 (SW 900, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +4.6 | 2e-04 | 13/39 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +3.9 | 0.005 | 9/42 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.005 | 11/43 (SW 900, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.005 | 10/41 (A498, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +3.4 | 0.023 | 14/43 (HOP62, J82, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.037 | 9/44 (A498, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.18× | +3.2 | 0.041 | 9/41 (NCI-H1573, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6512.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.357×** | -19.5 | 0e+00 | 37/38 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.311×** | -15.6 | 0e+00 | 38/39 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.307×** | -15.2 | 0e+00 | 35/41 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.368×** | -13.4 | 1e-38 | 36/43 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.392×** | -12.5 | 6e-34 | 32/41 (C-33 A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.495×** | -9.4 | 5e-19 | 28/42 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.360×** | -7.2 | 7e-11 | 24/41 (SW 900, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.575×** | -6.9 | 4e-10 | 25/42 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.584×** | -6.7 | 1e-09 | 23/41 (BT-474, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.411×** | -6.2 | 3e-08 | 22/38 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.628×** | -6.2 | 3e-08 | 21/43 (SK-MEL-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.766×** | -5.0 | 2e-05 | 22/42 (HT-29, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.696×** | -4.8 | 6e-05 | 20/42 (SW48, HT-29, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.695×** | -4.6 | 2e-04 | 14/41 (A-427, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.715×** | -4.5 | 3e-04 | 18/41 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.710×** | -4.2 | 8e-04 | 17/41 (LS 180, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6512. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 42.8 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0803× (z -31.6) |
| [[SW480 (line)]] | alt | 17.1 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -13.3) |
| [[HT-29 (line)]] | alt | 20.4 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -15.1) |
| [[LoVo (line)]] | wt | 25.1 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.106× (z -12.9) |
| [[LS 180 (line)]] | wt | 26.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 21.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -15.7) |
| [[NCI-H23 (line)]] | alt | 18.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0186× (z -23.9) |
| [[PANC-1 (line)]] | alt | 11.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -17.3) |
| [[C-33 A (line)]] | alt | 21.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -16.1) |
| [[NCI-H460 (line)]] | wt | 13.7 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0895× (z -10.8) |
| [[A549 (line)]] | wt | 12.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 8.87× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -13.3) |
| [[KATO III (line)]] | alt | 18.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -13.5) |
| [[MIA PaCa-2 (line)]] | alt | 19.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -17.2) |
| [[SW 900 (line)]] | alt | 30.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0735× (z -14.3) |
| [[A-172 (line)]] | wt | 5.09 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0338× (z -13.7) |
| [[A498 (line)]] | wt | 16.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.38× (z +9.0) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 21.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 32.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.169× (z -10.5) |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.103× (z -8.8) ⚠ cell-cycle shift, explains ~23% of this change |
| [[HEC-1-A (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.0) |
| [[HOP62 (line)]] | alt | 5.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 8.09 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0884× (z -13.2) |
| [[LOX-IMVI (line)]] | wt | 6.91 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0837× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 4.20 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -8.9) |
| [[SW1417 (line)]] | alt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +8.6) | — |
| [[SW48 (line)]] | wt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0640× (z -9.5) |
| [[AN3 CA (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6512), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM15]] | +0.67 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[GLB1L2]] | +0.57 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[PCLAF]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ZDHHC3]] | +0.57 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[MFSD14B]] | +0.56 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[TICRR]] | +0.55 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[GPC4]] | +0.55 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[ABHD12]] | +0.55 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[STT3B]] | +0.55 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[RAD54L]] | +0.55 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[RBBP7]] | +0.55 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[PASK]] | +0.54 | +0.47 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDRG1]] | -0.62 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[GSPT2]] | -0.60 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[DCTN6]] | -0.60 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[CWC22]] | -0.59 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[MED18]] | -0.58 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ARL14EP]] | -0.58 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[ZNF197]] | -0.57 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[ZNF271P]] | -0.56 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[NFU1]] | -0.56 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[THAP1]] | -0.55 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[SNRNP27]] | -0.55 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[NECAP2]] | -0.55 | -0.45 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers IMPA2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[SPINT2]] | B | SPINT2 activity raises IMPA2's level | lines that do not express SPINT2 (24) vs lines expressing it (26) | 1.86× lower at baseline in the lines without SPINT2 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, ENTPD2 |
| [[TOP2A]] | B | TOP2A activity lowers IMPA2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MFSD14B]] | C | IMPA2 activity raises MFSD14B's level | lines that do not express IMPA2 (4) vs lines expressing it (46) | 1.70× lower at baseline in the lines without IMPA2 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ATP11A, PLEKHG3; maybe low, not absent; its own permutation p |
| [[LPCAT3]] | C | IMPA2 activity raises LPCAT3's level | lines that do not express IMPA2 (4) vs lines expressing it (46) | 1.82× lower at baseline in the lines without IMPA2 | 0.077 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ATP11A, PLEKHG3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.556). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.9, 4.0); signed map (-30.3, -43.8). **Vector** length 80.0, 17.2% of its response variance represented; |z| ≥ 3 in 1,117 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +16.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +11.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.9 | +8.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.7 | -4.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +3.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.2 | +0.6 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.1 | +0.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.1 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -15.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -19.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.7 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -15.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -4.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -3.4 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | inositol monophosphatase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.21 — chr18:11,981,025-12,030,877 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phosphoinositide phosphatases |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 2 pathways, smallest: Synthesis of IP2, IP, and Ins in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O14732](https://www.uniprot.org/uniprotkb/O14732) (Inositol monophosphatase 2):

> Phosphatase that can use myo-inositol monophosphates, myo-inositol 1,4-diphosphate, scyllo-inositol-1,4-diphosphate, glucose-1-phosphate, beta-glycerophosphate and 2'-AMP as substrates in vitro. It is likely that IMPA2 has an as yet unidentified in vivo substrate(s). Has been implicated as the pharmacological target for lithium (Li(+)) action in brain.

**Summary**, from NCBI Gene [3613](https://www.ncbi.nlm.nih.gov/gene/3613):

> This locus encodes an inositol monophosphatase. The encoded protein catalyzes the dephosphoylration of inositol monophosphate and plays an important role in phosphatidylinositol signaling. This locus may be associated with susceptibility to bipolar disorder. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:6051](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6051) · Entrez [3613](https://www.ncbi.nlm.nih.gov/gene/3613) · UniProt [O14732](https://www.uniprot.org/uniprotkb/O14732) · Ensembl [ENSG00000141401](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141401)

## Data

Gene col 6512: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6512); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6512, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6512]; `tensor/DDL_lfc|DDL_z.npy` [6512]; `embed/gene_vectors.npy` [6512]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6512 or target_col == 6512). Every well: [[IMPA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IMPA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
