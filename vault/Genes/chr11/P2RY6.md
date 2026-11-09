---
symbol: "P2RY6"
type: "gene"
col: 10143
ensembl_id: "ENSG00000171631"
name: "pyrimidinergic receptor P2Y6"
location: "11q13.4"
module: 155
arm: "+"
pooled_cpm: 6.45
n_lines_expressing: 21
n_dd_up: 10
n_dd_down: 18
n_dd_up_clean: 6
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 6
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# P2RY6

*pyrimidinergic receptor P2Y6* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.05× (z +10.3, q 4e-22, up in 0 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.91× (z +8.8, q 3e-16, up in 11 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.525× (z -6.2, q 3e-07, down in 13 of 19 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGG]] (+0.67, fdr 7e-06), [[FGB]] (+0.61, fdr 7e-06), [[ATAD3C]] (+0.57, fdr 2e-05); moves opposite to [[DUS4L]] (-0.44, fdr 2e-04), [[N4BP2]] (-0.43, fdr 3e-04), [[SLC30A9]] (-0.42, fdr 2e-04).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 6 go from it, the strongest it → [[RHOV]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10143.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.05×** | +10.3 | 4e-22 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.60×** | +9.2 | 2e-17 | 2/16 (NCI-H1573, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.91×** | +8.8 | 3e-16 | 11/19 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +6.6 | 5e-09 | 1/11 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.97×** | +6.5 | 9e-09 | 9/19 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +6.0 | 1e-07 | 3/19 (A549, AsPC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +4.2 | 0.002 | 13/19 (NCI-H2347, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.0 | 0.004 | 0/12 | top dose only | cell-cycle shift (explains ~19% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.70×** | +3.6 | 0.017 | 3/19 (A498, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.088 | 5/19 (A498, HS-578T, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.92× | +3.1 | 0.10 | 0/7 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10143.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.525×** | -6.2 | 3e-07 | 13/19 (BT-474, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.594×** | -5.0 | 2e-04 | 14/19 (Panc 03.27, A498, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.620×** | -4.6 | 8e-04 | 13/19 (BT-474, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.623×** | -4.5 | 8e-04 | 9/19 (A498, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.627×** | -4.5 | 8e-04 | 11/19 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.634×** | -4.4 | 0.001 | 13/17 (A498, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[4EGI-1 (drug)]] 0.5 µM |  | **0.610×** | -3.4 | 0.050 | 2/19 (NCI-H1573, SHP-77) | inconsistent across doses | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.489×** | -3.4 | 0.050 | 5/18 (A498, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.495×** | -3.3 | 0.051 | 9/19 (A498, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.699×** | -3.3 | 0.051 | 4/19 (MIA PaCa-2, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.713×** | -3.3 | 0.053 | 7/19 (BT-474, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.714×** | -3.2 | 0.053 | 14/19 (BT-474, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 5 µM |  | **0.504×** | -3.2 | 0.053 | 4/19 (SHP-77, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.520×** | -3.1 | 0.076 | 6/19 (MIA PaCa-2, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.726×** | -3.1 | 0.076 | 2/19 (BT-474, AN3 CA) | two highest doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.731×** | -3.0 | 0.091 | 7/19 (HepG2/C3A, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.725×** | -3.0 | 0.095 | 12/19 (A498, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10143. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 49.9 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -24.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.176× (z -14.2) |
| [[BT-474 (line)]] | alt | 29.7 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0567× (z -16.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0374× (z -13.3) |
| [[NCI-H2347 (line)]] | alt | 18.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -8.7) |
| [[J82 (line)]] | alt | 3.41 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0539× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 8.54 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0586× (z -9.4) ⚠ unreliable plate only · without an alert: [[5-Azacytidine (drug)]] 5 µM 0.0728× (z -8.6) |
| [[SHP-77 (line)]] | alt | 18.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -9.0) |
| [[AN3 CA (line)]] | alt | 37.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 3.28 | 0 | 1 | — | [[Entrectinib (drug)]] 5 µM 0.0531× (z -8.7) |
| [[HS-578T (line)]] | alt | 29.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 4.49 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0518× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 19.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.153× (z -9.1) |
| [[A-172 (line)]] | wt | 0.823 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.604 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.677 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.923 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.896 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.936 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.752 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.948 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.751 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.771 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.593 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.723 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.961 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.729 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10143), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 12 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGG]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[FGB]] | +0.61 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[ATAD3C]] | +0.57 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[LY6E-DT]] | +0.52 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[SERPINB3]] | +0.52 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[LINC01503]] | +0.51 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[PDGFRL]] | +0.51 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[S100A9]] | +0.51 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[EVL]] | +0.51 | +0.47 / +0.37 | both halves | 8e-05 |  |
| [[P2RY2]] | +0.50 | +0.48 / +0.39 | both halves | 5e-05 | same gene group; pathway: Class A/1 (Rhodopsin-like receptors); STRING 790; ⚠ same locus (22.1 kb, same strand: neighbours can correlate without regulation) |
| [[RHOV]] | +0.49 | +0.22 / +0.59 | both halves | 6e-04 |  |
| [[TRIM34]] | +0.49 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[SERPINB4]] | +0.49 | +0.56 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUS4L]] | -0.44 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[N4BP2]] | -0.43 | -0.28 / -0.35 | both halves | 3e-04 |  |
| [[SLC30A9]] | -0.42 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[MYSM1]] | -0.42 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[IL1RL1]] | -0.40 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[ALG13]] | -0.40 | -0.18 / -0.40 | ⚠ not reproduced | 0.001 |  |
| [[FRMD6-AS2]] | -0.40 | -0.29 / -0.31 | both halves | 2e-04 |  |
| [[KRR1]] | -0.40 | -0.32 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers P2RY6's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[GSDMC]] | C | GSDMC activity raises P2RY6's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 3.15× lower at baseline in the lines without GSDMC | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHOV]] | B | P2RY6 activity raises RHOV's level | lines that do not express P2RY6 (29) vs lines expressing it (21) | 2.52× lower at baseline in the lines without P2RY6 | 0.017 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, FGG |
| [[CORO2A]] | B | P2RY6 activity raises CORO2A's level | lines that do not express P2RY6 (29) vs lines expressing it (21) | 1.35× lower at baseline in the lines without P2RY6 | 0.035 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, FGG |
| [[AQP3]] | B | P2RY6 activity raises AQP3's level | lines that do not express P2RY6 (29) vs lines expressing it (21) | 1.69× lower at baseline in the lines without P2RY6 | 0.048 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, FGG |
| [[ALOX5]] | B | P2RY6 activity raises ALOX5's level | lines that do not express P2RY6 (29) vs lines expressing it (21) | 1.54× lower at baseline in the lines without P2RY6 | 0.090 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, FGG |
| [[P2RY2]] | C | P2RY6 activity raises P2RY2's level | lines that do not express P2RY6 (29) vs lines expressing it (21) | 2.89× lower at baseline in the lines without P2RY6 | 0.002 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, FGG; co-absent with the target |
| [[MMP7]] | C | P2RY6 activity raises MMP7's level | lines that do not express P2RY6 (29) vs lines expressing it (21) | 2.32× lower at baseline in the lines without P2RY6 | 0.085 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, FGG; co-absent with the target |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.1, 48.3); signed map (54.0, 22.5). **Vector** length 53.0, 12.5% of its response variance represented; |z| ≥ 3 in 560 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MyD88 deficiency (TLR2/4)* (reactome, mean cos +0.56 to 4); *IRAK4 deficiency (TLR2/4)* (reactome, mean cos +0.56 to 4); *Regulation of TLR by endogenous ligand* (reactome, mean cos +0.56 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +6.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.5 | +4.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +2.9 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.6 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.1 | +1.7 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -5.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -4.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.9 | -4.6 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.8 | -1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | pyrimidinergic receptor P2Y6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:73,264,498-73,305,103 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P2Y6 |
| Gene groups (HGNC) | P2Y receptors |
| Reactome | 7 pathways, smallest: P2Y receptors; Nucleotide-like (purinergic) receptors; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15077](https://www.uniprot.org/uniprotkb/Q15077) (P2Y purinoceptor 6):

> Receptor for extracellular UDP > UTP > ATP. The activity of this receptor is mediated by G proteins which activate a phosphatidylinositol-calcium second messenger system.

**Summary**, from NCBI Gene [5031](https://www.ncbi.nlm.nih.gov/gene/5031):

> The product of this gene belongs to the family of P2 receptors, which is activated by extracellular nucleotides and subdivided into P2X ligand-gated ion channels and P2Y G-protein coupled receptors. This family has several receptor subtypes with different pharmacological selectivity, which overlaps in some cases, for various adenosine and uridine nucleotides. This receptor, which is a G-protein coupled receptor, is responsive to UDP, partially responsive to UTP and ADP, and not responsive to …

**Accessions** — [HGNC:8543](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8543) · Entrez [5031](https://www.ncbi.nlm.nih.gov/gene/5031) · UniProt [Q15077](https://www.uniprot.org/uniprotkb/Q15077) · Ensembl [ENSG00000171631](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171631)

## Data

Gene col 10143: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10143); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10143, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10143]; `tensor/DDL_lfc|DDL_z.npy` [10143]; `embed/gene_vectors.npy` [10143]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10143 or target_col == 10143). Every well: [[P2RY6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/P2RY6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
