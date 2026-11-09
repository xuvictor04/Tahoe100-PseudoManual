---
symbol: "DDX24"
type: "gene"
col: 1598
ensembl_id: "ENSG00000089737"
name: "DEAD-box helicase 24"
location: "14q32.12"
module: 11
arm: "+"
pooled_cpm: 97.79
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# DDX24

*DEAD-box helicase 24* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (19 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.43× (z +16.9, q 0e+00, up in 47 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.0928×, HEC-1-A 0.445×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.209×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBCC]] (+0.61, fdr 2e-05), [[GPANK1]] (+0.60, fdr 1e-05), [[CPT2]] (+0.59, fdr 1e-05); moves opposite to [[CTC1]] (-0.61, fdr 3e-05), [[PABIR2]] (-0.53, fdr 8e-05), [[CPSF6]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1598.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +16.9 | 0e+00 | 47/49 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.95×** | +12.8 | 6e-35 | 39/48 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.00×** | +9.7 | 4e-20 | 44/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.71×** | +9.7 | 7e-20 | 47/49 (PANC-1, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.03×** | +9.5 | 1e-19 | 44/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.82×** | +8.4 | 5e-15 | 47/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.65×** | +6.8 | 1e-09 | 43/50 (A-427, HS-578T, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.47×** | +6.7 | 2e-09 | 37/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.57×** | +6.4 | 1e-08 | 33/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.59×** | +6.3 | 2e-08 | 37/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.53×** | +6.0 | 9e-08 | 37/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.49×** | +5.6 | 1e-06 | 35/48 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.46×** | +5.3 | 4e-06 | 36/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +5.0 | 2e-05 | 34/48 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.9 | 3e-05 | 31/48 (BT-474, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +4.7 | 1e-04 | 33/48 (PANC-1, hTERT-HPNE, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.9 | 0.002 | 27/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.007 | 30/48 (NCI-H460, HOP62, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.018 | 33/48 (Hs 766T, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.035 | 23/48 (SHP-77, NCI-H1792, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 1.18× | +3.1 | 0.043 | 16/49 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.058 | 19/48 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.33×** | +2.8 | 0.091 | 23/47 (LS 180, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.0928×, HEC-1-A 0.445×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.209×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1598. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 52.8 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +16.0) | — |
| [[NCI-H1792 (line)]] | alt | 80.2 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +14.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +14.6) | — |
| [[NCI-H460 (line)]] | wt | 74.7 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +15.5) | — |
| [[A549 (line)]] | wt | 75.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +14.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +13.7) | — |
| [[HEC-1-A (line)]] | alt | 122 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.445× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 94.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +12.6) | — |
| [[NCI-H1573 (line)]] | alt | 48.0 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +15.4) | — |
| [[RPMI-7951 (line)]] | alt | 103 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +12.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +10.2) | — |
| [[COLO 205 (line)]] | alt | 81.3 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 63.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +14.0) | — |
| [[LOX-IMVI (line)]] | wt | 66.9 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 137 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 91.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +16.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +13.7) | — |
| [[SW 900 (line)]] | alt | 199 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +13.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.99× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 106 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +13.3) | — |
| [[AsPC-1 (line)]] | alt | 70.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +11.8) | — |
| [[BT-474 (line)]] | alt | 110 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +12.2) | — |
| [[CFPAC-1 (line)]] | alt | 112 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +17.8) | — |
| [[HOP62 (line)]] | alt | 105 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +14.1) | — |
| [[hTERT-HPNE (line)]] | wt | 81.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +11.8) | — |
| [[J82 (line)]] | alt | 123 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +11.6) | — |
| [[KATO III (line)]] | alt | 71.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +15.1) | — |
| [[LS 180 (line)]] | wt | 82.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +10.3) | — |
| [[RKO (line)]] | wt | 147 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 125 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.0928× (z -23.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 101 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +13.8) | — |
| [[A-427 (line)]] | wt | 48.5 | 1 (1 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +8.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 108 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.2) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[C32 (line)]] | wt | 99.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.6) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[H4 (line)]] | wt | 66.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 115 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 77.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +12.4) | — |
| [[HT-29 (line)]] | alt | 62.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 112 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +17.9) | — |
| [[NCI-H2030 (line)]] | alt | 196 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +14.5) | — |
| [[NCI-H2347 (line)]] | alt | 199 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +13.4) | — |
| [[SW48 (line)]] | wt | 107 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +9.1) | — |
| [[A-172 (line)]] | wt | 75.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 119 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 97.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 87.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 144 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1598), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCC]] | +0.61 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[GPANK1]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[CPT2]] | +0.59 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[PDCD7]] | +0.59 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[SIX1]] | +0.58 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[UTP3]] | +0.57 | +0.65 / +0.52 | both halves | 1e-05 | STRING 621 |
| [[VPS25]] | +0.55 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[BLOC1S4]] | +0.55 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[ADPRS]] | +0.55 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[GRPEL1]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[OXSM]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[MPLKIP]] | +0.54 | +0.44 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTC1]] | -0.61 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[PABIR2]] | -0.53 | -0.37 / -0.58 | both halves | 8e-05 |  |
| [[CPSF6]] | -0.53 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[FAM91A1]] | -0.52 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[MMGT1]] | -0.51 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[SMG1P1]] | -0.49 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[MRPL42]] | -0.49 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[DHFR]] | -0.49 | -0.26 / -0.58 | both halves | 4e-04 |  |
| [[CS]] | -0.49 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[MAT2A]] | -0.48 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[OGT]] | -0.48 | -0.40 / -0.56 | both halves | 4e-05 |  |
| [[PRDX3]] | -0.48 | -0.36 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DDX24's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.497). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.7, 5.1); signed map (2.7, -17.0). **Vector** length 80.4, 24.2% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +16.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.5 | +6.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.3 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.5 | +6.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.7 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +6.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +4.9 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.8 | +0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.7 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.1 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | +2.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~98% of this change | -3.3 | +2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Auranofin (drug)]] 0.5 µM |  | -1.5 | -0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:94,048,287-94,081,202 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | DEAD-box helicases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZR7](https://www.uniprot.org/uniprotkb/Q9GZR7) (ATP-dependent RNA helicase DDX24):

> ATP-dependent RNA helicase that plays a role in various aspects of RNA metabolism including pre-mRNA splicing and is thereby involved in different biological processes such as cell cycle regulation or innate immunity. Plays an inhibitory role in TP53 transcriptional activity and subsequently in TP53 controlled cell growth arrest and senescence by inhibiting its EP300 mediated acetylation. Negatively regulates cytosolic RNA-mediated innate immune signaling at least in part by affecting …

**Summary**, from NCBI Gene [57062](https://www.ncbi.nlm.nih.gov/gene/57062):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. This gene encodes a …

**Accessions** — [HGNC:13266](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13266) · Entrez [57062](https://www.ncbi.nlm.nih.gov/gene/57062) · UniProt [Q9GZR7](https://www.uniprot.org/uniprotkb/Q9GZR7) · Ensembl [ENSG00000089737](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089737)

## Data

Gene col 1598: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1598); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1598, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1598]; `tensor/DDL_lfc|DDL_z.npy` [1598]; `embed/gene_vectors.npy` [1598]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1598 or target_col == 1598). Every well: [[DDX24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
