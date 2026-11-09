---
symbol: "RAB10"
type: "gene"
col: 1410
ensembl_id: "ENSG00000084733"
name: "RAB10, member RAS oncogene family"
location: "2p23.3"
module: 49
arm: "+"
pooled_cpm: 338.53
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# RAB10

*RAB10, member RAS oncogene family* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.45× (z +11.8, q 9e-30, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.789× (z -10.9, q 9e-25, down in 31 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPZB]] (+0.62, fdr 1e-05), [[RHOA]] (+0.56, fdr 2e-05), [[GNB1]] (+0.55, fdr 5e-05); moves opposite to [[CLK1]] (-0.61, fdr 2e-05), [[ZFPL1]] (-0.58, fdr 1e-04), [[TXNL4B]] (-0.55, fdr 2e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SH3RF2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1410.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +11.8 | 9e-30 | 42/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +11.8 | 9e-30 | 42/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.98×** | +11.5 | 4e-28 | 45/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +10.7 | 2e-24 | 42/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +9.8 | 2e-20 | 35/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +8.9 | 7e-17 | 37/47 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +8.6 | 6e-16 | 37/48 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +7.9 | 3e-13 | 35/48 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.23×** | +6.6 | 3e-09 | 26/48 (SHP-77, SNU-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | **1.23×** | +6.4 | 1e-08 | 24/44 (A549, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +6.3 | 2e-08 | 16/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.22×** | +6.1 | 5e-08 | 24/48 (SW1417, COLO 205, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **1.21×** | +6.0 | 7e-08 | 25/49 (A549, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.18× | +5.3 | 5e-06 | 21/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.18× | +5.2 | 8e-06 | 19/48 (NCI-H1573, A549, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.33×** | +4.8 | 7e-05 | 27/49 (NCI-H460, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.14× | +4.3 | 5e-04 | 16/47 (SW48, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **1.28×** | +4.2 | 7e-04 | 26/48 (LOX-IMVI, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.09× | +4.0 | 0.002 | 3/48 (AsPC-1, SW48, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.20× | +3.8 | 0.003 | 17/48 (PANC-1, SW 900, …) | two highest doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.12× | +3.7 | 0.005 | 13/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.11× | +3.2 | 0.029 | 10/48 (LoVo, SW 900, …) | inconsistent across doses |  |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 1.11× | +3.1 | 0.030 | 0/48 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1410.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.789×** | -10.9 | 9e-25 | 31/49 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.836× | -5.6 | 7e-06 | 23/47 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.853× | -5.1 | 5e-05 | 19/48 (CFPAC-1, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.833×** | -5.1 | 6e-05 | 24/48 (A549, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.861× | -4.8 | 1e-04 | 11/48 (J82, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.810×** | -4.6 | 5e-04 | 27/48 (SW480, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.921× | -3.8 | 0.012 | 2/48 (SW 1088, SW48) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.890× | -3.6 | 0.020 | 17/48 (NCI-H460, SNU-423, …) | all doses, stronger at high dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 0.891× | -3.2 | 0.087 | 6/48 (NCI-H460, SNU-1, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.909× | -3.1 | 0.11 | 5/48 (RKO, SK-MEL-2, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1410. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 341 | 8 (5 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.31× (z +17.3) | — |
| [[KATO III (line)]] | alt | 359 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +15.4) | — |
| [[SW480 (line)]] | alt | 310 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 2.87× (z +14.4) | — |
| [[A549 (line)]] | wt | 449 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -21.7) |
| [[HT-29 (line)]] | alt | 399 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 1.92× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 405 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.61× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 492 | 3 | 0 | [[Digitoxin (drug)]] 0.5 µM 1.93× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 251 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.80× (z +10.6) | [[Lonafarnib (drug)]] 5 µM 0.410× (z -9.2) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 433 | 3 | 0 | [[Digitoxin (drug)]] 0.5 µM 1.77× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 367 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 2.96× (z +13.4) | — |
| [[SNU-1 (line)]] | wt | 273 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -12.7) |
| [[SW48 (line)]] | wt | 491 | 2 (1 ⚠) | 1 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.30× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -9.4) |
| [[A-172 (line)]] | wt | 326 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -14.4) ⚠ cell-cycle shift, explains ~1% of this change |
| [[hTERT-HPNE (line)]] | wt | 186 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.91× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | — |
| [[J82 (line)]] | alt | 195 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 1.71× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.653× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 479 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.06× (z +10.2) ⚠ toxic | — |
| [[SHP-77 (line)]] | alt | 178 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.96× (z +11.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A-427 (line)]] | wt | 471 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.462× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A498 (line)]] | wt | 515 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -14.0) |
| [[C-33 A (line)]] | alt | 324 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.454× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[H4 (line)]] | wt | 179 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.98× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 321 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.94× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 333 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.77× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 277 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 1.58× (z +8.8) ⚠ toxic | — |
| [[HS-578T (line)]] | alt | 224 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.75× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | — |
| [[LoVo (line)]] | wt | 322 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.67× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 279 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.67× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | — |
| [[AN3 CA (line)]] | alt | 224 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 324 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 186 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 344 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 202 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 362 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 355 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 472 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 355 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 425 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 362 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 285 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 311 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 303 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 322 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 261 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 273 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 332 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 325 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 341 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1410), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPZB]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RHOA]] | +0.56 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[GNB1]] | +0.55 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[RSU1]] | +0.54 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[USP14]] | +0.53 | +0.39 / +0.60 | both halves | 6e-05 |  |
| [[CDC42BPB]] | +0.53 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[CDC42]] | +0.51 | +0.36 / +0.55 | both halves | 9e-05 | STRING 418 |
| [[GALNT10]] | +0.51 | +0.29 / +0.49 | both halves | 2e-04 |  |
| [[CHML]] | +0.50 | +0.34 / +0.51 | both halves | 1e-04 | pathway: RAB GEFs exchange GTP for GDP on RABs; STRING 741 |
| [[YWHAB]] | +0.50 | +0.56 / +0.23 | both halves | 5e-04 | pathway: Translocation of SLC2A4 (GLUT4) to the plasma membrane; STRING 621 |
| [[DIAPH1]] | +0.50 | +0.40 / +0.46 | both halves | 4e-05 |  |
| [[ACTN4]] | +0.49 | +0.44 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLK1]] | -0.61 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[ZFPL1]] | -0.58 | -0.34 / -0.66 | both halves | 1e-04 |  |
| [[TXNL4B]] | -0.55 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[PLPP5]] | -0.55 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[C14orf28]] | -0.55 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[TGDS]] | -0.55 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[BET1]] | -0.53 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[RSRP1]] | -0.53 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[UNC119B]] | -0.52 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[TMEM101]] | -0.52 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[FAM98C]] | -0.52 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[DNAJC4]] | -0.52 | -0.28 / -0.55 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH3RF2]] | B | SH3RF2 activity raises RAB10's level | lines that do not express SH3RF2 (16) vs lines expressing it (34) | 1.30× lower at baseline in the lines without SH3RF2 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC01564, CAPG, LINC00857; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction -0.206). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.1, -38.4); signed map (-10.2, 35.7). **Vector** length 122, 37.4% of its response variance represented; |z| ≥ 3 in 1,390 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.3 | +7.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.9 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +6.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +5.0 | +4.3 |
|  | [[EX229 (drug)]] 5 µM |  | +4.8 | +4.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.4 | +4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.9 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.0 | -10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -6.7 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -6.6 | -5.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | -5.8 | -5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.0 | -3.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.7 | -4.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -3.5 | -3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -3.4 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -2.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | RAB10, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:26,034,084-26,137,454 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 8 pathways, smallest: RAB geranylgeranylation; Translocation of SLC2A4 (GLUT4) to the plasma membrane; RAB GEFs exchange GTP for GDP on RABs |
| Matched by | ensembl_id |

**Function**, from UniProt [P61026](https://www.uniprot.org/uniprotkb/P61026) (Ras-related protein Rab-10):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different set of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB10 is mainly involved in the biosynthetic transport of proteins from the Golgi to the plasma membrane. Regulates, for …

**Summary**, from NCBI Gene [10890](https://www.ncbi.nlm.nih.gov/gene/10890):

> RAB10 belongs to the RAS (see HRAS; MIM 190020) superfamily of small GTPases. RAB proteins localize to exocytic and endocytic compartments and regulate intracellular vesicle trafficking (Bao et al., 1998 [PubMed 9918381]).[supplied by OMIM, Mar 2009]

**Accessions** — [HGNC:9759](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9759) · Entrez [10890](https://www.ncbi.nlm.nih.gov/gene/10890) · UniProt [P61026](https://www.uniprot.org/uniprotkb/P61026) · Ensembl [ENSG00000084733](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084733)

## Data

Gene col 1410: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1410); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1410, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1410]; `tensor/DDL_lfc|DDL_z.npy` [1410]; `embed/gene_vectors.npy` [1410]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1410 or target_col == 1410). Every well: [[RAB10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
