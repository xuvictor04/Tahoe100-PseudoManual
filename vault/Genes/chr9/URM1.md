---
symbol: "URM1"
type: "gene"
col: 9422
ensembl_id: "ENSG00000167118"
name: "ubiquitin related modifier 1"
location: "9q34.11"
module: 15
arm: "+"
pooled_cpm: 24.49
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# URM1

*ubiquitin related modifier 1* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.07× (z +17.2, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.699× (z -8.5, q 1e-14, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB8OS]] (+0.73, fdr 1e-05), [[PCF11-AS1]] (+0.71, fdr 1e-05), [[TAF11]] (+0.70, fdr 7e-06); moves opposite to [[SSX2IP]] (-0.63, fdr 1e-05), [[THEM6]] (-0.58, fdr 6e-05), [[HLTF]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9422.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +17.2 | 0e+00 | 44/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +9.1 | 3e-17 | 31/43 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +8.4 | 9e-15 | 34/46 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +7.2 | 6e-11 | 27/38 (A-172, C32, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +6.9 | 4e-10 | 31/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +6.8 | 1e-09 | 28/47 (SK-MEL-2, SHP-77, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +6.5 | 5e-09 | 21/34 (A498, LoVo, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +5.5 | 2e-06 | 24/47 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.1 | 2e-05 | 24/48 (A-172, HT-29, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.6 | 2e-04 | 23/46 (RKO, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +4.6 | 3e-04 | 23/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +4.4 | 5e-04 | 19/48 (SK-MEL-2, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +4.4 | 5e-04 | 22/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +4.0 | 0.003 | 16/46 (NCI-H1573, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.004 | 18/46 (AN3 CA, HT-29, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.009 | 14/45 (NCI-H460, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.018 | 14/48 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.026 | 9/46 (A549, H4, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.059 | 8/48 (PANC-1, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9422.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.699×** | -8.5 | 1e-14 | 39/48 (A498, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.689×** | -6.2 | 1e-07 | 33/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.737×** | -5.1 | 6e-05 | 25/47 (LOX-IMVI, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.748×** | -4.9 | 2e-04 | 25/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.766×** | -4.5 | 8e-04 | 19/47 (PANC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.870× | -3.3 | 0.083 | 21/47 (A-427, J82, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.825×** | -3.2 | 0.100 | 14/48 (LOX-IMVI, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Decitabine (drug)]] 5 µM |  | 0.829× | -3.0 | 0.18 | 8/47 (LoVo, HCT15, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9422. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 29.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +12.1) | — |
| [[A-427 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 29.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.7) | — |
| [[A549 (line)]] | wt | 27.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 13.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 42.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.2) | — |
| [[C32 (line)]] | wt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.102× (z -15.0) ⚠ transcription drop; cell-cycle shift, explains ~51% of this change |
| [[CHP-212 (line)]] | wt | 29.1 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0796× (z -10.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HepG2_C3A (line)]] | wt | 19.0 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0705× (z -13.7) |
| [[HS-578T (line)]] | alt | 19.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +10.3) | — |
| [[LoVo (line)]] | wt | 17.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 16.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 26.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 25.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 18.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +12.1) | — |
| [[RKO (line)]] | wt | 54.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 25.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 31.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9422), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB8OS]] | +0.73 | +0.68 / +0.53 | both halves | 1e-05 | pathway: tRNA processing |
| [[PCF11-AS1]] | +0.71 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TAF11]] | +0.70 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[ANKRD42-DT]] | +0.69 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[WDR20]] | +0.69 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[DCTN5]] | +0.67 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[GPALPP1]] | +0.66 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ZNF460-AS1]] | +0.65 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[SLC25A53]] | +0.64 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[DENND6A-AS1]] | +0.63 | +0.37 / +0.54 | both halves | 8e-05 |  |
| [[LRRC41]] | +0.62 | +0.38 / +0.62 | both halves | 7e-05 |  |
| [[CAPN10-DT]] | +0.61 | +0.46 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSX2IP]] | -0.63 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[THEM6]] | -0.58 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[HLTF]] | -0.56 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[LMCD1]] | -0.54 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[NR4A1]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ZNF184]] | -0.53 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[PLS1]] | -0.52 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[PHF6]] | -0.52 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises URM1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises URM1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.714). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.4, 23.7); signed map (-0.1, -1.5). **Vector** length 78.3, 15.6% of its response variance represented; |z| ≥ 3 in 803 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.0 | +17.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +4.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +5.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.5 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +6.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +3.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.0 | +3.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -8.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.3 | +0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.3 | -6.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.2 | -5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | +0.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -0.8 |
|  | [[Pimozide (drug)]] 5 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin related modifier 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,371,361-128,392,016 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2668; previously C9orf74 |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTM9](https://www.uniprot.org/uniprotkb/Q9BTM9) (Ubiquitin-related modifier 1):

> Acts as a sulfur carrier required for 2-thiolation of mcm(5)S(2)U at tRNA wobble positions of cytosolic tRNA(Lys), tRNA(Glu) and tRNA(Gln). Serves as sulfur donor in tRNA 2-thiolation reaction by being thiocarboxylated (-COSH) at its C-terminus by MOCS3. The sulfur is then transferred to tRNA to form 2-thiolation of mcm(5)S(2)U. Also acts as a ubiquitin-like protein (UBL) that is covalently conjugated via an isopeptide bond to lysine residues of target proteins such as MOCS3, ATPBD3, CTU2, …

**Summary**, from NCBI Gene [81605](https://www.ncbi.nlm.nih.gov/gene/81605):

> Enables sulfur carrier activity. Involved in tRNA thio-modification and tRNA wobble uridine modification. Predicted to be located in cytosol. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28378](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28378) · Entrez [81605](https://www.ncbi.nlm.nih.gov/gene/81605) · UniProt [Q9BTM9](https://www.uniprot.org/uniprotkb/Q9BTM9) · Ensembl [ENSG00000167118](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167118)

## Data

Gene col 9422: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9422); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9422, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9422]; `tensor/DDL_lfc|DDL_z.npy` [9422]; `embed/gene_vectors.npy` [9422]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9422 or target_col == 9422). Every well: [[URM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/URM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
