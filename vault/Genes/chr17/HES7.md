---
symbol: "HES7"
type: "gene"
col: 11000
ensembl_id: "ENSG00000179111"
name: "hes family bHLH transcription factor 7"
location: "17p13.1"
module: 94
arm: "+"
pooled_cpm: 5.7
n_lines_expressing: 37
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 27
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# HES7

*hes family bHLH transcription factor 7* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.27× (z +16.9, q 0e+00, up in 26 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.0610×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H23 0.173×; ⚠ cell-cycle shift, explains ~39% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H23 0.174×); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H23 0.206×); [[EX229 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0867×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC43A2]] (+0.62, fdr 1e-05), [[ZNF433]] (+0.60, fdr 1e-05), [[DUSP15]] (+0.60, fdr 1e-05); moves opposite to [[HERC2P9-1]] (-0.57, fdr 1e-04), [[XRCC5]] (-0.53, fdr 4e-05), [[UGGT1]] (-0.49, fdr 3e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[ZNF57]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11000.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.27×** | +16.9 | 0e+00 | 26/30 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.85×** | +12.2 | 8e-32 | 22/31 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.22×** | +9.3 | 3e-18 | 23/33 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.93×** | +8.9 | 1e-16 | 26/31 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **2.70×** | +8.2 | 3e-14 | 26/33 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **2.51×** | +7.6 | 4e-12 | 24/31 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.18×** | +6.4 | 1e-08 | 16/34 (HCT15, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.72×** | +6.3 | 2e-08 | 17/33 (NCI-H460, PANC-1, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.16×** | +6.3 | 2e-08 | 15/32 (A-427, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +6.2 | 3e-08 | 12/22 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +6.2 | 3e-08 | 1/7 (NCI-H2347) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.04×** | +5.7 | 7e-07 | 18/31 (SW1417, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.97×** | +5.6 | 1e-06 | 15/29 (HCT15, HT-29, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.90×** | +5.3 | 6e-06 | 18/32 (NCI-H460, C-33 A, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.43×** | +5.2 | 7e-06 | 15/26 (SW480, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +5.1 | 1e-05 | 12/26 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.16×** | +4.5 | 2e-04 | 9/19 (NCI-H23, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11000.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.0610×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H23 0.173×; ⚠ cell-cycle shift, explains ~39% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H23 0.174×); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H23 0.206×); [[EX229 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0867×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | 0.431× | -3.2 | 0.77 | 11/30 (NCI-H23, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11000. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 72.4 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0610× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.174× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 5.99 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.48× (z +13.0) | — |
| [[A498 (line)]] | wt | 1.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +9.8) | — |
| [[A549 (line)]] | wt | 5.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.68× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.68 | 0 | 1 | — | [[EX229 (drug)]] 0.05 µM 0.0867× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 6.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 8.29 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.52× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 4.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +12.4) | — |
| [[SW480 (line)]] | alt | 5.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +10.2) | — |
| [[A-172 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.647 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.634 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.30 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11000), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC43A2]] | +0.62 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[ZNF433]] | +0.60 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[DUSP15]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[WSB1]] | +0.57 | +0.34 / +0.64 | both halves | 1e-04 |  |
| [[TRPM4]] | +0.56 | +0.38 / +0.63 | both halves | 7e-05 |  |
| [[POLR1H]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[NGFR]] | +0.55 | +0.32 / +0.68 | both halves | 1e-04 |  |
| [[GLIS2]] | +0.54 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[HOXB-AS1]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ZNF563]] | +0.54 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[POLR2H]] | +0.54 | +0.35 / +0.67 | both halves | 1e-04 |  |
| [[ZNF442]] | +0.53 | +0.50 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2P9-1]] | -0.57 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[XRCC5]] | -0.53 | -0.42 / -0.64 | both halves | 4e-05 |  |
| [[UGGT1]] | -0.49 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[SMARCD1]] | -0.47 | -0.22 / -0.58 | both halves | 6e-04 |  |
| [[HERC2]] | -0.46 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[MTOR]] | -0.46 | -0.24 / -0.53 | both halves | 4e-04 |  |
| [[PSMD1]] | -0.46 | -0.28 / -0.55 | both halves | 3e-04 | pathway: Formation of paraxial mesoderm |
| [[CHID1]] | -0.46 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[EP400P1]] | -0.46 | -0.25 / -0.51 | both halves | 4e-04 |  |
| [[PSMD2]] | -0.45 | -0.36 / -0.50 | both halves | 1e-04 | pathway: Formation of paraxial mesoderm |
| [[GFM1]] | -0.45 | -0.18 / -0.50 | ⚠ one half (not replicated) | 1e-03 |  |
| [[TREX2]] | -0.45 | -0.33 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HES7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KREMEN2]] | B | KREMEN2 activity raises HES7's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 2.01× lower at baseline in the lines without KREMEN2 | 0.085 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF57]] | B | HES7 activity raises ZNF57's level | lines that do not express HES7 (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without HES7 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, ACTN2, ENSG00000281091; maybe low, not absent |
| [[ZNF580]] | B | HES7 activity raises ZNF580's level | lines that do not express HES7 (13) vs lines expressing it (37) | 1.26× lower at baseline in the lines without HES7 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, ACTN2, ENSG00000281091; maybe low, not absent |
| [[C1orf56]] | B | HES7 activity raises C1orf56's level | lines that do not express HES7 (13) vs lines expressing it (37) | 1.12× lower at baseline in the lines without HES7 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, ACTN2, ENSG00000281091; maybe low, not absent |
| [[CA11]] | B | HES7 activity raises CA11's level | lines that do not express HES7 (13) vs lines expressing it (37) | 1.86× lower at baseline in the lines without HES7 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, ACTN2, ENSG00000281091; maybe low, not absent |
| [[POLR2H]] | B | HES7 activity raises POLR2H's level | lines that do not express HES7 (13) vs lines expressing it (37) | 1.19× lower at baseline in the lines without HES7 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, ACTN2, ENSG00000281091; maybe low, not absent |
| [[SDSL]] | B | HES7 activity raises SDSL's level | lines that do not express HES7 (13) vs lines expressing it (37) | 1.21× lower at baseline in the lines without HES7 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, ACTN2, ENSG00000281091; maybe low, not absent |
| cells under [[Elimusertib hydrochloride (drug)]] 0.5 µM | B | HES7 activity raises the cells' numbers under Elimusertib hydrochloride 0.5 µM (protects the cells) | lines that do not express HES7 (13) vs lines expressing it (35) | the lines without HES7: 0.81× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, ACTN2, ENSG00000281091; maybe low, not absent |

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.623). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.7, 24.6); signed map (15.4, -16.1). **Vector** length 66.6, 14.4% of its response variance represented; |z| ≥ 3 in 684 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.2 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +9.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.2 | +7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +16.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.5 | +5.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +3.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.8 | +3.9 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.4 | +0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.0 | +2.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -1.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | +0.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | hes family bHLH transcription factor 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:8,120,592-8,124,106 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bHLHb37 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Reactome | 3 pathways, smallest: Somitogenesis; Formation of paraxial mesoderm; Gastrulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYE0](https://www.uniprot.org/uniprotkb/Q9BYE0) (Transcription factor HES-7):

> Transcriptional repressor. Represses transcription from both N box- and E box-containing promoters. May with HES1, cooperatively regulate somite formation in the presomitic mesoderm (PSM). May function as a segmentation clock, which is essential for coordinated somite segmentation (By similarity).

**Summary**, from NCBI Gene [84667](https://www.ncbi.nlm.nih.gov/gene/84667):

> This gene encodes a member of the hairy and enhancer of split family of bHLH transcription factors. The mouse ortholog of this gene is regulated by Notch signaling. The protein functions as a transcriptional repressor, and is implicated in correct patterning of the axial skeleton. A mutation in this gene has been shown to result in spondylocostal dysostosis. Multiple transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:15977](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15977) · Entrez [84667](https://www.ncbi.nlm.nih.gov/gene/84667) · UniProt [Q9BYE0](https://www.uniprot.org/uniprotkb/Q9BYE0) · Ensembl [ENSG00000179111](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179111)

## Data

Gene col 11000: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11000); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11000, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11000]; `tensor/DDL_lfc|DDL_z.npy` [11000]; `embed/gene_vectors.npy` [11000]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11000 or target_col == 11000). Every well: [[HES7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HES7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
