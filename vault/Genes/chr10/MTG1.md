---
symbol: "MTG1"
type: "gene"
col: 7316
ensembl_id: "ENSG00000148824"
name: "mitochondrial ribosome associated GTPase 1"
location: "10q26.3"
module: 18
arm: "+"
pooled_cpm: 37.86
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# MTG1

*mitochondrial ribosome associated GTPase 1* — 10q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.67× (z +10.1, q 2e-21, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.624× (z -13.3, q 2e-37, down in 46 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (HEC-1-A 0.461×, HCT15 0.324×, C-33 A 0.400×, LOX-IMVI 0.474×, …); [[Homoharringtonine (drug)]] 5 µM in 6 lines (SK-MEL-2 0.305×, HS-578T 0.313×, AN3 CA 0.269×, A-427 0.463×, …; ⚠ cell-cycle shift, explains ~88% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (J82 0.141×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (COLO 205 0.253×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POFUT1]] (+0.74, fdr 7e-06), [[AGK]] (+0.71, fdr 3e-05), [[EFTUD2]] (+0.70, fdr 1e-05); moves opposite to [[ARID4B]] (-0.64, fdr 4e-05), [[CDKN2C]] (-0.62, fdr 1e-05), [[GPRC5C]] (-0.61, fdr 2e-04).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7316.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +10.1 | 2e-21 | 37/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +8.7 | 7e-16 | 26/40 (SHP-77, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +8.3 | 1e-14 | 35/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +8.0 | 2e-13 | 29/46 (SHP-77, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +7.3 | 2e-11 | 0/49 | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +6.7 | 1e-09 | 33/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.005 | 16/48 (NCI-H23, H4, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.009 | 15/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.010 | 20/48 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.23×** | +3.7 | 0.011 | 18/44 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.22×** | +3.4 | 0.040 | 18/46 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 1.34× | +3.0 | 0.12 | 10/48 (PANC-1, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7316.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (HEC-1-A 0.461×, HCT15 0.324×, C-33 A 0.400×, LOX-IMVI 0.474×, …); [[Homoharringtonine (drug)]] 5 µM in 6 lines (SK-MEL-2 0.305×, HS-578T 0.313×, AN3 CA 0.269×, A-427 0.463×, …; ⚠ cell-cycle shift, explains ~88% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (J82 0.141×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (COLO 205 0.253×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.624×** | -13.3 | 2e-37 | 46/48 (HEC-1-A, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.801×** | -6.3 | 9e-08 | 24/48 (SK-MEL-2, HS-578T, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.712×** | -5.9 | 7e-07 | 28/47 (NCI-H23, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.764×** | -5.4 | 1e-05 | 23/46 (LoVo, CHP-212, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.788×** | -4.8 | 2e-04 | 24/48 (RKO, A-427, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.861× | -4.2 | 0.002 | 19/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 0.837× | -3.1 | 0.16 | 18/48 (NCI-H460, SNU-1, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.860× | -3.0 | 0.18 | 19/48 (NCI-H460, SW 1271, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7316. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 38.7 | 4 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.62× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -8.6) |
| [[SHP-77 (line)]] | alt | 53.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 13.3× (z +20.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 32.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.87× (z +15.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 32.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.70× (z +15.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -11.2) |
| [[A-427 (line)]] | wt | 58.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -10.5) ⚠ cell-cycle shift, explains ~88% of this change |
| [[A549 (line)]] | wt | 36.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -9.0) ⚠ cell-cycle shift, explains ~88% of this change |
| [[AN3 CA (line)]] | alt | 69.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -10.9) ⚠ cell-cycle shift, explains ~88% of this change |
| [[C-33 A (line)]] | alt | 56.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -10.3) |
| [[COLO 205 (line)]] | alt | 34.1 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.253× (z -8.7) |
| [[HCT15 (line)]] | alt | 37.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -10.9) |
| [[HS-578T (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -12.5) ⚠ cell-cycle shift, explains ~88% of this change |
| [[J82 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -14.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 32.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +12.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 46.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 49.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 41.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.576× (z -8.8) ⚠ cell-cycle shift, explains ~88% of this change |
| [[RKO (line)]] | wt | 52.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +12.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 40.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -13.8) ⚠ cell-cycle shift, explains ~88% of this change |
| [[SNU-423 (line)]] | alt | 39.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -9.7) |
| [[A-172 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7316), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POFUT1]] | +0.74 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[AGK]] | +0.71 | +0.43 / +0.80 | both halves | 3e-05 |  |
| [[EFTUD2]] | +0.70 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[TRAP1]] | +0.67 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[CARNMT1]] | +0.67 | +0.42 / +0.73 | both halves | 4e-05 |  |
| [[CAD]] | +0.66 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[RFT1]] | +0.66 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[ACTR5]] | +0.66 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[ACSF3]] | +0.66 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[FARSB]] | +0.64 | +0.39 / +0.70 | both halves | 6e-05 |  |
| [[ENTPD5]] | +0.64 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[SEH1L]] | +0.63 | +0.59 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID4B]] | -0.64 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[CDKN2C]] | -0.62 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[GPRC5C]] | -0.61 | -0.32 / -0.64 | both halves | 2e-04 |  |
| [[ATOSA]] | -0.60 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[YY1]] | -0.60 | -0.39 / -0.64 | both halves | 6e-05 |  |
| [[GPBP1]] | -0.59 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[CREB3L4]] | -0.59 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[SATB1]] | -0.59 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[CHODL]] | -0.58 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[ARID4A]] | -0.58 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[UPK2]] | -0.58 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[SPATC1]] | -0.57 | -0.43 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MTG1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.531). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-11.0, -36.8); signed map (-8.4, -47.3). **Vector** length 97.7, 21.2% of its response variance represented; |z| ≥ 3 in 807 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.0 | +6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +8.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +10.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.1 | +3.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.0 | +2.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.7 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.5 | -13.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | -5.7 | -6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -1.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosome associated GTPase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.3 — chr10:133,394,094-133,422,520 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GTPBP7 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BT17](https://www.uniprot.org/uniprotkb/Q9BT17) (Mitochondrial ribosome-associated GTPase 1):

> Plays a role in the regulation of the mitochondrial ribosome assembly and of translational activity. Displays mitochondrial GTPase activity.

**Summary**, from NCBI Gene [92170](https://www.ncbi.nlm.nih.gov/gene/92170):

> Enables GTPase activity. Involved in mitochondrial large ribosomal subunit assembly; regulation of mitochondrial translation; and regulation of respiratory system process. Located in mitochondrial inner membrane and mitochondrial ribosome. Is active in mitochondrial matrix. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:32159](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32159) · Entrez [92170](https://www.ncbi.nlm.nih.gov/gene/92170) · UniProt [Q9BT17](https://www.uniprot.org/uniprotkb/Q9BT17) · Ensembl [ENSG00000148824](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148824)

## Data

Gene col 7316: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7316); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7316, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7316]; `tensor/DDL_lfc|DDL_z.npy` [7316]; `embed/gene_vectors.npy` [7316]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7316 or target_col == 7316). Every well: [[MTG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
