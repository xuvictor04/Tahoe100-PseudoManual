---
symbol: "LIMD2"
type: "gene"
col: 5870
ensembl_id: "ENSG00000136490"
name: "LIM domain containing 2"
location: "17q23.3"
module: 92
arm: "+"
pooled_cpm: 3.16
n_lines_expressing: 44
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 7
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# LIMD2

*LIM domain containing 2* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.58× (z +10.4, q 2e-22, up in 6 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.62× (z +5.8, q 2e-06, up in 13 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.479× (z -6.2, q 3e-07, down in 22 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ROBO3]] (+0.58, fdr 9e-05), [[CMTM3]] (+0.57, fdr 2e-05), [[KIAA1614]] (+0.55, fdr 2e-04); moves opposite to [[MPHOSPH9]] (-0.45, fdr 2e-04), [[ALDH18A1]] (-0.45, fdr 5e-05), [[SEPTIN7P14]] (-0.43, fdr 2e-04).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TRBC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5870.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.58×** | +10.4 | 2e-22 | 6/7 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.76×** | +8.6 | 2e-15 | 14/17 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +5.8 | 2e-06 | 13/41 (HOP62, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +5.5 | 6e-06 | 5/9 (CFPAC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.68×** | +4.4 | 0.001 | 6/27 (Panc 03.27, NCI-H2347, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.84×** | +3.6 | 0.034 | 2/13 (J82, Panc 03.27) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.034 | 4/37 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.83×** | +3.5 | 0.034 | 5/30 (C-33 A, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.78×** | +3.4 | 0.050 | 9/29 (J82, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +3.1 | 0.096 | 6/19 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.44×** | +3.1 | 0.096 | 5/25 (A-172, A549, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.70×** | +3.1 | 0.096 | 1/27 (A549) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5870.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.479×** | -6.2 | 3e-07 | 22/38 (MIA PaCa-2, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.492×** | -6.0 | 7e-07 | 20/38 (A-172, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.541×** | -5.2 | 4e-05 | 16/34 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.557×** | -4.9 | 1e-04 | 20/39 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.560×** | -4.9 | 1e-04 | 18/41 (H4, LOX-IMVI, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.566×** | -4.8 | 1e-04 | 16/41 (LOX-IMVI, SW480, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.567×** | -4.8 | 1e-04 | 19/41 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.594×** | -4.4 | 8e-04 | 11/41 (LOX-IMVI, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.597×** | -4.3 | 9e-04 | 14/37 (HepG2/C3A, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.349×** | -3.8 | 0.008 | 11/35 (LOX-IMVI, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.740×** | -3.6 | 0.018 | 17/29 (A-172, A549, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.656×** | -3.5 | 0.019 | 10/27 (LOX-IMVI, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.396×** | -3.3 | 0.036 | 10/37 (A549, Hs 766T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.664×** | -3.3 | 0.037 | 10/32 (A-172, C-33 A, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.680×** | -3.2 | 0.045 | 6/41 (HepG2/C3A, NCI-H1792, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.417×** | -3.2 | 0.058 | 10/30 (LOX-IMVI, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5870. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 12.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 12.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0436× (z -14.2) |
| [[A-427 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.893 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.837 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.683 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.971 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.347 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.904 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.871 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.736 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.751 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.632 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5870), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROBO3]] | +0.58 | +0.36 / +0.67 | both halves | 9e-05 |  |
| [[CMTM3]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[KIAA1614]] | +0.55 | +0.60 / +0.32 | both halves | 2e-04 |  |
| [[GARIN1B]] | +0.54 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[TGFB1I1]] | +0.54 | +0.50 / +0.55 | both halves | 1e-05 | same gene group |
| [[GPSM3]] | +0.53 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[XG]] | +0.53 | +0.45 / +0.39 | both halves | 5e-05 |  |
| [[LPAR2]] | +0.51 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[DPYS]] | +0.51 | +0.45 / +0.33 | both halves | 1e-04 |  |
| [[MRC2]] | +0.51 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[MDGA1]] | +0.51 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[APBB1]] | +0.51 | +0.46 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPHOSPH9]] | -0.45 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[ALDH18A1]] | -0.45 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[SEPTIN7P14]] | -0.43 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[L2HGDH]] | -0.43 | -0.37 / -0.39 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRBC2]] | B | TRBC2 activity strengthens LIMD2's drug response | lines that do not express TRBC2 (33) vs lines expressing it (8) | the lines without TRBC2 respond 0.69× as strongly (z diff +0.51); rises at some drug-doses, falls at others (44% from rises): Panobinostat 0.5 µM: 0.52x vs 0.30x (z diff +1.9); Panobinostat 5 µM: 0.63x vs 0.39x (z diff +1.7); Selinexor 5 µM: 1.52x vs 1.92x (z diff +1.7) | 0.033 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |
| [[CMTM3]] | B | CMTM3 activity raises LIMD2's level | lines that do not express CMTM3 (11) vs lines expressing it (39) | 2.36× lower at baseline in the lines without CMTM3 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ZNF605, C2orf74, MAP1B |
| [[PDLIM4]] | B | PDLIM4 activity raises LIMD2's level | lines that do not express PDLIM4 (32) vs lines expressing it (18) | 1.71× lower at baseline in the lines without PDLIM4 | 0.089 | ⚠ within organs, on part of the lines; also absent: CARMN, CFI, IRAK3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.423). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.4, -1.0); signed map (10.7, 55.8). **Vector** length 45.5, 5.98% of its response variance represented; |z| ≥ 3 in 826 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +10.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.5 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +1.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -6.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -1.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | LIM domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:63,695,888-63,701,172 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10986 |
| Gene groups (HGNC) | LIM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BT23](https://www.uniprot.org/uniprotkb/Q9BT23) (LIM domain-containing protein 2):

> Acts as an activator of the protein-kinase ILK, thereby regulating cell motility.

**Summary**, from NCBI Gene [80774](https://www.ncbi.nlm.nih.gov/gene/80774):

> Predicted to enable actin filament binding activity. Predicted to be involved in actin filament bundle assembly. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28142](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28142) · Entrez [80774](https://www.ncbi.nlm.nih.gov/gene/80774) · UniProt [Q9BT23](https://www.uniprot.org/uniprotkb/Q9BT23) · Ensembl [ENSG00000136490](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136490)

## Data

Gene col 5870: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5870); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5870, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5870]; `tensor/DDL_lfc|DDL_z.npy` [5870]; `embed/gene_vectors.npy` [5870]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5870 or target_col == 5870). Every well: [[LIMD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIMD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
