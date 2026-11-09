---
symbol: "KLF13"
type: "gene"
col: 9877
ensembl_id: "ENSG00000169926"
name: "KLF transcription factor 13"
location: "15q13.3"
module: 2
arm: "+"
pooled_cpm: 42.74
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 29
n_dd_up_clean: 2
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# KLF13

*KLF transcription factor 13* — 15q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.59× (z +6.6, q 2e-08, up in 36 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 3.99×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.334× (z -22.1, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPKAPK2]] (+0.70, fdr 7e-06), [[AXIN1]] (+0.67, fdr 7e-06), [[GATAD2A]] (+0.63, fdr 7e-06); moves opposite to [[BTN3A3]] (-0.59, fdr 1e-05), [[INTU]] (-0.58, fdr 7e-06), [[PIGB]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GJB2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CYSTM1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9877.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 3.99×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.59×** | +6.6 | 2e-08 | 36/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.49×** | +5.5 | 1e-05 | 32/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.35×** | +4.1 | 0.010 | 19/48 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | 1.27× | +3.1 | 0.26 | 13/47 (C-33 A, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9877.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.334×** | -22.1 | 0e+00 | 44/47 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.334×** | -15.0 | 0e+00 | 38/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.500×** | -9.9 | 1e-20 | 40/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.494×** | -9.7 | 6e-20 | 40/45 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.537×** | -8.9 | 8e-17 | 31/47 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.575×** | -7.9 | 3e-13 | 33/48 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.362×** | -7.6 | 3e-12 | 33/49 (A549, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.580×** | -7.3 | 2e-11 | 34/48 (LOX-IMVI, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.603×** | -7.2 | 3e-11 | 29/48 (HOP62, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.627×** | -6.6 | 2e-09 | 28/48 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.413×** | -6.6 | 2e-09 | 31/42 (NCI-H23, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.625×** | -6.4 | 6e-09 | 29/48 (Panc 03.27, BT-474, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.653×** | -5.8 | 2e-07 | 27/47 (A-172, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.755×** | -5.7 | 6e-07 | 31/48 (NCI-H2347, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.680×** | -5.5 | 1e-06 | 28/47 (LoVo, KATO III, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.481×** | -5.5 | 2e-06 | 28/46 (KATO III, AsPC-1, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.709×** | -4.7 | 8e-05 | 25/47 (LoVo, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.752×** | -4.1 | 0.002 | 18/48 (CHP-212, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.699×** | -3.6 | 0.007 | 21/48 (LOX-IMVI, HOP62, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.780×** | -3.5 | 0.010 | 22/48 (J82, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Terfenadine (drug)]] 5 µM |  | 0.850× | -3.3 | 0.025 | 13/48 (HT-29, RPMI-7951, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9877. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 97.8 | 0 | 9 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0829× (z -22.3) |
| [[LOX-IMVI (line)]] | wt | 34.8 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -26.8) |
| [[LS 180 (line)]] | wt | 79.7 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -25.6) |
| [[A-172 (line)]] | wt | 47.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0620× (z -33.8) |
| [[HOP62 (line)]] | alt | 42.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -13.1) |
| [[PANC-1 (line)]] | alt | 26.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -23.3) |
| [[HT-29 (line)]] | alt | 88.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -14.7) |
| [[KATO III (line)]] | alt | 97.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -15.8) |
| [[SW480 (line)]] | alt | 46.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -20.8) |
| [[A549 (line)]] | wt | 65.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -21.6) |
| [[HEC-1-A (line)]] | alt | 31.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -18.8) |
| [[Hs 766T (line)]] | wt | 40.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -12.1) |
| [[J82 (line)]] | alt | 39.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -18.2) |
| [[MIA PaCa-2 (line)]] | alt | 21.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -16.2) |
| [[NCI-H1573 (line)]] | alt | 47.4 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.106× (z -13.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.329× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 47.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -17.9) |
| [[NCI-H2347 (line)]] | alt | 35.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -15.1) |
| [[RKO (line)]] | wt | 22.2 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.222× (z -9.1) |
| [[SW48 (line)]] | wt | 79.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -17.7) |
| [[A-427 (line)]] | wt | 31.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.294× (z -9.5) |
| [[A498 (line)]] | wt | 33.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -12.6) |
| [[AsPC-1 (line)]] | alt | 60.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.408× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 32.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 36.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.280× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 35.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -15.0) |
| [[SNU-423 (line)]] | alt | 17.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.4) |
| [[BT-474 (line)]] | alt | 26.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -13.5) |
| [[C-33 A (line)]] | alt | 32.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -9.2) |
| [[C32 (line)]] | wt | 22.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -9.8) |
| [[HS-578T (line)]] | alt | 42.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 37.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 89.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.0) |
| [[SHP-77 (line)]] | alt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[SK-MEL-2 (line)]] | alt | 37.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9877), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK2]] | +0.70 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[AXIN1]] | +0.67 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[GATAD2A]] | +0.63 | +0.64 / +0.63 | both halves | 7e-06 | pathway: Differentiation of T cells |
| [[CDC42BPB]] | +0.62 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[GFOD1]] | +0.62 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[TMC6]] | +0.60 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[VASP]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[MICAL2]] | +0.59 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[MICAL1]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[LINC00659]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[FBRSL1]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[PITPNM1]] | +0.58 | +0.64 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN3A3]] | -0.59 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[INTU]] | -0.58 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[PIGB]] | -0.58 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[BTN3A2]] | -0.56 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[EFCAB7]] | -0.56 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[CCDC43]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[FAM204A]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[ANAPC16]] | -0.54 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[PHC3]] | -0.54 | -0.46 / -0.46 | both halves | 3e-05 | pathway: Differentiation of T cells |
| [[CARD8]] | -0.54 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[MIX23]] | -0.52 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[BTN3A1]] | -0.52 | -0.51 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GJB2]] | B | GJB2 activity raises KLF13's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 1.49× lower at baseline in the lines without GJB2 | 0.068 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYSTM1]] | C | KLF13's natural level weakens CYSTM1's drug response | KLF13's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.25; direction not clear | 0.055 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.540). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-15.0, 2.0); signed map (-11.7, 40.3). **Vector** length 118, 36.0% of its response variance represented; |z| ≥ 3 in 1,339 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.9 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +0.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +5.2 | +6.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +5.0 | +5.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | -0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +1.8 |
| fall | [[NG25 (drug)]] 5 µM |  | -4.8 | -5.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.6 | -4.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -15.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.7 | -7.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.5 | -5.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.5 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -7.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.3 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | KLF transcription factor 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q13.3 — chr15:31,326,835-31,435,665 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RFLAT-1, BTEB3, NSLP1, FKLF-2 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KLF transcription factors |
| Reactome | 2 pathways, smallest: Differentiation of naive CD4+ T cells to T helper 2 cells (Th2 cells); Differentiation of T cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2Y9](https://www.uniprot.org/uniprotkb/Q9Y2Y9) (Krueppel-like factor 13):

> Transcription factor that activates expression from GC-rich minimal promoter regions, including genes in the cells of the erythroid lineage (By similarity). Represses transcription by binding to the BTE site, a GC-rich DNA element, in competition with the activator SP1. It also represses transcription by interacting with the corepressor Sin3A and HDAC1. Activates RANTES and CCL5 expression in T-cells.

**Summary**, from NCBI Gene [51621](https://www.ncbi.nlm.nih.gov/gene/51621):

> KLF13 belongs to a family of transcription factors that contain 3 classical zinc finger DNA-binding domains consisting of a zinc atom tetrahedrally coordinated by 2 cysteines and 2 histidines (C2H2 motif). These transcription factors bind to GC-rich sequences and related GT and CACCC boxes (Scohy et al., 2000 [PubMed 11087666]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:13672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13672) · Entrez [51621](https://www.ncbi.nlm.nih.gov/gene/51621) · UniProt [Q9Y2Y9](https://www.uniprot.org/uniprotkb/Q9Y2Y9) · Ensembl [ENSG00000169926](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169926)

## Data

Gene col 9877: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9877); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9877, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9877]; `tensor/DDL_lfc|DDL_z.npy` [9877]; `embed/gene_vectors.npy` [9877]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9877 or target_col == 9877). Every well: [[KLF13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLF13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
