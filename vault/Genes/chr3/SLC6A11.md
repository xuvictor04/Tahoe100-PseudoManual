---
symbol: "SLC6A11"
type: "gene"
col: 5280
ensembl_id: "ENSG00000132164"
name: "solute carrier family 6 member 11"
location: "3p25.3"
module: 128
arm: "+"
pooled_cpm: 2.25
n_lines_expressing: 15
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# SLC6A11

*solute carrier family 6 member 11* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.65× (z +12.9, q 1e-35, up in 1 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H23 0.0489×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H23 0.0795×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.0719×); [[Harringtonine (drug)]] 0.05 µM in 1 line (BT-474 0.0793×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.212×).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRKAR1B]] (+0.60, fdr 4e-04), [[ADGRB1]] (+0.57, fdr 6e-05), [[SRCIN1]] (+0.55, fdr 5e-04); moves opposite to [[ALDH6A1]] (-0.48, fdr 9e-05), [[PLAG1]] (-0.48, fdr 2e-04), [[ZNHIT1]] (-0.47, fdr 6e-05).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5280.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.65×** | +12.9 | 1e-35 | 1/6 (NCI-H2347) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.04×** | +12.2 | 7e-32 | 2/3 (NCI-H2347, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.88×** | +11.2 | 8e-27 | 1/3 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.73×** | +10.2 | 4e-22 | 2/3 (NCI-H2347, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.53×** | +6.5 | 7e-09 | 1/7 (NCI-H1573) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.89×** | +6.4 | 2e-08 | 5/9 (A549, NCI-H2347, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +6.2 | 4e-08 | 0/7 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +5.8 | 4e-07 | 1/7 (NCI-H2347) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.35×** | +5.8 | 4e-07 | 4/6 (NCI-H2347, C-33 A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.77×** | +5.7 | 6e-07 | 6/10 (NCI-H2347, C-33 A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.79×** | +5.2 | 1e-05 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +5.0 | 2e-05 | 1/7 (NCI-H2347) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.02×** | +5.0 | 3e-05 | 1/7 (A-427) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.92×** | +4.6 | 2e-04 | 0/7 | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.87×** | +4.4 | 4e-04 | 0/9 | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +4.4 | 5e-04 | 3/7 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +4.2 | 0.001 | 1/8 (NCI-H2347) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.007 | 1/8 (NCI-H2347) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **2.01×** | +3.5 | 0.011 | 0/7 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.61×** | +3.4 | 0.018 | 0/8 | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +3.3 | 0.019 | 3/7 (NCI-H2347, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.59×** | +3.3 | 0.021 | 0/7 | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.89×** | +3.2 | 0.028 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5280.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H23 0.0489×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H23 0.0795×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.0719×); [[Harringtonine (drug)]] 0.05 µM in 1 line (BT-474 0.0793×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.212×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.624× | -3.1 | 0.62 | 1/9 (A549) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.637× | -3.1 | 0.62 | 0/10 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5280. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 15.7 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0489× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.142× (z -9.7) |
| [[BT-474 (line)]] | alt | 20.6 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0719× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 43.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 3.81 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0715× (z -8.7) ⚠ transcription drop; unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +9.6) | — |
| [[A-172 (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.255 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.700 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.289 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.833 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.281 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.297 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.330 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.290 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.251 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.316 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.281 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.324 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.626 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.597 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.599 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.421 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.298 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5280), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 12 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKAR1B]] | +0.60 | +0.52 / +0.26 | both halves | 4e-04 | pathway: Neuronal System |
| [[ADGRB1]] | +0.57 | +0.50 / +0.39 | both halves | 6e-05 |  |
| [[SRCIN1]] | +0.55 | +0.70 / +0.24 | both halves | 5e-04 |  |
| [[TMEM52B]] | +0.55 | +0.57 / +0.20 | ⚠ one half (not replicated) | 7e-04 |  |
| [[CCDC169]] | +0.54 | +0.25 / +0.54 | both halves | 4e-04 |  |
| [[JPH3]] | +0.52 | +0.55 / +0.33 | both halves | 1e-04 |  |
| [[DANT1]] | +0.52 | +0.31 / +0.20 | both halves | 7e-04 |  |
| [[DGCR5]] | +0.52 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[LAMC3]] | +0.51 | +0.43 / +0.43 | both halves | 4e-05 |  |
| [[FAM184A]] | +0.51 | +0.33 / +0.38 | both halves | 1e-04 |  |
| [[MMRN1]] | +0.51 | +0.56 / +0.29 | both halves | 2e-04 |  |
| [[AGBL2]] | +0.50 | +0.39 / +0.36 | both halves | 1e-04 |  |
| [[HSF2BP]] | +0.50 | +0.35 / +0.39 | both halves | 1e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH6A1]] | -0.48 | -0.36 / -0.37 | both halves | 9e-05 | pathway: Metabolism of amino acids and derivatives |
| [[PLAG1]] | -0.48 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[ZNHIT1]] | -0.47 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[PMM1]] | -0.46 | -0.31 / -0.33 | both halves | 2e-04 |  |
| [[ACOT8]] | -0.45 | -0.41 / -0.28 | both halves | 3e-04 |  |
| [[ARL3]] | -0.44 | -0.26 / -0.23 | both halves | 5e-04 |  |
| [[DCTN3]] | -0.43 | -0.28 / -0.34 | both halves | 3e-04 |  |
| [[RAB40C]] | -0.43 | -0.32 / -0.34 | both halves | 1e-04 |  |
| [[TSC2]] | -0.43 | -0.36 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[ZER1]] | -0.43 | -0.25 / -0.37 | both halves | 4e-04 |  |
| [[KIAA0319L]] | -0.42 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[IFT122]] | -0.42 | -0.35 / -0.27 | both halves | 3e-04 |  |
| [[MMUT]] | -0.42 | -0.29 / -0.34 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC6A11's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.562). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.4, 37.0); signed map (25.3, 23.6). **Vector** length 24.6, 6.61% of its response variance represented; |z| ≥ 3 in 218 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +11.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.6 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +4.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +0.6 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.6 | +2.2 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -2.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | -0.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.6 | -0.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.5 | -1.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.5 | -2.3 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -0.4 | -1.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 6 member 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:10,816,201-10,940,714 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GAT3 |
| Gene groups (HGNC) | Solute carrier family 6 |
| Reactome | 9 pathways, smallest: Creatine metabolism; SLC-mediated transport of neurotransmitters; GABA synthesis, release, reuptake and degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P48066](https://www.uniprot.org/uniprotkb/P48066) (Sodium- and chloride-dependent GABA transporter 3):

> Mediates sodium- and chloride-dependent transport of gamma-aminobutyric acid (GABA). Can also mediate transport of beta-alanine and to a lower extent that of taurine and hypotaurine (By similarity).

**Summary**, from NCBI Gene [6538](https://www.ncbi.nlm.nih.gov/gene/6538):

> The protein encoded by this gene is a sodium-dependent transporter that uptakes gamma-aminobutyric acid (GABA), an inhibitory neurotransmitter, which ends the GABA neurotransmission. Defects in this gene may result in epilepsy, behavioral problems, or intellectual problems. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:11044](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11044) · Entrez [6538](https://www.ncbi.nlm.nih.gov/gene/6538) · UniProt [P48066](https://www.uniprot.org/uniprotkb/P48066) · Ensembl [ENSG00000132164](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132164)

## Data

Gene col 5280: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5280); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5280, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5280]; `tensor/DDL_lfc|DDL_z.npy` [5280]; `embed/gene_vectors.npy` [5280]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5280 or target_col == 5280). Every well: [[SLC6A11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC6A11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
