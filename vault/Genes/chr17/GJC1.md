---
symbol: "GJC1"
type: "gene"
col: 11349
ensembl_id: "ENSG00000182963"
name: "gap junction protein gamma 1"
location: "17q21.31"
module: 116
arm: "+"
pooled_cpm: 48.75
n_lines_expressing: 37
n_dd_up: 23
n_dd_down: 17
n_dd_up_clean: 19
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 8
direction_downstream: 12
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# GJC1

*gap junction protein gamma 1* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.45× (z +13.5, q 7e-39, up in 31 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.659× (z -6.3, q 1e-07, down in 19 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Budesonide (drug)]] 0.5 µM: 0.716× (z -5.1, q 7e-05, down in 21 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RGS20]] (+0.62, fdr 1e-05), [[NAV3]] (+0.58, fdr 1e-05), [[FRMD6]] (+0.57, fdr 1e-05); moves opposite to [[SNRPN]] (-0.52, fdr 1e-05), [[MED23]] (-0.47, fdr 6e-05), [[RAB2B]] (-0.45, fdr 4e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LINC00472]] → it (grade B ⚠); 12 go from it, the strongest it → [[LINC00472]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11349.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.45×** | +13.5 | 7e-39 | 31/34 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +13.1 | 6e-37 | 29/34 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.36×** | +13.0 | 2e-36 | 31/35 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.16×** | +11.2 | 6e-27 | 28/35 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +10.9 | 1e-25 | 31/34 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.95×** | +10.1 | 6e-22 | 29/34 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.90×** | +9.7 | 3e-20 | 29/35 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +8.7 | 2e-16 | 27/34 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.78×** | +8.7 | 3e-16 | 31/35 (C32, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.90×** | +8.4 | 2e-15 | 27/35 (PANC-1, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.72×** | +7.9 | 2e-13 | 30/34 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.44×** | +7.8 | 2e-13 | 29/35 (CFPAC-1, C32, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +7.3 | 1e-11 | 25/35 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.34×** | +6.7 | 7e-10 | 30/35 (LOX-IMVI, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.54×** | +6.6 | 2e-09 | 29/34 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +6.2 | 2e-08 | 26/35 (C32, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +6.1 | 4e-08 | 23/35 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.48×** | +5.9 | 1e-07 | 25/34 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.48×** | +5.9 | 1e-07 | 25/34 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11349.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.659×** | -6.3 | 1e-07 | 19/33 (A-427, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.692×** | -5.4 | 2e-05 | 17/32 (J82, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 0.5 µM |  | **0.716×** | -5.1 | 7e-05 | 21/35 (NCI-H460, A549, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.622×** | -4.3 | 0.002 | 19/34 (Panc 03.27, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.777×** | -3.8 | 0.012 | 15/35 (NCI-H460, A549, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.778×** | -3.8 | 0.012 | 18/34 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.782×** | -3.7 | 0.013 | 17/34 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.783×** | -3.7 | 0.013 | 18/35 (PANC-1, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.794×** | -3.5 | 0.027 | 17/34 (SW 1271, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.780×** | -3.5 | 0.027 | 17/34 (A549, CHP-212, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.803×** | -3.4 | 0.036 | 14/35 (NCI-H23, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.660×** | -3.3 | 0.046 | 12/34 (H4, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.808×** | -3.2 | 0.050 | 17/34 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.666×** | -3.2 | 0.050 | 14/35 (A-427, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.708×** | -3.2 | 0.059 | 14/35 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.721×** | -3.0 | 0.094 | 11/35 (HS-578T, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11349. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 68.0 | 12 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 5.75× (z +14.3) | — |
| [[C32 (line)]] | wt | 39.6 | 10 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +15.6) | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change |
| [[PANC-1 (line)]] | alt | 96.0 | 7 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.85× (z +14.0) | [[Panobinostat (drug)]] 5 µM 0.336× (z -11.4) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.340× (z -11.3) |
| [[A549 (line)]] | wt | 80.3 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.34× (z +22.5) | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change |
| [[LOX-IMVI (line)]] | wt | 146 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.348× (z -10.5) |
| [[HOP62 (line)]] | alt | 68.5 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +10.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 121 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +17.0) | — |
| [[HS-578T (line)]] | alt | 35.8 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.88× (z +12.4) | — |
| [[A-172 (line)]] | wt | 114 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +9.6) | — |
| [[A498 (line)]] | wt | 54.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +21.2) | — |
| [[SK-MEL-2 (line)]] | alt | 84.4 | 4 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.62× (z +12.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.76× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 64.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +17.7) | — |
| [[NCI-H1573 (line)]] | alt | 22.2 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.70× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 28.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 62.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 50.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +20.5) | — |
| [[SW1417 (line)]] | alt | 19.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +9.5) | — |
| [[A-427 (line)]] | wt | 79.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0682× (z -29.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.361× (z -8.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 125 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +8.8) | — |
| [[J82 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.307× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 69.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.100× (z -18.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 18.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +9.8) | — |
| [[SW 1271 (line)]] | alt | 42.5 | 0 | 1 | — | [[Talc (drug)]] 0.05 µM 0.0651× (z -8.8) |
| [[SW480 (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.13 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 75.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.99 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.97 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.56 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.15 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.85 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.74 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.09 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11349), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGS20]] | +0.62 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[NAV3]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[FRMD6]] | +0.57 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[FGF5]] | +0.55 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[SRGAP1]] | +0.55 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[MARCHF4]] | +0.55 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[FMNL3]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[TRAF1]] | +0.55 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[SCHIP1]] | +0.54 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[ETS1]] | +0.54 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[LINC00973]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[ROR1-AS1]] | +0.53 | +0.43 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPN]] | -0.52 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[MED23]] | -0.47 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[RAB2B]] | -0.45 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[C1R]] | -0.45 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[COPS8]] | -0.45 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[TSC22D3]] | -0.44 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[CROT]] | -0.44 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[TENT2]] | -0.43 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[FAM229B]] | -0.43 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[UBR3]] | -0.43 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[TMEM87A]] | -0.43 | -0.46 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00472]] | B | LINC00472 activity raises GJC1's level | lines that do not express LINC00472 (19) vs lines expressing it (31) | 3.23× lower at baseline in the lines without LINC00472 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000279289, RBMS3, C2orf74-DT |
| [[SPHK1]] | B | SPHK1 activity raises GJC1's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 2.78× lower at baseline in the lines without SPHK1 | 0.019 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |
| [[LIF]] | B | LIF activity strengthens GJC1's drug response | lines that do not express LIF (7) vs lines expressing it (28) | the lines without LIF respond 0.47× as strongly (z diff +1.98); strongest at Homoharringtonine 5 µM: 1.25x vs 2.39x (z diff +3.6) | 0.047 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213; target measured in part of the lines; the reference differs; artifact flags |
| [[SOCS2-AS1]] | B | SOCS2-AS1 activity raises GJC1's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 2.81× lower at baseline in the lines without SOCS2-AS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |
| [[FGF2]] | C | FGF2 activity raises GJC1's level | lines that do not express FGF2 (16) vs lines expressing it (34) | 4.24× lower at baseline in the lines without FGF2 | 0.023 | ⚠ within organs, on part of the lines; also absent: F2R, EML1, DPY19L2; co-absent with the target |
| [[AKT3]] | C | AKT3 activity raises GJC1's level | lines that do not express AKT3 (16) vs lines expressing it (34) | 4.60× lower at baseline in the lines without AKT3 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041; co-absent with the target |
| [[RGS20]] | C | RGS20 activity raises GJC1's level | lines that do not express RGS20 (12) vs lines expressing it (38) | 4.55× lower at baseline in the lines without RGS20 | 0.028 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, ENSG00000286964, SIX1; co-absent with the target |
| [[SCHIP1]] | C | SCHIP1 activity raises GJC1's level | lines that do not express SCHIP1 (7) vs lines expressing it (43) | 6.22× lower at baseline in the lines without SCHIP1 | 0.091 | ⚠ within organs, on part of the lines; also absent: DYRK3, IQCJ-SCHIP1, ROBO3; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 10, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00472]] | B | GJC1 activity raises LINC00472's level | lines that do not express GJC1 (13) vs lines expressing it (37) | 5.06× lower at baseline in the lines without GJC1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB |
| [[CROT]] | B | GJC1 activity strengthens CROT's drug response | lines that do not express GJC1 (11) vs lines expressing it (35) | the lines without GJC1 respond 0.62× as strongly (z diff +1.82); strongest at Homoharringtonine 5 µM: 0.74x vs 0.39x (z diff +4.7) | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB; target measured in part of the lines; artifact flags |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM | B | GJC1 activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 0.5 µM (protects the cells) | lines that do not express GJC1 (13) vs lines expressing it (35) | the lines without GJC1: 0.82× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB |
| [[CCND1]] | B | GJC1 activity raises CCND1's level | lines that do not express GJC1 (13) vs lines expressing it (37) | 1.35× lower at baseline in the lines without GJC1 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB |
| cells under [[Posaconazole (drug)]] 0.5 µM | B | GJC1 activity raises the cells' numbers under Posaconazole 0.5 µM (protects the cells) | lines that do not express GJC1 (13) vs lines expressing it (35) | the lines without GJC1: 0.83× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | B | GJC1 activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express GJC1 (13) vs lines expressing it (35) | the lines without GJC1: 1.21× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB |
| [[PLAU]] | B | GJC1 activity raises PLAU's level | lines that do not express GJC1 (13) vs lines expressing it (37) | 2.34× lower at baseline in the lines without GJC1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB |
| [[CDC42EP3]] | B | GJC1 activity raises CDC42EP3's level | lines that do not express GJC1 (13) vs lines expressing it (37) | 3.00× lower at baseline in the lines without GJC1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB |
| cells under [[Fenofibrate (drug)]] 0.05 µM | B | GJC1 activity lowers the cells' numbers under Fenofibrate 0.05 µM (makes them more sensitive) | lines that do not express GJC1 (13) vs lines expressing it (35) | the lines without GJC1: 1.30× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB |
| cells under [[Cobimetinib (drug)]] 0.5 µM | B | GJC1 activity lowers the cells' numbers under Cobimetinib 0.5 µM (makes them more sensitive) | lines that do not express GJC1 (13) vs lines expressing it (35) | the lines without GJC1: 1.23× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB |
| [[RGS20]] | C | GJC1 activity raises RGS20's level | lines that do not express GJC1 (13) vs lines expressing it (37) | 3.79× lower at baseline in the lines without GJC1 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB; co-absent with the target |
| [[LINC00973]] | C | GJC1 activity raises LINC00973's level | lines that do not express GJC1 (13) vs lines expressing it (37) | 2.35× lower at baseline in the lines without GJC1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB; co-absent with the target |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.612). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.7, 11.6); signed map (15.0, 43.8). **Vector** length 106, 30.4% of its response variance represented; |z| ≥ 3 in 1,120 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.0 | +7.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.1 | +8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +13.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +13.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.2 | +7.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +7.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.7 | +5.9 |
| fall | [[NG25 (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.6 | -2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | +1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | +2.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -2.2 | -3.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | gap junction protein gamma 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:44,798,448-44,830,816 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CX45; previously GJA7 |
| Gene groups (HGNC) | Gap junction proteins |
| Reactome | 8 pathways, smallest: Electric Transmission Across Gap Junctions; Transmission across Electrical Synapses; Gap junction assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P36383](https://www.uniprot.org/uniprotkb/P36383) (Gap junction gamma-1 protein):

> Structural component of the gap junction, a specialized intercellular structure consisting of a cluster of closely packed pairs of transmembrane channels, the connexons, that allow passage of small molecules and electrical signals between neighboring cells. Forms homotypic and heterotypic channels gated by transjunctional voltage (By similarity). Involved in intercellular innate immune signaling. Mediates translocation of 2',3'-cGAMP and 2',5'-oligoadenylates (2-5A) second messengers from …

**Summary**, from NCBI Gene [10052](https://www.ncbi.nlm.nih.gov/gene/10052):

> This gene is a member of the connexin gene family. The encoded protein is a component of gap junctions, which are composed of arrays of intercellular channels that provide a route for the diffusion of low molecular weight materials from cell to cell. Alternatively spliced transcript variants encoding the same isoform have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4280](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4280) · Entrez [10052](https://www.ncbi.nlm.nih.gov/gene/10052) · UniProt [P36383](https://www.uniprot.org/uniprotkb/P36383) · Ensembl [ENSG00000182963](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182963)

## Data

Gene col 11349: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11349); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11349, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11349]; `tensor/DDL_lfc|DDL_z.npy` [11349]; `embed/gene_vectors.npy` [11349]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11349 or target_col == 11349). Every well: [[GJC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GJC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
