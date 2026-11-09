---
symbol: "ANKRD20A1"
type: "gene"
col: 15298
ensembl_id: "ENSG00000260691"
name: "ankyrin repeat domain 20 family member A1"
location: "9q21.11"
module: 196
arm: "+"
pooled_cpm: 2.14
n_lines_expressing: 30
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 6
tags: ["gene", "module/196"]
generated_by: "tahoemap"
---

# ANKRD20A1

*ankyrin repeat domain 20 family member A1* — 9q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.46× (z +9.1, q 6e-17, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.59× (z +5.0, q 5e-05, up in 6 of 22 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 5 µM in 1 line (SW480 0.0963×); [[Bortezomib (drug)]] 0.05 µM in 1 line (Hs 766T 0.0822×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD20A4P]] (+0.79, fdr 7e-06), [[CACNA1H]] (+0.55, fdr 4e-05), [[CNTNAP3P2]] (+0.49, fdr 5e-05); moves opposite to [[SPAG16]] (-0.47, fdr 7e-05), [[WDFY3]] (-0.46, fdr 2e-04), [[FTX]] (-0.44, fdr 1e-04).
> It is in [[Module 196]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PTPRZ1]] → it (grade B ⚠); 6 go from it, the strongest it → [[NT5M]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15298.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.46×** | +9.1 | 6e-17 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +5.5 | 1e-05 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +5.2 | 4e-05 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +5.1 | 4e-05 | 1/9 (LOX-IMVI) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.55×** | +5.1 | 4e-05 | 0/2 | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +5.0 | 5e-05 | 6/22 (LS 180, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +4.8 | 1e-04 | 3/14 (SK-MEL-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.82×** | +4.6 | 4e-04 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +4.4 | 6e-04 | 5/23 (H4, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.68×** | +3.9 | 0.005 | 0/2 | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.49×** | +3.6 | 0.014 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +3.5 | 0.023 | 0/11 | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +3.4 | 0.033 | 2/24 (LOX-IMVI, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.31×** | +3.3 | 0.033 | 0/2 | rises with dose | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.84×** | +3.3 | 0.033 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.033 | 0/14 | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.50×** | +3.1 | 0.064 | 0/7 | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +3.1 | 0.064 | 2/15 (LS 180, SW480) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.32×** | +2.9 | 0.096 | 1/20 (SW1417) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15298.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 5 µM in 1 line (SW480 0.0963×); [[Bortezomib (drug)]] 0.05 µM in 1 line (Hs 766T 0.0822×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | 0.654× | -3.2 | 0.68 | 3/22 (A-172, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15298. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 8.59 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0822× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 4.71 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0963× (z -8.8) |
| [[A-172 (line)]] | wt | 0.695 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.213 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.321 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.934 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.626 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.264 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.281 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.607 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.248 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.597 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.277 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.215 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.657 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.232 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.555 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.645 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.874 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.882 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15298), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD20A4P]] | +0.79 | +0.71 / +0.75 | both halves | 7e-06 | same gene group; STRING 646 |
| [[CACNA1H]] | +0.55 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[CNTNAP3P2]] | +0.49 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[LAPTM5]] | +0.47 | +0.40 / +0.35 | both halves | 1e-04 |  |
| [[GLDC]] | +0.47 | +0.30 / +0.46 | both halves | 2e-04 |  |
| [[CACNA2D4]] | +0.47 | +0.39 / +0.45 | both halves | 5e-05 |  |
| [[LHX6]] | +0.46 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[PARVB]] | +0.46 | +0.33 / +0.35 | both halves | 1e-04 |  |
| [[NT5M]] | +0.46 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[SDC3]] | +0.45 | +0.33 / +0.45 | both halves | 1e-04 |  |
| [[PTPRZ1]] | +0.45 | +0.36 / +0.39 | both halves | 9e-05 |  |
| [[STN1]] | +0.45 | +0.33 / +0.38 | both halves | 1e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG16]] | -0.47 | -0.37 / -0.40 | both halves | 7e-05 |  |
| [[WDFY3]] | -0.46 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[FTX]] | -0.44 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[AEBP2]] | -0.44 | -0.25 / -0.37 | both halves | 4e-04 |  |
| [[EXOC4]] | -0.44 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[TBCK]] | -0.43 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[ARID1B]] | -0.43 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[GET3]] | -0.42 | -0.44 / -0.29 | both halves | 2e-04 |  |
| [[CCDC30]] | -0.42 | -0.31 / -0.27 | both halves | 3e-04 |  |
| [[SUMF1]] | -0.42 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[TLK2]] | -0.41 | -0.17 / -0.42 | ⚠ not reproduced | 0.001 |  |
| [[NEK11]] | -0.40 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[VPS13B]] | -0.40 | -0.28 / -0.39 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRZ1]] | B | PTPRZ1 activity raises ANKRD20A1's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 2.55× lower at baseline in the lines without PTPRZ1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[TERT]] | B | TERT activity raises ANKRD20A1's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.40× lower at baseline in the lines without TERT | 0.046 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[NT5M]] | B | NT5M activity raises ANKRD20A1's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.66× lower at baseline in the lines without NT5M | 0.066 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[LINC01844]] | B | LINC01844 activity raises ANKRD20A1's level | lines that do not express LINC01844 (11) vs lines expressing it (39) | 1.67× lower at baseline in the lines without LINC01844 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000287712, ADGRG2, ENSG00000291283; maybe low, not absent |
| [[CNTNAP3P2]] | B | CNTNAP3P2 activity raises ANKRD20A1's level | lines that do not express CNTNAP3P2 (19) vs lines expressing it (31) | 1.63× lower at baseline in the lines without CNTNAP3P2 | 0.091 | ⚠ within organs, on part of the lines; also absent: CNTNAP3B, CNTNAP3, CNTNAP3C |
| [[ANKRD20A4P]] | C | ANKRD20A4P activity raises ANKRD20A1's level | lines that do not express ANKRD20A4P (24) vs lines expressing it (26) | 1.98× lower at baseline in the lines without ANKRD20A4P | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000253503, ENSG00000253500, ADGRF5; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | ANKRD20A1 activity raises NT5M's level | lines that do not express ANKRD20A1 (20) vs lines expressing it (30) | 2.02× lower at baseline in the lines without ANKRD20A1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ANKRD20A4P, CTNNA2, SCN8A |
| [[DOT1L]] | B | ANKRD20A1 activity raises DOT1L's level | lines that do not express ANKRD20A1 (20) vs lines expressing it (30) | 1.37× lower at baseline in the lines without ANKRD20A1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ANKRD20A4P, CTNNA2, SCN8A |
| [[SDC3]] | B | ANKRD20A1 activity raises SDC3's level | lines that do not express ANKRD20A1 (20) vs lines expressing it (30) | 1.89× lower at baseline in the lines without ANKRD20A1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ANKRD20A4P, CTNNA2, SCN8A |
| [[CEP85]] | B | ANKRD20A1 activity raises CEP85's level | lines that do not express ANKRD20A1 (20) vs lines expressing it (30) | 1.41× lower at baseline in the lines without ANKRD20A1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ANKRD20A4P, CTNNA2, SCN8A |
| [[SEMA3F]] | B | ANKRD20A1 activity raises SEMA3F's level | lines that do not express ANKRD20A1 (20) vs lines expressing it (30) | 1.37× lower at baseline in the lines without ANKRD20A1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ANKRD20A4P, CTNNA2, SCN8A |
| [[ANKRD20A4P]] | C | ANKRD20A1 activity raises ANKRD20A4P's level | lines that do not express ANKRD20A1 (20) vs lines expressing it (30) | 2.34× lower at baseline in the lines without ANKRD20A1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ANKRD20A4P, CTNNA2, SCN8A; co-absent with the target |

