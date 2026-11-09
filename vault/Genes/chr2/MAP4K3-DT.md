---
symbol: "MAP4K3-DT"
type: "gene"
col: 13791
ensembl_id: "ENSG00000231312"
name: "MAP4K3 divergent transcript"
location: "2p22.1"
module: 4
arm: "-"
pooled_cpm: 50.83
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 19
n_dd_up_clean: 17
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MAP4K3-DT

*MAP4K3 divergent transcript* — 2p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.99× (z +17.7, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.536× (z -11.3, q 6e-27, down in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.341× (z -10.2, q 4e-22, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM178A]] (+0.55, fdr 3e-05, ⚠ read-through risk), [[UPP2]] (+0.49, fdr 3e-05), [[SCAMP5]] (+0.48, fdr 5e-05), [[ORMDL1]] (+0.48, fdr 1e-04); moves opposite to [[DCAF1]] (-0.51, fdr 1e-05), [[POLR3H]] (-0.51, fdr 4e-05), [[WDR18]] (-0.49, fdr 4e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TMEM178A]] → it (grade C ⚠); 1 goes from it, the strongest it → [[TMEM178A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13791.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +17.7 | 0e+00 | 45/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +10.8 | 2e-24 | 37/48 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +10.7 | 2e-24 | 43/48 (A-172, J82, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +7.8 | 8e-13 | 37/48 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.8 | 1e-12 | 36/49 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.58×** | +7.4 | 1e-11 | 31/48 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +6.6 | 2e-09 | 30/48 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +6.6 | 2e-09 | 23/39 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +6.5 | 6e-09 | 31/48 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +6.2 | 4e-08 | 32/48 (LS 180, BT-474, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +5.8 | 4e-07 | 27/48 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.36×** | +5.6 | 8e-07 | 31/48 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.35×** | +5.5 | 2e-06 | 27/48 (A-172, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +5.2 | 8e-06 | 29/48 (A-172, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **1.28×** | +4.4 | 5e-04 | 23/46 (NCI-H1573, SW1417, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.005 | 18/48 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.15× | +3.6 | 0.008 | 11/48 (LS 180, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13791.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.536×** | -11.3 | 6e-27 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.536×** | -11.3 | 6e-27 | 37/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.341×** | -10.2 | 4e-22 | 40/47 (RKO, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.538×** | -10.0 | 2e-21 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.373×** | -9.3 | 1e-18 | 42/49 (SW480, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.598×** | -9.3 | 2e-18 | 35/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.615×** | -8.4 | 3e-15 | 34/47 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.649×** | -7.8 | 4e-13 | 30/48 (SW 900, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.617×** | -7.8 | 4e-13 | 32/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.637×** | -7.3 | 2e-11 | 34/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.791×** | -6.0 | 1e-07 | 23/47 (A498, A549, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.715×** | -5.7 | 5e-07 | 26/48 (SW480, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.722×** | -5.7 | 7e-07 | 23/48 (A549, PANC-1, …) | rises with dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.602×** | -4.8 | 7e-05 | 23/48 (A498, J82, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.728×** | -4.6 | 2e-04 | 24/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.681×** | -3.6 | 0.010 | 15/48 (SW480, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.811×** | -3.6 | 0.012 | 19/47 (SW480, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13791. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 66.9 | 1 | 11 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.222× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.244× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 48.6 | 2 | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +16.2) | [[Harringtonine (drug)]] 0.5 µM 0.314× (z -12.2) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.407× (z -9.5) |
| [[PANC-1 (line)]] | alt | 58.2 | 1 | 7 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +10.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.271× (z -14.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.333× (z -12.3) |
| [[LS 180 (line)]] | wt | 57.3 | 3 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +11.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.312× (z -10.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.139× (z -9.3) |
| [[LoVo (line)]] | wt | 47.7 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +10.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.368× (z -10.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.188× (z -9.4) |
| [[A-172 (line)]] | wt | 35.2 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 2.91× (z +12.8) | — |
| [[Panc 03.27 (line)]] | alt | 65.8 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.293× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.163× (z -9.4) |
| [[RKO (line)]] | wt | 34.4 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +13.7) | [[Digitoxin (drug)]] 5 µM 0.195× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0734× (z -10.5) |
| [[SW 900 (line)]] | alt | 95.7 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -15.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.307× (z -9.2) |
| [[A498 (line)]] | wt | 81.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -21.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 80.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -19.5) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 102 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -11.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.319× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 48.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -14.4) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 40.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +10.3) | — |
| [[HepG2_C3A (line)]] | wt | 102 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.361× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 48.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +13.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.382× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 64.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 56.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -11.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 61.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +10.2) | — |
| [[CHP-212 (line)]] | wt | 43.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0759× (z -10.1) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 47.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 56.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.03× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 46.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.7) | — |
| [[J82 (line)]] | alt | 28.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.38× (z +9.6) | — |
| [[KATO III (line)]] | alt | 68.1 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.144× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 28.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +12.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 20.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 66.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 50.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -12.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 24.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +10.5) | — |
| [[SW48 (line)]] | wt | 39.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.194× (z -9.1) |
| [[AN3 CA (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13791), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM178A]] | +0.55 | +0.46 / +0.62 | both halves | 3e-05 | ⚠ **readthrough risk**: TMEM178A lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[UPP2]] | +0.49 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[SCAMP5]] | +0.48 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[ORMDL1]] | +0.48 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[HOTAIRM1]] | +0.48 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[BTG1-DT]] | +0.47 | +0.41 / +0.51 | both halves | 4e-05 | same gene group |
| [[KPNB1-DT]] | +0.46 | +0.45 / +0.46 | both halves | 3e-05 | same gene group |
| [[BET1]] | +0.46 | +0.52 / +0.37 | both halves | 8e-05 |  |
| [[EOGT-DT]] | +0.46 | +0.33 / +0.49 | both halves | 1e-04 | same gene group |
| [[APTR]] | +0.46 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[VAMP4]] | +0.45 | +0.35 / +0.49 | both halves | 1e-04 |  |
| [[MRPL33]] | +0.45 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[P2RX4]] | +0.44 | +0.46 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCAF1]] | -0.51 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[POLR3H]] | -0.51 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[WDR18]] | -0.49 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[DLAT]] | -0.49 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[SYDE1]] | -0.48 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[SPIDR]] | -0.47 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[ALMS1]] | -0.47 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[TEDC1]] | -0.46 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[RIF1]] | -0.46 | -0.32 / -0.58 | both halves | 2e-04 |  |
| [[TRRAP]] | -0.45 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[SMARCAD1]] | -0.45 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[WDR70]] | -0.45 | -0.16 / -0.37 | ⚠ not reproduced | 0.001 |  |
| [[BAP1]] | -0.44 | -0.47 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM178A]] | C | TMEM178A activity raises MAP4K3-DT's level | lines that do not express TMEM178A (3) vs lines expressing it (47) | 1.95× lower at baseline in the lines without TMEM178A | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MPP4, B4GALT1, LCA5; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM178A]] | C | MAP4K3-DT's natural level strengthens TMEM178A's drug response | MAP4K3-DT's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.27; direction not clear | 0.058 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.389). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-19.5, -43.9); signed map (34.8, 0.1). **Vector** length 85.8, 22.9% of its response variance represented; |z| ≥ 3 in 1,335 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +10.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +7.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +17.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.1 | +3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | +5.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.6 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.5 | -9.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.1 | +5.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -10.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -7.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -0.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | MAP4K3 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p22.1 — chr2:39,436,530-39,665,343 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54056](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54056) · Entrez [728730](https://www.ncbi.nlm.nih.gov/gene/728730) · Ensembl [ENSG00000231312](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231312)

## Data

Gene col 13791: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13791); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13791, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13791]; `tensor/DDL_lfc|DDL_z.npy` [13791]; `embed/gene_vectors.npy` [13791]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13791 or target_col == 13791). Every well: [[MAP4K3-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP4K3-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
