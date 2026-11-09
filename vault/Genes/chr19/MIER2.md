---
symbol: "MIER2"
type: "gene"
col: 2619
ensembl_id: "ENSG00000105556"
name: "MIER family member 2"
location: "19p13.3"
module: 2
arm: "+"
pooled_cpm: 13.66
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# MIER2

*MIER family member 2* — 19p13.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.347× (z -18.2, q 0e+00, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF473]] (+0.71, fdr 7e-06), [[GPSM1]] (+0.69, fdr 1e-05), [[AP1M1]] (+0.67, fdr 1e-05); moves opposite to [[CERT1]] (-0.68, fdr 3e-05), [[UVRAG]] (-0.60, fdr 1e-05), [[BMPR2]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2619.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.29× | +3.1 | 0.99 | 10/47 (SW480, MIA PaCa-2, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2619.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.347×** | -18.2 | 0e+00 | 43/46 (SW 900, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.424×** | -10.1 | 2e-21 | 37/46 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.440×** | -9.6 | 1e-19 | 37/47 (A-172, RKO, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.589×** | -6.0 | 3e-07 | 19/30 (SW480, Hs 766T, …) | inconsistent across doses | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.622×** | -5.8 | 7e-07 | 27/47 (A-172, A498, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.593×** | -5.7 | 9e-07 | 30/37 (NCI-H460, HEC-1-A, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.679×** | -4.7 | 2e-04 | 22/48 (A498, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.670×** | -4.7 | 2e-04 | 24/47 (NCI-H23, HS-578T, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.693×** | -4.5 | 5e-04 | 22/46 (HS-578T, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.706×** | -4.3 | 0.001 | 22/48 (A498, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.680×** | -4.3 | 0.001 | 22/46 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.725×** | -3.9 | 0.004 | 17/48 (NCI-H2347, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~20% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.762×** | -3.3 | 0.036 | 18/47 (LOX-IMVI, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.765×** | -3.2 | 0.062 | 10/46 (NCI-H1573, hTERT-HPNE, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.838× | -3.1 | 0.075 | 14/48 (NCI-H1573, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2619. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 23.2 | 0 | 6 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0301× (z -23.3) |
| [[NCI-H460 (line)]] | wt | 13.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0607× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -11.0) |
| [[HS-578T (line)]] | alt | 22.7 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -13.9) |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -9.6) |
| [[A498 (line)]] | wt | 18.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -14.5) |
| [[H4 (line)]] | wt | 18.8 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0911× (z -9.5) |
| [[Hs 766T (line)]] | wt | 16.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0974× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -10.5) |
| [[LoVo (line)]] | wt | 12.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 11.9 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -11.7) |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -10.8) |
| [[PANC-1 (line)]] | alt | 10.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -9.8) |
| [[RKO (line)]] | wt | 18.9 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0794× (z -12.9) |
| [[SW480 (line)]] | alt | 13.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -12.2) |
| [[A549 (line)]] | wt | 10.0 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.158× (z -8.8) |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -10.2) |
| [[C32 (line)]] | wt | 10.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0489× (z -12.1) |
| [[CFPAC-1 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0941× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~13% of this change |
| [[HCT15 (line)]] | alt | 19.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0602× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[HOP62 (line)]] | alt | 12.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -13.1) |
| [[J82 (line)]] | alt | 10.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -9.0) |
| [[KATO III (line)]] | alt | 6.62 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 16.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 12.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 18.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -13.1) |
| [[NCI-H2347 (line)]] | alt | 14.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RPMI-7951 (line)]] | alt | 9.77 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.107× (z -8.9) |
| [[SNU-423 (line)]] | alt | 14.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -9.3) |
| [[SW 900 (line)]] | alt | 16.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -15.1) |
| [[A-427 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2619), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF473]] | +0.71 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[GPSM1]] | +0.69 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[AP1M1]] | +0.67 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[WDR55]] | +0.66 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SGTA]] | +0.64 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[DPH7]] | +0.63 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[AARS2]] | +0.63 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[ZSCAN22]] | +0.62 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[ZNF527]] | +0.61 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[E2F4]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[GCN1]] | +0.61 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[TPCN2]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CERT1]] | -0.68 | -0.46 / -0.65 | both halves | 3e-05 |  |
| [[UVRAG]] | -0.60 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[BMPR2]] | -0.58 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[MKLN1]] | -0.58 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[WDFY3]] | -0.58 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[ARID2]] | -0.58 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[CDK19]] | -0.56 | -0.40 / -0.54 | both halves | 4e-05 |  |
| [[TAPT1]] | -0.56 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[BBX]] | -0.55 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[WAC-AS1]] | -0.55 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[CDC14A]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[NIFK-AS1]] | -0.55 | -0.54 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MIER2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ATP8B3]] | B | ATP8B3 activity raises MIER2's level | lines that do not express ATP8B3 (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without ATP8B3 | 0.066 | ⚠ within organs, on part of the lines; also absent: CEP85L, PARP3, SOAT1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.550). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-3.0, -26.1); signed map (-50.8, 1.0). **Vector** length 69.8, 12.0% of its response variance represented; |z| ≥ 3 in 996 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.3 | +1.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.8 | +3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.8 | -4.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.7 | +2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +0.3 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +0.8 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +1.2 | +1.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.2 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -18.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -10.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -9.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | -2.7 | -4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | MIER family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:305,573-344,815 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1193 |
| Gene groups (HGNC) | Myb/SANT domain containing; MIER complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N344](https://www.uniprot.org/uniprotkb/Q8N344) (Mesoderm induction early response protein 2):

> Transcriptional repressor.

**Summary**, from NCBI Gene [54531](https://www.ncbi.nlm.nih.gov/gene/54531):

> Enables histone deacetylase binding activity. Contributes to histone deacetylase activity. Predicted to be involved in negative regulation of transcription by RNA polymerase II. Located in cytoplasm and nucleus. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29210](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29210) · Entrez [54531](https://www.ncbi.nlm.nih.gov/gene/54531) · UniProt [Q8N344](https://www.uniprot.org/uniprotkb/Q8N344) · Ensembl [ENSG00000105556](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105556)

## Data

Gene col 2619: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2619); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2619, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2619]; `tensor/DDL_lfc|DDL_z.npy` [2619]; `embed/gene_vectors.npy` [2619]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2619 or target_col == 2619). Every well: [[MIER2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIER2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