## Where it sits

- **Module**: [[Module 196]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.676). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.9, 42.7); signed map (-14.7, 42.5). **Vector** length 20.0, 2.24% of its response variance represented; |z| ≥ 3 in 469 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.4 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.2 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.0 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.0 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.4 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.4 | +1.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.4 | -0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.4 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | +0.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -2.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.6 | -1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -0.5 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -0.5 | -0.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -0.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 20 family member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.11 — chr9:67,832,765-67,920,552 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434A171; previously ANKRD20A |
| Gene groups (HGNC) | N-Ank proteins |
| Matched by | ensembl_id |

UniProt [Q5TYW2](https://www.uniprot.org/uniprotkb/Q5TYW2) carries no function annotation.

**Summary**, from NCBI Gene [84210](https://www.ncbi.nlm.nih.gov/gene/84210):

> Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23665](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23665) · Entrez [84210](https://www.ncbi.nlm.nih.gov/gene/84210) · UniProt [Q5TYW2](https://www.uniprot.org/uniprotkb/Q5TYW2) · Ensembl [ENSG00000260691](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000260691)

## Data

Gene col 15298: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15298); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15298, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15298]; `tensor/DDL_lfc|DDL_z.npy` [15298]; `embed/gene_vectors.npy` [15298]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15298 or target_col == 15298). Every well: [[ANKRD20A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD20A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
