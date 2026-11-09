---
symbol: "NABP1"
type: "gene"
col: 10404
ensembl_id: "ENSG00000173559"
name: "nucleic acid binding protein 1"
location: "2q32.3"
module: 116
arm: "+"
pooled_cpm: 152.25
n_lines_expressing: 46
n_dd_up: 21
n_dd_down: 14
n_dd_up_clean: 16
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 16
direction_downstream: 15
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# NABP1

*nucleic acid binding protein 1* — 2q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.48× (z +15.1, q 0e+00, up in 35 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.475× (z -8.8, q 1e-15, down in 37 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABL2]] (+0.76, fdr 7e-06), [[ERCC1]] (+0.68, fdr 7e-06), [[BACH1]] (+0.67, fdr 7e-06); moves opposite to [[FBXO7]] (-0.62, fdr 7e-06), [[RCOR3]] (-0.60, fdr 1e-05), [[HSF2]] (-0.60, fdr 1e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[ITGB1-DT]] → it (grade B ⚠); 15 go from it, the strongest it → [[HSF2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10404.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.48×** | +15.1 | 0e+00 | 35/44 (hTERT-HPNE, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.97×** | +11.3 | 4e-27 | 41/44 (A-172, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.08×** | +8.6 | 1e-15 | 36/44 (hTERT-HPNE, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.87×** | +7.4 | 2e-11 | 39/45 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.4 | 7e-06 | 34/44 (Hs 766T, A498, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.56×** | +5.3 | 1e-05 | 28/44 (HT-29, A-172, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.56×** | +4.7 | 2e-04 | 27/44 (A498, A-427, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.49×** | +4.7 | 2e-04 | 32/44 (HEC-1-A, NCI-H1573, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.54×** | +4.5 | 4e-04 | 26/43 (HT-29, A-172, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.45×** | +4.2 | 0.002 | 25/43 (HT-29, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +4.1 | 0.003 | 23/44 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +3.9 | 0.005 | 23/44 (hTERT-HPNE, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.24×** | +3.6 | 0.014 | 23/45 (C-33 A, Hs 766T, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.024 | 23/44 (A498, RKO, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.044 | 18/45 (HT-29, CHP-212, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.081 | 18/44 (SW480, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.081 | 21/44 (hTERT-HPNE, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.081 | 21/44 (A-172, A498, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10404.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.475×** | -8.8 | 1e-15 | 37/44 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.573×** | -6.5 | 2e-08 | 34/44 (NCI-H23, H4, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.604×** | -5.7 | 2e-06 | 32/43 (J82, A549, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[NG25 (drug)]] 5 µM |  | **0.434×** | -5.1 | 4e-05 | 32/43 (RKO, NCI-H23, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.739×** | -5.0 | 5e-05 | 34/44 (BT-474, RKO, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM |  | **0.753×** | -4.7 | 2e-04 | 37/44 (COLO 205, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.671×** | -4.7 | 2e-04 | 35/44 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.686×** | -4.4 | 7e-04 | 30/44 (BT-474, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.691×** | -4.4 | 8e-04 | 34/44 (NCI-H1573, BT-474, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.721×** | -3.9 | 0.007 | 25/45 (NCI-H23, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); composition shift |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.719×** | -3.7 | 0.010 | 22/43 (NCI-H2030, HOP62, …) | top dose only |  |
| [[Erlotinib (drug)]] 5 µM |  | **0.736×** | -3.5 | 0.024 | 23/43 (BT-474, NCI-H2030, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.760×** | -3.1 | 0.081 | 22/44 (HEC-1-A, NCI-H23, …) | all doses, flat |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.773×** | -3.0 | 0.099 | 22/44 (RKO, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10404. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 156 | 0 | 13 (3 ⚠) | — | [[Neratinib (drug)]] 0.5 µM 0.125× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 384 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.269× (z -11.3) |
| [[RKO (line)]] | wt | 490 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -11.9) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[NG25 (drug)]] 5 µM 0.139× (z -9.1) |
| [[SW480 (line)]] | alt | 85.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +19.3) | — |
| [[HOP62 (line)]] | alt | 137 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +19.6) | [[Ponatinib (drug)]] 5 µM 0.256× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 169 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +20.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 67.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.74× (z +9.7) | [[Adagrasib (drug)]] 0.05 µM 0.607× (z -10.9) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 113 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +12.1) | [[Ponatinib (drug)]] 5 µM 0.364× (z -8.6) |
| [[HT-29 (line)]] | alt | 65.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +14.4) | — |
| [[J82 (line)]] | alt | 189 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.256× (z -11.4) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 379 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +10.2) | [[Ponatinib (drug)]] 5 µM 0.252× (z -10.9) |
| [[PANC-1 (line)]] | alt | 151 | 0 | 3 (2 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.315× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 112 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +11.3) | — |
| [[A498 (line)]] | wt | 124 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +15.6) | — |
| [[AsPC-1 (line)]] | alt | 167 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +19.8) | — |
| [[C32 (line)]] | wt | 53.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +16.0) | — |
| [[H4 (line)]] | wt | 205 | 0 | 2 (1 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.266× (z -8.9) |
| [[HS-578T (line)]] | alt | 117 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 479 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.66× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 127 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.53× (z +10.4) | — |
| [[SW 900 (line)]] | alt | 68.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +12.9) | — |
| [[A-172 (line)]] | wt | 119 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.42× (z +12.9) | — |
| [[A-427 (line)]] | wt | 269 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[A549 (line)]] | wt | 150 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.237× (z -10.0) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 285 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +13.0) | — |
| [[CHP-212 (line)]] | wt | 57.4 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0608× (z -11.8) |
| [[COLO 205 (line)]] | alt | 151 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +11.7) | — |
| [[HepG2_C3A (line)]] | wt | 142 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.212× (z -8.6) |
| [[Hs 766T (line)]] | wt | 43.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +16.5) | — |
| [[LoVo (line)]] | wt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +11.9) | — |
| [[NCI-H1792 (line)]] | alt | 126 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 82.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +12.8) | — |
| [[AN3 CA (line)]] | alt | 26.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 69.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 27.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 34.1 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 349 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 148 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10404), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABL2]] | +0.76 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[ERCC1]] | +0.68 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[BACH1]] | +0.67 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[C11orf91]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[MCL1]] | +0.66 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[LINC00513]] | +0.66 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[PPP1R10]] | +0.65 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[NOP14-AS1]] | +0.65 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[SLC9A1]] | +0.65 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[CFLAR-AS1]] | +0.63 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[ITGB1-DT]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[KBTBD8]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO7]] | -0.62 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[RCOR3]] | -0.60 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[HSF2]] | -0.60 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[TADA1]] | -0.59 | -0.62 / -0.58 | both halves | 8e-06 |  |
| [[KCTD3]] | -0.58 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[C12orf76]] | -0.58 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[COPS4]] | -0.58 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[MBIP]] | -0.58 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[MLLT10]] | -0.57 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[UBAC1]] | -0.57 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[KDM1A]] | -0.56 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[USP33]] | -0.56 | -0.61 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 13, C 3. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB1-DT]] | B | ITGB1-DT activity raises NABP1's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 2.48× lower at baseline in the lines without ITGB1-DT | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[ADTRP]] | B | ADTRP activity raises NABP1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 1.97× lower at baseline in the lines without ADTRP | 0.033 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[EGFR]] | B | EGFR activity raises NABP1's level | lines that do not express EGFR (7) vs lines expressing it (43) | 2.16× lower at baseline in the lines without EGFR | 0.038 | ⚠ within organs, on part of the lines; also absent: C1RL-AS1, PSD4, RNASEL |
| [[CCDC71L]] | B | CCDC71L activity raises NABP1's level | lines that do not express CCDC71L (8) vs lines expressing it (42) | 2.01× lower at baseline in the lines without CCDC71L | 0.041 | ⚠ within organs, on part of the lines; also absent: RAI14, VIM-AS1, ENSG00000243797; maybe low, not absent |
| [[TM4SF1-AS1]] | B | TM4SF1-AS1 activity raises NABP1's level | lines that do not express TM4SF1-AS1 (14) vs lines expressing it (36) | 1.65× lower at baseline in the lines without TM4SF1-AS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: CXCL1, MBP, TM4SF1 |
| [[PRKG2-AS1]] | B | PRKG2-AS1 activity raises NABP1's level | lines that do not express PRKG2-AS1 (23) vs lines expressing it (27) | 1.64× lower at baseline in the lines without PRKG2-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent |
| [[HRH1]] | B | HRH1 activity raises NABP1's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 2.32× lower at baseline in the lines without HRH1 | 0.075 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[C3orf52]] | B | C3orf52 activity raises NABP1's level | lines that do not express C3orf52 (6) vs lines expressing it (44) | 3.04× lower at baseline in the lines without C3orf52 | 0.081 | ⚠ within organs, on part of the lines; also absent: HTATIP2, TBILA, ISG20; maybe low, not absent; its own permutation p |
| [[KCNQ3]] | B | KCNQ3 activity raises NABP1's level | lines that do not express KCNQ3 (26) vs lines expressing it (24) | 1.74× lower at baseline in the lines without KCNQ3 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000236212, LINC02360, SLITRK4 |
| [[RND3]] | B | RND3 activity raises NABP1's level | lines that do not express RND3 (5) vs lines expressing it (45) | 2.58× lower at baseline in the lines without RND3 | 0.089 | ⚠ within organs, on part of the lines; also absent: GULP1, SFXN3, GALNT7; its own permutation p |
| [[MAST4]] | B | MAST4 activity raises NABP1's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 1.92× lower at baseline in the lines without MAST4 | 0.091 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[BMAL2]] | B | BMAL2 activity raises NABP1's level | lines that do not express BMAL2 (7) vs lines expressing it (43) | 2.32× lower at baseline in the lines without BMAL2 | 0.092 | ⚠ within organs, on part of the lines; also absent: SMCO2, STXBP2, PDLIM1; maybe low, not absent |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 0, C 15. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSF2]] | C | NABP1 activity lowers HSF2's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 3.00× higher at baseline in the lines without NABP1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent; its own permutation p |
| [[CDKN1A]] | C | NABP1 activity raises CDKN1A's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 2.94× lower at baseline in the lines without NABP1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent; its own permutation p |
| [[S100A11]] | C | NABP1 activity raises S100A11's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 2.52× lower at baseline in the lines without NABP1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent; its own permutation p |
| [[BLZF2P]] | C | NABP1 activity raises BLZF2P's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 2.42× lower at baseline in the lines without NABP1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent; co-absent with the target; its own permutation p |
| [[ITGA2-AS1]] | C | NABP1 activity raises ITGA2-AS1's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 2.37× lower at baseline in the lines without NABP1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent; co-absent with the target; its own permutation p |
| [[NAA16]] | C | NABP1 activity lowers NAA16's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 2.14× higher at baseline in the lines without NABP1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent; its own permutation p |
| [[MAZ]] | C | NABP1 activity lowers MAZ's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 1.58× higher at baseline in the lines without NABP1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent; its own permutation p |
| [[SOWAHC]] | C | NABP1 activity raises SOWAHC's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 2.44× lower at baseline in the lines without NABP1 | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent |
| [[TM4SF1-AS1]] | C | NABP1 activity raises TM4SF1-AS1's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 2.01× lower at baseline in the lines without NABP1 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent |
| [[HRH1]] | C | NABP1 activity raises HRH1's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 5.56× lower at baseline in the lines without NABP1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent; its own permutation p |
| [[C11orf91]] | C | NABP1 activity raises C11orf91's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 2.93× lower at baseline in the lines without NABP1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent; its own permutation p |
| [[PPIEL-1]] | C | NABP1 activity raises PPIEL-1's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 1.77× lower at baseline in the lines without NABP1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.5, -0.2); signed map (4.6, 31.1). **Vector** length 160, 58.4% of its response variance represented; |z| ≥ 3 in 1,419 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.8 | +11.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +8.1 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.4 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.9 | +8.6 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +6.5 | +4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.1 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.1 | +4.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +5.0 | +1.7 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -10.1 | -8.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.7 | -5.7 |
|  | [[NG25 (drug)]] 5 µM |  | -6.5 | -5.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -6.3 | -5.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -6.0 | -4.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -5.2 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | nucleic acid binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.3 — chr2:191,678,068-191,741,097 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22833, DKFZp667M1322, FLJ13624, MGC111163, SSB2, hSSB2, SOSS-B2; previously OBFC2A, NABP1-OT1 |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, ADIPOGENESIS |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AH0](https://www.uniprot.org/uniprotkb/Q96AH0) (SOSS complex subunit B2):

> Component of the SOSS complex, a multiprotein complex that functions downstream of the MRN complex to promote DNA repair and G2/M checkpoint. In the SOSS complex, acts as a sensor of single-stranded DNA that binds to single-stranded DNA, in particular to polypyrimidines. The SOSS complex associates with DNA lesions and influences diverse endpoints in the cellular DNA damage response including cell-cycle checkpoint activation, recombinational repair and maintenance of genomic stability. Required …

**Summary**, from NCBI Gene [64859](https://www.ncbi.nlm.nih.gov/gene/64859):

> Single-stranded DNA (ssDNA)-binding proteins, such as OBFC2A, are ubiquitous and essential for a variety of DNA metabolic processes, including replication, recombination, and detection and repair of damage (Richard et al., 2008 [PubMed 18449195]).[supplied by OMIM, Jun 2008]

**Accessions** — [HGNC:26232](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26232) · Entrez [64859](https://www.ncbi.nlm.nih.gov/gene/64859) · UniProt [Q96AH0](https://www.uniprot.org/uniprotkb/Q96AH0) · Ensembl [ENSG00000173559](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173559)

## Data

Gene col 10404: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10404); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10404, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10404]; `tensor/DDL_lfc|DDL_z.npy` [10404]; `embed/gene_vectors.npy` [10404]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10404 or target_col == 10404). Every well: [[NABP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NABP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
