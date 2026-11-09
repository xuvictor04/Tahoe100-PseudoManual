---
symbol: "UPK1B"
type: "gene"
col: 3569
ensembl_id: "ENSG00000114638"
name: "uroplakin 1B"
location: "3q13.32"
module: 19
arm: "+"
pooled_cpm: 2.68
n_lines_expressing: 11
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 6
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# UPK1B

*uroplakin 1B* — 3q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.99× (z +11.4, q 2e-27, up in 4 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.56× (z +8.4, q 4e-15, up in 3 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1573 0.0640×; ⚠ cell-cycle shift, explains ~42% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 0.102×; ⚠ cell-cycle shift, explains ~51% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1573 0.154×).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYP24A1]] (+0.68, fdr 1e-05), [[SMOC1]] (+0.58, fdr 2e-05), [[RSPO3]] (+0.57, fdr 1e-05); moves opposite to [[PRDM16]] (-0.46, fdr 1e-04), [[MAGEA1]] (-0.42, fdr 2e-04), [[TTC4]] (-0.40, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GPR141]] → it (grade C ⚠); 6 go from it, the strongest it → [[XDH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3569.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.99×** | +11.4 | 2e-27 | 4/4 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.24×** | +11.2 | 9e-27 | 1/2 (PANC-1) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.26×** | +10.8 | 6e-25 | 1/2 (PANC-1) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.56×** | +8.4 | 4e-15 | 3/5 (CFPAC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.61×** | +5.9 | 5e-07 | 1/4 (PANC-1) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.38×** | +5.3 | 1e-05 | 1/3 (PANC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.21×** | +5.0 | 4e-05 | 1/3 (PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +4.4 | 7e-04 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +4.3 | 9e-04 | 1/4 (PANC-1) | top dose only | cell-cycle shift (explains ~11% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.58×** | +4.3 | 1e-03 | 1/3 (PANC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +4.2 | 0.002 | 1/6 (NCI-H2030) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.22×** | +3.9 | 0.005 | 0/3 | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.98×** | +3.6 | 0.012 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.47×** | +3.4 | 0.023 | 0/7 | top dose only | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.13×** | +3.4 | 0.023 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.11×** | +3.4 | 0.026 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Posaconazole (drug)]] 0.5 µM |  | **1.66×** | +3.2 | 0.043 | 0/5 | inconsistent across doses |  |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.65×** | +2.9 | 0.097 | 0/4 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3569.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1573 0.0640×; ⚠ cell-cycle shift, explains ~42% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 0.102×; ⚠ cell-cycle shift, explains ~51% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1573 0.154×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.849× | -3.8 | 0.076 | 0/7 | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | 0.717× | -3.0 | 0.52 | 1/7 (PANC-1) | rises with dose | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3569. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 70.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0640× (z -22.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.154× (z -10.6) |
| [[PANC-1 (line)]] | alt | 4.18 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.30× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.556 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.851 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.841 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.735 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.647 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.568 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.596 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.651 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.543 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.507 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.516 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.468 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.877 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.555 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.422 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3569), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP24A1]] | +0.68 | +0.71 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[SMOC1]] | +0.58 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[RSPO3]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[EDIL3]] | +0.57 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[LXN]] | +0.56 | +0.48 / +0.54 | both halves | 2e-05 | **novel candidate** |
| [[LINC01456]] | +0.54 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[VAV3]] | +0.53 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[KLRK1]] | +0.51 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[EYA2]] | +0.49 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[CXXC4]] | +0.49 | +0.38 / +0.42 | both halves | 6e-05 |  |
| [[MGAT4C]] | +0.49 | +0.46 / +0.28 | both halves | 3e-04 |  |
| [[SYT13]] | +0.48 | +0.36 / +0.45 | both halves | 1e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM16]] | -0.46 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[MAGEA1]] | -0.42 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[TTC4]] | -0.40 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[UTP25]] | -0.39 | -0.41 / -0.31 | both halves | 2e-04 |  |
| [[DNAJA3]] | -0.39 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[ZNF202]] | -0.39 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[KLHDC4]] | -0.38 | -0.37 / -0.39 | both halves | 9e-05 |  |
| [[CUX2]] | -0.38 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[ZC3H8]] | -0.38 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[SHLD2]] | -0.38 | -0.31 / -0.33 | both halves | 2e-04 |  |
| [[TATDN1]] | -0.37 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[NUDCD3]] | -0.37 | -0.31 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR141]] | C | GPR141 activity raises UPK1B's level | lines that do not express GPR141 (39) vs lines expressing it (11) | 2.07× lower at baseline in the lines without GPR141 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, S100A8, LINC00879; co-absent with the target |
| [[ADGRG7]] | C | ADGRG7 activity raises UPK1B's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 1.75× lower at baseline in the lines without ADGRG7 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XDH]] | B | UPK1B activity raises XDH's level | lines that do not express UPK1B (39) vs lines expressing it (11) | 2.90× lower at baseline in the lines without UPK1B | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CES1, CGA, SLC15A5; maybe low, not absent |
| [[IQCD]] | B | UPK1B activity raises IQCD's level | lines that do not express UPK1B (39) vs lines expressing it (11) | 1.77× lower at baseline in the lines without UPK1B | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CES1, CGA, SLC15A5; maybe low, not absent |
| [[CYP24A1]] | C | UPK1B activity raises CYP24A1's level | lines that do not express UPK1B (39) vs lines expressing it (11) | 5.24× lower at baseline in the lines without UPK1B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CES1, CGA, SLC15A5; maybe low, not absent; co-absent with the target |
| [[RSPO3]] | C | UPK1B activity raises RSPO3's level | lines that do not express UPK1B (39) vs lines expressing it (11) | 4.32× lower at baseline in the lines without UPK1B | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CES1, CGA, SLC15A5; maybe low, not absent; co-absent with the target |
| [[RHOV]] | C | UPK1B activity raises RHOV's level | lines that do not express UPK1B (39) vs lines expressing it (11) | 2.30× lower at baseline in the lines without UPK1B | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CES1, CGA, SLC15A5; maybe low, not absent; co-absent with the target |
| [[VAV3]] | C | UPK1B activity raises VAV3's level | lines that do not express UPK1B (39) vs lines expressing it (11) | 2.12× lower at baseline in the lines without UPK1B | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CES1, CGA, SLC15A5; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.277). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.3, 32.6); signed map (38.5, 46.2). **Vector** length 20.2, 6.84% of its response variance represented; |z| ≥ 3 in 147 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +10.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.4 | +8.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +0.9 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.8 | +1.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.4 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.4 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.4 | +0.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.4 | +3.4 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -0.6 | -0.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.6 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -0.5 | +1.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.5 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.5 | -2.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | uroplakin 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.32 — chr3:119,173,517-119,205,143 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TSPAN20; previously UPK1 |
| Gene groups (HGNC) | Tetraspanin family |
| Matched by | ensembl_id |

