---
symbol: "FAM156A"
type: "gene"
col: 15596
ensembl_id: "ENSG00000268350"
name: "family with sequence similarity 156 member A"
location: "Xp11.22"
module: 216
arm: "+"
pooled_cpm: 8.41
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/216"]
generated_by: "tahoemap"
---

# FAM156A

*family with sequence similarity 156 member A* — Xp11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.37× (z +6.3, q 1e-07, up in 22 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.369× (z -14.0, q 5e-42, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DRD4]] (+0.53, fdr 9e-05), [[KIAA0319L]] (+0.53, fdr 2e-05), [[NOXRED1]] (+0.53, fdr 3e-05); moves opposite to [[RFK]] (-0.62, fdr 2e-04), [[NEO1]] (-0.56, fdr 8e-05), [[ENPP4]] (-0.54, fdr 3e-05).
> It is in [[Module 216]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MECOM]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PAAF1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15596.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.3 | 1e-07 | 22/41 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +6.1 | 3e-07 | 19/46 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +5.2 | 3e-05 | 14/45 (HT-29, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.36×** | +4.3 | 0.002 | 4/47 (SW480, NCI-H460, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.005 | 9/44 (NCI-H460, J82, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.012 | 8/46 (SNU-423, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.012 | 6/45 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +3.8 | 0.012 | 10/44 (A-172, NCI-H460, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.046 | 11/44 (A-427, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15596.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.369×** | -14.0 | 5e-42 | 39/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.413×** | -12.4 | 5e-33 | 30/43 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.454×** | -10.7 | 2e-24 | 29/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.450×** | -8.8 | 2e-16 | 23/36 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.490×** | -7.9 | 4e-13 | 26/45 (PANC-1, LOX-IMVI, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.589×** | -7.2 | 7e-11 | 26/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.691×** | -5.2 | 1e-05 | 17/46 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.691×** | -5.2 | 1e-05 | 15/45 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.736×** | -4.3 | 0.001 | 15/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.778×** | -3.5 | 0.024 | 14/45 (SW480, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.628×** | -3.4 | 0.032 | 11/45 (HepG2/C3A, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.847× | -3.3 | 0.048 | 3/46 (COLO 205, SW1417, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.855× | -3.1 | 0.082 | 10/46 (MIA PaCa-2, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15596. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 21.4 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.152× (z -16.6) |
| [[A-172 (line)]] | wt | 13.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -12.2) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 11.1 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0547× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.144× (z -13.1) |
| [[PANC-1 (line)]] | alt | 9.87 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -11.6) |
| [[Hs 766T (line)]] | wt | 13.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0735× (z -9.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 13.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -10.3) |
| [[LS 180 (line)]] | wt | 5.67 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 9.45 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0895× (z -10.0) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 9.21 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 15.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.185× (z -8.5) |
| [[SNU-1 (line)]] | wt | 7.64 | 0 | 1 | — | [[Clofarabine (drug)]] 0.05 µM 0.0561× (z -9.1) |
| [[SNU-423 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 9.07 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -9.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15596), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRD4]] | +0.53 | +0.37 / +0.64 | both halves | 9e-05 |  |
| [[KIAA0319L]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[NOXRED1]] | +0.53 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[ACAD10]] | +0.49 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[BMS1P4-1]] | +0.49 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[FBXL9P]] | +0.49 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[AGAP5]] | +0.49 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[ISY1]] | +0.48 | +0.36 / +0.50 | both halves | 9e-05 |  |
| [[DNHD1]] | +0.48 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[UBAP1L]] | +0.48 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[PPOX]] | +0.47 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[TRMT44]] | +0.47 | +0.37 / +0.40 | both halves | 8e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFK]] | -0.62 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[NEO1]] | -0.56 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[ENPP4]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[GPR37]] | -0.51 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[RAB27B]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[TP53I11]] | -0.50 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[INPP4B]] | -0.50 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[MARCKSL1]] | -0.48 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[AMOT]] | -0.48 | -0.25 / -0.52 | both halves | 4e-04 |  |
| [[MECOM]] | -0.47 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ABLIM1]] | -0.47 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[TBC1D1]] | -0.47 | -0.51 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MECOM]] | B | MECOM activity lowers FAM156A's level | lines that do not express MECOM (18) vs lines expressing it (32) | 1.50× higher at baseline in the lines without MECOM | 0.048 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |
| [[DRD4]] | B | DRD4 activity raises FAM156A's level | lines that do not express DRD4 (5) vs lines expressing it (45) | 1.68× lower at baseline in the lines without DRD4 | 0.085 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PRSS12]] | B | PRSS12 activity lowers FAM156A's level | lines that do not express PRSS12 (19) vs lines expressing it (31) | 1.32× higher at baseline in the lines without PRSS12 | 0.088 | ⚠ within organs, on part of the lines; also absent: MOXD1, TLL1, ENSG00000289884 |
| [[HDAC6]] | B | HDAC6 activity lowers FAM156A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAAF1]] | C | FAM156A's natural level strengthens PAAF1's drug response | FAM156A's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.43; direction not clear | 0.055 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 216]]; 12 genes; every member is in the + arm (projection on the module's main direction -0.583). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.6, 36.9); signed map (-17.2, 0.8). **Vector** length 49.1, 6.10% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.1 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -1.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.2 | +2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.1 | +1.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +0.9 | +4.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -1.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.4 | -12.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -14.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.1 | -7.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | +0.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.0 | -0.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -0.7 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 156 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.22 — chrX:52,926,402-52,995,472 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRO0659; previously TMEM29 |
| Gene groups (HGNC) | Proteins encoded by multiple genes |
| Matched by | ensembl_id |

UniProt [Q8NDB6](https://www.uniprot.org/uniprotkb/Q8NDB6) carries no function annotation.

**Summary**, from NCBI Gene [29057](https://www.ncbi.nlm.nih.gov/gene/29057):

> Located in nuclear envelope. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30114](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30114) · Entrez [29057](https://www.ncbi.nlm.nih.gov/gene/29057) · UniProt [Q8NDB6](https://www.uniprot.org/uniprotkb/Q8NDB6) · Ensembl [ENSG00000268350](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000268350)

## Data

Gene col 15596: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15596); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15596, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15596]; `tensor/DDL_lfc|DDL_z.npy` [15596]; `embed/gene_vectors.npy` [15596]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15596 or target_col == 15596). Every well: [[FAM156A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM156A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
