---
symbol: "TSC22D3"
type: "gene"
col: 8079
ensembl_id: "ENSG00000157514"
name: "TSC22 domain family member 3"
location: "Xq22.3"
module: 106
arm: "+"
pooled_cpm: 21.93
n_lines_expressing: 39
n_dd_up: 51
n_dd_down: 36
n_dd_up_clean: 50
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 13
direction_downstream: 14
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# TSC22D3

*TSC22 domain family member 3* — Xq22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 51 drug-doses (1 with an alert ⚠); the strongest is [[Budesonide (drug)]] 0.05 µM: 5.61× (z +14.5, q 1e-44, up in 30 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.525× (z -7.7, q 9e-12, down in 26 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLF9]] (+0.75, fdr 7e-06), [[ACSL1]] (+0.75, fdr 7e-06), [[IRAK3]] (+0.72, fdr 7e-06); moves opposite to [[DCBLD2]] (-0.61, fdr 7e-06), [[LINC00973]] (-0.61, fdr 1e-05), [[ANTXR2]] (-0.60, fdr 1e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[CXCL8]] → it (grade B ⚠); 14 go from it, the strongest it → [[DYNC2I1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 2 with an alert ⚠; shown: the 15 strongest. 51 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8079.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 0.05 µM |  | **5.61×** | +14.5 | 1e-44 | 30/36 (A498, HOP62, …) | all doses, flat | position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **5.22×** | +13.3 | 6e-38 | 30/36 (HOP62, H4, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **4.60×** | +12.8 | 3e-35 | 26/35 (H4, A498, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **4.44×** | +12.5 | 1e-33 | 28/35 (SNU-423, A498, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **4.07×** | +11.8 | 7e-30 | 29/36 (SNU-423, A498, …) | all doses, flat | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **4.01×** | +11.6 | 3e-29 | 28/35 (SNU-423, A498, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **3.88×** | +11.4 | 5e-28 | 27/37 (A498, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **3.68×** | +10.9 | 7e-26 | 26/37 (A498, H4, …) | all doses, flat | position effect removed |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **3.46×** | +10.4 | 2e-23 | 28/37 (A498, HOP62, …) | inconsistent across doses | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **3.50×** | +9.7 | 2e-20 | 26/34 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **3.14×** | +9.6 | 5e-20 | 25/37 (A498, H4, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **3.09×** | +9.4 | 2e-19 | 25/37 (A498, H4, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **2.20×** | +9.3 | 4e-19 | 28/37 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **3.17×** | +9.3 | 7e-19 | 34/35 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **3.03×** | +9.3 | 7e-19 | 32/35 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8079.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.525×** | -7.7 | 9e-12 | 26/36 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.453×** | -6.7 | 7e-09 | 31/37 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.459×** | -6.6 | 1e-08 | 28/37 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.227×** | -6.5 | 1e-08 | 27/35 (NCI-H2347, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.474×** | -6.3 | 3e-08 | 31/37 (A549, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.500×** | -5.8 | 5e-07 | 23/37 (HOP62, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.489×** | -5.8 | 5e-07 | 24/34 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.513×** | -5.6 | 1e-06 | 25/36 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.643×** | -5.3 | 8e-06 | 22/36 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.328×** | -4.9 | 5e-05 | 25/37 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.579×** | -4.6 | 2e-04 | 23/36 (NCI-H460, H4, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.590×** | -4.5 | 4e-04 | 23/35 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.596×** | -4.4 | 5e-04 | 20/37 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.614×** | -4.1 | 0.002 | 23/33 (A549, NCI-H1573, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.613×** | -4.0 | 0.003 | 20/36 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.633×** | -3.9 | 0.004 | 18/35 (NCI-H2030, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.647×** | -3.7 | 0.007 | 18/37 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.651×** | -3.6 | 0.007 | 18/35 (CFPAC-1, HT-29, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.655×** | -3.4 | 0.015 | 16/37 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.62 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8079. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 40.5 | 23 | 1 | [[Triamcinolone (drug)]] 5 µM 8.75× (z +16.6) | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 57.7 | 20 | 4 (1 ⚠) | [[Budesonide (drug)]] 0.05 µM 12.4× (z +14.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -14.8) |
| [[HOP62 (line)]] | alt | 38.0 | 21 (1 ⚠) | 0 | [[Budesonide (drug)]] 0.05 µM 20.2× (z +15.5) | — |
| [[Panc 03.27 (line)]] | alt | 29.4 | 18 | 2 | [[Triamcinolone (drug)]] 5 µM 5.41× (z +13.7) | [[Auranofin (drug)]] 5 µM 0.179× (z -9.9) |
| [[H4 (line)]] | wt | 40.9 | 18 | 1 | [[Budesonide (drug)]] 0.05 µM 46.2× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -11.6) |
| [[SNU-423 (line)]] | alt | 33.6 | 18 | 1 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 24.0× (z +15.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.152× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~97% of this change |
| [[HS-578T (line)]] | alt | 15.0 | 18 | 0 | [[Budesonide (drug)]] 0.05 µM 27.9× (z +13.1) | — |
| [[NCI-H2347 (line)]] | alt | 50.0 | 14 | 4 (1 ⚠) | [[Budesonide (drug)]] 5 µM 5.77× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -12.5) |
| [[SW 900 (line)]] | alt | 16.0 | 17 | 0 | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 21.8× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 9.71 | 12 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 22.6× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 114 | 5 | 6 (2 ⚠) | [[Budesonide (drug)]] 0.05 µM 3.34× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -20.2) |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 10 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 14.6× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 19.0 | 9 | 0 | [[Budesonide (drug)]] 0.05 µM 15.4× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 22.6 | 7 | 1 | [[Budesonide (drug)]] 0.05 µM 8.51× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 30.3 | 4 | 3 (1 ⚠) | [[Budesonide (drug)]] 0.05 µM 5.70× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.0909× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -10.7) |
| [[A549 (line)]] | wt | 25.7 | 0 | 6 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0951× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~97% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.151× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 43.2 | 1 (1 ⚠) | 5 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.58× (z +9.3) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -18.3) |
| [[A-172 (line)]] | wt | 11.5 | 4 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 8.09× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 31.1 | 3 | 0 | [[Triamcinolone (drug)]] 5 µM 3.53× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 14.7 | 1 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 7.10× (z +8.9) | — |
| [[C32 (line)]] | wt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[HCT15 (line)]] | alt | 13.8 | 0 | 1 | — | [[Thymol (drug)]] 5 µM 0.184× (z -8.7) |
| [[KATO III (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 8.13 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.148× (z -10.0) |
| [[SW48 (line)]] | wt | 8.77 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0469× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 7.85 | 1 | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 5.07× (z +8.5) | — |
| [[A-427 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.08 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.91 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.18 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.82 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.90 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8079), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF9]] | +0.75 | +0.76 / +0.73 | both halves | 7e-06 | STRING 539 |
| [[ACSL1]] | +0.75 | +0.74 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[IRAK3]] | +0.72 | +0.66 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[SSBP2]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[MAOA]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[MT1E]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[FLVCR2]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SAA1]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ZMYND8]] | +0.63 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[B4GALT1]] | +0.63 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[TLR2]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[PER1]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 | STRING 488 |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCBLD2]] | -0.61 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[LINC00973]] | -0.61 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[ANTXR2]] | -0.60 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[EVA1A]] | -0.59 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[PLAU]] | -0.58 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[FGF5]] | -0.58 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[SIGLEC15]] | -0.56 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[SEMA3A]] | -0.56 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[LIF]] | -0.55 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[NAV3]] | -0.54 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[ANXA10]] | -0.53 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[PTHLH]] | -0.53 | -0.59 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL8]] | B | CXCL8 activity raises TSC22D3's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 2.70× lower at baseline in the lines without CXCL8 | 0.008 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[ANXA10]] | B | ANXA10 activity raises TSC22D3's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 2.29× lower at baseline in the lines without ANXA10 | 0.018 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[ANTXR2]] | B | ANTXR2 activity raises TSC22D3's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 2.74× lower at baseline in the lines without ANTXR2 | 0.025 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[FOXC2]] | B | FOXC2 activity raises TSC22D3's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 2.28× lower at baseline in the lines without FOXC2 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT |
| [[TLR2]] | B | TLR2 activity raises TSC22D3's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.97× lower at baseline in the lines without TLR2 | 0.047 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[CD44]] | B | CD44 activity raises TSC22D3's level | lines that do not express CD44 (15) vs lines expressing it (35) | 2.21× lower at baseline in the lines without CD44 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[CD274]] | B | CD274 activity raises TSC22D3's level | lines that do not express CD274 (18) vs lines expressing it (32) | 1.99× lower at baseline in the lines without CD274 | 0.054 | ⚠ within organs, on part of the lines; also absent: GBP5, IL1B, PDCD1LG2 |
| [[DENND3]] | B | DENND3 activity raises TSC22D3's level | lines that do not express DENND3 (7) vs lines expressing it (43) | 2.46× lower at baseline in the lines without DENND3 | 0.058 | ⚠ within organs, on part of the lines; also absent: JAG1, DUSP1, AMIGO2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises TSC22D3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RTN4RL1]] | B | RTN4RL1 activity lowers TSC22D3's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 1.77× higher at baseline in the lines without RTN4RL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| [[LIF]] | B | LIF activity raises TSC22D3's level | lines that do not express LIF (10) vs lines expressing it (40) | 2.22× lower at baseline in the lines without LIF | 0.063 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |
| [[LINC01589]] | B | LINC01589 activity raises TSC22D3's level | lines that do not express LINC01589 (23) vs lines expressing it (27) | 1.74× lower at baseline in the lines without LINC01589 | 0.071 | ⚠ within organs, on part of the lines; also absent: HNF1B, ENSG00000279806, GOLT1A |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNC2I1]] | B | TSC22D3 activity strengthens DYNC2I1's drug response | lines that do not express TSC22D3 (11) vs lines expressing it (38) | the lines without TSC22D3 respond 0.66× as strongly (z diff +2.26); strongest at Digitoxin 5 µM: 0.75x vs 0.52x (z diff +3.8) | 0.020 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CPD]] | B | TSC22D3 activity raises CPD's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 1.36× lower at baseline in the lines without TSC22D3 | 0.030 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[CXCL8]] | B | TSC22D3 activity raises CXCL8's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 4.19× lower at baseline in the lines without TSC22D3 | 0.037 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[PACSIN2]] | B | TSC22D3 activity raises PACSIN2's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 1.32× lower at baseline in the lines without TSC22D3 | 0.043 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[DUSP1]] | B | TSC22D3 activity raises DUSP1's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 1.73× lower at baseline in the lines without TSC22D3 | 0.044 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[B4GALT1]] | B | TSC22D3 activity raises B4GALT1's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 1.92× lower at baseline in the lines without TSC22D3 | 0.048 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[DENND3]] | B | TSC22D3 activity raises DENND3's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 1.88× lower at baseline in the lines without TSC22D3 | 0.049 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[IRAK3]] | B | TSC22D3 activity raises IRAK3's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 2.27× lower at baseline in the lines without TSC22D3 | 0.068 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| cells under [[Futibatinib (drug)]] 5 µM | B | TSC22D3 activity lowers the cells' numbers under Futibatinib 5 µM (makes them more sensitive) | lines that do not express TSC22D3 (11) vs lines expressing it (37) | the lines without TSC22D3: 1.19× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[MFGE8]] | B | TSC22D3 activity raises MFGE8's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 2.33× lower at baseline in the lines without TSC22D3 | 0.074 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[SLPI]] | B | TSC22D3 activity raises SLPI's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 2.63× lower at baseline in the lines without TSC22D3 | 0.088 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[FOXC2]] | B | TSC22D3 activity raises FOXC2's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 2.42× lower at baseline in the lines without TSC22D3 | 0.093 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.7, 15.4); signed map (16.4, 30.0). **Vector** length 145, 48.3% of its response variance represented; |z| ≥ 3 in 1,732 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Budesonide (drug)]] 0.05 µM |  | +9.0 | +14.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +8.7 | +13.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +8.1 | +11.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +8.0 | +9.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +7.9 | +8.2 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -6.3 | -2.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.7 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.3 | -2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.0 | -5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -4.5 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -2.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.1 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -4.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | TSC22 domain family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.3 — chrX:107,713,221-107,777,342 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DIP, GILZ, TSC-22R, hDIP; previously DSIPI |
| Gene groups (HGNC) | TSC22 domain family |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99576](https://www.uniprot.org/uniprotkb/Q99576) (TSC22 domain family protein 3):

> Protects T-cells from IL2 deprivation-induced apoptosis through the inhibition of FOXO3A transcriptional activity that leads to the down-regulation of the pro-apoptotic factor BCL2L11. In macrophages, plays a role in the anti-inflammatory and immunosuppressive effects of glucocorticoids and IL10. In T-cells, inhibits anti-CD3-induced NFKB1 nuclear translocation and thereby NFKB1 DNA-binding activities. In vitro, suppresses AP-1 transcription factor complex DNA-binding activities (By …

**Summary**, from NCBI Gene [1831](https://www.ncbi.nlm.nih.gov/gene/1831):

> This gene encodes the anti-inflammatory protein glucocorticoid (GC)-induced leucine zipper. Expression of this gene stimulated by glucocorticoids and interleukin 10 and it appears to play a key role in the anti-inflammatory and immunosuppressive effects of this steroid. This protein has also been shown to inhibit pro-inflammatory molecules including nuclear factor &#954;B. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:3051](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3051) · Entrez [1831](https://www.ncbi.nlm.nih.gov/gene/1831) · UniProt [Q99576](https://www.uniprot.org/uniprotkb/Q99576) · Ensembl [ENSG00000157514](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157514)

## Data

Gene col 8079: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8079); `tables/drug_effects.parquet` (88 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8079, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8079]; `tensor/DDL_lfc|DDL_z.npy` [8079]; `embed/gene_vectors.npy` [8079]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8079 or target_col == 8079). Every well: [[TSC22D3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSC22D3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
