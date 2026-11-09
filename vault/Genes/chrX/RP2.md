---
symbol: "RP2"
type: "gene"
col: 2226
ensembl_id: "ENSG00000102218"
name: "RP2 activator of ARL3 GTPase"
location: "Xp11.3"
module: 146
arm: "-"
pooled_cpm: 26.53
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# RP2

*RP2 activator of ARL3 GTPase* — Xp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.39× (z +7.8, q 5e-12, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.675× (z -6.6, q 2e-08, down in 29 of 40 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 0.125×, A549 0.258×, NCI-H460 0.341×, A-427 0.253×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SW 900 0.116×, A549 0.294×, SW1417 0.297×, RPMI-7951 0.243×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change); [[Docetaxel (drug)]] 0.05 µM in 2 lines (RPMI-7951 0.233×, H4 0.158×; ⚠ transcription drop); [[Pyridoxine (drug)]] 0.5 µM in 1 line (H4 0.0799×); [[PH-797804 (drug)]] 0.5 µM in 1 line (HCT15 0.0879×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLIC1]] (+0.57, fdr 1e-05), [[ATP6V1D]] (+0.54, fdr 2e-05), [[STK10]] (+0.49, fdr 2e-05); moves opposite to [[PCCB]] (-0.55, fdr 1e-05), [[PUM2]] (-0.55, fdr 4e-05), [[RYK]] (-0.54, fdr 3e-05).
> It sits in the **-** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MANCR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2226.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +7.8 | 5e-12 | 28/47 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +7.5 | 1e-11 | 28/48 (J82, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +6.9 | 1e-09 | 25/48 (SW1417, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +6.4 | 2e-08 | 26/48 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +5.8 | 6e-07 | 23/48 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.1 | 3e-05 | 21/46 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.62×** | +4.3 | 0.002 | 15/48 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +4.1 | 0.003 | 16/47 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +4.1 | 0.003 | 13/48 (NCI-H460, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +4.0 | 0.004 | 13/47 (hTERT-HPNE, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.007 | 11/47 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.023 | 16/47 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.060 | 7/48 (SW480, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.088 | 14/48 (NCI-H460, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2226.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 0.125×, A549 0.258×, NCI-H460 0.341×, A-427 0.253×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SW 900 0.116×, A549 0.294×, SW1417 0.297×, RPMI-7951 0.243×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change); [[Docetaxel (drug)]] 0.05 µM in 2 lines (RPMI-7951 0.233×, H4 0.158×; ⚠ transcription drop); [[Pyridoxine (drug)]] 0.5 µM in 1 line (H4 0.0799×); [[PH-797804 (drug)]] 0.5 µM in 1 line (HCT15 0.0879×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.675×** | -6.6 | 2e-08 | 29/40 (NCI-H1573, A549, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -6.5 | 2e-08 | 8/48 (SW 900, LS 180, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.725×** | -5.4 | 1e-05 | 25/44 (RPMI-7951, H4, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.803×** | -3.6 | 0.052 | 14/43 (NCI-H2347, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | 0.819× | -3.2 | 0.10 | 16/45 (A549, MIA PaCa-2, …) | top dose only |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | 0.768× | -3.2 | 0.10 | 10/48 (CHP-212, MIA PaCa-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.768× | -3.2 | 0.10 | 12/45 (Hs 766T, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.830× | -3.2 | 0.10 | 18/47 (A498, SNU-423, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.824× | -3.1 | 0.10 | 15/48 (SNU-423, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | 0.819× | -3.1 | 0.10 | 16/35 (SW 900, A549, …) | inconsistent across doses | composition shift |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.777× | -3.0 | 0.12 | 9/48 (HCT15, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2226. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.9 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -9.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 39.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -10.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 21.9 | 0 | 2 (1 ⚠) | — | [[Pyridoxine (drug)]] 0.5 µM 0.0799× (z -12.0) |
| [[J82 (line)]] | alt | 45.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 37.0 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.233× (z -9.5) ⚠ transcription drop |
| [[A-427 (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -8.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 9.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +10.0) | — |
| [[HCT15 (line)]] | alt | 20.8 | 0 | 1 | — | [[PH-797804 (drug)]] 0.5 µM 0.0879× (z -9.2) |
| [[HT-29 (line)]] | alt | 28.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 29.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.316× (z -8.8) ⚠ toxic |
| [[RKO (line)]] | wt | 19.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[SW1417 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[A-172 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 35.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2226), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLIC1]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ATP6V1D]] | +0.54 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[STK10]] | +0.49 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[WNT9A]] | +0.47 | +0.51 / +0.37 | both halves | 8e-05 |  |
| [[RAI14]] | +0.47 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[PDGFB]] | +0.47 | +0.60 / +0.34 | both halves | 1e-04 |  |
| [[WDR47]] | +0.46 | +0.41 / +0.40 | both halves | 5e-05 |  |
| [[ZBTB43]] | +0.46 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[ZNF92]] | +0.46 | +0.46 / +0.36 | both halves | 1e-04 |  |
| [[TUBA1A]] | +0.46 | +0.48 / +0.38 | both halves | 7e-05 | pathway: Assembly of the 9+0 primary cilium |
| [[SDCBP]] | +0.45 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[NAGK]] | +0.45 | +0.46 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCCB]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[PUM2]] | -0.55 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[RYK]] | -0.54 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[REV1]] | -0.53 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[TARBP1]] | -0.50 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[VGLL4]] | -0.50 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[SLC2A11]] | -0.50 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[NDUFS6]] | -0.50 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[DDX54]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ZBED3]] | -0.48 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[MIA2]] | -0.48 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[BRWD1]] | -0.47 | -0.40 / -0.41 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MANCR]] | B | MANCR activity raises RP2's level | lines that do not express MANCR (20) vs lines expressing it (30) | 1.48× lower at baseline in the lines without MANCR | 0.060 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **-** arm (projection on the module's main direction -0.468). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-7.8, -15.0); signed map (7.2, 17.1). **Vector** length 83.3, 16.3% of its response variance represented; |z| ≥ 3 in 894 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.6 | +7.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +4.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.7 | +3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +2.6 | +3.8 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +2.7 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.5 | +1.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +0.9 |
|  | [[Posaconazole (drug)]] 5 µM |  | +1.3 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.1 | -3.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | RP2 activator of ARL3 GTPase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.3 — chrX:46,837,043-46,882,358 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TBCCD2, NME10, NM23-H10 |
| Reactome | 5 pathways, smallest: Trafficking of myristoylated proteins to the cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [O75695](https://www.uniprot.org/uniprotkb/O75695) (Protein XRP2):

> Acts as a GTPase-activating protein (GAP) involved in trafficking between the Golgi and the ciliary membrane. Involved in localization of proteins, such as NPHP3, to the cilium membrane by inducing hydrolysis of GTP ARL3, leading to the release of UNC119 (or UNC119B). Acts as a GTPase-activating protein (GAP) for tubulin in concert with tubulin-specific chaperone C, but does not enhance tubulin heterodimerization. Acts as a guanine nucleotide dissociation inhibitor towards ADP-ribosylation …

**Summary**, from NCBI Gene [6102](https://www.ncbi.nlm.nih.gov/gene/6102):

> The RP2 locus has been implicated as one cause of X-linked retinitis pigmentosa. The predicted gene product shows homology with human cofactor C, a protein involved in the ultimate step of beta-tubulin folding. Progressive retinal degeneration may therefore be due to the accumulation of incorrectly-folded photoreceptor or neuron-specific tubulin isoforms followed by progressive cell death [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10274](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10274) · Entrez [6102](https://www.ncbi.nlm.nih.gov/gene/6102) · UniProt [O75695](https://www.uniprot.org/uniprotkb/O75695) · Ensembl [ENSG00000102218](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102218)

## Data

Gene col 2226: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2226); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2226, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2226]; `tensor/DDL_lfc|DDL_z.npy` [2226]; `embed/gene_vectors.npy` [2226]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2226 or target_col == 2226). Every well: [[RP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
