---
symbol: "WDR25"
type: "gene"
col: 10723
ensembl_id: "ENSG00000176473"
name: "WD repeat domain 25"
location: "14q32.2"
module: 49
arm: "+"
pooled_cpm: 33.83
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# WDR25

*WD repeat domain 25* — 14q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.08× (z +18.8, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.531× (z -10.6, q 2e-23, down in 28 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.815× (z -3.4, q 0.035, down in 19 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H460 0.182×, KATO III 0.0896×, LoVo 0.184×, Hs 766T 0.129×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (J82 0.0602×, SW480 0.156×, SW1417 0.226×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.121×, NCI-H2030 0.245×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SHP-77 0.373×, A498 0.487×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H2030 0.390×).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WARS1]] (+0.59, fdr 1e-05, ⚠ same locus), [[SLC35B1]] (+0.54, fdr 1e-05), [[FICD]] (+0.50, fdr 3e-05), [[XBP1]] (+0.48, fdr 2e-05); moves opposite to [[RPSAP58]] (-0.40, fdr 6e-04), [[DCBLD1]] (-0.40, fdr 5e-05), [[FUT10]] (-0.39, fdr 3e-04).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[RMND5B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10723.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.08×** | +18.8 | 0e+00 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.65×** | +16.2 | 0e+00 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.39×** | +14.6 | 1e-45 | 43/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +14.2 | 2e-43 | 33/47 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +10.8 | 3e-25 | 32/48 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +9.6 | 1e-19 | 34/48 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +8.7 | 2e-16 | 37/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +6.4 | 1e-08 | 30/47 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.37×** | +5.2 | 1e-05 | 24/47 (SW48, A-427, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.82×** | +5.2 | 1e-05 | 27/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.35×** | +5.0 | 3e-05 | 20/47 (CFPAC-1, HOP62, …) | two highest doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.19× | +4.1 | 0.002 | 15/48 (LoVo, SNU-1, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +3.7 | 0.008 | 18/48 (SK-MEL-2, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.025 | 8/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.025 | 10/48 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Encorafenib (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.066 | 10/48 (Hs 766T, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +2.9 | 0.091 | 15/48 (NCI-H460, CFPAC-1, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.19× | +2.9 | 0.091 | 5/48 (A-427, AN3 CA, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10723.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H460 0.182×, KATO III 0.0896×, LoVo 0.184×, Hs 766T 0.129×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (J82 0.0602×, SW480 0.156×, SW1417 0.226×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.121×, NCI-H2030 0.245×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SHP-77 0.373×, A498 0.487×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H2030 0.390×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.531×** | -10.6 | 2e-23 | 28/45 (LoVo, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.616×** | -7.5 | 2e-11 | 25/40 (J82, SW480, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.720×** | -5.5 | 7e-06 | 22/48 (SHP-77, LoVo, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.721×** | -5.5 | 7e-06 | 27/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.714×** | -5.4 | 7e-06 | 21/38 (NCI-H460, KATO III, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.761×** | -4.6 | 5e-04 | 23/47 (SHP-77, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.774×** | -4.3 | 0.001 | 21/48 (SHP-77, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.778×** | -4.0 | 0.004 | 23/45 (NCI-H23, LoVo, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.640×** | -3.9 | 0.006 | 21/46 (LoVo, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.815×** | -3.4 | 0.035 | 19/47 (NCI-H2030, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 5 µM |  | 0.709× | -3.0 | 0.14 | 10/43 (MIA PaCa-2, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10723. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 46.1 | 5 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.390× (z -8.9) |
| [[SW480 (line)]] | alt | 30.5 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.80× (z +14.4) | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -18.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 115 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.160× (z -14.2) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.373× (z -10.8) |
| [[LoVo (line)]] | wt | 62.2 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -16.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 21.8 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.94× (z +9.5) | [[Harringtonine (drug)]] 5 µM 0.226× (z -12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.487× (z -9.0) |
| [[A549 (line)]] | wt | 21.3 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.91× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[CFPAC-1 (line)]] | alt | 27.8 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 29.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +12.7) | — |
| [[PANC-1 (line)]] | alt | 19.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.54× (z +14.7) | — |
| [[A-427 (line)]] | wt | 23.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +11.2) | — |
| [[HCT15 (line)]] | alt | 28.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -9.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 19.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.77× (z +11.1) | — |
| [[LOX-IMVI (line)]] | wt | 13.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.45× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 29.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +14.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.239× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[NCI-H460 (line)]] | wt | 81.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[Panc 03.27 (line)]] | alt | 36.3 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -9.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 27.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -10.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 45.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0896× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[SNU-423 (line)]] | alt | 14.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 35.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -11.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[AsPC-1 (line)]] | alt | 19.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.38× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 25.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[HS-578T (line)]] | alt | 28.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.6) | — |
| [[J82 (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0602× (z -20.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 43.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[NCI-H1792 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 48.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.0) | — |
| [[SNU-1 (line)]] | wt | 46.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +10.7) | — |
| [[AN3 CA (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10723), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 15 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WARS1]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SLC35B1]] | +0.54 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[FICD]] | +0.50 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[XBP1]] | +0.48 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[SEC61B]] | +0.47 | +0.38 / +0.46 | both halves | 6e-05 |  |
| [[SIL1]] | +0.47 | +0.54 / +0.38 | both halves | 7e-05 |  |
| [[CHAC1]] | +0.46 | +0.35 / +0.49 | both halves | 1e-04 |  |
| [[GOT1]] | +0.44 | +0.22 / +0.48 | both halves | 6e-04 |  |
| [[DNAJB9]] | +0.44 | +0.38 / +0.44 | both halves | 7e-05 |  |
| [[SELENOS]] | +0.43 | +0.32 / +0.44 | both halves | 1e-04 |  |
| [[MARS1]] | +0.43 | +0.33 / +0.46 | both halves | 1e-04 |  |
| [[SESN2]] | +0.42 | +0.27 / +0.50 | both halves | 3e-04 |  |
| [[LCA5L]] | +0.42 | +0.47 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPSAP58]] | -0.40 | -0.21 / -0.34 | both halves | 6e-04 |  |
| [[DCBLD1]] | -0.40 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[FUT10]] | -0.39 | -0.28 / -0.29 | both halves | 3e-04 |  |
| [[APP]] | -0.39 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[HPSE]] | -0.38 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[CHRNA5]] | -0.38 | -0.39 / -0.27 | both halves | 3e-04 |  |
| [[LAPTM4B]] | -0.37 | -0.36 / -0.28 | both halves | 3e-04 |  |
| [[CTSH]] | -0.37 | -0.22 / -0.34 | both halves | 6e-04 |  |
| [[TMEM64]] | -0.37 | -0.20 / -0.31 | both halves | 7e-04 |  |
| [[IL17RB]] | -0.36 | -0.33 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[RHOBTB3]] | -0.36 | -0.12 / -0.38 | ⚠ not reproduced | 0.002 |  |
| [[CENPV]] | -0.36 | -0.33 / -0.26 | both halves | 4e-04 |  |
| [[UBE2E1]] | -0.35 | -0.32 / -0.29 | both halves | 2e-04 |  |
| [[NECTIN3]] | -0.35 | -0.30 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RMND5B]] | C | WDR25's natural level strengthens RMND5B's drug response | WDR25's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.33; direction not clear | 0.070 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.374). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.4, -39.3); signed map (-56.8, 13.1). **Vector** length 86.5, 19.9% of its response variance represented; |z| ≥ 3 in 1,182 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +10.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.6 | +5.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Belumosudil (mesylate) (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.9 | +1.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -1.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -0.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.6 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -2.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.5 | -1.3 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.2 — chr14:100,376,418-100,530,303 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4645; previously C14orf67 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q64LD2](https://www.uniprot.org/uniprotkb/Q64LD2) carries no function annotation.

**Summary**, from NCBI Gene [79446](https://www.ncbi.nlm.nih.gov/gene/79446):

> This gene encodes a protein containing 7 WD repeats. WD repeats are approximately 30 to 40-amino acid domains containing several conserved residues, typically having a Tryptophan-Aspartic acid dipeptide (WD) at the C-terminal end. WD domains are involved in protein-protein interactions in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr …

**Accessions** — [HGNC:21064](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21064) · Entrez [79446](https://www.ncbi.nlm.nih.gov/gene/79446) · UniProt [Q64LD2](https://www.uniprot.org/uniprotkb/Q64LD2) · Ensembl [ENSG00000176473](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176473)

## Data

Gene col 10723: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10723); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10723, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10723]; `tensor/DDL_lfc|DDL_z.npy` [10723]; `embed/gene_vectors.npy` [10723]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10723 or target_col == 10723). Every well: [[WDR25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
