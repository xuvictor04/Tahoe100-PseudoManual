---
symbol: "TPTE2P6"
type: "gene"
col: 13016
ensembl_id: "ENSG00000205822"
name: "TPTE2 pseudogene 6"
location: "13q12.12"
module: 75
arm: "+"
pooled_cpm: 11.24
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# TPTE2P6

*TPTE2 pseudogene 6* — 13q12.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.00× (z +17.9, q 0e+00, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.647× (z -8.0, q 1e-12, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTN]] (+0.78, fdr 7e-06), [[PSMD14-DT]] (+0.75, fdr 7e-06), [[EYS]] (+0.75, fdr 7e-06); moves opposite to [[SLC39A3]] (-0.64, fdr 4e-05), [[NAA40]] (-0.62, fdr 3e-05), [[STUB1]] (-0.59, fdr 0.001, ⚠ one half only (not replicated)).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF341-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13016.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +17.9 | 0e+00 | 40/44 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +12.8 | 9e-35 | 19/23 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +11.2 | 8e-27 | 22/34 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +10.8 | 3e-25 | 18/30 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.23×** | +5.4 | 6e-06 | 20/46 (LOX-IMVI, LoVo, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.8 | 1e-04 | 15/43 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.41×** | +4.4 | 7e-04 | 3/45 (SW480, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +4.3 | 0.001 | 10/46 (BT-474, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.8 | 0.009 | 13/45 (NCI-H2030, SW48, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.011 | 13/44 (LOX-IMVI, C32, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.021 | 1/42 (BT-474) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.022 | 8/44 (A-172, A498, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~9% of this change | **1.20×** | +3.4 | 0.030 | 14/41 (HS-578T, AsPC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Bicalutamide (drug)]] 0.5 µM |  | **1.20×** | +3.3 | 0.033 | 2/46 (C32, Panc 03.27) | inconsistent across doses | position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.20× | +3.3 | 0.037 | 6/47 (RPMI-7951, C32, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.043 | 5/45 (SNU-1, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Tranilast (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.043 | 2/45 (C32, HCT15) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.049 | 2/45 (LS 180, PANC-1) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.060 | 3/47 (AsPC-1, HepG2/C3A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13016.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.647×** | -8.0 | 1e-12 | 25/47 (COLO 205, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.886× | -7.8 | 2e-12 | 9/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.698×** | -6.6 | 9e-09 | 22/47 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.709×** | -6.3 | 5e-08 | 20/47 (AsPC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.735×** | -5.6 | 2e-06 | 18/47 (Hs 766T, A-427, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.753×** | -5.2 | 2e-05 | 14/47 (HT-29, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.766×** | -4.9 | 8e-05 | 18/44 (HepG2/C3A, C-33 A, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.835× | -3.1 | 0.12 | 8/45 (SK-MEL-2, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.835× | -3.1 | 0.14 | 6/47 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.848× | -3.0 | 0.14 | 7/47 (LOX-IMVI, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13016. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 9.39 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +9.9) ⚠ cell-cycle shift, explains ~13% of this change | [[Digitoxin (drug)]] 0.5 µM 0.212× (z -8.7) ⚠ cell-cycle shift, explains ~5% of this change |
| [[A-427 (line)]] | wt | 6.55 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.140× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 9.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +8.5) | — |
| [[C32 (line)]] | wt | 13.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +10.1) | — |
| [[J82 (line)]] | alt | 9.52 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.210× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -9.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 12.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.0) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 13.4 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0746× (z -10.9) |
| [[SW480 (line)]] | alt | 11.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.01× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13016), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTN]] | +0.78 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[PSMD14-DT]] | +0.75 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[EYS]] | +0.75 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[PLCG1-AS1]] | +0.75 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[C2CD5-AS1]] | +0.72 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[LINC01090]] | +0.72 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[CHMP3-AS1]] | +0.72 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[DLEU7]] | +0.72 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[SYNM-AS1]] | +0.70 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[LHFPL3]] | +0.69 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[EHBP1-AS1]] | +0.68 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[CTDSPL2-DT]] | +0.68 | +0.62 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC39A3]] | -0.64 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[NAA40]] | -0.62 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[STUB1]] | -0.59 | -0.57 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity raises TPTE2P6's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.34× lower at baseline in the lines without ZNF341-AS1 | 0.042 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises TPTE2P6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.9, 24.5); signed map (31.9, 1.9). **Vector** length 65.6, 9.85% of its response variance represented; |z| ≥ 3 in 819 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +17.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +5.8 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.4 | +0.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.7 | -7.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -5.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.5 | -6.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.5 | -4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.1 | -6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.1 | -1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | TPTE2 pseudogene 6 |
| Locus type | pseudogene |
| Location | 13q12.12 — chr13:24,408,157-24,597,660 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42644](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42644) · Entrez [374491](https://www.ncbi.nlm.nih.gov/gene/374491) · Ensembl [ENSG00000205822](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205822)

## Data

Gene col 13016: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13016); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13016, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13016]; `tensor/DDL_lfc|DDL_z.npy` [13016]; `embed/gene_vectors.npy` [13016]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13016 or target_col == 13016). Every well: [[TPTE2P6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPTE2P6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
