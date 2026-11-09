---
symbol: "TCP1"
type: "gene"
col: 4183
ensembl_id: "ENSG00000120438"
name: "t-complex 1"
location: "6q25.3"
module: 60
arm: "+"
pooled_cpm: 102.38
n_lines_expressing: 50
n_dd_up: 40
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# TCP1

*t-complex 1* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (25 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.88× (z +18.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Posaconazole (drug)]] 5 µM: 0.783× (z -4.0, q 0.020, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCT3]] (+0.77, fdr 7e-06), [[AHSA1]] (+0.76, fdr 7e-06), [[STIP1]] (+0.76, fdr 7e-06); moves opposite to [[TNRC6C]] (-0.72, fdr 7e-06), [[LRCH3]] (-0.68, fdr 7e-06), [[UNK]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 29 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 25 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4183.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.88×** | +18.0 | 0e+00 | 48/48 (SW1417, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.71×** | +17.0 | 0e+00 | 47/49 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.62×** | +16.4 | 0e+00 | 48/48 (A-172, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.59×** | +16.2 | 0e+00 | 48/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.69×** | +16.2 | 0e+00 | 43/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.70×** | +14.9 | 0e+00 | 48/48 (SW1417, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.65×** | +11.5 | 7e-29 | 45/45 (SW1417, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.95×** | +11.4 | 4e-28 | 48/48 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.99×** | +11.3 | 1e-27 | 44/47 (NCI-H460, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.01×** | +11.0 | 3e-26 | 38/45 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.80×** | +10.0 | 1e-21 | 46/48 (SNU-423, LoVo, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.90×** | +9.5 | 1e-19 | 47/49 (PANC-1, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.73×** | +9.3 | 4e-19 | 45/48 (A-172, SNU-423, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.97×** | +8.2 | 6e-15 | 45/49 (SW1417, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.34×** | +7.6 | 2e-12 | 46/48 (C32, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +4.8 | 4e-05 | 24/48 (NCI-H2347, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Infigratinib (drug)]] 5 µM |  | **1.64×** | +4.4 | 2e-04 | 38/48 (SW1417, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.27×** | +4.0 | 0.001 | 26/47 (HOP62, NCI-H460, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.002 | 24/48 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.002 | 26/48 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.002 | 23/48 (SK-MEL-2, HEC-1-A, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.5 | 0.008 | 18/49 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.15× | +3.3 | 0.013 | 11/49 (A-172, KATO III, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4183.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Posaconazole (drug)]] 5 µM |  | **0.783×** | -4.0 | 0.020 | 27/48 (AsPC-1, NCI-H2347, …) | top dose only | plate-row cell shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.794×** | -4.0 | 0.020 | 31/48 (KATO III, HCT15, …) | two highest doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 0.857× | -3.7 | 0.035 | 18/48 (LS 180, HCT15, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.749×** | -3.5 | 0.056 | 25/48 (CHP-212, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 0.826× | -3.3 | 0.11 | 23/48 (NCI-H23, A549, …) | inconsistent across doses | position effect removed |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.827× | -3.2 | 0.15 | 20/48 (CFPAC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift |
| [[Ponatinib (drug)]] 5 µM |  | 0.839× | -3.0 | 0.19 | 22/48 (RKO, J82, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4183. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 80.9 | 14 (12 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.88× (z +17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.54× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 124 | 12 (8 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.78× (z +14.6) | — |
| [[A-172 (line)]] | wt | 72.6 | 11 (7 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.04× (z +18.3) | — |
| [[KATO III (line)]] | alt | 116 | 9 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.04× (z +17.6) | — |
| [[LoVo (line)]] | wt | 115 | 9 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.07× (z +15.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 118 | 9 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.13× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.26× (z +13.8) | — |
| [[PANC-1 (line)]] | alt | 128 | 9 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.78× (z +13.5) | — |
| [[SW480 (line)]] | alt | 151 | 8 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.78× (z +15.1) | — |
| [[CFPAC-1 (line)]] | alt | 52.5 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.37× (z +15.3) | — |
| [[HOP62 (line)]] | alt | 72.5 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.30× (z +12.1) | — |
| [[Hs 766T (line)]] | wt | 79.5 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.86× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.98× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 89.0 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.37× (z +15.2) | — |
| [[RKO (line)]] | wt | 110 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.87× (z +13.5) | — |
| [[HS-578T (line)]] | alt | 112 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.96× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 104 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.58× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 118 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.34× (z +18.3) | — |
| [[A-427 (line)]] | wt | 188 | 4 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.68× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.47× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 58.1 | 5 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.90× (z +14.1) | — |
| [[HEC-1-A (line)]] | alt | 88.9 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.99× (z +14.9) | — |
| [[LS 180 (line)]] | wt | 95.6 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.41× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 83.2 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.79× (z +11.5) | — |
| [[SK-MEL-2 (line)]] | alt | 95.3 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.99× (z +10.6) | — |
| [[A498 (line)]] | wt | 113 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.77× (z +11.9) | — |
| [[A549 (line)]] | wt | 82.5 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.10× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HCT15 (line)]] | alt | 141 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.74× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 76.9 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.93× (z +12.0) | — |
| [[J82 (line)]] | alt | 111 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.96× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 79.2 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +13.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 106 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.04× (z +12.1) | — |
| [[COLO 205 (line)]] | alt | 35.2 | 3 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 7.24× (z +11.8) ⚠ toxic; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H23 (line)]] | alt | 102 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.83× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.37× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 71.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.76× (z +12.8) | — |
| [[SNU-1 (line)]] | wt | 85.0 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.79× (z +13.9) | — |
| [[SW 900 (line)]] | alt | 101 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.72× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 68.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 6.45× (z +17.9) | — |
| [[C-33 A (line)]] | alt | 119 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.85× (z +12.7) | — |
| [[SHP-77 (line)]] | alt | 133 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[AN3 CA (line)]] | alt | 187 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.51× (z +12.8) | — |
| [[H4 (line)]] | wt | 58.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.99× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HepG2_C3A (line)]] | wt | 127 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +8.8) ⚠ cell-cycle shift, explains ~88% of this change | — |
| [[NCI-H1573 (line)]] | alt | 54.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW 1088 (line)]] | alt | 79.0 | 0 | 1 | — | [[Vortioxetine (drug)]] 0.05 µM 0.0639× (z -9.8) |
| [[SW 1271 (line)]] | alt | 105 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0966× (z -11.7) |
| [[SW48 (line)]] | wt | 126 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[AsPC-1 (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 141 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4183), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT3]] | +0.77 | +0.78 / +0.72 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[AHSA1]] | +0.76 | +0.70 / +0.78 | both halves | 7e-06 | STRING 529 |
| [[STIP1]] | +0.76 | +0.71 / +0.78 | both halves | 7e-06 | STRING 968 |
| [[CCT4]] | +0.75 | +0.79 / +0.71 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[HSPA8]] | +0.75 | +0.74 / +0.71 | both halves | 7e-06 | STRING 931 |
| [[HSPD1]] | +0.72 | +0.74 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 958 |
| [[HSP90AB1]] | +0.72 | +0.72 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 956 |
| [[CCT6A]] | +0.72 | +0.74 / +0.68 | both halves | 7e-06 | same gene group; pathway: Association of TriC/CCT with target proteins during biosynthesis; STRING 999 |
| [[GPN1]] | +0.72 | +0.71 / +0.67 | both halves | 7e-06 | STRING 549 |
| [[HSP90AA1]] | +0.71 | +0.66 / +0.73 | both halves | 7e-06 | pathway: Assembly of the 9+0 primary cilium; STRING 906 |
| [[PSMD2]] | +0.70 | +0.70 / +0.65 | both halves | 7e-06 | STRING 796 |
| [[CACYBP]] | +0.70 | +0.72 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6C]] | -0.72 | -0.72 / -0.62 | both halves | 7e-06 | pathway: Cilium Assembly |
| [[LRCH3]] | -0.68 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[UNK]] | -0.67 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[RBX1]] | -0.61 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[HMGCL]] | -0.59 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[LIPT1]] | -0.59 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[CHKB]] | -0.59 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[ZCCHC3]] | -0.59 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[POLR1H]] | -0.58 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[PURA]] | -0.58 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[FOXA2]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[POLR2L]] | -0.58 | -0.62 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.781). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-20.2, -11.9); signed map (-26.7, -29.4). **Vector** length 92.6, 34.1% of its response variance represented; |z| ≥ 3 in 1,521 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Attenuation phase* (reactome, mean cos +0.52 to 13); *HSF1-dependent transactivation* (reactome, mean cos +0.51 to 14); *HSF1 activation* (reactome, mean cos +0.51 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.3 | +14.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.7 | +18.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.3 | +16.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.1 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +16.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.0 | +8.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +7.6 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +2.0 | +0.6 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -7.9 | +3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.6 | +1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | -6.2 | +5.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | -5.5 | +4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -5.1 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.8 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -1.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.7 | +0.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.2 | -0.1 |
|  | [[EX229 (drug)]] 0.5 µM |  | -2.2 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | t-complex 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:159,778,498-159,789,703 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D6S230E, CCT1, Ccta |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes; Chaperonin containing TCP1 |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 18 pathways, smallest: Folding of actin by CCT/TriC; Formation of tubulin folding intermediates by CCT/TriC; BBSome-mediated cargo-targeting to cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [P17987](https://www.uniprot.org/uniprotkb/P17987) (T-complex protein 1 subunit alpha):

> Component of the chaperonin-containing T-complex (TRiC), a molecular chaperone complex that assists the folding of actin, tubulin and other proteins upon ATP hydrolysis. The TRiC complex mediates the folding of WRAP53/TCAB1, thereby regulating telomere maintenance. As part of the TRiC complex may play a role in the assembly of BBSome, a complex involved in ciliogenesis regulating transports vesicles to the cilia.

**Summary**, from NCBI Gene [6950](https://www.ncbi.nlm.nih.gov/gene/6950):

> The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including actin and tubulin. Alternate transcriptional splice variants of this gene, encoding …

**Accessions** — [HGNC:11655](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11655) · Entrez [6950](https://www.ncbi.nlm.nih.gov/gene/6950) · UniProt [P17987](https://www.uniprot.org/uniprotkb/P17987) · Ensembl [ENSG00000120438](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120438)

## Data

Gene col 4183: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4183); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4183, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4183]; `tensor/DDL_lfc|DDL_z.npy` [4183]; `embed/gene_vectors.npy` [4183]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4183 or target_col == 4183). Every well: [[TCP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
