---
symbol: "KDM7A-DT"
type: "gene"
col: 15269
ensembl_id: "ENSG00000260231"
name: "KDM7A divergent transcript"
location: "7q34"
module: 101
arm: "+"
pooled_cpm: 5.3
n_lines_expressing: 46
n_dd_up: 19
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# KDM7A-DT

*KDM7A divergent transcript* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 4.50× (z +14.6, q 1e-45, up in 15 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.95× (z +9.9, q 7e-21, up in 18 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.485× (z -7.2, q 5e-10, down in 21 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM7A]] (+0.68, fdr 7e-06, ⚠ same locus), [[HCG20]] (+0.66, fdr 7e-06), [[NOP14-AS1]] (+0.65, fdr 7e-06), [[LIF]] (+0.61, fdr 1e-05); moves opposite to [[GPX8]] (-0.55, fdr 1e-05), [[INTS10]] (-0.54, fdr 1e-05), [[ANAPC10]] (-0.50, fdr 3e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); 6 go from it, the strongest it → [[KDM7A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15269.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.50×** | +14.6 | 1e-45 | 15/16 (HS-578T, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.11×** | +11.9 | 3e-30 | 16/24 (NCI-H460, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +9.9 | 7e-21 | 18/36 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +8.7 | 6e-16 | 5/9 (HS-578T, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +6.8 | 9e-10 | 21/41 (A498, BT-474, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +5.9 | 5e-07 | 17/40 (C32, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.69×** | +5.5 | 2e-06 | 14/40 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +5.5 | 3e-06 | 6/19 (NCI-H1573, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +4.7 | 1e-04 | 8/23 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +4.7 | 2e-04 | 12/41 (A498, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +4.6 | 2e-04 | 16/39 (HS-578T, SW1417, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +4.4 | 5e-04 | 15/41 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.32×** | +4.1 | 0.002 | 11/34 (Hs 766T, SW1417, …) | inconsistent across doses | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.002 | 6/42 (A498, HepG2/C3A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.002 | 7/41 (HS-578T, LS 180, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.47×** | +3.8 | 0.006 | 7/32 (NCI-H460, C32, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.006 | 13/40 (NCI-H460, SHP-77, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +3.6 | 0.009 | 10/40 (NCI-H460, HS-578T, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.013 | 9/30 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15269.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.485×** | -7.2 | 5e-10 | 21/40 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.545×** | -6.4 | 6e-08 | 18/40 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.744×** | -4.4 | 0.002 | 18/41 (HCT15, RKO, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.640×** | -4.3 | 0.002 | 13/41 (SW480, NCI-H1573, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.695×** | -3.8 | 0.017 | 13/42 (NCI-H1573, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.713×** | -3.5 | 0.039 | 12/40 (A498, SW480, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.731×** | -3.3 | 0.087 | 8/40 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.725× | -3.2 | 0.11 | 9/40 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15269. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 8.05 | 0 | 3 | — | [[Bortezomib (drug)]] 0.05 µM 0.189× (z -9.6) |
| [[BT-474 (line)]] | alt | 19.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.140× (z -8.6) |
| [[HS-578T (line)]] | alt | 8.46 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 26.7× (z +12.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 10.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 5.34× (z +8.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.0780× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 4.45 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.4× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 2.39 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0459× (z -9.9) |
| [[Hs 766T (line)]] | wt | 9.27 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +9.1) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[KATO III (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.143× (z -9.1) ⚠ toxic |
| [[SW1417 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.738 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.821 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15269), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM7A]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 | ⚠ same locus (0.2 kb: neighbours can correlate without regulation) |
| [[HCG20]] | +0.66 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[NOP14-AS1]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[LIF]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[IER3]] | +0.60 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[IL1A]] | +0.59 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[EHD1]] | +0.59 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[CSRNP1]] | +0.59 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ITGA2-AS1]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[CXCL8]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[EPHA2]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SHB]] | +0.57 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[HOMER1]] | +0.56 | +0.56 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPX8]] | -0.55 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[INTS10]] | -0.54 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ANAPC10]] | -0.50 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[RUFY2]] | -0.48 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[CDC23]] | -0.48 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[PHKB]] | -0.48 | -0.43 / -0.55 | both halves | 4e-05 |  |
| [[NUP85]] | -0.47 | -0.46 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises KDM7A-DT's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SHH]] | B | SHH activity raises KDM7A-DT's level | lines that do not express SHH (29) vs lines expressing it (21) | 1.42× lower at baseline in the lines without SHH | 0.094 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[TOP2A]] | B | TOP2A activity lowers KDM7A-DT's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KDM7A]] | C | KDM7A-DT activity raises KDM7A's level | lines that do not express KDM7A-DT (4) vs lines expressing it (46) | 2.32× lower at baseline in the lines without KDM7A-DT | 0.028 | ⚠ few lines (4 vs 46); across organs; also absent: FBXO6, MCF2L2, KIAA1522; maybe low, not absent |
| [[KDM7A]] | C | KDM7A-DT activity strengthens KDM7A's drug response | lines that do not express KDM7A-DT (3) vs lines expressing it (45) | the lines without KDM7A-DT respond 0.41× as strongly (z diff +3.28); strongest at Dinaciclib 0.5 µM: 0.68x vs 0.37x (z diff +5.0) | 0.047 | ⚠ few lines (4 vs 46); across organs; also absent: FBXO6, MCF2L2, KIAA1522; maybe low, not absent; target measured in part of the lines; artifact flags |
| cells under [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM | C | KDM7A-DT activity raises the cells' numbers under Fedratinib (hydrochloride hydrate) 5 µM (protects the cells) | lines that do not express KDM7A-DT (4) vs lines expressing it (44) | the lines without KDM7A-DT: 0.71× the cells of the other lines | 0.048 | ⚠ few lines (4 vs 46); across organs; also absent: FBXO6, MCF2L2, KIAA1522; maybe low, not absent |
| [[SOWAHC]] | C | KDM7A-DT activity raises SOWAHC's level | lines that do not express KDM7A-DT (4) vs lines expressing it (46) | 2.25× lower at baseline in the lines without KDM7A-DT | 0.055 | ⚠ few lines (4 vs 46); across organs; also absent: FBXO6, MCF2L2, KIAA1522; maybe low, not absent; co-absent with the target |
| cells under [[SBI-0640756 (drug)]] 5 µM | C | KDM7A-DT activity lowers the cells' numbers under SBI-0640756 5 µM (makes them more sensitive) | lines that do not express KDM7A-DT (4) vs lines expressing it (44) | the lines without KDM7A-DT: 1.36× the cells of the other lines | 0.057 | ⚠ few lines (4 vs 46); across organs; also absent: FBXO6, MCF2L2, KIAA1522; maybe low, not absent |
| cells under [[NG25 (drug)]] 5 µM | C | KDM7A-DT activity raises the cells' numbers under NG25 5 µM (protects the cells) | lines that do not express KDM7A-DT (4) vs lines expressing it (44) | the lines without KDM7A-DT: 0.59× the cells of the other lines | 0.0999 | ⚠ few lines (4 vs 46); across organs; also absent: FBXO6, MCF2L2, KIAA1522; maybe low, not absent |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.663). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.8, -3.7); signed map (3.9, 31.5). **Vector** length 75.5, 14.1% of its response variance represented; |z| ≥ 3 in 934 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +14.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +5.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +1.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.1 | -6.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.7 | -7.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -3.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | KDM7A divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q34 — chr7:140,177,184-140,179,640 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously JHDM1D-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48959](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48959) · Entrez [100134229](https://www.ncbi.nlm.nih.gov/gene/100134229) · Ensembl [ENSG00000260231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000260231)

## Data

Gene col 15269: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15269); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15269, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15269]; `tensor/DDL_lfc|DDL_z.npy` [15269]; `embed/gene_vectors.npy` [15269]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15269 or target_col == 15269). Every well: [[KDM7A-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDM7A-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
