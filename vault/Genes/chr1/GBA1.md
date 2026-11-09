---
symbol: "GBA1"
type: "gene"
col: 10843
ensembl_id: "ENSG00000177628"
name: "glucosylceramidase beta 1"
location: "1q22"
module: 122
arm: "+"
pooled_cpm: 8.15
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# GBA1

*glucosylceramidase beta 1* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.01× (z +10.7, q 4e-24, up in 13 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.54× (z +9.4, q 1e-18, up in 40 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM in 1 line (C32 0.0520×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (SW1417 0.0695×); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.317×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NXT2]] (+0.73, fdr 7e-06), [[IGF2R]] (+0.71, fdr 7e-06), [[TPP1]] (+0.70, fdr 7e-06); moves opposite to [[COX5A]] (-0.64, fdr 1e-05, ⚠ COX5A in the vector space only through flagged drug-doses), [[PIBF1]] (-0.60, fdr 1e-05), [[SNU13]] (-0.60, fdr 1e-05), [[SEC22A]] (-0.59, fdr 2e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10843.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.01×** | +10.7 | 4e-24 | 13/14 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.54×** | +9.4 | 1e-18 | 40/46 (LoVo, SHP-77, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.88×** | +9.0 | 3e-17 | 35/46 (HOP62, SHP-77, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +7.4 | 2e-11 | 23/31 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +7.1 | 2e-10 | 11/20 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +6.8 | 9e-10 | 27/43 (PANC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.73×** | +5.6 | 2e-06 | 23/47 (NCI-H460, KATO III, …) | two highest doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.65×** | +5.0 | 3e-05 | 21/45 (NCI-H2030, KATO III, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +4.7 | 2e-04 | 18/45 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.60×** | +4.6 | 2e-04 | 15/41 (PANC-1, NCI-H2030, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.57×** | +4.6 | 2e-04 | 18/47 (NCI-H460, KATO III, …) | two highest doses | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **1.37×** | +4.4 | 6e-04 | 18/47 (HT-29, SW480, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.52×** | +4.2 | 1e-03 | 17/45 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.50×** | +4.1 | 0.002 | 14/47 (HT-29, HEC-1-A, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.49×** | +4.0 | 0.002 | 11/46 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.002 | 17/48 (HOP62, J82, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.012 | 17/43 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.012 | 11/45 (LOX-IMVI, MIA PaCa-2, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.015 | 12/46 (NCI-H1573, J82, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10843.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM in 1 line (C32 0.0520×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (SW1417 0.0695×); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.317×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | 0.704× | -3.4 | 0.35 | 11/44 (KATO III, C-33 A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10843. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 6.03 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM 0.0520× (z -11.0) |
| [[HOP62 (line)]] | alt | 3.89 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0751× (z -9.4) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 14.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 7.58 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -9.7) |
| [[SW1417 (line)]] | alt | 5.20 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0695× (z -9.7) |
| [[A-172 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10843), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NXT2]] | +0.73 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[IGF2R]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[TPP1]] | +0.70 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[SMCR8]] | +0.69 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[NRAS]] | +0.67 | +0.46 / +0.71 | both halves | 2e-05 |  |
| [[ZNF300]] | +0.67 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[LAMP1]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 | STRING 613 |
| [[GNS]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ATP6V1C1]] | +0.66 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[M6PR]] | +0.65 | +0.52 / +0.65 | both halves | 1e-05 | pathway: Glycosphingolipid catabolism |
| [[SF3B4]] | +0.64 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[PEX19]] | +0.63 | +0.50 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX5A]] ⚠ | -0.64 | -0.49 / -0.63 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PIBF1]] | -0.60 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[SNU13]] | -0.60 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[SEC22A]] | -0.59 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[ZXDC]] | -0.57 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[CDKN2D]] | -0.57 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[RPL36]] | -0.56 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[ATP5ME]] | -0.55 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[ARID3A]] | -0.55 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[ANAPC11]] | -0.54 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[PPP1R35]] ⚠ | -0.54 | -0.40 / -0.52 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SRGAP2D]] | -0.54 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[PPP1R14B]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[TMEM258]] | -0.54 | -0.48 / -0.58 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GBA1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-22.0, -20.4); signed map (-23.7, -35.8). **Vector** length 73.8, 12.6% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.2 | +9.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.0 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.8 | +4.0 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | +1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.1 | +3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +1.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | glucosylceramidase beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,234,452-155,244,699 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GLUC, GBA |
| Gene groups (HGNC) | Glycoside hydrolase family; Glucosylceramidases |
| Reactome | 7 pathways, smallest: Glycosphingolipid catabolism; Association of TriC/CCT with target proteins during biosynthesis; Glycosphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P04062](https://www.uniprot.org/uniprotkb/P04062) (Lysosomal acid glucosylceramidase):

> Glucosylceramidase that catalyzes, within the lysosomal compartment, the hydrolysis of glucosylceramides/GlcCers (such as beta-D-glucosyl-(1<->1')-N-acylsphing-4-enine) into free ceramides (such as N-acylsphing-4-enine) and glucose. Plays a central role in the degradation of complex lipids and the turnover of cellular membranes. Through the production of ceramides, participates in the PKC-activated salvage pathway of ceramide formation. Catalyzes the glucosylation of cholesterol, through a …

**Summary**, from NCBI Gene [2629](https://www.ncbi.nlm.nih.gov/gene/2629):

> This gene encodes a lysosomal membrane protein that cleaves the beta-glucosidic linkage of glycosylceramide, an intermediate in glycolipid metabolism. Mutations in this gene cause Gaucher disease, a lysosomal storage disease characterized by an accumulation of glucocerebrosides. A related pseudogene is approximately 12 kb downstream of this gene on chromosome 1. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:4177](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4177) · Entrez [2629](https://www.ncbi.nlm.nih.gov/gene/2629) · UniProt [P04062](https://www.uniprot.org/uniprotkb/P04062) · Ensembl [ENSG00000177628](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177628)

## Data

Gene col 10843: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10843); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10843, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10843]; `tensor/DDL_lfc|DDL_z.npy` [10843]; `embed/gene_vectors.npy` [10843]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10843 or target_col == 10843). Every well: [[GBA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GBA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
