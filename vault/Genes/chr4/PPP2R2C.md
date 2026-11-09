---
symbol: "PPP2R2C"
type: "gene"
col: 1072
ensembl_id: "ENSG00000074211"
name: "protein phosphatase 2 regulatory subunit Bgamma"
location: "4p16.1"
module: 195
arm: "+"
pooled_cpm: 48.15
n_lines_expressing: 32
n_dd_up: 13
n_dd_down: 33
n_dd_up_clean: 8
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/195"]
generated_by: "tahoemap"
---

# PPP2R2C

*protein phosphatase 2 regulatory subunit Bgamma* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.03× (z +9.7, q 2e-19, up in 23 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.431× (z -16.2, q 0e+00, down in 25 of 30 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.377× (z -13.3, q 8e-38, down in 25 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAQR5]] (+0.67, fdr 7e-06), [[MBOAT2]] (+0.63, fdr 1e-05), [[IGSF9B]] (+0.61, fdr 1e-05); moves opposite to [[CTSO]] (-0.59, fdr 3e-05), [[NAALADL2]] (-0.53, fdr 6e-05), [[REL]] (-0.53, fdr 1e-04).
> It is in [[Module 195]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[HMOX2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1072.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.03×** | +9.7 | 2e-19 | 23/29 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.01×** | +9.6 | 2e-19 | 23/29 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.76×** | +7.3 | 5e-11 | 20/30 (BT-474, MIA PaCa-2, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.0 | 8e-05 | 13/30 (SW480, J82, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.43×** | +4.9 | 1e-04 | 19/29 (HOP62, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.40×** | +4.5 | 8e-04 | 17/29 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.37×** | +4.3 | 0.001 | 15/29 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.33×** | +4.0 | 0.005 | 16/31 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +3.4 | 0.039 | 11/30 (H4, NCI-H2030, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.28×** | +3.4 | 0.042 | 13/30 (J82, NCI-H2347, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.054 | 11/30 (HOP62, H4, …) | top dose only |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.55×** | +3.1 | 0.072 | 9/30 (SW 900, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.072 | 9/30 (NCI-H2347, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.55×** | +3.1 | 0.072 | 11/30 (AsPC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1072.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.431×** | -16.2 | 0e+00 | 25/30 (AsPC-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.377×** | -13.3 | 8e-38 | 25/30 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.538×** | -11.9 | 1e-30 | 25/31 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.461×** | -10.2 | 5e-22 | 23/29 (LOX-IMVI, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.491×** | -9.7 | 4e-20 | 25/30 (A-427, NCI-H23, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.505×** | -8.6 | 7e-16 | 22/28 (A-172, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.531×** | -8.3 | 1e-14 | 23/28 (AsPC-1, NCI-H1573, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.583×** | -7.3 | 1e-11 | 20/29 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.596×** | -7.0 | 1e-10 | 20/30 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.595×** | -6.8 | 6e-10 | 17/29 (A-172, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.609×** | -6.8 | 7e-10 | 18/30 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.612×** | -6.4 | 7e-09 | 21/31 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.625×** | -6.4 | 7e-09 | 18/29 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.722×** | -6.3 | 2e-08 | 20/30 (A-172, BT-474, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -6.0 | 8e-08 | 21/29 (A-172, AsPC-1, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.697×** | -4.9 | 3e-05 | 17/30 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.727×** | -4.2 | 9e-04 | 13/30 (HOP62, C-33 A, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.750×** | -3.9 | 0.002 | 13/30 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.819×** | -3.7 | 0.005 | 14/31 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.764×** | -3.7 | 0.006 | 11/30 (AsPC-1, CFPAC-1, …) | rises with dose | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.618×** | -3.4 | 0.013 | 12/29 (Hs 766T, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.779×** | -3.4 | 0.015 | 14/29 (CFPAC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Arbutin (drug)]] 5 µM |  | **0.802×** | -2.9 | 0.075 | 9/29 (H4, NCI-H2030, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.803×** | -2.9 | 0.076 | 12/29 (AsPC-1, HEC-1-A, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.805×** | -2.8 | 0.082 | 11/29 (AsPC-1, CFPAC-1, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1072. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 50.3 | 13 | 10 (7 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 5.97× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -15.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -14.7) |
| [[AsPC-1 (line)]] | alt | 59.4 | 0 | 22 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0762× (z -23.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -16.5) |
| [[LOX-IMVI (line)]] | wt | 88.6 | 0 | 21 (17 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0586× (z -18.4) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -13.9) |
| [[A-172 (line)]] | wt | 109 | 0 | 15 (12 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -12.5) |
| [[A549 (line)]] | wt | 141 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -13.1) ⚠ cell-cycle shift, explains ~50% of this change |
| [[H4 (line)]] | wt | 18.1 | 5 | 1 (1 ⚠) | [[Clobetasol propionate (drug)]] 5 µM 11.5× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -9.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H1573 (line)]] | alt | 183 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -21.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -14.3) |
| [[CFPAC-1 (line)]] | alt | 60.7 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -16.5) |
| [[LoVo (line)]] | wt | 20.9 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -17.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.245× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 79.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 88.3 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -15.5) |
| [[NCI-H460 (line)]] | wt | 72.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -19.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -9.9) |
| [[BT-474 (line)]] | alt | 80.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.96× (z +8.7) ⚠ cell-cycle shift, explains ~37% of this change | [[Dinaciclib (drug)]] 5 µM 0.288× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.450× (z -9.4) |
| [[C-33 A (line)]] | alt | 56.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 86.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0901× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[SW 900 (line)]] | alt | 27.8 | 1 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.75× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -9.4) |
| [[A-427 (line)]] | wt | 85.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0584× (z -26.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.299× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 30.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -16.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -14.6) |
| [[NCI-H1792 (line)]] | alt | 74.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0846× (z -23.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -13.5) |
| [[PANC-1 (line)]] | alt | 81.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -16.8) |
| [[SW 1271 (line)]] | alt | 104 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -11.1) |
| [[J82 (line)]] | alt | 13.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.35× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 20.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -9.3) |
| [[SNU-423 (line)]] | alt | 29.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -10.2) |
| [[SW480 (line)]] | alt | 31.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.01× (z +8.8) | — |
| [[A498 (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.90 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.43 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.85 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.37 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.01 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.82 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.29 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.00 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.33 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.35 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.31 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.58 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1072), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAQR5]] | +0.67 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[MBOAT2]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[IGSF9B]] | +0.61 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[PBX4]] | +0.61 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[FMNL2]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[SLC8B1]] | +0.58 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ACOT7]] | +0.58 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[ITGB1BP1]] | +0.57 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[TOX2]] | +0.56 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[DOCK9]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[FLNB]] | +0.56 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[SGTB]] | +0.55 | +0.56 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSO]] | -0.59 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[NAALADL2]] | -0.53 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[REL]] | -0.53 | -0.56 / -0.36 | both halves | 1e-04 |  |
| [[MEF2C]] | -0.53 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[TAPBPL]] | -0.52 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[HNMT]] | -0.52 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[ANXA2R-AS1]] | -0.51 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[TNFSF10]] | -0.51 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[SLC4A4]] | -0.51 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[BCLAF1]] | -0.51 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[AOPEP]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[HNF4G]] | -0.50 | -0.44 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises PPP2R2C's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 7.0% of all compounds | 0.030 | ⚠ off-target possible; 4 compounds |
| [[TOP2A]] | B | TOP2A activity raises PPP2R2C's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDYL2]] | B | CDYL2 activity raises PPP2R2C's level | lines that do not express CDYL2 (19) vs lines expressing it (31) | 1.72× lower at baseline in the lines without CDYL2 | 0.072 | ⚠ within organs, on part of the lines; also absent: B3GALT5, BCL11B, ENSG00000225330 |
| [[NR2E3]] | B | NR2E3 activity raises PPP2R2C's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 2.09× lower at baseline in the lines without NR2E3 | 0.081 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMOX2]] | B | PPP2R2C activity raises HMOX2's level | lines that do not express PPP2R2C (18) vs lines expressing it (32) | 1.12× lower at baseline in the lines without PPP2R2C | 0.092 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, CACNG6, JAKMIP1 |

