---
symbol: "NSUN6"
type: "gene"
col: 14256
ensembl_id: "ENSG00000241058"
name: "NOP2/Sun RNA methyltransferase 6"
location: "10p12.31"
module: 30
arm: "-"
pooled_cpm: 94.64
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# NSUN6

*NOP2/Sun RNA methyltransferase 6* — 10p12.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.03× (z +20.8, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.482× (z -9.7, q 2e-19, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTR3-AS1]] (+0.62, fdr 1e-05), [[ADAMTSL4-AS2]] (+0.59, fdr 1e-05), [[ERRFI1-DT]] (+0.58, fdr 2e-05); moves opposite to [[TRAF6]] (-0.63, fdr 7e-06), [[SNTA1]] (-0.60, fdr 3e-05), [[ASAP3]] (-0.58, fdr 4e-05).
> It sits in the **-** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14256.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.03×** | +20.8 | 0e+00 | 47/49 (NCI-H2347, SNU-423, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.06×** | +17.9 | 0e+00 | 46/50 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.64×** | +16.5 | 0e+00 | 45/48 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +9.7 | 5e-20 | 37/48 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.93×** | +8.7 | 5e-16 | 41/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +7.9 | 3e-13 | 40/48 (A-172, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.62×** | +6.4 | 1e-08 | 34/48 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.60×** | +6.2 | 3e-08 | 32/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +6.1 | 8e-08 | 35/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +5.2 | 1e-05 | 31/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +4.9 | 5e-05 | 31/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.39×** | +4.4 | 6e-04 | 30/48 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.71×** | +3.7 | 0.009 | 25/49 (NCI-H460, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.30×** | +3.5 | 0.018 | 23/49 (AsPC-1, SW 900, …) | inconsistent across doses | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +3.4 | 0.029 | 22/48 (BT-474, NCI-H460, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.091 | 22/48 (LOX-IMVI, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14256.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.482×** | -9.7 | 2e-19 | 44/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.497×** | -9.3 | 5e-18 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.529×** | -8.4 | 6e-15 | 33/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.532×** | -8.4 | 9e-15 | 34/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.563×** | -7.6 | 3e-12 | 35/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.549×** | -7.5 | 6e-12 | 39/48 (NCI-H1573, J82, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.599×** | -6.8 | 9e-10 | 37/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.427×** | -5.9 | 3e-07 | 41/44 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.675×** | -5.0 | 4e-05 | 29/47 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.741×** | -3.8 | 0.009 | 28/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.750×** | -3.7 | 0.013 | 27/47 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.776×** | -3.4 | 0.037 | 24/48 (CHP-212, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Asciminib (drug)]] 0.05 µM |  | **0.768×** | -3.3 | 0.037 | 28/48 (SW 1088, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14256. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 72.4 | 3 | 9 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +15.3) | [[Digitoxin (drug)]] 0.5 µM 0.186× (z -18.3) |
| [[MIA PaCa-2 (line)]] | alt | 102 | 7 (3 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.71× (z +22.8) | [[Ixazomib citrate (drug)]] 5 µM 0.301× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 68.8 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.33× (z +24.8) | — |
| [[SW480 (line)]] | alt | 105 | 3 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +16.4) | [[Digitoxin (drug)]] 0.5 µM 0.310× (z -13.5) |
| [[J82 (line)]] | alt | 76.2 | 4 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +16.8) | [[Ixazomib citrate (drug)]] 5 µM 0.245× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 127 | 3 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +14.8) | [[Digitoxin (drug)]] 5 µM 0.166× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 179 | 2 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.106× (z -22.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.340× (z -11.3) |
| [[SNU-423 (line)]] | alt | 52.7 | 7 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 25.8× (z +25.5) | — |
| [[NCI-H2347 (line)]] | alt | 31.4 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.30× (z +26.0) | — |
| [[SK-MEL-2 (line)]] | alt | 137 | 4 | 2 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 5.09× (z +14.6) | [[Ixazomib citrate (drug)]] 5 µM 0.321× (z -10.6) |
| [[A-172 (line)]] | wt | 87.6 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +20.7) | — |
| [[H4 (line)]] | wt | 64.9 | 3 | 2 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.36× (z +13.0) | [[Digitoxin (drug)]] 0.05 µM 0.185× (z -10.8) |
| [[Hs 766T (line)]] | wt | 78.7 | 4 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.14× (z +17.9) | [[Ixazomib citrate (drug)]] 5 µM 0.316× (z -8.9) |
| [[HT-29 (line)]] | alt | 61.1 | 3 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +13.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.346× (z -9.2) |
| [[KATO III (line)]] | alt | 91.0 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.230× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.287× (z -13.3) |
| [[C32 (line)]] | wt | 42.3 | 4 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +17.2) | — |
| [[HCT15 (line)]] | alt | 118 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +11.4) | [[Ixazomib citrate (drug)]] 5 µM 0.284× (z -11.6) |
| [[HOP62 (line)]] | alt | 64.7 | 4 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 16.0× (z +24.6) | — |
| [[HS-578T (line)]] | alt | 47.5 | 4 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 20.8× (z +21.9) | — |
| [[LOX-IMVI (line)]] | wt | 75.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +15.9) | — |
| [[SW 900 (line)]] | alt | 53.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.08× (z +18.3) | — |
| [[A549 (line)]] | wt | 93.7 | 1 (1 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 3.01× (z +8.8) ⚠ cell-cycle shift, explains ~52% of this change | [[Digitoxin (drug)]] 0.5 µM 0.304× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 47.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +20.6) | — |
| [[BT-474 (line)]] | alt | 48.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +11.8) | — |
| [[C-33 A (line)]] | alt | 118 | 2 | 1 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 4.31× (z +10.7) | [[Digitoxin (drug)]] 0.5 µM 0.266× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 78.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.89× (z +20.5) | — |
| [[HEC-1-A (line)]] | alt | 111 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +12.2) | — |
| [[HepG2_C3A (line)]] | wt | 228 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.333× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 59.0 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 9.11× (z +14.0) | — |
| [[LS 180 (line)]] | wt | 97.4 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +10.4) | [[Digitoxin (drug)]] 0.5 µM 0.349× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 309 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.305× (z -10.1) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.170× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 50.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.82× (z +18.7) | — |
| [[RKO (line)]] | wt | 152 | 3 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 6.79× (z +16.3) | — |
| [[RPMI-7951 (line)]] | alt | 147 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 9.09× (z +17.6) | — |
| [[LoVo (line)]] | wt | 103 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +16.5) | — |
| [[NCI-H1792 (line)]] | alt | 89.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.98× (z +18.0) | [[Digitoxin (drug)]] 5 µM 0.306× (z -9.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 177 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.317× (z -9.4) |
| [[A-427 (line)]] | wt | 140 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.347× (z -10.2) |
| [[A498 (line)]] | wt | 67.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +10.3) | — |
| [[NCI-H596 (line)]] | alt | 94.4 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.151× (z -10.5) |
| [[SNU-1 (line)]] | wt | 68.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +11.5) | — |
| [[SW48 (line)]] | wt | 108 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.218× (z -8.5) |
| [[AN3 CA (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 93.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14256), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTR3-AS1]] | +0.62 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[ADAMTSL4-AS2]] | +0.59 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[ERRFI1-DT]] | +0.58 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[POLG2]] | +0.58 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[INTS6]] | +0.58 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[IRF3]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[RAPGEF6]] | +0.58 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[HELQ]] | +0.58 | +0.71 / +0.41 | both halves | 4e-05 |  |
| [[MZF1-AS1]] | +0.58 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[PPIEL-1]] | +0.57 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[LETM2]] | +0.57 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[R3HDM2]] | +0.57 | +0.69 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAF6]] | -0.63 | -0.66 / -0.63 | both halves | 7e-06 |  |
| [[SNTA1]] | -0.60 | -0.70 / -0.44 | both halves | 3e-05 |  |
| [[ASAP3]] | -0.58 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[USP35]] | -0.57 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[AP2A2]] | -0.56 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[PLD2]] | -0.56 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[SNN]] | -0.56 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[ANKRD52]] | -0.55 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[KRAS]] | -0.53 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[GLB1]] | -0.53 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[SERAC1]] | -0.53 | -0.64 / -0.38 | both halves | 7e-05 |  |
| [[UNC45A]] | -0.53 | -0.61 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NSUN6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises NSUN6's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **-** arm (projection on the module's main direction -0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (35.3, -6.9); signed map (16.0, 19.7). **Vector** length 116, 38.1% of its response variance represented; |z| ≥ 3 in 1,299 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +17.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +16.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.9 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +9.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +0.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +0.2 |
|  | [[γ-Oryzanol (drug)]] 0.05 µM |  | +2.0 | +1.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -9.6 | -9.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -8.4 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.9 | -6.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -2.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -5.7 | -5.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.2 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.0 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | NOP2/Sun RNA methyltransferase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.31 — chr10:18,545,561-18,659,285 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23743; previously NOPD1, ARL5B-AS1 |
| Gene groups (HGNC) | NOP2/Sun RNA methyltransferase family; DNA/RNA methyltransferases |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEA1](https://www.uniprot.org/uniprotkb/Q8TEA1) (tRNA):

> S-adenosyl-L-methionine-dependent methyltransferase that specifically methylates the C5 position of cytosine 72 in tRNA(Thr)(TGT) and tRNA(Cys)(GCA). In vitro also methylates tRNA(Thr)(AGT). Methylation requires, in the acceptor stem region, the presence of the 3'-CCA terminus, the target site C72, the discriminator base U73, and the second and third base pairs (2:71 and 3:70) in the tRNA substrates.

**Summary**, from NCBI Gene [221078](https://www.ncbi.nlm.nih.gov/gene/221078):

> Enables tRNA (cytidine-N5)-methyltransferase activity and tRNA binding activity. Involved in tRNA C5-cytosine methylation. Located in cytoplasm. Implicated in autosomal recessive intellectual developmental disorder 82. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23529](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23529) · Entrez [221078](https://www.ncbi.nlm.nih.gov/gene/221078) · UniProt [Q8TEA1](https://www.uniprot.org/uniprotkb/Q8TEA1) · Ensembl [ENSG00000241058](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241058)

## Data

Gene col 14256: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14256); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14256, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14256]; `tensor/DDL_lfc|DDL_z.npy` [14256]; `embed/gene_vectors.npy` [14256]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14256 or target_col == 14256). Every well: [[NSUN6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSUN6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
