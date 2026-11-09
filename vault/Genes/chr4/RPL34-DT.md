---
symbol: "RPL34-DT"
type: "gene"
col: 13963
ensembl_id: "ENSG00000234492"
name: "RPL34 divergent transcript"
location: "4q25"
module: 37
arm: "+"
pooled_cpm: 5.81
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 27
n_dd_up_clean: 17
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# RPL34-DT

*RPL34 divergent transcript* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 4.04× (z +14.3, q 2e-43, up in 39 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.214× (z -15.8, q 0e+00, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00159]] (+0.65, fdr 1e-05), [[ISY1]] (+0.63, fdr 4e-05), [[ADAM20]] (+0.62, fdr 1e-05); moves opposite to [[EXOC6]] (-0.56, fdr 7e-05), [[CEP83]] (-0.54, fdr 9e-05), [[TAF1B]] (-0.51, fdr 6e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LINC02641]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13963.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **4.04×** | +14.3 | 2e-43 | 39/42 (SK-MEL-2, SHP-77, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +12.2 | 5e-32 | 32/39 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.58×** | +6.6 | 1e-08 | 17/46 (NCI-H23, A498, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +6.0 | 4e-07 | 16/45 (HEC-1-A, C-33 A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +5.9 | 5e-07 | 21/37 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.75×** | +5.7 | 1e-06 | 20/45 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.72×** | +5.1 | 2e-05 | 18/42 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +5.0 | 3e-05 | 16/46 (BT-474, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.40×** | +4.8 | 1e-04 | 18/44 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.57×** | +4.6 | 3e-04 | 11/43 (C32, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.54×** | +4.3 | 0.001 | 10/45 (NCI-H1573, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +4.1 | 0.002 | 1/7 (C32) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.016 | 9/45 (C32, SW480, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.021 | 8/46 (KATO III, H4, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.44×** | +3.4 | 0.022 | 7/45 (C32, NCI-H23, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.041 | 13/45 (NCI-H23, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.041 | 6/46 (NCI-H2347, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13963.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.214×** | -15.8 | 0e+00 | 40/46 (H4, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.431×** | -12.2 | 9e-32 | 33/40 (COLO 205, HS-578T, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.298×** | -11.9 | 2e-30 | 36/45 (HS-578T, COLO 205, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.320×** | -11.7 | 2e-29 | 31/38 (COLO 205, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.347×** | -10.1 | 9e-22 | 29/43 (C32, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.363×** | -9.6 | 6e-20 | 30/42 (HOP62, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.400×** | -9.4 | 5e-19 | 29/45 (H4, HS-578T, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.487×** | -7.4 | 1e-11 | 26/39 (A498, HS-578T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.485×** | -7.1 | 6e-11 | 23/35 (HS-578T, COLO 205, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.508×** | -7.0 | 2e-10 | 25/46 (LoVo, HS-578T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.520×** | -6.7 | 1e-09 | 22/44 (RPMI-7951, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.570×** | -5.8 | 4e-07 | 14/45 (H4, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.581×** | -5.4 | 4e-06 | 18/42 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.585×** | -5.1 | 1e-05 | 19/43 (RPMI-7951, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.556×** | -5.0 | 3e-05 | 17/46 (H4, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.458×** | -4.2 | 1e-03 | 17/42 (KATO III, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.685×** | -3.9 | 0.003 | 16/45 (SNU-1, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.697×** | -3.7 | 0.006 | 14/43 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.787×** | -3.5 | 0.013 | 10/45 (C32, CFPAC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.530×** | -3.4 | 0.017 | 10/39 (H4, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.723×** | -3.3 | 0.021 | 11/44 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.724×** | -3.3 | 0.021 | 12/39 (LS 180, Panc 03.27, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.558×** | -3.1 | 0.039 | 9/38 (SK-MEL-2, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13963. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 20.7 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0659× (z -19.3) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -10.8) |
| [[COLO 205 (line)]] | alt | 28.8 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0555× (z -19.8) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0725× (z -11.8) |
| [[C32 (line)]] | wt | 12.7 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0189× (z -15.7) |
| [[H4 (line)]] | wt | 18.4 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0322× (z -12.7) |
| [[RPMI-7951 (line)]] | alt | 26.3 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -12.9) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A498 (line)]] | wt | 7.27 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0483× (z -12.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[hTERT-HPNE (line)]] | wt | 8.53 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -9.7) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0415× (z -9.5) |
| [[LS 180 (line)]] | wt | 5.21 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0832× (z -12.1) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0768× (z -8.8) |
| [[HOP62 (line)]] | alt | 4.94 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0363× (z -12.6) |
| [[HT-29 (line)]] | alt | 3.00 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0589× (z -11.1) ⚠ cell-cycle shift, explains ~49% of this change |
| [[LoVo (line)]] | wt | 4.72 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0854× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 2.81 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -8.7) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SHP-77 (line)]] | alt | 21.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.68× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 9.03 | 1 | 0 | [[Auranofin (drug)]] 5 µM 12.5× (z +10.2) | — |
| [[A-172 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.937 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13963), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00159]] | +0.65 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[ISY1]] | +0.63 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[ADAM20]] | +0.62 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[CAPN10-DT]] | +0.60 | +0.33 / +0.67 | both halves | 1e-04 | same gene group |
| [[EPM2AIP1]] | +0.59 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[CDC26]] | +0.59 | +0.38 / +0.63 | both halves | 7e-05 |  |
| [[MED6]] | +0.59 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[LINC02112]] | +0.59 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[ADAM20P1]] | +0.58 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[ZNF248]] | +0.58 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ZFC3H1]] | +0.57 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[NMRK1]] | +0.55 | +0.43 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC6]] | -0.56 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[CEP83]] | -0.54 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[TAF1B]] | -0.51 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[USP25]] | -0.49 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[SMC6]] | -0.48 | -0.26 / -0.50 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02641]] | B | LINC02641 activity raises RPL34-DT's level | lines that do not express LINC02641 (14) vs lines expressing it (36) | 1.55× lower at baseline in the lines without LINC02641 | 0.059 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent |
| [[LINC02885]] | B | LINC02885 activity raises RPL34-DT's level | lines that do not express LINC02885 (15) vs lines expressing it (35) | 1.68× lower at baseline in the lines without LINC02885 | 0.066 | ⚠ within organs, on part of the lines; also absent: LINC01399, PCDHB2, ENSG00000258168; maybe low, not absent |
| [[IQCJ]] | B | IQCJ activity raises RPL34-DT's level | lines that do not express IQCJ (6) vs lines expressing it (44) | 2.27× lower at baseline in the lines without IQCJ | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000222042, MR1, HECTD2; maybe low, not absent |
| [[DISC1]] | B | DISC1 activity raises RPL34-DT's level | lines that do not express DISC1 (5) vs lines expressing it (45) | 2.28× lower at baseline in the lines without DISC1 | 0.095 | ⚠ within organs, on part of the lines; also absent: DCP1B, LINC01341, ENSG00000237356; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers RPL34-DT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[LINC00159]] | C | LINC00159 activity raises RPL34-DT's level | lines that do not express LINC00159 (4) vs lines expressing it (46) | 2.52× lower at baseline in the lines without LINC00159 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF391, LINC01341, HHAT; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.530). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.9, 26.6); signed map (7.3, 4.5). **Vector** length 72.6, 13.5% of its response variance represented; |z| ≥ 3 in 1,131 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.2 | +14.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +12.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +6.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | -2.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | +5.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.9 | -3.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.8 | -11.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -2.4 | -12.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -5.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.3 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | RPL34 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q25 — chr4:108,538,190-108,620,475 (-) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ37673, RP11-462C24.1; previously RPL34-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26749](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26749) · Entrez [285456](https://www.ncbi.nlm.nih.gov/gene/285456) · Ensembl [ENSG00000234492](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234492)

## Data

Gene col 13963: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13963); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13963, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13963]; `tensor/DDL_lfc|DDL_z.npy` [13963]; `embed/gene_vectors.npy` [13963]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13963 or target_col == 13963). Every well: [[RPL34-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL34-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
