---
symbol: "TBC1D8"
type: "gene"
col: 12908
ensembl_id: "ENSG00000204634"
name: "TBC1 domain family member 8"
location: "2q11.2"
module: 97
arm: "+"
pooled_cpm: 317.76
n_lines_expressing: 44
n_dd_up: 26
n_dd_down: 49
n_dd_up_clean: 24
n_dd_down_clean: 40
in_vector_space: true
direction_upstream: 22
direction_downstream: 40
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# TBC1D8

*TBC1 domain family member 8* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (2 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.5 µM: 1.59× (z +8.3, q 5e-14, up in 32 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 49 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.394× (z -15.9, q 0e+00, down in 39 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPN12]] (+0.70, fdr 7e-06), [[AKAP13]] (+0.70, fdr 7e-06), [[HPCAL1]] (+0.67, fdr 7e-06); moves opposite to [[BBOX1-AS1]] (-0.59, fdr 1e-05), [[LINC02100]] (-0.57, fdr 2e-05), [[ZSCAN31]] (-0.54, fdr 3e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[DIO3OS]] → it (grade B ⚠); 40 go from it, the strongest it → [[OSBPL8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12908.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.59×** | +8.3 | 5e-14 | 32/42 (NCI-H1573, RPMI-7951, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.59×** | +8.2 | 5e-14 | 33/44 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.58×** | +8.2 | 6e-14 | 29/42 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +7.7 | 2e-12 | 24/42 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +7.5 | 1e-11 | 21/42 (J82, NCI-H23, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.45×** | +6.6 | 3e-09 | 26/42 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.43×** | +6.4 | 2e-08 | 25/42 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.42×** | +6.2 | 3e-08 | 24/42 (RPMI-7951, HS-578T, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.41×** | +6.2 | 4e-08 | 24/42 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.41×** | +6.0 | 1e-07 | 24/43 (NCI-H1573, J82, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.38×** | +5.8 | 3e-07 | 25/42 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.38×** | +5.7 | 5e-07 | 26/42 (HS-578T, NCI-H1573, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.44×** | +5.7 | 5e-07 | 24/41 (NCI-H1573, RPMI-7951, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.36×** | +5.5 | 2e-06 | 23/42 (NCI-H1573, RPMI-7951, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +5.4 | 3e-06 | 19/42 (NCI-H23, HS-578T, …) | all doses, stronger at high dose |  |
| [[Econazole (drug)]] 5 µM |  | **1.34×** | +5.3 | 5e-06 | 27/42 (NCI-H1573, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 49 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12908.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.394×** | -15.9 | 0e+00 | 39/42 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.534×** | -15.8 | 0e+00 | 35/42 (NCI-H2030, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.440×** | -14.6 | 0e+00 | 38/42 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.388×** | -12.3 | 1e-32 | 40/42 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.543×** | -10.4 | 2e-23 | 31/39 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.666×** | -10.2 | 2e-22 | 27/43 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.613×** | -8.7 | 3e-16 | 36/42 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.585×** | -8.3 | 9e-15 | 33/39 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.638×** | -8.0 | 9e-14 | 34/42 (AsPC-1, SW 900, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.662×** | -7.3 | 1e-11 | 36/42 (NCI-H2030, LoVo, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **0.695×** | -7.3 | 1e-11 | 34/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.667×** | -7.2 | 3e-11 | 34/42 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.463×** | -7.2 | 3e-11 | 30/43 (SK-MEL-2, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.660×** | -7.1 | 5e-11 | 31/41 (HepG2/C3A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.672×** | -7.1 | 6e-11 | 29/42 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.684×** | -6.7 | 6e-10 | 34/42 (NCI-H460, HepG2/C3A, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.493×** | -6.6 | 2e-09 | 31/42 (AsPC-1, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.694×** | -6.5 | 3e-09 | 29/42 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **0.728×** | -6.2 | 1e-08 | 30/43 (NCI-H460, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.717×** | -6.1 | 3e-08 | 32/42 (NCI-H460, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12908. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 385 | 19 | 8 (1 ⚠) | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 3.73× (z +13.2) | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -23.0) |
| [[NCI-H460 (line)]] | wt | 586 | 0 | 27 (7 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.141× (z -19.7) |
| [[SK-MEL-2 (line)]] | alt | 196 | 11 | 11 (3 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.55× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.188× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.195× (z -18.0) |
| [[PANC-1 (line)]] | alt | 729 | 0 | 19 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -24.4) |
| [[HS-578T (line)]] | alt | 121 | 18 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 3.33× (z +11.9) | — |
| [[RPMI-7951 (line)]] | alt | 164 | 16 | 2 | [[Clobetasol propionate (drug)]] 0.05 µM 3.68× (z +11.3) | [[Harringtonine (drug)]] 5 µM 0.242× (z -11.8) |
| [[A549 (line)]] | wt | 806 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -29.4) |
| [[AsPC-1 (line)]] | alt | 563 | 0 | 14 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.224× (z -18.3) |
| [[NCI-H2030 (line)]] | alt | 778 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -31.6) |
| [[J82 (line)]] | alt | 118 | 12 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 2.91× (z +11.4) | — |
| [[LoVo (line)]] | wt | 630 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -18.0) |
| [[HepG2_C3A (line)]] | wt | 623 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -23.1) |
| [[SW 900 (line)]] | alt | 575 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -15.2) |
| [[A-172 (line)]] | wt | 138 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.281× (z -12.8) |
| [[HEC-1-A (line)]] | alt | 230 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.515× (z -11.7) |
| [[SW480 (line)]] | alt | 388 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 344 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -11.7) |
| [[HOP62 (line)]] | alt | 135 | 1 | 4 (1 ⚠) | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 2.38× (z +8.8) | [[Harringtonine (drug)]] 5 µM 0.241× (z -13.9) |
| [[HT-29 (line)]] | alt | 338 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -10.7) |
| [[KATO III (line)]] | alt | 180 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -12.6) |
| [[LS 180 (line)]] | wt | 303 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 405 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 118 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.17× (z +8.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.418× (z -9.7) |
| [[SW1417 (line)]] | alt | 341 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -12.3) |
| [[C32 (line)]] | wt | 172 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.386× (z -9.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 314 | 1 (1 ⚠) | 2 | [[Selinexor (drug)]] 5 µM 2.12× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.310× (z -13.2) |
| [[NCI-H23 (line)]] | alt | 113 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.149× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 266 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.331× (z -10.8) |
| [[SNU-423 (line)]] | alt | 254 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -16.3) |
| [[Hs 766T (line)]] | wt | 298 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -12.1) |
| [[SW 1271 (line)]] | alt | 429 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -8.9) |
| [[SW48 (line)]] | wt | 116 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.304× (z -10.3) |
| [[BT-474 (line)]] | alt | 325 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -10.8) |
| [[H4 (line)]] | wt | 164 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -8.7) |
| [[HCT15 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -10.6) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 218 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.05 µM 0.133× (z -8.6) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 58.8 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 168 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 106 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 72.2 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 62.8 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 69.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.7 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 63.8 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 90.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12908), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPN12]] | +0.70 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[AKAP13]] | +0.70 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[HPCAL1]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[TOP1]] | +0.67 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[PACSIN2]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[KIF13B]] | +0.64 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[LINC02320]] | +0.63 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[PKP2]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[STN1]] | +0.63 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TMEM164]] | +0.62 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[MT2A]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[NCOA3]] | +0.61 | +0.63 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBOX1-AS1]] | -0.59 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[LINC02100]] | -0.57 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[ZSCAN31]] | -0.54 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[SLAMF7]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[ZBTB21]] | -0.53 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[GPR158]] | -0.53 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[OTUD7B]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[TBC1D22B]] | -0.52 | -0.50 / -0.43 | both halves | 3e-05 | same gene group; STRING 516 |
| [[BLTP3B]] | -0.52 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[RASGRP1]] | -0.52 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[NEURL3]] | -0.51 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[DRAM1]] | -0.50 | -0.49 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 22, C 0. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIO3OS]] | B | DIO3OS activity raises TBC1D8's level | lines that do not express DIO3OS (25) vs lines expressing it (25) | 2.56× lower at baseline in the lines without DIO3OS | 5e-04 | ⚠ within organs, on part of the lines; also absent: NPSR1-AS1, ENSG00000258919, TOX3 |
| [[ABCC3]] | B | ABCC3 activity raises TBC1D8's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.55× lower at baseline in the lines without ABCC3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[PPARG]] | B | PPARG activity raises TBC1D8's level | lines that do not express PPARG (20) vs lines expressing it (30) | 2.30× lower at baseline in the lines without PPARG | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[TGFBR2]] | B | TGFBR2 activity raises TBC1D8's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 2.90× lower at baseline in the lines without TGFBR2 | 0.008 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[EPAS1]] | B | EPAS1 activity raises TBC1D8's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 2.48× lower at baseline in the lines without EPAS1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[S100P]] | B | S100P activity raises TBC1D8's level | lines that do not express S100P (34) vs lines expressing it (16) | 2.27× lower at baseline in the lines without S100P | 0.012 | ⚠ within organs, on part of the lines; also absent: POF1B, ENSG00000287426, CEACAM6 |
| [[NEURL3]] | B | NEURL3 activity raises TBC1D8's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 2.32× lower at baseline in the lines without NEURL3 | 0.012 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[MYO1E]] | B | MYO1E activity raises TBC1D8's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 2.59× lower at baseline in the lines without MYO1E | 0.016 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[LAMA3]] | B | LAMA3 activity raises TBC1D8's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.00× lower at baseline in the lines without LAMA3 | 0.023 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[TNS4]] | B | TNS4 activity raises TBC1D8's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 2.14× lower at baseline in the lines without TNS4 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[EVA1C]] | B | EVA1C activity raises TBC1D8's level | lines that do not express EVA1C (15) vs lines expressing it (35) | 1.90× lower at baseline in the lines without EVA1C | 0.030 | ⚠ within organs, on part of the lines; also absent: PI3, ENSG00000260877, CYB5R2 |
| [[DIO3OS]] | B | DIO3OS activity strengthens TBC1D8's drug response | lines that do not express DIO3OS (20) vs lines expressing it (24) | the lines without DIO3OS respond 0.76× as strongly (z diff +1.81); strongest at Idarubicin (hydrochloride) 5 µM: 0.88x vs 0.51x (z diff +5.5) | 0.032 | ⚠ within organs, on part of the lines; also absent: NPSR1-AS1, ENSG00000258919, TOX3; target measured in part of the lines; artifact flags |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 40, C 0. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSBPL8]] | B | TBC1D8 activity lowers OSBPL8's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 1.63× higher at baseline in the lines without TBC1D8 | 0.002 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[ABCC3]] | B | TBC1D8 activity raises ABCC3's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 5.83× lower at baseline in the lines without TBC1D8 | 0.002 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[AKAP13]] | B | TBC1D8 activity raises AKAP13's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 1.53× lower at baseline in the lines without TBC1D8 | 0.005 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[RPS6KA2]] | B | TBC1D8 activity raises RPS6KA2's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 3.08× lower at baseline in the lines without TBC1D8 | 0.007 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[ESYT2]] | B | TBC1D8 activity raises ESYT2's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 1.78× lower at baseline in the lines without TBC1D8 | 0.011 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[ABLIM3]] | B | TBC1D8 activity raises ABLIM3's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 3.43× lower at baseline in the lines without TBC1D8 | 0.012 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[PPP3CA]] | B | TBC1D8 activity raises PPP3CA's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 2.22× lower at baseline in the lines without TBC1D8 | 0.012 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[DENND3]] | B | TBC1D8 activity raises DENND3's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 1.98× lower at baseline in the lines without TBC1D8 | 0.014 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[ANKRD30A]] | B | TBC1D8 activity lowers ANKRD30A's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 3.41× higher at baseline in the lines without TBC1D8 | 0.017 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[EPAS1]] | B | TBC1D8 activity raises EPAS1's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 3.82× lower at baseline in the lines without TBC1D8 | 0.017 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[ITGB5]] | B | TBC1D8 activity raises ITGB5's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 1.83× lower at baseline in the lines without TBC1D8 | 0.019 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[ROR1]] | B | TBC1D8 activity raises ROR1's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 3.78× lower at baseline in the lines without TBC1D8 | 0.019 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.834). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.5, 12.4); signed map (12.5, 33.7). **Vector** length 146, 52.4% of its response variance represented; |z| ≥ 3 in 2,102 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Budesonide (drug)]] 0.05 µM |  | +6.5 | +6.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +6.4 | +6.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.9 | +8.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +5.8 | +6.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.7 | +7.7 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | +5.7 | +5.5 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -11.3 | -5.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -9.6 | -7.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -8.6 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -8.6 | -5.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -8.5 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.8 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:101,007,228-101,252,866 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HBLP1, VRP, AD3, GRAMD8 |
| Gene groups (HGNC) | GRAM domain containing; TBC1 domain family members |
| Matched by | ensembl_id |

**Function**, from UniProt [O95759](https://www.uniprot.org/uniprotkb/O95759) (TBC1 domain family member 8):

> May act as a GTPase-activating protein for Rab family protein(s).

**Summary**, from NCBI Gene [11138](https://www.ncbi.nlm.nih.gov/gene/11138):

> Predicted to enable GTPase activator activity. Predicted to be involved in blood circulation and positive regulation of cell population proliferation. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17791](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17791) · Entrez [11138](https://www.ncbi.nlm.nih.gov/gene/11138) · UniProt [O95759](https://www.uniprot.org/uniprotkb/O95759) · Ensembl [ENSG00000204634](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204634)

## Data

Gene col 12908: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12908); `tables/drug_effects.parquet` (84 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12908, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12908]; `tensor/DDL_lfc|DDL_z.npy` [12908]; `embed/gene_vectors.npy` [12908]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12908 or target_col == 12908). Every well: [[TBC1D8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
