---
symbol: "POLR2F"
type: "gene"
col: 1877
ensembl_id: "ENSG00000100142"
name: "RNA polymerase II, I and III subunit F"
location: "22q13.1"
module: 3
arm: "+"
pooled_cpm: 28.11
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# POLR2F

*RNA polymerase II, I and III subunit F* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.67× (z +12.0, q 3e-30, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.99× (z +11.9, q 5e-30, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.717× (z -5.8, q 4e-06, down in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SK-MEL-2 0.448×, HEC-1-A 0.489×, CFPAC-1 0.400×); [[Tolmetin (drug)]] 5 µM in 1 line (NCI-H661 0.0701×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHPS]] (+0.77, fdr 7e-06), [[MARK4]] (+0.66, fdr 1e-05), [[ASB16-AS1]] (+0.63, fdr 1e-05); moves opposite to [[DCLRE1A]] (-0.60, fdr 2e-05), [[LACC1]] (-0.58, fdr 3e-05), [[ZXDB]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1877.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.67×** | +12.0 | 3e-30 | 44/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +11.9 | 5e-30 | 43/48 (A498, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.41×** | +10.7 | 2e-24 | 44/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.34×** | +10.3 | 6e-23 | 38/42 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.28×** | +10.0 | 1e-21 | 41/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.95×** | +7.8 | 4e-13 | 30/38 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +6.7 | 2e-09 | 32/44 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.67×** | +6.0 | 1e-07 | 33/47 (SW480, A498, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.60×** | +5.7 | 7e-07 | 31/46 (SW480, PANC-1, …) | top dose only | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.79×** | +5.1 | 2e-05 | 32/48 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.3 | 8e-04 | 21/48 (HS-578T, PANC-1, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.64×** | +4.3 | 8e-04 | 26/47 (A-427, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.62×** | +4.2 | 0.001 | 28/46 (NCI-H460, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.61×** | +4.1 | 0.001 | 27/47 (HT-29, C-33 A, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.60×** | +4.1 | 0.002 | 24/48 (NCI-H460, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.012 | 17/48 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.025 | 16/47 (KATO III, SNU-423, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.045 | 15/46 (A-172, HCT15, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.045 | 13/48 (C32, KATO III, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.054 | 13/48 (A-172, NCI-H2030, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.41×** | +3.0 | 0.056 | 14/48 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1877.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SK-MEL-2 0.448×, HEC-1-A 0.489×, CFPAC-1 0.400×); [[Tolmetin (drug)]] 5 µM in 1 line (NCI-H661 0.0701×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.717×** | -5.8 | 4e-06 | 27/47 (SK-MEL-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Folic acid (drug)]] 5 µM |  | 0.826× | -3.3 | 0.26 | 16/48 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.772× | -3.2 | 0.29 | 18/47 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1877. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 38.9 | 6 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.07× (z +11.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 39.8 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 17.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +10.2) | — |
| [[A498 (line)]] | wt | 27.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +11.8) | — |
| [[A549 (line)]] | wt | 14.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 23.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -8.9) |
| [[COLO 205 (line)]] | alt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 30.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +8.8) | — |
| [[KATO III (line)]] | alt | 38.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 22.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2030 (line)]] | alt | 34.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +8.8) | — |
| [[NCI-H661 (line)]] | alt | 34.2 | 0 | 1 | — | [[Tolmetin (drug)]] 5 µM 0.0701× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 21.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 30.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 162 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -10.0) |
| [[A-172 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 98.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1877), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHPS]] | +0.77 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[MARK4]] | +0.66 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ASB16-AS1]] | +0.63 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[SMARCD2]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |
| [[PTOV1]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 | same gene group |
| [[SNHG25]] | +0.63 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[DEXI]] | +0.62 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[ATPAF2]] | +0.61 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[CD81]] | +0.61 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[KIAA2013]] | +0.61 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[TAF11]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins; STRING 900 |
| [[PTDSS2]] | +0.60 | +0.48 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCLRE1A]] | -0.60 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[LACC1]] | -0.58 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ZXDB]] | -0.57 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[PPID]] | -0.56 | -0.62 / -0.33 | both halves | 1e-04 | pathway: ESR-mediated signaling |
| [[TIGD2]] | -0.56 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[LGALSL]] | -0.55 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[ZNF678]] | -0.55 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[ZNF641]] | -0.53 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[HSPB8]] | -0.53 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[YTHDC2]] | -0.53 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[DSP]] | -0.53 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[PDAP1]] | -0.52 | -0.44 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers POLR2F's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.508). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-11.9, -3.1); signed map (-41.2, 3.1). **Vector** length 75.8, 17.8% of its response variance represented; |z| ≥ 3 in 795 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +4.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +3.5 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +11.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.9 | +3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.8 | +3.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +5.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.8 | +4.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.4 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | +0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | +0.3 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -1.4 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.8 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.4 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase II, I and III subunit F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:37,952,607-38,041,915 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPB6, HRBP14.4 |
| Gene groups (HGNC) | RNA polymerase subunits; MicroRNA protein coding host genes |
| Hallmark sets | DNA_REPAIR, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 94 pathways, smallest: RNA Polymerase III Chain Elongation; Signaling by FGFR2 IIIa TM; PIWI-interacting RNA (piRNA) biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P61218](https://www.uniprot.org/uniprotkb/P61218) (DNA-directed RNA polymerases I, II, and III subunit RPABC2):

> DNA-dependent RNA polymerase catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. Common component of RNA polymerases I, II, and III which synthesize ribosomal RNA precursors, mRNA precursors and many functional non-coding RNAs, and small RNAs, such as 5S rRNA and tRNAs, respectively. Pol II is the central component of the basal RNA polymerase II transcription machinery. Pols are composed of mobile elements that move relative to each other. In …

**Summary**, from NCBI Gene [5435](https://www.ncbi.nlm.nih.gov/gene/5435):

> This gene encodes the sixth largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. In yeast, this polymerase subunit, in combination with at least two other subunits, forms a structure that stabilizes the transcribing polymerase on the DNA template. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:9193](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9193) · Entrez [5435](https://www.ncbi.nlm.nih.gov/gene/5435) · UniProt [P61218](https://www.uniprot.org/uniprotkb/P61218) · Ensembl [ENSG00000100142](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100142)

## Data

Gene col 1877: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1877); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1877, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1877]; `tensor/DDL_lfc|DDL_z.npy` [1877]; `embed/gene_vectors.npy` [1877]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1877 or target_col == 1877). Every well: [[POLR2F — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR2F.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
