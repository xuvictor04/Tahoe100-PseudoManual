---
symbol: "BCL2A1"
type: "gene"
col: 6397
ensembl_id: "ENSG00000140379"
name: "BCL2 related protein A1"
location: "15q25.1"
module: 81
arm: "+"
pooled_cpm: 9.7
n_lines_expressing: 24
n_dd_up: 17
n_dd_down: 33
n_dd_up_clean: 9
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 7
direction_downstream: 43
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# BCL2A1

*BCL2 related protein A1* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +5.7, q 5e-06, up in 2 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (2 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 0.423× (z -6.4, q 8e-08, down in 15 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM158]] (+0.77, fdr 7e-06), [[STC1]] (+0.76, fdr 7e-06), [[MAST4]] (+0.74, fdr 7e-06); moves opposite to [[TMTC1]] (-0.58, fdr 1e-05), [[MGST1]] (-0.54, fdr 2e-05), [[LARP1]] (-0.53, fdr 3e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[FRMD6]] → it (grade B ⚠); 43 go from it, the strongest it → [[CORO2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6397.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +5.7 | 5e-06 | 2/19 (NCI-H1792, HS-578T) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.29×** | +5.5 | 5e-06 | 14/19 (C32, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +5.5 | 5e-06 | 3/13 (A549, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.09×** | +5.5 | 5e-06 | 16/20 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~15% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.07×** | +5.4 | 6e-06 | 4/19 (SK-MEL-2, HS-578T, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +5.4 | 8e-06 | 13/20 (HS-578T, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.85×** | +4.6 | 4e-04 | 1/16 (PANC-1) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.79×** | +4.3 | 0.001 | 8/20 (SK-MEL-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.76×** | +4.0 | 0.003 | 0/12 | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.78×** | +4.0 | 0.004 | 11/19 (A549, PANC-1, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.71×** | +3.9 | 0.006 | 11/19 (PANC-1, hTERT-HPNE, …) | all doses, flat | composition shift; position effect removed |
| [[TAK-901 (drug)]] 0.5 µM |  | **2.12×** | +3.7 | 0.010 | 4/20 (HOP62, C32, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.5 | 0.021 | 7/17 (NCI-H2030, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **1.56×** | +3.3 | 0.039 | 0/14 | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.37×** | +3.3 | 0.039 | 4/10 (LOX-IMVI, A549, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.069 | 6/20 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.87×** | +3.1 | 0.070 | 6/19 (NCI-H1792, PANC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 3 with an alert ⚠; shown: the 15 strongest. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6397.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.423×** | -6.4 | 8e-08 | 15/20 (H4, A549, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.547×** | -6.2 | 1e-07 | 17/20 (RKO, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.453×** | -6.2 | 1e-07 | 18/20 (RKO, HOP62, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.445×** | -6.0 | 2e-07 | 17/20 (A549, NCI-H2030, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.460×** | -5.8 | 8e-07 | 14/20 (H4, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.469×** | -5.7 | 2e-06 | 13/20 (H4, NCI-H2030, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.460×** | -5.4 | 7e-06 | 14/19 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.502×** | -5.1 | 2e-05 | 11/20 (H4, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.477×** | -5.1 | 2e-05 | 15/20 (RKO, NCI-H1792, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.584×** | -4.9 | 6e-05 | 13/20 (RKO, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.586×** | -4.9 | 6e-05 | 16/20 (RKO, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.518×** | -4.7 | 1e-04 | 14/19 (RKO, A-427, …) | rises with dose | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.539×** | -4.6 | 2e-04 | 16/20 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.647×** | -4.6 | 2e-04 | 14/20 (H4, A549, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.552×** | -4.4 | 4e-04 | 14/20 (H4, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6397. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 52.9 | 0 | 12 | — | [[Cobimetinib (drug)]] 5 µM 0.0444× (z -15.5) |
| [[H4 (line)]] | wt | 13.1 | 0 | 5 (1 ⚠) | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0208× (z -11.4) |
| [[HOP62 (line)]] | alt | 10.7 | 0 | 4 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.341× (z -15.2) ⚠ position not correctable · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0465× (z -12.3) |
| [[C32 (line)]] | wt | 43.9 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 26.2× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -10.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -10.1) |
| [[A-427 (line)]] | wt | 12.6 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.0307× (z -14.6) |
| [[A549 (line)]] | wt | 70.4 | 0 | 2 (1 ⚠) | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.251× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 52.6 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -9.0) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.218× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 39.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 8.89 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.499× (z -9.1) ⚠ position not correctable · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0924× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 20.7 | 0 | 2 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.308× (z -16.4) ⚠ position not correctable |
| [[hTERT-HPNE (line)]] | wt | 14.5 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0763× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 2.99 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.336× (z -9.6) ⚠ position not correctable |
| [[NCI-H2347 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0902× (z -16.6) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 14.7 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 8.31× (z +10.7) | — |
| [[A-172 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.943 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.999 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.953 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.901 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.920 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.886 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.879 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6397), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM158]] | +0.77 | +0.70 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[STC1]] | +0.76 | +0.76 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[MAST4]] | +0.74 | +0.76 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[PKIA]] | +0.72 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[PLAUR]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ANTXR2]] | +0.69 | +0.70 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[LRRC8C]] | +0.69 | +0.65 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[TFPI2]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SHANK1]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[CD274]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[EHD1]] | +0.66 | +0.69 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[MARCHF4]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMTC1]] | -0.58 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[MGST1]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[LARP1]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMD6]] | B | FRMD6 activity raises BCL2A1's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 3.40× lower at baseline in the lines without FRMD6 | 0.039 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers BCL2A1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.0% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds |
| [[CTSL]] | B | CTSL activity raises BCL2A1's level | lines that do not express CTSL (9) vs lines expressing it (41) | 3.19× lower at baseline in the lines without CTSL | 0.097 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000286964, FRMD6, SYDE1; maybe low, not absent |
| [[TMEM156]] | C | TMEM156 activity raises BCL2A1's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 3.12× lower at baseline in the lines without TMEM156 | 0.003 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4; co-absent with the target |
| [[PTGS2]] | C | PTGS2 activity raises BCL2A1's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.90× lower at baseline in the lines without PTGS2 | 0.039 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4; co-absent with the target |
| [[G0S2]] | C | G0S2 activity raises BCL2A1's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 1.89× lower at baseline in the lines without G0S2 | 0.079 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD; co-absent with the target |
| [[ARHGAP22]] | C | ARHGAP22 activity raises BCL2A1's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 2.98× lower at baseline in the lines without ARHGAP22 | 0.097 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2; co-absent with the target |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 30, C 13. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CORO2B]] | B | BCL2A1 activity raises CORO2B's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.04× lower at baseline in the lines without BCL2A1 | 0.004 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[SMTN]] | B | BCL2A1 activity raises SMTN's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 1.89× lower at baseline in the lines without BCL2A1 | 0.005 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[CSGALNACT2]] | B | BCL2A1 activity raises CSGALNACT2's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 1.61× lower at baseline in the lines without BCL2A1 | 0.008 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[LRRC8C]] | B | BCL2A1 activity raises LRRC8C's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.42× lower at baseline in the lines without BCL2A1 | 0.010 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[PIK3CD]] | B | BCL2A1 activity raises PIK3CD's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.34× lower at baseline in the lines without BCL2A1 | 0.012 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[NGRN]] | B | BCL2A1 activity raises NGRN's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 1.44× lower at baseline in the lines without BCL2A1 | 0.013 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[RPSAP52]] | B | BCL2A1 activity raises RPSAP52's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.92× lower at baseline in the lines without BCL2A1 | 0.016 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[CSNK1E]] | B | BCL2A1 activity raises CSNK1E's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 1.62× lower at baseline in the lines without BCL2A1 | 0.017 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[LINC02454]] | B | BCL2A1 activity raises LINC02454's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.47× lower at baseline in the lines without BCL2A1 | 0.019 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[ARHGAP31]] | B | BCL2A1 activity raises ARHGAP31's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.60× lower at baseline in the lines without BCL2A1 | 0.022 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[SEMA7A]] | B | BCL2A1 activity raises SEMA7A's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.02× lower at baseline in the lines without BCL2A1 | 0.024 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[ZNF697]] | B | BCL2A1 activity raises ZNF697's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 1.99× lower at baseline in the lines without BCL2A1 | 0.026 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.785). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.1, 3.7); signed map (3.5, 47.7). **Vector** length 92.1, 30.2% of its response variance represented; |z| ≥ 3 in 838 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *KRAS signaling up* (hallmark, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.4 | +5.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.2 | +5.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +2.1 | +3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.8 | +1.9 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.6 | -6.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.3 | -6.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.3 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -5.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.1 | -4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 related protein A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:79,960,892-79,971,196 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GRS, BFL1, BCL2L5, ACC-1, ACC-2, ACC2, ACC1; previously HBPA1 |
| Gene groups (HGNC) | Minor histocompatibility antigens; BCL2 family |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 7 pathways, smallest: Regulation of MITF-M-dependent genes involved in apoptosis; Nuclear events stimulated by ALK signaling in cancer; Signaling by ALK fusions and activated point mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16548](https://www.uniprot.org/uniprotkb/Q16548) (Bcl-2-related protein A1):

> Retards apoptosis induced by IL-3 deprivation. May function in the response of hemopoietic cells to external signals and in maintaining endothelial survival during infection (By similarity). Can inhibit apoptosis induced by serum starvation in the mammary epithelial cell line HC11 (By similarity).

**Summary**, from NCBI Gene [597](https://www.ncbi.nlm.nih.gov/gene/597):

> This gene encodes a member of the BCL-2 protein family. The proteins of this family form hetero- or homodimers and act as anti- and pro-apoptotic regulators that are involved in a wide variety of cellular activities such as embryonic development, homeostasis and tumorigenesis. The protein encoded by this gene is able to reduce the release of pro-apoptotic cytochrome c from mitochondria and block caspase activation. This gene is a direct transcription target of NF-kappa B in response to …

**Accessions** — [HGNC:991](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:991) · Entrez [597](https://www.ncbi.nlm.nih.gov/gene/597) · UniProt [Q16548](https://www.uniprot.org/uniprotkb/Q16548) · Ensembl [ENSG00000140379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140379)

## Data

Gene col 6397: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6397); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6397, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6397]; `tensor/DDL_lfc|DDL_z.npy` [6397]; `embed/gene_vectors.npy` [6397]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6397 or target_col == 6397). Every well: [[BCL2A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL2A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
