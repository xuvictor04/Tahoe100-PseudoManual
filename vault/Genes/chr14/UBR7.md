---
symbol: "UBR7"
type: "gene"
col: 262
ensembl_id: "ENSG00000012963"
name: "ubiquitin protein ligase E3 component n-recognin 7"
location: "14q32.12"
module: 6
arm: "+"
pooled_cpm: 19.23
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# UBR7

*ubiquitin protein ligase E3 component n-recognin 7* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (21 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.14× (z +21.1, q 0e+00, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.92× (z +12.0, q 5e-31, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.730× (z -5.8, q 4e-06, down in 23 of 48 measured lines) ⚠ cell-cycle shift, explains ~88% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 0.05 µM: 0.809× (z -3.9, q 0.009, down in 9 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HAT1]] (+0.76, fdr 7e-06), [[ZGRF1]] (+0.72, fdr 7e-06), [[TK1]] (+0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 27 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 262.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **3.14×** | +21.1 | 0e+00 | 47/48 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **3.09×** | +20.8 | 0e+00 | 46/48 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.95×** | +19.9 | 0e+00 | 45/47 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.92×** | +12.0 | 5e-31 | 41/48 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.82×** | +11.1 | 2e-26 | 30/46 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | **1.82×** | +11.0 | 2e-26 | 25/40 (C32, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.87×** | +10.7 | 1e-24 | 22/36 (PANC-1, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.50×** | +10.6 | 2e-24 | 33/47 (SNU-423, NCI-H1573, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.74×** | +10.2 | 1e-22 | 39/47 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.66×** | +9.0 | 2e-17 | 26/42 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **1.60×** | +8.4 | 2e-15 | 26/45 (PANC-1, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.55×** | +7.8 | 4e-13 | 20/30 (PANC-1, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.52×** | +7.4 | 5e-12 | 29/48 (NCI-H23, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.47×** | +7.1 | 5e-11 | 19/47 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.46×** | +7.0 | 1e-10 | 27/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.58×** | +4.4 | 3e-04 | 9/48 (NCI-H2347, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.005 | 14/45 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Temuterkib (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.014 | 4/48 (SW 1271, SHP-77, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.033 | 4/45 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.033 | 6/48 (J82, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +2.9 | 0.056 | 4/48 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +2.9 | 0.063 | 12/48 (SW480, J82, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.17× | +2.8 | 0.069 | 2/48 (NCI-H2030, H4) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 262.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.730×** | -5.8 | 4e-06 | 23/48 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.813×** | -5.4 | 2e-05 | 22/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.770×** | -4.6 | 0.001 | 16/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.798×** | -4.2 | 0.004 | 19/48 (A549, NCI-H661, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.805×** | -4.0 | 0.007 | 12/47 (SHP-77, SW1417, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.809×** | -3.9 | 0.009 | 9/48 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.820×** | -3.5 | 0.033 | 13/47 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.821×** | -3.5 | 0.033 | 10/47 (RKO, LS 180, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.876× | -3.5 | 0.034 | 12/48 (A-427, AsPC-1, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.827×** | -3.4 | 0.041 | 11/47 (NCI-H661, COLO 205, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.884× | -3.2 | 0.064 | 12/48 (CFPAC-1, BT-474, …) | top dose only |  |
| [[Pentagastrin (drug)]] 5 µM |  | 0.884× | -3.2 | 0.064 | 3/48 (Hs 766T, LOX-IMVI, …) | top dose only | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.845× | -3.1 | 0.078 | 9/47 (A-172, CFPAC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.888× | -3.1 | 0.078 | 14/48 (NCI-H1792, KATO III, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.846× | -3.1 | 0.078 | 12/47 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Clotrimazole (drug)]] 5 µM |  | 0.891× | -3.0 | 0.087 | 9/48 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.844× | -3.0 | 0.087 | 6/47 (RPMI-7951, A549, …) | top dose only | plate-row cell shift; position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.851× | -3.0 | 0.090 | 6/47 (C-33 A, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.893× | -3.0 | 0.093 | 12/48 (COLO 205, LOX-IMVI, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.845× | -2.9 | 0.094 | 7/48 (HEC-1-A, CHP-212, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 262. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 10.6 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +10.1) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[PANC-1 (line)]] | alt | 14.5 | 5 (5 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.37× (z +10.0) ⚠ cell-cycle shift, explains ~35% of this change | [[Selinexor (drug)]] 5 µM 0.478× (z -8.6) ⚠ cell-cycle shift, explains ~97% of this change |
| [[SW480 (line)]] | alt | 25.9 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.88× (z +10.0) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[HEC-1-A (line)]] | alt | 22.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.49× (z +9.9) ⚠ cell-cycle shift, explains ~35% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.322× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 14.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.71× (z +9.2) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 13.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.64× (z +10.0) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2347 (line)]] | alt | 19.8 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.67× (z +11.0) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[A549 (line)]] | wt | 14.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.37× (z +8.9) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 8.75 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.97× (z +9.9) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2030 (line)]] | alt | 32.3 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.76× (z +8.9) ⚠ toxic; cell-cycle shift, explains ~35% of this change | — |
| [[Panc 03.27 (line)]] | alt | 15.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.32× (z +8.8) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[SW1417 (line)]] | alt | 17.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.91× (z +9.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[AN3 CA (line)]] | alt | 27.1 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0977× (z -8.5) |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0922× (z -9.1) |
| [[C32 (line)]] | wt | 17.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | — |
| [[CFPAC-1 (line)]] | alt | 20.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.55× (z +9.4) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[COLO 205 (line)]] | alt | 14.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +8.9) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[H4 (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.109× (z -10.7) ⚠ cell-cycle shift, explains ~2% of this change |
| [[HT-29 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.343× (z -9.0) ⚠ cell-cycle shift, explains ~97% of this change |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +9.0) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[LS 180 (line)]] | wt | 12.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.60× (z +9.2) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[SNU-423 (line)]] | alt | 11.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.42× (z +14.6) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[A-172 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 262), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAT1]] | +0.76 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[ZGRF1]] | +0.72 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[TK1]] | +0.71 | +0.65 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[RRM2]] | +0.71 | +0.62 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[FANCI]] | +0.71 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[CENPK]] | +0.70 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[TCF19]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CENPU]] | +0.70 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[NCAPD3]] | +0.70 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[E2F8]] | +0.70 | +0.68 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[WDHD1]] | +0.70 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[SPC25]] | +0.69 | +0.66 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.703). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.4, -46.6); signed map (-39.3, -43.5). **Vector** length 90.6, 20.7% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.55 to 28); *DNA Replication* (reactome, mean cos +0.55 to 40); *E2F G1/S* (control, mean cos +0.54 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.8 | +19.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.0 | +20.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | +3.0 | +11.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +2.9 | +21.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.7 | +10.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.7 | +2.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.6 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +4.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +1.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | -5.4 | -5.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | -5.2 | -5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | -5.1 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -0.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin protein ligase E3 component n-recognin 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:93,207,241-93,229,215 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C14orf130 |
| Gene groups (HGNC) | Ubiquitin protein ligase E3 component n-recognins |
| Hallmark sets | E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N806](https://www.uniprot.org/uniprotkb/Q8N806) (Putative E3 ubiquitin-protein ligase UBR7):

> E3 ubiquitin-protein ligase which is a component of the N-end rule pathway. Recognizes and binds to proteins bearing specific N-terminal residues that are destabilizing according to the N-end rule, leading to their ubiquitination and subsequent degradation.

**Summary**, from NCBI Gene [55148](https://www.ncbi.nlm.nih.gov/gene/55148):

> This gene encodes a UBR box-containing protein that belongs to the E3 ubiquitin ligase family. The protein also contains a plant homeodomain (PHD) in the C-terminus. In mammals, the encoded protein recognizes N-degrons, the destabilizing N-terminal residues of short-lived proteins, which results in ubiquitinylation, and proteolysis via the proteasome. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:20344](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20344) · Entrez [55148](https://www.ncbi.nlm.nih.gov/gene/55148) · UniProt [Q8N806](https://www.uniprot.org/uniprotkb/Q8N806) · Ensembl [ENSG00000012963](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012963)

## Data

Gene col 262: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 262); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 262, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 262]; `tensor/DDL_lfc|DDL_z.npy` [262]; `embed/gene_vectors.npy` [262]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 262 or target_col == 262). Every well: [[UBR7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBR7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
