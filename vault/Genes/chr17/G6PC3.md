---
symbol: "G6PC3"
type: "gene"
col: 6504
ensembl_id: "ENSG00000141349"
name: "glucose-6-phosphatase catalytic subunit 3"
location: "17q21.31"
module: 29
arm: "+"
pooled_cpm: 8.45
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# G6PC3

*glucose-6-phosphatase catalytic subunit 3* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.21× (z +14.1, q 2e-42, up in 27 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.33× (z +4.8, q 2e-04, up in 17 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.756× (z -4.8, q 8e-04, down in 23 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.291×, SK-MEL-2 0.253×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0682×); [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (Hs 766T 0.104×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATRAID]] (+0.62, fdr 1e-05), [[CYB561A3]] (+0.59, fdr 1e-05), [[TSPAN6]] (+0.58, fdr 3e-05); moves opposite to [[SNHG6]] (-0.51, fdr 3e-05), [[RPS6]] (-0.49, fdr 3e-05, ⚠ RPS6 in the vector space only through flagged drug-doses), [[RPL37A]] (-0.47, fdr 6e-05, ⚠ RPL37A in the vector space only through flagged drug-doses), [[NRTN]] (-0.44, fdr 3e-04), [[NSA2]] (-0.43, fdr 7e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6504.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.21×** | +14.1 | 2e-42 | 27/29 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.01×** | +12.8 | 4e-35 | 15/17 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.02×** | +7.9 | 7e-13 | 18/22 (SW480, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +5.4 | 1e-05 | 20/33 (KATO III, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +4.8 | 2e-04 | 17/48 (A-427, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.50×** | +4.7 | 3e-04 | 17/44 (A-172, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.30×** | +4.5 | 6e-04 | 20/45 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.36×** | +3.7 | 0.013 | 16/37 (KATO III, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.026 | 13/42 (A549, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.72×** | +3.4 | 0.034 | 5/36 (SHP-77, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.22×** | +3.4 | 0.034 | 7/48 (MIA PaCa-2, NCI-H661, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.34×** | +3.4 | 0.034 | 11/44 (HOP62, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.067 | 10/48 (A-427, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6504.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.291×, SK-MEL-2 0.253×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0682×); [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (Hs 766T 0.104×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.756×** | -4.8 | 8e-04 | 23/45 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.717×** | -3.9 | 0.029 | 16/45 (COLO 205, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6504. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +9.1) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 6.29 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.104× (z -8.8) |
| [[KATO III (line)]] | alt | 10.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.91× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 3.09 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0682× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -9.6) |
| [[SW480 (line)]] | alt | 7.08 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6504), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATRAID]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[CYB561A3]] | +0.59 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[TSPAN6]] | +0.58 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[PNPO]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[TOR1A]] | +0.55 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[SUMO3]] | +0.55 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[SIGMAR1]] | +0.53 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[MRPS7]] | +0.53 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[FUCA2]] | +0.53 | +0.51 / +0.36 | both halves | 9e-05 |  |
| [[FASTK]] | +0.52 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[RRAGA]] | +0.52 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[NIT2]] | +0.52 | +0.53 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 6 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG6]] | -0.51 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[RPS6]] ⚠ | -0.49 | -0.43 / -0.47 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL37A]] ⚠ | -0.47 | -0.49 / -0.39 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS16]] ⚠ | -0.45 | -0.36 / -0.42 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS27A]] ⚠ | -0.44 | -0.41 / -0.38 | both halves | 6e-05 | pathway: Diseases of carbohydrate metabolism; ⚠ in the vector space only through flagged drug-doses |
| [[RPS3]] ⚠ | -0.44 | -0.38 / -0.39 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NRTN]] | -0.44 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[NSA2]] | -0.43 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[RPL34]] | -0.43 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[WBP2NL]] | -0.43 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[RPL9]] ⚠ | -0.43 | -0.39 / -0.40 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNED1-AS1]] | -0.42 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[RPL36]] | -0.42 | -0.45 / -0.32 | both halves | 1e-04 |  |
| [[MIGA2]] | -0.42 | -0.48 / -0.29 | both halves | 3e-04 |  |
| [[TPT1]] | -0.42 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[RPL5]] | -0.42 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[BNIPL]] | -0.42 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[RPL35A]] | -0.42 | -0.44 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers G6PC3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.484). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.1, -19.3); signed map (-20.5, -40.1). **Vector** length 47.0, 5.83% of its response variance represented; |z| ≥ 3 in 734 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.8 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +14.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +12.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.4 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +2.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.4 | +3.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.3 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -2.5 | -4.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -3.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Ciclopirox (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -2.0 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -0.9 | -1.3 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | glucose-6-phosphatase catalytic subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:44,070,620-44,082,151 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UGRP |
| Gene groups (HGNC) | Glucose 6-phosphatases, catalytic |
| Reactome | 6 pathways, smallest: Glycogen storage diseases; Gluconeogenesis; Diseases of carbohydrate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUM1](https://www.uniprot.org/uniprotkb/Q9BUM1) (Glucose-6-phosphatase 3):

> Hydrolyzes glucose-6-phosphate to glucose in the endoplasmic reticulum. May form with the glucose-6-phosphate transporter (SLC37A4/G6PT) a ubiquitously expressed complex responsible for glucose production through glycogenolysis and gluconeogenesis. Probably required for normal neutrophil function.

**Summary**, from NCBI Gene [92579](https://www.ncbi.nlm.nih.gov/gene/92579):

> This gene encodes the catalytic subunit of glucose-6-phosphatase (G6Pase). G6Pase is located in the endoplasmic reticulum (ER) and catalyzes the hydrolysis of glucose-6-phosphate to glucose and phosphate in the last step of the gluconeogenic and glycogenolytic pathways. Mutations in this gene result in autosomal recessive severe congenital neutropenia. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:24861](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24861) · Entrez [92579](https://www.ncbi.nlm.nih.gov/gene/92579) · UniProt [Q9BUM1](https://www.uniprot.org/uniprotkb/Q9BUM1) · Ensembl [ENSG00000141349](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141349)

## Data

Gene col 6504: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6504); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6504, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6504]; `tensor/DDL_lfc|DDL_z.npy` [6504]; `embed/gene_vectors.npy` [6504]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6504 or target_col == 6504). Every well: [[G6PC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/G6PC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
