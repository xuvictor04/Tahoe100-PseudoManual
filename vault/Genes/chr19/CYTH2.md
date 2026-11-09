---
symbol: "CYTH2"
type: "gene"
col: 2605
ensembl_id: "ENSG00000105443"
name: "cytohesin 2"
location: "19q13.33"
module: 190
arm: "+"
pooled_cpm: 44.36
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 24
n_dd_up_clean: 6
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/190"]
generated_by: "tahoemap"
---

# CYTH2

*cytohesin 2* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.39× (z +6.0, q 8e-07, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.479× (z -11.7, q 4e-29, down in 44 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.722× (z -8.4, q 1e-14, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OTUD5]] (+0.72, fdr 7e-06), [[CACTIN]] (+0.63, fdr 1e-05), [[DMWD]] (+0.63, fdr 1e-05); moves opposite to [[MTX2]] (-0.63, fdr 1e-05), [[TPD52L1]] (-0.61, fdr 1e-05), [[STEAP2]] (-0.61, fdr 1e-05).
> It is in [[Module 190]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2605.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +6.0 | 8e-07 | 32/48 (SW1417, SNU-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +5.4 | 2e-05 | 27/48 (LS 180, SNU-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.8 | 3e-04 | 24/47 (BT-474, SW1417, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +4.7 | 4e-04 | 25/49 (COLO 205, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.6 | 5e-04 | 21/48 (MIA PaCa-2, KATO III, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.17× | +4.1 | 0.003 | 18/48 (SW1417, A498, …) | top dose only | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.006 | 22/47 (LoVo, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.22×** | +3.5 | 0.034 | 17/47 (NCI-H2030, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **1.21×** | +3.5 | 0.034 | 21/48 (SW1417, KATO III, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.067 | 17/48 (KATO III, NCI-H1573, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.073 | 11/48 (Hs 766T, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.094 | 10/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.1 | 0.094 | 12/48 (HS-578T, J82, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.0 | 0.094 | 10/42 (NCI-H460, SNU-423, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2605.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.479×** | -11.7 | 4e-29 | 44/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.722×** | -8.4 | 1e-14 | 42/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.634×** | -8.3 | 2e-14 | 38/48 (LOX-IMVI, C32, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.642×** | -8.1 | 1e-13 | 35/48 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.657×** | -7.7 | 2e-12 | 37/48 (hTERT-HPNE, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.743×** | -7.6 | 2e-12 | 32/48 (J82, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.660×** | -7.6 | 3e-12 | 33/48 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.504×** | -6.5 | 5e-09 | 39/49 (AsPC-1, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.521×** | -6.2 | 3e-08 | 31/47 (SNU-1, RKO, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.524×** | -6.2 | 4e-08 | 35/47 (NCI-H1792, SNU-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.539×** | -5.9 | 2e-07 | 32/48 (RPMI-7951, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.553×** | -5.6 | 8e-07 | 29/47 (AsPC-1, NCI-H1792, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.578×** | -5.2 | 8e-06 | 28/48 (AsPC-1, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.758×** | -5.0 | 2e-05 | 27/48 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.705×** | -4.5 | 2e-04 | 25/48 (NCI-H1792, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.788×** | -4.2 | 0.001 | 22/47 (SNU-1, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2605. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 55.6 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.263× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 49.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.70× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.372× (z -9.0) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 33.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 64.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 58.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.296× (z -10.0) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 58.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.361× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 48.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.215× (z -11.9) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 49.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.332× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 31.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.280× (z -10.6) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 45.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.261× (z -9.4) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 62.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 43.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2605), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OTUD5]] | +0.72 | +0.61 / +0.77 | both halves | 7e-06 |  |
| [[CACTIN]] | +0.63 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[DMWD]] | +0.63 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[SP2]] | +0.62 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[RGL2]] | +0.61 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[ZFTRAF1]] | +0.60 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[ZNF324]] | +0.59 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[ADGRL1-AS1]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[TEPSIN]] | +0.57 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[FBRS]] | +0.57 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[RAB11B-AS1]] | +0.57 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[DMPK]] | +0.56 | +0.58 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTX2]] | -0.63 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[TPD52L1]] | -0.61 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[STEAP2]] | -0.61 | -0.49 / -0.69 | both halves | 1e-05 |  |
| [[SLC18B1]] | -0.58 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[MRPS35]] | -0.58 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[OTUD6B]] | -0.57 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[UBA5]] | -0.56 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[PPAT]] | -0.56 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[SLC25A12]] | -0.56 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[SNRPA1]] | -0.56 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[TMEM182]] | -0.55 | -0.32 / -0.62 | both halves | 2e-04 |  |
| [[FIP1L1]] | -0.55 | -0.51 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises CYTH2's level | compounds that target MAP2K1: 3 of 4 lower it (Cobimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 190]]; 18 genes; every member is in the + arm (projection on the module's main direction -0.630). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.2, -22.4); signed map (2.0, -7.5). **Vector** length 115, 29.8% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.5 | +4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +4.0 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.4 | +2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.4 | +2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +0.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.7 | +1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.7 | -11.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.4 | -8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.9 | -7.7 |
|  | [[EX229 (drug)]] 5 µM |  | -5.1 | -5.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.0 | -6.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.9 | -5.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.9 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | cytohesin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,469,208-48,482,314 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CTS18.1, Sec7p-L, ARNO, Sec7p-like, cytohesin-2; previously PSCD2L, PSCD2 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Cytohesins |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 4 pathways, smallest: Intra-Golgi traffic; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99418](https://www.uniprot.org/uniprotkb/Q99418) (Cytohesin-2):

> Acts as a guanine-nucleotide exchange factor (GEF). Promotes guanine-nucleotide exchange on ARF1, ARF3 and ARF6. Activates ARF factors through replacement of GDP with GTP (By similarity). The cell membrane form, in association with ARL4 proteins, recruits ARF6 to the plasma membrane. Involved in neurite growth (By similarity).

**Summary**, from NCBI Gene [9266](https://www.ncbi.nlm.nih.gov/gene/9266):

> The protein encoded by this gene is a member of the PSCD family. Members of this family have identical structural organization that consists of an N-terminal coiled-coil motif, a central Sec7 domain, and a C-terminal pleckstrin homology (PH) domain. The coiled-coil motif is involved in homodimerization, the Sec7 domain contains guanine-nucleotide exchange protein (GEP) activity, and the PH domain interacts with phospholipids and is responsible for association of PSCDs with membranes. Members of …

**Accessions** — [HGNC:9502](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9502) · Entrez [9266](https://www.ncbi.nlm.nih.gov/gene/9266) · UniProt [Q99418](https://www.uniprot.org/uniprotkb/Q99418) · Ensembl [ENSG00000105443](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105443)

## Data

Gene col 2605: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2605); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2605, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2605]; `tensor/DDL_lfc|DDL_z.npy` [2605]; `embed/gene_vectors.npy` [2605]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2605 or target_col == 2605). Every well: [[CYTH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYTH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
