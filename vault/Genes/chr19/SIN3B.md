---
symbol: "SIN3B"
type: "gene"
col: 4816
ensembl_id: "ENSG00000127511"
name: "SIN3 transcription regulator family member B"
location: "19p13.11"
module: 2
arm: "+"
pooled_cpm: 43.01
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# SIN3B

*SIN3 transcription regulator family member B* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.53× (z +7.2, q 4e-10, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.632× (z -11.0, q 2e-25, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALNS]] (+0.65, fdr 1e-05), [[FCHSD1]] (+0.65, fdr 1e-05), [[PPP1R12C]] (+0.64, fdr 2e-05); moves opposite to [[QKI]] (-0.60, fdr 3e-05), [[CDC14A]] (-0.59, fdr 1e-05), [[DYRK1A]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4816.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +7.2 | 4e-10 | 41/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +6.5 | 2e-08 | 39/48 (AsPC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +5.4 | 1e-05 | 28/48 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +5.0 | 1e-04 | 30/48 (BT-474, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.7 | 2e-04 | 30/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.30×** | +4.5 | 7e-04 | 21/48 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 0.002 | 27/48 (BT-474, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +3.8 | 0.010 | 24/47 (SHP-77, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.072 | 21/48 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.26×** | +3.1 | 0.096 | 17/48 (LoVo, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.0 | 0.13 | 11/47 (A-172, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4816.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.632×** | -11.0 | 2e-25 | 36/48 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.847× | -4.0 | 0.018 | 19/48 (H4, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.764×** | -3.8 | 0.025 | 22/48 (MIA PaCa-2, C32, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.769×** | -3.7 | 0.028 | 24/48 (A-427, C32, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **0.814×** | -3.5 | 0.054 | 22/46 (HCT15, A-427, …) | inconsistent across doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4816. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 33.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -12.5) |
| [[C32 (line)]] | wt | 38.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -12.1) |
| [[LS 180 (line)]] | wt | 45.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 38.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -11.8) |
| [[SHP-77 (line)]] | alt | 56.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Sonidegib (drug)]] 5 µM 0.0639× (z -13.3) |
| [[SNU-423 (line)]] | alt | 45.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -10.1) |
| [[HCT15 (line)]] | alt | 59.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0755× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[HEC-1-A (line)]] | alt | 64.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.290× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 42.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -9.9) |
| [[KATO III (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 38.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 43.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 56.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 39.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -11.0) |
| [[RKO (line)]] | wt | 51.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 46.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[SNU-1 (line)]] | wt | 50.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 35.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -11.1) |
| [[SW48 (line)]] | wt | 52.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 70.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 38.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4816), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNS]] | +0.65 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[FCHSD1]] | +0.65 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R12C]] | +0.64 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[ZNF875]] | +0.63 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[GPSM1]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[SYMPK]] | +0.61 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[FBRSL1]] | +0.60 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[AP2A2]] | +0.60 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[TMEM259]] | +0.59 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[TRIP4]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[RNF123]] | +0.58 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[HSF1]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QKI]] | -0.60 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[CDC14A]] | -0.59 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[DYRK1A]] | -0.57 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[CPNE8]] | -0.57 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[LHFPL6]] | -0.56 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[TIFA]] | -0.54 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[MEIS2]] | -0.54 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[NFKBID]] | -0.52 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[CDKN2C]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[PARP8]] | -0.51 | -0.23 / -0.50 | both halves | 5e-04 |  |
| [[TAPT1]] | -0.51 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[MICOS10]] | -0.51 | -0.46 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SIN3B's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SNTA1]] | B | SNTA1 activity raises SIN3B's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.55× lower at baseline in the lines without SNTA1 | 0.025 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers SIN3B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers SIN3B's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.643). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-1.7, -25.3); signed map (-29.5, 0.2). **Vector** length 83.8, 18.0% of its response variance represented; |z| ≥ 3 in 735 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.0 | -1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +6.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.7 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | +4.1 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | +4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | -0.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.3 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -1.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -3.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -3.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -0.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.7 | -1.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.6 | +0.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | SIN3 transcription regulator family member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:16,829,398-16,880,353 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0700 |
| Gene groups (HGNC) | EMSY complex; SIN3 histone deacetylase complex subunits |
| Reactome | 11 pathways, smallest: RUNX1 regulates genes involved in megakaryocyte differentiation and platelet function; Cytoprotection by HMOX1; NoRC negatively regulates rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [O75182](https://www.uniprot.org/uniprotkb/O75182) (Paired amphipathic helix protein Sin3b):

> Acts as a transcriptional repressor. Interacts with MXI1 to repress MYC responsive genes and antagonize MYC oncogenic activities. Interacts with MAD-MAX heterodimers by binding to MAD. The heterodimer then represses transcription by tethering SIN3B to DNA. Also forms a complex with FOXK1 which represses transcription. With FOXK1, regulates cell cycle progression probably by repressing cell cycle inhibitor genes expression. As part of the SIN3B complex represses transcription and counteracts the …

**Summary**, from NCBI Gene [23309](https://www.ncbi.nlm.nih.gov/gene/23309):

> Predicted to enable transcription corepressor activity. Predicted to be involved in cardiac muscle tissue development; negative regulation of transcription by RNA polymerase II; and skeletal muscle tissue development. Predicted to be located in nucleus. Predicted to be part of Sin3-type complex. Predicted to be active in chromatin. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19354](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19354) · Entrez [23309](https://www.ncbi.nlm.nih.gov/gene/23309) · UniProt [O75182](https://www.uniprot.org/uniprotkb/O75182) · Ensembl [ENSG00000127511](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127511)

## Data

Gene col 4816: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4816); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4816, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4816]; `tensor/DDL_lfc|DDL_z.npy` [4816]; `embed/gene_vectors.npy` [4816]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4816 or target_col == 4816). Every well: [[SIN3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIN3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
