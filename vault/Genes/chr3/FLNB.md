---
symbol: "FLNB"
type: "gene"
col: 5809
ensembl_id: "ENSG00000136068"
name: "filamin B"
location: "3p14.3"
module: 136
arm: "+"
pooled_cpm: 682.7
n_lines_expressing: 47
n_dd_up: 8
n_dd_down: 33
n_dd_up_clean: 7
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 19
direction_downstream: 14
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# FLNB

*filamin B* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.40× (z +9.6, q 3e-19, up in 34 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.275× (z -36.5, q 0e+00, down in 46 of 46 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLNB-AS1]] (+0.78, fdr 7e-06, ⚠ same locus), [[LRRFIP1]] (+0.74, fdr 7e-06), [[PAQR5]] (+0.72, fdr 7e-06), [[ZFYVE28]] (+0.68, fdr 1e-05); moves opposite to [[AHI1-DT]] (-0.67, fdr 3e-04), [[GALNT7-DT]] (-0.65, fdr 5e-04), [[TTC32]] (-0.64, fdr 2e-04).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 14 go from it, the strongest it → [[TNIK]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5809.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +9.6 | 3e-19 | 34/45 (SW1417, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +6.8 | 4e-09 | 26/45 (hTERT-HPNE, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +6.6 | 1e-08 | 36/46 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +5.4 | 8e-06 | 26/45 (LOX-IMVI, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.30×** | +5.2 | 2e-05 | 24/45 (hTERT-HPNE, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.52×** | +4.4 | 1e-03 | 31/45 (SW480, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.24×** | +4.3 | 0.001 | 24/45 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.23×** | +4.2 | 0.002 | 21/44 (HOP62, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.6 | 0.020 | 17/46 (CHP-212, SW480, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.074 | 17/45 (AsPC-1, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Neratinib (drug)]] 5 µM |  | 1.17× | +3.2 | 0.080 | 19/45 (NCI-H460, SW48, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.17× | +3.1 | 0.088 | 18/44 (NCI-H1573, HepG2/C3A, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5809.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.275×** | -36.5 | 0e+00 | 46/46 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.412×** | -25.1 | 0e+00 | 41/45 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.373×** | -19.0 | 0e+00 | 42/45 (C32, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.395×** | -17.9 | 0e+00 | 39/44 (J82, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.439×** | -16.5 | 0e+00 | 41/45 (SK-MEL-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.459×** | -15.0 | 0e+00 | 41/45 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.561×** | -11.1 | 9e-27 | 38/47 (C32, KATO III, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.703×** | -9.9 | 2e-21 | 36/45 (SNU-1, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.611×** | -9.8 | 5e-21 | 40/45 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.715×** | -9.5 | 2e-19 | 35/45 (A549, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.633×** | -8.5 | 1e-15 | 32/42 (J82, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.670×** | -8.0 | 5e-14 | 32/45 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.696×** | -7.2 | 2e-11 | 31/45 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.723×** | -6.5 | 3e-09 | 26/45 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.731×** | -6.3 | 1e-08 | 29/45 (LoVo, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.733×** | -6.2 | 2e-08 | 26/45 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.748×** | -5.8 | 2e-07 | 32/45 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Amsacrine (drug)]] 5 µM |  | **0.817×** | -5.7 | 4e-07 | 27/45 (A549, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5809. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 1,503 | 0 | 28 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.106× (z -35.5) |
| [[RKO (line)]] | wt | 878 | 0 | 25 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -24.6) |
| [[AsPC-1 (line)]] | alt | 2,456 | 0 | 24 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0953× (z -39.8) |
| [[HOP62 (line)]] | alt | 872 | 0 | 23 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -31.1) |
| [[KATO III (line)]] | alt | 893 | 0 | 23 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -33.9) |
| [[J82 (line)]] | alt | 1,201 | 0 | 21 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -35.8) |
| [[SW480 (line)]] | alt | 440 | 5 (2 ⚠) | 14 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.75× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.73× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -24.7) |
| [[A-172 (line)]] | wt | 1,061 | 0 | 17 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -26.6) |
| [[C32 (line)]] | wt | 572 | 0 | 17 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -31.7) |
| [[A549 (line)]] | wt | 993 | 0 | 15 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -40.2) |
| [[HS-578T (line)]] | alt | 352 | 2 | 13 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.17× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -24.6) |
| [[SK-MEL-2 (line)]] | alt | 584 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -35.7) |
| [[SNU-1 (line)]] | wt | 1,155 | 1 | 14 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.90× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -34.8) |
| [[RPMI-7951 (line)]] | alt | 647 | 0 | 14 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -29.5) |
| [[H4 (line)]] | wt | 344 | 1 | 12 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.07× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -25.3) |
| [[Hs 766T (line)]] | wt | 2,614 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0996× (z -38.1) |
| [[MIA PaCa-2 (line)]] | alt | 603 | 4 | 8 (1 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 2.18× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -30.4) |
| [[NCI-H460 (line)]] | wt | 678 | 0 | 12 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -32.1) |
| [[SNU-423 (line)]] | alt | 781 | 1 | 11 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.56× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -23.8) |
| [[PANC-1 (line)]] | alt | 381 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -28.1) |
| [[HepG2_C3A (line)]] | wt | 702 | 1 (1 ⚠) | 7 (3 ⚠) | [[Daptomycin (drug)]] 5 µM 1.81× (z +8.9) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -29.5) |
| [[LOX-IMVI (line)]] | wt | 292 | 6 | 2 | [[Panobinostat (drug)]] 5 µM 3.20× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -12.3) |
| [[LS 180 (line)]] | wt | 976 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -29.2) |
| [[NCI-H1573 (line)]] | alt | 376 | 1 (1 ⚠) | 7 (3 ⚠) | [[Daptomycin (drug)]] 5 µM 1.97× (z +8.7) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -19.0) |
| [[NCI-H2030 (line)]] | alt | 586 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -23.7) |
| [[SW 900 (line)]] | alt | 289 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -17.8) |
| [[BT-474 (line)]] | alt | 283 | 2 | 4 | [[Tucidinostat (drug)]] 5 µM 1.88× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -18.1) |
| [[CFPAC-1 (line)]] | alt | 792 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -22.1) |
| [[HEC-1-A (line)]] | alt | 925 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -29.6) |
| [[NCI-H2347 (line)]] | alt | 691 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -19.6) |
| [[SW1417 (line)]] | alt | 261 | 4 | 2 | [[Tucidinostat (drug)]] 5 µM 1.96× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -25.3) |
| [[hTERT-HPNE (line)]] | wt | 194 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 4.87× (z +15.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 579 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -24.7) |
| [[Panc 03.27 (line)]] | alt | 592 | 1 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.93× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -27.3) |
| [[A498 (line)]] | wt | 268 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -20.0) |
| [[CHP-212 (line)]] | wt | 293 | 1 | 3 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.74× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -22.2) |
| [[HCT15 (line)]] | alt | 476 | 1 | 3 | [[Tucidinostat (drug)]] 5 µM 2.09× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -18.9) |
| [[AN3 CA (line)]] | alt | 363 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -14.1) |
| [[C-33 A (line)]] | alt | 191 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -11.4) |
| [[HT-29 (line)]] | alt | 379 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -22.0) |
| [[COLO 205 (line)]] | alt | 189 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -12.6) |
| [[SW 1088 (line)]] | alt | 270 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -9.0) |
| [[SW 1271 (line)]] | alt | 589 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -17.9) |
| [[SW48 (line)]] | wt | 188 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.59× (z +9.7) | — |
| [[A-427 (line)]] | wt | 92.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 500 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 156 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 562 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 165 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5809), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLNB-AS1]] | +0.78 | +0.74 / +0.71 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[LRRFIP1]] | +0.74 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[PAQR5]] | +0.72 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[ZFYVE28]] | +0.68 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[SERPINB1]] | +0.68 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[LANCL3]] | +0.68 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[DGKD]] | +0.68 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[EHD4]] | +0.68 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[HK1]] | +0.67 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[NIBAN2]] | +0.67 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[PBX4]] | +0.67 | +0.61 / +0.36 | both halves | 1e-04 |  |
| [[HPCAL1]] | +0.66 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[SPTLC2]] | +0.66 | +0.58 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHI1-DT]] | -0.67 | -0.66 / -0.27 | both halves | 3e-04 |  |
| [[GALNT7-DT]] | -0.65 | -0.63 / -0.24 | both halves | 5e-04 |  |
| [[TTC32]] | -0.64 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[EFCAB2]] | -0.62 | -0.56 / -0.27 | both halves | 3e-04 |  |
| [[RNF146]] | -0.62 | -0.60 / -0.26 | both halves | 4e-04 |  |
| [[MR1]] | -0.61 | -0.61 / -0.20 | both halves | 7e-04 |  |
| [[CREBBP]] | -0.60 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[HOXB7]] | -0.60 | -0.52 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[OXA1L-DT]] | -0.60 | -0.56 / -0.22 | both halves | 6e-04 |  |
| [[KANSL1L]] | -0.60 | -0.61 / -0.21 | both halves | 7e-04 |  |
| [[DNAI4]] | -0.59 | -0.59 / -0.24 | both halves | 5e-04 |  |
| [[C11orf52]] | -0.59 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[MAIP1]] | -0.59 | -0.54 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 17, C 2. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FLNB's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.2% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[SERPINB1]] | B | SERPINB1 activity raises FLNB's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 2.46× lower at baseline in the lines without SERPINB1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[SLCO4A1]] | B | SLCO4A1 activity raises FLNB's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 2.26× lower at baseline in the lines without SLCO4A1 | 0.012 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[S100A16]] | B | S100A16 activity raises FLNB's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 2.12× lower at baseline in the lines without S100A16 | 0.014 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[PLEK2]] | B | PLEK2 activity raises FLNB's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 1.59× lower at baseline in the lines without PLEK2 | 0.027 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[PROSER2]] | B | PROSER2 activity raises FLNB's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 1.84× lower at baseline in the lines without PROSER2 | 0.028 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |
| [[TOR4A]] | B | TOR4A activity raises FLNB's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 1.87× lower at baseline in the lines without TOR4A | 0.032 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[SYT11]] | B | SYT11 activity lowers FLNB's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 1.80× higher at baseline in the lines without SYT11 | 0.037 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1 |
| [[ENPEP]] | B | ENPEP activity lowers FLNB's level | lines that do not express ENPEP (25) vs lines expressing it (25) | 1.77× higher at baseline in the lines without ENPEP | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC02253, KCNE3, ENSG00000265554; maybe low, not absent |
| [[F3]] | B | F3 activity raises FLNB's level | lines that do not express F3 (24) vs lines expressing it (26) | 1.80× lower at baseline in the lines without F3 | 0.053 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[GPRC5A]] | B | GPRC5A activity raises FLNB's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without GPRC5A | 0.062 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[TNIK]] | B | TNIK activity raises FLNB's level | lines that do not express TNIK (11) vs lines expressing it (39) | 1.50× lower at baseline in the lines without TNIK | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, FUT2, PTPRE |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 0, C 14. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNIK]] | C | FLNB activity raises TNIK's level | lines that do not express FLNB (3) vs lines expressing it (47) | 7.10× lower at baseline in the lines without FLNB | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |
| [[PAG1]] | C | FLNB activity raises PAG1's level | lines that do not express FLNB (3) vs lines expressing it (47) | 4.55× lower at baseline in the lines without FLNB | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |
| [[ATP2B4]] | C | FLNB activity raises ATP2B4's level | lines that do not express FLNB (3) vs lines expressing it (47) | 4.08× lower at baseline in the lines without FLNB | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |
| [[TOR4A]] | C | FLNB activity raises TOR4A's level | lines that do not express FLNB (3) vs lines expressing it (47) | 3.43× lower at baseline in the lines without FLNB | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |
| [[AFAP1]] | C | FLNB activity raises AFAP1's level | lines that do not express FLNB (3) vs lines expressing it (47) | 3.40× lower at baseline in the lines without FLNB | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |
| [[AKAP13]] | C | FLNB activity raises AKAP13's level | lines that do not express FLNB (3) vs lines expressing it (47) | 1.74× lower at baseline in the lines without FLNB | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |
| [[MR1]] | C | FLNB activity raises MR1's level | lines that do not express FLNB (3) vs lines expressing it (47) | 1.77× lower at baseline in the lines without FLNB | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent |
| [[PORCN]] | C | FLNB activity raises PORCN's level | lines that do not express FLNB (3) vs lines expressing it (47) | 2.15× lower at baseline in the lines without FLNB | 0.086 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent |
| [[S100A16]] | C | FLNB activity raises S100A16's level | lines that do not express FLNB (3) vs lines expressing it (47) | 7.87× lower at baseline in the lines without FLNB | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |
| [[GPRC5A]] | C | FLNB activity raises GPRC5A's level | lines that do not express FLNB (3) vs lines expressing it (47) | 4.17× lower at baseline in the lines without FLNB | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |
| [[ANXA2]] | C | FLNB activity raises ANXA2's level | lines that do not express FLNB (3) vs lines expressing it (47) | 2.80× lower at baseline in the lines without FLNB | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |
| [[EHD4]] | C | FLNB activity raises EHD4's level | lines that do not express FLNB (3) vs lines expressing it (47) | 2.04× lower at baseline in the lines without FLNB | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.7, 5.6); signed map (-4.8, 44.9). **Vector** length 151, 57.1% of its response variance represented; |z| ≥ 3 in 2,270 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +14.3 | +6.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +14.1 | +5.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +13.0 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +12.8 | +9.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +8.5 | +1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +5.1 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.1 | +3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.6 | +4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.5 | +1.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -10.0 | -9.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.5 | -17.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.1 | -9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -36.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.8 | -9.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.8 | -6.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -6.4 | -4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.1 | -4.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.4 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | filamin B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:58,008,398-58,172,251 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAP, TABP, ABP-278, FH1; previously FLN1L, LRS1 |
| Gene groups (HGNC) | Filamin family |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY, MITOTIC_SPINDLE |
| Reactome | 4 pathways, smallest: ISG15 antiviral mechanism; Antimicrobial mechanism of IFN-stimulated genes; Interferon Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O75369](https://www.uniprot.org/uniprotkb/O75369) (Filamin-B):

> Connects cell membrane constituents to the actin cytoskeleton. May promote orthogonal branching of actin filaments and links actin filaments to membrane glycoproteins. Anchors various transmembrane proteins to the actin cytoskeleton. Interaction with FLNA may allow neuroblast migration from the ventricular zone into the cortical plate. Various interactions and localizations of isoforms affect myotube morphology and myogenesis. Isoform 6 accelerates muscle differentiation in vitro.

**Summary**, from NCBI Gene [2317](https://www.ncbi.nlm.nih.gov/gene/2317):

> This gene encodes a member of the filamin family. The encoded protein interacts with glycoprotein Ib alpha as part of the process to repair vascular injuries. The platelet glycoprotein Ib complex includes glycoprotein Ib alpha, and it binds the actin cytoskeleton. Mutations in this gene have been found in several conditions: atelosteogenesis type 1 and type 3; boomerang dysplasia; autosomal dominant Larsen syndrome; and spondylocarpotarsal synostosis syndrome. Multiple alternatively spliced …

**Accessions** — [HGNC:3755](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3755) · Entrez [2317](https://www.ncbi.nlm.nih.gov/gene/2317) · UniProt [O75369](https://www.uniprot.org/uniprotkb/O75369) · Ensembl [ENSG00000136068](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136068)

## Data

Gene col 5809: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5809); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5809, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5809]; `tensor/DDL_lfc|DDL_z.npy` [5809]; `embed/gene_vectors.npy` [5809]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5809 or target_col == 5809). Every well: [[FLNB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLNB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
