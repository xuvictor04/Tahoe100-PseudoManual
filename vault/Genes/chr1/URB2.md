---
symbol: "URB2"
type: "gene"
col: 5753
ensembl_id: "ENSG00000135763"
name: "URB2 ribosome biogenesis homolog"
location: "1q42.13"
module: 5
arm: "+"
pooled_cpm: 14.62
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 20
n_dd_up_clean: 20
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# URB2

*URB2 ribosome biogenesis homolog* — 1q42.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (13 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.37× (z +11.7, q 4e-29, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.639× (z -6.0, q 1e-06, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR4]] (+0.84, fdr 7e-06), [[TSEN2]] (+0.83, fdr 7e-06), [[POLR1B]] (+0.82, fdr 7e-06); moves opposite to [[MXD1]] (-0.64, fdr 7e-06), [[WBP1]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TERT]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Belzutifan (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5753.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.37×** | +11.7 | 4e-29 | 42/46 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **5.13×** | +11.4 | 8e-28 | 38/44 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.27×** | +10.9 | 1e-25 | 40/47 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.27×** | +10.9 | 1e-25 | 38/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.22×** | +10.6 | 3e-24 | 34/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.05×** | +9.6 | 1e-19 | 35/46 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +8.4 | 3e-15 | 35/43 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.85×** | +8.2 | 2e-14 | 31/46 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.83×** | +8.0 | 6e-14 | 23/47 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.79×** | +7.7 | 6e-13 | 29/47 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.79×** | +7.5 | 3e-12 | 28/42 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.69×** | +6.9 | 2e-10 | 11/20 (A549, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +5.9 | 2e-07 | 21/46 (RPMI-7951, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +5.5 | 2e-06 | 19/47 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +5.4 | 2e-06 | 26/45 (Panc 03.27, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +4.8 | 4e-05 | 16/46 (NCI-H23, H4, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.96×** | +4.7 | 8e-05 | 19/44 (NCI-H460, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.44×** | +4.6 | 1e-04 | 18/46 (NCI-H1792, LoVo, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.42×** | +4.4 | 2e-04 | 15/46 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.37×** | +4.2 | 8e-04 | 17/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.002 | 9/47 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.011 | 6/47 (NCI-H460, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5753.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM |  | **0.639×** | -6.0 | 1e-06 | 24/46 (Hs 766T, LS 180, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **0.688×** | -5.0 | 1e-04 | 20/48 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.772×** | -4.9 | 1e-04 | 21/48 (LoVo, LOX-IMVI, …) | all doses, flat | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.692×** | -4.8 | 3e-04 | 16/46 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.738×** | -4.3 | 0.002 | 17/48 (SK-MEL-2, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.807×** | -4.1 | 0.004 | 21/46 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **0.739×** | -4.1 | 0.004 | 18/46 (KATO III, RKO, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.752×** | -3.8 | 0.008 | 13/47 (SW1417, HEC-1-A, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.774×** | -3.7 | 0.014 | 18/47 (HepG2/C3A, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.763×** | -3.6 | 0.016 | 9/47 (A-427, LoVo, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.767×** | -3.6 | 0.018 | 15/46 (A498, NCI-H460, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.772×** | -3.6 | 0.018 | 12/48 (NCI-H23, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.777×** | -3.4 | 0.030 | 10/47 (LoVo, A-427, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.779×** | -3.4 | 0.030 | 14/46 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.841× | -3.3 | 0.034 | 15/48 (SW48, A498, …) | rises with dose | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.678×** | -3.3 | 0.034 | 9/44 (NCI-H1792, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.702×** | -3.0 | 0.079 | 12/45 (A498, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5753. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 25.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0293× (z -26.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 37.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -10.5) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -9.7) |
| [[SW480 (line)]] | alt | 19.4 | 2 | 0 | [[Digitoxin (drug)]] 0.5 µM 3.77× (z +9.3) | — |
| [[A-172 (line)]] | wt | 9.20 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.452× (z -12.4) ⚠ position not correctable |
| [[NCI-H23 (line)]] | alt | 17.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 22.0 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.62× (z +9.0) ⚠ unreliable plate only | — |
| [[Panc 03.27 (line)]] | alt | 9.13 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.73× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 43.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 22.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5753), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR4]] | +0.84 | +0.85 / +0.86 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.83 | +0.82 / +0.81 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.82 | +0.81 / +0.82 | both halves | 7e-06 | STRING 638 |
| [[POLR1A]] | +0.80 | +0.81 / +0.78 | both halves | 7e-06 |  |
| [[DHX33]] | +0.80 | +0.84 / +0.82 | both halves | 7e-06 |  |
| [[MDN1]] | +0.79 | +0.83 / +0.75 | both halves | 7e-06 |  |
| [[LETM1]] | +0.78 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.78 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[PUS1]] | +0.78 | +0.75 / +0.78 | both halves | 7e-06 |  |
| [[NOP2]] | +0.77 | +0.75 / +0.78 | both halves | 7e-06 |  |
| [[BYSL]] | +0.77 | +0.76 / +0.78 | both halves | 7e-06 |  |
| [[CTPS1]] | +0.76 | +0.73 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXD1]] | -0.64 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[WBP1]] | -0.64 | -0.68 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises URB2's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.47× lower at baseline in the lines without TERT | 0.007 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[MAP2K1]] | B | MAP2K1 activity raises URB2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Belzutifan (drug)]] 5 µM | C | URB2's natural level raises the cells' numbers under Belzutifan 5 µM (protects the cells) | URB2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.59 | 0.475 over the table, 0.080 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.774). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-12.9, -37.2); signed map (-4.6, -49.3). **Vector** length 103, 25.9% of its response variance represented; |z| ≥ 3 in 1,205 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.67 to 13); *rRNA processing* (reactome, mean cos +0.57 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.58 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.0 | +10.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | +5.0 | +7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +11.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +3.6 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +4.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -4.5 | +3.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -4.2 | -4.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.5 | -6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.8 | -1.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.2 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | URB2 ribosome biogenesis homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.13 — chr1:229,626,247-229,660,200 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NPA2, NET10; previously KIAA0133 |
| Gene groups (HGNC) | Ribosome biogenesis factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14146](https://www.uniprot.org/uniprotkb/Q14146) (Unhealthy ribosome biogenesis protein 2 homolog):

> Essential for hematopietic stem cell development through the regulation of p53/TP53 pathway.

**Summary**, from NCBI Gene [9816](https://www.ncbi.nlm.nih.gov/gene/9816):

> Predicted to be involved in regulation of signal transduction by p53 class mediator and ribosome biogenesis. Located in midbody and nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28967](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28967) · Entrez [9816](https://www.ncbi.nlm.nih.gov/gene/9816) · UniProt [Q14146](https://www.uniprot.org/uniprotkb/Q14146) · Ensembl [ENSG00000135763](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135763)

## Data

Gene col 5753: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5753); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5753, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5753]; `tensor/DDL_lfc|DDL_z.npy` [5753]; `embed/gene_vectors.npy` [5753]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5753 or target_col == 5753). Every well: [[URB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/URB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
