---
symbol: "C12orf4"
type: "gene"
col: 520
ensembl_id: "ENSG00000047621"
name: "FERRY endosomal RAB5 effector complex subunit 3"
location: "12p13.32"
module: 89
arm: "+"
pooled_cpm: 27.83
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# C12orf4

*FERRY endosomal RAB5 effector complex subunit 3* — 12p13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.22× (z +18.2, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.698× (z -8.3, q 9e-14, down in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A549 0.131×, LoVo 0.155×, SW480 0.346×, H4 0.141×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (HEC-1-A 0.314×, HOP62 0.335×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C32 0.262×, COLO 205 0.234×; ⚠ toxic; transcription drop); [[Ipatasertib (drug)]] 0.5 µM in 1 line (HCT15 0.107×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (SNU-1 0.207×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (Hs 766T 0.308×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA9]] (+0.61, fdr 1e-05), [[ALKBH1]] (+0.61, fdr 1e-05), [[TMEM128]] (+0.59, fdr 7e-06); moves opposite to [[CTBP2]] (-0.61, fdr 1e-05), [[ZSWIM6]] (-0.50, fdr 1e-04), [[PEAK1]] (-0.50, fdr 5e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF223]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 520.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.22×** | +18.2 | 0e+00 | 45/48 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.11×** | +12.0 | 8e-31 | 43/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.87×** | +8.9 | 1e-16 | 38/48 (HOP62, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +8.5 | 2e-15 | 32/48 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +8.2 | 2e-14 | 30/48 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +6.7 | 1e-09 | 28/48 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +5.1 | 3e-05 | 25/48 (A-427, LS 180, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.34×** | +4.5 | 4e-04 | 25/46 (SW480, SNU-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +4.4 | 7e-04 | 19/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.68×** | +4.4 | 7e-04 | 21/48 (HOP62, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.014 | 22/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.036 | 13/48 (J82, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.23×** | +3.3 | 0.036 | 14/48 (PANC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 1.15× | +3.1 | 0.073 | 12/48 (LS 180, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +3.1 | 0.073 | 15/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 520.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A549 0.131×, LoVo 0.155×, SW480 0.346×, H4 0.141×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (HEC-1-A 0.314×, HOP62 0.335×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C32 0.262×, COLO 205 0.234×; ⚠ toxic; transcription drop); [[Ipatasertib (drug)]] 0.5 µM in 1 line (HCT15 0.107×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (SNU-1 0.207×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (Hs 766T 0.308×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.698×** | -8.3 | 9e-14 | 39/48 (HOP62, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.678×** | -6.3 | 8e-08 | 32/48 (LOX-IMVI, LS 180, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.702×** | -5.5 | 5e-06 | 23/46 (HEC-1-A, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.713×** | -5.5 | 5e-06 | 19/44 (C32, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.765×** | -4.4 | 0.001 | 21/45 (AsPC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 0.824× | -3.1 | 0.16 | 9/48 (NCI-H2347, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 520. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 21.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +14.4) | — |
| [[SW480 (line)]] | alt | 47.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 46.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.8) | — |
| [[LoVo (line)]] | wt | 22.9 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.37× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.155× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 15.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +10.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 26.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 32.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +9.2) | [[Ipatasertib (drug)]] 0.5 µM 0.107× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 26.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.314× (z -9.6) ⚠ toxic |
| [[HOP62 (line)]] | alt | 32.7 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.335× (z -9.6) ⚠ toxic · without an alert: [[Tucidinostat (drug)]] 5 µM 0.513× (z -8.6) |
| [[Hs 766T (line)]] | wt | 28.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +10.9) | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.308× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 29.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +12.4) | — |
| [[NCI-H1573 (line)]] | alt | 20.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +12.8) | — |
| [[NCI-H460 (line)]] | wt | 22.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +15.3) | — |
| [[SNU-1 (line)]] | wt | 29.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +10.1) | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.207× (z -9.0) |
| [[SW 900 (line)]] | alt | 45.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +10.4) | — |
| [[A498 (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 32.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -9.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -8.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 30.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 25.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.19× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 21.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +9.4) | — |
| [[J82 (line)]] | alt | 32.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.9) | — |
| [[KATO III (line)]] | alt | 30.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 37.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +14.3) | — |
| [[NCI-H2030 (line)]] | alt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 55.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +16.8) | — |
| [[NCI-H2347 (line)]] | alt | 37.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +8.7) | — |
| [[RKO (line)]] | wt | 33.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +11.8) | — |
| [[AN3 CA (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 520), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA9]] | +0.61 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[ALKBH1]] | +0.61 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[TMEM128]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[POLR3F]] | +0.59 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[SLC25A46]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[BBS1]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[VPS33A]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[WDR73]] | +0.57 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[COQ6]] | +0.57 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[MTERF4]] | +0.56 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[CWF19L1]] | +0.56 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[ZNF136]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTBP2]] | -0.61 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[ZSWIM6]] | -0.50 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[PEAK1]] | -0.50 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[EPB41L5]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[CBL]] | -0.47 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[CRISPLD2]] | -0.47 | -0.36 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF223]] | B | ZNF223 activity weakens C12orf4's drug response | lines that do not express ZNF223 (11) vs lines expressing it (37) | the lines without ZNF223 respond 1.20× as strongly (z diff -0.67); strongest at Panobinostat 5 µM: 2.11x vs 1.50x (z diff -2.1) | 0.099 | ⚠ within organs, on part of the lines; also absent: ZNF284, TGFB1I1, ZNF891; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.525). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.0, 6.3); signed map (-11.2, -17.5). **Vector** length 85.1, 18.2% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +18.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +12.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +8.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | +3.6 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.8 | +8.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.9 | +3.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.6 | -8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.7 | -6.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.6 | -5.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.9 | +0.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | FERRY endosomal RAB5 effector complex subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.32 — chr12:4,487,735-4,538,508 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Fy-3; previously C12orf4 |
| Gene groups (HGNC) | FERRY complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ89](https://www.uniprot.org/uniprotkb/Q9NQ89) (Ferry endosomal RAB5 effector complex subunit 3):

> Component of the FERRY complex (Five-subunit Endosomal Rab5 and RNA/ribosome intermediary). The FERRY complex directly interacts with mRNAs and RAB5A, and functions as a RAB5A effector involved in the localization and the distribution of specific mRNAs most likely by mediating their endosomal transport. The complex recruits mRNAs and ribosomes to early endosomes through direct mRNA-interaction. Plays a role in mast cell degranulation.

**Summary**, from NCBI Gene [57102](https://www.ncbi.nlm.nih.gov/gene/57102):

> This gene is highly conserved from nematodes to humans. In rat, the orthologous gene encodes a cytoplasmic protein that is involved in mast cell degranulation. The human gene has been implicated in autosomal recessive intellectual disability. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:1184](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1184) · Entrez [57102](https://www.ncbi.nlm.nih.gov/gene/57102) · UniProt [Q9NQ89](https://www.uniprot.org/uniprotkb/Q9NQ89) · Ensembl [ENSG00000047621](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047621)

## Data

Gene col 520: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 520); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 520, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 520]; `tensor/DDL_lfc|DDL_z.npy` [520]; `embed/gene_vectors.npy` [520]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 520 or target_col == 520). Every well: [[C12orf4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C12orf4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
