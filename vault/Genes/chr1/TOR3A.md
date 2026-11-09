---
symbol: "TOR3A"
type: "gene"
col: 11800
ensembl_id: "ENSG00000186283"
name: "torsin family 3 member A"
location: "1q25.2"
module: 5
arm: "+"
pooled_cpm: 6.45
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TOR3A

*torsin family 3 member A* — 1q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (23 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.50× (z +12.1, q 4e-31, up in 26 of 31 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +11.3, q 6e-27, up in 29 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.760× (z -3.8, q 0.080, down in 11 of 45 measured lines) ⚠ cell-cycle shift, explains ~36% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Megestrol (drug)]] 0.5 µM in 1 line (Hs 766T 0.0727×); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (C32 0.0620×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 0.183×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Piroxicam (drug)]] 0.5 µM in 1 line (COLO 205 0.0550×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PANK1]] (+0.66, fdr 2e-05), [[NADK]] (+0.62, fdr 1e-05), [[ZNF142]] (+0.62, fdr 1e-05); moves opposite to [[SPAG9]] (-0.59, fdr 3e-05), [[CALN1]] (-0.58, fdr 4e-05), [[UBE2B]] (-0.57, fdr 5e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 23 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11800.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.50×** | +12.1 | 4e-31 | 26/31 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +11.3 | 6e-27 | 29/42 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.82×** | +8.0 | 3e-13 | 22/41 (NCI-H460, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.75×** | +7.7 | 1e-12 | 17/30 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.78×** | +7.7 | 2e-12 | 11/13 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.76×** | +7.3 | 2e-11 | 23/43 (A-172, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.62×** | +6.6 | 2e-09 | 20/42 (HOP62, SW1417, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +6.1 | 9e-08 | 14/33 (SW480, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.54×** | +5.7 | 7e-07 | 16/42 (LS 180, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.48×** | +5.4 | 3e-06 | 16/46 (PANC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.45×** | +5.2 | 1e-05 | 16/47 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.45×** | +5.1 | 1e-05 | 17/46 (PANC-1, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +5.1 | 1e-05 | 16/46 (HOP62, C32, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.44×** | +5.1 | 2e-05 | 14/47 (PANC-1, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.44×** | +5.0 | 2e-05 | 13/47 (HOP62, C32, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.004 | 9/38 (SHP-77, LS 180, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +3.8 | 0.004 | 12/40 (A-427, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.007 | 14/48 (HOP62, A-427, …) | top dose only | position effect removed |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.30×** | +3.4 | 0.016 | 8/39 (LoVo, SW 900, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.029 | 3/45 (SW48, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.030 | 2/43 (A549, SW480) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (maleate) (drug)]] 0.05 µM |  | **1.26×** | +2.9 | 0.067 | 6/44 (NCI-H2347, SK-MEL-2, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +2.8 | 0.080 | 8/45 (C-33 A, NCI-H23, …) | top dose only |  |
| [[Finasteride (drug)]] 0.05 µM |  | **1.24×** | +2.8 | 0.090 | 3/45 (Panc 03.27, NCI-H2030, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.23×** | +2.7 | 0.096 | 4/46 (SK-MEL-2, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11800.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Megestrol (drug)]] 0.5 µM in 1 line (Hs 766T 0.0727×); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (C32 0.0620×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 0.183×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Piroxicam (drug)]] 0.5 µM in 1 line (COLO 205 0.0550×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.760×** | -3.8 | 0.080 | 11/45 (MIA PaCa-2, C32, …) | two highest doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.784× | -3.4 | 0.19 | 5/47 (AsPC-1, HOP62, …) | inconsistent across doses |  |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.786× | -3.2 | 0.19 | 8/46 (NCI-H2030, NCI-H1792, …) | rises with dose |  |
| [[Meloxicam (drug)]] 0.5 µM |  | 0.794× | -3.2 | 0.19 | 7/45 (CFPAC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.806× | -3.0 | 0.30 | 12/40 (LOX-IMVI, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11800. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 5.38 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0620× (z -9.7) |
| [[COLO 205 (line)]] | alt | 4.96 | 0 | 1 | — | [[Piroxicam (drug)]] 0.5 µM 0.0550× (z -8.5) |
| [[Hs 766T (line)]] | wt | 5.37 | 0 | 1 | — | [[Megestrol (drug)]] 0.5 µM 0.0727× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 5.51 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0939× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 9.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 4.34 | 0 | 1 | — | [[Ixazomib (drug)]] 0.05 µM 0.0683× (z -8.5) |
| [[SW480 (line)]] | alt | 6.91 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.80× (z +9.1) ⚠ toxic | — |
| [[A-427 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11800), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PANK1]] | +0.66 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[NADK]] | +0.62 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[ZNF142]] | +0.62 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[TOR1A]] | +0.61 | +0.55 / +0.41 | both halves | 4e-05 | same gene group; STRING 401 |
| [[MRPS15]] | +0.61 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[SEPHS1]] | +0.61 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[PRDM15]] | +0.61 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[ARHGEF11]] | +0.60 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[ARSB]] | +0.60 | +0.64 / +0.38 | both halves | 7e-05 |  |
| [[PRCC]] | +0.59 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[PASK]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[MCM9]] | +0.59 | +0.53 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG9]] | -0.59 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[CALN1]] | -0.58 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[UBE2B]] | -0.57 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[NBEAL1]] | -0.56 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[RING1]] | -0.55 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[CCNI]] | -0.53 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[MOSPD2]] | -0.53 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[GNG7]] | -0.52 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[LINC00624]] | -0.51 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[SYP]] | -0.51 | -0.25 / -0.42 | both halves | 4e-04 |  |
| [[BCL10]] | -0.49 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[OAZ1]] | -0.49 | -0.39 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TOR3A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.500). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-16.8, -28.7); signed map (-8.9, -40.4). **Vector** length 50.9, 6.11% of its response variance represented; |z| ≥ 3 in 898 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +11.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | +3.3 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +2.9 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +2.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.5 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | +1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | torsin family 3 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.2 — chr1:179,082,070-179,098,023 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22345, ADIR2; previously ADIR |
| Gene groups (HGNC) | Minor histocompatibility antigens; Torsins |
| Matched by | ensembl_id |

UniProt [Q9H497](https://www.uniprot.org/uniprotkb/Q9H497) carries no function annotation.

**Summary**, from NCBI Gene [64222](https://www.ncbi.nlm.nih.gov/gene/64222):

> Enables ATP hydrolysis activity. Located in endoplasmic reticulum lumen. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11997](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11997) · Entrez [64222](https://www.ncbi.nlm.nih.gov/gene/64222) · UniProt [Q9H497](https://www.uniprot.org/uniprotkb/Q9H497) · Ensembl [ENSG00000186283](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186283)

## Data

Gene col 11800: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11800); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11800, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11800]; `tensor/DDL_lfc|DDL_z.npy` [11800]; `embed/gene_vectors.npy` [11800]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11800 or target_col == 11800). Every well: [[TOR3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOR3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
