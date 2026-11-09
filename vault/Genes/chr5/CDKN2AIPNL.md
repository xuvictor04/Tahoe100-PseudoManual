---
symbol: "CDKN2AIPNL"
type: "gene"
col: 14121
ensembl_id: "ENSG00000237190"
name: "XRN2 binding domain containing 1"
location: "5q31.1"
module: 29
arm: "+"
pooled_cpm: 8.23
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# CDKN2AIPNL

*XRN2 binding domain containing 1* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.52× (z +16.1, q 0e+00, up in 15 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.37× (z +3.6, q 0.020, up in 11 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (PANC-1 5.73×, NCI-H460 5.96×, HOP62 7.13×, NCI-H1792 10.4×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 6.20×, SW480 5.41×, HEC-1-A 4.48×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.679× (z -4.2, q 0.017, down in 13 of 45 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.784× (z -3.9, q 0.026, down in 18 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.271×); [[Acetazolamide (drug)]] 0.5 µM in 1 line (C-33 A 0.0710×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (SHP-77 0.101×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM104B]] (+0.66, fdr 7e-06), [[PGAM1]] (+0.64, fdr 2e-05), [[COX11]] (+0.64, fdr 1e-05); moves opposite to [[NOXRED1]] (-0.54, fdr 3e-05), [[FAM32A]] (-0.53, fdr 1e-04), [[SELENOK]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14121.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (PANC-1 5.73×, NCI-H460 5.96×, HOP62 7.13×, NCI-H1792 10.4×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 6.20×, SW480 5.41×, HEC-1-A 4.48×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.52×** | +16.1 | 0e+00 | 15/15 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.85×** | +15.4 | 0e+00 | 30/32 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.97×** | +11.5 | 3e-28 | 21/22 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +7.8 | 8e-13 | 29/34 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.73×** | +6.3 | 4e-08 | 23/37 (SNU-423, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.38×** | +3.7 | 0.020 | 12/47 (A498, J82, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.37×** | +3.6 | 0.020 | 13/47 (HS-578T, A498, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.37×** | +3.6 | 0.020 | 11/48 (PANC-1, SW 1088, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.36×** | +3.5 | 0.032 | 12/47 (A498, J82, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.34×** | +3.4 | 0.045 | 10/43 (RKO, NCI-H1573, …) | rises with dose |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | 1.33× | +3.1 | 0.10 | 7/40 (J82, NCI-H1573, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~59% of this change | 1.33× | +3.1 | 0.10 | 12/38 (NCI-H1792, AsPC-1, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.0 | 0.12 | 12/48 (HS-578T, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14121.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.271×); [[Acetazolamide (drug)]] 0.5 µM in 1 line (C-33 A 0.0710×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (SHP-77 0.101×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.679×** | -4.2 | 0.017 | 13/45 (PANC-1, SW48, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.784×** | -3.9 | 0.026 | 18/45 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.538×** | -3.7 | 0.043 | 12/46 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.763× | -3.1 | 0.30 | 20/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14121. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Selinexor (drug)]] 5 µM 0.415× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 11.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.41× (z +11.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 7.95 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.5 µM 0.0710× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.48× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 8.76 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.13× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LS 180 (line)]] | wt | 8.38 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.84× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 6.97 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.4× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 8.30 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.101× (z -9.0) |
| [[A-172 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14121), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM104B]] | +0.66 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[PGAM1]] | +0.64 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[COX11]] | +0.64 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[NME4]] | +0.63 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[SIGMAR1]] | +0.62 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ATRAID]] | +0.62 | +0.68 / +0.46 | both halves | 3e-05 |  |
| [[TMEM19]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[TSPAN6]] | +0.59 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[DHX15]] | +0.59 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[MED14]] | +0.59 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[VMA21]] | +0.59 | +0.63 / +0.39 | both halves | 5e-05 |  |
| [[ICMT]] | +0.58 | +0.58 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOXRED1]] | -0.54 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[FAM32A]] | -0.53 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[SELENOK]] | -0.53 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[CHMP5]] | -0.53 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[TCF25]] | -0.52 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[LRSAM1]] | -0.50 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[UBE2CP5]] | -0.50 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[SNHG12]] | -0.50 | -0.49 / -0.29 | both halves | 3e-04 |  |
| [[ZRSR2]] | -0.49 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[SNHG6]] | -0.49 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[TRAPPC2B]] | -0.48 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[SNHG32]] | -0.48 | -0.44 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CDKN2AIPNL's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.596). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.3, -18.6); signed map (-22.6, -41.4). **Vector** length 46.1, 5.73% of its response variance represented; |z| ≥ 3 in 737 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.9 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +16.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +7.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.3 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +3.0 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | +1.0 | +2.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +0.9 | +2.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.7 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.3 | -3.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -3.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.1 | -1.3 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | XRN2 binding domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:134,402,065-134,411,881 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13017, C2AIL; previously CDKN2AIPNL |
| Gene groups (HGNC) | XTBD family |
| Matched by | ensembl_id |

UniProt [Q96HQ2](https://www.uniprot.org/uniprotkb/Q96HQ2) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:30545](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30545) · Entrez [91368](https://www.ncbi.nlm.nih.gov/gene/91368) · UniProt [Q96HQ2](https://www.uniprot.org/uniprotkb/Q96HQ2) · Ensembl [ENSG00000237190](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237190)

## Data

Gene col 14121: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14121); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14121, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14121]; `tensor/DDL_lfc|DDL_z.npy` [14121]; `embed/gene_vectors.npy` [14121]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14121 or target_col == 14121). Every well: [[CDKN2AIPNL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDKN2AIPNL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
