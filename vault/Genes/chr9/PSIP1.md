---
symbol: "PSIP1"
type: "gene"
col: 9051
ensembl_id: "ENSG00000164985"
name: "PC4 and SRSF1 interacting protein 1"
location: "9p22.3"
module: 22
arm: "+"
pooled_cpm: 95.62
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# PSIP1

*PC4 and SRSF1 interacting protein 1* — 9p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.26× (z +19.6, q 0e+00, up in 46 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.46× (z +6.3, q 3e-08, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.721× (z -5.4, q 4e-05, down in 33 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.549× (z -5.2, q 6e-05, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DEK]] (+0.76, fdr 7e-06), [[CENPU]] (+0.69, fdr 7e-06), [[EZH2]] (+0.67, fdr 7e-06); moves opposite to [[ZNF778]] (-0.58, fdr 3e-05), [[GPN2]] (-0.57, fdr 3e-05), [[FBXO28]] (-0.57, fdr 1e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GGH]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9051.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.26×** | +19.6 | 0e+00 | 46/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.88×** | +16.9 | 0e+00 | 40/41 (SNU-423, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.37×** | +13.3 | 4e-38 | 41/43 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.49×** | +6.7 | 4e-09 | 35/46 (SW 900, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.47×** | +6.5 | 1e-08 | 29/46 (LOX-IMVI, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +6.3 | 3e-08 | 33/46 (LOX-IMVI, SW1417, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.45×** | +6.2 | 4e-08 | 30/46 (SW1417, LOX-IMVI, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +5.9 | 3e-07 | 26/46 (NCI-H2347, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.36×** | +5.2 | 1e-05 | 27/46 (LOX-IMVI, SW1417, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +4.9 | 5e-05 | 29/46 (AN3 CA, NCI-H2030, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | **1.34×** | +4.7 | 1e-04 | 30/45 (C32, HS-578T, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +4.4 | 5e-04 | 32/46 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 1.19× | +4.0 | 0.002 | 14/46 (HS-578T, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.29×** | +4.0 | 0.002 | 24/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.25×** | +3.6 | 0.010 | 24/46 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.43×** | +3.1 | 0.060 | 19/47 (NCI-H2347, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9051.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.721×** | -5.4 | 4e-05 | 33/46 (SW 900, HT-29, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.549×** | -5.2 | 6e-05 | 31/46 (RKO, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.581×** | -4.7 | 5e-04 | 25/47 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.619×** | -4.2 | 0.004 | 28/45 (SNU-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.788×** | -3.9 | 0.009 | 23/46 (Panc 03.27, SW480, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.637×** | -3.9 | 0.009 | 23/46 (SW 900, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.804×** | -3.6 | 0.026 | 20/45 (SK-MEL-2, HOP62, …) | two highest doses | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **0.667×** | -3.5 | 0.033 | 15/46 (SW 900, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.819×** | -3.3 | 0.060 | 22/46 (SW48, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.823×** | -3.2 | 0.068 | 21/46 (SW 900, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.823×** | -3.2 | 0.068 | 21/46 (A-427, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.760×** | -3.1 | 0.097 | 19/46 (A498, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9051. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 114 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.82× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 0.05 µM 0.402× (z -8.5) |
| [[A498 (line)]] | wt | 109 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Selinexor (drug)]] 5 µM 0.561× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 127 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LS 180 (line)]] | wt | 86.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[PH-797804 (drug)]] 5 µM 0.180× (z -8.7) |
| [[SW1417 (line)]] | alt | 96.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 151 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A549 (line)]] | wt | 85.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[CFPAC-1 (line)]] | alt | 35.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HEC-1-A (line)]] | alt | 190 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HOP62 (line)]] | alt | 94.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[Hs 766T (line)]] | wt | 73.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HS-578T (line)]] | alt | 78.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.81× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HT-29 (line)]] | alt | 99.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[J82 (line)]] | alt | 291 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[KATO III (line)]] | alt | 113 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.83× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1792 (line)]] | alt | 33.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.47× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2030 (line)]] | alt | 31.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[PANC-1 (line)]] | alt | 55.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SNU-423 (line)]] | alt | 84.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.98× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 156 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.599× (z -9.0) |
| [[C32 (line)]] | wt | 31.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HCT15 (line)]] | alt | 194 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.06× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LoVo (line)]] | wt | 73.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 73.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[RKO (line)]] | wt | 150 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[PH-797804 (drug)]] 5 µM 0.152× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 76.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SHP-77 (line)]] | alt | 160 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SNU-1 (line)]] | wt | 214 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.536× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 130 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[AN3 CA (line)]] | alt | 186 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 24.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[C-33 A (line)]] | alt | 136 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HepG2_C3A (line)]] | wt | 38.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 60.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.41× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H23 (line)]] | alt | 38.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H596 (line)]] | alt | 82.7 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.126× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 109 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 110 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.81× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW 1088 (line)]] | alt | 66.3 | 0 | 1 | — | [[Idoxuridine (drug)]] 5 µM 0.0638× (z -8.6) |
| [[SW 900 (line)]] | alt | 97.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW48 (line)]] | wt | 110 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[BT-474 (line)]] | alt | 22.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9051), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DEK]] | +0.76 | +0.72 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 464 |
| [[CENPU]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[EZH2]] | +0.67 | +0.79 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[PBK]] | +0.67 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[H2AZ2]] | +0.66 | +0.55 / +0.66 | both halves | 1e-05 | pathway: Epigenetic regulation by WDR5-containing histone modifying complexes |
| [[NUF2]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CDCA7L]] | +0.64 | +0.54 / +0.63 | both halves | 1e-05 | STRING 900 |
| [[RAD21]] | +0.64 | +0.67 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[SLC25A40]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[TTK]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[HLTF]] | +0.63 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[ANLN]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF778]] | -0.58 | -0.44 / -0.44 | both halves | 3e-05 | pathway: Epigenetic regulation of gene expression |
| [[GPN2]] | -0.57 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[FBXO28]] | -0.57 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[PEX16]] | -0.56 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[YRDC]] | -0.56 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[TSSC4]] | -0.56 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[TMEM199]] | -0.55 | -0.23 / -0.56 | both halves | 5e-04 |  |
| [[COMMD5]] | -0.54 | -0.26 / -0.53 | both halves | 4e-04 |  |
| [[EXOSC4]] | -0.54 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[LRRC41]] | -0.54 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[ZNF593]] | -0.53 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[TIMM22]] | -0.53 | -0.41 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GGH]] | B | GGH activity raises PSIP1's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.37× lower at baseline in the lines without GGH | 0.048 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[PBK]] | C | PBK activity raises PSIP1's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.01× lower at baseline in the lines without PBK | 0.013 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.565). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.3, -53.3); signed map (-46.7, -37.7). **Vector** length 118, 38.3% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Condensation of Prometaphase Chromosomes* (reactome, mean cos +0.52 to 8); *Kinesins* (reactome, mean cos +0.51 to 10); *Initiation of Nuclear Envelope (NE) Reformation* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +3.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.9 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +2.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.4 | +1.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.8 | -3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | -6.9 | +0.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.5 | -5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | +0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.0 | -3.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | -5.6 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -2.5 |
|  | [[EX229 (drug)]] 5 µM |  | -4.7 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | PC4 and SRSF1 interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p22.3 — chr9:15,464,066-15,510,995 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p52, LEDGF, p75, DFS70; previously PSIP2 |
| Gene groups (HGNC) | Heparin binding growth factor family |
| Hallmark sets | E2F_TARGETS |
| Reactome | 15 pathways, smallest: Autointegration results in viral DNA circles; Integration of viral DNA into host genomic DNA; APOBEC3G mediated resistance to HIV-1 infection |
| Matched by | ensembl_id |