**Function**, from UniProt [O75841](https://www.uniprot.org/uniprotkb/O75841) (Uroplakin-1b):

> Component of the asymmetric unit membrane (AUM); a highly specialized biomembrane elaborated by terminally differentiated urothelial cells. May play an important role in normal bladder epithelial physiology, possibly in regulating membrane permeability of superficial umbrella cells or in stabilizing the apical membrane through AUM/cytoskeletal interactions (By similarity).

**Summary**, from NCBI Gene [7348](https://www.ncbi.nlm.nih.gov/gene/7348):

> The protein encoded by this gene is a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Most of these members are cell-surface proteins that are characterized by the presence of four hydrophobic domains. The proteins mediate signal transduction events that play a role in the regulation of cell development, activation, growth and motility. This encoded protein is found in the asymmetrical unit membrane (AUM) where it can form a complex with other transmembrane 4 …

**Accessions** — [HGNC:12578](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12578) · Entrez [7348](https://www.ncbi.nlm.nih.gov/gene/7348) · UniProt [O75841](https://www.uniprot.org/uniprotkb/O75841) · Ensembl [ENSG00000114638](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114638)

## Data

Gene col 3569: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3569); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3569, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3569]; `tensor/DDL_lfc|DDL_z.npy` [3569]; `embed/gene_vectors.npy` [3569]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3569 or target_col == 3569). Every well: [[UPK1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UPK1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
