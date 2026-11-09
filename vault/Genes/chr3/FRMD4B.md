---
symbol: "FRMD4B"
type: "gene"
col: 3563
ensembl_id: "ENSG00000114541"
name: "FERM domain containing 4B"
location: "3p14.1"
module: 8
arm: "+"
pooled_cpm: 42.45
n_lines_expressing: 30
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 55
direction_downstream: 66
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# FRMD4B

*FERM domain containing 4B* — 3p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.71× (z +11.7, q 9e-29, up in 21 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.623× (z -7.3, q 2e-10, down in 21 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM47]] (+0.70, fdr 7e-06), [[ELF3]] (+0.65, fdr 7e-06), [[FRK]] (+0.63, fdr 1e-05); moves opposite to [[SEC14L1]] (-0.47, fdr 4e-05), [[HSF1]] (-0.47, fdr 8e-05), [[CCM2]] (-0.46, fdr 2e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 55 arrows point to it, the strongest [[EFNA1]] → it (grade B ⚠); 66 go from it, the strongest it → [[ATP1B1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3563.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.71×** | +11.7 | 9e-29 | 21/28 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +8.9 | 1e-16 | 17/28 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +4.6 | 8e-04 | 12/29 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +4.5 | 1e-03 | 15/28 (HEC-1-A, AsPC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.019 | 12/29 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.023 | 16/28 (HEC-1-A, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3563.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.623×** | -7.3 | 2e-10 | 21/28 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.661×** | -6.4 | 5e-08 | 14/28 (NCI-H460, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -5.1 | 8e-05 | 3/29 (HCT15, SW 900, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.726×** | -4.9 | 1e-04 | 18/28 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -4.6 | 5e-04 | 18/28 (HT-29, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.815×** | -4.5 | 8e-04 | 15/29 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.734×** | -4.4 | 9e-04 | 19/26 (HEC-1-A, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.760×** | -4.2 | 0.002 | 11/28 (A549, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.768×** | -4.1 | 0.003 | 15/28 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.766×** | -3.9 | 0.005 | 11/28 (C32, A549, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.781×** | -3.8 | 0.008 | 7/28 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.806×** | -3.3 | 0.042 | 8/28 (A498, HEC-1-A, …) | top dose only |  |
| [[vincristine (drug)]] 0.05 µM |  | **0.796×** | -3.3 | 0.042 | 6/28 (HT-29, KATO III, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.821×** | -3.0 | 0.098 | 10/29 (HT-29, AsPC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.812×** | -3.0 | 0.098 | 2/28 (HCT15, BT-474) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3563. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 161 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -21.7) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.127× (z -14.0) |
| [[NCI-H1573 (line)]] | alt | 191 | 1 (1 ⚠) | 9 (7 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.27× (z +10.1) ⚠ cell-cycle shift, explains ~26% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -18.1) ⚠ cell-cycle shift, explains <1% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.442× (z -9.9) |
| [[A498 (line)]] | wt | 52.8 | 4 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.62× (z +16.2) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.39× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -12.2) ⚠ cell-cycle shift, explains <1% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.364× (z -8.6) |
| [[C32 (line)]] | wt | 101 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -19.4) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.206× (z -10.5) |
| [[Hs 766T (line)]] | wt | 132 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -12.0) ⚠ cell-cycle shift, explains <1% of this change |
| [[HT-29 (line)]] | alt | 90.0 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -16.2) ⚠ cell-cycle shift, explains <1% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.192× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 41.2 | 1 | 2 (1 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.57× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.328× (z -10.6) |
| [[KATO III (line)]] | alt | 52.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 67.2 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.180× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 127 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -15.0) ⚠ cell-cycle shift, explains <1% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.194× (z -14.1) |
| [[AsPC-1 (line)]] | alt | 34.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +11.1) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[CFPAC-1 (line)]] | alt | 84.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.2) ⚠ cell-cycle shift, explains ~62% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[A549 (line)]] | wt | 43.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.337× (z -9.4) ⚠ cell-cycle shift, explains ~66% of this change |
| [[BT-474 (line)]] | alt | 28.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +8.5) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[COLO 205 (line)]] | alt | 87.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -13.6) ⚠ cell-cycle shift, explains <1% of this change |
| [[LoVo (line)]] | wt | 28.3 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 4.07× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 42.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.293× (z -9.1) |
| [[A-172 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.57 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.27 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.86 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.84 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.87 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.92 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.24 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.20 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.34 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.82 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.56 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.44 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 20.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3563), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM47]] | +0.70 | +0.65 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ELF3]] | +0.65 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[FRK]] | +0.63 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[HHLA2]] | +0.63 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[TRIM31]] | +0.61 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[NEDD9]] | +0.61 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[DAPP1]] | +0.58 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ATP1B1]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[LNX1]] | +0.58 | +0.36 / +0.67 | both halves | 9e-05 |  |
| [[SLC6A7]] | +0.58 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[WDR72]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[RHOV]] | +0.57 | +0.51 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC14L1]] | -0.47 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[HSF1]] | -0.47 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[CCM2]] | -0.46 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[LY6G5B]] | -0.46 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[MROH1]] | -0.46 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[CUL4A]] | -0.45 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[BCL7C]] | -0.45 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[SRR]] | -0.45 | -0.32 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*55 arrows, 55 of them with an alert ⚠; grade A 0, B 16, C 39. Shown: the 12 strongest; 43 more arrows (43 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFNA1]] | B | EFNA1 activity raises FRMD4B's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 3.05× lower at baseline in the lines without EFNA1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[BARX2]] | B | BARX2 activity raises FRMD4B's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 3.16× lower at baseline in the lines without BARX2 | 0.014 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[MMP7]] | B | MMP7 activity raises FRMD4B's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 3.68× lower at baseline in the lines without MMP7 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[MAP2K1]] | B | MAP2K1 activity lowers FRMD4B's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[RNF183]] | B | RNF183 activity raises FRMD4B's level | lines that do not express RNF183 (36) vs lines expressing it (14) | 2.31× lower at baseline in the lines without RNF183 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, LINC02964, VIL1 |
| [[FAAH2]] | B | FAAH2 activity raises FRMD4B's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.60× lower at baseline in the lines without FAAH2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[ATP1B1]] | B | ATP1B1 activity raises FRMD4B's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 3.99× lower at baseline in the lines without ATP1B1 | 0.034 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[XDH]] | B | XDH activity raises FRMD4B's level | lines that do not express XDH (22) vs lines expressing it (28) | 2.64× lower at baseline in the lines without XDH | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564 |
| [[CHN2]] | B | CHN2 activity raises FRMD4B's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 2.29× lower at baseline in the lines without CHN2 | 0.049 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[CX3CL1]] | B | CX3CL1 activity raises FRMD4B's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 2.03× lower at baseline in the lines without CX3CL1 | 0.055 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[AGR3]] | B | AGR3 activity raises FRMD4B's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 3.50× lower at baseline in the lines without AGR3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[BMP2]] | B | BMP2 activity raises FRMD4B's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without BMP2 | 0.066 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |

