---
symbol: "KPNB1-DT"
type: "gene"
col: 15426
ensembl_id: "ENSG00000263766"
name: "KPNB1 divergent transcript"
location: "17q21.32"
module: 15
arm: "+"
pooled_cpm: 23.97
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# KPNB1-DT

*KPNB1 divergent transcript* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.66× (z +20.7, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.692× (z -5.3, q 6e-05, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EHBP1-AS1]] (+0.71, fdr 7e-06), [[GATD1-DT]] (+0.68, fdr 7e-06), [[EOGT-DT]] (+0.66, fdr 9e-06); moves opposite to [[THEM6]] (-0.61, fdr 1e-05), [[SRRD]] (-0.60, fdr 2e-04), [[KBTBD6]] (-0.59, fdr 4e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15426.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.66×** | +20.7 | 0e+00 | 47/48 (NCI-H1792, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +11.0 | 6e-26 | 39/47 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +9.4 | 7e-19 | 25/32 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +9.1 | 2e-17 | 38/48 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +7.3 | 3e-11 | 25/38 (C32, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +6.7 | 2e-09 | 31/43 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +4.9 | 6e-05 | 24/48 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +4.7 | 2e-04 | 19/45 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +4.6 | 2e-04 | 23/47 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.5 | 3e-04 | 25/48 (HOP62, SW1417, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.6 | 0.017 | 1/48 (NCI-H23) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.017 | 15/48 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.026 | 12/47 (A-172, NCI-H2030, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15426.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.692×** | -5.3 | 6e-05 | 23/47 (CFPAC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.756×** | -4.2 | 0.006 | 21/48 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.589×** | -4.2 | 0.006 | 18/46 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.770×** | -3.9 | 0.012 | 22/48 (PANC-1, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.617×** | -3.8 | 0.016 | 15/48 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.849× | -3.5 | 0.047 | 16/48 (NCI-H1792, SK-MEL-2, …) | top dose only | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.816× | -3.1 | 0.16 | 13/47 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | 0.817× | -3.0 | 0.16 | 16/47 (H4, NCI-H2030, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15426. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 21.1 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +13.8) | — |
| [[HOP62 (line)]] | alt | 30.3 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +12.7) | [[Lonafarnib (drug)]] 5 µM 0.108× (z -10.4) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 45.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.0) | [[Lonafarnib (drug)]] 5 µM 0.0955× (z -10.0) ⚠ toxic |
| [[HS-578T (line)]] | alt | 24.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +11.0) | — |
| [[HT-29 (line)]] | alt | 20.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.06× (z +14.1) | — |
| [[KATO III (line)]] | alt | 28.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +14.3) | — |
| [[NCI-H460 (line)]] | wt | 21.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +10.7) | — |
| [[A-172 (line)]] | wt | 18.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +8.8) | — |
| [[A-427 (line)]] | wt | 26.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -10.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 21.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +12.7) | — |
| [[AsPC-1 (line)]] | alt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 20.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 29.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +13.7) | — |
| [[COLO 205 (line)]] | alt | 28.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 16.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +9.0) | — |
| [[J82 (line)]] | alt | 24.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +11.7) | — |
| [[LoVo (line)]] | wt | 15.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 29.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +11.4) | — |
| [[NCI-H1792 (line)]] | alt | 22.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +14.4) | — |
| [[NCI-H2030 (line)]] | alt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 29.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +10.8) | — |
| [[PANC-1 (line)]] | alt | 36.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +11.9) | — |
| [[RKO (line)]] | wt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 25.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 25.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +11.9) | — |
| [[SNU-1 (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0852× (z -11.5) ⚠ transcription drop |
| [[SNU-423 (line)]] | alt | 24.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 20.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +13.9) | — |
| [[A498 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15426), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHBP1-AS1]] | +0.71 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[GATD1-DT]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 | same gene group |
| [[EOGT-DT]] | +0.66 | +0.57 / +0.65 | both halves | 9e-06 | same gene group |
| [[ZNF451-AS1]] | +0.65 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[TICAM2-AS1]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[SPESP1]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[SPATA1]] | +0.65 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[C2CD5-AS1]] | +0.64 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[ZNF213-AS1]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[TRNAU1AP]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[KIAA2026]] | +0.63 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[USP34-DT]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THEM6]] | -0.61 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[SRRD]] | -0.60 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[KBTBD6]] | -0.59 | -0.26 / -0.54 | both halves | 4e-04 |  |
| [[DLAT]] | -0.58 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[PRMT5]] | -0.57 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[NLE1]] | -0.55 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[PROSER1]] | -0.55 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[PRELID3B]] | -0.55 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[PSMG1]] | -0.55 | -0.41 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KPNB1-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ARL17B]] | B | ARL17B activity raises KPNB1-DT's level | lines that do not express ARL17B (25) vs lines expressing it (25) | 1.17× lower at baseline in the lines without ARL17B | 0.0998 | ⚠ within organs, on part of the lines; also absent: ENSG00000290457, ENSG00000251598, AFAP1-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.622). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (1.7, 22.6); signed map (27.2, -0.2). **Vector** length 77.5, 14.8% of its response variance represented; |z| ≥ 3 in 833 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +20.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +11.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +4.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.5 | +1.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -3.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -3.4 | +2.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.7 | -5.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.6 | -2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.8 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[OTS514 (drug)]] 5 µM |  | -1.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | KPNB1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q21.32 — chr17:47,603,860-47,649,449 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55336](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55336) · Entrez [112268184](https://www.ncbi.nlm.nih.gov/gene/112268184) · Ensembl [ENSG00000263766](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000263766)

## Data

Gene col 15426: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15426); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15426, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15426]; `tensor/DDL_lfc|DDL_z.npy` [15426]; `embed/gene_vectors.npy` [15426]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15426 or target_col == 15426). Every well: [[KPNB1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KPNB1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
