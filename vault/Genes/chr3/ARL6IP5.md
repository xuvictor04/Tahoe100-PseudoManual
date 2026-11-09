---
symbol: "ARL6IP5"
type: "gene"
col: 6924
ensembl_id: "ENSG00000144746"
name: "ARF like GTPase 6 interacting protein 5"
location: "3p14.1"
module: 45
arm: "+"
pooled_cpm: 76.91
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 6
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# ARL6IP5

*ARF like GTPase 6 interacting protein 5* — 3p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.62× (z +9.7, q 2e-19, up in 35 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 1.33× (z +4.2, q 0.004, up in 35 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SK-MEL-2 4.30×, NCI-H1573 4.34×, NCI-H460 3.35×, A-172 2.83×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 4.46×, A-172 3.10×, A498 3.42×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.511× (z -9.9, q 2e-20, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V1A]] (+0.70, fdr 1e-05), [[DCAF5]] (+0.68, fdr 7e-06), [[DSTN]] (+0.66, fdr 1e-05); moves opposite to [[PUS1]] (-0.64, fdr 7e-06), [[RRP7A]] (-0.64, fdr 1e-05), [[EEFSEC]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6924.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SK-MEL-2 4.30×, NCI-H1573 4.34×, NCI-H460 3.35×, A-172 2.83×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 4.46×, A-172 3.10×, A498 3.42×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.62×** | +9.7 | 2e-19 | 35/39 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.70×** | +8.8 | 4e-16 | 45/47 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +5.7 | 3e-06 | 35/40 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.004 | 35/47 (AsPC-1, hTERT-HPNE, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | 1.24× | +3.2 | 0.12 | 24/47 (MIA PaCa-2, NCI-H23, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | 1.36× | +3.2 | 0.12 | 26/47 (SW1417, C32, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.79× | +3.2 | 0.12 | 25/46 (HOP62, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6924.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.511×** | -9.9 | 2e-20 | 39/47 (SW 900, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.507×** | -7.1 | 4e-10 | 38/47 (RPMI-7951, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.555×** | -6.2 | 1e-07 | 34/47 (SW 900, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.570×** | -5.9 | 6e-07 | 32/47 (H4, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.625×** | -4.9 | 1e-04 | 32/47 (PANC-1, SW 900, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.661×** | -4.3 | 0.001 | 30/47 (SW 900, SNU-423, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.744× | -3.1 | 0.16 | 26/46 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6924. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 97.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 73.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 83.1 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.34× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -15.3) |
| [[NCI-H460 (line)]] | wt | 60.8 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -16.9) |
| [[SW 900 (line)]] | alt | 143 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -18.2) |
| [[LS 180 (line)]] | wt | 107 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.349× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 59.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -17.2) |
| [[A498 (line)]] | wt | 78.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -8.6) |
| [[C32 (line)]] | wt | 88.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 111 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.390× (z -8.9) |
| [[H4 (line)]] | wt | 67.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 127 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -17.3) |
| [[A549 (line)]] | wt | 72.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.31× (z +8.9) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 43.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.150× (z -11.3) |
| [[Hs 766T (line)]] | wt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -15.2) |
| [[HS-578T (line)]] | alt | 90.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -12.9) |
| [[HT-29 (line)]] | alt | 66.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -9.0) |
| [[J82 (line)]] | alt | 54.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +8.7) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 63.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 78.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -15.8) |
| [[NCI-H2347 (line)]] | alt | 237 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -11.8) |
| [[PANC-1 (line)]] | alt | 52.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 85.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 92.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -9.4) |
| [[A-427 (line)]] | wt | 14.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 109 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 76.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 76.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 52.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6924), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1A]] | +0.70 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[DCAF5]] | +0.68 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[DSTN]] | +0.66 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[USP33]] | +0.64 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[ERP29]] | +0.64 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[TMEM59]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[RELCH]] | +0.63 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[DNASE2]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[CAT]] | +0.60 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[SH3BGRL]] | +0.59 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[LMBRD1]] | +0.59 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[BEX3]] | +0.59 | +0.60 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUS1]] | -0.64 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[RRP7A]] | -0.64 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[EEFSEC]] | -0.61 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[METTL1]] | -0.59 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[ZNF121]] | -0.59 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[REXO1]] | -0.59 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[WDR4]] | -0.58 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[PWP2]] | -0.58 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[FAM83G]] | -0.58 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[EPOP]] | -0.57 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[FAAP100]] | -0.57 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[NIP7]] | -0.57 | -0.62 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ARL6IP5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAGEA4]] | B | MAGEA4 activity lowers ARL6IP5's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 1.77× higher at baseline in the lines without MAGEA4 | 0.088 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.686). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-2.1, -19.7); signed map (-24.6, -4.6). **Vector** length 101, 34.3% of its response variance represented; |z| ≥ 3 in 716 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +7.0 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.3 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.1 | +2.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.5 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.2 | +1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -7.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -1.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -9.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.6 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -1.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.7 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 6 interacting protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.1 — chr3:69,084,937-69,106,092 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRAF3, JWA, GTRAP3-18, DERP11, HSPC127, Yip6b |
| Gene groups (HGNC) | YIP superfamily |
| Reactome | 4 pathways, smallest: Glutamate Neurotransmitter Release Cycle; Neurotransmitter release cycle; Transmission across Chemical Synapses |
| Matched by | ensembl_id |

**Function**, from UniProt [O75915](https://www.uniprot.org/uniprotkb/O75915) (PRA1 family protein 3):

> Regulates intracellular concentrations of taurine and glutamate. Negatively modulates SLC1A1/EAAC1 glutamate transport activity by decreasing its affinity for glutamate in a PKC activity-dependent manner. Plays a role in the retention of SLC1A1/EAAC1 in the endoplasmic reticulum.

**Summary**, from NCBI Gene [10550](https://www.ncbi.nlm.nih.gov/gene/10550):

> Expression of this gene is affected by vitamin A. The encoded protein of this gene may be associated with the cytoskeleton. A similar protein in rats may play a role in the regulation of cell differentiation. The rat protein binds and inhibits the cell membrane glutamate transporter EAAC1. The expression of the rat gene is upregulated by retinoic acid, which results in a specific reduction in EAAC1-mediated glutamate transport. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16937](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16937) · Entrez [10550](https://www.ncbi.nlm.nih.gov/gene/10550) · UniProt [O75915](https://www.uniprot.org/uniprotkb/O75915) · Ensembl [ENSG00000144746](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144746)

## Data

Gene col 6924: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6924); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6924, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6924]; `tensor/DDL_lfc|DDL_z.npy` [6924]; `embed/gene_vectors.npy` [6924]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6924 or target_col == 6924). Every well: [[ARL6IP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL6IP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
