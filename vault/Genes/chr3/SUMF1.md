---
symbol: "SUMF1"
type: "gene"
col: 6882
ensembl_id: "ENSG00000144455"
name: "sulfatase modifying factor 1"
location: "3p26.1"
module: 10
arm: "+"
pooled_cpm: 133.5
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 42
n_dd_up_clean: 10
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# SUMF1

*sulfatase modifying factor 1* — 3p26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.47× (z +4.3, q 0.012, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (23 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.272× (z -14.9, q 0e+00, down in 45 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.416× (z -10.0, q 1e-21, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOC4]] (+0.72, fdr 7e-06), [[ZRANB2-DT]] (+0.69, fdr 7e-06), [[VPS13B]] (+0.66, fdr 1e-05); moves opposite to [[ZNF684]] (-0.57, fdr 1e-04), [[EXTL3]] (-0.53, fdr 4e-05), [[SBK1]] (-0.51, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EFCAB6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6882.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +4.3 | 0.012 | 35/47 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Omeprazole (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.067 | 36/48 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.41×** | +3.5 | 0.069 | 34/48 (J82, LOX-IMVI, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.79×** | +3.5 | 0.069 | 32/50 (NCI-H596, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.087 | 29/47 (SW480, LoVo, …) | rises with dose |  |
| [[Afatinib (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.087 | 31/49 (HEC-1-A, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.087 | 28/48 (NCI-H1792, HEC-1-A, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.087 | 21/48 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.32×** | +3.2 | 0.087 | 25/49 (RPMI-7951, HEC-1-A, …) | inconsistent across doses |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.32×** | +3.2 | 0.087 | 27/48 (RPMI-7951, SNU-1, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +3.1 | 0.094 | 29/48 (NCI-H2030, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 23 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6882.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.272×** | -14.9 | 0e+00 | 45/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.427×** | -13.7 | 2e-40 | 45/48 (HEC-1-A, HOP62, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.302×** | -13.7 | 2e-40 | 46/48 (LoVo, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.328×** | -12.2 | 3e-32 | 47/48 (HEC-1-A, A-172, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.395×** | -10.6 | 4e-24 | 46/48 (COLO 205, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.399×** | -10.5 | 8e-24 | 44/48 (LoVo, BT-474, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.416×** | -10.0 | 1e-21 | 46/48 (HCT15, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.411×** | -9.8 | 1e-20 | 41/47 (RKO, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.451×** | -8.7 | 2e-16 | 40/47 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.643×** | -7.1 | 6e-11 | 44/48 (HEC-1-A, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.308×** | -7.0 | 1e-10 | 43/49 (NCI-H1573, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.554×** | -6.7 | 8e-10 | 39/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.567×** | -6.5 | 4e-09 | 39/48 (HCT15, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.531×** | -6.4 | 7e-09 | 35/48 (BT-474, H4, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.575×** | -6.3 | 1e-08 | 38/48 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.592×** | -5.8 | 2e-07 | 40/48 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.379×** | -5.8 | 2e-07 | 33/48 (NCI-H1573, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.684×** | -4.3 | 4e-04 | 34/49 (CHP-212, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.674×** | -4.3 | 5e-04 | 33/48 (J82, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.705×** | -3.8 | 0.003 | 32/48 (MIA PaCa-2, C-33 A, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.804×** | -3.5 | 0.008 | 26/49 (HEC-1-A, C32, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.809×** | -3.4 | 0.012 | 23/49 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.734×** | -3.4 | 0.012 | 28/48 (KATO III, BT-474, …) | top dose only | plate-row cell shift |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **0.815×** | -3.3 | 0.017 | 28/49 (HEC-1-A, LoVo, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.747×** | -3.3 | 0.018 | 28/48 (SW1417, HepG2/C3A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.49 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6882. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 148 | 0 | 13 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.163× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -15.1) |
| [[H4 (line)]] | wt | 180 | 0 | 12 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -13.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.224× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 448 | 0 | 12 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.184× (z -17.5) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.147× (z -10.8) |
| [[J82 (line)]] | alt | 109 | 0 | 10 (7 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.208× (z -13.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.237× (z -12.1) |
| [[PANC-1 (line)]] | alt | 67.0 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -15.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.299× (z -11.7) |
| [[A-427 (line)]] | wt | 164 | 0 | 9 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.335× (z -12.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.225× (z -8.6) |
| [[BT-474 (line)]] | alt | 178 | 0 | 9 (8 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.217× (z -15.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.375× (z -10.2) |
| [[C32 (line)]] | wt | 149 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -16.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -13.0) |
| [[HCT15 (line)]] | alt | 274 | 0 | 9 (7 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.131× (z -14.9) |
| [[HEC-1-A (line)]] | alt | 321 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -24.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.147× (z -19.2) |
| [[LoVo (line)]] | wt | 176 | 0 | 9 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.264× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 151 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 270 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.181× (z -8.9) |
| [[A549 (line)]] | wt | 138 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -18.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.255× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 96.3 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -18.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.285× (z -10.0) |
| [[COLO 205 (line)]] | alt | 99.6 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.153× (z -14.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -11.7) |
| [[SW480 (line)]] | alt | 98.5 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -14.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.202× (z -13.0) |
| [[HOP62 (line)]] | alt | 152 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -21.5) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -13.8) |
| [[HS-578T (line)]] | alt | 115 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -11.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.241× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 250 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -16.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H460 (line)]] | wt | 109 | 0 | 6 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.267× (z -10.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.356× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 229 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -15.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SNU-423 (line)]] | alt | 152 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -15.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.237× (z -12.5) |
| [[A-172 (line)]] | wt | 152 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -20.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -14.2) |
| [[hTERT-HPNE (line)]] | wt | 139 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -17.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[KATO III (line)]] | alt | 120 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.203× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.334× (z -9.4) |
| [[LS 180 (line)]] | wt | 66.6 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.145× (z -13.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[Panc 03.27 (line)]] | alt | 124 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -15.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[CHP-212 (line)]] | wt | 156 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.126× (z -12.3) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 86.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -9.0) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SW1417 (line)]] | alt | 120 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -9.2) ⚠ cell-cycle shift, explains ~47% of this change |
| [[AN3 CA (line)]] | alt | 79.6 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0969× (z -11.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HT-29 (line)]] | alt | 92.7 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.298× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 89.6 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -10.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[RKO (line)]] | wt | 105 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0745× (z -18.9) ⚠ toxic |
| [[SW 900 (line)]] | alt | 148 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.275× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 51.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -10.0) ⚠ cell-cycle shift, explains ~47% of this change |
| [[C-33 A (line)]] | alt | 68.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[Hs 766T (line)]] | wt | 54.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.232× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[AsPC-1 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 87.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6882), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC4]] | +0.72 | +0.61 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ZRANB2-DT]] | +0.69 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[VPS13B]] | +0.66 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[IMMP2L]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SEMA6A-AS1]] | +0.63 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[FHIT]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[LRGUK]] | +0.59 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[FARS2]] | +0.59 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[CASC2]] | +0.57 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[CCDC191]] | +0.57 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[FAM174A-DT]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[TMEM232]] | +0.57 | +0.51 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF684]] | -0.57 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[EXTL3]] | -0.53 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[SBK1]] | -0.51 | -0.29 / -0.58 | both halves | 2e-04 |  |
| [[ADGRB2]] | -0.51 | -0.35 / -0.62 | both halves | 1e-04 |  |
| [[SMCO4]] | -0.50 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[ARHGEF26]] | -0.49 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[IL22RA1]] | -0.49 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[SLC35A1]] | -0.49 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[ESYT3]] | -0.48 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[NOL4L]] | -0.48 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[EML2]] | -0.48 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[KIAA0513]] | -0.48 | -0.36 / -0.51 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFCAB6]] | B | EFCAB6 activity raises SUMF1's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.80× lower at baseline in the lines without EFCAB6 | 0.039 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.450). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-26.2, 29.8); signed map (10.3, -12.6). **Vector** length 84.5, 35.0% of its response variance represented; |z| ≥ 3 in 1,497 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belumosudil (drug)]] 5 µM |  | +5.3 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | -2.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.0 | -7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +2.9 | -13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +2.8 | -3.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.5 | +3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +0.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.3 | -7.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.3 | -4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.9 | -5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.6 | -9.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.8 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.2 | -2.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -3.0 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | sulfatase modifying factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p26.1 — chr3:3,700,814-4,467,273 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FGE, UNQ3037 |
| Gene groups (HGNC) | Oxidoreductases |
| Reactome | 6 pathways, smallest: The activation of arylsulfatases; Glycosphingolipid catabolism; Glycosphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBK3](https://www.uniprot.org/uniprotkb/Q8NBK3) (Formylglycine-generating enzyme):

> Oxidase that catalyzes the conversion of cysteine to 3-oxoalanine on target proteins, using molecular oxygen and an unidentified reducing agent. 3-oxoalanine modification, which is also named formylglycine (fGly), occurs in the maturation of arylsulfatases and some alkaline phosphatases that use the hydrated form of 3-oxoalanine as a catalytic nucleophile. Known substrates include GALNS, ARSA, STS and ARSE.

**Summary**, from NCBI Gene [285362](https://www.ncbi.nlm.nih.gov/gene/285362):

> This gene encodes an enzyme that catalyzes the hydrolysis of sulfate esters by oxidizing a cysteine residue in the substrate sulfatase to an active site 3-oxoalanine residue, which is also known as C-alpha-formylglycine. Mutations in this gene cause multiple sulfatase deficiency, a lysosomal storage disorder. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:20376](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20376) · Entrez [285362](https://www.ncbi.nlm.nih.gov/gene/285362) · UniProt [Q8NBK3](https://www.uniprot.org/uniprotkb/Q8NBK3) · Ensembl [ENSG00000144455](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144455)

## Data

Gene col 6882: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6882); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6882, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6882]; `tensor/DDL_lfc|DDL_z.npy` [6882]; `embed/gene_vectors.npy` [6882]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6882 or target_col == 6882). Every well: [[SUMF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUMF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
