---
symbol: "RANBP6"
type: "gene"
col: 5958
ensembl_id: "ENSG00000137040"
name: "RAN binding protein 6"
location: "9p24.1"
module: 16
arm: "+"
pooled_cpm: 14.71
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# RANBP6

*RAN binding protein 6* — 9p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.59× (z +15.4, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.799× (z -5.2, q 9e-05, down in 20 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (KATO III 0.182×, Hs 766T 0.152×, A-172 0.229×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.126×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.225×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSTF2T]] (+0.70, fdr 7e-06), [[MRPL47]] (+0.68, fdr 7e-06), [[ZKSCAN2]] (+0.67, fdr 7e-06); moves opposite to [[NAP1L1]] (-0.58, fdr 3e-05), [[PMS2P4-1]] (-0.58, fdr 1e-05), [[LONRF1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ANAPC1P4]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5958.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.59×** | +15.4 | 0e+00 | 45/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.39×** | +14.1 | 1e-42 | 44/47 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.24×** | +13.1 | 9e-37 | 37/44 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.13×** | +12.2 | 3e-32 | 42/46 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.15×** | +11.5 | 2e-28 | 25/32 (SW480, LS 180, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.02×** | +11.3 | 9e-28 | 33/46 (SW480, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.99×** | +11.1 | 1e-26 | 37/46 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.03×** | +11.0 | 2e-26 | 37/45 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.62×** | +11.0 | 2e-26 | 33/45 (SW48, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.12×** | +9.6 | 3e-20 | 35/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.76×** | +9.1 | 3e-18 | 34/46 (A-172, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +7.8 | 2e-13 | 35/45 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.30×** | +7.1 | 7e-11 | 27/43 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.50×** | +6.3 | 1e-08 | 12/26 (HEC-1-A, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **1.46×** | +6.1 | 3e-08 | 16/38 (Hs 766T, AsPC-1, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +6.1 | 3e-08 | 24/46 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.00×** | +5.9 | 2e-07 | 22/47 (NCI-H460, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.2 | 6e-06 | 15/47 (SW480, AN3 CA, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.005 | 13/46 (HEC-1-A, KATO III, …) | two highest doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.26×** | +3.7 | 0.006 | 11/43 (SW 900, LoVo, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Busulfan (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.016 | 5/46 (PANC-1, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5958.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (KATO III 0.182×, Hs 766T 0.152×, A-172 0.229×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.126×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.225×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.799×** | -5.2 | 9e-05 | 20/45 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tomivosertib (drug)]] 5 µM |  | 0.701× | -3.1 | 0.51 | 5/45 (SNU-1, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5958. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +9.7) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 5 µM 0.229× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[HEC-1-A (line)]] | alt | 26.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LS 180 (line)]] | wt | 22.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.41× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +10.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.63× (z +8.8) | — |
| [[A549 (line)]] | wt | 16.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +10.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[Hs 766T (line)]] | wt | 18.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[KATO III (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[NCI-H2030 (line)]] | alt | 7.21 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.150× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[NCI-H23 (line)]] | alt | 7.82 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 17.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.06× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -12.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 18.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +10.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW480 (line)]] | alt | 20.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.82× (z +9.0) | — |
| [[A-427 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5958), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSTF2T]] | +0.70 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[MRPL47]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[ZKSCAN2]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[ZNF780A]] | +0.67 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[BBS10]] | +0.66 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[EID1]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[PABIR1]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ASF1A]] | +0.60 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[KLHL9]] | +0.60 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[ZNF510]] | +0.60 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[CEP41]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ZNF260]] | +0.60 | +0.60 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAP1L1]] | -0.58 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[PMS2P4-1]] | -0.58 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[LONRF1]] | -0.56 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[CD247]] | -0.55 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[KCTD7]] | -0.55 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[TMEM50B]] | -0.55 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[SNHG1]] | -0.54 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[KDELR1]] | -0.54 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[RPS4X]] | -0.53 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[SOS1]] | -0.53 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[RPL13A]] | -0.53 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[SMG1P5]] | -0.52 | -0.58 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANAPC1P4]] | C | ANAPC1P4 activity raises RANBP6's level | lines that do not express ANAPC1P4 (4) vs lines expressing it (46) | 1.88× lower at baseline in the lines without ANAPC1P4 | 0.034 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP19, MIR4435-2HG, MSX1; maybe low, not absent |
| [[CEP41]] | C | CEP41 activity raises RANBP6's level | lines that do not express CEP41 (4) vs lines expressing it (46) | 1.15× lower at baseline in the lines without CEP41 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LRRIQ3, LINC02175, WDR35; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.681). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.5, 14.9); signed map (0.4, -30.3). **Vector** length 80.2, 15.3% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +9.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +11.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.3 | +11.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +7.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +2.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.0 | +3.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.4 | -5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.4 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +1.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.6 | -0.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | RAN binding protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.1 — chr9:6,011,025-6,015,625 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O60518](https://www.uniprot.org/uniprotkb/O60518) (Ran-binding protein 6):

> May function in nuclear protein import as nuclear transport receptor.

**Summary**, from NCBI Gene [26953](https://www.ncbi.nlm.nih.gov/gene/26953):

> Predicted to enable nuclear import signal receptor activity and nuclear localization sequence binding activity. Predicted to be involved in protein import into nucleus. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9851](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9851) · Entrez [26953](https://www.ncbi.nlm.nih.gov/gene/26953) · UniProt [O60518](https://www.uniprot.org/uniprotkb/O60518) · Ensembl [ENSG00000137040](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137040)

## Data

Gene col 5958: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5958); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5958, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5958]; `tensor/DDL_lfc|DDL_z.npy` [5958]; `embed/gene_vectors.npy` [5958]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5958 or target_col == 5958). Every well: [[RANBP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RANBP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
