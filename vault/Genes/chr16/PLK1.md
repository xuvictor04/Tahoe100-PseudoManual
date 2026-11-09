---
symbol: "PLK1"
type: "gene"
col: 9372
ensembl_id: "ENSG00000166851"
name: "polo like kinase 1"
location: "16p12.2"
module: 22
arm: "+"
pooled_cpm: 15.66
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 29
n_dd_up_clean: 10
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# PLK1

*polo like kinase 1* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.73× (z +10.2, q 8e-22, up in 32 of 46 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.03× (z +9.5, q 2e-19, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (14 with an alert ⚠); the strongest is [[Cytarabine (drug)]] 5 µM: 0.395× (z -11.7, q 1e-28, down in 39 of 46 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Amsacrine (drug)]] 5 µM: 0.627× (z -8.6, q 2e-15, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNB1]] (+0.93, fdr 7e-06), [[CCNB2]] (+0.91, fdr 7e-06), [[KIF20A]] (+0.90, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9372.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.73×** | +10.2 | 8e-22 | 32/46 (NCI-H2030, PANC-1, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | **2.16×** | +9.9 | 9e-21 | 34/45 (HOP62, SW1417, …) | all doses, flat | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **4.03×** | +9.5 | 2e-19 | 41/48 (NCI-H2030, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.88×** | +8.0 | 2e-13 | 32/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.65×** | +6.7 | 3e-09 | 28/46 (HEC-1-A, LOX-IMVI, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.61×** | +6.3 | 3e-08 | 26/47 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.37×** | +5.9 | 3e-07 | 30/48 (SHP-77, CFPAC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.37×** | +5.9 | 3e-07 | 25/48 (HT-29, J82, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +5.6 | 2e-06 | 19/37 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.12×** | +5.2 | 1e-05 | 21/45 (J82, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.9 | 4e-05 | 4/48 (HOP62, SNU-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 1e-04 | 19/47 (HOP62, H4, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 1e-04 | 15/47 (SNU-423, SW 900, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.37×** | +3.9 | 0.005 | 16/47 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.34×** | +3.8 | 0.005 | 16/47 (PANC-1, H4, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.34×** | +3.7 | 0.006 | 13/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.012 | 14/48 (HT-29, CFPAC-1, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.016 | 20/47 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.05 µM |  | **1.27×** | +2.9 | 0.080 | 6/48 (SW 900, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 15 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9372.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.395×** | -11.7 | 1e-28 | 39/46 (A-427, NCI-H661, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.627×** | -8.6 | 2e-15 | 34/48 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.538×** | -8.1 | 9e-14 | 36/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.535×** | -7.9 | 5e-13 | 29/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.549×** | -7.8 | 5e-13 | 34/48 (A549, A-427, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.563×** | -7.5 | 6e-12 | 28/47 (LS 180, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.580×** | -7.1 | 9e-11 | 27/47 (HS-578T, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.587×** | -7.0 | 2e-10 | 25/47 (A-172, LOX-IMVI, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.591×** | -6.9 | 4e-10 | 30/46 (A-427, PANC-1, …) | two highest doses |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.682×** | -6.7 | 1e-09 | 27/48 (NCI-H460, A-427, …) | all doses, flat |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.400×** | -6.3 | 2e-08 | 31/46 (LOX-IMVI, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.612×** | -6.1 | 6e-08 | 27/47 (PANC-1, SW480, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.608×** | -6.0 | 9e-08 | 27/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.634×** | -6.0 | 1e-07 | 26/48 (LOX-IMVI, LS 180, …) | two highest doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.638×** | -5.4 | 2e-06 | 21/47 (LoVo, A-427, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.668×** | -5.3 | 5e-06 | 26/47 (C32, A-427, …) | top dose only |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | **0.710×** | -4.5 | 2e-04 | 20/48 (Hs 766T, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.731×** | -4.1 | 0.001 | 19/47 (SW48, A-172, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.750×** | -3.8 | 0.005 | 11/46 (hTERT-HPNE, HT-29, …) | all doses, flat | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.757×** | -3.6 | 0.007 | 18/47 (A-427, H4, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.678×** | -3.6 | 0.007 | 12/48 (HCT15, SNU-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.748×** | -3.5 | 0.011 | 20/46 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Trimetrexate (drug)]] 5 µM |  | **0.827×** | -3.5 | 0.011 | 13/48 (SW480, LoVo, …) | top dose only |  |
| [[Amsacrine (drug)]] 0.5 µM |  | **0.767×** | -3.4 | 0.012 | 15/48 (A549, SW48, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.852× | -2.9 | 0.065 | 8/48 (HT-29, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.62 per unit of S-phase module lfc, +1.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9372. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 13.8 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +14.1) ⚠ cell-cycle shift, would explain all of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.261× (z -9.5) ⚠ cell-cycle shift, explains ~63% of this change |
| [[A-427 (line)]] | wt | 27.8 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.231× (z -12.2) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 23.8 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.339× (z -8.6) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A549 (line)]] | wt | 17.3 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | [[Amsacrine (drug)]] 5 µM 0.273× (z -9.5) |
| [[J82 (line)]] | alt | 23.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | [[Bortezomib (drug)]] 5 µM 0.0703× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~71% of this change |
| [[NCI-H2030 (line)]] | alt | 16.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +14.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[COLO 205 (line)]] | alt | 6.59 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.05 µM 0.0469× (z -9.1) |
| [[H4 (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0777× (z -9.6) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HEC-1-A (line)]] | alt | 19.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 18.0 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 4.20× (z +8.7) ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[Hs 766T (line)]] | wt | 16.6 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.202× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 15.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.153× (z -9.7) ⚠ cell-cycle shift, explains ~57% of this change |
| [[LS 180 (line)]] | wt | 17.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0943× (z -11.1) ⚠ cell-cycle shift, explains ~57% of this change |
| [[MIA PaCa-2 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Sapanisertib (drug)]] 0.05 µM 0.117× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 12.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 16.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 16.3 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0539× (z -10.1) |
| [[SW1417 (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +11.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW48 (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.105× (z -9.3) ⚠ cell-cycle shift, explains ~63% of this change |
| [[A-172 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9372), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNB1]] | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | pathway: APC/C-mediated degradation of cell cycle proteins; STRING 999 |
| [[CCNB2]] | +0.91 | +0.90 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 995 |
| [[KIF20A]] | +0.90 | +0.87 / +0.92 | both halves | 7e-06 | pathway: Mitotic Telophase/Cytokinesis; STRING 990 |
| [[KNSTRN]] | +0.90 | +0.90 / +0.89 | both halves | 7e-06 | STRING 660 |
| [[CDC20]] | +0.90 | +0.90 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[AURKA]] | +0.88 | +0.91 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 997 |
| [[DEPDC1]] | +0.87 | +0.86 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 600 |
| [[TROAP]] | +0.86 | +0.82 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 805 |
| [[CCNA2]] | +0.86 | +0.85 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 958 |
| [[BUB1]] | +0.86 | +0.83 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 996 |
| [[ARHGAP11A]] | +0.86 | +0.85 / +0.85 | both halves | 7e-06 | STRING 532 |
| [[DLGAP5]] | +0.86 | +0.83 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 807 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PLK1's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.8% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PIMREG]] | B | PIMREG activity raises PLK1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.87× lower at baseline in the lines without PIMREG | 0.028 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises PLK1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.01× lower at baseline in the lines without AURKB | 0.043 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[FAM72D]] | C | FAM72D activity raises PLK1's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 1.92× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises PLK1's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.04× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[CDC20]] | C | CDC20 activity raises PLK1's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.12× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.853). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.1, -57.5); signed map (-51.5, -43.4). **Vector** length 135, 40.8% of its response variance represented; |z| ≥ 3 in 1,385 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Condensation of Prometaphase Chromosomes* (reactome, mean cos +0.72 to 8); *APC/C:Cdc20 mediated degradation of mitotic proteins* (reactome, mean cos +0.73 to 12); *spermatogenesis* (hallmark, mean cos +0.70 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | +8.5 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.5 | +10.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | +5.8 | +8.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +9.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.0 | +5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +6.7 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.9 | +5.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +3.1 | +3.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.0 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +1.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | -6.4 | -7.1 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -6.3 | -11.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -6.3 | -7.9 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -5.7 | -8.1 |
|  | [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -5.6 | -7.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -5.2 | -8.6 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -4.4 | -5.4 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -4.2 | -6.7 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -4.1 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | polo like kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.2 — chr16:23,677,656-23,690,367 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PLK |
| Gene groups (HGNC) | Polo like kinase family |
| Hallmark sets | MYC_TARGETS_V2, MTORC1_SIGNALING, G2M_CHECKPOINT, MITOTIC_SPINDLE, E2F_TARGETS |
| Reactome | 49 pathways, smallest: Phosphorylation of Emi1; Activation of NIMA Kinases NEK9, NEK6, NEK7; Mitotic Telophase/Cytokinesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P53350](https://www.uniprot.org/uniprotkb/P53350) (Serine/threonine-protein kinase PLK1):

> Serine/threonine-protein kinase that performs several important functions throughout M phase of the cell cycle, including the regulation of centrosome maturation and spindle assembly, the removal of cohesins from chromosome arms, the inactivation of anaphase-promoting complex/cyclosome (APC/C) inhibitors, and the regulation of mitotic exit and cytokinesis. Polo-like kinase proteins act by binding and phosphorylating proteins that are already phosphorylated on a specific motif recognized by the …

**Summary**, from NCBI Gene [5347](https://www.ncbi.nlm.nih.gov/gene/5347):

> The Ser/Thr protein kinase encoded by this gene belongs to the CDC5/Polo subfamily. It is highly expressed during mitosis and elevated levels are found in many different types of cancer. Depletion of this protein in cancer cells dramatically inhibited cell proliferation and induced apoptosis; hence, it is a target for cancer therapy. [provided by RefSeq, Sep 2015]

**Accessions** — [HGNC:9077](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9077) · Entrez [5347](https://www.ncbi.nlm.nih.gov/gene/5347) · UniProt [P53350](https://www.uniprot.org/uniprotkb/P53350) · Ensembl [ENSG00000166851](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166851)

## Data

Gene col 9372: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9372); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9372, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9372]; `tensor/DDL_lfc|DDL_z.npy` [9372]; `embed/gene_vectors.npy` [9372]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9372 or target_col == 9372). Every well: [[PLK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
