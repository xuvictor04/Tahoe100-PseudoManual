---
symbol: "VAPB"
type: "gene"
col: 4489
ensembl_id: "ENSG00000124164"
name: "VAMP associated protein B and C"
location: "20q13.32"
module: 164
arm: "+"
pooled_cpm: 112.92
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# VAPB

*VAMP associated protein B and C* — 20q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.99× (z +13.5, q 2e-38, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.657× (z -22.1, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLX9]] (+0.58, fdr 1e-05), [[TRMU]] (+0.56, fdr 3e-05), [[XPNPEP1]] (+0.51, fdr 2e-04); moves opposite to [[PEAK1]] (-0.47, fdr 5e-05), [[SERINC5]] (-0.47, fdr 5e-05), [[ETNK1]] (-0.46, fdr 1e-04).
> It is in [[Module 164]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4489.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.99×** | +13.5 | 2e-38 | 36/49 (LoVo, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.20×** | +7.0 | 1e-09 | 23/48 (A-172, A498, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.42×** | +6.8 | 2e-09 | 25/48 (LS 180, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.15× | +5.3 | 2e-05 | 13/48 (HCT15, Hs 766T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.14× | +4.8 | 2e-04 | 10/48 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Roxadustat (drug)]] 5 µM |  | 1.13× | +4.4 | 1e-03 | 15/48 (SHP-77, BT-474, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.08× | +4.2 | 0.002 | 3/49 (HCT15, CHP-212, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.11× | +3.8 | 0.009 | 4/48 (SHP-77, HepG2/C3A, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.011 | 16/48 (SHP-77, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[OTS514 (drug)]] 5 µM |  | 1.19× | +3.3 | 0.048 | 10/46 (SW480, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 1.10× | +3.3 | 0.057 | 4/47 (J82, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 5 µM |  | 1.17× | +3.1 | 0.082 | 11/46 (CFPAC-1, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.09× | +3.1 | 0.092 | 14/48 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | 1.12× | +3.0 | 0.093 | 8/48 (NCI-H2030, LoVo, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.09× | +3.0 | 0.093 | 5/47 (NCI-H2030, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.08× | +3.0 | 0.098 | 7/48 (A498, LS 180, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 17 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4489.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -22.1 | 0e+00 | 44/49 (BT-474, C32, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.699×** | -18.8 | 0e+00 | 31/48 (A-172, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.737×** | -10.9 | 2e-25 | 30/48 (NCI-H1573, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.787×** | -8.6 | 1e-15 | 28/47 (SK-MEL-2, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.801×** | -8.2 | 2e-14 | 29/48 (SK-MEL-2, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.804×** | -8.1 | 4e-14 | 28/48 (BT-474, J82, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.806×** | -8.0 | 8e-14 | 28/48 (HEC-1-A, J82, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.844× | -6.1 | 1e-07 | 23/48 (SNU-423, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.852× | -6.0 | 2e-07 | 19/48 (HEC-1-A, J82, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.900× | -5.5 | 2e-06 | 11/48 (BT-474, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.865× | -5.4 | 4e-06 | 15/48 (J82, CFPAC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.904× | -5.3 | 5e-06 | 10/48 (SK-MEL-2, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.871× | -5.1 | 1e-05 | 15/48 (SNU-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~14% of this change | **0.783×** | -4.8 | 8e-05 | 17/45 (J82, BT-474, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.885× | -4.5 | 2e-04 | 13/48 (SK-MEL-2, AN3 CA, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.892× | -4.2 | 7e-04 | 15/48 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 0.860× | -2.9 | 0.082 | 5/48 (C32, HT-29, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4489. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 464 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -17.9) |
| [[C32 (line)]] | wt | 119 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -18.6) |
| [[A-172 (line)]] | wt | 88.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -26.8) |
| [[HEC-1-A (line)]] | alt | 108 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 2.98× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.634× (z -10.5) |
| [[SNU-1 (line)]] | wt | 118 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -12.7) |
| [[SNU-423 (line)]] | alt | 127 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -23.0) |
| [[HOP62 (line)]] | alt | 123 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 108 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -16.3) |
| [[NCI-H1573 (line)]] | alt | 90.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -25.8) |
| [[SK-MEL-2 (line)]] | alt | 127 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -18.5) |
| [[NCI-H1792 (line)]] | alt | 112 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -16.0) |
| [[RKO (line)]] | wt | 104 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -26.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -10.5) |
| [[A498 (line)]] | wt | 86.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.74× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.663× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 95.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -19.1) |
| [[CFPAC-1 (line)]] | alt | 107 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.596× (z -12.6) |
| [[Hs 766T (line)]] | wt | 160 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -13.3) |
| [[hTERT-HPNE (line)]] | wt | 67.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -10.6) |
| [[LoVo (line)]] | wt | 75.0 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.23× (z +11.6) | — |
| [[NCI-H2030 (line)]] | alt | 162 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -13.9) |
| [[PANC-1 (line)]] | alt | 87.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -21.2) |
| [[SHP-77 (line)]] | alt | 171 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -17.1) |
| [[SW 1088 (line)]] | alt | 101 | 0 | 2 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.102× (z -10.0) ⚠ toxic · without an alert: [[Fumaric acid (drug)]] 0.05 µM 0.110× (z -9.0) |
| [[A-427 (line)]] | wt | 98.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -15.4) |
| [[A549 (line)]] | wt | 79.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -9.9) |
| [[COLO 205 (line)]] | alt | 97.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 98.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.655× (z -8.6) |
| [[J82 (line)]] | alt | 118 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.588× (z -12.4) |
| [[KATO III (line)]] | alt | 134 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.34× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 77.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.57× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 149 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.83× (z +10.8) | — |
| [[NCI-H2347 (line)]] | alt | 60.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.632× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 114 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -14.7) |
| [[NCI-H661 (line)]] | alt | 91.3 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.221× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 118 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.398× (z -9.9) |
| [[SW 900 (line)]] | alt | 84.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 146 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.56× (z +8.6) | — |
| [[SW480 (line)]] | alt | 124 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.24× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 135 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 79.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 130 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4489), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLX9]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[TRMU]] | +0.56 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[XPNPEP1]] | +0.51 | +0.61 / +0.32 | both halves | 2e-04 |  |
| [[SELENOO]] | +0.50 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[ZNF2]] | +0.50 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[DDX55]] | +0.50 | +0.51 / +0.37 | both halves | 9e-05 |  |
| [[NUDCD3]] | +0.49 | +0.53 / +0.40 | both halves | 4e-05 |  |
| [[ZNF544]] | +0.49 | +0.49 / +0.39 | both halves | 6e-05 |  |
| [[ZNF567]] | +0.48 | +0.39 / +0.44 | both halves | 6e-05 |  |
| [[ZNF470]] | +0.48 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[HDHD5]] | +0.48 | +0.53 / +0.40 | both halves | 4e-05 |  |
| [[FBXO45]] | +0.48 | +0.58 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEAK1]] | -0.47 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[SERINC5]] | -0.47 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[ETNK1]] | -0.46 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[CPNE8]] | -0.44 | -0.37 / -0.37 | both halves | 9e-05 | pathway: RHOD GTPase cycle |
| [[EPB41L5]] | -0.41 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[LYRM1]] | -0.40 | -0.49 / -0.24 | both halves | 5e-04 |  |
| [[DNAJC22]] | -0.39 | -0.49 / -0.20 | ⚠ not reproduced | 8e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.428). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-32.8, -11.0); signed map (-40.2, 21.0). **Vector** length 106, 25.9% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.2 | +13.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.6 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.1 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +4.7 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +4.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -22.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.8 | -8.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.9 | -10.9 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~2% of this change | -2.9 | -3.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -2.8 | -5.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -2.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.9 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -4.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | -1.3 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | VAMP associated protein B and C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.32 — chr20:58,389,229-58,451,101 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VAP-B, VAP-C, ALS8 |
| Gene groups (HGNC) | Motile sperm domain containing |
| Reactome | 11 pathways, smallest: Sphingolipid de novo biosynthesis; RHOD GTPase cycle; RHOC GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O95292](https://www.uniprot.org/uniprotkb/O95292) (Vesicle-associated membrane protein-associated protein B/C):

> Endoplasmic reticulum (ER)-anchored protein that mediates the formation of contact sites between the ER and endosomes via interaction with FFAT motif-containing proteins such as STARD3 or WDR44. Interacts with STARD3 in a FFAT motif phosphorylation dependent manner. Via interaction with WDR44 participates in neosynthesized protein export. Participates in the endoplasmic reticulum unfolded protein response (UPR) by inducing ERN1/IRE1 activity. Involved in cellular calcium homeostasis regulation.

**Summary**, from NCBI Gene [9217](https://www.ncbi.nlm.nih.gov/gene/9217):

> The protein encoded by this gene is a type IV membrane protein found in plasma and intracellular vesicle membranes. The encoded protein is found as a homodimer and as a heterodimer with VAPA. This protein also can interact with VAMP1 and VAMP2 and may be involved in vesicle trafficking. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12649](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12649) · Entrez [9217](https://www.ncbi.nlm.nih.gov/gene/9217) · UniProt [O95292](https://www.uniprot.org/uniprotkb/O95292) · Ensembl [ENSG00000124164](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124164)

## Data

Gene col 4489: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4489); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4489, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4489]; `tensor/DDL_lfc|DDL_z.npy` [4489]; `embed/gene_vectors.npy` [4489]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4489 or target_col == 4489). Every well: [[VAPB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VAPB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
