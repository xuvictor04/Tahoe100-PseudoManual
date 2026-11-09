---
symbol: "USP34-DT"
type: "gene"
col: 15672
ensembl_id: "ENSG00000270820"
name: "USP34 divergent transcript"
location: "2p15"
module: 35
arm: "+"
pooled_cpm: 9.57
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# USP34-DT

*USP34 divergent transcript* — 2p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.78× (z +21.9, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.583× (z -8.2, q 2e-13, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP4S1]] (+0.77, fdr 1e-05), [[SPATA1]] (+0.77, fdr 7e-06), [[KMT2E-AS1]] (+0.76, fdr 1e-05); moves opposite to [[RRP1B]] (-0.68, fdr 3e-05), [[THEM6]] (-0.65, fdr 1e-04), [[C20orf27]] (-0.63, fdr 4e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZNF846]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15672.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.78×** | +21.9 | 0e+00 | 43/45 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +10.5 | 2e-23 | 32/43 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +10.2 | 5e-22 | 15/23 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +9.8 | 2e-20 | 29/45 (NCI-H2030, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +9.1 | 9e-18 | 25/36 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +8.1 | 7e-14 | 26/42 (SW1417, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.6 | 1e-06 | 19/48 (HEC-1-A, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +5.3 | 1e-05 | 7/19 (J82, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +5.1 | 2e-05 | 18/45 (SNU-423, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +5.1 | 2e-05 | 17/47 (CFPAC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +4.7 | 1e-04 | 12/31 (BT-474, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +4.1 | 0.002 | 7/39 (HOP62, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.003 | 10/44 (HOP62, RKO, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.055 | 6/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15672.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.583×** | -8.2 | 2e-13 | 26/47 (NCI-H1792, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.691×** | -5.6 | 6e-06 | 18/47 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.707×** | -5.2 | 3e-05 | 19/47 (NCI-H1792, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.737×** | -4.6 | 5e-04 | 16/47 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.750×** | -4.4 | 0.002 | 16/46 (NCI-H1792, H4, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.767×** | -4.0 | 0.006 | 15/42 (LS 180, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.793×** | -3.5 | 0.036 | 10/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | 0.675× | -3.1 | 0.13 | 9/38 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.868× | -3.0 | 0.16 | 10/48 (C32, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15672. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 6.62 | 0 | 3 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0834× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 6.58 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +10.5) | [[AZD2858 (drug)]] 0.5 µM 0.0881× (z -8.8) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 8.81 | 0 | 2 (1 ⚠) | — | [[Saquinavir (drug)]] 0.5 µM 0.108× (z -8.8) |
| [[SW480 (line)]] | alt | 8.76 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +11.5) | — |
| [[A498 (line)]] | wt | 7.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 7.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 8.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +9.9) | — |
| [[KATO III (line)]] | alt | 14.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 5.44 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0712× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.280× (z -8.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Panc 03.27 (line)]] | alt | 5.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.07× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 6.34 | 0 | 1 | — | [[Terfenadine (drug)]] 0.5 µM 0.0989× (z -8.9) |
| [[SW1417 (line)]] | alt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +9.9) | — |
| [[A-172 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15672), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP4S1]] | +0.77 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[SPATA1]] | +0.77 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[KMT2E-AS1]] | +0.76 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[LINC01090]] | +0.75 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[SPAG5-AS1]] | +0.75 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[SPEN-AS1]] | +0.75 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[ZNF213-AS1]] | +0.75 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[GPAT4-AS1]] | +0.73 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[ZNF341-AS1]] | +0.73 | +0.67 / +0.40 | both halves | 5e-05 |  |
| [[PBLD]] | +0.72 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[PPP1R12A-AS2]] | +0.72 | +0.69 / +0.38 | both halves | 7e-05 |  |
| [[MED28-DT]] | +0.72 | +0.62 / +0.52 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP1B]] | -0.68 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[THEM6]] | -0.65 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[C20orf27]] | -0.63 | -0.65 / -0.25 | both halves | 4e-04 |  |
| [[SMYD3]] | -0.62 | -0.49 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers USP34-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises USP34-DT's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FAM106A]] | B | FAM106A activity lowers USP34-DT's level | lines that do not express FAM106A (30) vs lines expressing it (20) | 1.26× higher at baseline in the lines without FAM106A | 0.097 | ⚠ within organs, on part of the lines; also absent: CCDC144BP, SULF1, POSTN |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF846]] | C | USP34-DT's natural level strengthens ZNF846's drug response | USP34-DT's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.17; direction not clear | 0.024 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.792). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (9.6, 21.6); signed map (28.9, -2.4). **Vector** length 78.9, 14.0% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +21.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +9.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.4 | +5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +5.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +2.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.5 | -5.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.1 | -8.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.7 | -5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.5 | -4.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.4 | -4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | -1.5 | -1.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | USP34 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p15 — chr2:61,471,188-61,484,130 (+) |
| Ensembl biotype | lncRNA |
| Also known as | AC016727.1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55262](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55262) · Entrez [105377633](https://www.ncbi.nlm.nih.gov/gene/105377633) · Ensembl [ENSG00000270820](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000270820)

## Data

Gene col 15672: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15672); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15672, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15672]; `tensor/DDL_lfc|DDL_z.npy` [15672]; `embed/gene_vectors.npy` [15672]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15672 or target_col == 15672). Every well: [[USP34-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP34-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
