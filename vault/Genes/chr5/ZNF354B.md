---
symbol: "ZNF354B"
type: "gene"
col: 10918
ensembl_id: "ENSG00000178338"
name: "zinc finger protein 354B"
location: "5q35.3"
module: 1
arm: "+"
pooled_cpm: 15.07
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ZNF354B

*zinc finger protein 354B* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.72× (z +12.0, q 2e-30, up in 35 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-172 0.133×, MIA PaCa-2 0.243×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.166×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.0754×; ⚠ cell-cycle shift, explains ~33% of this change); [[Radotinib (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0699×); [[Thymol (drug)]] 0.5 µM in 1 line (SW48 0.102×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (AN3 CA 0.0816×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF354A]] (+0.68, fdr 7e-06), [[POGK]] (+0.67, fdr 7e-06), [[ZNF507]] (+0.67, fdr 7e-06); moves opposite to [[DPM1]] (-0.60, fdr 1e-05), [[SLC39A9]] (-0.59, fdr 1e-05), [[GBF1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CA9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10918.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +12.0 | 2e-30 | 35/47 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.74×** | +8.3 | 3e-14 | 29/48 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +6.6 | 8e-09 | 27/47 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +5.2 | 2e-05 | 19/42 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.23×** | +4.6 | 5e-04 | 19/48 (A498, CFPAC-1, …) | top dose only | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +4.4 | 1e-03 | 16/47 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.3 | 0.001 | 17/47 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 0.002 | 17/48 (NCI-H1573, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.007 | 18/47 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.009 | 8/48 (CFPAC-1, SW48, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.27×** | +3.7 | 0.010 | 10/47 (NCI-H2347, RPMI-7951, …) | rises with dose | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | 1.18× | +3.6 | 0.015 | 6/48 (NCI-H2030, NCI-H1792, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.032 | 12/47 (NCI-H2030, LOX-IMVI, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.037 | 11/47 (HEC-1-A, BT-474, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.26×** | +3.3 | 0.037 | 7/31 (CFPAC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.064 | 16/47 (HOP62, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10918.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-172 0.133×, MIA PaCa-2 0.243×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.166×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.0754×; ⚠ cell-cycle shift, explains ~33% of this change); [[Radotinib (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0699×); [[Thymol (drug)]] 0.5 µM in 1 line (SW48 0.102×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (AN3 CA 0.0816×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.738× | -3.4 | 0.18 | 16/44 (NCI-H1792, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | 0.808× | -3.4 | 0.18 | 18/46 (NCI-H460, NCI-H1573, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.746× | -3.3 | 0.18 | 14/46 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.752× | -3.2 | 0.18 | 14/46 (AN3 CA, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.805× | -3.1 | 0.20 | 13/44 (SW48, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10918. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 16.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.334× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[Panc 03.27 (line)]] | alt | 23.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW48 (line)]] | wt | 23.7 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0754× (z -12.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Thymol (drug)]] 0.5 µM 0.102× (z -10.4) |
| [[AN3 CA (line)]] | alt | 42.1 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0816× (z -9.8) |
| [[COLO 205 (line)]] | alt | 8.23 | 0 | 1 | — | [[Cilostazol (drug)]] 0.05 µM 0.0684× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 21.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.0) | — |
| [[J82 (line)]] | alt | 18.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 7.75 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0699× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 16.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +10.0) | — |
| [[A-427 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10918), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF354A]] | +0.68 | +0.71 / +0.72 | both halves | 7e-06 | same gene group |
| [[POGK]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 | same gene group |
| [[ZNF507]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 | same gene group |
| [[NOP14]] | +0.66 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[NUDT19]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[DCAF17]] | +0.64 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ZNF649]] | +0.62 | +0.66 / +0.53 | both halves | 1e-05 | same gene group |
| [[ZNF239]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 | same gene group |
| [[COA7]] | +0.62 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[ANKRD40]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[ZBTB24]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 | same gene group |
| [[DIS3L]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPM1]] | -0.60 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[SLC39A9]] | -0.59 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[GBF1]] | -0.58 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[SAR1A]] | -0.58 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[TMED9]] | -0.56 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[P4HA1]] | -0.55 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[COPA]] | -0.55 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[RAB1A]] | -0.55 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[MXD1]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[QSOX1]] | -0.55 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[COX7A2]] ⚠ | -0.53 | -0.44 / -0.49 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[FAM162A]] | -0.53 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[NDRG1]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA9]] | B | CA9 activity lowers ZNF354B's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.43× higher at baseline in the lines without CA9 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.9, -37.9); signed map (0.6, -40.6). **Vector** length 68.9, 11.0% of its response variance represented; |z| ≥ 3 in 871 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +5.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | +12.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.6 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +2.6 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +1.3 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.6 | +1.6 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.4 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.0 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -1.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 354B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:178,859,953-178,888,122 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KID2, FLJ25008 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LW1](https://www.uniprot.org/uniprotkb/Q96LW1) (Zinc finger protein 354B):

> Transcriptional repressor that binds DNA upon activation by RAS proteins signal transduction to initiate transcriptional silencing through the recruitment of additional DNA-binding proteins, multisubunit complexes and chromatin-modifying activities to establish a platform for DNMT1 recruitment.

**Summary**, from NCBI Gene [117608](https://www.ncbi.nlm.nih.gov/gene/117608):

> Predicted to enable several functions, including DNA-binding transcription factor activity, RNA polymerase II-specific; RNA polymerase II cis-regulatory region sequence-specific DNA binding activity; and transcription corepressor activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to act upstream of or within negative regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul …

**Accessions** — [HGNC:17197](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17197) · Entrez [117608](https://www.ncbi.nlm.nih.gov/gene/117608) · UniProt [Q96LW1](https://www.uniprot.org/uniprotkb/Q96LW1) · Ensembl [ENSG00000178338](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178338)

## Data

Gene col 10918: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10918); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10918, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10918]; `tensor/DDL_lfc|DDL_z.npy` [10918]; `embed/gene_vectors.npy` [10918]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10918 or target_col == 10918). Every well: [[ZNF354B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF354B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