### Downstream of this gene

*66 arrows, 66 of them with an alert ⚠; grade A 0, B 29, C 37. Shown: the 12 strongest; 54 more arrows (54 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP1B1]] | B | FRMD4B activity raises ATP1B1's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 3.72× lower at baseline in the lines without FRMD4B | 4e-04 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[EFNA1]] | B | FRMD4B activity raises EFNA1's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 2.83× lower at baseline in the lines without FRMD4B | 0.003 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[RND1]] | B | FRMD4B activity raises RND1's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 2.39× lower at baseline in the lines without FRMD4B | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[RASGEF1B]] | B | FRMD4B activity raises RASGEF1B's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 2.35× lower at baseline in the lines without FRMD4B | 0.006 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[LNX1]] | B | FRMD4B activity raises LNX1's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 3.56× lower at baseline in the lines without FRMD4B | 0.009 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[BCL7C]] | B | FRMD4B activity lowers BCL7C's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 1.43× higher at baseline in the lines without FRMD4B | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[TNFRSF21]] | B | FRMD4B activity raises TNFRSF21's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 2.88× lower at baseline in the lines without FRMD4B | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[PCSK5]] | B | FRMD4B activity raises PCSK5's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 3.12× lower at baseline in the lines without FRMD4B | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[RHOU]] | B | FRMD4B activity raises RHOU's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 1.80× lower at baseline in the lines without FRMD4B | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[CHN2]] | B | FRMD4B activity raises CHN2's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 3.06× lower at baseline in the lines without FRMD4B | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[MAP3K8]] | B | FRMD4B activity raises MAP3K8's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 1.91× lower at baseline in the lines without FRMD4B | 0.020 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[BARX2]] | B | FRMD4B activity raises BARX2's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 2.70× lower at baseline in the lines without FRMD4B | 0.021 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.575). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.0, 54.2); signed map (58.7, 3.2). **Vector** length 99.2, 29.7% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +11.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | +0.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +2.9 | +1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.6 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +3.7 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.1 | +1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.4 | -7.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -4.5 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -2.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -5.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.3 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | FERM domain containing 4B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.1 — chr3:69,168,782-69,542,583 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1013, GRSP1 |
| Gene groups (HGNC) | FERM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2L6](https://www.uniprot.org/uniprotkb/Q9Y2L6) (FERM domain-containing protein 4B):

> Member of GRP1 signaling complexes that are acutely recruited to plasma membrane ruffles in response to insulin receptor signaling. May function as a scaffolding protein that regulates epithelial cell polarity by connecting ARF6 activation with the PAR3 complex. Plays a redundant role with FRMD4A in epithelial polarization.

**Summary**, from NCBI Gene [23150](https://www.ncbi.nlm.nih.gov/gene/23150):

> This gene encodes a GRP1-binding protein which contains a FERM protein interaction domain as well as two coiled coil domains. This protein may play a role as a scaffolding protein. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:24886](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24886) · Entrez [23150](https://www.ncbi.nlm.nih.gov/gene/23150) · UniProt [Q9Y2L6](https://www.uniprot.org/uniprotkb/Q9Y2L6) · Ensembl [ENSG00000114541](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114541)

## Data

Gene col 3563: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3563); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3563, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3563]; `tensor/DDL_lfc|DDL_z.npy` [3563]; `embed/gene_vectors.npy` [3563]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3563 or target_col == 3563). Every well: [[FRMD4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRMD4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
