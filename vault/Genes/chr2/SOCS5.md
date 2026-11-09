---
symbol: "SOCS5"
type: "gene"
col: 10061
ensembl_id: "ENSG00000171150"
name: "suppressor of cytokine signaling 5"
location: "2p21"
module: 35
arm: "+"
pooled_cpm: 79.0
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# SOCS5

*suppressor of cytokine signaling 5* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.96× (z +12.0, q 3e-30, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.431× (z -14.0, q 8e-42, down in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.572× (z -9.3, q 3e-18, down in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (LS 180 0.0677×, HCT15 0.0947×, Panc 03.27 0.149×, NCI-H2030 0.228×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (Panc 03.27 0.127×, CHP-212 0.107×, A-172 0.270×, NCI-H1573 0.308×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 3 lines (hTERT-HPNE 0.253×, A549 0.417×, A-172 0.416×).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SP3]] (+0.61, fdr 1e-05), [[MSL2]] (+0.59, fdr 8e-06), [[ZKSCAN7-AS1]] (+0.58, fdr 1e-04); moves opposite to [[LMBR1]] (-0.47, fdr 7e-05), [[GAN]] (-0.46, fdr 8e-05), [[SLC9A1]] (-0.44, fdr 2e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SOCS2-AS1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LINC01118]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10061.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.96×** | +12.0 | 3e-30 | 45/49 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +6.5 | 2e-08 | 30/48 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +5.7 | 2e-06 | 32/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +5.7 | 2e-06 | 29/48 (NCI-H2030, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +4.7 | 3e-04 | 26/48 (NCI-H2030, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.9 | 0.011 | 23/48 (NCI-H23, PANC-1, …) | top dose only | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.17× | +3.8 | 0.014 | 20/48 (A549, CFPAC-1, …) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10061.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (LS 180 0.0677×, HCT15 0.0947×, Panc 03.27 0.149×, NCI-H2030 0.228×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (Panc 03.27 0.127×, CHP-212 0.107×, A-172 0.270×, NCI-H1573 0.308×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 3 lines (hTERT-HPNE 0.253×, A549 0.417×, A-172 0.416×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.431×** | -14.0 | 8e-42 | 43/49 (Panc 03.27, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.475×** | -11.5 | 5e-28 | 39/44 (LS 180, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.572×** | -9.3 | 3e-18 | 39/48 (hTERT-HPNE, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.599×** | -8.5 | 2e-15 | 40/48 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.658×** | -7.0 | 4e-10 | 37/48 (hTERT-HPNE, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.787×** | -4.0 | 0.007 | 25/48 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.776×** | -3.9 | 0.008 | 24/45 (NCI-H2030, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.805×** | -3.3 | 0.060 | 24/47 (RKO, hTERT-HPNE, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.828× | -3.1 | 0.11 | 18/48 (H4, J82, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.831× | -3.1 | 0.12 | 20/48 (AN3 CA, HCT15, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10061. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 232 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -13.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.253× (z -10.4) |
| [[A549 (line)]] | wt | 141 | 1 (1 ⚠) | 3 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.97× (z +9.3) ⚠ cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -12.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.417× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 143 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.99× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.228× (z -15.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 111 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.416× (z -8.6) |
| [[A-427 (line)]] | wt | 91.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.17× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -13.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 55.1 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 11.2× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 84.3 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.52× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 122 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +15.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.314× (z -11.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 68.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +15.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.00× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -10.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 68.8 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.92× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.504× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 61.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -8.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 75.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -9.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 54.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0677× (z -23.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 51.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 57.1 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.29× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 99.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -20.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 57.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -11.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 92.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.99× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -9.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 84.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -8.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[AsPC-1 (line)]] | alt | 61.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C-33 A (line)]] | alt | 75.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.345× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[CHP-212 (line)]] | wt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -13.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 75.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0947× (z -18.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 60.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.72× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 85.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -9.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 159 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.362× (z -9.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HT-29 (line)]] | alt | 50.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -9.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 48.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.00× (z +9.0) | — |
| [[LoVo (line)]] | wt | 37.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -12.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 52.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 73.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -13.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 84.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -11.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -10.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 47.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.6× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 75.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 87.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10061), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 16 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SP3]] | +0.61 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[MSL2]] | +0.59 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[ZKSCAN7-AS1]] | +0.58 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[PRRT2]] | +0.58 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[ZBED5-AS1]] | +0.53 | +0.20 / +0.46 | both halves | 7e-04 |  |
| [[LINC01119]] | +0.52 | +0.62 / +0.43 | both halves | 3e-05 | ⚠ same locus (36.5 kb, same strand: neighbours can correlate without regulation) |
| [[LINC00938]] | +0.52 | +0.33 / +0.47 | both halves | 1e-04 |  |
| [[LINC01118]] | +0.51 | +0.60 / +0.44 | both halves | 3e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PRSS23]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[PLEKHF2]] | +0.49 | +0.33 / +0.45 | both halves | 1e-04 |  |
| [[C1D]] | +0.49 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[MRPS14]] | +0.49 | +0.31 / +0.48 | both halves | 2e-04 |  |
| [[RCHY1]] | +0.48 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[C3orf38]] | +0.47 | +0.27 / +0.40 | both halves | 3e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMBR1]] | -0.47 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[GAN]] | -0.46 | -0.37 / -0.49 | both halves | 8e-05 | pathway: Neddylation |
| [[SLC9A1]] | -0.44 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[ATF6]] | -0.44 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[PRKCZ]] | -0.44 | -0.13 / -0.39 | ⚠ not reproduced | 0.002 |  |
| [[VPS13D]] | -0.43 | -0.16 / -0.48 | ⚠ not reproduced | 0.001 |  |
| [[TBC1D16]] | -0.43 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[LRRFIP1]] | -0.42 | -0.19 / -0.37 | ⚠ not reproduced | 9e-04 |  |
| [[EPS15L1]] | -0.41 | -0.23 / -0.38 | both halves | 5e-04 |  |
| [[AGTPBP1]] | -0.41 | -0.27 / -0.37 | both halves | 3e-04 |  |
| [[GMDS]] | -0.41 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[MTHFD1L]] | -0.41 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[MROH1]] | -0.41 | -0.27 / -0.47 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOCS2-AS1]] | B | SOCS2-AS1 activity raises SOCS5's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 1.47× lower at baseline in the lines without SOCS2-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |
| [[CARMN]] | B | CARMN activity raises SOCS5's level | lines that do not express CARMN (40) vs lines expressing it (10) | 1.79× lower at baseline in the lines without CARMN | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN |
| [[HDAC6]] | B | HDAC6 activity raises SOCS5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PRKCZ]] | B | PRKCZ activity lowers SOCS5's level | lines that do not express PRKCZ (10) vs lines expressing it (40) | 1.73× higher at baseline in the lines without PRKCZ | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000258593, AP1G2, CHMP4C |
| [[SOCS2]] | B | SOCS2 activity raises SOCS5's level | lines that do not express SOCS2 (10) vs lines expressing it (40) | 1.44× lower at baseline in the lines without SOCS2 | 0.097 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, HOXC9, TMEM45A |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01118]] | C | SOCS5's natural level strengthens LINC01118's drug response | SOCS5's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.51; direction not clear | 0.018 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.316). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (6.5, 25.7); signed map (37.0, -3.1). **Vector** length 91.0, 24.1% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +6.3 | +3.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +12.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | +4.6 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.6 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +0.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.2 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +0.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -2.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.6 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.4 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -0.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | suppressor of cytokine signaling 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:46,698,952-46,780,245 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0671, SOCS-5, CIS6, CISH6, Cish5 |
| Gene groups (HGNC) | SH2 domain containing; Suppressors of cytokine signaling |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 4 pathways, smallest: Interleukin-4 and Interleukin-13 signaling; Neddylation; Signaling by Interleukins |
| Matched by | ensembl_id |

