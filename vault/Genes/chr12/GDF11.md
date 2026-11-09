---
symbol: "GDF11"
type: "gene"
col: 5700
ensembl_id: "ENSG00000135414"
name: "growth differentiation factor 11"
location: "12q13.2"
module: 15
arm: "-"
pooled_cpm: 8.71
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# GDF11

*growth differentiation factor 11* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 4.28× (z +18.1, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.798× (z -4.0, q 0.031, down in 10 of 46 measured lines) ⚠ cell-cycle shift, explains ~31% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.102×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (SNU-423 0.0833×); [[Ivabradine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW 900 0.147×; ⚠ transcription drop; unreliable plate only); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (A-427 0.233×).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP1A3]] (+0.67, fdr 1e-05), [[CADM4]] (+0.62, fdr 1e-05), [[SHF]] (+0.57, fdr 1e-04); moves opposite to [[TRAPPC13]] (-0.65, fdr 1e-05), [[DDX59]] (-0.60, fdr 3e-05), [[ANGEL2]] (-0.60, fdr 3e-05).
> It sits in the **-** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SEMA6B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5700.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **4.28×** | +18.1 | 0e+00 | 42/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.74×** | +16.4 | 0e+00 | 44/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.16×** | +14.3 | 3e-44 | 42/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.94×** | +11.6 | 4e-29 | 40/46 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.52×** | +11.5 | 1e-28 | 27/33 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.47×** | +11.3 | 2e-27 | 43/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.43×** | +10.6 | 1e-24 | 12/15 (C32, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.93×** | +8.1 | 3e-14 | 30/43 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +8.1 | 4e-14 | 24/42 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.88×** | +7.8 | 3e-13 | 32/45 (SW1417, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.97×** | +7.8 | 3e-13 | 17/22 (NCI-H2347, J82, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +7.5 | 4e-12 | 27/45 (NCI-H460, A-172, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.87×** | +6.9 | 3e-10 | 28/47 (A-427, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.53×** | +5.3 | 6e-06 | 17/46 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.99×** | +4.5 | 3e-04 | 13/42 (J82, HOP62, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.025 | 9/45 (NCI-H23, A549, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.65×** | +3.3 | 0.030 | 3/43 (C32, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.038 | 10/45 (H4, HCT15, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5700.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.102×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (SNU-423 0.0833×); [[Ivabradine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW 900 0.147×; ⚠ transcription drop; unreliable plate only); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (A-427 0.233×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.798×** | -4.0 | 0.031 | 10/46 (PANC-1, SHP-77, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.612× | -3.2 | 0.33 | 7/42 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.781× | -3.1 | 0.33 | 11/46 (H4, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.788× | -3.0 | 0.36 | 7/47 (SHP-77, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5700. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 14.4 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 5.28× (z +9.6) | [[Ixazomib citrate (drug)]] 0.5 µM 0.233× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 8.83 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +13.0) | — |
| [[PANC-1 (line)]] | alt | 4.34 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.05× (z +9.6) | — |
| [[SW480 (line)]] | alt | 20.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.70× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 5.28 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +9.3) | — |
| [[J82 (line)]] | alt | 12.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.56× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 8.05 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +9.1) | [[Cobimetinib (drug)]] 5 µM 0.0833× (z -10.7) |
| [[A-172 (line)]] | wt | 8.28 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.28× (z +8.9) | — |
| [[A498 (line)]] | wt | 6.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +10.9) | — |
| [[C32 (line)]] | wt | 23.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.10× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HOP62 (line)]] | alt | 5.94 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 5.80 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.54× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 9.02 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.60× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 4.45 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0980× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.147× (z -8.6) ⚠ transcription drop; unreliable plate only |
| [[A549 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5700), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP1A3]] | +0.67 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[CADM4]] | +0.62 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[SHF]] | +0.57 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[ASMTL]] | +0.57 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[HPSE]] | +0.56 | +0.32 / +0.61 | both halves | 2e-04 |  |
| [[ANKDD1A]] | +0.55 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[SLC35B2]] | +0.55 | +0.56 / +0.29 | both halves | 2e-04 |  |
| [[NR4A1]] | +0.54 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[SEMA6B]] | +0.53 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[SUSD4]] | +0.52 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[PLPPR2]] | +0.52 | +0.19 / +0.60 | ⚠ one half (not replicated) | 9e-04 |  |
| [[SYN1]] | +0.52 | +0.37 / +0.63 | both halves | 8e-05 |  |
| [[LMCD1]] | +0.52 | +0.37 / +0.48 | both halves | 9e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC13]] | -0.65 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[DDX59]] | -0.60 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[ANGEL2]] | -0.60 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[TMEM267]] | -0.57 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[PUS10]] | -0.57 | -0.20 / -0.49 | ⚠ not reproduced | 7e-04 |  |
| [[PAAF1]] | -0.57 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[MFSD8]] | -0.56 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[NOPCHAP1]] | -0.55 | -0.37 / -0.26 | both halves | 3e-04 |  |
| [[TMEM68]] | -0.55 | -0.61 / -0.28 | both halves | 3e-04 |  |
| [[STARD7-AS1]] | -0.54 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[CLCC1]] | -0.53 | -0.57 / -0.26 | both halves | 4e-04 |  |
| [[C2orf76]] | -0.52 | -0.15 / -0.42 | ⚠ not reproduced | 0.001 |  |
| [[PPP1R8]] | -0.52 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[TSTD3]] | -0.52 | -0.23 / -0.44 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6B]] | B | SEMA6B activity raises GDF11's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.51× lower at baseline in the lines without SEMA6B | 0.025 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[SEPTIN3]] | B | SEPTIN3 activity raises GDF11's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 1.58× lower at baseline in the lines without SEPTIN3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[ATP1A3]] | B | ATP1A3 activity raises GDF11's level | lines that do not express ATP1A3 (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without ATP1A3 | 0.074 | ⚠ within organs, on part of the lines; also absent: KIF26A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **-** arm (projection on the module's main direction -0.532). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.3, 21.0); signed map (-22.2, 29.4). **Vector** length 65.3, 10.6% of its response variance represented; |z| ≥ 3 in 1,061 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +11.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +7.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.9 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.2 | +11.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.9 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +7.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +6.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.6 | +2.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | -0.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -2.5 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -0.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | growth differentiation factor 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:55,743,122-55,757,264 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BMP-11, BMP11 |
| Gene groups (HGNC) | Transforming growth factor beta superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [O95390](https://www.uniprot.org/uniprotkb/O95390) (Growth/differentiation factor 11):

> Secreted signal that acts globally to regulate anterior/posterior axial patterning during development. May play critical roles in patterning both mesodermal and neural tissues (By similarity). It is required for proper vertebral patterning and orofacial development. Signals through activin receptors type-2, ACVR2A and ACVR2B, and activin receptors type-1, ACVR1B, ACVR1C and TGFBR1 leading to the phosphorylation of SMAD2 and SMAD3.

**Summary**, from NCBI Gene [10220](https://www.ncbi.nlm.nih.gov/gene/10220):

> This gene encodes a secreted ligand of the TGF-beta (transforming growth factor-beta) superfamily of proteins. Ligands of this family bind various TGF-beta receptors leading to recruitment and activation of SMAD family transcription factors that regulate gene expression. The encoded preproprotein is proteolytically processed to generate each subunit of the disulfide-linked homodimer. This protein plays a role in the development of the nervous and other organ systems, and may regulate aging. …

**Accessions** — [HGNC:4216](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4216) · Entrez [10220](https://www.ncbi.nlm.nih.gov/gene/10220) · UniProt [O95390](https://www.uniprot.org/uniprotkb/O95390) · Ensembl [ENSG00000135414](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135414)

## Data

Gene col 5700: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5700); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5700, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5700]; `tensor/DDL_lfc|DDL_z.npy` [5700]; `embed/gene_vectors.npy` [5700]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5700 or target_col == 5700). Every well: [[GDF11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GDF11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
