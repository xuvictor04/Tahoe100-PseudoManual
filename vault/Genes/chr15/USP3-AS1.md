---
symbol: "USP3-AS1"
type: "gene"
col: 15180
ensembl_id: "ENSG00000259248"
name: "USP3 antisense RNA 1"
location: "15q22.31"
module: 39
arm: "+"
pooled_cpm: 15.52
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# USP3-AS1

*USP3 antisense RNA 1* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +11.3, q 1e-26, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.784× (z -3.6, q 0.067, down in 10 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKD2L2]] (+0.63, fdr 7e-06), [[EFCAB10]] (+0.61, fdr 1e-05), [[SLC5A11]] (+0.61, fdr 1e-05); moves opposite to [[TOP3B]] (-0.50, fdr 1e-04), [[UMPS]] (-0.49, fdr 4e-04), [[ZNF649]] (-0.46, fdr 3e-04).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15180.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +11.3 | 1e-26 | 33/47 (RKO, LS 180, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +7.6 | 6e-12 | 31/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +7.3 | 6e-11 | 27/39 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.3 | 4e-08 | 27/46 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.7 | 1e-06 | 27/48 (LS 180, HT-29, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +5.3 | 1e-05 | 17/29 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **1.40×** | +4.9 | 9e-05 | 20/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +4.4 | 9e-04 | 18/47 (KATO III, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.19× | +3.7 | 0.015 | 14/48 (A498, HOP62, …) | rises with dose | low cells (technical?) |
| [[Tazarotene (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.022 | 7/47 (HepG2/C3A, SW480, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.037 | 10/47 (AsPC-1, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.24×** | +3.2 | 0.058 | 13/48 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Artemether (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.079 | 5/47 (SK-MEL-2, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15180.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.784×** | -3.6 | 0.067 | 10/47 (hTERT-HPNE, HS-578T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.786×** | -3.6 | 0.067 | 14/47 (HCT15, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.787×** | -3.6 | 0.067 | 12/46 (NCI-H2030, LoVo, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.789×** | -3.4 | 0.085 | 12/47 (RPMI-7951, COLO 205, …) | all doses, flat | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.798×** | -3.4 | 0.085 | 18/46 (COLO 205, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bimatoprost (drug)]] 5 µM |  | 0.856× | -3.3 | 0.100 | 11/48 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.813× | -3.1 | 0.15 | 15/48 (NCI-H23, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.808× | -3.1 | 0.15 | 7/47 (CHP-212, hTERT-HPNE, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15180. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 24.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.2) | — |
| [[RKO (line)]] | wt | 14.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 24.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change · without an alert: [[Temsirolimus (drug)]] 0.5 µM 0.213× (z -8.7) |
| [[SW48 (line)]] | wt | 16.3 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0749× (z -11.0) |
| [[A-172 (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.187× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 16.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 22.2 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.0671× (z -8.5) |
| [[C-33 A (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0904× (z -10.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -10.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 12.1 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0865× (z -9.2) |
| [[HT-29 (line)]] | alt | 16.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0704× (z -11.6) |
| [[LS 180 (line)]] | wt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 15.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.113× (z -10.5) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15180), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKD2L2]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[EFCAB10]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[SLC5A11]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[TOMM20L-DT]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[SLC7A9]] | +0.57 | +0.62 / +0.40 | both halves | 4e-05 |  |
| [[LNCRNA-IUR]] | +0.57 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[CNBD2]] | +0.57 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[CTDSPL2-DT]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[POLN]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ABHD15-AS1]] | +0.56 | +0.49 / +0.61 | both halves | 1e-05 | same gene group |
| [[MASP2]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[MFSD2B]] | +0.55 | +0.51 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOP3B]] | -0.50 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[UMPS]] | -0.49 | -0.26 / -0.60 | both halves | 4e-04 |  |
| [[ZNF649]] | -0.46 | -0.29 / -0.58 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers USP3-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.474). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.9, -11.3); signed map (21.0, 5.3). **Vector** length 62.7, 9.38% of its response variance represented; |z| ≥ 3 in 784 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | +3.6 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +6.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +2.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.2 | +1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | +1.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.4 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -2.3 | -3.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -2.7 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | USP3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q22.31 — chr15:63,544,247-63,601,589 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44140](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44140) · Entrez [100130855](https://www.ncbi.nlm.nih.gov/gene/100130855) · Ensembl [ENSG00000259248](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259248)

## Data

Gene col 15180: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15180); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15180, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15180]; `tensor/DDL_lfc|DDL_z.npy` [15180]; `embed/gene_vectors.npy` [15180]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15180 or target_col == 15180). Every well: [[USP3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