**Function**, from UniProt [O75475](https://www.uniprot.org/uniprotkb/O75475) (PC4 and SFRS1-interacting protein):

> Transcriptional coactivator involved in neuroepithelial stem cell differentiation and neurogenesis. Involved in particular in lens epithelial cell gene regulation and stress responses. May play an important role in lens epithelial to fiber cell terminal differentiation. May play a protective role during stress-induced apoptosis. Isoform 2 is a more general and stronger transcriptional coactivator. Isoform 2 may also act as an adapter to coordinate pre-mRNA splicing. Cellular cofactor for …

**Summary**, from NCBI Gene [11168](https://www.ncbi.nlm.nih.gov/gene/11168):

> Enables DNA-binding transcription factor binding activity; chromatin binding activity; and transcription coactivator activity. Involved in mRNA 5'-splice site recognition and positive regulation of transcription by RNA polymerase II. Located in heterochromatin; nuclear periphery; and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9527](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9527) · Entrez [11168](https://www.ncbi.nlm.nih.gov/gene/11168) · UniProt [O75475](https://www.uniprot.org/uniprotkb/O75475) · Ensembl [ENSG00000164985](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164985)

## Data

Gene col 9051: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9051); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9051, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9051]; `tensor/DDL_lfc|DDL_z.npy` [9051]; `embed/gene_vectors.npy` [9051]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9051 or target_col == 9051). Every well: [[PSIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
