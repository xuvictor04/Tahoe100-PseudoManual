---
symbol: "ANKRD20A7P"
type: "gene"
col: 14103
ensembl_id: "ENSG00000236816"
name: "ankyrin repeat domain 20 family member A7, pseudogene"
location: "9p11.1"
module: 22
arm: "+"
pooled_cpm: 2.9
n_lines_expressing: 20
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# ANKRD20A7P

*ankyrin repeat domain 20 family member A7, pseudogene* — 9p11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.90× (z +12.9, q 3e-35, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.94× (z +7.9, q 5e-13, up in 1 of 12 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LOX-IMVI 0.0868×, H4 0.151×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.0811×, SNU-423 0.124×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LOX-IMVI 0.152×, SNU-423 0.139×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (HepG2/C3A 0.0561×, LOX-IMVI 0.192×).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYT9]] (+0.55, fdr 1e-04), [[DPY19L2P1]] (+0.54, fdr 5e-05), [[ANKRD20A4P]] (+0.51, fdr 4e-05); moves opposite to [[NCSTN]] (-0.46, fdr 1e-04), [[BECN1]] (-0.45, fdr 9e-04, ⚠ not reproduced), [[SELENOF]] (-0.45, fdr 2e-04), [[ITFG1]] (-0.44, fdr 4e-04).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SYT9]] → it (grade C ⚠); 2 go from it, the strongest it → [[ANKRD20A11P]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14103.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.90×** | +12.9 | 3e-35 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.30×** | +10.1 | 2e-21 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.30×** | +9.3 | 2e-18 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +7.9 | 5e-13 | 1/12 (H4) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.75×** | +6.7 | 3e-09 | 4/16 (NCI-H1573, RPMI-7951, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +5.9 | 4e-07 | 0/11 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +5.6 | 2e-06 | 0/11 | top dose only | cell-cycle shift (explains ~8% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.22×** | +4.8 | 1e-04 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.61×** | +4.0 | 0.004 | 0/11 | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +3.9 | 0.005 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.40×** | +3.9 | 0.006 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.5 | 0.019 | 0/11 | top dose only |  |
| [[Allantoin (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +3.5 | 0.020 | 0/13 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +3.5 | 0.022 | 3/13 (H4, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +3.3 | 0.040 | 5/13 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.063 | 0/14 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +3.0 | 0.077 | 4/11 (MIA PaCa-2, H4, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.48×** | +3.0 | 0.077 | 1/11 (LOX-IMVI) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14103.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LOX-IMVI 0.0868×, H4 0.151×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.0811×, SNU-423 0.124×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LOX-IMVI 0.152×, SNU-423 0.139×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (HepG2/C3A 0.0561×, LOX-IMVI 0.192×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.866× | -4.5 | 0.004 | 3/17 (C-33 A, SK-MEL-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.686× | -3.2 | 0.37 | 7/14 (H4, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14103. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 12.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0868× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -10.0) |
| [[H4 (line)]] | wt | 102 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -11.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 12.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 8.88 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.152× (z -9.7) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 8.68 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0561× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 9.55 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0811× (z -11.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.638 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.938 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.506 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.479 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.759 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.544 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.277 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.263 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.303 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.747 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.437 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.596 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14103), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYT9]] | +0.55 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[DPY19L2P1]] | +0.54 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[ANKRD20A4P]] | +0.51 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[ADRA1B]] | +0.50 | +0.40 / +0.40 | both halves | 5e-05 |  |
| [[KIF20B]] | +0.46 | +0.39 / +0.40 | both halves | 5e-05 |  |
| [[PGBD1]] | +0.46 | +0.32 / +0.43 | both halves | 2e-04 |  |
| [[CEP135]] | +0.45 | +0.40 / +0.42 | both halves | 4e-05 |  |
| [[FMN2]] | +0.45 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[N4BP3]] | +0.45 | +0.29 / +0.36 | both halves | 2e-04 |  |
| [[RGS7]] | +0.44 | +0.37 / +0.47 | both halves | 8e-05 |  |
| [[NOL4]] | +0.44 | +0.40 / +0.41 | both halves | 5e-05 |  |
| [[RCCD1]] | +0.43 | +0.28 / +0.37 | both halves | 3e-04 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCSTN]] | -0.46 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[BECN1]] | -0.45 | -0.19 / -0.43 | ⚠ not reproduced | 9e-04 |  |
| [[SELENOF]] | -0.45 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[ITFG1]] | -0.44 | -0.26 / -0.42 | both halves | 4e-04 |  |
| [[LMAN2]] | -0.43 | -0.23 / -0.45 | both halves | 5e-04 |  |
| [[CCNO-DT]] | -0.42 | -0.24 / -0.28 | both halves | 4e-04 |  |
| [[LIG3]] | -0.41 | -0.35 / -0.28 | both halves | 3e-04 |  |
| [[GHITM]] | -0.41 | -0.37 / -0.30 | both halves | 2e-04 |  |
| [[ARSD]] | -0.40 | -0.29 / -0.32 | both halves | 2e-04 |  |
| [[YPEL5]] | -0.40 | -0.30 / -0.33 | both halves | 2e-04 |  |
| [[DNAJB11]] | -0.40 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[FTX]] | -0.40 | -0.25 / -0.32 | both halves | 4e-04 |  |
| [[CMPK1]] | -0.40 | -0.33 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYT9]] | C | SYT9 activity raises ANKRD20A7P's level | lines that do not express SYT9 (35) vs lines expressing it (15) | 1.83× lower at baseline in the lines without SYT9 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, ZNF732, S100A8; co-absent with the target |
| [[POU3F3]] | C | POU3F3 activity raises ANKRD20A7P's level | lines that do not express POU3F3 (34) vs lines expressing it (16) | 1.47× lower at baseline in the lines without POU3F3 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PANTR1, EPGN, ENSG00000244468; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD20A11P]] | C | ANKRD20A7P activity raises ANKRD20A11P's level | lines that do not express ANKRD20A7P (30) vs lines expressing it (20) | 1.79× lower at baseline in the lines without ANKRD20A7P | 0.072 | ⚠ within organs, on part of the lines; also absent: BNC1, MAGEA1, ENSG00000275649; co-absent with the target |
| [[ANKRD20A4P]] | C | ANKRD20A7P activity raises ANKRD20A4P's level | lines that do not express ANKRD20A7P (30) vs lines expressing it (20) | 2.18× lower at baseline in the lines without ANKRD20A7P | 0.094 | ⚠ within organs, on part of the lines; also absent: BNC1, MAGEA1, ENSG00000275649; co-absent with the target |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.279). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.9, 29.0); signed map (30.7, 32.2). **Vector** length 25.5, 4.20% of its response variance represented; |z| ≥ 3 in 375 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.0 | +3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.0 | +7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +0.8 | +2.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +0.8 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.8 | -0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.8 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.5 | +0.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.5 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -0.8 | +5.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | +1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -0.8 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.8 | +1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.7 | +0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.7 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.5 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.5 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 20 family member A7, pseudogene |
| Locus type | pseudogene |
| Location | 9p11.1 — chr9:42,852,675-42,920,095 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:31980](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31980) · Entrez [653436](https://www.ncbi.nlm.nih.gov/gene/653436) · Ensembl [ENSG00000236816](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236816)

## Data

Gene col 14103: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14103); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14103, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14103]; `tensor/DDL_lfc|DDL_z.npy` [14103]; `embed/gene_vectors.npy` [14103]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14103 or target_col == 14103). Every well: [[ANKRD20A7P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD20A7P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
