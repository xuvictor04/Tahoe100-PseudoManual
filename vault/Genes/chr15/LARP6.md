---
symbol: "LARP6"
type: "gene"
col: 9255
ensembl_id: "ENSG00000166173"
name: "La ribonucleoprotein 6, translational regulator"
location: "15q23"
module: 63
arm: "+"
pooled_cpm: 17.27
n_lines_expressing: 42
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# LARP6

*La ribonucleoprotein 6, translational regulator* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 1.42× (z +6.0, q 1e-06, up in 22 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.439× (z -10.1, q 5e-21, down in 31 of 40 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.677× (z -6.8, q 3e-09, down in 21 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H460 0.242×, NCI-H1792 0.347×, LoVo 0.370×, A-172 0.445×); [[Panobinostat (drug)]] 5 µM in 4 lines (A-172 0.193×, LoVo 0.186×, NCI-H1792 0.304×, HS-578T 0.281×; ⚠ cell-cycle shift, explains ~27% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (NCI-H1792 0.218×, LoVo 0.241×, MIA PaCa-2 0.249×; ⚠ cell-cycle shift, explains ~31% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AAK1]] (+0.63, fdr 7e-06), [[CEBPG]] (+0.60, fdr 1e-05), [[TRIB3]] (+0.60, fdr 1e-05); moves opposite to [[ADGRG6]] (-0.49, fdr 3e-05), [[YAP1]] (-0.46, fdr 6e-05), [[NASP]] (-0.45, fdr 1e-04).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SIRLNT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9255.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **1.42×** | +6.0 | 1e-06 | 22/40 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +5.5 | 1e-05 | 18/32 (MIA PaCa-2, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +5.3 | 3e-05 | 22/40 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +4.6 | 5e-04 | 17/30 (SW 900, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +4.4 | 0.001 | 20/40 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +4.4 | 0.001 | 16/37 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.43×** | +4.3 | 0.001 | 16/40 (LoVo, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +4.3 | 0.001 | 23/40 (CFPAC-1, SHP-77, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.1 | 0.002 | 17/38 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.009 | 18/39 (A498, SW480, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.7 | 0.011 | 14/39 (LoVo, C-33 A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.015 | 17/39 (SW 900, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.75×** | +3.6 | 0.016 | 12/40 (H4, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.34×** | +3.5 | 0.017 | 17/39 (SNU-423, SW 900, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.4 | 0.022 | 11/38 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.034 | 15/40 (H4, SHP-77, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.043 | 14/40 (NCI-H460, SNU-1, …) | top dose only | position effect removed |
| [[Neratinib (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.070 | 7/39 (LoVo, NCI-H460, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.075 | 10/39 (H4, SW 900, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.42×** | +3.0 | 0.075 | 12/36 (J82, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +2.9 | 0.084 | 10/40 (LoVo, Hs 766T, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.58×** | +2.9 | 0.097 | 8/40 (LoVo, A498, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9255.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H460 0.242×, NCI-H1792 0.347×, LoVo 0.370×, A-172 0.445×); [[Panobinostat (drug)]] 5 µM in 4 lines (A-172 0.193×, LoVo 0.186×, NCI-H1792 0.304×, HS-578T 0.281×; ⚠ cell-cycle shift, explains ~27% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (NCI-H1792 0.218×, LoVo 0.241×, MIA PaCa-2 0.249×; ⚠ cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.439×** | -10.1 | 5e-21 | 31/40 (A-172, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.545×** | -7.4 | 3e-11 | 27/40 (NCI-H1792, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.677×** | -6.8 | 3e-09 | 21/39 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.582×** | -6.6 | 5e-09 | 25/40 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.698×** | -4.2 | 0.002 | 17/38 (A498, A-172, …) | top dose only | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.743×** | -3.6 | 0.025 | 14/40 (RPMI-7951, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.769×** | -3.2 | 0.098 | 13/40 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.765× | -3.1 | 0.13 | 10/39 (NCI-H2347, A-172, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9255. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 36.4 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -11.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.347× (z -11.0) |
| [[A-172 (line)]] | wt | 41.5 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.193× (z -13.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.445× (z -9.1) |
| [[LoVo (line)]] | wt | 30.9 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -12.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.370× (z -10.8) |
| [[HS-578T (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -8.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.249× (z -9.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -14.0) |
| [[A-427 (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 11.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9255), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AAK1]] | +0.63 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[CEBPG]] | +0.60 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[TRIB3]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CLGN]] | +0.60 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[GARS1]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[LINC00662]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[SESN2]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SLC35D2]] | +0.57 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[NIBAN1]] | +0.57 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[ADM2]] | +0.56 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[ARHGEF2]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SARS1]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRG6]] | -0.49 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[YAP1]] | -0.46 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[NASP]] | -0.45 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[MAML2]] | -0.44 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[TFAM]] | -0.44 | -0.48 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIRLNT]] | B | SIRLNT activity raises LARP6's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 2.66× lower at baseline in the lines without SIRLNT | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[HDAC6]] | B | HDAC6 activity raises LARP6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[POPDC3]] | B | POPDC3 activity raises LARP6's level | lines that do not express POPDC3 (18) vs lines expressing it (32) | 2.28× lower at baseline in the lines without POPDC3 | 0.079 | ⚠ within organs, on part of the lines; also absent: WIPF1, WDR17, BVES-AS1 |
| [[MAP1B]] | B | MAP1B activity raises LARP6's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 2.78× lower at baseline in the lines without MAP1B | 0.088 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL |
| [[SPIRE1]] | C | SPIRE1 activity raises LARP6's level | lines that do not express SPIRE1 (3) vs lines expressing it (47) | 6.22× lower at baseline in the lines without SPIRE1 | 0.014 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23 |
| [[LRRC49]] | C | LRRC49 activity raises LARP6's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 3.38× lower at baseline in the lines without LRRC49 | 0.054 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.591). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.5, 49.2); signed map (-11.9, 24.2). **Vector** length 80.6, 19.4% of its response variance represented; |z| ≥ 3 in 702 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.0 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +5.3 |
|  | [[Artesunate (drug)]] 5 µM |  | +3.6 | +6.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.6 | +4.4 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +3.8 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -0.6 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.8 | -2.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | La ribonucleoprotein 6, translational regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:70,829,130-70,854,157 (-) |
| Ensembl biotype | protein_coding |
| Also known as | acheron, FLJ11196 |
| Gene groups (HGNC) | La ribonucleoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRS8](https://www.uniprot.org/uniprotkb/Q9BRS8) (La-related protein 6):

> Regulates the coordinated translation of type I collagen alpha-1 and alpha-2 mRNAs, CO1A1 and CO1A2. Stabilizes mRNAs through high-affinity binding of a stem-loop structure in their 5' UTR. This regulation requires VIM and MYH10 filaments, and the helicase DHX9.

**Summary**, from NCBI Gene [55323](https://www.ncbi.nlm.nih.gov/gene/55323):

> Enables RNA binding activity and myosin binding activity. Involved in positive regulation of collagen biosynthetic process. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24012](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24012) · Entrez [55323](https://www.ncbi.nlm.nih.gov/gene/55323) · UniProt [Q9BRS8](https://www.uniprot.org/uniprotkb/Q9BRS8) · Ensembl [ENSG00000166173](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166173)

## Data

Gene col 9255: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9255); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9255, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9255]; `tensor/DDL_lfc|DDL_z.npy` [9255]; `embed/gene_vectors.npy` [9255]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9255 or target_col == 9255). Every well: [[LARP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LARP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
