---
symbol: "TMEM41A"
type: "gene"
col: 8803
ensembl_id: "ENSG00000163900"
name: "transmembrane protein 41A"
location: "3q27.2"
module: 105
arm: "+"
pooled_cpm: 43.54
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# TMEM41A

*transmembrane protein 41A* — 3q27.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.50× (z +12.8, q 2e-34, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.577× (z -12.3, q 4e-32, down in 30 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.700× (z -7.7, q 2e-12, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (BT-474 0.204×, HEC-1-A 0.364×, A-172 0.274×, J82 0.306×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.195×, C-33 A 0.260×, C32 0.237×, Panc 03.27 0.356×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-172 0.397×, Panc 03.27 0.445×, NCI-H2347 0.508×, PANC-1 0.545×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A-172 0.325×, PANC-1 0.504×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SHP-77 0.197×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AMD1]] (+0.61, fdr 3e-05), [[DTX2P1-UPK3BP1-PMS2P11]] (+0.56, fdr 6e-05), [[MED26]] (+0.56, fdr 6e-05); moves opposite to [[SLC25A24]] (-0.58, fdr 7e-05), [[FAM114A2]] (-0.57, fdr 3e-05), [[DDX1]] (-0.57, fdr 1e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8803.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +12.8 | 2e-34 | 32/48 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.69×** | +11.2 | 8e-27 | 35/47 (HOP62, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.58×** | +10.2 | 5e-22 | 36/48 (J82, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.56×** | +10.0 | 2e-21 | 35/48 (AsPC-1, J82, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.59×** | +9.9 | 4e-21 | 32/48 (HOP62, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.44×** | +8.2 | 3e-14 | 33/48 (AsPC-1, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.41×** | +7.4 | 2e-11 | 28/47 (MIA PaCa-2, SW1417, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +6.7 | 2e-09 | 29/48 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +6.1 | 5e-08 | 22/48 (J82, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +6.0 | 1e-07 | 24/48 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.27×** | +5.3 | 5e-06 | 23/47 (J82, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.26×** | +5.2 | 8e-06 | 16/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.25×** | +5.0 | 2e-05 | 22/47 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.46×** | +4.4 | 4e-04 | 15/48 (AsPC-1, H4, …) | top dose only | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.45×** | +4.4 | 5e-04 | 12/47 (PANC-1, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.002 | 12/47 (HT-29, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.004 | 13/48 (A498, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.6 | 0.011 | 10/48 (KATO III, A-172, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.018 | 7/48 (LOX-IMVI, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.028 | 10/48 (SW480, HOP62, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.029 | 12/47 (C-33 A, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.030 | 10/47 (AsPC-1, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.030 | 9/48 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.20×** | +2.9 | 0.067 | 5/48 (A498, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8803.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (BT-474 0.204×, HEC-1-A 0.364×, A-172 0.274×, J82 0.306×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.195×, C-33 A 0.260×, C32 0.237×, Panc 03.27 0.356×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-172 0.397×, Panc 03.27 0.445×, NCI-H2347 0.508×, PANC-1 0.545×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A-172 0.325×, PANC-1 0.504×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SHP-77 0.197×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.577×** | -12.3 | 4e-32 | 30/45 (A-427, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.649×** | -9.3 | 4e-18 | 24/38 (BT-474, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.665×** | -8.5 | 5e-15 | 26/40 (KATO III, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.700×** | -7.7 | 2e-12 | 34/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -5.5 | 4e-06 | 2/49 (CHP-212, NCI-H661) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.788×** | -5.3 | 9e-06 | 24/47 (A-172, Panc 03.27, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.785×** | -5.2 | 2e-05 | 27/47 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.862× | -4.7 | 2e-04 | 21/47 (A-172, Panc 03.27, …) | two highest doses | composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.812×** | -4.5 | 5e-04 | 21/47 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.869× | -3.2 | 0.091 | 15/48 (LS 180, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8803. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 35.8 | 3 (2 ⚠) | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +14.8) | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.325× (z -10.7) |
| [[HOP62 (line)]] | alt | 32.1 | 4 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.360× (z -9.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 52.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -15.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 50.6 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -12.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 112 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 45.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.504× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 53.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 57.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -12.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 65.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -18.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 44.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 76.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.336× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[A-427 (line)]] | wt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -12.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 24.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 25.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.16× (z +8.8) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[BT-474 (line)]] | alt | 58.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -13.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 36.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -11.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 28.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 87.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 55.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 32.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.59× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[SHP-77 (line)]] | alt | 19.1 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.197× (z -9.6) |
| [[SNU-423 (line)]] | alt | 31.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 73.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 45.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8803), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AMD1]] | +0.61 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[DTX2P1-UPK3BP1-PMS2P11]] | +0.56 | +0.38 / +0.60 | both halves | 6e-05 |  |
| [[MED26]] | +0.56 | +0.39 / +0.60 | both halves | 6e-05 |  |
| [[CNOT8]] | +0.56 | +0.34 / +0.62 | both halves | 1e-04 |  |
| [[FUT11]] | +0.56 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[NUDT22]] | +0.56 | +0.23 / +0.66 | both halves | 5e-04 |  |
| [[ABHD17B]] | +0.55 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[ZNF143]] | +0.54 | +0.36 / +0.59 | both halves | 1e-04 |  |
| [[TOR1B]] | +0.54 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[TPTEP2-CSNK1E]] | +0.54 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[B3GAT3]] | +0.54 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[C4orf3]] | +0.53 | +0.44 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A24]] | -0.58 | -0.38 / -0.59 | both halves | 7e-05 |  |
| [[FAM114A2]] | -0.57 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[DDX1]] | -0.57 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[IMPACT]] | -0.56 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[NDUFS1]] | -0.56 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[SLC25A46]] | -0.56 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[OCRL]] | -0.56 | -0.31 / -0.63 | both halves | 2e-04 |  |
| [[NOTCH2NLC]] | -0.56 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[NUDT9]] | -0.55 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[CFL2]] | -0.55 | -0.40 / -0.56 | both halves | 4e-05 |  |
| [[NBN]] | -0.55 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[PTAR1]] | -0.54 | -0.34 / -0.60 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMEM41A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TMTC2]] | B | TMTC2 activity raises TMEM41A's level | lines that do not express TMTC2 (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without TMTC2 | 0.068 | ⚠ within organs, on part of the lines; also absent: RNF125, GPR19; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.548). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-24.4, 4.1); signed map (-41.1, 18.5). **Vector** length 104, 24.1% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | +5.5 | +7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.3 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +12.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +6.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.2 | +9.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.7 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +6.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.2 | +3.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +4.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.9 | -7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.4 | -4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.0 | -9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.9 | -12.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -7.8 | -5.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 41A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.2 — chr3:185,476,496-185,499,057 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC15397 |
| Matched by | ensembl_id |

UniProt [Q96HV5](https://www.uniprot.org/uniprotkb/Q96HV5) carries no function annotation.

**Summary**, from NCBI Gene [90407](https://www.ncbi.nlm.nih.gov/gene/90407):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30544](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30544) · Entrez [90407](https://www.ncbi.nlm.nih.gov/gene/90407) · UniProt [Q96HV5](https://www.uniprot.org/uniprotkb/Q96HV5) · Ensembl [ENSG00000163900](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163900)

## Data

Gene col 8803: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8803); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8803, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8803]; `tensor/DDL_lfc|DDL_z.npy` [8803]; `embed/gene_vectors.npy` [8803]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8803 or target_col == 8803). Every well: [[TMEM41A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM41A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
