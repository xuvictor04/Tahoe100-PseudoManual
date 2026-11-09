---
symbol: "RAB39A"
type: "gene"
col: 11020
ensembl_id: "ENSG00000179331"
name: "RAB39A, member RAS oncogene family"
location: "11q22.3"
module: 176
arm: "+"
pooled_cpm: 3.51
n_lines_expressing: 30
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 12
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# RAB39A

*RAB39A, member RAS oncogene family* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.36× (z +16.7, q 0e+00, up in 23 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHRNA5]] (+0.61, fdr 1e-05), [[MBOAT2]] (+0.61, fdr 1e-05), [[SLC8B1]] (+0.60, fdr 3e-05); moves opposite to [[ZNF337-AS1]] (-0.61, fdr 1e-04), [[RC3H2]] (-0.54, fdr 5e-05), [[ZNF862]] (-0.54, fdr 3e-05).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GPX3]] → it (grade B ⚠); 12 go from it, the strongest it → [[GPRIN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11020.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.36×** | +16.7 | 0e+00 | 23/24 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.43×** | +14.8 | 0e+00 | 23/24 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.22×** | +14.3 | 6e-44 | 23/23 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.11×** | +11.3 | 3e-27 | 18/20 (PANC-1, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.96×** | +10.8 | 7e-25 | 21/23 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +9.9 | 4e-21 | 0/10 | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +9.5 | 2e-19 | 1/6 (PANC-1) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.96×** | +9.4 | 3e-19 | 16/24 (SW1417, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +9.2 | 2e-18 | 8/18 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.49×** | +9.0 | 8e-18 | 20/22 (A498, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.64×** | +8.9 | 3e-17 | 1/8 (SW480) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.06×** | +7.2 | 3e-11 | 18/24 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.14×** | +7.1 | 4e-11 | 16/19 (A498, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +7.0 | 1e-10 | 2/14 (SHP-77, LOX-IMVI) | top dose only | cell-cycle shift (explains ~17% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.48×** | +6.4 | 5e-09 | 2/8 (SHP-77, PANC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +5.8 | 3e-07 | 9/21 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.22×** | +5.6 | 6e-07 | 13/23 (A498, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +5.2 | 7e-06 | 8/23 (NCI-H2347, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +4.6 | 1e-04 | 11/16 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +4.5 | 2e-04 | 7/21 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11020.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.913× | -3.4 | 0.19 | 6/24 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | 0.711× | -3.4 | 0.19 | 5/23 (BT-474, SW1417, …) | inconsistent across doses |  |
| [[Finasteride (drug)]] 5 µM |  | 0.712× | -3.3 | 0.22 | 1/22 (NCI-H2030) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11020. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 4.48 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 9.12× (z +10.2) | — |
| [[A498 (line)]] | wt | 4.61 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 10.9× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 43.1 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.81× (z +8.7) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[A-172 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.963 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.569 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.918 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.670 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.761 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.648 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.735 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.548 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.648 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.718 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.576 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.445 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.553 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.471 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.757 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.974 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.573 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11020), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHRNA5]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[MBOAT2]] | +0.61 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SLC8B1]] | +0.60 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[ATP1A3]] | +0.58 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[HSP90AA2P]] | +0.57 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[HPSE]] | +0.57 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[TEX15]] | +0.56 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[RBM11]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[CACYBP]] | +0.56 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[DPF1]] | +0.56 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[TSPAN33]] | +0.56 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[LINC00937]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF337-AS1]] | -0.61 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[RC3H2]] | -0.54 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[ZNF862]] | -0.54 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[ENTPD3-AS1]] | -0.54 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[PSKH1]] | -0.54 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[ANKRD17-DT]] | -0.53 | -0.46 / -0.29 | both halves | 3e-04 |  |
| [[RNF146]] | -0.52 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[CBR4]] | -0.52 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[PPP3CB]] | -0.50 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[ERMARD]] | -0.50 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[CCAR1]] | -0.50 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[ST7L]] | -0.49 | -0.37 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPX3]] | B | GPX3 activity lowers RAB39A's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.33× higher at baseline in the lines without GPX3 | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |
| [[NFASC]] | C | NFASC activity raises RAB39A's level | lines that do not express NFASC (27) vs lines expressing it (23) | 2.35× lower at baseline in the lines without NFASC | 0.003 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A; co-absent with the target |
| [[SDK2]] | C | SDK2 activity raises RAB39A's level | lines that do not express SDK2 (16) vs lines expressing it (34) | 2.18× lower at baseline in the lines without SDK2 | 0.065 | ⚠ within organs, on part of the lines; also absent: NRIP3, ZNF549, MGAT5B; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRIN1]] | B | RAB39A activity raises GPRIN1's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 1.99× lower at baseline in the lines without RAB39A | 0.012 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent |
| [[CACNA2D2]] | B | RAB39A activity raises CACNA2D2's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 1.98× lower at baseline in the lines without RAB39A | 0.022 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent |
| [[CDK18]] | B | RAB39A activity lowers CDK18's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 1.62× higher at baseline in the lines without RAB39A | 0.035 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent |
| [[RNF146]] | B | RAB39A activity raises RNF146's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 1.35× lower at baseline in the lines without RAB39A | 0.068 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent |
| [[ACTR3B]] | B | RAB39A activity raises ACTR3B's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 1.34× lower at baseline in the lines without RAB39A | 0.073 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent |
| [[DPF1]] | B | RAB39A activity strengthens DPF1's drug response | lines that do not express RAB39A (16) vs lines expressing it (26) | the lines without RAB39A respond 0.82× as strongly (z diff +0.97); strongest at Homoharringtonine 5 µM: 1.91x vs 4.30x (z diff +3.3) | 0.088 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CCAR1]] | B | RAB39A activity raises CCAR1's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 1.14× lower at baseline in the lines without RAB39A | 0.088 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent |
| [[DDX59]] | B | RAB39A activity raises DDX59's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 1.27× lower at baseline in the lines without RAB39A | 0.092 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent |
| [[SRRM3]] | C | RAB39A activity raises SRRM3's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 1.99× lower at baseline in the lines without RAB39A | 0.009 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent; co-absent with the target |
| [[SDK2]] | C | RAB39A activity raises SDK2's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 4.22× lower at baseline in the lines without RAB39A | 0.013 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent; co-absent with the target |
| [[NFASC]] | C | RAB39A activity raises NFASC's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 3.32× lower at baseline in the lines without RAB39A | 0.061 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent; co-absent with the target |
| [[ELAVL2]] | C | RAB39A activity raises ELAVL2's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 2.31× lower at baseline in the lines without RAB39A | 0.089 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.517). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.6, 7.3); signed map (-19.4, 30.2). **Vector** length 42.4, 7.91% of its response variance represented; |z| ≥ 3 in 605 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.5 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +9.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.2 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +9.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +9.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +5.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.0 | +3.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.5 | +4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +0.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -1.4 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | RAB39A, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:107,928,448-107,963,482 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RAB39 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 7 pathways, smallest: Intra-Golgi traffic; RAB geranylgeranylation; RAB GEFs exchange GTP for GDP on RABs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14964](https://www.uniprot.org/uniprotkb/Q14964) (Ras-related protein Rab-39A):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB39A regulates autophagosome-lysosome fusion via recruitment of the HOPS endosomal tethering complex onto lysosomes; …

**Summary**, from NCBI Gene [54734](https://www.ncbi.nlm.nih.gov/gene/54734):

> Enables G protein activity. Involved in autophagosome-lysosome fusion; phagosome acidification; and phagosome-lysosome fusion. Located in autolysosome membrane and phagocytic vesicle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16521](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16521) · Entrez [54734](https://www.ncbi.nlm.nih.gov/gene/54734) · UniProt [Q14964](https://www.uniprot.org/uniprotkb/Q14964) · Ensembl [ENSG00000179331](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179331)

## Data

Gene col 11020: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11020); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11020, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11020]; `tensor/DDL_lfc|DDL_z.npy` [11020]; `embed/gene_vectors.npy` [11020]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11020 or target_col == 11020). Every well: [[RAB39A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB39A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
