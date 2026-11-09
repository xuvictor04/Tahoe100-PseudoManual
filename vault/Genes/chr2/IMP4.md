---
symbol: "IMP4"
type: "gene"
col: 5894
ensembl_id: "ENSG00000136718"
name: "IMP U3 small nucleolar ribonucleoprotein 4"
location: "2q21.1"
module: 1
arm: "+"
pooled_cpm: 14.05
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# IMP4

*IMP U3 small nucleolar ribonucleoprotein 4* — 2q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.00× (z +8.1, q 5e-13, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.726× (z -3.8, q 0.094, down in 14 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Vilanterol (drug)]] 0.5 µM in 1 line (HCT15 0.0628×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SW48 0.0945×); [[Allantoin (drug)]] 0.05 µM in 1 line (Hs 766T 0.103×; ⚠ transcription drop); [[Resveratrol (drug)]] 5 µM in 1 line (SNU-1 0.231×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFRD2]] (+0.82, fdr 7e-06), [[DDX31]] (+0.79, fdr 7e-06), [[PRMT5]] (+0.79, fdr 7e-06); moves opposite to [[GNAS]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ALDH1B1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5894.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.00×** | +8.1 | 5e-13 | 33/47 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +6.7 | 4e-09 | 32/42 (NCI-H2030, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.51×** | +6.7 | 4e-09 | 28/47 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.76×** | +6.5 | 9e-09 | 26/38 (HT-29, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.65×** | +5.8 | 7e-07 | 30/43 (PANC-1, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +5.6 | 2e-06 | 27/46 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.70×** | +5.2 | 2e-05 | 24/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +5.2 | 2e-05 | 28/47 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.54×** | +4.8 | 1e-04 | 23/46 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.8 | 1e-04 | 2/48 (NCI-H1792, CHP-212) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.53×** | +4.7 | 1e-04 | 25/46 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.52×** | +4.7 | 2e-04 | 24/43 (A549, A-172, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.12×** | +4.6 | 2e-04 | 22/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.50×** | +4.5 | 3e-04 | 13/24 (SW480, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +3.9 | 0.004 | 22/47 (LOX-IMVI, SNU-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.005 | 17/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.66×** | +3.7 | 0.008 | 9/45 (NCI-H460, A498, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.73×** | +3.3 | 0.027 | 14/44 (RKO, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.71×** | +3.2 | 0.032 | 9/45 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.70×** | +3.2 | 0.033 | 6/39 (NCI-H460, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.68×** | +3.1 | 0.041 | 15/45 (NCI-H460, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +3.1 | 0.047 | 17/47 (A549, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.070 | 12/46 (SHP-77, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5894.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Vilanterol (drug)]] 0.5 µM in 1 line (HCT15 0.0628×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SW48 0.0945×); [[Allantoin (drug)]] 0.05 µM in 1 line (Hs 766T 0.103×; ⚠ transcription drop); [[Resveratrol (drug)]] 5 µM in 1 line (SNU-1 0.231×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.726×** | -3.8 | 0.094 | 14/46 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.734× | -3.5 | 0.13 | 18/46 (AN3 CA, LOX-IMVI, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.822× | -3.3 | 0.20 | 15/48 (A498, CHP-212, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5894. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 14.6 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0628× (z -11.8) |
| [[Hs 766T (line)]] | wt | 8.63 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.103× (z -9.7) ⚠ transcription drop |
| [[PANC-1 (line)]] | alt | 18.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.2) ⚠ cell-cycle shift, explains ~75% of this change | — |
| [[SHP-77 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SNU-1 (line)]] | wt | 15.5 | 0 | 1 | — | [[Resveratrol (drug)]] 5 µM 0.231× (z -9.0) |
| [[SW48 (line)]] | wt | 19.3 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0945× (z -10.0) |
| [[A-172 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5894), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFRD2]] | +0.82 | +0.83 / +0.77 | both halves | 7e-06 |  |
| [[DDX31]] | +0.79 | +0.77 / +0.75 | both halves | 7e-06 | STRING 511 |
| [[PRMT5]] | +0.79 | +0.82 / +0.72 | both halves | 7e-06 |  |
| [[BYSL]] | +0.77 | +0.73 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 999 |
| [[NOL6]] | +0.73 | +0.78 / +0.65 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 998 |
| [[NOP16]] | +0.73 | +0.71 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 756 |
| [[TRMT61A]] | +0.73 | +0.70 / +0.76 | both halves | 7e-06 | STRING 473 |
| [[UTP14A]] | +0.73 | +0.72 / +0.68 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 995 |
| [[BCS1L]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[MRPL15]] | +0.72 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[CLUH]] | +0.72 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[RRS1]] | +0.72 | +0.70 / +0.73 | both halves | 7e-06 | STRING 885 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.59 | -0.55 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALDH1B1]] | C | ALDH1B1 activity raises IMP4's level | lines that do not express ALDH1B1 (3) vs lines expressing it (47) | 1.61× lower at baseline in the lines without ALDH1B1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, CDC25A, NDC80; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.753). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.5, -38.4); signed map (-2.6, -44.3). **Vector** length 68.0, 13.4% of its response variance represented; |z| ≥ 3 in 758 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +3.2 | +6.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +2.8 | +4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +4.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.3 | +3.2 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.3 | +0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.1 | -3.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | IMP U3 small nucleolar ribonucleoprotein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.1 — chr2:130,342,877-130,347,967 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC19606, BXDC4 |
| Gene groups (HGNC) | Brix domain containing; MPP10 subcomplex |
| Hallmark sets | MYC_TARGETS_V2 |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96G21](https://www.uniprot.org/uniprotkb/Q96G21) (U3 small nucleolar ribonucleoprotein protein IMP4):

> Component of the 60-80S U3 small nucleolar ribonucleoprotein (U3 snoRNP). Required for the early cleavages during pre-18S ribosomal RNA processing. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and …

**Summary**, from NCBI Gene [92856](https://www.ncbi.nlm.nih.gov/gene/92856):

> The protein encoded by this gene, along with IMP3 and MPP10, is part of the 60-80S U3 small nucleolar ribonucleoprotein (U3 snoRNP) complex. This complex is necessary for the early cleavage steps of pre-18S ribosomal RNA processing. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:30856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30856) · Entrez [92856](https://www.ncbi.nlm.nih.gov/gene/92856) · UniProt [Q96G21](https://www.uniprot.org/uniprotkb/Q96G21) · Ensembl [ENSG00000136718](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136718)

## Data

Gene col 5894: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5894); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5894, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5894]; `tensor/DDL_lfc|DDL_z.npy` [5894]; `embed/gene_vectors.npy` [5894]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5894 or target_col == 5894). Every well: [[IMP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IMP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
