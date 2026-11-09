---
symbol: "PDGFRL"
type: "gene"
col: 2426
ensembl_id: "ENSG00000104213"
name: "platelet derived growth factor receptor like"
location: "8p22"
module: 70
arm: "+"
pooled_cpm: 7.68
n_lines_expressing: 34
n_dd_up: 19
n_dd_down: 28
n_dd_up_clean: 15
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# PDGFRL

*platelet derived growth factor receptor like* — 8p22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 2.05× (z +9.1, q 5e-17, up in 15 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.470× (z -9.6, q 4e-19, down in 21 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC7A2]] (+0.59, fdr 1e-05, ⚠ same locus), [[CFH]] (+0.58, fdr 3e-05), [[TNFAIP6]] (+0.55, fdr 1e-05), [[MEIS1]] (+0.55, fdr 3e-05); moves opposite to [[KLC1]] (-0.50, fdr 4e-05), [[FXYD5]] (-0.47, fdr 2e-05), [[CORO2B]] (-0.47, fdr 3e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PLPP3]] → it (grade B ⚠); 5 go from it, the strongest it → [[TIFA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2426.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.05×** | +9.1 | 5e-17 | 15/29 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +9.0 | 5e-17 | 13/30 (LoVo, SNU-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +6.1 | 2e-07 | 8/27 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.59×** | +5.6 | 2e-06 | 12/29 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.57×** | +5.6 | 2e-06 | 11/32 (SW 900, NCI-H2347, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.44×** | +5.4 | 8e-06 | 14/30 (NCI-H2347, SW 900, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.34×** | +5.0 | 4e-05 | 8/31 (NCI-H2347, NCI-H23, …) | all doses, flat | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +4.4 | 8e-04 | 1/12 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +4.4 | 8e-04 | 9/30 (SW 900, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.27×** | +4.2 | 0.001 | 10/30 (SW 900, NCI-H2030, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.002 | 12/29 (NCI-H2347, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.29×** | +3.8 | 0.006 | 10/32 (SW 900, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.006 | 11/26 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.024 | 8/29 (NCI-H2347, NCI-H1573, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.024 | 10/30 (BT-474, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.051 | 6/29 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.094 | 3/30 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2426.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.470×** | -9.6 | 4e-19 | 21/30 (SW 900, A498, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.520×** | -7.8 | 1e-12 | 18/28 (SW 900, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.579×** | -6.9 | 7e-10 | 20/29 (SW 900, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.587×** | -6.8 | 2e-09 | 19/29 (SW 900, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.602×** | -6.4 | 1e-08 | 19/30 (NCI-H23, SW 900, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.607×** | -6.3 | 2e-08 | 16/30 (AN3 CA, BT-474, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.632×** | -5.8 | 5e-07 | 12/30 (SW 900, BT-474, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.636×** | -5.8 | 6e-07 | 14/30 (NCI-H460, A498, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.641×** | -5.7 | 1e-06 | 14/29 (SHP-77, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.674×** | -5.0 | 3e-05 | 12/30 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.669×** | -4.9 | 5e-05 | 13/30 (CFPAC-1, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.763×** | -4.9 | 5e-05 | 15/28 (NCI-H23, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.690×** | -4.7 | 1e-04 | 12/30 (AN3 CA, NCI-H2347, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.701×** | -4.5 | 3e-04 | 15/30 (SHP-77, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.693×** | -4.5 | 3e-04 | 10/22 (A-172, A498, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.719×** | -4.2 | 8e-04 | 16/29 (SHP-77, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.722×** | -4.1 | 0.001 | 11/30 (A498, SNU-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.807×** | -3.9 | 0.003 | 8/29 (A549, SHP-77, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.816×** | -3.7 | 0.006 | 9/30 (SW 900, AN3 CA, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.837× | -3.2 | 0.032 | 10/31 (A498, NCI-H2030, …) | top dose only |  |
| [[vincristine (drug)]] 0.05 µM |  | **0.771×** | -3.1 | 0.042 | 8/30 (SNU-1, C-33 A, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2426. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 26.0 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.334× (z -10.6) |
| [[SHP-77 (line)]] | alt | 31.7 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0334× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.146× (z -14.5) |
| [[SW 900 (line)]] | alt | 19.6 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0942× (z -11.6) |
| [[AN3 CA (line)]] | alt | 87.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -14.2) |
| [[A-172 (line)]] | wt | 7.12 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.02× (z +11.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -9.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HS-578T (line)]] | alt | 20.8 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.92× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 8.15 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -12.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H2347 (line)]] | alt | 29.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -11.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.348× (z -11.1) |
| [[A549 (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0372× (z -10.1) ⚠ toxic |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -11.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HCT15 (line)]] | alt | 9.16 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -9.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H1573 (line)]] | alt | 4.81 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 8.82 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0843× (z -9.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.869 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.762 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.907 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.844 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.683 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.963 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.948 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.663 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.839 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2426), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC7A2]] | +0.59 | +0.59 / +0.55 | both halves | 1e-05 | ⚠ same locus (5.9 kb, same strand: neighbours can correlate without regulation) |
| [[CFH]] | +0.58 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[TNFAIP6]] | +0.55 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[MEIS1]] | +0.55 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[BTN3A1]] | +0.54 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[MTMR7]] | +0.54 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[EFNA1]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[GPRIN3]] | +0.52 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[BASP1]] | +0.51 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[SLITRK5]] | +0.51 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[P2RY6]] | +0.51 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[CEBPD]] | +0.51 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[SFTA3-1]] | +0.51 | +0.55 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLC1]] | -0.50 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[FXYD5]] | -0.47 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[CORO2B]] | -0.47 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[CAPN2]] | -0.45 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[KCTD13]] | -0.45 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[AXIN1]] | -0.45 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[NBPF15]] | -0.45 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[ARHGEF2]] | -0.44 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[KPNA4]] | -0.44 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[S100A16]] | -0.44 | -0.44 / -0.43 | both halves | 4e-05 |  |
| [[GATAD2A]] | -0.44 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[CEP170B]] | -0.44 | -0.37 / -0.44 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLPP3]] | B | PLPP3 activity raises PDGFRL's level | lines that do not express PLPP3 (5) vs lines expressing it (45) | 2.66× lower at baseline in the lines without PLPP3 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000284686; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers PDGFRL's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[MTUS1]] | B | MTUS1 activity raises PDGFRL's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 1.99× lower at baseline in the lines without MTUS1 | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[SLC7A2]] | C | SLC7A2 activity raises PDGFRL's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 3.13× lower at baseline in the lines without SLC7A2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TIFA]] | B | PDGFRL activity raises TIFA's level | lines that do not express PDGFRL (16) vs lines expressing it (34) | 1.31× lower at baseline in the lines without PDGFRL | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC16A7, ITPR1, TOX2 |
| [[BDH2]] | B | PDGFRL activity raises BDH2's level | lines that do not express PDGFRL (16) vs lines expressing it (34) | 1.48× lower at baseline in the lines without PDGFRL | 0.042 | ⚠ within organs, on part of the lines; also absent: SLC16A7, ITPR1, TOX2 |
| [[KLC1]] | B | PDGFRL activity raises KLC1's level | lines that do not express PDGFRL (16) vs lines expressing it (34) | 1.12× lower at baseline in the lines without PDGFRL | 0.084 | ⚠ within organs, on part of the lines; also absent: SLC16A7, ITPR1, TOX2 |
| [[SLC16A7]] | C | PDGFRL activity raises SLC16A7's level | lines that do not express PDGFRL (16) vs lines expressing it (34) | 3.41× lower at baseline in the lines without PDGFRL | 0.020 | ⚠ within organs, on part of the lines; also absent: SLC16A7, ITPR1, TOX2; co-absent with the target |
| [[SLC7A2]] | C | PDGFRL activity raises SLC7A2's level | lines that do not express PDGFRL (16) vs lines expressing it (34) | 4.02× lower at baseline in the lines without PDGFRL | 0.044 | ⚠ within organs, on part of the lines; also absent: SLC16A7, ITPR1, TOX2; co-absent with the target |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.425). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.2, 23.7); signed map (47.2, 25.3). **Vector** length 69.4, 14.6% of its response variance represented; |z| ≥ 3 in 789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.1 | +3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +5.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.8 | +5.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.4 | -9.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -5.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -2.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.3 | -6.3 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.3 | -6.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -6.8 |

