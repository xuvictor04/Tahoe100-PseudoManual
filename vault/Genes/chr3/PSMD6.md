---
symbol: "PSMD6"
type: "gene"
col: 8741
ensembl_id: "ENSG00000163636"
name: "proteasome 26S subunit, non-ATPase 6"
location: "3p14.1"
module: 64
arm: "+"
pooled_cpm: 30.21
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# PSMD6

*proteasome 26S subunit, non-ATPase 6* — 3p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (22 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 3.39× (z +18.6, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Entecavir (monohydrate) (drug)]] 5 µM: 0.764× (z -3.9, q 0.036, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0556×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.204×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (COLO 205 0.0963×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMC5]] (+0.81, fdr 7e-06), [[PSMC3]] (+0.71, fdr 7e-06), [[MRPL9]] (+0.71, fdr 7e-06); moves opposite to [[IGFBP2]] (-0.57, fdr 1e-05), [[PTMA]] (-0.56, fdr 3e-05), [[PRDX4]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 22 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8741.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.39×** | +18.6 | 0e+00 | 47/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.12×** | +17.3 | 0e+00 | 47/47 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.10×** | +17.2 | 0e+00 | 47/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.32×** | +17.1 | 0e+00 | 45/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.24×** | +13.4 | 4e-39 | 45/48 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.33×** | +12.4 | 3e-33 | 47/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.12×** | +11.4 | 2e-28 | 41/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.90×** | +9.8 | 8e-21 | 42/48 (C32, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.75×** | +8.5 | 9e-16 | 42/48 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **1.70×** | +8.1 | 3e-14 | 35/44 (MIA PaCa-2, A-427, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.70×** | +8.1 | 3e-14 | 45/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.11×** | +8.1 | 3e-14 | 40/48 (LOX-IMVI, HOP62, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.73×** | +8.0 | 6e-14 | 38/42 (Panc 03.27, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.69×** | +8.0 | 6e-14 | 38/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.67×** | +7.8 | 2e-13 | 43/48 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.63×** | +7.7 | 5e-13 | 39/48 (KATO III, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +4.8 | 3e-05 | 21/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +4.1 | 7e-04 | 17/48 (SNU-423, MIA PaCa-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.63×** | +3.9 | 0.002 | 22/47 (LS 180, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.012 | 12/48 (SHP-77, SW48, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +2.9 | 0.058 | 13/48 (A498, LOX-IMVI, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.30×** | +2.9 | 0.060 | 18/44 (LS 180, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8741.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0556×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.204×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (COLO 205 0.0963×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **0.764×** | -3.9 | 0.036 | 19/48 (HEC-1-A, LOX-IMVI, …) | top dose only | plate-row cell shift; position effect removed |
| [[Rifaximin (drug)]] 5 µM |  | **0.769×** | -3.8 | 0.036 | 22/47 (hTERT-HPNE, CFPAC-1, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.817× | -3.1 | 0.40 | 17/48 (C32, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8741. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 40.2 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.26× (z +12.8) | — |
| [[NCI-H460 (line)]] | wt | 25.6 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.98× (z +13.7) | — |
| [[PANC-1 (line)]] | alt | 20.0 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +14.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.77× (z +14.1) | — |
| [[HOP62 (line)]] | alt | 21.9 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.07× (z +12.0) | — |
| [[LoVo (line)]] | wt | 28.5 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.19× (z +13.6) | — |
| [[NCI-H1573 (line)]] | alt | 29.3 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.93× (z +13.3) | — |
| [[SNU-423 (line)]] | alt | 29.3 | 6 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.84× (z +11.4) | — |
| [[C32 (line)]] | wt | 29.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.64× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 38.6 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.23× (z +13.2) | — |
| [[HEC-1-A (line)]] | alt | 38.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.23× (z +12.8) | — |
| [[KATO III (line)]] | alt | 26.9 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.93× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 26.5 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.76× (z +12.1) | — |
| [[A-172 (line)]] | wt | 28.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +12.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.76× (z +10.2) | — |
| [[A498 (line)]] | wt | 27.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +11.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.84× (z +9.0) | — |
| [[A549 (line)]] | wt | 21.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +11.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.90× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 22.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.69× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 30.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.35× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 42.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.39× (z +11.0) | — |
| [[A-427 (line)]] | wt | 21.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.71× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 32.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +10.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.45× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 20.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.14× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 23.0 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.99× (z +8.8) | — |
| [[J82 (line)]] | alt | 36.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.83× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 47.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.80× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 48.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.45× (z +11.8) | — |
| [[RPMI-7951 (line)]] | alt | 44.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.86× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 59.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 15.7 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.68× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 27.1 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0556× (z -10.4) |
| [[COLO 205 (line)]] | alt | 11.5 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0963× (z -9.3) |
| [[HCT15 (line)]] | alt | 35.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.89× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 26.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.49× (z +8.6) | — |
| [[RKO (line)]] | wt | 51.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.98× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 40.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[SW 900 (line)]] | alt | 27.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[AN3 CA (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8741), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMC5]] | +0.81 | +0.87 / +0.75 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMC3]] | +0.71 | +0.79 / +0.61 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[MRPL9]] | +0.71 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[PSMD11]] | +0.70 | +0.72 / +0.69 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMD4]] | +0.69 | +0.78 / +0.59 | both halves | 7e-06 | same gene group; pathway: Proteasome assembly; STRING 999 |
| [[MRPL45]] | +0.68 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[ANXA7]] | +0.67 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[NSFL1C]] | +0.65 | +0.56 / +0.79 | both halves | 1e-05 | STRING 410 |
| [[NUDT9]] | +0.64 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[RNF6]] | +0.64 | +0.78 / +0.61 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[PSMD7]] | +0.64 | +0.78 / +0.49 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMC1]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGFBP2]] | -0.57 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[PTMA]] | -0.56 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[PRDX4]] | -0.56 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[SLC25A5]] | -0.54 | -0.58 / -0.43 | both halves | 4e-05 | pathway: HIV Infection |
| [[CA5BP1]] | -0.53 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[ATP1B3]] | -0.52 | -0.56 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.737). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-22.7, -9.7); signed map (-6.3, -35.9). **Vector** length 72.2, 17.4% of its response variance represented; |z| ≥ 3 in 1,219 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.7 | +17.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.6 | +13.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.6 | +18.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +17.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +9.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +8.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -3.5 | +4.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | -3.3 | +6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -3.2 | +7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -3.1 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | +0.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -1.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit, non-ATPase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.1 — chr3:64,010,550-64,024,010 (-) |
| Ensembl biotype | protein_coding |
| Also known as | S10, p44S10, KIAA0107, Rpn7 |
| Gene groups (HGNC) | Proteasome |
| Reactome | 170 pathways, smallest: Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC); Cross-presentation of soluble exogenous antigens (endosomes) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15008](https://www.uniprot.org/uniprotkb/Q15008) (26S proteasome non-ATPase regulatory subunit 6):

> Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair.

**Summary**, from NCBI Gene [9861](https://www.ncbi.nlm.nih.gov/gene/9861):

> This gene encodes a member of the protease subunit S10 family. The encoded protein is a subunit of the 26S proteasome which colocalizes with DNA damage foci and is involved in the ATP-dependent degradation of ubiquinated proteins. Alternative splicing results in multiple transcript variants [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:9564](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9564) · Entrez [9861](https://www.ncbi.nlm.nih.gov/gene/9861) · UniProt [Q15008](https://www.uniprot.org/uniprotkb/Q15008) · Ensembl [ENSG00000163636](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163636)

## Data

Gene col 8741: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8741); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8741, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8741]; `tensor/DDL_lfc|DDL_z.npy` [8741]; `embed/gene_vectors.npy` [8741]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8741 or target_col == 8741). Every well: [[PSMD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
