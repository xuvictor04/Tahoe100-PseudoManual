---
symbol: "FAT1"
type: "gene"
col: 1386
ensembl_id: "ENSG00000083857"
name: "FAT atypical cadherin 1"
location: "4q35.2"
module: 197
arm: "+"
pooled_cpm: 378.24
n_lines_expressing: 47
n_dd_up: 21
n_dd_down: 14
n_dd_up_clean: 15
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/197"]
generated_by: "tahoemap"
---

# FAT1

*FAT atypical cadherin 1* — 4q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.78× (z +22.2, q 0e+00, up in 30 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.609× (z -10.8, q 1e-24, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK6]] (+0.68, fdr 7e-06), [[IRS1]] (+0.66, fdr 7e-06), [[ENC1]] (+0.65, fdr 7e-06); moves opposite to [[QPCTL]] (-0.68, fdr 7e-06), [[ZNF500]] (-0.68, fdr 1e-05), [[TULP3]] (-0.65, fdr 1e-05).
> It is in [[Module 197]], a single-armed module (Nervous system development).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MTNR1A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[BAHD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1386.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.78×** | +22.2 | 0e+00 | 30/45 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.47×** | +13.4 | 2e-38 | 33/45 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.10×** | +11.4 | 5e-28 | 30/45 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.95×** | +8.7 | 5e-16 | 40/46 (NCI-H1573, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +7.4 | 1e-11 | 37/45 (SW480, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +7.2 | 6e-11 | 29/45 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.20×** | +6.3 | 2e-08 | 32/45 (SW480, SW48, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +6.1 | 9e-08 | 31/45 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +5.4 | 4e-06 | 26/45 (RPMI-7951, H4, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +5.2 | 1e-05 | 26/45 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +4.8 | 7e-05 | 24/44 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.40×** | +4.8 | 9e-05 | 22/42 (SK-MEL-2, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.8 | 0.006 | 21/36 (HOP62, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.27×** | +3.7 | 0.008 | 25/45 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.30×** | +3.7 | 0.008 | 28/45 (C32, SW1417, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.011 | 23/46 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.029 | 20/45 (SK-MEL-2, PANC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.034 | 19/44 (C32, HOP62, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.044 | 21/45 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.24×** | +3.0 | 0.060 | 18/46 (SW480, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1386.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.609×** | -10.8 | 1e-24 | 36/46 (LS 180, COLO 205, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.602×** | -7.5 | 1e-11 | 35/44 (SHP-77, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.745×** | -4.6 | 1e-03 | 28/45 (SW48, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.748×** | -4.3 | 0.002 | 24/45 (LS 180, KATO III, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Retinoic acid (drug)]] 5 µM |  | **0.822×** | -4.3 | 0.002 | 25/46 (CFPAC-1, BT-474, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -4.2 | 0.003 | 27/47 (LS 180, SW48, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.771×** | -3.9 | 0.009 | 35/46 (SW 1088, HepG2/C3A, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.784×** | -3.8 | 0.011 | 28/45 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.784×** | -3.8 | 0.011 | 25/45 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.786×** | -3.7 | 0.011 | 24/45 (LoVo, LS 180, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.744×** | -3.3 | 0.056 | 26/45 (SHP-77, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.866× | -3.2 | 0.075 | 14/46 (SHP-77, COLO 205, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.817×** | -3.1 | 0.075 | 24/45 (SW1417, SK-MEL-2, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.819×** | -3.1 | 0.079 | 22/45 (BT-474, C-33 A, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.871× | -3.0 | 0.089 | 14/45 (A498, H4, …) | rises with dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **0.823×** | -3.0 | 0.089 | 21/45 (NCI-H460, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1386. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 219 | 16 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +27.3) | — |
| [[HOP62 (line)]] | alt | 172 | 12 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +35.8) | — |
| [[LS 180 (line)]] | wt | 1,937 | 0 | 12 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -23.5) |
| [[SW48 (line)]] | wt | 893 | 5 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +18.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -15.9) |
| [[SNU-423 (line)]] | alt | 134 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +32.6) | — |
| [[SW 900 (line)]] | alt | 389 | 10 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +17.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.320× (z -8.9) ⚠ toxic |
| [[A549 (line)]] | wt | 223 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.5× (z +34.1) | — |
| [[NCI-H1573 (line)]] | alt | 332 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +36.1) | — |
| [[A-172 (line)]] | wt | 207 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +21.8) | — |
| [[A498 (line)]] | wt | 636 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +20.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -14.9) |
| [[RPMI-7951 (line)]] | alt | 230 | 7 (2 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 12.5× (z +22.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -12.0) |
| [[H4 (line)]] | wt | 195 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.92× (z +15.8) | — |
| [[LoVo (line)]] | wt | 1,294 | 1 | 6 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.74× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.226× (z -17.2) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -16.9) |
| [[PANC-1 (line)]] | alt | 255 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.56× (z +32.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -9.7) |
| [[SNU-1 (line)]] | wt | 372 | 5 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.8× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[SW480 (line)]] | alt | 218 | 5 | 1 | [[PH-797804 (drug)]] 5 µM 7.35× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -13.1) |
| [[A-427 (line)]] | wt | 274 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.64× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.360× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.467× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 264 | 5 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.50× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 433 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +19.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 283 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +20.8) | — |
| [[SK-MEL-2 (line)]] | alt | 159 | 5 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.29× (z +14.8) | — |
| [[BT-474 (line)]] | alt | 171 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +15.5) | — |
| [[CFPAC-1 (line)]] | alt | 315 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +34.7) | — |
| [[KATO III (line)]] | alt | 855 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -16.3) |
| [[LOX-IMVI (line)]] | wt | 227 | 3 | 1 | [[Harringtonine (drug)]] 5 µM 2.82× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -10.0) |
| [[SHP-77 (line)]] | alt | 428 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -14.9) |
| [[C32 (line)]] | wt | 187 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 5.22× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 558 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +23.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -20.0) |
| [[HCT15 (line)]] | alt | 1,720 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -18.3) |
| [[HepG2_C3A (line)]] | wt | 668 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -10.6) |
| [[J82 (line)]] | alt | 230 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +19.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 213 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +16.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 97.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +18.3) | — |
| [[SW1417 (line)]] | alt | 658 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -17.9) |
| [[HT-29 (line)]] | alt | 544 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -15.5) |
| [[RKO (line)]] | wt | 157 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.72× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.438× (z -9.0) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 268 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +13.1) | — |
| [[C-33 A (line)]] | alt | 323 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 121 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | — |
| [[Panc 03.27 (line)]] | alt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.5) | — |
| [[AN3 CA (line)]] | alt | 56.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 197 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 91.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 289 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 88.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 380 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 296 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1386), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*33 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK6]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[IRS1]] | +0.66 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ENC1]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[NAB1]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[BBS10]] | +0.62 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[HNRNPK]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[TMEM185B]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PLCB4]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[TRIM44]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[CDH2]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[GPR39]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[THBS1]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*67 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QPCTL]] | -0.68 | -0.58 / -0.69 | both halves | 7e-06 |  |
| [[ZNF500]] | -0.68 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[TULP3]] | -0.65 | -0.56 / -0.68 | both halves | 1e-05 |  |
| [[PPOX]] | -0.65 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[RUFY2]] | -0.64 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[IL17RA]] | -0.64 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[ATXN3]] | -0.62 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[RAB6A]] | -0.61 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[NDUFAF7]] | -0.61 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[LMBR1L]] | -0.61 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[GET1-SH3BGR]] | -0.61 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[MFSD8]] | -0.61 | -0.56 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTNR1A]] | B | MTNR1A activity raises FAT1's level | lines that do not express MTNR1A (7) vs lines expressing it (43) | 2.82× lower at baseline in the lines without MTNR1A | 0.006 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[KITLG]] | B | KITLG activity raises FAT1's level | lines that do not express KITLG (10) vs lines expressing it (40) | 1.96× lower at baseline in the lines without KITLG | 0.040 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[LMO7]] | B | LMO7 activity raises FAT1's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 1.94× lower at baseline in the lines without LMO7 | 0.091 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[AHR]] | B | AHR activity raises FAT1's level | lines that do not express AHR (7) vs lines expressing it (43) | 1.66× lower at baseline in the lines without AHR | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[TOP2A]] | B | TOP2A activity raises FAT1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[AP1S3]] | C | AP1S3 activity raises FAT1's level | lines that do not express AP1S3 (4) vs lines expressing it (46) | 1.65× lower at baseline in the lines without AP1S3 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02842, ENSG00000236283, LRIF1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BAHD1]] | C | FAT1 activity lowers BAHD1's level | lines that do not express FAT1 (3) vs lines expressing it (47) | 1.72× higher at baseline in the lines without FAT1 | 0.067 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ARHGAP15, CDKN1A, CYP2E1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 197]] — Nervous system development; 16 genes; every member is in the + arm (projection on the module's main direction 0.760). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.2, -3.9); signed map (22.7, 34.8). **Vector** length 144, 47.4% of its response variance represented; |z| ≥ 3 in 1,532 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +12.2 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | +12.2 | +1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | +11.8 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +11.3 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.5 | +22.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.8 | +3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.5 | +2.7 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +4.1 | +3.0 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.5 | -3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.4 | -2.3 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -3.6 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -0.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.5 | -3.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | FAT atypical cadherin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.2 — chr4:186,587,794-186,726,722 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDHF7, CDHR8; previously FAT |
| Gene groups (HGNC) | Cadherin related |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14517](https://www.uniprot.org/uniprotkb/Q14517) (Protocadherin Fat 1):

> [Protocadherin Fat 1]: Plays an essential role for cellular polarization, directed cell migration and modulating cell-cell contact.

**Summary**, from NCBI Gene [2195](https://www.ncbi.nlm.nih.gov/gene/2195):

> This gene is an ortholog of the Drosophila fat gene, which encodes a tumor suppressor essential for controlling cell proliferation during Drosophila development. The gene product is a member of the cadherin superfamily, a group of integral membrane proteins characterized by the presence of cadherin-type repeats. In addition to containing 34 tandem cadherin-type repeats, the gene product has five epidermal growth factor (EGF)-like repeats and one laminin A-G domain. This gene is expressed at …

**Accessions** — [HGNC:3595](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3595) · Entrez [2195](https://www.ncbi.nlm.nih.gov/gene/2195) · UniProt [Q14517](https://www.uniprot.org/uniprotkb/Q14517) · Ensembl [ENSG00000083857](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083857)

## Data

Gene col 1386: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1386); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1386, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1386]; `tensor/DDL_lfc|DDL_z.npy` [1386]; `embed/gene_vectors.npy` [1386]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1386 or target_col == 1386). Every well: [[FAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
