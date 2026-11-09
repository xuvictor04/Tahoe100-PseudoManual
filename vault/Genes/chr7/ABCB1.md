---
symbol: "ABCB1"
type: "gene"
col: 1433
ensembl_id: "ENSG00000085563"
name: "ATP binding cassette subfamily B member 1"
location: "7q21.12"
module: 61
arm: "+"
pooled_cpm: 15.04
n_lines_expressing: 18
n_dd_up: 44
n_dd_down: 0
n_dd_up_clean: 29
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# ABCB1

*ATP binding cassette subfamily B member 1* — 7q21.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.63× (z +21.8, q 0e+00, up in 12 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEX15]] (+0.56, fdr 1e-04), [[RNF223]] (+0.50, fdr 2e-04), [[RUNDC3B]] (+0.49, fdr 4e-05, ⚠ same locus), [[SEMA6A]] (+0.49, fdr 3e-05); moves opposite to [[TCTN3]] (-0.44, fdr 1e-04), [[PSKH1]] (-0.42, fdr 3e-04), [[PDSS2]] (-0.42, fdr 6e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[RUNDC3B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1433.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.63×** | +21.8 | 0e+00 | 12/14 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **7.94×** | +20.9 | 0e+00 | 14/15 (SW480, CFPAC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **3.81×** | +19.1 | 0e+00 | 15/15 (LoVo, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.34×** | +17.2 | 0e+00 | 9/15 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.18×** | +14.4 | 6e-45 | 12/15 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.83×** | +13.5 | 1e-39 | 11/15 (J82, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.86×** | +13.1 | 4e-37 | 11/12 (J82, HOP62, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.65×** | +13.0 | 6e-37 | 14/15 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.57×** | +12.8 | 8e-36 | 14/15 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.50×** | +12.6 | 1e-34 | 14/15 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.77×** | +12.4 | 2e-33 | 7/13 (J82, HOP62, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.16×** | +11.6 | 3e-29 | 15/15 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.77×** | +10.3 | 5e-23 | 15/15 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.87×** | +10.2 | 9e-23 | 14/15 (CFPAC-1, A498, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +6.7 | 9e-10 | 9/13 (SHP-77, A498, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.93×** | +6.6 | 1e-09 | 13/15 (A498, J82, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.89×** | +6.4 | 6e-09 | 13/15 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.86×** | +6.2 | 1e-08 | 4/15 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.89×** | +6.0 | 4e-08 | 11/15 (A498, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1433.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -3.7 | 0.11 | 2/16 (LoVo, HOP62) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.692× | -3.5 | 0.15 | 0/15 | inconsistent across doses |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.740× | -3.1 | 0.39 | 0/15 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1433. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 15.1 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.46× (z +15.7) | — |
| [[A498 (line)]] | wt | 80.4 | 10 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 9.72× (z +18.2) | — |
| [[LoVo (line)]] | wt | 60.2 | 9 | 0 | [[Tucidinostat (drug)]] 5 µM 5.12× (z +15.2) | — |
| [[CFPAC-1 (line)]] | alt | 22.5 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +21.2) | — |
| [[HepG2_C3A (line)]] | wt | 157 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.78× (z +11.7) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.30× (z +8.8) | — |
| [[J82 (line)]] | alt | 18.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.50× (z +13.3) | — |
| [[NCI-H2030 (line)]] | alt | 10.5 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 4.51× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 3.87 | 2 | 0 | [[Auranofin (drug)]] 5 µM 44.4× (z +11.8) | — |
| [[SHP-77 (line)]] | alt | 147 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.08× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 10.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 8.65× (z +11.9) | — |
| [[H4 (line)]] | wt | 14.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 13.2× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 4.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.93× (z +10.4) | — |
| [[A-172 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.38 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.38 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.70 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1433), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEX15]] | +0.56 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[RNF223]] | +0.50 | +0.30 / +0.46 | both halves | 2e-04 |  |
| [[RUNDC3B]] | +0.49 | +0.42 / +0.43 | both halves | 4e-05 | STRING 593; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SEMA6A]] | +0.49 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[RASGEF1B]] | +0.49 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[HSPA2]] | +0.48 | +0.37 / +0.49 | both halves | 8e-05 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[SLC22A23]] | +0.47 | +0.37 / +0.44 | both halves | 7e-05 |  |
| [[AHR]] | +0.47 | +0.32 / +0.49 | both halves | 2e-04 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[PGBD5]] | +0.47 | +0.57 / +0.37 | both halves | 8e-05 |  |
| [[PRKG1]] | +0.47 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[SH3GL2]] | +0.47 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[INA]] | +0.47 | +0.29 / +0.48 | both halves | 2e-04 |  |
| [[PLCL1]] | +0.47 | +0.44 / +0.53 | both halves | 3e-05 | pathway: HALLMARK_UV_RESPONSE_UP |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCTN3]] | -0.44 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[PSKH1]] | -0.42 | -0.26 / -0.37 | both halves | 3e-04 |  |
| [[PDSS2]] | -0.42 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[FAM156A]] | -0.41 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[RMDN3]] | -0.40 | -0.28 / -0.38 | both halves | 3e-04 |  |
| [[GLE1]] | -0.40 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[KIAA0319L]] | -0.40 | -0.37 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ABCB1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLCG2]] | B | PLCG2 activity lowers ABCB1's level | lines that do not express PLCG2 (10) vs lines expressing it (40) | 2.10× higher at baseline in the lines without PLCG2 | 0.081 | ⚠ within organs, on part of the lines; also absent: CRACD; maybe low, not absent |
| [[GABRA2]] | C | GABRA2 activity raises ABCB1's level | lines that do not express GABRA2 (24) vs lines expressing it (26) | 2.24× lower at baseline in the lines without GABRA2 | 0.099 | ⚠ within organs, on part of the lines; also absent: LINC02253, ASXL3, ENSG00000257883; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RUNDC3B]] | B | ABCB1 activity raises RUNDC3B's level | lines that do not express ABCB1 (32) vs lines expressing it (18) | 2.26× lower at baseline in the lines without ABCB1 | 0.002 | ⚠ within organs, on part of the lines; also absent: TIMD4, ZNF736P9Y, PSG1; maybe low, not absent |
| [[RMDN3]] | B | ABCB1 activity raises RMDN3's level | lines that do not express ABCB1 (32) vs lines expressing it (18) | 1.20× lower at baseline in the lines without ABCB1 | 0.087 | ⚠ within organs, on part of the lines; also absent: TIMD4, ZNF736P9Y, PSG1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.445). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.7, 26.2); signed map (31.2, 30.4). **Vector** length 47.8, 11.9% of its response variance represented; |z| ≥ 3 in 500 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +19.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.9 | +13.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +20.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +13.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +6.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +0.5 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -3.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -2.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.8 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.7 | -1.8 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.7 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily B member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.12 — chr7:87,503,017-87,713,323 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P-gp, CD243, GP170, ABC20, p-170, PGY1; previously PGY1, MDR1, CLCS |
| Gene groups (HGNC) | CD molecules; ATP binding cassette subfamily B; ATPase phospholipid transporting |
| Hallmark sets | PEROXISOME, UV_RESPONSE_UP, KRAS_SIGNALING_UP, IL2_STAT5_SIGNALING |
| Reactome | 7 pathways, smallest: Abacavir transmembrane transport; Atorvastatin ADME; Prednisone ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [P08183](https://www.uniprot.org/uniprotkb/P08183) (ATP-dependent translocase ABCB1):

> Translocates phospholipids and drugs across the membrane. Catalyzes the flop of phospholipids from the cytoplasmic to the exoplasmic leaflet of the apical membrane. Participates mainly to the flop of phosphatidylcholine, phosphatidylethanolamine, beta-D-glucosylceramides and sphingomyelins. Energy-dependent efflux pump responsible for decreased drug accumulation in multidrug-resistant cells. May contribute to hepatobiliary and renal excretion of etiocholanolone-3-glucuronate. Appears to have …

**Summary**, from NCBI Gene [5243](https://www.ncbi.nlm.nih.gov/gene/5243):

> The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MDR/TAP subfamily. Members of the MDR/TAP subfamily are involved in multidrug resistance. The protein encoded by this gene is an ATP-dependent drug …

**Accessions** — [HGNC:40](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40) · Entrez [5243](https://www.ncbi.nlm.nih.gov/gene/5243) · UniProt [P08183](https://www.uniprot.org/uniprotkb/P08183) · Ensembl [ENSG00000085563](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085563)

## Data

Gene col 1433: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1433); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1433, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1433]; `tensor/DDL_lfc|DDL_z.npy` [1433]; `embed/gene_vectors.npy` [1433]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1433 or target_col == 1433). Every well: [[ABCB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
