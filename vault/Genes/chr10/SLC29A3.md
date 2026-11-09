---
symbol: "SLC29A3"
type: "gene"
col: 12560
ensembl_id: "ENSG00000198246"
name: "solute carrier family 29 member 3"
location: "10q22.1"
module: 115
arm: "+"
pooled_cpm: 6.5
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 20
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# SLC29A3

*solute carrier family 29 member 3* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.96× (z +14.2, q 1e-42, up in 6 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +5.2, q 3e-05, up in 14 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.404× (z -11.9, q 1e-29, down in 27 of 44 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.352× (z -7.4, q 1e-11, down in 22 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HAGLR]] (+0.55, fdr 4e-05), [[RNF44]] (+0.54, fdr 4e-05), [[PRR5]] (+0.53, fdr 1e-05); moves opposite to [[TOGARAM1]] (-0.48, fdr 4e-05), [[PKN2]] (-0.48, fdr 4e-05), [[HCFC2]] (-0.47, fdr 5e-05).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC4A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12560.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.96×** | +14.2 | 1e-42 | 6/13 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +8.1 | 1e-13 | 10/18 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +6.3 | 5e-08 | 16/31 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.2 | 3e-05 | 14/39 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +5.1 | 3e-05 | 18/46 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +4.9 | 9e-05 | 12/26 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.004 | 6/47 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.012 | 6/45 (SW 900, C-33 A, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.20× | +3.5 | 0.031 | 7/47 (A-427, COLO 205, …) | rises with dose | low cells (technical?) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.039 | 5/44 (J82, AN3 CA, …) | inconsistent across doses | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.25× | +3.1 | 0.12 | 4/47 (NCI-H460, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12560.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.404×** | -11.9 | 1e-29 | 27/44 (NCI-H460, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.517×** | -9.0 | 8e-17 | 23/41 (KATO III, HS-578T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.576×** | -7.5 | 1e-11 | 23/47 (SW48, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.680×** | -7.4 | 1e-11 | 19/40 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.352×** | -7.4 | 1e-11 | 22/45 (KATO III, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.581×** | -7.4 | 1e-11 | 22/46 (SW1417, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.598×** | -7.0 | 2e-10 | 24/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.629×** | -6.3 | 2e-08 | 19/45 (RPMI-7951, COLO 205, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.648×** | -5.7 | 8e-07 | 17/42 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.478×** | -5.3 | 8e-06 | 15/44 (LS 180, A498, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.478×** | -5.2 | 8e-06 | 15/41 (RKO, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.490×** | -5.1 | 2e-05 | 14/44 (SW480, AN3 CA, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.624×** | -4.6 | 2e-04 | 13/47 (PANC-1, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.728×** | -4.3 | 6e-04 | 15/45 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.739×** | -3.9 | 0.004 | 13/45 (H4, HepG2/C3A, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.617×** | -3.4 | 0.019 | 12/42 (RKO, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.785×** | -3.1 | 0.068 | 5/45 (BT-474, A-172, …) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 0.5 µM |  | **0.736×** | -3.0 | 0.083 | 4/45 (SW480, HepG2/C3A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Busulfan (drug)]] 5 µM |  | 0.860× | -2.9 | 0.095 | 8/45 (SNU-1, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12560. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 11.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -10.8) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -10.5) |
| [[A498 (line)]] | wt | 8.34 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.29× (z +10.4) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 0.5 µM 0.203× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 4.95 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.106× (z -11.1) |
| [[PANC-1 (line)]] | alt | 3.93 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -12.1) ⚠ cell-cycle shift, explains ~93% of this change |
| [[A549 (line)]] | wt | 6.38 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -9.8) ⚠ cell-cycle shift, explains ~93% of this change |
| [[HepG2_C3A (line)]] | wt | 20.2 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.102× (z -11.0) ⚠ toxic |
| [[HOP62 (line)]] | alt | 8.74 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.2× (z +11.8) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 3.98 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 15.2× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 5.89 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0943× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 7.14 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -10.5) ⚠ cell-cycle shift, explains ~93% of this change |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0570× (z -8.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW 900 (line)]] | alt | 4.76 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 23.5× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 12.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0680× (z -9.3) |
| [[A-172 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12560), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAGLR]] | +0.55 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[RNF44]] | +0.54 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[PRR5]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[MERTK]] | +0.53 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[PRR5-ARHGAP8]] | +0.52 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[UBFD1]] | +0.52 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[THOC5]] | +0.52 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[GAB2]] | +0.50 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[MSI1]] | +0.49 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[CPNE2]] | +0.49 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[CRACD]] | +0.49 | +0.40 / +0.52 | both halves | 4e-05 |  |
| [[NCK2]] | +0.48 | +0.43 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOGARAM1]] | -0.48 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[PKN2]] | -0.48 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[HCFC2]] | -0.47 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[CSTF1]] | -0.47 | -0.37 / -0.50 | both halves | 9e-05 |  |
| [[TRMT1L]] | -0.46 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[SSH2]] | -0.45 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[GALK2]] | -0.45 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[PPP1R12A]] | -0.45 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[ETAA1]] | -0.45 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[TMEM205]] | -0.44 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[LRRC37A2]] | -0.44 | -0.26 / -0.43 | both halves | 4e-04 |  |
| [[LMLN]] | -0.43 | -0.39 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC4A3]] | B | SLC4A3 activity raises SLC29A3's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 1.09× lower at baseline in the lines without SLC4A3 | 0.016 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.442). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (0.9, 39.3); signed map (-21.2, 37.8). **Vector** length 66.0, 9.71% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +8.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +5.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +1.6 |
|  | [[Pyridoxine (drug)]] 0.5 µM |  | +1.4 | +1.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.6 | -7.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.5 | -11.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -2.4 | -7.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.3 | -5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -5.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -4.6 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.4 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 29 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:71,319,259-71,381,423 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ENT3, FLJ11160, hENT3 |
| Gene groups (HGNC) | Solute carrier family 29 |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 8 pathways, smallest: Ribavirin ADME; Transport of nucleosides and free purine and pyrimidine bases across the plasma membrane; Transport of vitamins, nucleosides, and related molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZD2](https://www.uniprot.org/uniprotkb/Q9BZD2) (Equilibrative nucleoside transporter 3):

> Uniporter that mediates the facilitative transport of nucleoside across lysosomal and mitochondrial membranes. Functions as a non-electrogenic Na(+)-independent transporter. Transport activity is pH-dependent and enhanced under acidic conditions, consistent with localization to acidic intracellular compartments. Protons are not cotransported but likely modulate transport by altering the ionization state of the transporter which dictates its conformation, thereby regulating substrate …

**Summary**, from NCBI Gene [55315](https://www.ncbi.nlm.nih.gov/gene/55315):

> This gene encodes a nucleoside transporter. The encoded protein plays a role in cellular uptake of nucleosides, nucleobases, and their related analogs. Mutations in this gene have been associated with H syndrome, which is characterized by cutaneous hyperpigmentation and hypertrichosis, hepatosplenomegaly, heart anomalies, and hypogonadism. A related disorder, PHID (pigmented hypertrichosis with insulin-dependent diabetes mellitus), has also been associated with mutations at this locus. …

**Accessions** — [HGNC:23096](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23096) · Entrez [55315](https://www.ncbi.nlm.nih.gov/gene/55315) · UniProt [Q9BZD2](https://www.uniprot.org/uniprotkb/Q9BZD2) · Ensembl [ENSG00000198246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198246)

## Data

Gene col 12560: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12560); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12560, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12560]; `tensor/DDL_lfc|DDL_z.npy` [12560]; `embed/gene_vectors.npy` [12560]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12560 or target_col == 12560). Every well: [[SLC29A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC29A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
