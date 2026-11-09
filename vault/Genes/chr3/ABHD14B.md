---
symbol: "ABHD14B"
type: "gene"
col: 3587
ensembl_id: "ENSG00000114779"
name: "abhydrolase domain containing 14B"
location: "3p21.2"
module: 29
arm: "+"
pooled_cpm: 9.49
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# ABHD14B

*abhydrolase domain containing 14B* — 3p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.73× (z +13.8, q 2e-40, up in 31 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.30× (z +5.1, q 4e-05, up in 20 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 4.20×, NCI-H1792 7.80×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.532× (z -12.2, q 1e-31, down in 29 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GAA]] (+0.59, fdr 1e-05), [[ATRAID]] (+0.57, fdr 3e-05), [[MDH2]] (+0.56, fdr 1e-05); moves opposite to [[PSMA7]] (-0.51, fdr 4e-05), [[EIF5B]] (-0.47, fdr 1e-04), [[UPF3B]] (-0.46, fdr 3e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CRTAP]] → it (grade C ⚠); 1 goes from it, the strongest it → [[EIF5B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3587.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 4.20×, NCI-H1792 7.80×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.73×** | +13.8 | 2e-40 | 31/33 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +11.9 | 2e-30 | 16/19 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +9.3 | 4e-18 | 20/25 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +7.5 | 1e-11 | 24/36 (NCI-H1573, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +5.1 | 4e-05 | 20/47 (SW 900, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +4.3 | 0.001 | 19/40 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.8 | 0.012 | 1/16 (NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | 1.54× | +3.1 | 0.13 | 3/43 (HEC-1-A, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, none with an alert; shown: the 15 strongest. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3587.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.532×** | -12.2 | 1e-31 | 29/43 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.490×** | -9.8 | 4e-20 | 29/42 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.606×** | -6.9 | 1e-09 | 25/47 (PANC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.619×** | -6.3 | 4e-08 | 18/44 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.663×** | -5.3 | 1e-05 | 18/43 (J82, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.697×** | -5.0 | 7e-05 | 18/47 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.705×** | -4.8 | 1e-04 | 17/47 (AN3 CA, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.708×** | -4.8 | 1e-04 | 19/45 (HT-29, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.725×** | -4.2 | 0.002 | 16/45 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.749×** | -4.0 | 0.004 | 16/46 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.750×** | -3.9 | 0.004 | 18/46 (SW480, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.757×** | -3.8 | 0.006 | 15/46 (SNU-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.602×** | -3.6 | 0.011 | 8/44 (HT-29, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.768×** | -3.6 | 0.012 | 15/46 (H4, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.778×** | -3.4 | 0.022 | 15/47 (LOX-IMVI, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3587. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.79 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -9.5) |
| [[RKO (line)]] | wt | 10.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0970× (z -11.1) |
| [[A-172 (line)]] | wt | 6.22 | 0 | 1 | — | [[Clofarabine (drug)]] 5 µM 0.0602× (z -12.1) |
| [[A-427 (line)]] | wt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -9.1) |
| [[A549 (line)]] | wt | 7.23 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -8.7) |
| [[BT-474 (line)]] | alt | 4.39 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.5 µM 0.0501× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 6.57 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.80× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 15.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -11.0) |
| [[PANC-1 (line)]] | alt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -11.8) |
| [[SW 900 (line)]] | alt | 4.90 | 0 | 1 | — | [[Furosemide (drug)]] 0.5 µM 0.0603× (z -8.9) |
| [[SW480 (line)]] | alt | 9.40 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.238× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3587), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GAA]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ATRAID]] | +0.57 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[MDH2]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[EIF2D]] | +0.56 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[STRADB]] | +0.55 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[FAM210B]] | +0.55 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[DPP7]] | +0.54 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[CIPC]] | +0.53 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[SNHG16]] | +0.53 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[CREG1]] | +0.53 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[GSTK1]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 | pathway: Biological oxidations |
| [[SUMF2]] | +0.52 | +0.55 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMA7]] | -0.51 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[EIF5B]] | -0.47 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[UPF3B]] | -0.46 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[POLR2J3-1]] | -0.43 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[RBM25]] | -0.43 | -0.47 / -0.37 | both halves | 9e-05 |  |
| [[PIGBOS1]] | -0.43 | -0.38 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRTAP]] | C | CRTAP activity raises ABHD14B's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.61× lower at baseline in the lines without CRTAP | 0.061 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EIF5B]] | C | ABHD14B's natural level weakens EIF5B's drug response | ABHD14B's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.08; direction not clear | 0.059 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.6, -19.6); signed map (-22.0, -40.5). **Vector** length 54.3, 7.61% of its response variance represented; |z| ≥ 3 in 795 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +9.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.2 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +13.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | -0.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.3 | +2.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.9 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.4 | -9.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -3.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.0 | -1.4 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -0.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | abhydrolase domain containing 14B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.2 — chr3:51,968,510-51,983,409 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC15429, CIB |
| Gene groups (HGNC) | Abhydrolase domain containing |
| Reactome | 3 pathways, smallest: Cytosolic sulfonation of small molecules; Phase II - Conjugation of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IU4](https://www.uniprot.org/uniprotkb/Q96IU4) (Putative protein-lysine deacylase ABHD14B):

> Acts as an atypical protein-lysine deacetylase in vitro. Catalyzes the deacetylation of lysine residues using CoA as substrate, generating acetyl-CoA and the free amine of protein-lysine residues. Additional experiments are however required to confirm the protein-lysine deacetylase activity in vivo (Probable). Has hydrolase activity towards various surrogate p-nitrophenyl (pNp) substrates, such as pNp-butyrate, pNp-acetate and pNp-octanoate in vitro, with a strong preference for pNp-acetate. …

**Summary**, from NCBI Gene [84836](https://www.ncbi.nlm.nih.gov/gene/84836):

> Enables hydrolase activity. Involved in positive regulation of transcription by RNA polymerase II. Located in cytosol; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28235](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28235) · Entrez [84836](https://www.ncbi.nlm.nih.gov/gene/84836) · UniProt [Q96IU4](https://www.uniprot.org/uniprotkb/Q96IU4) · Ensembl [ENSG00000114779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114779)

## Data

Gene col 3587: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3587); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3587, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3587]; `tensor/DDL_lfc|DDL_z.npy` [3587]; `embed/gene_vectors.npy` [3587]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3587 or target_col == 3587). Every well: [[ABHD14B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD14B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
