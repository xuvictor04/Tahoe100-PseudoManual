---
symbol: "PLEKHG4"
type: "gene"
col: 12143
ensembl_id: "ENSG00000196155"
name: "pleckstrin homology and RhoGEF domain containing G4"
location: "16q22.1"
module: 96
arm: "+"
pooled_cpm: 2.51
n_lines_expressing: 39
n_dd_up: 9
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# PLEKHG4

*pleckstrin homology and RhoGEF domain containing G4* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.08× (z +8.9, q 4e-16, up in 2 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.54× (z +5.0, q 9e-05, up in 10 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.377× (z -8.0, q 6e-13, down in 20 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAF1C]] (+0.66, fdr 7e-06), [[FAAP100]] (+0.65, fdr 7e-06), [[ARFRP1]] (+0.65, fdr 1e-05); moves opposite to [[COX8A]] (-0.53, fdr 3e-05), [[ABHD18]] (-0.53, fdr 4e-05), [[SBNO1]] (-0.53, fdr 1e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TMTC2]] → it (grade B ⚠); 5 go from it, the strongest it → [[LEPR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12143.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.08×** | +8.9 | 4e-16 | 2/4 (NCI-H2030, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +5.5 | 8e-06 | 2/6 (NCI-H2030, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +5.0 | 9e-05 | 10/25 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.28×** | +5.0 | 9e-05 | 5/11 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +3.6 | 0.036 | 8/27 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.77×** | +3.3 | 0.071 | 1/20 (LS 180) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.50×** | +3.3 | 0.071 | 7/27 (HT-29, HS-578T, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.074 | 5/27 (SW 900, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.32×** | +3.2 | 0.079 | 3/31 (SW480, NCI-H1792, …) | top dose only | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.70× | +3.1 | 0.10 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.49× | +3.0 | 0.13 | 2/23 (LS 180, SW480) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12143.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.377×** | -8.0 | 6e-13 | 20/35 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.522×** | -5.4 | 2e-05 | 15/32 (LS 180, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.525×** | -5.3 | 2e-05 | 18/29 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.576×** | -4.5 | 8e-04 | 14/35 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.631×** | -3.8 | 0.017 | 13/19 (NCI-H2030, HOP62, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12143. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 3.21 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0396× (z -11.5) |
| [[SW480 (line)]] | alt | 2.15 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0851× (z -8.8) |
| [[A-172 (line)]] | wt | 0.200 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.395 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.203 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.785 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.343 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.284 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.145 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.663 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.337 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.689 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.682 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.904 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12143), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF1C]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[FAAP100]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[ARFRP1]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[NCDN]] | +0.65 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[MYL5]] | +0.61 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[DEDD]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[ZNF783]] ⚠ | +0.58 | +0.57 / +0.55 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SAYSD1]] | +0.58 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[ATXN7L2]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[WIZ]] | +0.58 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[RTL6]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[DMAP1]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[SYNPO]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX8A]] | -0.53 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[ABHD18]] | -0.53 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[SBNO1]] | -0.53 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[TSPO]] | -0.53 | -0.57 / -0.32 | both halves | 1e-04 |  |
| [[HIGD2A]] | -0.52 | -0.58 / -0.40 | both halves | 4e-05 |  |
| [[LEPR]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ATP5PF]] | -0.52 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[PRDX4]] | -0.52 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[GNB2]] | -0.51 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[OST4]] | -0.50 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[DDT]] | -0.50 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[ZNHIT1]] | -0.50 | -0.40 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMTC2]] | B | TMTC2 activity lowers PLEKHG4's level | lines that do not express TMTC2 (6) vs lines expressing it (44) | 1.84× higher at baseline in the lines without TMTC2 | 0.031 | ⚠ within organs, on part of the lines; also absent: RNF125, GPR19; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LEPR]] | B | PLEKHG4 activity raises LEPR's level | lines that do not express PLEKHG4 (11) vs lines expressing it (39) | 1.63× lower at baseline in the lines without PLEKHG4 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC2A12, PPP1R1C, TMEM51-AS1 |
| [[SPICE1]] | B | PLEKHG4 activity raises SPICE1's level | lines that do not express PLEKHG4 (11) vs lines expressing it (39) | 1.36× lower at baseline in the lines without PLEKHG4 | 0.020 | ⚠ within organs, on part of the lines; also absent: SLC2A12, PPP1R1C, TMEM51-AS1 |
| [[CASKIN2]] | B | PLEKHG4 activity lowers CASKIN2's level | lines that do not express PLEKHG4 (11) vs lines expressing it (39) | 1.24× higher at baseline in the lines without PLEKHG4 | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC2A12, PPP1R1C, TMEM51-AS1 |
| [[MEGF8]] | B | PLEKHG4 activity raises MEGF8's level | lines that do not express PLEKHG4 (11) vs lines expressing it (39) | 1.52× lower at baseline in the lines without PLEKHG4 | 0.051 | ⚠ within organs, on part of the lines; also absent: SLC2A12, PPP1R1C, TMEM51-AS1 |
| [[PRR14]] | B | PLEKHG4 activity lowers PRR14's level | lines that do not express PLEKHG4 (11) vs lines expressing it (39) | 1.24× higher at baseline in the lines without PLEKHG4 | 0.082 | ⚠ within organs, on part of the lines; also absent: SLC2A12, PPP1R1C, TMEM51-AS1 |

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-11.8, -25.2); signed map (-8.7, -32.0). **Vector** length 41.7, 6.15% of its response variance represented; |z| ≥ 3 in 641 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +1.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.8 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -8.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.0 | -2.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology and RhoGEF domain containing G4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,277,510-67,289,499 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434I216, ARHGEF44; previously SCA4 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs |
| Reactome | 6 pathways, smallest: RHOA GTPase cycle; CDC42 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q58EX7](https://www.uniprot.org/uniprotkb/Q58EX7) (Puratrophin-1):

> Possible role in intracellular signaling and cytoskeleton dynamics at the Golgi.

**Summary**, from NCBI Gene [25894](https://www.ncbi.nlm.nih.gov/gene/25894):

> The protein encoded by this gene can function as a guanine nucleotide exchange factor (GEF) and may play a role in intracellular signaling and cytoskeleton dynamics at the Golgi apparatus. Polymorphisms in the region of this gene have been found to be associated with spinocerebellar ataxia in some study populations. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2015]

**Accessions** — [HGNC:24501](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24501) · Entrez [25894](https://www.ncbi.nlm.nih.gov/gene/25894) · UniProt [Q58EX7](https://www.uniprot.org/uniprotkb/Q58EX7) · Ensembl [ENSG00000196155](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196155)

## Data

Gene col 12143: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12143); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12143, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12143]; `tensor/DDL_lfc|DDL_z.npy` [12143]; `embed/gene_vectors.npy` [12143]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12143 or target_col == 12143). Every well: [[PLEKHG4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHG4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