## What is on record

|  |  |
|---|---|
| Name | platelet derived growth factor receptor like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p22 — chr8:17,576,433-17,644,071 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRLTS |
| Gene groups (HGNC) | I-set domain containing |
| Matched by | ensembl_id |

UniProt [Q15198](https://www.uniprot.org/uniprotkb/Q15198) carries no function annotation.

**Summary**, from NCBI Gene [5157](https://www.ncbi.nlm.nih.gov/gene/5157):

> This gene encodes a protein with significant sequence similarity to the ligand binding domain of platelet-derived growth factor receptor beta. Mutations in this gene, or deletion of a chromosomal segment containing this gene, are associated with sporadic hepatocellular carcinomas, colorectal cancers, and non-small cell lung cancers. This suggests this gene product may function as a tumor suppressor. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8805](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8805) · Entrez [5157](https://www.ncbi.nlm.nih.gov/gene/5157) · UniProt [Q15198](https://www.uniprot.org/uniprotkb/Q15198) · Ensembl [ENSG00000104213](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104213)

## Data

Gene col 2426: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2426); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2426, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2426]; `tensor/DDL_lfc|DDL_z.npy` [2426]; `embed/gene_vectors.npy` [2426]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2426 or target_col == 2426). Every well: [[PDGFRL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDGFRL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
