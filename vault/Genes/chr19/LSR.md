---
symbol: "LSR"
type: "gene"
col: 2646
ensembl_id: "ENSG00000105699"
name: "lipolysis stimulated lipoprotein receptor"
location: "19q13.12"
module: 141
arm: "+"
pooled_cpm: 50.08
n_lines_expressing: 31
n_dd_up: 7
n_dd_down: 25
n_dd_up_clean: 5
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 12
direction_downstream: 13
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# LSR

*lipolysis stimulated lipoprotein receptor* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.00× (z +16.4, q 0e+00, up in 28 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (3 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.590× (z -8.5, q 1e-14, down in 22 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGR2]] (+0.65, fdr 7e-06), [[EGR3]] (+0.63, fdr 1e-05), [[PLK3]] (+0.62, fdr 7e-06); moves opposite to [[APIP]] (-0.52, fdr 3e-05), [[QRSL1]] (-0.47, fdr 3e-05), [[VWA8]] (-0.47, fdr 3e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 13 go from it, the strongest it → [[HAP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2646.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +16.4 | 0e+00 | 28/30 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +10.8 | 1e-24 | 20/29 (SW 900, AsPC-1, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.2 | 5e-05 | 19/29 (LS 180, SW48, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +4.4 | 0.002 | 13/29 (PANC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.8 | 0.017 | 9/29 (PANC-1, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.017 | 12/29 (NCI-H2347, A-427, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.24×** | +3.5 | 0.042 | 14/28 (A498, A549, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.22×** | +3.3 | 0.063 | 11/28 (A498, KATO III, …) | inconsistent across doses | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.0 | 0.16 | 0/30 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 4 with an alert ⚠; shown: the 15 strongest. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2646.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.590×** | -8.5 | 1e-14 | 22/28 (HCT15, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.653×** | -7.1 | 3e-10 | 22/28 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.634×** | -7.0 | 4e-10 | 24/29 (SW480, A-427, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.659×** | -7.0 | 5e-10 | 22/29 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.665×** | -6.8 | 1e-09 | 25/30 (NCI-H23, A-427, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.673×** | -6.4 | 2e-08 | 22/29 (A-427, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.709×** | -6.1 | 7e-08 | 20/30 (NCI-H23, A-427, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.703×** | -5.9 | 3e-07 | 20/29 (NCI-H1573, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.721×** | -5.5 | 3e-06 | 21/29 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.708×** | -5.4 | 3e-06 | 18/28 (NCI-H23, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.796×** | -5.3 | 5e-06 | 14/29 (SW480, SW48, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.736×** | -5.1 | 2e-05 | 18/28 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.762×** | -4.5 | 2e-04 | 17/29 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.795×** | -4.5 | 3e-04 | 16/30 (NCI-H23, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.610×** | -4.3 | 6e-04 | 15/28 (SK-MEL-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2646. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 36.4 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +12.5) | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.275× (z -10.3) |
| [[PANC-1 (line)]] | alt | 26.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.16× (z +16.2) | — |
| [[AsPC-1 (line)]] | alt | 66.0 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +15.1) | [[Auranofin (drug)]] 5 µM 0.358× (z -8.9) |
| [[A498 (line)]] | wt | 21.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +13.6) | — |
| [[A549 (line)]] | wt | 12.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.68× (z +14.6) | — |
| [[HepG2_C3A (line)]] | wt | 48.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +9.8) | — |
| [[KATO III (line)]] | alt | 123 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.348× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 27.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +16.2) | — |
| [[C-33 A (line)]] | alt | 36.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 128 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +14.7) | — |
| [[LoVo (line)]] | wt | 61.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 59.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 72.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.306× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 43.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +17.1) | — |
| [[Panc 03.27 (line)]] | alt | 156 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +8.7) | — |
| [[RKO (line)]] | wt | 25.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +12.3) | — |
| [[SK-MEL-2 (line)]] | alt | 48.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.48 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 84.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.30 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.12 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.06 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.55 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 121 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.92 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.54 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.46 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.95 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.65 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.34 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.75 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.94 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 88.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 71.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2646), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGR2]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[EGR3]] | +0.63 | +0.57 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[PLK3]] | +0.62 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[VASP]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[NOP14-AS1]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ASTL]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[BTBD19]] | +0.60 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[HAP1]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[BCL2L12]] | +0.58 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[IRF3]] | +0.56 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[ADAMTSL4-AS2]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[SPRED2]] | +0.55 | +0.41 / +0.61 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APIP]] | -0.52 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[QRSL1]] | -0.47 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[VWA8]] | -0.47 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[VPS36]] | -0.46 | -0.54 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 9, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LSR's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity raises LSR's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[LINC00659]] | B | LINC00659 activity raises LSR's level | lines that do not express LINC00659 (26) vs lines expressing it (24) | 3.06× lower at baseline in the lines without LINC00659 | 0.075 | ⚠ within organs, on part of the lines; also absent: KLK6, TRIM15, ENSG00000225680 |
| [[PDGFB]] | B | PDGFB activity raises LSR's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 2.09× lower at baseline in the lines without PDGFB | 0.078 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[HAP1]] | B | HAP1 activity raises LSR's level | lines that do not express HAP1 (12) vs lines expressing it (38) | 3.04× lower at baseline in the lines without HAP1 | 0.080 | ⚠ within organs, on part of the lines; also absent: HID1, NRARP, PDE9A |
| [[EPHA2]] | B | EPHA2 activity raises LSR's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 4.28× lower at baseline in the lines without EPHA2 | 0.085 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[CRABP2]] | B | CRABP2 activity raises LSR's level | lines that do not express CRABP2 (24) vs lines expressing it (26) | 2.46× lower at baseline in the lines without CRABP2 | 0.088 | ⚠ within organs, on part of the lines; also absent: ESPN, ACP7, HAS2 |
| [[NECTIN1]] | B | NECTIN1 activity raises LSR's level | lines that do not express NECTIN1 (8) vs lines expressing it (42) | 3.86× lower at baseline in the lines without NECTIN1 | 0.089 | ⚠ within organs, on part of the lines; also absent: PRR5; maybe low, not absent |
| [[EPHA2-AS1]] | B | EPHA2-AS1 activity raises LSR's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 4.11× lower at baseline in the lines without EPHA2-AS1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent |
| [[CDC42BPG]] | C | CDC42BPG activity raises LSR's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 5.55× lower at baseline in the lines without CDC42BPG | 0.001 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent; co-absent with the target |
| [[PTAFR]] | C | PTAFR activity raises LSR's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 5.18× lower at baseline in the lines without PTAFR | 0.003 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent; co-absent with the target |
| [[TMC6]] | C | TMC6 activity raises LSR's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 6.67× lower at baseline in the lines without TMC6 | 0.006 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 10, C 3. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HAP1]] | B | LSR activity raises HAP1's level | lines that do not express LSR (19) vs lines expressing it (31) | 2.55× lower at baseline in the lines without LSR | 0.009 | ⚠ within organs, on part of the lines; also absent: ENTPD2, EPHA10, OCLN |
| [[EPHA2]] | B | LSR activity raises EPHA2's level | lines that do not express LSR (19) vs lines expressing it (31) | 3.02× lower at baseline in the lines without LSR | 0.018 | ⚠ within organs, on part of the lines; also absent: ENTPD2, EPHA10, OCLN |
| [[GALE]] | B | LSR activity raises GALE's level | lines that do not express LSR (19) vs lines expressing it (31) | 1.63× lower at baseline in the lines without LSR | 0.019 | ⚠ within organs, on part of the lines; also absent: ENTPD2, EPHA10, OCLN |
| [[IQCD]] | B | LSR activity raises IQCD's level | lines that do not express LSR (19) vs lines expressing it (31) | 1.65× lower at baseline in the lines without LSR | 0.025 | ⚠ within organs, on part of the lines; also absent: ENTPD2, EPHA10, OCLN |
| [[ARHGAP27]] | B | LSR activity raises ARHGAP27's level | lines that do not express LSR (19) vs lines expressing it (31) | 2.37× lower at baseline in the lines without LSR | 0.031 | ⚠ within organs, on part of the lines; also absent: ENTPD2, EPHA10, OCLN |
| [[EPHA2-AS1]] | B | LSR activity raises EPHA2-AS1's level | lines that do not express LSR (19) vs lines expressing it (31) | 2.03× lower at baseline in the lines without LSR | 0.056 | ⚠ within organs, on part of the lines; also absent: ENTPD2, EPHA10, OCLN |
| [[ABHD11]] | B | LSR activity raises ABHD11's level | lines that do not express LSR (19) vs lines expressing it (31) | 2.12× lower at baseline in the lines without LSR | 0.062 | ⚠ within organs, on part of the lines; also absent: ENTPD2, EPHA10, OCLN |
| [[RDH13]] | B | LSR activity raises RDH13's level | lines that do not express LSR (19) vs lines expressing it (31) | 1.71× lower at baseline in the lines without LSR | 0.066 | ⚠ within organs, on part of the lines; also absent: ENTPD2, EPHA10, OCLN |
| [[SLC25A45]] | B | LSR activity raises SLC25A45's level | lines that do not express LSR (19) vs lines expressing it (31) | 1.51× lower at baseline in the lines without LSR | 0.089 | ⚠ within organs, on part of the lines; also absent: ENTPD2, EPHA10, OCLN |
| [[ITPKC]] | B | LSR activity raises ITPKC's level | lines that do not express LSR (19) vs lines expressing it (31) | 2.14× lower at baseline in the lines without LSR | 0.096 | ⚠ within organs, on part of the lines; also absent: ENTPD2, EPHA10, OCLN |
| [[TMC6]] | C | LSR activity raises TMC6's level | lines that do not express LSR (19) vs lines expressing it (31) | 3.77× lower at baseline in the lines without LSR | 0.005 | ⚠ within organs, on part of the lines; also absent: ENTPD2, EPHA10, OCLN; co-absent with the target |
| [[CDC42BPG]] | C | LSR activity raises CDC42BPG's level | lines that do not express LSR (19) vs lines expressing it (31) | 3.34× lower at baseline in the lines without LSR | 0.011 | ⚠ within organs, on part of the lines; also absent: ENTPD2, EPHA10, OCLN; co-absent with the target |

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.632). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.4, -1.3); signed map (5.3, 30.9). **Vector** length 96.4, 28.5% of its response variance represented; |z| ≥ 3 in 760 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +16.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.9 | +4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +10.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.5 | +0.9 |
|  | [[SBI-0640756 (drug)]] 5 µM |  | +1.5 | +0.3 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.4 | +0.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.4 | -7.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.9 | -7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.6 | -7.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.6 | -8.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | -5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.6 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.5 | -6.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.4 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | lipolysis stimulated lipoprotein receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,248,330-35,267,964 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LISCH7, ILDR3 |
| Gene groups (HGNC) | Immunoglobulin like domain containing |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 5 pathways, smallest: VLDL clearance; LDL clearance; Plasma lipoprotein clearance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86X29](https://www.uniprot.org/uniprotkb/Q86X29) (Lipolysis-stimulated lipoprotein receptor):

> Probable role in the clearance of triglyceride-rich lipoprotein from blood. Binds chylomicrons, LDL and VLDL in presence of free fatty acids and allows their subsequent uptake in the cells (By similarity). Maintains epithelial barrier function by recruiting MARVELD2/tricellulin to tricellular tight junctions (By similarity).

**Summary**, from NCBI Gene [51599](https://www.ncbi.nlm.nih.gov/gene/51599):

> Predicted to be involved in several processes, including establishment of skin barrier; protein localization to tricellular tight junction; and tricellular tight junction assembly. Predicted to act upstream of or within maintenance of blood-brain barrier. Located in plasma membrane and tight junction. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29572](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29572) · Entrez [51599](https://www.ncbi.nlm.nih.gov/gene/51599) · UniProt [Q86X29](https://www.uniprot.org/uniprotkb/Q86X29) · Ensembl [ENSG00000105699](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105699)

## Data

Gene col 2646: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2646); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2646, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2646]; `tensor/DDL_lfc|DDL_z.npy` [2646]; `embed/gene_vectors.npy` [2646]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2646 or target_col == 2646). Every well: [[LSR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
