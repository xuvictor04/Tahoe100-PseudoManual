---
symbol: "JAKMIP3"
type: "gene"
col: 12010
ensembl_id: "ENSG00000188385"
name: "Janus kinase and microtubule interacting protein 3"
location: "10q26.3"
module: 117
arm: "+"
pooled_cpm: 6.95
n_lines_expressing: 39
n_dd_up: 25
n_dd_down: 24
n_dd_up_clean: 19
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# JAKMIP3

*Janus kinase and microtubule interacting protein 3* — 10q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.66× (z +12.4, q 1e-32, up in 4 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.87× (z +11.7, q 4e-29, up in 13 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.543× (z -8.1, q 3e-13, down in 19 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD11]] (+0.65, fdr 7e-06), [[ABCC2]] (+0.64, fdr 7e-06), [[ALOX12P2-1]] (+0.63, fdr 1e-05); moves opposite to [[TXNDC17]] (-0.55, fdr 1e-05), [[PIGF]] (-0.53, fdr 5e-05), [[B3GAT3]] (-0.52, fdr 4e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ABCC2]] → it (grade B ⚠); 4 go from it, the strongest it → [[PGD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12010.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.66×** | +12.4 | 1e-32 | 4/7 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.87×** | +11.7 | 4e-29 | 13/29 (NCI-H460, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +9.8 | 2e-20 | 7/20 (NCI-H1792, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.14×** | +9.5 | 5e-19 | 20/34 (HOP62, LS 180, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.87×** | +8.2 | 2e-14 | 19/35 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.68×** | +6.8 | 8e-10 | 20/35 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +5.6 | 2e-06 | 4/12 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.0 | 4e-05 | 8/31 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +4.7 | 2e-04 | 11/35 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +4.5 | 3e-04 | 8/33 (NCI-H1573, SW480, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 5e-04 | 11/30 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +4.4 | 5e-04 | 14/33 (SW480, NCI-H1573, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.54×** | +4.0 | 0.002 | 3/35 (HOP62, SNU-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.002 | 7/30 (BT-474, HT-29, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +4.0 | 0.003 | 5/35 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +4.0 | 0.003 | 8/33 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.010 | 12/35 (LS 180, CHP-212, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.011 | 7/33 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.32×** | +3.4 | 0.020 | 2/28 (NCI-H2030, Hs 766T) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12010.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.543×** | -8.1 | 3e-13 | 19/36 (COLO 205, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.658×** | -5.6 | 7e-06 | 18/27 (SNU-1, SW 900, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.696×** | -4.8 | 2e-04 | 13/35 (A-427, KATO III, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.689×** | -4.8 | 2e-04 | 11/35 (H4, NCI-H460, …) | all doses, flat | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.712×** | -4.5 | 7e-04 | 9/33 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.732×** | -4.2 | 0.003 | 8/35 (NCI-H460, SW480, …) | all doses, flat | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.732×** | -4.0 | 0.004 | 11/30 (HT-29, AN3 CA, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.810×** | -4.0 | 0.004 | 12/35 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.735×** | -4.0 | 0.005 | 8/35 (C-33 A, LS 180, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.743×** | -3.8 | 0.007 | 10/34 (MIA PaCa-2, C-33 A, …) | rises with dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.752×** | -3.8 | 0.007 | 5/35 (COLO 205, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.736×** | -3.8 | 0.007 | 3/35 (LoVo, SNU-1, …) | all doses, flat | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.769×** | -3.5 | 0.019 | 10/34 (NCI-H23, NCI-H460, …) | all doses, flat |  |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 0.834× | -3.4 | 0.023 | 9/35 (LoVo, H4, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.783×** | -3.3 | 0.040 | 6/35 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.641×** | -3.1 | 0.063 | 5/32 (LS 180, AN3 CA, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.723×** | -3.1 | 0.063 | 3/35 (SNU-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.786×** | -3.0 | 0.070 | 7/35 (CHP-212, HepG2/C3A, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.05 µM |  | **0.799×** | -3.0 | 0.076 | 4/35 (NCI-H23, AsPC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.662×** | -2.9 | 0.100 | 4/33 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM |  | **0.795×** | -2.8 | 0.100 | 3/35 (SW1417, NCI-H23, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12010. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 60.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 25.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +12.1) | — |
| [[A-172 (line)]] | wt | 6.43 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0739× (z -10.3) |
| [[A-427 (line)]] | wt | 7.16 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0775× (z -10.6) |
| [[HCT15 (line)]] | alt | 6.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.64× (z +10.0) | — |
| [[LoVo (line)]] | wt | 2.70 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0690× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 9.96 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -10.1) |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0751× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 9.40 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0844× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW480 (line)]] | alt | 13.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -9.0) |
| [[A498 (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.814 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.936 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12010), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD11]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ABCC2]] | +0.64 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[ALOX12P2-1]] | +0.63 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[CAPS2]] | +0.62 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[GNGT1]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[HTATIP2]] | +0.60 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[TRIM16L]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[LRP1B]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[FECH]] | +0.57 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ME1]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[EGF]] | +0.55 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[EWSR1]] | +0.55 | +0.51 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC17]] | -0.55 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[PIGF]] | -0.53 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[B3GAT3]] | -0.52 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[POLR2H]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[SP4]] | -0.50 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[MCRIP1]] | -0.48 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[RELL1]] | -0.47 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[SF3B5]] ⚠ | -0.47 | -0.34 / -0.43 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TAF5]] | -0.47 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[ARMC10]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.46 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[HERPUD2]] | -0.46 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[RASA1]] | -0.46 | -0.56 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCC2]] | B | ABCC2 activity raises JAKMIP3's level | lines that do not express ABCC2 (22) vs lines expressing it (28) | 1.71× lower at baseline in the lines without ABCC2 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, NR0B1, DNAJC12; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGD]] | B | JAKMIP3 activity raises PGD's level | lines that do not express JAKMIP3 (11) vs lines expressing it (39) | 1.88× lower at baseline in the lines without JAKMIP3 | 0.021 | ⚠ within organs, on part of the lines; also absent: RHOU, ABCG1, CASZ1; maybe low, not absent |
| [[TACC2]] | B | JAKMIP3 activity raises TACC2's level | lines that do not express JAKMIP3 (11) vs lines expressing it (39) | 2.12× lower at baseline in the lines without JAKMIP3 | 0.037 | ⚠ within organs, on part of the lines; also absent: RHOU, ABCG1, CASZ1; maybe low, not absent |
| [[RASA1]] | B | JAKMIP3 activity lowers RASA1's level | lines that do not express JAKMIP3 (11) vs lines expressing it (39) | 1.39× higher at baseline in the lines without JAKMIP3 | 0.041 | ⚠ within organs, on part of the lines; also absent: RHOU, ABCG1, CASZ1; maybe low, not absent |
| [[DNAJC7]] | B | JAKMIP3 activity lowers DNAJC7's level | lines that do not express JAKMIP3 (11) vs lines expressing it (39) | 1.13× higher at baseline in the lines without JAKMIP3 | 0.061 | ⚠ within organs, on part of the lines; also absent: RHOU, ABCG1, CASZ1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-6.9, 48.1); signed map (50.5, -8.8). **Vector** length 54.1, 8.34% of its response variance represented; |z| ≥ 3 in 841 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +9.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.5 | +8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +3.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.4 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -8.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -1.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -4.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -0.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | Janus kinase and microtubule interacting protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.3 — chr10:132,036,336-132,184,858 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37857, NECC2, KIAA4091, bA140A10.5; previously C10orf39, C10orf14 |
| Matched by | ensembl_id |

UniProt [Q5VZ66](https://www.uniprot.org/uniprotkb/Q5VZ66) carries no function annotation.

**Summary**, from NCBI Gene [282973](https://www.ncbi.nlm.nih.gov/gene/282973):

> Predicted to enable kinase binding activity and microtubule binding activity. Predicted to be located in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23523](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23523) · Entrez [282973](https://www.ncbi.nlm.nih.gov/gene/282973) · UniProt [Q5VZ66](https://www.uniprot.org/uniprotkb/Q5VZ66) · Ensembl [ENSG00000188385](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188385)

## Data

Gene col 12010: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12010); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12010, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12010]; `tensor/DDL_lfc|DDL_z.npy` [12010]; `embed/gene_vectors.npy` [12010]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12010 or target_col == 12010). Every well: [[JAKMIP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JAKMIP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
