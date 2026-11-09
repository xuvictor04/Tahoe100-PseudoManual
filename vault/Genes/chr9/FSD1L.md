---
symbol: "FSD1L"
type: "gene"
col: 2798
ensembl_id: "ENSG00000106701"
name: "fibronectin type III and SPRY domain containing 1 like"
location: "9q31.2"
module: 17
arm: "+"
pooled_cpm: 66.01
n_lines_expressing: 47
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 27
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# FSD1L

*fibronectin type III and SPRY domain containing 1 like* — 9q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.45× (z +6.3, q 2e-07, up in 34 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.391× (z -20.6, q 0e+00, down in 44 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC7B]] (+0.63, fdr 7e-06), [[PRXL2C]] (+0.61, fdr 9e-06), [[CCSER2]] (+0.59, fdr 3e-05); moves opposite to [[TPCN1]] (-0.53, fdr 1e-05), [[SRGAP3]] (-0.51, fdr 3e-05), [[TTC41P]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 27 go from it, the strongest it → [[FBXL2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2798.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.45×** | +6.3 | 2e-07 | 34/44 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.41×** | +6.0 | 4e-07 | 31/44 (NCI-H2030, SW480, …) | rises with dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.27×** | +5.1 | 7e-05 | 28/45 (C32, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.32×** | +4.9 | 1e-04 | 24/45 (SW1417, SW480, …) | all doses, flat |  |
| [[Neratinib (drug)]] 5 µM |  | **1.29×** | +4.5 | 7e-04 | 21/45 (NCI-H460, hTERT-HPNE, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.27×** | +4.3 | 0.002 | 21/45 (SW480, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.32×** | +4.1 | 0.003 | 22/45 (SW480, C32, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +4.0 | 0.004 | 19/45 (HOP62, C32, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.24×** | +3.8 | 0.009 | 19/45 (SW1417, PANC-1, …) | all doses, flat |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.030 | 17/45 (SW1417, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.093 | 13/45 (LoVo, BT-474, …) | rises with dose |  |
| [[Baicalin (drug)]] 5 µM |  | 1.15× | +3.1 | 0.098 | 5/46 (LOX-IMVI, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2798.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.391×** | -20.6 | 0e+00 | 44/45 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.464×** | -13.5 | 2e-39 | 38/46 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.488×** | -12.2 | 7e-32 | 29/40 (SK-MEL-2, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.557×** | -9.6 | 2e-19 | 26/43 (A-172, C32, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.594×** | -9.2 | 5e-18 | 35/45 (HEC-1-A, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.597×** | -8.7 | 2e-16 | 31/47 (A-172, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.700×** | -7.9 | 2e-13 | 29/45 (LOX-IMVI, HOP62, …) | top dose only | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -6.7 | 2e-09 | 28/45 (A-172, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.713×** | -6.0 | 2e-07 | 27/45 (A-172, HS-578T, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~65% of this change | **0.776×** | -4.5 | 4e-04 | 24/45 (Hs 766T, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.805×** | -4.4 | 4e-04 | 25/45 (A-172, HOP62, …) | top dose only | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.619×** | -4.0 | 0.003 | 20/44 (BT-474, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 0.852× | -3.5 | 0.019 | 19/45 (hTERT-HPNE, NCI-H23, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.839× | -3.1 | 0.078 | 16/45 (HOP62, HS-578T, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 0.843× | -3.0 | 0.10 | 17/45 (SW48, LOX-IMVI, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2798. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 186 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -20.4) |
| [[LOX-IMVI (line)]] | wt | 112 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -18.0) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -17.3) |
| [[MIA PaCa-2 (line)]] | alt | 98.1 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -13.3) |
| [[HEC-1-A (line)]] | alt | 109 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -15.8) |
| [[HS-578T (line)]] | alt | 81.1 | 1 (1 ⚠) | 5 (4 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.66× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -16.6) |
| [[HOP62 (line)]] | alt | 80.8 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -15.0) |
| [[J82 (line)]] | alt | 126 | 1 (1 ⚠) | 4 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.40× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 69.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -11.1) |
| [[SW1417 (line)]] | alt | 54.4 | 4 (4 ⚠) | 1 | [[Selinexor (drug)]] 0.05 µM 3.26× (z +11.1) ⚠ cell-cycle shift, explains ~43% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -12.8) |
| [[A498 (line)]] | wt | 60.9 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A549 (line)]] | wt | 106 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -16.7) |
| [[C32 (line)]] | wt | 55.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -11.3) |
| [[SNU-423 (line)]] | alt | 79.1 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -14.4) |
| [[AsPC-1 (line)]] | alt | 75.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -16.0) |
| [[C-33 A (line)]] | alt | 110 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[Hs 766T (line)]] | wt | 131 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -15.5) |
| [[NCI-H1792 (line)]] | alt | 66.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -10.3) |
| [[NCI-H596 (line)]] | alt | 62.8 | 2 | 1 | [[Methylthiouracil (drug)]] 0.05 µM 2.31× (z +17.4) | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.596× (z -11.1) |
| [[RKO (line)]] | wt | 146 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -10.9) |
| [[PANC-1 (line)]] | alt | 52.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -10.6) |
| [[SW48 (line)]] | wt | 41.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -10.2) |
| [[AN3 CA (line)]] | alt | 90.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -10.3) |
| [[BT-474 (line)]] | alt | 31.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 19.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +8.7) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[HepG2_C3A (line)]] | wt | 44.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.290× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~14% of this change |
| [[NCI-H23 (line)]] | alt | 55.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H2347 (line)]] | alt | 33.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 39.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -16.4) |
| [[RPMI-7951 (line)]] | alt | 83.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -10.3) |
| [[SW 1271 (line)]] | alt | 87.6 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.102× (z -9.5) |
| [[SW480 (line)]] | alt | 60.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -12.0) |
| [[A-427 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.23 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.54 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.6 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 87.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2798), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC7B]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[PRXL2C]] | +0.61 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[CCSER2]] | +0.59 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[SVIL-AS1-1]] | +0.59 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[MTMR9]] | +0.57 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[STX2]] | +0.57 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[FBXL2]] | +0.56 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[PRELID3A]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[SLC15A4]] | +0.54 | +0.66 / +0.38 | both halves | 7e-05 |  |
| [[KIF3C]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[SLC25A43]] | +0.54 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[LIMK1]] | +0.54 | +0.66 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPCN1]] | -0.53 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[SRGAP3]] | -0.51 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[TTC41P]] | -0.49 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[IQCD]] | -0.48 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[PHF8]] | -0.47 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[OARD1]] | -0.46 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[TM9SF3]] | -0.45 | -0.24 / -0.41 | both halves | 4e-04 |  |
| [[PIPOX]] | -0.45 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[COPB2]] | -0.44 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[STX5]] | -0.44 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[ALG11]] | -0.44 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FSD1L's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SACS]] | B | SACS activity raises FSD1L's level | lines that do not express SACS (5) vs lines expressing it (45) | 3.62× lower at baseline in the lines without SACS | 0.058 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity lowers FSD1L's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DENND5A]], [[SPIRE1]] | C | DENND5A, SPIRE1 activity raises FSD1L's level | lines that do not express DENND5A, SPIRE1 (3) vs lines expressing them (47) | 4.09× lower at baseline in the lines without DENND5A, SPIRE1 | 0.015 | ⚠ few lines (3 vs 47); across organs; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23; co-absent with the target; co-absent genes |
| [[USP31]] | C | USP31 activity raises FSD1L's level | lines that do not express USP31 (3) vs lines expressing it (47) | 3.49× lower at baseline in the lines without USP31 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 0, C 27. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXL2]] | C | FSD1L activity raises FBXL2's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 8.09× lower at baseline in the lines without FSD1L | 0.002 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| [[SPIRE1]] | C | FSD1L activity raises SPIRE1's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 4.79× lower at baseline in the lines without FSD1L | 0.003 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent; co-absent with the target |
| [[CPNE2]] | C | FSD1L activity raises CPNE2's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 4.44× lower at baseline in the lines without FSD1L | 0.003 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent; co-absent with the target |
| [[OARD1]] | C | FSD1L activity lowers OARD1's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 2.62× higher at baseline in the lines without FSD1L | 0.004 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| [[DENND5A]] | C | FSD1L activity raises DENND5A's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 4.80× lower at baseline in the lines without FSD1L | 0.004 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent; co-absent with the target |
| [[STX2]] | C | FSD1L activity raises STX2's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 3.93× lower at baseline in the lines without FSD1L | 0.004 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| cells under [[Lonafarnib (drug)]] 5 µM | C | FSD1L, [[NAB2]] activity raises the cells' numbers under Lonafarnib 5 µM (protects the cells) | lines that do not express FSD1L, NAB2 (3) vs lines expressing them (45) | the lines without FSD1L, NAB2: 0.09× the cells of the other lines | 0.013 | ⚠ few lines (3 vs 47); across organs; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent; co-absent genes |
| [[TTC7B]] | C | FSD1L activity raises TTC7B's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 7.45× lower at baseline in the lines without FSD1L | 0.015 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| [[UBE2Q2P1]] | C | FSD1L activity raises UBE2Q2P1's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 2.72× lower at baseline in the lines without FSD1L | 0.016 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| [[SACS]] | C | FSD1L activity raises SACS's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 4.28× lower at baseline in the lines without FSD1L | 0.022 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| [[PPP3CC]] | C | FSD1L activity strengthens PPP3CC's drug response | lines that do not express FSD1L (3) vs lines expressing it (45) | the lines without FSD1L respond 0.42× as strongly (z diff +3.68); strongest at Idarubicin (hydrochloride) 5 µM: 1.00x vs 0.63x (z diff +5.5) | 0.026 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[XPO6]] | C | FSD1L activity raises XPO6's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 1.83× lower at baseline in the lines without FSD1L | 0.026 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.288). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-4.9, -1.9); signed map (-21.9, -6.8). **Vector** length 106, 30.4% of its response variance represented; |z| ≥ 3 in 956 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +5.7 | +4.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.5 | +2.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.9 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.5 | +2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.9 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | -0.1 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.6 | +4.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -20.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -9.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -6.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -8.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.1 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -4.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | +1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | fibronectin type III and SPRY domain containing 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.2 — chr9:105,447,796-105,552,433 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CSDUFD1, CCDC10, FSD1NL, FSD1CL |
| Gene groups (HGNC) | Fibronectin type III domain containing |
| Matched by | ensembl_id |

UniProt [Q9BXM9](https://www.uniprot.org/uniprotkb/Q9BXM9) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:13753](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13753) · Entrez [83856](https://www.ncbi.nlm.nih.gov/gene/83856) · UniProt [Q9BXM9](https://www.uniprot.org/uniprotkb/Q9BXM9) · Ensembl [ENSG00000106701](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106701)

## Data

Gene col 2798: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2798); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2798, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2798]; `tensor/DDL_lfc|DDL_z.npy` [2798]; `embed/gene_vectors.npy` [2798]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2798 or target_col == 2798). Every well: [[FSD1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FSD1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
