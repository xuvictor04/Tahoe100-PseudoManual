---
symbol: "ERCC6L2"
type: "gene"
col: 11247
ensembl_id: "ENSG00000182150"
name: "ERCC excision repair 6 like 2"
location: "9q22.32"
module: 30
arm: "-"
pooled_cpm: 139.14
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# ERCC6L2

*ERCC excision repair 6 like 2* — 9q22.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.52× (z +25.8, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.535× (z -12.3, q 3e-32, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WARS2-AS1]] (+0.80, fdr 1e-05), [[ST7L]] (+0.80, fdr 7e-06), [[MED1]] (+0.73, fdr 7e-06); moves opposite to [[SDHAP4]] (-0.75, fdr 7e-06), [[SDHAP1]] (-0.75, fdr 7e-06), [[ANKRD27]] (-0.74, fdr 1e-05).
> It sits in the **-** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SPINT2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11247.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.52×** | +25.8 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.28×** | +16.3 | 0e+00 | 47/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.76×** | +10.7 | 1e-24 | 43/48 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +8.3 | 1e-14 | 38/48 (HCT15, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +5.6 | 2e-06 | 30/48 (BT-474, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.9 | 1e-04 | 28/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.2 | 0.002 | 27/48 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.24×** | +4.2 | 0.002 | 26/48 (LoVo, H4, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +4.0 | 0.004 | 25/48 (BT-474, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.11 | 10/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11247.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.535×** | -12.3 | 3e-32 | 44/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.565×** | -11.3 | 6e-27 | 42/48 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.573×** | -11.0 | 7e-26 | 43/48 (RKO, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.657×** | -8.0 | 2e-13 | 35/47 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.669×** | -7.6 | 3e-12 | 29/44 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.706×** | -6.9 | 6e-10 | 38/48 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.719×** | -6.5 | 6e-09 | 35/48 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.737×** | -5.9 | 3e-07 | 30/49 (C-33 A, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.748×** | -5.7 | 7e-07 | 29/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.754×** | -5.1 | 2e-05 | 27/45 (A-172, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **0.785×** | -4.8 | 9e-05 | 32/48 (Hs 766T, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 0.853× | -4.4 | 5e-04 | 17/48 (RKO, SK-MEL-2, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.664×** | -4.2 | 0.001 | 31/49 (SK-MEL-2, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.691×** | -3.8 | 0.005 | 23/49 (SNU-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.850× | -3.2 | 0.052 | 19/48 (SK-MEL-2, SW 900, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.892× | -3.2 | 0.052 | 12/49 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.799×** | -3.2 | 0.052 | 24/48 (NCI-H1792, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.852× | -3.0 | 0.075 | 20/48 (J82, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11247. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 212 | 3 (1 ⚠) | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.393× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 182 | 4 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +29.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.367× (z -16.0) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.504× (z -11.4) |
| [[RKO (line)]] | wt | 273 | 1 | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -12.7) |
| [[SW480 (line)]] | alt | 195 | 2 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +19.8) | [[Belinostat (drug)]] 5 µM 0.489× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 214 | 3 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +19.5) | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.442× (z -10.0) |
| [[A-172 (line)]] | wt | 214 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +23.3) | [[Dinaciclib (drug)]] 0.05 µM 0.468× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 145 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +19.6) | [[Dinaciclib (drug)]] 5 µM 0.171× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.469× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 193 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.330× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 157 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +22.8) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.399× (z -11.8) |
| [[PANC-1 (line)]] | alt | 127 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +26.0) | [[Belinostat (drug)]] 5 µM 0.408× (z -12.0) |
| [[A-427 (line)]] | wt | 85.1 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.98× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -23.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.436× (z -9.9) |
| [[BT-474 (line)]] | alt | 89.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.8) | — |
| [[HCT15 (line)]] | alt | 169 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +19.6) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.458× (z -9.1) |
| [[HT-29 (line)]] | alt | 115 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.478× (z -9.7) |
| [[C32 (line)]] | wt | 123 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +20.4) | — |
| [[COLO 205 (line)]] | alt | 130 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.390× (z -10.2) |
| [[LoVo (line)]] | wt | 126 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +21.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.431× (z -12.0) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 84.2 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.2) | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 101 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +12.8) | — |
| [[hTERT-HPNE (line)]] | wt | 109 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +13.3) | [[Belinostat (drug)]] 5 µM 0.414× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 51.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +19.8) | — |
| [[SK-MEL-2 (line)]] | alt | 156 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +21.1) | — |
| [[SNU-1 (line)]] | wt | 207 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.04× (z +14.2) | — |
| [[A498 (line)]] | wt | 120 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 64.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +14.1) | — |
| [[C-33 A (line)]] | alt | 227 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -23.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[CFPAC-1 (line)]] | alt | 46.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +18.6) | — |
| [[H4 (line)]] | wt | 148 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +15.7) | — |
| [[HEC-1-A (line)]] | alt | 179 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 153 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +19.4) | — |
| [[Hs 766T (line)]] | wt | 144 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +19.7) | — |
| [[HS-578T (line)]] | alt | 71.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +12.4) | — |
| [[KATO III (line)]] | alt | 151 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -12.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 120 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +8.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.455× (z -9.3) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 116 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +16.4) | — |
| [[SW 1271 (line)]] | alt | 379 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.327× (z -8.6) |
| [[SW 900 (line)]] | alt | 95.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +15.6) | — |
| [[A549 (line)]] | wt | 128 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +13.2) | — |
| [[AN3 CA (line)]] | alt | 139 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +9.9) | — |
| [[CHP-212 (line)]] | wt | 159 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -10.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 162 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +13.7) | — |
| [[NCI-H2030 (line)]] | alt | 74.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +15.9) | — |
| [[SNU-423 (line)]] | alt | 123 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +16.8) | — |
| [[SW1417 (line)]] | alt | 120 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.459× (z -8.6) |
| [[SW48 (line)]] | wt | 143 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.8) | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 121 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11247), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WARS2-AS1]] | +0.80 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[ST7L]] | +0.80 | +0.78 / +0.58 | both halves | 7e-06 |  |
| [[MED1]] | +0.73 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[ZBED5]] | +0.72 | +0.74 / +0.43 | both halves | 3e-05 |  |
| [[MSRA]] | +0.72 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[LZIC]] | +0.72 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[CPSF2]] | +0.71 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[BPTF]] | +0.70 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[ZNF764]] | +0.70 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[NEPRO-AS1]] | +0.70 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[ZNF518A]] | +0.70 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[SON]] | +0.69 | +0.69 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP4]] | -0.75 | -0.79 / -0.59 | both halves | 7e-06 |  |
| [[SDHAP1]] | -0.75 | -0.77 / -0.60 | both halves | 7e-06 |  |
| [[ANKRD27]] | -0.74 | -0.73 / -0.54 | both halves | 1e-05 |  |
| [[MYPOP]] | -0.74 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[SEC11A]] | -0.72 | -0.72 / -0.64 | both halves | 7e-06 |  |
| [[SLC9A6]] | -0.72 | -0.69 / -0.55 | both halves | 1e-05 |  |
| [[USP35]] | -0.72 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[STX7]] | -0.72 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[NTAN1]] | -0.71 | -0.72 / -0.56 | both halves | 1e-05 |  |
| [[TMEM185A]] | -0.71 | -0.72 / -0.58 | both halves | 7e-06 |  |
| [[STAM]] | -0.70 | -0.73 / -0.55 | both halves | 1e-05 |  |
| [[PAPSS1]] | -0.70 | -0.68 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPINT2]] | B | SPINT2 activity lowers ERCC6L2's level | lines that do not express SPINT2 (24) vs lines expressing it (26) | 1.39× higher at baseline in the lines without SPINT2 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, ENTPD2 |
| [[LINC02516]] | B | LINC02516 activity raises ERCC6L2's level | lines that do not express LINC02516 (19) vs lines expressing it (31) | 1.34× lower at baseline in the lines without LINC02516 | 0.050 | ⚠ within organs, on part of the lines; also absent: ADAM23, TEK, SPOCK3 |
| [[ZNF702P]] | B | ZNF702P activity lowers ERCC6L2's level | lines that do not express ZNF702P (24) vs lines expressing it (26) | 1.35× higher at baseline in the lines without ZNF702P | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, VGLL3, GPA33 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **-** arm (projection on the module's main direction -0.799). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.9, -5.7); signed map (17.6, -25.7). **Vector** length 145, 50.0% of its response variance represented; |z| ≥ 3 in 1,254 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +13.8 | +16.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +13.4 | +25.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +11.5 | +10.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +10.0 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.5 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.4 | +4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +1.7 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.8 | +2.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -9.3 | -12.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -8.0 | -6.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.4 | -11.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.3 | -11.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -7.0 | -6.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.3 | -4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.3 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.5 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | ERCC excision repair 6 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.32 — chr9:95,871,264-96,121,154 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37706, RAD26L, HEBO; previously C9orf102 |
| Gene groups (HGNC) | SNF2 related family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T890](https://www.uniprot.org/uniprotkb/Q5T890) (DNA excision repair protein ERCC-6-like 2):

> Promotes double-strand break (DSB) end-joining and facilitates programmed recombination by controlling how DNA ends are joined in a spatially oriented manner during repair (By similarity). Also plays a role in DNA repair by restricting DNA end resection in double strand break (DSB) repair. Facilitates replication of complex DNA regions and regulates the maintenance of chromatin structure.

**Summary**, from NCBI Gene [375748](https://www.ncbi.nlm.nih.gov/gene/375748):

> This gene encodes a member of the Snf2 family of helicase-like proteins. The encoded protein may play a role in DNA repair and mitochondrial function. Mutations in this gene have been associated with bone marrow failure syndrome 2. Alternatively spliced transcript variants that encode different protein isoforms have been described. [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:26922](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26922) · Entrez [375748](https://www.ncbi.nlm.nih.gov/gene/375748) · UniProt [Q5T890](https://www.uniprot.org/uniprotkb/Q5T890) · Ensembl [ENSG00000182150](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182150)

## Data

Gene col 11247: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11247); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11247, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11247]; `tensor/DDL_lfc|DDL_z.npy` [11247]; `embed/gene_vectors.npy` [11247]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11247 or target_col == 11247). Every well: [[ERCC6L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERCC6L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
