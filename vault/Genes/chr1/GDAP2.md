---
symbol: "GDAP2"
type: "gene"
col: 12224
ensembl_id: "ENSG00000196505"
name: "ganglioside induced differentiation associated protein 2"
location: "1p12"
module: 142
arm: "+"
pooled_cpm: 61.07
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# GDAP2

*ganglioside induced differentiation associated protein 2* — 1p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.19× (z +13.1, q 1e-36, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.620× (z -8.1, q 4e-13, down in 35 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.746× (z -5.0, q 1e-04, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.102×, A549 0.354×, NCI-H2347 0.477×, KATO III 0.385×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (Hs 766T 0.286×, AN3 CA 0.131×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 2 lines (SW 900 0.309×, H4 0.277×; ⚠ transcription drop; cell-cycle shift, explains ~54% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.144×); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.174×); [[Decitabine (drug)]] 0.05 µM in 1 line (CHP-212 0.0818×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFCAB14]] (+0.73, fdr 7e-06), [[GRB2]] (+0.71, fdr 1e-05), [[UFD1]] (+0.70, fdr 7e-06); moves opposite to [[LIPT1]] (-0.61, fdr 1e-05), [[PNRC2]] (-0.61, fdr 1e-05), [[PIM3]] (-0.60, fdr 1e-05).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12224.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.19×** | +13.1 | 1e-36 | 47/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.07×** | +12.2 | 7e-32 | 47/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.01×** | +11.7 | 3e-29 | 47/48 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.08×** | +11.6 | 5e-29 | 46/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +10.5 | 1e-23 | 40/49 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.80×** | +9.8 | 7e-21 | 44/48 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.67×** | +8.6 | 7e-16 | 43/48 (HOP62, LS 180, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.52×** | +8.3 | 1e-14 | 40/49 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.64×** | +6.4 | 1e-08 | 35/48 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.47×** | +6.3 | 2e-08 | 34/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +5.7 | 5e-07 | 36/48 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +5.3 | 5e-06 | 35/48 (HOP62, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.8 | 0.006 | 20/48 (SW1417, BT-474, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.26×** | +3.7 | 0.008 | 24/49 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.6 | 0.011 | 21/45 (A-427, H4, …) | all doses, flat | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.038 | 15/48 (RPMI-7951, SNU-423, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.038 | 18/48 (CFPAC-1, HOP62, …) | top dose only |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.054 | 15/48 (J82, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12224.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.102×, A549 0.354×, NCI-H2347 0.477×, KATO III 0.385×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (Hs 766T 0.286×, AN3 CA 0.131×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 2 lines (SW 900 0.309×, H4 0.277×; ⚠ transcription drop; cell-cycle shift, explains ~54% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.144×); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.174×); [[Decitabine (drug)]] 0.05 µM in 1 line (CHP-212 0.0818×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.620×** | -8.1 | 4e-13 | 35/49 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.706×** | -5.7 | 4e-06 | 28/43 (AN3 CA, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.746×** | -5.0 | 1e-04 | 26/48 (A498, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.780×** | -3.9 | 0.014 | 22/45 (Hs 766T, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **0.805×** | -3.7 | 0.022 | 25/48 (SW 900, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.798×** | -3.7 | 0.022 | 22/48 (A498, AsPC-1, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **0.814×** | -3.5 | 0.038 | 24/48 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.872× | -3.3 | 0.068 | 18/48 (A498, NCI-H2347, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12224. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 37.3 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.12× (z +11.0) | — |
| [[SW480 (line)]] | alt | 61.4 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +12.4) | — |
| [[AsPC-1 (line)]] | alt | 54.2 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.62× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -13.0) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 47.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.19× (z +11.6) | — |
| [[LS 180 (line)]] | wt | 71.0 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.14× (z +10.6) | [[Docetaxel (drug)]] 0.05 µM 0.397× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~54% of this change |
| [[HEC-1-A (line)]] | alt | 52.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 50.0 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +12.0) | — |
| [[NCI-H2347 (line)]] | alt | 64.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.23× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.477× (z -8.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 75.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -11.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 38.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 62.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -10.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 58.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 58.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.61× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 57.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.70× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 47.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.63× (z +10.1) | — |
| [[A-427 (line)]] | wt | 42.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -19.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 51.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -9.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 53.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.80× (z +10.1) | — |
| [[CHP-212 (line)]] | wt | 63.3 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0818× (z -12.0) |
| [[H4 (line)]] | wt | 77.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.277× (z -9.2) ⚠ transcription drop; cell-cycle shift, explains ~54% of this change |
| [[HepG2_C3A (line)]] | wt | 50.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.20× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 56.3 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.144× (z -15.0) |
| [[KATO III (line)]] | alt | 51.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 48.8 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.49× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 49.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.38× (z +9.5) | — |
| [[NCI-H596 (line)]] | alt | 56.5 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.174× (z -13.5) |
| [[Panc 03.27 (line)]] | alt | 68.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 60.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.309× (z -10.0) ⚠ transcription drop; cell-cycle shift, explains ~54% of this change |
| [[SW1417 (line)]] | alt | 50.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +10.4) | — |
| [[SW48 (line)]] | wt | 44.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +8.5) | — |
| [[A-172 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 79.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 62.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 103 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12224), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB14]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[GRB2]] | +0.71 | +0.77 / +0.57 | both halves | 1e-05 |  |
| [[UFD1]] | +0.70 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[ZCCHC17]] | +0.70 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[KATNB1]] | +0.69 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[RARS2]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[ZW10]] | +0.68 | +0.80 / +0.46 | both halves | 3e-05 |  |
| [[TIMM10B]] | +0.68 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[SAP130]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[BABAM1]] | +0.66 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[PSMD13]] | +0.66 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[STRAP]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIPT1]] | -0.61 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[PNRC2]] | -0.61 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[PIM3]] | -0.60 | -0.57 / -0.68 | both halves | 1e-05 |  |
| [[FOSL2]] | -0.60 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[DDX43]] | -0.60 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[TXNIP]] | -0.59 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[ZFHX2]] | -0.58 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[EBI3]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[TGIF2]] | -0.57 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[MAPK1IP1L]] | -0.57 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[DLX2]] | -0.56 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[POGZ]] | -0.56 | -0.42 / -0.56 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GDAP2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.708). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.0, -9.0); signed map (-49.5, -4.4). **Vector** length 101, 29.4% of its response variance represented; |z| ≥ 3 in 1,032 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.2 | +11.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.8 | +9.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.3 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +10.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.0 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +6.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +1.7 | +0.9 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | +1.4 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -9.7 | -0.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -7.4 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.4 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.8 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.2 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.7 | -2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ganglioside induced differentiation associated protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p12 — chr1:117,863,485-117,929,621 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20142, dJ776P7.1, MACROD3 |
| Gene groups (HGNC) | BCH domain containing ; Macro domain containing; CRAL-TRIO lipid binding domain containing |
| Matched by | ensembl_id |

UniProt [Q9NXN4](https://www.uniprot.org/uniprotkb/Q9NXN4) carries no function annotation.

**Summary**, from NCBI Gene [54834](https://www.ncbi.nlm.nih.gov/gene/54834):

> Predicted to act upstream of or within response to retinoic acid. Located in lysosomal membrane. Implicated in autosomal recessive spinocerebellar ataxia 27. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18010](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18010) · Entrez [54834](https://www.ncbi.nlm.nih.gov/gene/54834) · UniProt [Q9NXN4](https://www.uniprot.org/uniprotkb/Q9NXN4) · Ensembl [ENSG00000196505](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196505)

## Data

Gene col 12224: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12224); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12224, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12224]; `tensor/DDL_lfc|DDL_z.npy` [12224]; `embed/gene_vectors.npy` [12224]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12224 or target_col == 12224). Every well: [[GDAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GDAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