## Where it sits

- **Module**: [[Module 195]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.9, 3.5); signed map (-13.4, 43.2). **Vector** length 111, 32.2% of its response variance represented; |z| ≥ 3 in 1,114 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.1 | +9.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.9 | +9.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | +5.8 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.5 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.1 | +4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -13.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.6 | -4.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -3.4 | -3.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -3.2 | -3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.2 | -16.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -2.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.8 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 2 regulatory subunit Bgamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:6,320,578-6,563,600 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PR52, IMYPNO, MGC33570, PR55G, B55gamma |
| Gene groups (HGNC) | WD repeat domain containing; Protein phosphatase 2 regulatory subunits |
| Hallmark sets | APICAL_JUNCTION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2T4](https://www.uniprot.org/uniprotkb/Q9Y2T4) (Serine/threonine-protein phosphatase 2A 55 kDa regulatory subunit B gamma isoform):

> The B regulatory subunit might modulate substrate selectivity and catalytic activity, and might also direct the localization of the catalytic enzyme to a particular subcellular compartment.

**Summary**, from NCBI Gene [5522](https://www.ncbi.nlm.nih.gov/gene/5522):

> The product of this gene belongs to the phosphatase 2 regulatory subunit B family. Protein phosphatase 2 is one of the four major Ser/Thr phosphatases, and it is implicated in the negative control of cell growth and division. It consists of a common heteromeric core enzyme, which is composed of a catalytic subunit and a constant regulatory subunit, that associates with a variety of regulatory subunits. The B regulatory subunit might modulate substrate selectivity and catalytic activity. This …

**Accessions** — [HGNC:9306](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9306) · Entrez [5522](https://www.ncbi.nlm.nih.gov/gene/5522) · UniProt [Q9Y2T4](https://www.uniprot.org/uniprotkb/Q9Y2T4) · Ensembl [ENSG00000074211](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074211)

## Data

Gene col 1072: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1072); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1072, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1072]; `tensor/DDL_lfc|DDL_z.npy` [1072]; `embed/gene_vectors.npy` [1072]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1072 or target_col == 1072). Every well: [[PPP2R2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP2R2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
