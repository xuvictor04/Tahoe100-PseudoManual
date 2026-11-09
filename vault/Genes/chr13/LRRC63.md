---
symbol: "LRRC63"
type: "gene"
col: 10450
ensembl_id: "ENSG00000173988"
name: "leucine rich repeat containing 63"
location: "13q14.13"
module: 19
arm: "+"
pooled_cpm: 2.73
n_lines_expressing: 25
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# LRRC63

*leucine rich repeat containing 63* — 13q14.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.25× (z +9.2, q 2e-17, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.19× (z +7.3, q 3e-11, up in 14 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.470× (z -5.1, q 2e-04, down in 14 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLITRK5]] (+0.70, fdr 7e-06), [[FBXO15]] (+0.63, fdr 1e-05), [[RAB3C]] (+0.63, fdr 1e-05); moves opposite to [[CCL3]] (-0.46, fdr 2e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[P3H2-AS1]] → it (grade C ⚠); 4 go from it, the strongest it → [[LRRC34]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10450.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.25×** | +9.2 | 2e-17 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.85×** | +8.3 | 4e-14 | 0/2 | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.04×** | +7.4 | 3e-11 | 3/6 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.19×** | +7.3 | 3e-11 | 14/21 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **2.08×** | +6.8 | 1e-09 | 13/21 (NCI-H23, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +6.3 | 3e-08 | 1/16 (HEC-1-A) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.23×** | +5.3 | 1e-05 | 10/17 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.53×** | +4.4 | 8e-04 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.89×** | +4.2 | 0.002 | 7/20 (J82, NCI-H460, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +3.6 | 0.019 | 0/10 | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.69×** | +3.5 | 0.029 | 13/21 (J82, SK-MEL-2, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.63×** | +3.2 | 0.057 | 0/18 | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.65×** | +3.2 | 0.065 | 2/18 (NCI-H460, J82) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +3.1 | 0.087 | 6/19 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.61×** | +3.0 | 0.091 | 2/20 (A498, RPMI-7951) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10450.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.470×** | -5.1 | 2e-04 | 14/20 (J82, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.479×** | -4.9 | 2e-04 | 15/21 (NCI-H23, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.504×** | -4.4 | 0.002 | 10/20 (NCI-H460, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.519×** | -4.4 | 0.002 | 12/18 (J82, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~12% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | 0.711× | -3.2 | 0.13 | 14/16 (NCI-H460, RPMI-7951, …) | rises with dose | composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.622× | -3.2 | 0.14 | 3/20 (NCI-H23, NCI-H460, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.626× | -3.0 | 0.20 | 6/18 (NCI-H460, J82, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10450. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.1 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0992× (z -16.4) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.101× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 8.17 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0186× (z -14.3) |
| [[J82 (line)]] | alt | 5.53 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0270× (z -12.7) |
| [[RPMI-7951 (line)]] | alt | 4.18 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0856× (z -8.7) ⚠ cell-cycle shift, explains ~90% of this change |
| [[A-172 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.801 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.834 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.866 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.599 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.382 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.479 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.324 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.998 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.266 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.358 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.355 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.569 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10450), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLITRK5]] | +0.70 | +0.61 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[FBXO15]] | +0.63 | +0.66 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[RAB3C]] | +0.63 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[LINC00461]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SNCA]] | +0.62 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[PAX7]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[SLITRK4]] | +0.61 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[LINC01035]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ASXL3]] | +0.59 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SCARA5]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[OCA2]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[NCKAP5-AS2]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCL3]] | -0.46 | -0.48 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P3H2-AS1]] | C | P3H2-AS1 activity raises LRRC63's level | lines that do not express P3H2-AS1 (30) vs lines expressing it (20) | 2.03× lower at baseline in the lines without P3H2-AS1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: P3H2, SRGN, KIRREL3; co-absent with the target |
| [[COL4A3]] | C | COL4A3 activity raises LRRC63's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 2.05× lower at baseline in the lines without COL4A3 | 0.039 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4; co-absent with the target |
| [[COL4A4]] | C | COL4A4 activity raises LRRC63's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 2.09× lower at baseline in the lines without COL4A4 | 0.059 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A; co-absent with the target |
| [[EPGN]] | C | EPGN activity raises LRRC63's level | lines that do not express EPGN (41) vs lines expressing it (9) | 2.38× lower at baseline in the lines without EPGN | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, TBXT, ENSG00000289418; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC34]] | B | LRRC63 activity lowers LRRC34's level | lines that do not express LRRC63 (25) vs lines expressing it (25) | 1.35× higher at baseline in the lines without LRRC63 | 0.051 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, STAC, CRLF2 |
| [[LRRIQ3]] | B | LRRC63 activity raises LRRIQ3's level | lines that do not express LRRC63 (25) vs lines expressing it (25) | 1.70× lower at baseline in the lines without LRRC63 | 0.060 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, STAC, CRLF2 |
| [[FBXO15]] | B | LRRC63 activity raises FBXO15's level | lines that do not express LRRC63 (25) vs lines expressing it (25) | 2.16× lower at baseline in the lines without LRRC63 | 0.090 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, STAC, CRLF2 |
| [[BASP1-AS1]] | C | LRRC63 activity raises BASP1-AS1's level | lines that do not express LRRC63 (25) vs lines expressing it (25) | 3.37× lower at baseline in the lines without LRRC63 | 0.046 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, STAC, CRLF2; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.642). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.8, 36.2); signed map (42.3, 42.1). **Vector** length 47.9, 11.8% of its response variance represented; |z| ≥ 3 in 572 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +0.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +4.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -5.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.7 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.3 | -4.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -0.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -0.9 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -0.9 | -2.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -2.2 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 63 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.13 — chr13:46,211,928-46,277,115 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RP11-139H14.4 |
| Matched by | ensembl_id |

UniProt [Q05C16](https://www.uniprot.org/uniprotkb/Q05C16) carries no function annotation.

**Summary**, from NCBI Gene [220416](https://www.ncbi.nlm.nih.gov/gene/220416):

> Predicted to be involved in intracellular signal transduction. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:34296](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34296) · Entrez [220416](https://www.ncbi.nlm.nih.gov/gene/220416) · UniProt [Q05C16](https://www.uniprot.org/uniprotkb/Q05C16) · Ensembl [ENSG00000173988](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173988)

## Data

Gene col 10450: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10450); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10450, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10450]; `tensor/DDL_lfc|DDL_z.npy` [10450]; `embed/gene_vectors.npy` [10450]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10450 or target_col == 10450). Every well: [[LRRC63 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC63.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
