---
symbol: "FBXO30"
type: "gene"
col: 3994
ensembl_id: "ENSG00000118496"
name: "F-box protein 30"
location: "6q24.3"
module: 135
arm: "+"
pooled_cpm: 26.22
n_lines_expressing: 48
n_dd_up: 25
n_dd_down: 6
n_dd_up_clean: 21
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# FBXO30

*F-box protein 30* — 6q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.24× (z +15.1, q 0e+00, up in 42 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.622× (z -6.1, q 5e-07, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF6]] (+0.76, fdr 1e-05), [[RHBDD3]] (+0.71, fdr 4e-05), [[BAG2]] (+0.71, fdr 1e-05); moves opposite to [[EFHC1]] (-0.67, fdr 1e-05), [[ORC4]] (-0.66, fdr 1e-05), [[SNX1]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SLC17A7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3994.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.24×** | +15.1 | 0e+00 | 42/45 (LoVo, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.25×** | +14.7 | 0e+00 | 42/46 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.08×** | +14.4 | 6e-45 | 44/46 (NCI-H2030, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.69×** | +12.0 | 5e-31 | 43/46 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.55×** | +12.0 | 5e-31 | 41/45 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.24×** | +10.3 | 5e-23 | 42/45 (LoVo, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.10×** | +9.3 | 1e-18 | 43/46 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.12×** | +9.2 | 2e-18 | 41/46 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +9.1 | 6e-18 | 36/46 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.93×** | +8.4 | 3e-15 | 42/45 (SW 900, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +7.0 | 1e-10 | 36/46 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.73×** | +7.0 | 1e-10 | 32/46 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.64×** | +6.4 | 9e-09 | 35/45 (SW 900, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 0.5 µM |  | **1.47×** | +5.0 | 3e-05 | 26/46 (RKO, HCT15, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +4.9 | 3e-05 | 25/41 (HepG2/C3A, A-172, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.43×** | +4.5 | 2e-04 | 25/45 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3994.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.622×** | -6.1 | 5e-07 | 31/46 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.651×** | -5.5 | 8e-06 | 28/46 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.771×** | -4.8 | 4e-04 | 25/46 (SW 1271, HOP62, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.712×** | -4.4 | 0.002 | 22/45 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.724×** | -4.1 | 0.005 | 21/43 (PANC-1, hTERT-HPNE, …) | two highest doses | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.613×** | -3.6 | 0.026 | 19/44 (LS 180, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.783× | -3.2 | 0.12 | 18/45 (HCT15, CHP-212, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.792× | -3.0 | 0.18 | 15/45 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3994. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 28.5 | 9 | 0 | [[Auranofin (drug)]] 5 µM 5.48× (z +15.1) | — |
| [[LoVo (line)]] | wt | 17.4 | 5 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 12.4× (z +18.4) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[HT-29 (line)]] | alt | 17.9 | 5 | 0 | [[Auranofin (drug)]] 5 µM 9.92× (z +13.5) | — |
| [[SNU-423 (line)]] | alt | 37.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 18.1 | 2 | 1 | [[Auranofin (drug)]] 5 µM 9.76× (z +11.0) | [[Thymol (drug)]] 0.5 µM 0.152× (z -9.2) |
| [[HOP62 (line)]] | alt | 24.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +10.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 45.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 32.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +10.6) | — |
| [[NCI-H460 (line)]] | wt | 32.4 | 3 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.98× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 40.5 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.352× (z -9.1) |
| [[A498 (line)]] | wt | 19.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.76× (z +11.6) | — |
| [[A549 (line)]] | wt | 22.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +10.8) | — |
| [[C32 (line)]] | wt | 19.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 8.41× (z +11.9) | — |
| [[HEC-1-A (line)]] | alt | 21.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 14.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.71× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 48.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.99× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 12.6 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.76× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 20.3 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.12× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.157× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[SW1417 (line)]] | alt | 23.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.1) | — |
| [[A-172 (line)]] | wt | 24.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.22× (z +12.4) | — |
| [[AsPC-1 (line)]] | alt | 12.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.3× (z +12.4) | — |
| [[COLO 205 (line)]] | alt | 7.95 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0759× (z -9.0) |
| [[H4 (line)]] | wt | 21.4 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.104× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 28.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.54× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 16.3 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.162× (z -9.9) |
| [[HS-578T (line)]] | alt | 40.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.318× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 39.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 12.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.64× (z +8.6) | — |
| [[RKO (line)]] | wt | 61.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 27.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.30× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 36.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.91× (z +8.9) | — |
| [[A-427 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.40 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3994), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF6]] | +0.76 | +0.72 / +0.57 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[RHBDD3]] | +0.71 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[BAG2]] | +0.71 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[AP5M1]] | +0.69 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[HTATIP2]] | +0.68 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[C17orf80]] | +0.68 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[EIF5]] | +0.66 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[PSMD11]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[AIFM2]] | +0.65 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[YIPF7]] | +0.65 | +0.63 / +0.34 | both halves | 1e-04 |  |
| [[GPATCH2]] | +0.65 | +0.68 / +0.27 | both halves | 3e-04 |  |
| [[PRDM5]] | +0.65 | +0.52 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFHC1]] | -0.67 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[ORC4]] | -0.66 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[SNX1]] | -0.65 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[IFT172]] | -0.65 | -0.59 / -0.38 | both halves | 7e-05 |  |
| [[GMCL1]] | -0.65 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[RAB3A]] | -0.65 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[C1QL1]] | -0.65 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[ARL3]] | -0.64 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[PIBF1]] | -0.63 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[HEATR5B]] | -0.62 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[FHIP1A]] | -0.62 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[RRAS]] | -0.61 | -0.54 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC17A7]] | B | SLC17A7 activity raises FBXO30's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 2.77× lower at baseline in the lines without SLC17A7 | 0.008 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[NUP62CL]] | B | NUP62CL activity lowers FBXO30's level | lines that do not express NUP62CL (19) vs lines expressing it (31) | 1.22× higher at baseline in the lines without NUP62CL | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC01589, ABCC3, GOLT1A |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises FBXO30's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises FBXO30's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **+** arm (projection on the module's main direction 0.812). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-16.5, 10.7); signed map (21.2, -25.1). **Vector** length 108, 29.4% of its response variance represented; |z| ≥ 3 in 1,186 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.5 | +15.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.5 | +12.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.4 | +12.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.2 | +10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +3.7 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -7.3 | -6.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.0 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.0 | -5.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | +0.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -3.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 30 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.3 — chr6:145,793,502-145,814,795 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC21674, Fbx30 |
| Gene groups (HGNC) | F-boxes other; Zinc fingers TRAF-type |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TB52](https://www.uniprot.org/uniprotkb/Q8TB52) (F-box only protein 30):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex. Required for muscle atrophy following denervation.

**Summary**, from NCBI Gene [84085](https://www.ncbi.nlm.nih.gov/gene/84085):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of the ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:15600](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15600) · Entrez [84085](https://www.ncbi.nlm.nih.gov/gene/84085) · UniProt [Q8TB52](https://www.uniprot.org/uniprotkb/Q8TB52) · Ensembl [ENSG00000118496](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118496)

## Data

Gene col 3994: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3994); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3994, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3994]; `tensor/DDL_lfc|DDL_z.npy` [3994]; `embed/gene_vectors.npy` [3994]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3994 or target_col == 3994). Every well: [[FBXO30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
