---
symbol: "DTX3"
type: "gene"
col: 10932
ensembl_id: "ENSG00000178498"
name: "deltex E3 ubiquitin ligase 3"
location: "12q13.3"
module: 96
arm: "+"
pooled_cpm: 4.41
n_lines_expressing: 36
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# DTX3

*deltex E3 ubiquitin ligase 3* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.79× (z +6.5, q 6e-08, up in 5 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.38× (z +5.2, q 3e-05, up in 11 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.348× (z -12.2, q 2e-31, down in 27 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DXO]] (+0.68, fdr 7e-06), [[TBKBP1]] (+0.66, fdr 1e-05), [[GPRASP1]] (+0.65, fdr 1e-05); moves opposite to [[SPTLC2]] (-0.58, fdr 4e-05), [[ARPC1B]] (-0.58, fdr 3e-05), [[NHP2]] (-0.55, fdr 6e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[ENGASE]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10932.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +6.5 | 6e-08 | 5/9 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.45×** | +6.1 | 4e-07 | 13/31 (A-172, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +5.2 | 3e-05 | 11/27 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.43×** | +4.1 | 0.005 | 6/28 (A549, LOX-IMVI, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.041 | 4/29 (H4, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.5 | 0.041 | 2/33 (MIA PaCa-2, NCI-H23) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.53×** | +3.5 | 0.041 | 1/26 (hTERT-HPNE) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +3.3 | 0.055 | 5/20 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.055 | 4/29 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 1.30× | +3.0 | 0.13 | 6/31 (HS-578T, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10932.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.348×** | -12.2 | 2e-31 | 27/31 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.349×** | -12.1 | 2e-31 | 27/31 (NCI-H23, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.364×** | -11.7 | 4e-29 | 27/32 (NCI-H1792, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.538×** | -7.1 | 1e-10 | 20/32 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.561×** | -6.7 | 3e-09 | 15/29 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.685×** | -6.2 | 7e-08 | 16/28 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.387×** | -5.7 | 8e-07 | 15/28 (C32, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.625×** | -5.2 | 1e-05 | 14/28 (HOP62, NCI-H1792, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.436×** | -5.0 | 3e-05 | 15/32 (NCI-H1792, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.659×** | -4.6 | 2e-04 | 12/27 (C32, NCI-H2030, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.762×** | -4.4 | 5e-04 | 11/32 (C32, SHP-77, …) | top dose only | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.832× | -3.0 | 0.13 | 6/31 (NCI-H1573, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.48 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10932. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 34.0 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -13.5) |
| [[C32 (line)]] | wt | 7.93 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0951× (z -9.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A-172 (line)]] | wt | 7.27 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -9.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[hTERT-HPNE (line)]] | wt | 9.88 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0986× (z -9.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 4.57 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0384× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 5.57 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -9.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 3.23 | 0 | 1 | — | [[Cilostazol (drug)]] 0.05 µM 0.0751× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 4.39 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0457× (z -10.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 11.2 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0986× (z -10.2) |
| [[SW480 (line)]] | alt | 6.69 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -10.4) |
| [[A-427 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.413 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.295 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.324 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.434 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10932), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DXO]] | +0.68 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[TBKBP1]] | +0.66 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[GPRASP1]] | +0.65 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[MED12]] | +0.64 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CCDC102A]] | +0.64 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[TSSK3]] | +0.62 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[ARMCX1]] | +0.62 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[MYL5]] | +0.62 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[CDK3]] | +0.62 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[SH2B1]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[WDR6]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[ATXN7L2]] | +0.60 | +0.53 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTLC2]] | -0.58 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[ARPC1B]] | -0.58 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[NHP2]] | -0.55 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[LSM4]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[KIAA1958]] | -0.52 | -0.37 / -0.44 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DTX3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CA11]] | B | CA11 activity lowers DTX3's level | lines that do not express CA11 (6) vs lines expressing it (44) | 1.66× higher at baseline in the lines without CA11 | 0.065 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENGASE]] | B | DTX3 activity raises ENGASE's level | lines that do not express DTX3 (14) vs lines expressing it (36) | 1.16× lower at baseline in the lines without DTX3 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with ARID1A, SETD1B; also absent: NRIP3, UPK1A-AS1, SDK2 |
| [[KCNMB3]] | B | DTX3 activity raises KCNMB3's level | lines that do not express DTX3 (14) vs lines expressing it (36) | 1.85× lower at baseline in the lines without DTX3 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with ARID1A, SETD1B; also absent: NRIP3, UPK1A-AS1, SDK2 |

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.644). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-3.2, 17.0); signed map (15.7, -13.7). **Vector** length 48.8, 8.06% of its response variance represented; |z| ≥ 3 in 612 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.6 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.5 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | -0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +1.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.5 | -12.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.7 | -7.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.6 | -12.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -5.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -5.0 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.1 | -2.1 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | deltex E3 ubiquitin ligase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:57,604,622-57,609,804 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34766, RNF154 |
| Gene groups (HGNC) | Ring finger proteins; Deltex E3 ubiquitin ligase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N9I9](https://www.uniprot.org/uniprotkb/Q8N9I9) (E3 ubiquitin-protein ligase DTX3):

> Functions as an ubiquitin ligase protein, and regulates Notch signaling. By promoting the ubiquitination and subsequent degradation of target proteins, it can block activation of the Notch signaling pathway, potentially acting as a tumor suppressor in human cancers.; [Isoform 3]: Involved in the angiogenic EPHB4 kinase degradation in cancer cell.

**Summary**, from NCBI Gene [196403](https://www.ncbi.nlm.nih.gov/gene/196403):

> DTX3 functions as an E3 ubiquitin ligase (Takeyama et al., 2003 [PubMed 12670957]).[supplied by OMIM, Nov 2009]

**Accessions** — [HGNC:24457](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24457) · Entrez [196403](https://www.ncbi.nlm.nih.gov/gene/196403) · UniProt [Q8N9I9](https://www.uniprot.org/uniprotkb/Q8N9I9) · Ensembl [ENSG00000178498](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178498)

## Data

Gene col 10932: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10932); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10932, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10932]; `tensor/DDL_lfc|DDL_z.npy` [10932]; `embed/gene_vectors.npy` [10932]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10932 or target_col == 10932). Every well: [[DTX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DTX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
