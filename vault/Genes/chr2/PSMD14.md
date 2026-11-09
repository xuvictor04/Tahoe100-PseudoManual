---
symbol: "PSMD14"
type: "gene"
col: 3638
ensembl_id: "ENSG00000115233"
name: "proteasome 26S subunit, non-ATPase 14"
location: "2q24.2"
module: 60
arm: "+"
pooled_cpm: 208.03
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 33
n_dd_up_clean: 20
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# PSMD14

*proteasome 26S subunit, non-ATPase 14* — 2q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (13 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 3.94× (z +19.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.664× (z -5.9, q 2e-06, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD2]] (+0.71, fdr 7e-06), [[PSMB7]] (+0.66, fdr 7e-06), [[OLA1]] (+0.65, fdr 9e-06); moves opposite to [[GABARAP]] (-0.65, fdr 1e-05, ⚠ GABARAP in the vector space only through flagged drug-doses), [[NEU1]] (-0.61, fdr 1e-05), [[SIRT1]] (-0.58, fdr 1e-05), [[LSM14B]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3638.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.94×** | +19.8 | 0e+00 | 48/48 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.65×** | +18.7 | 0e+00 | 48/48 (LoVo, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.48×** | +17.0 | 0e+00 | 48/48 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **6.64×** | +14.2 | 1e-43 | 49/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.48×** | +13.1 | 2e-37 | 46/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.15×** | +11.1 | 2e-26 | 45/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **4.14×** | +10.7 | 1e-24 | 47/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.98×** | +9.8 | 5e-21 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.39×** | +9.0 | 2e-17 | 48/49 (HT-29, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.80×** | +8.5 | 2e-15 | 42/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +8.1 | 2e-14 | 45/48 (C32, COLO 205, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.44×** | +7.4 | 6e-12 | 34/48 (COLO 205, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +7.3 | 9e-12 | 38/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.53×** | +7.0 | 1e-10 | 42/45 (KATO III, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.56×** | +6.5 | 4e-09 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +5.1 | 1e-05 | 29/48 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +4.6 | 1e-04 | 35/49 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.35×** | +4.2 | 8e-04 | 30/48 (Hs 766T, A549, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.015 | 24/47 (SK-MEL-2, NCI-H1573, …) | rises with dose | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.022 | 27/48 (SW480, Hs 766T, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3638.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.664×** | -5.9 | 2e-06 | 38/48 (RKO, J82, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.682×** | -5.3 | 3e-05 | 41/50 (AsPC-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.775×** | -5.2 | 3e-05 | 28/49 (RKO, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.700×** | -5.2 | 3e-05 | 34/48 (KATO III, RKO, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.705×** | -4.9 | 1e-04 | 34/47 (SK-MEL-2, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.742×** | -4.8 | 2e-04 | 36/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.545×** | -4.6 | 4e-04 | 35/50 (H4, AsPC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.787×** | -4.4 | 6e-04 | 30/48 (AsPC-1, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.739×** | -4.4 | 7e-04 | 32/48 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.753×** | -4.1 | 0.002 | 30/47 (SK-MEL-2, RKO, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.751×** | -4.0 | 0.003 | 31/48 (AsPC-1, HCT15, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.821×** | -3.9 | 0.004 | 29/49 (NCI-H2122, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.832×** | -3.7 | 0.009 | 22/48 (SW480, HCT15, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.776×** | -3.7 | 0.009 | 28/48 (HOP62, A549, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.765×** | -3.7 | 0.009 | 30/48 (SK-MEL-2, HepG2/C3A, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.779×** | -3.6 | 0.010 | 30/48 (KATO III, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3638. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 133 | 13 (3 ⚠) | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 6.32× (z +21.1) | [[Ponatinib (drug)]] 0.05 µM 0.415× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 269 | 12 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.37× (z +19.5) | — |
| [[PANC-1 (line)]] | alt | 176 | 12 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.22× (z +17.6) | — |
| [[SW480 (line)]] | alt | 207 | 12 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.83× (z +21.5) | — |
| [[LoVo (line)]] | wt | 140 | 11 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.56× (z +22.3) | — |
| [[NCI-H1792 (line)]] | alt | 184 | 11 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.09× (z +16.2) | — |
| [[HT-29 (line)]] | alt | 104 | 10 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 8.78× (z +21.2) | — |
| [[NCI-H1573 (line)]] | alt | 76.7 | 10 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 9.57× (z +19.1) | — |
| [[COLO 205 (line)]] | alt | 71.3 | 9 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 14.1× (z +18.1) | — |
| [[HepG2_C3A (line)]] | wt | 323 | 8 (3 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.03× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.452× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 211 | 9 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.49× (z +17.4) | — |
| [[NCI-H23 (line)]] | alt | 206 | 9 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.59× (z +15.8) | — |
| [[RKO (line)]] | wt | 383 | 5 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.00× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -13.6) |
| [[SW48 (line)]] | wt | 273 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.70× (z +14.4) | — |
| [[Panc 03.27 (line)]] | alt | 136 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.16× (z +17.2) | — |
| [[SW1417 (line)]] | alt | 175 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.97× (z +14.3) | — |
| [[C32 (line)]] | wt | 173 | 6 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.32× (z +12.6) | — |
| [[Hs 766T (line)]] | wt | 109 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.63× (z +14.8) | — |
| [[A-172 (line)]] | wt | 213 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.23× (z +15.4) | — |
| [[A549 (line)]] | wt | 193 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.07× (z +11.0) | — |
| [[H4 (line)]] | wt | 339 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.12× (z +12.4) | — |
| [[HCT15 (line)]] | alt | 201 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.60× (z +17.3) | — |
| [[HEC-1-A (line)]] | alt | 187 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.19× (z +16.3) | — |
| [[HOP62 (line)]] | alt | 278 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 10.3× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 243 | 4 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.01× (z +12.1) | [[Cobimetinib (drug)]] 5 µM 0.443× (z -8.6) |
| [[A498 (line)]] | wt | 207 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.52× (z +16.9) | — |
| [[AsPC-1 (line)]] | alt | 253 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.51× (z +10.3) | — |
| [[C-33 A (line)]] | alt | 185 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.95× (z +11.3) | — |
| [[HS-578T (line)]] | alt | 195 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.58× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 161 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.91× (z +13.2) | — |
| [[J82 (line)]] | alt | 247 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.43× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 241 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.83× (z +13.1) | — |
| [[RPMI-7951 (line)]] | alt | 237 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.78× (z +14.3) | — |
| [[SNU-1 (line)]] | wt | 233 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.35× (z +14.7) | — |
| [[SW 900 (line)]] | alt | 262 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.73× (z +10.1) | — |
| [[A-427 (line)]] | wt | 242 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.70× (z +12.2) | — |
| [[BT-474 (line)]] | alt | 157 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.49× (z +14.1) | — |
| [[CFPAC-1 (line)]] | alt | 157 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.09× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 346 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.91× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 144 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.91× (z +12.0) | — |
| [[SNU-423 (line)]] | alt | 148 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.39× (z +13.5) | — |
| [[AN3 CA (line)]] | alt | 268 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.70× (z +10.5) | — |
| [[NCI-H2347 (line)]] | alt | 211 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.20× (z +9.6) | — |
| [[CHP-212 (line)]] | wt | 145 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.55× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 377 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +9.3) | — |
| [[SW 1271 (line)]] | alt | 212 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.95× (z +9.4) | — |
| [[NCI-H2122 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 159 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3638), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD2]] | +0.71 | +0.70 / +0.73 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMB7]] | +0.66 | +0.64 / +0.68 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[OLA1]] | +0.65 | +0.73 / +0.57 | both halves | 9e-06 | STRING 488 |
| [[PSMD12]] | +0.63 | +0.57 / +0.66 | both halves | 1e-05 | same gene group; pathway: HALLMARK_MTORC1_SIGNALING; STRING 999 |
| [[CCT5]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 759 |
| [[PSMD1]] | +0.62 | +0.57 / +0.68 | both halves | 1e-05 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[DGKG]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[CCT4]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 793 |
| [[CCT6A]] | +0.60 | +0.54 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 747 |
| [[PSMA1]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[HSPH1]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[CCT2]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 792 |

## Genes that move opposite

*37 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABARAP]] ⚠ | -0.65 | -0.67 / -0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NEU1]] | -0.61 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[SIRT1]] | -0.58 | -0.65 / -0.53 | both halves | 1e-05 | pathway: Adherens junctions interactions |
| [[LSM14B]] | -0.57 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[TOLLIP]] | -0.57 | -0.57 / -0.58 | both halves | 9e-06 | pathway: Interleukin-1 family signaling |
| [[FLCN]] | -0.57 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[KLHL24]] | -0.56 | -0.66 / -0.44 | both halves | 3e-05 |  |
| [[SAT2]] | -0.55 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[RRAGC]] | -0.55 | -0.57 / -0.58 | both halves | 9e-06 | pathway: Intracellular signaling by second messengers |
| [[BMF]] | -0.55 | -0.56 / -0.45 | both halves | 3e-05 | pathway: Apoptosis |
| [[TXNIP]] | -0.55 | -0.55 / -0.51 | both halves | 1e-05 | pathway: Cellular response to chemical stress |
| [[CHKB]] | -0.55 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[GPX4]] | -0.54 | -0.57 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.2, -12.9); signed map (-27.9, -29.5). **Vector** length 97.9, 45.4% of its response variance represented; |z| ≥ 3 in 1,998 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.58 to 4); *Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding* (reactome, mean cos +0.58 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +8.3 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +8.0 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.8 | +18.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +7.2 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.7 | +19.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | -0.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +9.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.4 | +1.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -7.6 | +13.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.6 | +8.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.4 | +9.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -5.6 | +11.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -4.8 | +5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -4.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.5 | +0.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.0 | -4.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.9 | -4.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit, non-ATPase 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.2 — chr2:161,308,425-161,411,717 (+) |
| Ensembl biotype | protein_coding |
| Also known as | POH1, pad1, Rpn11 |
| Gene groups (HGNC) | Proteasome; JAMM/MPN+ metallopeptidase family |
| Hallmark sets | MTORC1_SIGNALING, MYC_TARGETS_V1 |
| Reactome | 171 pathways, smallest: Metalloprotease DUBs; Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC) |
| Matched by | ensembl_id |

**Function**, from UniProt [O00487](https://www.uniprot.org/uniprotkb/O00487) (Ubiquitin C-terminal hydrolase PSMD14):

> Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair. The PSMD14 …

**Summary**, from NCBI Gene [10213](https://www.ncbi.nlm.nih.gov/gene/10213):

> This gene encodes a component of the 26S proteasome. The 26S proteasome is a large multiprotein complex that catalyzes the degradation of ubiquitinated intracellular proteins. The encoded protein is a component of the 19S regulatory cap complex of the 26S proteasome and mediates substrate deubiquitination. A pseudogene of this gene is also located on the long arm of chromosome 2. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:16889](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16889) · Entrez [10213](https://www.ncbi.nlm.nih.gov/gene/10213) · UniProt [O00487](https://www.uniprot.org/uniprotkb/O00487) · Ensembl [ENSG00000115233](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115233)

## Data

Gene col 3638: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3638); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3638, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3638]; `tensor/DDL_lfc|DDL_z.npy` [3638]; `embed/gene_vectors.npy` [3638]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3638 or target_col == 3638). Every well: [[PSMD14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMD14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
