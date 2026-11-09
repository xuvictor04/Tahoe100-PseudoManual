---
symbol: "MT1G"
type: "gene"
col: 4589
ensembl_id: "ENSG00000125144"
name: "metallothionein 1G"
location: "16q13"
module: 123
arm: "+"
pooled_cpm: 6.72
n_lines_expressing: 19
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# MT1G

*metallothionein 1G* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 12.5× (z +15.6, q 0e+00, up in 13 of 15 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Chlorhexidine (diacetate) (drug)]] 5 µM: 6.25× (z +11.3, q 2e-27, up in 16 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (COLO 205 0.0259×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD20A9P]] (+0.60, fdr 3e-05), [[ARL4A]] (+0.57, fdr 3e-05), [[PIM3]] (+0.57, fdr 2e-05); moves opposite to [[NADSYN1]] (-0.60, fdr 4e-05), [[NAXD]] (-0.54, fdr 5e-05), [[METTL4]] (-0.51, fdr 1e-04).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MT1F]] → it (grade C ⚠); 5 go from it, the strongest it → [[HCFC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4589.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **12.5×** | +15.6 | 0e+00 | 13/15 (SW480, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **6.25×** | +11.3 | 2e-27 | 16/16 (SW480, KATO III, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **11.6×** | +10.7 | 1e-24 | 10/15 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.98×** | +7.5 | 8e-12 | 4/7 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **5.07×** | +7.1 | 1e-10 | 6/13 (KATO III, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **4.95×** | +6.7 | 2e-09 | 12/16 (SW480, CFPAC-1, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.51×** | +6.6 | 4e-09 | 16/16 (SW480, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.40×** | +5.4 | 5e-06 | 14/16 (SW48, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.69×** | +5.2 | 1e-05 | 1/10 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.19×** | +5.1 | 2e-05 | 8/16 (KATO III, SW1417, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.82×** | +4.5 | 3e-04 | 6/15 (SW480, CFPAC-1, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.50×** | +4.0 | 0.003 | 6/16 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **2.45×** | +3.9 | 0.004 | 8/13 (CFPAC-1, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.43×** | +3.7 | 0.008 | 5/13 (SNU-423, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.30×** | +3.6 | 0.011 | 14/16 (SW480, KATO III, …) | two highest doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.25×** | +3.5 | 0.015 | 8/16 (CFPAC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4589.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (COLO 205 0.0259×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.431× | -3.4 | 0.31 | 6/16 (RPMI-7951, HOP62, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.444× | -3.3 | 0.31 | 3/16 (RPMI-7951, LoVo, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.92 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4589. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 15.3 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 43.2× (z +16.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 18.4× (z +12.7) | — |
| [[CFPAC-1 (line)]] | alt | 76.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +14.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 12.6× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 5.06 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.5× (z +11.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 11.6× (z +9.0) | — |
| [[KATO III (line)]] | alt | 10.3 | 2 (1 ⚠) | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 22.2× (z +10.1) | — |
| [[COLO 205 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0259× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 5.81 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 144× (z +12.1) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[Hs 766T (line)]] | wt | 14.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.1× (z +10.4) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[LS 180 (line)]] | wt | 48.5 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 6.74× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 5.90 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 112× (z +12.4) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 0.717 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.446 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.556 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.656 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.613 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.726 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.779 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.682 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.986 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.626 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.626 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.681 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4589), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 7 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD20A9P]] | +0.60 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[ARL4A]] | +0.57 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[PIM3]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[MT1E]] | +0.57 | +0.54 / +0.50 | both halves | 1e-05 | same gene group; pathway: Metallothioneins bind metals; STRING 795; ⚠ same locus (39.6 kb: neighbours can correlate without regulation) |
| [[SYP]] | +0.56 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[MT1F]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 | same gene group; pathway: Metallothioneins bind metals; STRING 911; ⚠ same locus (6.0 kb: neighbours can correlate without regulation) |
| [[DUSP2]] | +0.54 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[KLF2]] | +0.54 | +0.35 / +0.37 | both halves | 1e-04 |  |
| [[MIDN]] | +0.53 | +0.43 / +0.45 | both halves | 4e-05 |  |
| [[DHRS2]] | +0.52 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[IRF2BP2]] | +0.52 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[KRTCAP2]] | +0.51 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[RNF223]] | +0.51 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[HAGHL]] | +0.51 | +0.35 / +0.52 | both halves | 1e-04 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NADSYN1]] | -0.60 | -0.43 / -0.58 | both halves | 4e-05 |  |
| [[NAXD]] | -0.54 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[METTL4]] | -0.51 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[MRE11]] | -0.50 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[MSL3]] | -0.49 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[NNT]] | -0.49 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[ZCCHC4]] | -0.48 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[LY6G5B]] | -0.48 | -0.26 / -0.52 | both halves | 4e-04 |  |
| [[RBBP4]] | -0.48 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[PAPOLA]] | -0.48 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[ZNF731P]] | -0.47 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[PEX26]] | -0.47 | -0.32 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MT1F]] | C | MT1F activity raises MT1G's level | lines that do not express MT1F (17) vs lines expressing it (33) | 2.78× lower at baseline in the lines without MT1F | 0.010 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862; co-absent with the target |
| [[RNF223]] | C | RNF223 activity raises MT1G's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 3.08× lower at baseline in the lines without RNF223 | 0.045 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2; co-absent with the target |
| [[FOXA2]] | C | FOXA2 activity raises MT1G's level | lines that do not express FOXA2 (28) vs lines expressing it (22) | 2.52× lower at baseline in the lines without FOXA2 | 0.076 | ⚠ within organs, on part of the lines; also absent: TFF1, GPX2, F5; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HCFC1]] | B | MT1G activity lowers HCFC1's level | lines that do not express MT1G (31) vs lines expressing it (19) | 1.27× higher at baseline in the lines without MT1G | 0.065 | ⚠ within organs, on part of the lines; also absent: TFF2, PROM1, FOXQ1 |
| [[TXNIP]] | B | MT1G activity raises TXNIP's level | lines that do not express MT1G (31) vs lines expressing it (19) | 3.09× lower at baseline in the lines without MT1G | 0.071 | ⚠ within organs, on part of the lines; also absent: TFF2, PROM1, FOXQ1 |
| cells under [[Gallic acid (hydrate) (drug)]] 0.05 µM | B | MT1G activity lowers the cells' numbers under Gallic acid (hydrate) 0.05 µM (makes them more sensitive) | lines that do not express MT1G (31) vs lines expressing it (17) | the lines without MT1G: 1.15× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: TFF2, PROM1, FOXQ1 |
| [[MT1F]] | C | MT1G activity raises MT1F's level | lines that do not express MT1G (31) vs lines expressing it (19) | 2.06× lower at baseline in the lines without MT1G | 0.037 | ⚠ within organs, on part of the lines; also absent: TFF2, PROM1, FOXQ1; co-absent with the target |
| [[MT1E]] | C | MT1G activity raises MT1E's level | lines that do not express MT1G (31) vs lines expressing it (19) | 4.04× lower at baseline in the lines without MT1G | 0.085 | ⚠ within organs, on part of the lines; also absent: TFF2, PROM1, FOXQ1; co-absent with the target |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.518). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-4.3, 24.6); signed map (12.0, 26.6). **Vector** length 39.7, 10.1% of its response variance represented; |z| ≥ 3 in 344 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.9 | +15.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.3 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.1 | +10.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.0 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +5.1 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +0.8 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.8 | +0.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +2.4 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | +0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.9 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.8 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -0.7 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | metallothionein 1G |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:56,666,730-56,668,065 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MT1K; previously MT1 |
| Gene groups (HGNC) | Metallothioneins |
| Reactome | 3 pathways, smallest: Metallothioneins bind metals; Response to metal ions; Cellular responses to stimuli |
| Matched by | ensembl_id |

**Function**, from UniProt [P13640](https://www.uniprot.org/uniprotkb/P13640) (Metallothionein-1G):

> Metallothioneins have a high content of cysteine residues that bind various heavy metals; these proteins are transcriptionally regulated by both heavy metals and glucocorticoids.

**Summary**, from NCBI Gene [4495](https://www.ncbi.nlm.nih.gov/gene/4495):

> Enables zinc ion binding activity. Involved in several processes, including cellular response to cadmium ion; cellular response to copper ion; and cellular response to zinc ion. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7399](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7399) · Entrez [4495](https://www.ncbi.nlm.nih.gov/gene/4495) · UniProt [P13640](https://www.uniprot.org/uniprotkb/P13640) · Ensembl [ENSG00000125144](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125144)

## Data

Gene col 4589: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4589); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4589, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4589]; `tensor/DDL_lfc|DDL_z.npy` [4589]; `embed/gene_vectors.npy` [4589]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4589 or target_col == 4589). Every well: [[MT1G — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT1G.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
