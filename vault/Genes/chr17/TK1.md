---
symbol: "TK1"
type: "gene"
col: 9556
ensembl_id: "ENSG00000167900"
name: "thymidine kinase 1"
location: "17q25.3"
module: 6
arm: "+"
pooled_cpm: 20.86
n_lines_expressing: 47
n_dd_up: 16
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 10
direction_downstream: 35
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# TK1

*thymidine kinase 1* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.39× (z +12.1, q 3e-31, up in 37 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.48× (z +3.9, q 0.005, up in 20 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A549 6.22×, PANC-1 3.65×, SW480 2.56×, RKO 4.18×; ⚠ cell-cycle shift, explains ~46% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (SW480 5.32×, A549 7.81×, NCI-H460 5.77×; ⚠ cell-cycle shift, explains ~92% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (SW480 4.54×, A549 7.09×, NCI-H460 5.17×; ⚠ cell-cycle shift, explains ~81% of this change).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.561× (z -8.1, q 2e-13, down in 33 of 45 measured lines) ⚠ cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.499× (z -6.9, q 2e-09, down in 27 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAPG2]] (+0.86, fdr 7e-06), [[PCLAF]] (+0.86, fdr 7e-06), [[GINS2]] (+0.85, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 35 go from it, the strongest it → [[PBK]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 14 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9556.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A549 6.22×, PANC-1 3.65×, SW480 2.56×, RKO 4.18×; ⚠ cell-cycle shift, explains ~46% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (SW480 5.32×, A549 7.81×, NCI-H460 5.77×; ⚠ cell-cycle shift, explains ~92% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (SW480 4.54×, A549 7.09×, NCI-H460 5.17×; ⚠ cell-cycle shift, explains ~81% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **3.39×** | +12.1 | 3e-31 | 37/39 (PANC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **3.10×** | +10.8 | 9e-25 | 28/31 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **2.68×** | +9.8 | 2e-20 | 35/45 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **2.57×** | +9.4 | 8e-19 | 36/44 (SW480, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **2.56×** | +9.3 | 1e-18 | 39/45 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.92×** | +9.2 | 4e-18 | 33/43 (A549, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **2.66×** | +9.0 | 2e-17 | 29/36 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.95×** | +6.4 | 1e-08 | 31/45 (SW480, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.83×** | +5.8 | 5e-07 | 31/43 (SW480, PANC-1, …) | top dose only |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.41×** | +4.8 | 9e-05 | 30/45 (HT-29, SW480, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.36×** | +4.3 | 9e-04 | 23/45 (SW480, PANC-1, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.48×** | +3.9 | 0.005 | 20/45 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.44×** | +3.6 | 0.013 | 17/45 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.023 | 19/43 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.40×** | +3.3 | 0.031 | 20/45 (A498, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9556.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.561×** | -8.1 | 2e-13 | 33/45 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.499×** | -6.9 | 2e-09 | 27/43 (H4, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.625×** | -6.6 | 6e-09 | 28/43 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.537×** | -6.1 | 1e-07 | 31/45 (A498, LS 180, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.473×** | -5.9 | 4e-07 | 29/45 (A-172, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.587×** | -3.8 | 0.014 | 21/45 (SW480, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.692×** | -3.7 | 0.019 | 18/44 (A-172, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.788×** | -3.4 | 0.054 | 19/45 (HS-578T, COLO 205, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.726×** | -3.2 | 0.082 | 19/45 (COLO 205, SNU-1, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.799×** | -3.2 | 0.082 | 19/45 (NCI-H460, CFPAC-1, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.523×** | -3.1 | 0.085 | 15/43 (A498, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.802×** | -3.1 | 0.085 | 20/45 (CFPAC-1, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.30 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9556. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 13.4 | 5 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.22× (z +13.7) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[A498 (line)]] | wt | 35.6 | 1 (1 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | [[Selinexor (drug)]] 5 µM 0.164× (z -17.4) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SW480 (line)]] | alt | 23.0 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.32× (z +12.8) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[A-427 (line)]] | wt | 42.0 | 1 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.74× (z +8.6) ⚠ cell-cycle shift, explains ~92% of this change | [[Selinexor (drug)]] 5 µM 0.166× (z -16.7) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.169× (z -16.5) |
| [[LS 180 (line)]] | wt | 16.6 | 0 | 3 (1 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.196× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 11.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.77× (z +9.9) ⚠ cell-cycle shift, explains ~92% of this change | [[Selinexor (drug)]] 5 µM 0.343× (z -8.6) ⚠ cell-cycle shift, explains ~57% of this change |
| [[PANC-1 (line)]] | alt | 18.1 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +12.5) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[H4 (line)]] | wt | 22.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0539× (z -11.6) |
| [[HCT15 (line)]] | alt | 33.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.1000× (z -11.5) |
| [[HT-29 (line)]] | alt | 22.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.72× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | [[Selinexor (drug)]] 5 µM 0.301× (z -9.1) ⚠ cell-cycle shift, explains ~57% of this change |
| [[KATO III (line)]] | alt | 53.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 17.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -15.3) |
| [[NCI-H23 (line)]] | alt | 30.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -12.5) |
| [[A-172 (line)]] | wt | 24.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.235× (z -10.3) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HEC-1-A (line)]] | alt | 50.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -9.7) |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 26.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +8.7) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[RKO (line)]] | wt | 14.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +9.4) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[SNU-423 (line)]] | alt | 13.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +8.5) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[SW48 (line)]] | wt | 20.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -10.3) |
| [[AN3 CA (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.08 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.72 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.91 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9556), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAPG2]] | +0.86 | +0.87 / +0.84 | both halves | 7e-06 | STRING 424 |
| [[PCLAF]] | +0.86 | +0.83 / +0.86 | both halves | 7e-06 | STRING 820 |
| [[GINS2]] | +0.85 | +0.85 / +0.81 | both halves | 7e-06 | STRING 572 |
| [[SPC25]] | +0.84 | +0.84 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 689 |
| [[EXO1]] | +0.84 | +0.85 / +0.82 | both halves | 7e-06 | STRING 657 |
| [[RRM2]] | +0.84 | +0.80 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 914 |
| [[TCF19]] | +0.84 | +0.80 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[MYBL2]] | +0.83 | +0.83 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 765 |
| [[RAD51AP1]] | +0.83 | +0.83 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 446 |
| [[SPC24]] | +0.82 | +0.81 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 444 |
| [[MELK]] | +0.82 | +0.81 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 792 |
| [[DTL]] | +0.82 | +0.82 / +0.80 | both halves | 7e-06 | STRING 516 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TK1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TCF19]] | C | TCF19 activity raises TK1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.67× lower at baseline in the lines without TCF19 | 0.005 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent; co-absent with the target |
| [[AURKB]] | C | AURKB activity raises TK1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.07× lower at baseline in the lines without AURKB | 0.011 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[PBK]] | C | PBK activity raises TK1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.63× lower at baseline in the lines without PBK | 0.035 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[MCM10]] | C | MCM10 activity raises TK1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.25× lower at baseline in the lines without MCM10 | 0.043 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[C21orf58]], [[CDC45]], [[CENPM]], [[SKA3]] | C | C21orf58, CDC45, CENPM, SKA3 activity raises TK1's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.92× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises TK1's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.88× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[CLSPN]] | C | CLSPN activity raises TK1's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.45× lower at baseline in the lines without CLSPN | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent |
| [[PKMYT1]] | C | PKMYT1 activity raises TK1's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 2.94× lower at baseline in the lines without PKMYT1 | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; co-absent with the target |
| [[MYBL2]] | C | MYBL2 activity raises TK1's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.64× lower at baseline in the lines without MYBL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 0, C 35. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PBK]] | C | [[DIAPH3]], [[MELK]], TK1 activity raises PBK's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 4.05× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[IQGAP3]] | C | [[DIAPH3]], [[MELK]], TK1 activity raises IQGAP3's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 3.79× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[PCLAF]] | C | [[MELK]], TK1 activity raises PCLAF's level | lines that do not express MELK, TK1 (3) vs lines expressing them (47) | 3.56× lower at baseline in the lines without MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[EME1]] | C | [[DIAPH3]], [[MELK]], TK1 activity raises EME1's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 3.22× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[FANCI]] | C | [[DIAPH3]], [[MELK]], TK1 activity raises FANCI's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 3.15× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[GGH]] | C | [[MELK]], TK1 activity raises GGH's level | lines that do not express MELK, TK1 (3) vs lines expressing them (47) | 3.07× lower at baseline in the lines without MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[ZWINT]] | C | [[DIAPH3]], [[MELK]], TK1 activity raises ZWINT's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 2.80× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[FBXO5]] | C | [[DIAPH3]], [[MELK]], TK1 activity raises FBXO5's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 2.76× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[MAD2L1]] | C | [[DIAPH3]], [[MELK]], TK1 activity raises MAD2L1's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 2.76× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[KNTC1]] | C | [[DIAPH3]], [[MELK]], TK1 activity raises KNTC1's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 2.70× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CDT1]] | C | [[MELK]], TK1 activity raises CDT1's level | lines that do not express MELK, TK1 (3) vs lines expressing them (47) | 2.68× lower at baseline in the lines without MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[BRIP1]] | C | [[DIAPH3]], [[MELK]], TK1 activity raises BRIP1's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 2.61× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.842). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.6, -45.3); signed map (-38.3, -44.3). **Vector** length 127, 40.8% of its response variance represented; |z| ≥ 3 in 1,066 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.67 to 28); *DNA Replication* (reactome, mean cos +0.66 to 40); *E2F G1/S* (control, mean cos +0.67 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | +5.2 | +12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | +5.1 | +10.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | +4.9 | +9.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +4.8 | +9.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +4.2 | +9.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.6 | +3.9 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +2.5 | +3.4 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.5 | +2.8 |
|  | [[Methotrexate (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.3 | +2.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -8.5 | -8.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | -7.3 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.3 | -6.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | -5.9 | -5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.3 | -6.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.5 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -1.4 |
|  | [[EX229 (drug)]] 5 µM |  | -3.3 | -3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.0 | -1.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | thymidine kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:78,174,091-78,187,233 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Deoxyribonucleoside kinases |
| Hallmark sets | E2F_TARGETS |
| Reactome | 8 pathways, smallest: Pyrimidine salvage; Nucleotide salvage; G1/S-Specific Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [P04183](https://www.uniprot.org/uniprotkb/P04183) (Thymidine kinase, cytosolic):

> Cell-cycle-regulated enzyme of importance in nucleotide metabolism. Catalyzes the first enzymatic step in the salvage pathway converting thymidine into thymidine monophosphate. Transcriptional regulation limits expression to the S phase of the cell cycle and transient expression coincides with the oscillation in the intracellular dTTP concentration (Probable). Also important for the activation of anticancer and antiviral nucleoside analog prodrugs such as 1-b-d-arabinofuranosylcytosine (AraC) …

**Summary**, from NCBI Gene [7083](https://www.ncbi.nlm.nih.gov/gene/7083):

> The protein encoded by this gene is a cytosolic enzyme that catalyzes the addition of a gamma-phosphate group to thymidine. This creates dTMP and is the first step in the biosynthesis of dTTP, which is one component required for DNA replication. The encoded protein, whose levels fluctuate depending on the cell cycle stage, can act as a low activity dimer or a high activity tetramer. High levels of this protein have been used as a biomarker for diagnosing and categorizing many types of cancers. …

**Accessions** — [HGNC:11830](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11830) · Entrez [7083](https://www.ncbi.nlm.nih.gov/gene/7083) · UniProt [P04183](https://www.uniprot.org/uniprotkb/P04183) · Ensembl [ENSG00000167900](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167900)

## Data

Gene col 9556: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9556); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9556, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9556]; `tensor/DDL_lfc|DDL_z.npy` [9556]; `embed/gene_vectors.npy` [9556]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9556 or target_col == 9556). Every well: [[TK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
