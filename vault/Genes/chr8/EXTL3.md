---
symbol: "EXTL3"
type: "gene"
col: 256
ensembl_id: "ENSG00000012232"
name: "exostosin like glycosyltransferase 3"
location: "8p21.1"
module: 159
arm: "+"
pooled_cpm: 31.28
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# EXTL3

*exostosin like glycosyltransferase 3* — 8p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.70× (z +31.5, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.930× (z -5.3, q 5e-05, down in 4 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Harringtonine (drug)]] 0.05 µM: 0.791× (z -4.4, q 0.001, down in 18 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW48 0.105×, NCI-H2030 0.309×, NCI-H1573 0.243×, NCI-H2347 0.344×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (HEC-1-A 0.328×, SW 900 0.155×, AsPC-1 0.281×, KATO III 0.287×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LS 180 0.120×, NCI-H2347 0.233×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM184B]] (+0.64, fdr 1e-05), [[DNAJC5]] (+0.62, fdr 3e-05), [[NIPA1]] (+0.61, fdr 1e-05); moves opposite to [[TCTN1]] (-0.62, fdr 1e-05), [[TRMT13]] (-0.61, fdr 1e-05), [[GABPB2]] (-0.59, fdr 4e-05).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ZCCHC24]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 256.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.70×** | +31.5 | 0e+00 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.99×** | +28.2 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.99×** | +28.2 | 0e+00 | 46/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.13×** | +21.7 | 0e+00 | 45/48 (HS-578T, A498, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +21.0 | 0e+00 | 39/47 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.55×** | +19.1 | 0e+00 | 46/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +12.0 | 2e-31 | 37/47 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.90×** | +11.3 | 6e-28 | 44/48 (SW480, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.66×** | +10.4 | 2e-23 | 36/46 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.55×** | +8.6 | 4e-16 | 28/46 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.41×** | +6.8 | 7e-10 | 23/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.39×** | +6.7 | 8e-10 | 27/47 (AsPC-1, A-172, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.35×** | +5.9 | 1e-07 | 21/47 (Hs 766T, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.6 | 2e-04 | 17/48 (A-427, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +4.5 | 3e-04 | 13/47 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.48×** | +4.2 | 0.001 | 15/45 (SW480, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.005 | 13/48 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.32×** | +2.9 | 0.086 | 5/45 (A-172, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 256.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW48 0.105×, NCI-H2030 0.309×, NCI-H1573 0.243×, NCI-H2347 0.344×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (HEC-1-A 0.328×, SW 900 0.155×, AsPC-1 0.281×, KATO III 0.287×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LS 180 0.120×, NCI-H2347 0.233×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -5.3 | 5e-05 | 4/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.774×** | -5.0 | 1e-04 | 22/46 (NCI-H1573, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.636×** | -4.8 | 3e-04 | 20/45 (BT-474, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.791×** | -4.4 | 0.001 | 18/45 (PANC-1, NCI-H2347, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.835× | -3.5 | 0.044 | 18/48 (NCI-H1573, HS-578T, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.843× | -3.5 | 0.044 | 12/48 (AN3 CA, NCI-H1573, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.890× | -3.2 | 0.093 | 13/48 (LS 180, HOP62, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.854× | -3.2 | 0.093 | 12/48 (HEC-1-A, Panc 03.27, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.859× | -3.1 | 0.12 | 17/48 (NCI-H2347, NCI-H2030, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.850× | -3.1 | 0.13 | 14/40 (LS 180, NCI-H2347, …) | inconsistent across doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 256. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 44.8 | 6 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.73× (z +14.5) | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -15.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 32.4 | 8 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.68× (z +19.2) | — |
| [[A-172 (line)]] | wt | 26.0 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.66× (z +13.2) | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 59.1 | 6 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.83× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 17.4 | 6 | 0 | [[Belinostat (drug)]] 5 µM 4.91× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 20.2 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.67× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.155× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 17.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.39× (z +14.8) | — |
| [[HEC-1-A (line)]] | alt | 64.3 | 3 (1 ⚠) | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.38× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.328× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 18.9 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.10× (z +15.4) | — |
| [[KATO III (line)]] | alt | 35.2 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.59× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 66.3 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.18× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 50.3 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 14.5 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +15.8) | — |
| [[A549 (line)]] | wt | 27.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.50× (z +13.2) | — |
| [[CFPAC-1 (line)]] | alt | 14.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +11.1) | — |
| [[H4 (line)]] | wt | 24.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 9.07× (z +10.4) | — |
| [[HCT15 (line)]] | alt | 27.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.19× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 42.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.57× (z +13.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 10.0× (z +12.6) | — |
| [[NCI-H2030 (line)]] | alt | 54.2 | 2 | 2 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.81× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 22.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 10.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.99× (z +9.9) | — |
| [[A-427 (line)]] | wt | 30.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.04× (z +11.0) | — |
| [[BT-474 (line)]] | alt | 33.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.34× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 23.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.01× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 23.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.95× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 66.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 12.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.46× (z +12.8) | — |
| [[SK-MEL-2 (line)]] | alt | 25.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.69× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 15.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.13× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 21.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.91× (z +10.8) | — |
| [[HepG2_C3A (line)]] | wt | 31.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.23× (z +9.5) | — |
| [[J82 (line)]] | alt | 8.46 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.25× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 24.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.47× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 31.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.45× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 34.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 256), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM184B]] | +0.64 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[DNAJC5]] | +0.62 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[NIPA1]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[MAP3K9]] | +0.60 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[EIF4E3]] | +0.59 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[PDXP]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CSNK1E]] | +0.59 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[SEMA4F]] | +0.58 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[UBTD1]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[ENTPD4]] | +0.58 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[CRLF3]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[LDLRAP1]] | +0.57 | +0.45 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCTN1]] | -0.62 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[TRMT13]] | -0.61 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[GABPB2]] | -0.59 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[SENP6]] | -0.58 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[GTF2H1]] | -0.58 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[TTC27]] | -0.58 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[ARMCX4]] | -0.58 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[USP40]] | -0.57 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[NOL8]] | -0.57 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[U2SURP]] | -0.57 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[GOPC]] | -0.55 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[GATB]] | -0.54 | -0.41 / -0.54 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZCCHC24]] | B | ZCCHC24 activity lowers EXTL3's level | lines that do not express ZCCHC24 (5) vs lines expressing it (45) | 2.11× higher at baseline in the lines without ZCCHC24 | 0.037 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |
| [[TRIP6]] | B | TRIP6 activity lowers EXTL3's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.67× higher at baseline in the lines without TRIP6 | 0.075 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[TOP2A]] | B | TOP2A activity lowers EXTL3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[STIMATE]] | C | STIMATE's natural level weakens EXTL3's drug response | STIMATE's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.05; direction not clear | 0.051 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TCTN1]] | C | TCTN1 activity lowers EXTL3's level | lines that do not express TCTN1 (3) vs lines expressing it (47) | 2.00× higher at baseline in the lines without TCTN1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DPF1, PHC1, DNAJC18; maybe low, not absent; its own permutation p |
| [[WARS2-AS1]] | C | WARS2-AS1 activity lowers EXTL3's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 1.81× higher at baseline in the lines without WARS2-AS1 | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.623). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.7, 3.3); signed map (-34.0, 18.7). **Vector** length 89.7, 20.6% of its response variance represented; |z| ≥ 3 in 1,258 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.2 | +21.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +12.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.4 | +19.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +11.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.1 | +10.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +1.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.7 | -3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | +2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +0.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.1 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.9 | -3.2 |
|  | [[AZD-8055 (drug)]] 5 µM |  | -1.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | exostosin like glycosyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.1 — chr8:28,600,469-28,756,561 (+) |
| Ensembl biotype | protein_coding |
| Also known as | botv, REGR |
| Gene groups (HGNC) | Exostosin glycosyltransferase family |
| Reactome | 9 pathways, smallest: HS-GAG biosynthesis; Heparan sulfate/heparin (HS-GAG) metabolism; XBP1(S) activates chaperone genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O43909](https://www.uniprot.org/uniprotkb/O43909) (Exostosin-like 3):

> Glycosyltransferase which regulates the biosynthesis of heparan sulfate (HS). Initiates HS synthesis by transferring the first N-acetyl-alpha-D-glucosamine (alpha-GlcNAc) residue (GlcNAcT-I activity) to the tetrasaccharide linker (GlcA-Gal-Gal-Xyl-)Ser core linker. May also transfer alpha-GlcNAc residues during HS elongation (GlcNAcT-II activity). Lacks glucuronyl transferase II (GlcAT-II) activity. Important for both skeletal development and hematopoiesis, through the formation of HS …

**Summary**, from NCBI Gene [2137](https://www.ncbi.nlm.nih.gov/gene/2137):

> This gene encodes a single-pass membrane protein which functions as a glycosyltransferase. The encoded protein catalyzes the transfer of N-acetylglucosamine to glycosaminoglycan chains. This reaction is important in heparin and heparan sulfate synthesis. Alternative splicing results in the multiple transcript variants. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:3518](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3518) · Entrez [2137](https://www.ncbi.nlm.nih.gov/gene/2137) · UniProt [O43909](https://www.uniprot.org/uniprotkb/O43909) · Ensembl [ENSG00000012232](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012232)

## Data

Gene col 256: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 256); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 256, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 256]; `tensor/DDL_lfc|DDL_z.npy` [256]; `embed/gene_vectors.npy` [256]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 256 or target_col == 256). Every well: [[EXTL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXTL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
