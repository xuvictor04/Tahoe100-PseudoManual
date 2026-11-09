---
symbol: "NCOA6"
type: "gene"
col: 12634
ensembl_id: "ENSG00000198646"
name: "nuclear receptor coactivator 6"
location: "20q11.22"
module: 172
arm: "+"
pooled_cpm: 161.02
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 19
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# NCOA6

*nuclear receptor coactivator 6* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 1.43× (z +5.2, q 1e-04, up in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 2.01×, SW480 1.37×; ⚠ cell-cycle shift, explains ~61% of this change); [[TAK-901 (drug)]] 0.05 µM in 1 line (BT-474 1.70×).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.358× (z -28.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCBP3]] (+0.60, fdr 2e-05), [[PPP6R2]] (+0.58, fdr 2e-05), [[TLK1]] (+0.58, fdr 1e-05); moves opposite to [[ARL5B]] (-0.61, fdr 1e-05), [[SHB]] (-0.53, fdr 6e-05), [[EGR3]] (-0.52, fdr 3e-05).
> It is in [[Module 172]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12634.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 2.01×, SW480 1.37×; ⚠ cell-cycle shift, explains ~61% of this change); [[TAK-901 (drug)]] 0.05 µM in 1 line (BT-474 1.70×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +5.2 | 1e-04 | 25/48 (NCI-H1573, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +4.8 | 3e-04 | 21/47 (CFPAC-1, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.8 | 3e-04 | 20/48 (COLO 205, SHP-77, …) | rises with dose | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.19× | +4.6 | 5e-04 | 20/47 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +4.5 | 1e-03 | 6/48 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 1.14× | +3.5 | 0.045 | 9/48 (J82, KATO III, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.14× | +3.3 | 0.086 | 8/50 (RKO, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.2 | 0.094 | 14/48 (RPMI-7951, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | 1.12× | +3.1 | 0.14 | 12/48 (KATO III, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12634.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.358×** | -28.7 | 0e+00 | 47/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.362×** | -28.3 | 0e+00 | 48/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.444×** | -22.7 | 0e+00 | 47/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.508×** | -18.2 | 0e+00 | 39/44 (A549, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.644×** | -17.3 | 0e+00 | 43/49 (BT-474, A-172, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.592×** | -14.6 | 0e+00 | 40/49 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.581×** | -14.0 | 1e-42 | 37/45 (A549, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.644×** | -12.3 | 9e-33 | 43/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.651×** | -11.5 | 8e-29 | 37/50 (LOX-IMVI, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.773×** | -10.1 | 2e-22 | 39/48 (NCI-H2347, LOX-IMVI, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.744×** | -7.9 | 1e-13 | 34/48 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.767×** | -7.1 | 6e-11 | 26/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 0.837× | -7.0 | 1e-10 | 23/48 (NCI-H1792, A-172, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -6.9 | 3e-10 | 22/48 (J82, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.807×** | -6.0 | 8e-08 | 29/48 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.807×** | -6.0 | 9e-08 | 26/49 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.821×** | -5.5 | 1e-06 | 25/48 (BT-474, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.869× | -5.5 | 1e-06 | 14/48 (A-172, BT-474, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.686×** | -5.5 | 1e-06 | 34/49 (NCI-H460, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.726×** | -4.7 | 8e-05 | 33/48 (PANC-1, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.824×** | -3.8 | 0.003 | 23/48 (NCI-H23, AsPC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.889× | -3.0 | 0.052 | 13/47 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12634. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 165 | 0 | 14 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -21.7) |
| [[A-172 (line)]] | wt | 139 | 0 | 13 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -23.9) |
| [[BT-474 (line)]] | alt | 769 | 1 | 12 (7 ⚠) | [[TAK-901 (drug)]] 0.05 µM 1.70× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -26.2) |
| [[NCI-H1573 (line)]] | alt | 153 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -19.5) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.277× (z -19.3) |
| [[NCI-H2347 (line)]] | alt | 128 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -17.1) |
| [[HS-578T (line)]] | alt | 129 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -18.5) |
| [[C32 (line)]] | wt | 108 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -20.2) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.355× (z -13.0) |
| [[HOP62 (line)]] | alt | 124 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.324× (z -17.3) |
| [[NCI-H1792 (line)]] | alt | 217 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -23.6) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.237× (z -22.0) |
| [[NCI-H2030 (line)]] | alt | 168 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 196 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -24.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.299× (z -19.0) |
| [[RKO (line)]] | wt | 153 | 1 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.5) ⚠ cell-cycle shift, explains ~61% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -12.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.420× (z -11.9) |
| [[SNU-423 (line)]] | alt | 165 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -15.4) |
| [[A549 (line)]] | wt | 123 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -23.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.340× (z -17.0) |
| [[AsPC-1 (line)]] | alt | 175 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -19.6) |
| [[HT-29 (line)]] | alt | 189 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -15.9) |
| [[J82 (line)]] | alt | 274 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.354× (z -18.3) |
| [[MIA PaCa-2 (line)]] | alt | 153 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -24.2) |
| [[NCI-H460 (line)]] | wt | 149 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -21.0) |
| [[SW480 (line)]] | alt | 155 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.314× (z -23.7) |
| [[A498 (line)]] | wt | 100 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.436× (z -14.5) |
| [[Hs 766T (line)]] | wt | 215 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -17.8) |
| [[KATO III (line)]] | alt | 192 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.397× (z -15.1) |
| [[LS 180 (line)]] | wt | 127 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -17.9) |
| [[Panc 03.27 (line)]] | alt | 194 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.358× (z -17.3) |
| [[PANC-1 (line)]] | alt | 106 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.366× (z -18.7) |
| [[SW1417 (line)]] | alt | 308 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.351× (z -19.4) |
| [[A-427 (line)]] | wt | 160 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.296× (z -18.6) |
| [[CFPAC-1 (line)]] | alt | 112 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.452× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 137 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.390× (z -16.6) |
| [[HepG2_C3A (line)]] | wt | 168 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.352× (z -13.1) |
| [[hTERT-HPNE (line)]] | wt | 92.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -12.9) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -9.8) |
| [[C-33 A (line)]] | alt | 155 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -15.3) |
| [[LoVo (line)]] | wt | 103 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -17.5) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.393× (z -15.4) |
| [[RPMI-7951 (line)]] | alt | 155 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.471× (z -9.3) |
| [[SHP-77 (line)]] | alt | 93.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.405× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 156 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.351× (z -13.9) |
| [[SW48 (line)]] | wt | 129 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.253× (z -13.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.340× (z -10.5) |
| [[COLO 205 (line)]] | alt | 150 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.332× (z -12.7) |
| [[SNU-1 (line)]] | wt | 187 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.351× (z -13.5) |
| [[SW 1271 (line)]] | alt | 326 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -9.0) |
| [[SW 900 (line)]] | alt | 106 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.384× (z -12.4) |
| [[HCT15 (line)]] | alt | 135 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.402× (z -10.2) |
| [[CHP-212 (line)]] | wt | 96.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW 1088 (line)]] | alt | 125 | 0 | 1 | — | [[Saquinavir (drug)]] 5 µM 0.255× (z -8.7) |
| [[AN3 CA (line)]] | alt | 150 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 88.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 183 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12634), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCBP3]] | +0.60 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[PPP6R2]] | +0.58 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[TLK1]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[BICRA]] | +0.58 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ELMOD3]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[SETD2]] | +0.57 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[KIAA0232]] | +0.55 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[RUFY1]] | +0.55 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[SLC38A7]] | +0.54 | +0.26 / +0.59 | both halves | 4e-04 |  |
| [[PGLS]] | +0.53 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[RILPL1]] | +0.53 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[EHMT1]] | +0.52 | +0.42 / +0.60 | both halves | 4e-05 | pathway: Epigenetic regulation of gene expression |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL5B]] | -0.61 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[SHB]] | -0.53 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[EGR3]] | -0.52 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[COTL1]] | -0.52 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[IVNS1ABP]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[GLS]] | -0.51 | -0.37 / -0.55 | both halves | 7e-05 |  |
| [[ITGA1]] | -0.51 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ZNF697]] | -0.50 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[EXTL2]] | -0.50 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[EPB41L2]] | -0.49 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[LIF]] | -0.49 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[MAP2K3]] | -0.49 | -0.44 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.672). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-47.5, 12.8); signed map (-2.5, -10.4). **Vector** length 87.4, 25.7% of its response variance represented; |z| ≥ 3 in 1,289 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +0.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | +3.9 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.8 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | +3.6 | -5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.1 | +0.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.0 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.5 | -10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.5 | -6.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -6.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.0 | -11.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.8 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -0.7 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.8 | -0.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | +1.5 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | -1.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor coactivator 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:34,689,097-34,825,651 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0181, RAP250, ASC2, AIB3, PRIP, TRBP, NRC |
| Hallmark sets | APICAL_SURFACE |
| Reactome | 32 pathways, smallest: BMAL1:CLOCK,NPAS2 activates circadian expression; RORA,B,C and NR1D1 (REV-ERBA) regulate gene expression; Expression of BMAL (ARNTL), CLOCK, and NPAS2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14686](https://www.uniprot.org/uniprotkb/Q14686) (Nuclear receptor coactivator 6):

> Nuclear receptor coactivator that directly binds nuclear receptors and stimulates the transcriptional activities in a hormone-dependent fashion. Coactivates expression in an agonist- and AF2-dependent manner. Involved in the coactivation of different nuclear receptors, such as for steroids (GR and ERs), retinoids (RARs and RXRs), thyroid hormone (TRs), vitamin D3 (VDR) and prostanoids (PPARs). Probably functions as a general coactivator, rather than just a nuclear receptor coactivator. May also …

**Summary**, from NCBI Gene [23054](https://www.ncbi.nlm.nih.gov/gene/23054):

> The protein encoded by this gene is a transcriptional coactivator that can interact with nuclear hormone receptors to enhance their transcriptional activator functions. This protein has been shown to be involved in the hormone-dependent coactivation of several receptors, including prostanoid, retinoid, vitamin D3, thyroid hormone, and steroid receptors. Alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:15936](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15936) · Entrez [23054](https://www.ncbi.nlm.nih.gov/gene/23054) · UniProt [Q14686](https://www.uniprot.org/uniprotkb/Q14686) · Ensembl [ENSG00000198646](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198646)

## Data

Gene col 12634: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12634); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12634, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12634]; `tensor/DDL_lfc|DDL_z.npy` [12634]; `embed/gene_vectors.npy` [12634]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12634 or target_col == 12634). Every well: [[NCOA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCOA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
