---
symbol: "NMD3"
type: "gene"
col: 9786
ensembl_id: "ENSG00000169251"
name: "NMD3 ribosome export adaptor"
location: "3q26.1"
module: 41
arm: "+"
pooled_cpm: 102.81
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# NMD3

*NMD3 ribosome export adaptor* — 3q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.50× (z +11.0, q 2e-25, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.778× (z -6.6, q 3e-08, down in 26 of 44 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SNU-1 0.201×, Panc 03.27 0.333×, HEC-1-A 0.369×, AsPC-1 0.403×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-1 0.461×, BT-474 0.610×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.204×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.541×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIOK2]] (+0.60, fdr 2e-05), [[ASNSD1]] (+0.52, fdr 5e-05), [[RAB33B]] (+0.52, fdr 1e-04); moves opposite to [[SYMPK]] (-0.49, fdr 4e-04), [[C2CD3]] (-0.47, fdr 1e-04), [[NFATC2IP]] (-0.47, fdr 7e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9786.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +11.0 | 2e-25 | 36/48 (HT-29, PANC-1, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.30×** | +10.0 | 5e-21 | 30/48 (LoVo, HT-29, …) | two highest doses | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +9.6 | 1e-19 | 34/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.77×** | +8.1 | 8e-14 | 37/49 (SW480, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +7.9 | 2e-13 | 32/47 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +7.2 | 8e-11 | 0/50 | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.61×** | +6.7 | 1e-09 | 33/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.9 | 5e-05 | 24/45 (NCI-H1573, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.20× | +4.9 | 8e-05 | 22/48 (A-427, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.16× | +4.0 | 0.003 | 17/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.9 | 0.005 | 9/48 (A-427, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.15× | +3.8 | 0.006 | 14/48 (SK-MEL-2, NCI-H460, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.29×** | +3.7 | 0.011 | 15/47 (H4, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.6 | 0.011 | 14/48 (A-427, RKO, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.019 | 15/48 (HEC-1-A, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.08× | +3.1 | 0.065 | 7/49 (CFPAC-1, KATO III, …) | two highest doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.099 | 9/47 (LOX-IMVI, SW48, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9786.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SNU-1 0.201×, Panc 03.27 0.333×, HEC-1-A 0.369×, AsPC-1 0.403×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-1 0.461×, BT-474 0.610×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.204×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.541×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.778×** | -6.6 | 3e-08 | 26/44 (SNU-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.841× | -4.7 | 8e-04 | 16/48 (A498, SNU-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.856× | -4.2 | 0.005 | 21/48 (A498, BT-474, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.864× | -3.8 | 0.018 | 18/47 (AsPC-1, SW 900, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change | 0.888× | -3.2 | 0.14 | 20/49 (SNU-1, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.890× | -3.2 | 0.14 | 7/47 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.892× | -3.1 | 0.14 | 8/48 (LoVo, hTERT-HPNE, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.893× | -3.1 | 0.14 | 12/48 (SNU-1, BT-474, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.893× | -3.1 | 0.14 | 7/48 (AN3 CA, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9786. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 46.9 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +14.4) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.27× (z +12.3) | — |
| [[A-427 (line)]] | wt | 109 | 5 (3 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.95× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 106 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.02× (z +12.1) | — |
| [[SNU-1 (line)]] | wt | 249 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.541× (z -9.2) |
| [[HT-29 (line)]] | alt | 89.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +15.8) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +12.1) | — |
| [[SW480 (line)]] | alt | 104 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 1.81× (z +10.0) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.85× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 87.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.03× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.403× (z -11.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 85.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.4) ⚠ cell-cycle shift, explains ~22% of this change | [[Dinaciclib (drug)]] 5 µM 0.496× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 99.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +14.2) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.02× (z +8.9) | — |
| [[RKO (line)]] | wt | 127 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.204× (z -22.1) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 96.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.1) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[A498 (line)]] | wt | 146 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.607× (z -8.6) ⚠ cell-cycle shift, explains ~16% of this change |
| [[A549 (line)]] | wt | 88.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.6) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[BT-474 (line)]] | alt | 204 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.610× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 80.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.38× (z +11.4) | — |
| [[COLO 205 (line)]] | alt | 80.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.6) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[HEC-1-A (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -12.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 113 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +17.5) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[LS 180 (line)]] | wt | 88.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.94× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 96.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.02× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.28× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 56.2 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.77× (z +11.6) ⚠ toxic | — |
| [[Panc 03.27 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -13.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 74.9 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.37× (z +9.4) ⚠ toxic | — |
| [[SW1417 (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.507× (z -9.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 98.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 80.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 142 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 102 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 139 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 73.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 96.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 116 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9786), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIOK2]] | +0.60 | +0.67 / +0.47 | both halves | 2e-05 | STRING 918 |
| [[ASNSD1]] | +0.52 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[RAB33B]] | +0.52 | +0.63 / +0.33 | both halves | 1e-04 |  |
| [[MAGED1]] | +0.51 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ZNF622]] | +0.51 | +0.52 / +0.42 | both halves | 4e-05 | STRING 990 |
| [[EBAG9]] | +0.50 | +0.51 / +0.37 | both halves | 8e-05 |  |
| [[ZNF451]] | +0.50 | +0.57 / +0.36 | both halves | 1e-04 |  |
| [[RBM7]] | +0.49 | +0.58 / +0.40 | both halves | 4e-05 |  |
| [[GNL3]] | +0.49 | +0.54 / +0.39 | both halves | 5e-05 | STRING 914 |
| [[GNL2]] | +0.49 | +0.53 / +0.36 | both halves | 9e-05 | STRING 990 |
| [[SUPT20H]] | +0.48 | +0.54 / +0.31 | both halves | 2e-04 |  |
| [[ZNF550]] | +0.48 | +0.55 / +0.24 | both halves | 5e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYMPK]] | -0.49 | -0.56 / -0.26 | both halves | 4e-04 |  |
| [[C2CD3]] | -0.47 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[NFATC2IP]] | -0.47 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[WDR62]] | -0.44 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[LIN52]] | -0.43 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[FBXO36]] | -0.42 | -0.44 / -0.25 | both halves | 4e-04 |  |
| [[NSD2]] | -0.42 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[C1orf159]] | -0.41 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[GRK6]] | -0.41 | -0.42 / -0.29 | both halves | 2e-04 |  |
| [[CEP72]] | -0.41 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[ZNF544]] | -0.41 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[KATNIP]] | -0.41 | -0.47 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.371). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-37.0, -5.6); signed map (-13.1, -10.9). **Vector** length 105, 26.6% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +11.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +3.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.6 | +9.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +2.8 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.5 | +4.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +1.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.4 | -3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.2 | +1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | +0.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.9 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | NMD3 ribosome export adaptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.1 — chr3:161,104,696-161,253,532 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-07 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96D46](https://www.uniprot.org/uniprotkb/Q96D46) (60S ribosomal export protein NMD3):

> Acts as an adapter for the XPO1/CRM1-mediated export of the 60S ribosomal subunit.

**Summary**, from NCBI Gene [51068](https://www.ncbi.nlm.nih.gov/gene/51068):

> Ribosomal 40S and 60S subunits associate in the nucleolus and are exported to the cytoplasm. The protein encoded by this gene is involved in the passage of the 60S subunit through the nuclear pore complex and into the cytoplasm. Several transcript variants exist for this gene, but the full-length natures of only two have been described to date. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:24250](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24250) · Entrez [51068](https://www.ncbi.nlm.nih.gov/gene/51068) · UniProt [Q96D46](https://www.uniprot.org/uniprotkb/Q96D46) · Ensembl [ENSG00000169251](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169251)

## Data

Gene col 9786: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9786); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9786, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9786]; `tensor/DDL_lfc|DDL_z.npy` [9786]; `embed/gene_vectors.npy` [9786]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9786 or target_col == 9786). Every well: [[NMD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NMD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
