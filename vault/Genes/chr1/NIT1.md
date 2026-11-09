---
symbol: "NIT1"
type: "gene"
col: 8191
ensembl_id: "ENSG00000158793"
name: "nitrilase 1"
location: "1q23.3"
module: 227
arm: "+"
pooled_cpm: 15.68
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 10
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/227"]
generated_by: "tahoemap"
---

# NIT1

*nitrilase 1* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.49× (z +10.0, q 1e-20, up in 33 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.401× (z -8.4, q 3e-14, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERN1]] (+0.64, fdr 1e-05), [[LUCAT1]] (+0.63, fdr 7e-06), [[STK40]] (+0.61, fdr 1e-05); moves opposite to [[KCTD3]] (-0.57, fdr 3e-05), [[GTF2I]] (-0.54, fdr 3e-05), [[SMAD6]] (-0.54, fdr 3e-05).
> It is in [[Module 227]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Bendamustine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8191.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +10.0 | 1e-20 | 33/45 (AsPC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +8.6 | 2e-15 | 34/47 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +8.4 | 7e-15 | 31/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +7.7 | 1e-12 | 28/47 (MIA PaCa-2, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +7.2 | 6e-11 | 15/29 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +6.6 | 4e-09 | 22/47 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.40×** | +6.0 | 2e-07 | 23/47 (MIA PaCa-2, LS 180, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.5 | 3e-06 | 21/45 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +4.9 | 5e-05 | 15/47 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.33×** | +4.9 | 6e-05 | 18/45 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.002 | 11/44 (NCI-H2030, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.47×** | +3.9 | 0.004 | 7/43 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.006 | 8/42 (HOP62, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.006 | 9/45 (LS 180, SW480, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.23×** | +3.6 | 0.010 | 13/38 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.010 | 16/47 (NCI-H460, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.013 | 6/42 (Hs 766T, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8191.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.401×** | -8.4 | 3e-14 | 31/43 (A-427, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.752×** | -7.1 | 4e-10 | 25/47 (SNU-423, NCI-H460, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.478×** | -6.8 | 2e-09 | 28/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.681×** | -6.7 | 2e-09 | 23/47 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.691×** | -6.5 | 9e-09 | 23/46 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.746×** | -5.2 | 2e-05 | 18/46 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.756×** | -4.9 | 7e-05 | 17/47 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.810×** | -3.7 | 0.015 | 12/48 (NCI-H2030, H4, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.813×** | -3.6 | 0.017 | 12/46 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.692×** | -3.4 | 0.041 | 8/22 (HOP62, PANC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8191. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 18.4 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.347× (z -9.4) |
| [[A-427 (line)]] | wt | 19.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -11.9) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0816× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0617× (z -15.1) ⚠ transcription drop |
| [[H4 (line)]] | wt | 16.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.112× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 8.00 | 0 | 1 | — | [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.0836× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -9.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 12.0 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0386× (z -9.2) |
| [[SNU-423 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -9.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8191), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERN1]] | +0.64 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[LUCAT1]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[STK40]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[TPT1-AS1]] | +0.59 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[GTPBP2]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[RELL2]] | +0.59 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[RBCK1]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[UPP1]] | +0.58 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[GPATCH2L]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[KCTD5]] | +0.57 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[PTPRH]] | +0.57 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[MAP1LC3B]] | +0.56 | +0.54 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD3]] | -0.57 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[GTF2I]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[SMAD6]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[DHX9]] | -0.53 | -0.37 / -0.57 | both halves | 7e-05 |  |
| [[ALDH7A1]] | -0.53 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[HNRNPR]] | -0.52 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[ZZZ3]] | -0.52 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[DHRS4L2]] | -0.52 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[NFIA]] | -0.52 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[HADH]] | -0.51 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[TNS3]] | -0.51 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[DUT]] | -0.50 | -0.45 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bendamustine (drug)]] 0.5 µM | C | NIT1's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | NIT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.59 | 0.474 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 227]]; 9 genes; every member is in the + arm (projection on the module's main direction 0.811). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.8, -6.2); signed map (-1.3, 31.0). **Vector** length 77.3, 14.3% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.9 | +7.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.7 | +6.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.6 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.2 | +4.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.1 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.0 | -7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -8.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -2.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | nitrilase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:161,118,086-161,125,445 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86X76](https://www.uniprot.org/uniprotkb/Q86X76) (Deaminated glutathione amidase):

> Catalyzes the hydrolysis of the amide bond in N-(4-oxoglutarate)-L-cysteinylglycine (deaminated glutathione), a metabolite repair reaction to dispose of the harmful deaminated glutathione. Plays a role in cell growth and apoptosis: loss of expression promotes cell growth, resistance to DNA damage stress and increased incidence to NMBA-induced tumors. Has tumor suppressor properties that enhances the apoptotic responsiveness in cancer cells; this effect is additive to the tumor suppressor …

**Summary**, from NCBI Gene [4817](https://www.ncbi.nlm.nih.gov/gene/4817):

> This gene encodes a member of the nitrilase protein family with homology to bacterial and plant nitrilases, enzymes that cleave nitriles and organic amides to the corresponding carboxylic acids plus ammonia. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:7828](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7828) · Entrez [4817](https://www.ncbi.nlm.nih.gov/gene/4817) · UniProt [Q86X76](https://www.uniprot.org/uniprotkb/Q86X76) · Ensembl [ENSG00000158793](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158793)

## Data

Gene col 8191: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8191); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8191, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8191]; `tensor/DDL_lfc|DDL_z.npy` [8191]; `embed/gene_vectors.npy` [8191]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8191 or target_col == 8191). Every well: [[NIT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
