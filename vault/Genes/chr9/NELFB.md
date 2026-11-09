---
symbol: "NELFB"
type: "gene"
col: 12071
ensembl_id: "ENSG00000188986"
name: "negative elongation factor complex member B"
location: "9q34.3"
module: 3
arm: "+"
pooled_cpm: 29.65
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# NELFB

*negative elongation factor complex member B* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.69× (z +10.0, q 7e-21, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.715× (z -6.2, q 4e-07, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-172 0.352×, SNU-1 0.254×, J82 0.509×, NCI-H2347 0.521×; ⚠ cell-cycle shift, explains ~46% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-172 0.222×, SNU-1 0.140×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 0.122×, NCI-H460 0.400×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 0.354×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.586×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHRF1]] (+0.66, fdr 1e-05), [[MARK4]] (+0.64, fdr 3e-05), [[MEX3D]] (+0.62, fdr 1e-05); moves opposite to [[ABLIM1]] (-0.52, fdr 4e-05), [[RASEF]] (-0.51, fdr 5e-05), [[ARAP2]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12071.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +10.0 | 7e-21 | 35/47 (SW480, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.34×** | +8.0 | 4e-13 | 25/47 (A498, NCI-H1792, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +7.3 | 4e-11 | 29/48 (RKO, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +7.1 | 2e-10 | 28/48 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.41×** | +6.7 | 3e-09 | 28/48 (SW480, RKO, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.39×** | +6.4 | 2e-08 | 28/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +5.5 | 4e-06 | 23/46 (SW480, C-33 A, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.31×** | +5.1 | 2e-05 | 25/46 (HS-578T, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.30×** | +5.0 | 4e-05 | 20/43 (SW1417, LS 180, …) | two highest doses | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.62×** | +4.8 | 7e-05 | 22/48 (NCI-H460, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.26×** | +4.3 | 0.001 | 17/37 (SW480, LoVo, …) | two highest doses | composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.007 | 16/46 (LoVo, NCI-H460, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.007 | 13/48 (SNU-423, RKO, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.14× | +3.7 | 0.010 | 10/48 (A498, A-427, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.025 | 16/47 (HOP62, CFPAC-1, …) | two highest doses | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.025 | 13/47 (HCT15, hTERT-HPNE, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.025 | 13/47 (LOX-IMVI, HEC-1-A, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.025 | 5/47 (LoVo, SW480, …) | inconsistent across doses | position effect removed |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.052 | 4/47 (SNU-423, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12071.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-172 0.352×, SNU-1 0.254×, J82 0.509×, NCI-H2347 0.521×; ⚠ cell-cycle shift, explains ~46% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-172 0.222×, SNU-1 0.140×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 0.122×, NCI-H460 0.400×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 0.354×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.586×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.715×** | -6.2 | 4e-07 | 29/48 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 0.868× | -3.8 | 0.041 | 18/48 (A498, Panc 03.27, …) | top dose only | low cells (technical?) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.829×** | -3.6 | 0.067 | 9/48 (HEC-1-A, LS 180, …) | two highest doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.884× | -3.3 | 0.14 | 15/48 (A498, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.844× | -3.2 | 0.14 | 4/48 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Finasteride (drug)]] 5 µM |  | 0.847× | -3.0 | 0.23 | 8/47 (HT-29, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12071. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 61.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -16.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.354× (z -11.2) |
| [[C32 (line)]] | wt | 27.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.9× (z +27.0) ⚠ cell-cycle shift, explains ~46% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.277× (z -9.1) ⚠ toxic |
| [[LoVo (line)]] | wt | 25.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +15.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 15.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +14.4) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 28.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +20.4) ⚠ cell-cycle shift, explains ~46% of this change | [[Dinaciclib (drug)]] 5 µM 0.400× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[SNU-1 (line)]] | wt | 26.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 42.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +30.6) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[A549 (line)]] | wt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[AsPC-1 (line)]] | alt | 29.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 24.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.36× (z +24.7) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 24.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.70× (z +17.1) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[J82 (line)]] | alt | 54.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -10.0) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LOX-IMVI (line)]] | wt | 34.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +18.7) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H1792 (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.9× (z +28.9) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H2347 (line)]] | alt | 26.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -8.7) ⚠ cell-cycle shift, explains ~46% of this change |
| [[RPMI-7951 (line)]] | alt | 23.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.74× (z +17.2) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 33.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.0) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[SNU-423 (line)]] | alt | 30.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.6) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[SW480 (line)]] | alt | 26.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.37× (z +9.2) | — |
| [[A-427 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12071), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHRF1]] | +0.66 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[MARK4]] | +0.64 | +0.46 / +0.70 | both halves | 3e-05 |  |
| [[MEX3D]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ZNF251]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[MPND]] | +0.62 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[MARCHF2]] | +0.61 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[PPP6R1]] | +0.61 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[SELENOO]] | +0.60 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[RBAK-RBAKDN]] | +0.59 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[CSK]] | +0.59 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[TRIM11]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.58 | +0.41 / +0.60 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABLIM1]] | -0.52 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[RASEF]] | -0.51 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[ARAP2]] | -0.50 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[RFK]] | -0.49 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[LINC02605]] | -0.49 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[PHACTR2]] | -0.48 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[NFKB1]] | -0.48 | -0.29 / -0.45 | both halves | 3e-04 | pathway: Affinity selection of immunoglobulins |
| [[DECR1]] | -0.48 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[ETNK1]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.504). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-12.1, -5.6); signed map (-41.3, 3.9). **Vector** length 82.8, 16.0% of its response variance represented; |z| ≥ 3 in 797 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.1 | +10.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.5 | +6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +7.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +0.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.2 | -6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | -0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.3 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.7 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | negative elongation factor complex member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,255,327-137,273,542 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1182, NELF-B; previously COBRA1 |
| Gene groups (HGNC) | Negative elongation factor complex members |
| Hallmark sets | DNA_REPAIR |
| Reactome | 29 pathways, smallest: NTRK3 as a dependence receptor; Signaling by NTRK3 (TRKC); Abortive elongation of HIV-1 transcript in the absence of Tat |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WX92](https://www.uniprot.org/uniprotkb/Q8WX92) (Negative elongation factor B):

> Essential component of the NELF complex, a complex that negatively regulates the elongation of transcription by RNA polymerase II. The NELF complex, which acts via an association with the DSIF complex and causes transcriptional pausing, is counteracted by the P-TEFb kinase complex. May be able to induce chromatin unfolding. Essential for early embryogenesis; plays an important role in maintaining the undifferentiated state of embryonic stem cells (ESCs) by preventing unscheduled expression of …

**Summary**, from NCBI Gene [25920](https://www.ncbi.nlm.nih.gov/gene/25920):

> NELFB is a subunit of negative elongation factor (NELF), which also includes NELFA (WHSC2; MIM 606026), either NELFC or NELFD (TH1L; MIM 605297), and NELFE (RDBP; MIM 154040). NELF acts with DRB sensitivity-inducing factor (DSIF), a heterodimer of SPT4 (SUPT4H1; MIM 603555) and SPT5 (SUPT5H; MIM 602102), to cause transcriptional pausing of RNA polymerase II (see MIM 180660) (Narita et al., 2003 [PubMed 12612062]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24324](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24324) · Entrez [25920](https://www.ncbi.nlm.nih.gov/gene/25920) · UniProt [Q8WX92](https://www.uniprot.org/uniprotkb/Q8WX92) · Ensembl [ENSG00000188986](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188986)

## Data

Gene col 12071: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12071); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12071, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12071]; `tensor/DDL_lfc|DDL_z.npy` [12071]; `embed/gene_vectors.npy` [12071]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12071 or target_col == 12071). Every well: [[NELFB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NELFB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
