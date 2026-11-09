---
symbol: "DMAP1"
type: "gene"
col: 10887
ensembl_id: "ENSG00000178028"
name: "DNA methyltransferase 1 associated protein 1"
location: "1p34.1"
module: 127
arm: "+"
pooled_cpm: 8.28
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# DMAP1

*DNA methyltransferase 1 associated protein 1* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.67× (z +6.6, q 3e-08, up in 7 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.39× (z +4.2, q 0.003, up in 11 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.537× (z -11.7, q 9e-29, down in 32 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HARS2]] (+0.72, fdr 7e-06), [[BAP1]] (+0.70, fdr 7e-06), [[TTC31]] (+0.68, fdr 7e-06); moves opposite to [[SNX14]] (-0.61, fdr 1e-05), [[GAN]] (-0.58, fdr 1e-05), [[TPTEP2-CSNK1E]] (-0.55, fdr 1e-05).
> It is in [[Module 127]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF613]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10887.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +6.6 | 3e-08 | 7/14 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +6.3 | 7e-08 | 13/22 (HEC-1-A, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +5.5 | 9e-06 | 16/32 (LoVo, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.29×** | +4.7 | 3e-04 | 15/47 (NCI-H2030, AsPC-1, …) | rises with dose | low cells (technical?); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +4.2 | 0.003 | 11/45 (NCI-H2030, PANC-1, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.8 | 0.011 | 13/38 (A-427, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.46×** | +3.6 | 0.026 | 8/41 (NCI-H1792, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.032 | 8/45 (Hs 766T, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.64×** | +3.4 | 0.036 | 6/42 (RKO, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.047 | 12/43 (LS 180, HCT15, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.047 | 6/43 (LS 180, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.094 | 6/48 (A498, SNU-423, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.29× | +3.0 | 0.11 | 6/45 (NCI-H2030, C32, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10887.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.537×** | -11.7 | 9e-29 | 32/44 (PANC-1, SHP-77, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.595×** | -6.9 | 2e-09 | 27/48 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.608×** | -6.6 | 8e-09 | 24/44 (SW480, HCT15, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.646×** | -5.8 | 1e-06 | 24/46 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.750×** | -5.4 | 8e-06 | 20/46 (J82, PANC-1, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.692×** | -4.9 | 1e-04 | 19/46 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.694×** | -4.7 | 3e-04 | 21/44 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.735×** | -4.1 | 0.003 | 14/47 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.737×** | -4.1 | 0.003 | 14/47 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.756×** | -3.7 | 0.012 | 12/48 (CFPAC-1, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.766×** | -3.5 | 0.021 | 13/46 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.780×** | -3.3 | 0.046 | 10/48 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10887. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 7.72 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -8.8) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 7.28 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM 0.0717× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 6.51 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0986× (z -10.9) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 6.71 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -8.5) |
| [[PANC-1 (line)]] | alt | 13.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0948× (z -9.8) |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.176× (z -8.5) |
| [[SW 900 (line)]] | alt | 7.39 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -9.2) |
| [[SW480 (line)]] | alt | 9.72 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10887), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HARS2]] | +0.72 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[BAP1]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[TTC31]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ABCF3]] | +0.67 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[PRPF31]] | +0.65 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[UCK1]] | +0.65 | +0.73 / +0.58 | both halves | 8e-06 |  |
| [[PIGO]] | +0.65 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[TAF1C]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ZBTB17]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[ARAF]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[ACP2]] | +0.64 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[STK36]] | +0.62 | +0.65 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX14]] | -0.61 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[GAN]] | -0.58 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[TMTC2]] | -0.53 | -0.50 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF613]] | B | ZNF613 activity raises DMAP1's level | lines that do not express ZNF613 (7) vs lines expressing it (43) | 1.34× lower at baseline in the lines without ZNF613 | 0.019 | ⚠ within organs, on part of the lines; also absent: ZNF850, ENSG00000283201, ZNF571 |
| [[TP73-AS1]] | B | TP73-AS1 activity raises DMAP1's level | lines that do not express TP73-AS1 (17) vs lines expressing it (33) | 1.16× lower at baseline in the lines without TP73-AS1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000176593, ZNF606, GAMT; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-32.7, -2.9); signed map (-11.6, -30.1). **Vector** length 66.8, 10.6% of its response variance represented; |z| ≥ 3 in 780 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +4.7 | +4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +6.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +6.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | -0.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -11.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.2 | -4.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.4 | -1.6 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | DNA methyltransferase 1 associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:44,213,455-44,220,681 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DNMAP1, FLJ11543, KIAA1425, DNMTAP1, EAF2, MEAF2, SWC4 |
| Gene groups (HGNC) | Myb/SANT domain containing; SRCAP complex subunits; Tip60/Nua4 histone acetyltransferase complex subunits |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPF5](https://www.uniprot.org/uniprotkb/Q9NPF5) (DNA methyltransferase 1-associated protein 1):

> Involved in transcription repression and activation. Its interaction with HDAC2 may provide a mechanism for histone deacetylation in heterochromatin following replication of DNA at late firing origins. Can also repress transcription independently of histone deacetylase activity. May specifically potentiate DAXX-mediated repression of glucocorticoid receptor-dependent transcription. Component of the NuA4 histone acetyltransferase (HAT) complex which is involved in transcriptional activation of …

**Summary**, from NCBI Gene [55929](https://www.ncbi.nlm.nih.gov/gene/55929):

> This gene encodes a subunit of several, distinct complexes involved in the repression or activation of transcription. The encoded protein can independently repress transcription and is targeted to replication foci throughout S phase by interacting directly with the N-terminus of DNA methyltransferase 1. During late S phase, histone deacetylase 2 is added to this complex, providing a means to deacetylate histones in transcriptionally inactive heterochromatin following replication. The encoded …

**Accessions** — [HGNC:18291](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18291) · Entrez [55929](https://www.ncbi.nlm.nih.gov/gene/55929) · UniProt [Q9NPF5](https://www.uniprot.org/uniprotkb/Q9NPF5) · Ensembl [ENSG00000178028](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178028)

## Data

Gene col 10887: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10887); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10887, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10887]; `tensor/DDL_lfc|DDL_z.npy` [10887]; `embed/gene_vectors.npy` [10887]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10887 or target_col == 10887). Every well: [[DMAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DMAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
