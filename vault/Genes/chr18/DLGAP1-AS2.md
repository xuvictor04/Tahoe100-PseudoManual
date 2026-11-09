---
symbol: "DLGAP1-AS2"
type: "gene"
col: 15376
ensembl_id: "ENSG00000262001"
name: "DLGAP1 antisense RNA 2"
location: "18p11.31"
module: 35
arm: "+"
pooled_cpm: 20.08
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 21
n_dd_up_clean: 13
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# DLGAP1-AS2

*DLGAP1 antisense RNA 2* — 18p11.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.57× (z +10.2, q 1e-21, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.305× (z -19.1, q 0e+00, down in 43 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLGAP1-AS1]] (+0.75, fdr 7e-06, ⚠ same locus), [[PEBP4]] (+0.63, fdr 1e-05), [[LPXN]] (+0.62, fdr 4e-05), [[BHLHE40-AS1]] (+0.60, fdr 4e-05); moves opposite to [[PRKAR2A]] (-0.56, fdr 5e-05), [[TRAM2]] (-0.55, fdr 5e-05), [[NOMO3]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 035]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15376.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +10.2 | 1e-21 | 30/46 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +8.0 | 4e-13 | 31/45 (A-172, A-427, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +7.5 | 2e-11 | 19/44 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +7.0 | 4e-10 | 26/44 (MIA PaCa-2, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.50×** | +6.5 | 8e-09 | 21/45 (HT-29, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.33×** | +6.5 | 8e-09 | 21/46 (HS-578T, J82, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +5.9 | 4e-07 | 16/38 (NCI-H2030, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.3 | 7e-06 | 18/43 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +5.0 | 4e-05 | 11/45 (HOP62, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +4.9 | 5e-05 | 13/33 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +4.6 | 3e-04 | 16/45 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.20×** | +4.2 | 1e-03 | 18/46 (KATO III, HT-29, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 1e-03 | 16/44 (HOP62, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ferulic acid (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.001 | 13/45 (SW480, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.18× | +3.8 | 0.005 | 11/46 (MIA PaCa-2, SW1417, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.031 | 8/45 (HepG2/C3A, HT-29, …) | top dose only |  |
| [[Penfluridol (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.036 | 13/45 (A-172, HEC-1-A, …) | top dose only |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.052 | 10/46 (PANC-1, A-427, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15376.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.305×** | -19.1 | 0e+00 | 43/45 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.328×** | -17.9 | 0e+00 | 41/45 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.400×** | -14.7 | 0e+00 | 39/45 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.606×** | -8.0 | 1e-13 | 26/43 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.610×** | -7.9 | 3e-13 | 29/45 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.438×** | -6.9 | 4e-10 | 21/42 (SW480, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.657×** | -6.7 | 1e-09 | 24/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.676×** | -6.3 | 2e-08 | 21/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.475×** | -6.2 | 3e-08 | 22/41 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.912× | -5.3 | 6e-06 | 9/46 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.801×** | -5.0 | 3e-05 | 23/46 (SW480, PANC-1, …) | top dose only | composition shift |
| [[Dexamethasone (drug)]] 5 µM |  | **0.762×** | -4.4 | 6e-04 | 13/45 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.599×** | -4.3 | 7e-04 | 16/44 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.772×** | -4.1 | 0.001 | 17/45 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.778×** | -4.0 | 0.002 | 18/44 (SW480, SHP-77, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.811×** | -3.4 | 0.026 | 8/45 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.850× | -3.3 | 0.030 | 13/46 (NCI-H23, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **0.820×** | -3.2 | 0.044 | 8/45 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.822×** | -3.1 | 0.048 | 9/44 (NCI-H1573, H4, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.695×** | -3.1 | 0.061 | 14/39 (C-33 A, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.827×** | -3.0 | 0.061 | 6/45 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.825×** | -3.0 | 0.077 | 16/44 (SW 900, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15376. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 41.3 | 0 | 15 (11 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -22.0) |
| [[PANC-1 (line)]] | alt | 31.3 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -15.8) |
| [[HT-29 (line)]] | alt | 32.8 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -13.0) |
| [[LoVo (line)]] | wt | 19.8 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.108× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.232× (z -10.8) |
| [[HOP62 (line)]] | alt | 18.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +11.0) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.57× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 37.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -16.5) |
| [[A-427 (line)]] | wt | 79.4 | 1 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 2.28× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.315× (z -11.9) |
| [[C-33 A (line)]] | alt | 30.0 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0531× (z -16.0) |
| [[MIA PaCa-2 (line)]] | alt | 34.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.15× (z +11.1) | [[Adagrasib (drug)]] 0.05 µM 0.660× (z -9.9) ⚠ position not correctable |
| [[NCI-H23 (line)]] | alt | 81.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -18.4) |
| [[SK-MEL-2 (line)]] | alt | 36.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -13.4) |
| [[A-172 (line)]] | wt | 14.5 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +8.9) ⚠ cell-cycle shift, explains ~83% of this change | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 10.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -9.3) |
| [[LS 180 (line)]] | wt | 13.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 7.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.75× (z +8.8) | — |
| [[H4 (line)]] | wt | 17.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0703× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[Hs 766T (line)]] | wt | 14.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +9.6) ⚠ cell-cycle shift, explains ~83% of this change | — |
| [[J82 (line)]] | alt | 7.12 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.127× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 16.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.325× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 8.34 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -8.6) |
| [[SNU-1 (line)]] | wt | 11.3 | 0 | 1 | — | [[Rapamycin (drug)]] 0.5 µM 0.0594× (z -11.1) |
| [[SW1417 (line)]] | alt | 11.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.192× (z -9.7) |
| [[SW48 (line)]] | wt | 33.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0832× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A498 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15376), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLGAP1-AS1]] | +0.75 | +0.71 / +0.77 | both halves | 7e-06 | same gene group; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PEBP4]] | +0.63 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[LPXN]] | +0.62 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[BHLHE40-AS1]] | +0.60 | +0.53 / +0.42 | both halves | 4e-05 | same gene group |
| [[GSK3B-DT]] | +0.60 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[PPP1R12A-AS2]] | +0.59 | +0.45 / +0.47 | both halves | 3e-05 | same gene group |
| [[SMIM15-AS1]] | +0.59 | +0.53 / +0.32 | both halves | 2e-04 | same gene group |
| [[LINC01277]] | +0.59 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[ZCWPW1]] | +0.58 | +0.53 / +0.29 | both halves | 2e-04 |  |
| [[TSGA10]] | +0.58 | +0.45 / +0.35 | both halves | 1e-04 |  |
| [[EIF5]] | +0.58 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[DUSP28]] | +0.58 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[LURAP1L-AS1]] | +0.57 | +0.51 / +0.47 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKAR2A]] | -0.56 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[TRAM2]] | -0.55 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[NOMO3]] | -0.51 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[PPP1R12B]] | -0.51 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[EFNA3]] | -0.50 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[SUFU]] | -0.50 | -0.40 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (12.0, 9.5); signed map (21.1, -4.3). **Vector** length 107, 25.6% of its response variance represented; |z| ≥ 3 in 1,101 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.2 | +8.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +5.8 | +6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.7 | +6.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +5.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.7 | -17.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.5 | -19.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.9 | -14.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -6.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.8 | -7.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -2.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -2.1 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | DLGAP1 antisense RNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 18p11.31 — chr18:3,594,114-3,610,103 (+) |
| Ensembl biotype | lncRNA |
| Also known as | MGC11082 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [84777](https://www.ncbi.nlm.nih.gov/gene/84777):

> Biomarker of hepatocellular carcinoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28146](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28146) · Entrez [84777](https://www.ncbi.nlm.nih.gov/gene/84777) · Ensembl [ENSG00000262001](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000262001)

## Data

Gene col 15376: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15376); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15376, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15376]; `tensor/DDL_lfc|DDL_z.npy` [15376]; `embed/gene_vectors.npy` [15376]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15376 or target_col == 15376). Every well: [[DLGAP1-AS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLGAP1-AS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