**Function**, from UniProt [O75159](https://www.uniprot.org/uniprotkb/O75159) (Suppressor of cytokine signaling 5):

> SOCS family proteins form part of a classical negative feedback system that regulates cytokine signal transduction. May be a substrate-recognition component of a SCF-like ECS (Elongin BC-CUL2/5-SOCS-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Inhibits for instance EGF signaling by mediating the degradation of the EGF receptor/EGFR. Involved in the regulation of T-helper cell differentiation by …

**Summary**, from NCBI Gene [9655](https://www.ncbi.nlm.nih.gov/gene/9655):

> The protein encoded by this gene contains a SH2 domain and a SOCS BOX domain. The protein thus belongs to the suppressor of cytokine signaling (SOCS) family, also known as STAT-induced STAT inhibitor (SSI) protein family. SOCS family members are known to be cytokine-inducible negative regulators of cytokine signaling. The specific function of this protein has not yet been determined. Two alternatively spliced transcript variants encoding an identical protein have been reported. [provided by …

**Accessions** — [HGNC:16852](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16852) · Entrez [9655](https://www.ncbi.nlm.nih.gov/gene/9655) · UniProt [O75159](https://www.uniprot.org/uniprotkb/O75159) · Ensembl [ENSG00000171150](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171150)

## Data

Gene col 10061: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10061); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10061, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10061]; `tensor/DDL_lfc|DDL_z.npy` [10061]; `embed/gene_vectors.npy` [10061]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10061 or target_col == 10061). Every well: [[SOCS5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOCS5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
