---
symbol: "MED30"
type: "gene"
col: 9004
ensembl_id: "ENSG00000164758"
name: "mediator complex subunit 30"
location: "8q24.11"
module: 45
arm: "+"
pooled_cpm: 16.72
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# MED30

*mediator complex subunit 30* — 8q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.57× (z +7.3, q 2e-10, up in 27 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.58× (z +3.9, q 0.012, up in 15 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.527× (z -10.4, q 2e-22, down in 42 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.666× (z -9.3, q 4e-18, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TERF1]] (+0.76, fdr 7e-06), [[AUH]] (+0.73, fdr 7e-06), [[FBXO3]] (+0.72, fdr 7e-06); moves opposite to [[SLC2A9]] (-0.64, fdr 3e-05), [[IDI2-AS1]] (-0.62, fdr 2e-05), [[CYREN]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9004.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +7.3 | 2e-10 | 27/46 (LS 180, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.39×** | +5.3 | 3e-05 | 22/48 (LS 180, PANC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +5.2 | 4e-05 | 15/32 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.7 | 5e-04 | 15/44 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.58×** | +3.9 | 0.012 | 15/48 (A498, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.028 | 14/47 (LoVo, LOX-IMVI, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.24×** | +3.6 | 0.028 | 15/42 (HT-29, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.054 | 8/47 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.48×** | +3.3 | 0.054 | 12/45 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | 1.21× | +3.1 | 0.13 | 12/46 (HT-29, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9004.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.527×** | -10.4 | 2e-22 | 42/47 (NCI-H2347, NCI-H2030, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.666×** | -9.3 | 4e-18 | 32/46 (HS-578T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.890× | -6.6 | 1e-08 | 11/48 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -5.9 | 4e-07 | 20/46 (NCI-H23, SW 900, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.703×** | -5.5 | 5e-06 | 19/47 (HS-578T, HT-29, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[EX229 (drug)]] 5 µM |  | **0.530×** | -5.4 | 7e-06 | 21/46 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.534×** | -5.3 | 9e-06 | 24/47 (SK-MEL-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.742×** | -4.8 | 1e-04 | 12/47 (HOP62, SNU-423, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.814×** | -4.7 | 2e-04 | 17/48 (SNU-423, RKO, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.576×** | -4.7 | 2e-04 | 16/44 (SW 900, AN3 CA, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.585×** | -4.5 | 3e-04 | 14/46 (SW 900, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.827×** | -4.3 | 7e-04 | 23/46 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.601×** | -4.3 | 7e-04 | 17/45 (Hs 766T, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.775×** | -4.1 | 0.002 | 20/46 (NCI-H1573, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.865× | -3.3 | 0.038 | 8/48 (RPMI-7951, SW 900, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.828×** | -3.0 | 0.080 | 5/48 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Volasertib (drug)]] 0.5 µM |  | **0.768×** | -3.0 | 0.080 | 4/48 (SW 1271, SW 900, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9004. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 33.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -10.0) |
| [[SW 900 (line)]] | alt | 22.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.285× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 16.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -13.0) |
| [[CFPAC-1 (line)]] | alt | 14.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -9.7) |
| [[H4 (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0693× (z -9.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HS-578T (line)]] | alt | 30.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 20.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -11.9) |
| [[LS 180 (line)]] | wt | 18.0 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.45× (z +9.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -8.5) |
| [[SNU-423 (line)]] | alt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.6) |
| [[A-172 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9004), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERF1]] | +0.76 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[AUH]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[FBXO3]] | +0.72 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[CCDC28A]] | +0.72 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[PLEKHM3]] | +0.69 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[LMBRD1]] | +0.69 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[SNX1]] | +0.69 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[OSBPL9]] | +0.67 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[HACL1]] | +0.66 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[DPY30]] | +0.66 | +0.60 / +0.52 | both halves | 1e-05 | pathway: Epigenetic regulation by WDR5-containing histone modifying complexes |
| [[DNAJC19]] | +0.65 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[TMEM185A]] | +0.65 | +0.67 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC2A9]] | -0.64 | -0.69 / -0.45 | both halves | 3e-05 |  |
| [[IDI2-AS1]] | -0.62 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[CYREN]] | -0.61 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[PPIEL-1]] | -0.61 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[CSTF3]] | -0.60 | -0.62 / -0.38 | both halves | 6e-05 |  |
| [[PPIEL]] | -0.58 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[PCSK6]] | -0.58 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[DNAJC11]] | -0.58 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[PCBP1-AS1]] | -0.58 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[PARD6G-AS1]] | -0.57 | -0.60 / -0.36 | both halves | 1e-04 |  |
| [[NPIPB4]] | -0.57 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[MPDU1]] | -0.57 | -0.57 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MED30's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (4.8, -46.8); signed map (-29.9, -8.2). **Vector** length 84.3, 17.1% of its response variance represented; |z| ≥ 3 in 781 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +3.2 | +3.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.1 | +3.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +0.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +0.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.1 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -9.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.2 | -4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -4.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.8 | -5.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.7 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 30 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.11 — chr8:117,520,713-117,540,262 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRAP25; previously THRAP6 |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 13 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96HR3](https://www.uniprot.org/uniprotkb/Q96HR3) (Mediator of RNA polymerase II transcription subunit 30):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [90390](https://www.ncbi.nlm.nih.gov/gene/90390):

> The multiprotein TRAP/Mediator complex facilitates gene expression through a wide variety of transcriptional activators. MED30 is a component of this complex that appears to be metazoan specific (Baek et al., 2002 [PubMed 11909976]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:23032](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23032) · Entrez [90390](https://www.ncbi.nlm.nih.gov/gene/90390) · UniProt [Q96HR3](https://www.uniprot.org/uniprotkb/Q96HR3) · Ensembl [ENSG00000164758](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164758)

## Data

Gene col 9004: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9004); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9004, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9004]; `tensor/DDL_lfc|DDL_z.npy` [9004]; `embed/gene_vectors.npy` [9004]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9004 or target_col == 9004). Every well: [[MED30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
