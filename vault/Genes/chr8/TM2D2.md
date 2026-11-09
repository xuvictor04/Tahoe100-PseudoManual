---
symbol: "TM2D2"
type: "gene"
col: 9811
ensembl_id: "ENSG00000169490"
name: "TM2 domain containing 2"
location: "8p11.22"
module: 7
arm: "+"
pooled_cpm: 10.51
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TM2D2

*TM2 domain containing 2* — 8p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.89× (z +10.9, q 5e-25, up in 46 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (Hs 766T 0.0788×, A549 0.126×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Decitabine (drug)]] 0.5 µM in 1 line (SW1417 0.0618×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 0.223×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FADD]] (+0.65, fdr 9e-06), [[TRADD]] (+0.64, fdr 8e-05), [[RIC8A]] (+0.64, fdr 2e-05); moves opposite to [[TMEM237]] (-0.55, fdr 1e-04), [[ARL5B]] (-0.54, fdr 4e-05), [[ARHGEF9]] (-0.53, fdr 5e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9811.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.89×** | +10.9 | 5e-25 | 46/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.64×** | +10.0 | 5e-21 | 41/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.46×** | +9.3 | 3e-18 | 39/46 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.41×** | +9.1 | 2e-17 | 39/46 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.40×** | +9.0 | 2e-17 | 41/47 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.47×** | +8.8 | 2e-16 | 41/46 (NCI-H2347, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +7.2 | 4e-11 | 29/44 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +7.0 | 2e-10 | 29/36 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +5.9 | 2e-07 | 29/46 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.68×** | +5.4 | 4e-06 | 25/43 (J82, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +5.0 | 3e-05 | 23/48 (CFPAC-1, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +4.8 | 6e-05 | 27/47 (J82, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.5 | 4e-04 | 20/48 (Hs 766T, CFPAC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.54×** | +4.3 | 7e-04 | 5/18 (A498, PANC-1, …) | top dose only | composition shift; position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.17×** | +4.2 | 0.001 | 14/34 (NCI-H2347, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +3.9 | 0.003 | 16/46 (J82, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.018 | 12/45 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +3.0 | 0.076 | 8/47 (A549, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9811.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (Hs 766T 0.0788×, A549 0.126×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Decitabine (drug)]] 0.5 µM in 1 line (SW1417 0.0618×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 0.223×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | 0.731× | -3.1 | 0.53 | 12/45 (BT-474, A-172, …) | top dose only |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.745× | -3.0 | 0.53 | 8/48 (Hs 766T, J82, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9811. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 25.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 13.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0788× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 4.30 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0721× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 13.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.86× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 4.50 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0618× (z -10.5) |
| [[A-427 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.69 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9811), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FADD]] | +0.65 | +0.57 / +0.69 | both halves | 9e-06 |  |
| [[TRADD]] | +0.64 | +0.37 / +0.65 | both halves | 8e-05 |  |
| [[RIC8A]] | +0.64 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[TMEM115]] | +0.63 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[PSMB6]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[PSMB4]] | +0.62 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[TRAPPC2B]] | +0.61 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[BRF2]] | +0.61 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[RAB5IF]] | +0.61 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[TIMM22]] | +0.60 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[CPTP]] | +0.60 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[JOSD2]] | +0.60 | +0.35 / +0.64 | both halves | 1e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM237]] | -0.55 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[ARL5B]] | -0.54 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[ARHGEF9]] | -0.53 | -0.24 / -0.62 | both halves | 5e-04 |  |
| [[SRSF1]] | -0.51 | -0.21 / -0.55 | both halves | 7e-04 |  |
| [[FAM81A]] | -0.50 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[HNRNPD]] | -0.49 | -0.27 / -0.54 | both halves | 3e-04 |  |
| [[SF1]] | -0.49 | -0.17 / -0.60 | ⚠ one half (not replicated) | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TM2D2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP1A]] | B | MAP1A activity lowers TM2D2's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 1.26× higher at baseline in the lines without MAP1A | 0.096 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.473). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-43.6, -4.7); signed map (-23.2, -24.5). **Vector** length 73.5, 14.4% of its response variance represented; |z| ≥ 3 in 855 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.7 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.6 | +9.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.5 | +8.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.3 | +4.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +5.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +4.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.1 | +0.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | -0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | -5.0 | +4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -3.0 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.0 | -1.2 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | TM2 domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.22 — chr8:38,988,808-38,996,824 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BLP1 |
| Gene groups (HGNC) | TM2 domain containing family |
| Matched by | ensembl_id |

UniProt [Q9BX73](https://www.uniprot.org/uniprotkb/Q9BX73) carries no function annotation.

**Summary**, from NCBI Gene [83877](https://www.ncbi.nlm.nih.gov/gene/83877):

> The protein encoded by this gene contains a structural module related to that of the seven transmembrane domain G protein-coupled receptor superfamily. This protein has sequence and structural similarities to the beta-amyloid binding protein (BBP), but, unlike BBP, it does not regulate a response to beta-amyloid peptide. This protein may have regulatory roles in cell death or proliferation signal cascades. This gene has multiple alternatively spliced transcript variants which encode two …

**Accessions** — [HGNC:24127](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24127) · Entrez [83877](https://www.ncbi.nlm.nih.gov/gene/83877) · UniProt [Q9BX73](https://www.uniprot.org/uniprotkb/Q9BX73) · Ensembl [ENSG00000169490](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169490)

## Data

Gene col 9811: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9811); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9811, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9811]; `tensor/DDL_lfc|DDL_z.npy` [9811]; `embed/gene_vectors.npy` [9811]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9811 or target_col == 9811). Every well: [[TM2D2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TM2D2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
