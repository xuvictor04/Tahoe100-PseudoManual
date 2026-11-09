---
symbol: "FRY"
type: "gene"
col: 1064
ensembl_id: "ENSG00000073910"
name: "FRY microtubule binding protein"
location: "13q13.1"
module: 97
arm: "+"
pooled_cpm: 70.77
n_lines_expressing: 36
n_dd_up: 23
n_dd_down: 46
n_dd_up_clean: 23
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# FRY

*FRY microtubule binding protein* — 13q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.49× (z +22.1, q 0e+00, up in 29 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 46 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.332× (z -18.8, q 0e+00, down in 32 of 34 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF13B]] (+0.58, fdr 4e-05), [[PKP2]] (+0.58, fdr 2e-05), [[NCOA3]] (+0.56, fdr 2e-05); moves opposite to [[SPRYD4]] (-0.52, fdr 7e-05), [[ANXA2R-OT1]] (-0.52, fdr 1e-04), [[THBS4]] (-0.52, fdr 2e-04).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[C2CD4A]] → it (grade B ⚠); 5 go from it, the strongest it → [[SERPINA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 1 with an alert ⚠; shown: the 15 strongest. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1064.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.49×** | +22.1 | 0e+00 | 29/34 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.30×** | +14.3 | 1e-43 | 29/34 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.26×** | +14.0 | 5e-42 | 32/35 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.19×** | +13.4 | 5e-39 | 24/34 (J82, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.15×** | +13.1 | 3e-37 | 25/34 (J82, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.93×** | +11.2 | 2e-27 | 22/34 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.56×** | +8.4 | 3e-15 | 22/35 (SW480, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.50×** | +7.0 | 2e-10 | 20/33 (HOP62, SW 900, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.50×** | +6.9 | 3e-10 | 19/33 (HOP62, SW 900, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.47×** | +6.4 | 8e-09 | 22/33 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.36×** | +5.3 | 5e-06 | 17/33 (NCI-H460, HOP62, …) | rises with dose | low cells (technical?) |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.28×** | +4.3 | 9e-04 | 12/36 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.001 | 14/34 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.002 | 12/34 (HOP62, SW 900, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.26×** | +4.0 | 0.002 | 14/34 (LS 180, BT-474, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 46 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1064.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.332×** | -18.8 | 0e+00 | 32/34 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.339×** | -18.4 | 0e+00 | 30/33 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.410×** | -15.2 | 0e+00 | 32/34 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.441×** | -13.9 | 6e-42 | 28/34 (SW 900, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.449×** | -13.6 | 5e-40 | 31/33 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.581×** | -13.0 | 8e-37 | 26/34 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.486×** | -12.3 | 1e-32 | 22/34 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.494×** | -12.0 | 3e-31 | 27/34 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.497×** | -11.4 | 2e-28 | 23/34 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.542×** | -10.4 | 1e-23 | 26/33 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.553×** | -10.1 | 4e-22 | 27/34 (SW 900, NCI-H1573, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.357×** | -9.2 | 2e-18 | 23/34 (HOP62, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.717×** | -8.0 | 7e-14 | 22/34 (CFPAC-1, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.631×** | -7.5 | 2e-12 | 23/33 (NCI-H23, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.731×** | -7.5 | 3e-12 | 21/35 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.469×** | -6.7 | 6e-10 | 22/35 (SHP-77, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.695×** | -6.2 | 2e-08 | 20/34 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.781×** | -5.9 | 1e-07 | 17/35 (CFPAC-1, SW 900, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1064. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 200 | 1 | 22 (11 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.21× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -21.2) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.0780× (z -20.5) |
| [[SW 900 (line)]] | alt | 270 | 1 | 20 (10 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.13× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -17.7) |
| [[NCI-H1573 (line)]] | alt | 351 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0312× (z -36.9) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0283× (z -26.8) |
| [[HT-29 (line)]] | alt | 666 | 0 | 17 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0766× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -19.2) |
| [[NCI-H23 (line)]] | alt | 95.2 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0501× (z -42.4) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0777× (z -24.6) |
| [[KATO III (line)]] | alt | 102 | 0 | 11 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0769× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 51.0 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -17.3) |
| [[LS 180 (line)]] | wt | 38.2 | 2 | 9 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.85× (z +16.0) | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -15.5) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -11.3) |
| [[SW480 (line)]] | alt | 47.0 | 3 | 8 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.85× (z +16.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 79.1 | 2 | 8 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.71× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -16.9) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0860× (z -15.8) |
| [[HOP62 (line)]] | alt | 39.3 | 3 (1 ⚠) | 7 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.06× (z +12.7) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.230× (z -11.8) |
| [[J82 (line)]] | alt | 89.3 | 4 | 6 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.70× (z +13.1) | [[Digitoxin (drug)]] 5 µM 0.204× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -14.0) |
| [[LoVo (line)]] | wt | 44.8 | 2 | 8 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.00× (z +12.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -12.9) |
| [[SHP-77 (line)]] | alt | 203 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -14.4) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.327× (z -11.1) |
| [[BT-474 (line)]] | alt | 64.8 | 2 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 6.26× (z +13.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.107× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 21.6 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 3.25× (z +11.6) | — |
| [[HS-578T (line)]] | alt | 36.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -11.9) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 42.6 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 5.54× (z +12.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -8.8) |
| [[A-427 (line)]] | wt | 26.5 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.284× (z -12.0) |
| [[C32 (line)]] | wt | 21.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.05× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 20.8 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.38× (z +15.2) | — |
| [[SNU-1 (line)]] | wt | 39.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -9.1) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.290× (z -9.0) |
| [[C-33 A (line)]] | alt | 72.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 33.6 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.108× (z -8.6) |
| [[H4 (line)]] | wt | 24.1 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0750× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -9.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[NCI-H661 (line)]] | alt | 132 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -17.2) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SW 1271 (line)]] | alt | 71.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -8.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 14.1 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 16.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 16.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.95 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.19 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.17 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 16.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.60 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.34 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.47 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 38.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1064), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF13B]] | +0.58 | +0.43 / +0.57 | both halves | 4e-05 |  |
| [[PKP2]] | +0.58 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[NCOA3]] | +0.56 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[MT1X]] | +0.56 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[MAOA]] | +0.54 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[LINC00540]] | +0.53 | +0.31 / +0.44 | both halves | 2e-04 |  |
| [[TREM1]] | +0.53 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[AKAP13]] | +0.53 | +0.43 / +0.37 | both halves | 8e-05 |  |
| [[ID1]] | +0.52 | +0.50 / +0.37 | both halves | 8e-05 |  |
| [[LIFR]] | +0.51 | +0.27 / +0.48 | both halves | 3e-04 |  |
| [[USP2]] | +0.51 | +0.25 / +0.46 | both halves | 4e-04 |  |
| [[ABCG1]] | +0.51 | +0.30 / +0.52 | both halves | 2e-04 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRYD4]] | -0.52 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[ANXA2R-OT1]] | -0.52 | -0.32 / -0.40 | both halves | 1e-04 |  |
| [[THBS4]] | -0.52 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[CSTF3]] | -0.50 | -0.28 / -0.37 | both halves | 3e-04 |  |
| [[TYSND1]] | -0.50 | -0.33 / -0.29 | both halves | 2e-04 |  |
| [[ANKRD18B]] | -0.50 | -0.26 / -0.31 | both halves | 4e-04 |  |
| [[SLC25A21]] | -0.50 | -0.31 / -0.31 | both halves | 2e-04 |  |
| [[DNAAF10]] | -0.49 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[PLS3-AS1]] | -0.48 | -0.28 / -0.34 | both halves | 3e-04 |  |
| [[MKRN3]] | -0.47 | -0.30 / -0.31 | both halves | 2e-04 |  |
| [[LINC02100]] | -0.47 | -0.27 / -0.31 | both halves | 3e-04 |  |
| [[TLCD3A]] | -0.47 | -0.26 / -0.35 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C2CD4A]] | B | C2CD4A activity raises FRY's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 3.11× lower at baseline in the lines without C2CD4A | 0.015 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L |
| [[TMEM45B]] | B | TMEM45B activity raises FRY's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 1.85× lower at baseline in the lines without TMEM45B | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[PAG1]] | B | PAG1 activity raises FRY's level | lines that do not express PAG1 (15) vs lines expressing it (35) | 2.33× lower at baseline in the lines without PAG1 | 0.087 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINA1]] | B | FRY activity raises SERPINA1's level | lines that do not express FRY (14) vs lines expressing it (36) | 1.75× lower at baseline in the lines without FRY | 0.058 | ⚠ within organs, on part of the lines; also absent: ADGRV1, DTNA, ZNF385B |
| [[KLF8]] | B | FRY activity raises KLF8's level | lines that do not express FRY (14) vs lines expressing it (36) | 2.06× lower at baseline in the lines without FRY | 0.067 | ⚠ within organs, on part of the lines; also absent: ADGRV1, DTNA, ZNF385B |
| [[CPE]] | B | FRY activity raises CPE's level | lines that do not express FRY (14) vs lines expressing it (36) | 2.52× lower at baseline in the lines without FRY | 0.074 | ⚠ within organs, on part of the lines; also absent: ADGRV1, DTNA, ZNF385B |
| [[PAG1]] | B | FRY activity raises PAG1's level | lines that do not express FRY (14) vs lines expressing it (36) | 2.38× lower at baseline in the lines without FRY | 0.087 | ⚠ within organs, on part of the lines; also absent: ADGRV1, DTNA, ZNF385B |
| [[TC2N]] | B | FRY activity raises TC2N's level | lines that do not express FRY (14) vs lines expressing it (36) | 1.84× lower at baseline in the lines without FRY | 0.091 | ⚠ within organs, on part of the lines; also absent: ADGRV1, DTNA, ZNF385B |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.565). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.6, 12.1); signed map (11.7, 33.2). **Vector** length 95.9, 24.8% of its response variance represented; |z| ≥ 3 in 1,437 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +22.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.2 | +14.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.3 | +14.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.3 | +13.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.0 | +11.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.4 | +1.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.9 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +8.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.6 | +6.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.4 | -8.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -6.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -7.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -4.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -2.8 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.3 | -4.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -0.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | FRY microtubule binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.1 — chr13:31,846,713-32,299,125 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA37E23.1, 13CDNA73, CG003; previously C13orf14 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TBA9](https://www.uniprot.org/uniprotkb/Q5TBA9) (Protein furry homolog):

> Plays a crucial role in the structural integrity of mitotic centrosomes and in the maintenance of spindle bipolarity by promoting PLK1 activity at the spindle poles in early mitosis. May function as a scaffold promoting the interaction between AURKA and PLK1, thereby enhancing AURKA-mediated PLK1 phosphorylation.

**Summary**, from NCBI Gene [10129](https://www.ncbi.nlm.nih.gov/gene/10129):

> Predicted to enable enzyme inhibitor activity. Predicted to be involved in cell morphogenesis and neuron projection development. Predicted to be located in centrosome; cytoplasm; and spindle pole. Predicted to be active in cell cortex and site of polarized growth. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20367](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20367) · Entrez [10129](https://www.ncbi.nlm.nih.gov/gene/10129) · UniProt [Q5TBA9](https://www.uniprot.org/uniprotkb/Q5TBA9) · Ensembl [ENSG00000073910](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073910)

## Data

Gene col 1064: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1064); `tables/drug_effects.parquet` (92 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1064, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1064]; `tensor/DDL_lfc|DDL_z.npy` [1064]; `embed/gene_vectors.npy` [1064]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1064 or target_col == 1064). Every well: [[FRY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
