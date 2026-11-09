---
symbol: "LAMB2P1"
type: "gene"
col: 15663
ensembl_id: "ENSG00000270441"
name: "laminin subunit beta 2 pseudogene 1"
location: "3p21.31"
module: 114
arm: "+"
pooled_cpm: 5.1
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# LAMB2P1

*laminin subunit beta 2 pseudogene 1* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 1.58× (z +4.6, q 0.002, up in 14 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 5.60×).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.484× (z -7.3, q 2e-10, down in 28 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.524× (z -6.5, q 2e-08, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NR1H3]] (+0.73, fdr 7e-06), [[ZNF586]] (+0.65, fdr 1e-05), [[CHRNE]] (+0.65, fdr 7e-06); moves opposite to [[ADAM15]] (-0.59, fdr 3e-05), [[NAGA]] (-0.56, fdr 1e-05), [[TMX1]] (-0.55, fdr 1e-05).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC02609]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15663.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 5.60×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.58×** | +4.6 | 0.002 | 14/47 (SW480, KATO III, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.8 | 0.049 | 11/28 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | 1.26× | +3.3 | 0.21 | 17/39 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | 1.35× | +3.0 | 0.36 | 3/47 (A498, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15663.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.484×** | -7.3 | 2e-10 | 28/47 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.505×** | -6.8 | 2e-09 | 21/39 (NCI-H460, SW1417, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.524×** | -6.5 | 2e-08 | 24/47 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.320×** | -6.0 | 4e-07 | 27/42 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.559×** | -5.8 | 7e-07 | 20/44 (KATO III, PANC-1, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.562×** | -5.8 | 8e-07 | 23/45 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.553×** | -5.7 | 1e-06 | 23/33 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.387×** | -5.0 | 5e-05 | 19/39 (HEC-1-A, CFPAC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.610×** | -4.8 | 1e-04 | 17/44 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.623×** | -4.7 | 1e-04 | 18/45 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.647×** | -4.4 | 7e-04 | 14/47 (NCI-H1792, RKO, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.645×** | -4.2 | 0.001 | 15/44 (HS-578T, J82, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.696×** | -3.6 | 0.013 | 12/46 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.701×** | -3.5 | 0.016 | 14/47 (NCI-H23, HT-29, …) | top dose only |  |
| [[Auranofin (drug)]] 0.5 µM |  | **0.710×** | -3.4 | 0.024 | 13/44 (hTERT-HPNE, PANC-1, …) | inconsistent across doses |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.721×** | -3.3 | 0.038 | 8/46 (HOP62, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.710×** | -3.2 | 0.039 | 12/43 (SK-MEL-2, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM |  | **0.706×** | -3.2 | 0.039 | 9/41 (C32, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15663. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 5.26 | 0 | 3 (2 ⚠) | — | [[Oxaprozin (drug)]] 0.05 µM 0.0523× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 4.63 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0555× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 6.65 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.176× (z -9.8) ⚠ cell-cycle shift, explains ~46% of this change |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0901× (z -8.5) ⚠ cell-cycle shift, explains ~52% of this change |
| [[CFPAC-1 (line)]] | alt | 3.33 | 0 | 1 | — | [[Peretinoin (drug)]] 5 µM 0.0917× (z -8.6) |
| [[H4 (line)]] | wt | 6.09 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0396× (z -9.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 15.0 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0531× (z -9.4) |
| [[HOP62 (line)]] | alt | 6.36 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0804× (z -11.1) ⚠ cell-cycle shift, explains ~48% of this change |
| [[KATO III (line)]] | alt | 3.81 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0782× (z -8.5) |
| [[LoVo (line)]] | wt | 7.23 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H1573 (line)]] | alt | 5.27 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0490× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 5.66 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0464× (z -11.2) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 3.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 3.61 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 4.03 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.102× (z -10.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15663), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR1H3]] | +0.73 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[ZNF586]] | +0.65 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[CHRNE]] | +0.65 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[LINC01772]] | +0.64 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[ZNF226]] | +0.63 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[MTERF4]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[ZNF721]] | +0.62 | +0.65 / +0.57 | both halves | 8e-06 |  |
| [[CDKL3]] | +0.62 | +0.77 / +0.51 | both halves | 1e-05 |  |
| [[TMEM91]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[BMS1P4-1]] | +0.61 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[C19orf18]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ZNF271P]] | +0.61 | +0.68 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM15]] | -0.59 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[NAGA]] | -0.56 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[TMX1]] | -0.55 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[AP2M1]] | -0.55 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[SLC25A39]] | -0.55 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[PRPS1]] | -0.54 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[PGRMC1]] | -0.53 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[YWHAQ]] | -0.53 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[DPY19L1]] | -0.53 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[MYH10]] | -0.52 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[CNPY3]] | -0.52 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[PABIR2]] | -0.52 | -0.62 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02609]] | B | LINC02609 activity raises LAMB2P1's level | lines that do not express LINC02609 (6) vs lines expressing it (44) | 1.47× lower at baseline in the lines without LINC02609 | 0.013 | ⚠ within organs, on part of the lines; also absent: TPST1, HLTF, FERMT2; maybe low, not absent |
| [[MYH10]] | B | MYH10 activity raises LAMB2P1's level | lines that do not express MYH10 (10) vs lines expressing it (40) | 1.36× lower at baseline in the lines without MYH10 | 0.042 | ⚠ within organs, on part of the lines; also absent: MAPT, MOCS1, GAMT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.1, 26.8); signed map (2.8, -3.1). **Vector** length 58.8, 8.31% of its response variance represented; |z| ≥ 3 in 961 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +4.6 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +1.4 | +1.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | +1.1 | +2.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +1.1 | +1.6 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +1.0 | +2.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | -3.3 | -5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.5 | -1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -2.0 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -5.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.3 | -2.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | laminin subunit beta 2 pseudogene 1 |
| Locus type | pseudogene |
| Location | 3p21.31 — chr3:49,140,086-49,160,851 (-) |
| Ensembl biotype | unprocessed_pseudogene |
| Also known as | ; previously LAMB2L |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:6488](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6488) · Entrez [22973](https://www.ncbi.nlm.nih.gov/gene/22973) · Ensembl [ENSG00000270441](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000270441)

## Data

Gene col 15663: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15663); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15663, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15663]; `tensor/DDL_lfc|DDL_z.npy` [15663]; `embed/gene_vectors.npy` [15663]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15663 or target_col == 15663). Every well: [[LAMB2P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMB2P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
