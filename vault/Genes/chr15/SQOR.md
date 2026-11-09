---
symbol: "SQOR"
type: "gene"
col: 6062
ensembl_id: "ENSG00000137767"
name: "sulfide quinone oxidoreductase"
location: "15q21.1"
module: 139
arm: "+"
pooled_cpm: 40.21
n_lines_expressing: 43
n_dd_up: 7
n_dd_down: 27
n_dd_up_clean: 7
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 21
direction_downstream: 2
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# SQOR

*sulfide quinone oxidoreductase* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.60× (z +8.7, q 3e-15, up in 23 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.441× (z -16.0, q 0e+00, down in 36 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGTRAP]] (+0.59, fdr 2e-05), [[IRAK3]] (+0.55, fdr 2e-05), [[TLR2]] (+0.54, fdr 5e-05); moves opposite to [[HHIP]] (-0.53, fdr 3e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[FGA]] → it (grade B ⚠); 2 go from it, the strongest it → [[AGTRAP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6062.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +8.7 | 3e-15 | 23/41 (SW1417, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +7.4 | 4e-11 | 19/41 (HOP62, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +5.0 | 1e-04 | 15/41 (SW1417, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +4.9 | 2e-04 | 17/42 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.5 | 7e-04 | 12/38 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.22×** | +4.0 | 0.007 | 13/41 (HOP62, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.014 | 14/40 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +3.6 | 0.027 | 15/41 (SW1417, KATO III, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | 1.19× | +3.4 | 0.033 | 13/41 (HOP62, CFPAC-1, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.033 | 13/40 (SK-MEL-2, COLO 205, …) | rises with dose | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.033 | 13/41 (HOP62, CFPAC-1, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.039 | 8/41 (Hs 766T, NCI-H2347, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.042 | 14/41 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.19× | +3.2 | 0.049 | 13/40 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Econazole (drug)]] 5 µM |  | 1.17× | +3.1 | 0.069 | 12/41 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.18× | +3.1 | 0.069 | 7/42 (HOP62, CFPAC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6062.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.441×** | -16.0 | 0e+00 | 36/41 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.641×** | -12.3 | 2e-32 | 25/40 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.545×** | -11.9 | 3e-30 | 32/41 (A549, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.549×** | -11.7 | 1e-29 | 36/41 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.632×** | -9.0 | 3e-17 | 29/41 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.666×** | -8.0 | 2e-13 | 25/41 (CFPAC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.669×** | -7.6 | 3e-12 | 23/36 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.788×** | -6.6 | 3e-09 | 22/42 (A549, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.718×** | -6.5 | 6e-09 | 23/41 (LoVo, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.734×** | -6.0 | 9e-08 | 20/40 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.742×** | -5.8 | 3e-07 | 20/41 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.751×** | -5.6 | 1e-06 | 24/42 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **0.755×** | -5.3 | 6e-06 | 18/38 (NCI-H1792, COLO 205, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.764×** | -5.3 | 6e-06 | 20/41 (LoVo, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.779×** | -4.9 | 4e-05 | 17/39 (RPMI-7951, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.784×** | -4.8 | 7e-05 | 16/41 (A549, SW 900, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.641×** | -4.5 | 2e-04 | 16/40 (PANC-1, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.795×** | -4.5 | 2e-04 | 18/41 (NCI-H460, CFPAC-1, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.648×** | -4.4 | 3e-04 | 12/39 (A549, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.667×** | -4.1 | 1e-03 | 16/40 (A549, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.678×** | -4.0 | 0.002 | 15/40 (A549, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6062. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 113 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -26.0) |
| [[NCI-H1573 (line)]] | alt | 194 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -27.0) |
| [[BT-474 (line)]] | alt | 84.0 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.125× (z -17.6) |
| [[CFPAC-1 (line)]] | alt | 128 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -18.0) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.383× (z -15.7) |
| [[COLO 205 (line)]] | alt | 78.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -17.7) |
| [[NCI-H460 (line)]] | wt | 38.3 | 0 | 5 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.292× (z -10.3) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 0.305× (z -10.0) |
| [[PANC-1 (line)]] | alt | 70.4 | 1 | 4 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.17× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -15.9) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.415× (z -10.6) |
| [[SW 900 (line)]] | alt | 50.5 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -12.1) |
| [[LoVo (line)]] | wt | 31.8 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.275× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.324× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 46.5 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.199× (z -10.4) |
| [[LS 180 (line)]] | wt | 53.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.312× (z -12.4) |
| [[HT-29 (line)]] | alt | 24.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -9.4) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.424× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 21.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Pemetrexed (drug)]] 5 µM 0.160× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 111 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -10.1) |
| [[A498 (line)]] | wt | 92.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -14.3) |
| [[J82 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0997× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 23.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -9.1) |
| [[SNU-423 (line)]] | alt | 27.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.308× (z -9.1) |
| [[SW48 (line)]] | wt | 12.1 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0955× (z -8.7) |
| [[A-172 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.90 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.12 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.42 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.57 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.93 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.16 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6062), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGTRAP]] | +0.59 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[IRAK3]] | +0.55 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[TLR2]] | +0.54 | +0.39 / +0.60 | both halves | 5e-05 |  |
| [[MLKL]] | +0.53 | +0.52 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[XDH]] | +0.53 | +0.42 / +0.50 | both halves | 4e-05 | same gene group |
| [[NCOA3]] | +0.53 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[C3]] | +0.53 | +0.35 / +0.56 | both halves | 1e-04 | pathway: HALLMARK_ADIPOGENESIS |
| [[LINC02015]] | +0.52 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[FTH1]] | +0.51 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[VSTM2L]] | +0.51 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[PI3]] | +0.51 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[HS3ST3B1]] | +0.51 | +0.45 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HHIP]] | -0.53 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 21, C 0. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGA]] | B | FGA activity raises SQOR's level | lines that do not express FGA (43) vs lines expressing it (7) | 3.71× lower at baseline in the lines without FGA | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG |
| [[ITIH2]] | B | ITIH2 activity raises SQOR's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 2.63× lower at baseline in the lines without ITIH2 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH |
| [[GPR141]] | B | GPR141 activity raises SQOR's level | lines that do not express GPR141 (39) vs lines expressing it (11) | 2.48× lower at baseline in the lines without GPR141 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, S100A8, LINC00879 |
| [[SLPI]] | B | SLPI activity raises SQOR's level | lines that do not express SLPI (25) vs lines expressing it (25) | 2.28× lower at baseline in the lines without SLPI | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2 |
| [[TYMP]] | B | TYMP activity raises SQOR's level | lines that do not express TYMP (20) vs lines expressing it (30) | 2.43× lower at baseline in the lines without TYMP | 0.030 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[SDR16C5]] | B | SDR16C5 activity strengthens SQOR's drug response | lines that do not express SDR16C5 (22) vs lines expressing it (20) | the lines without SDR16C5 respond 0.54× as strongly (z diff +1.75); strongest at Idarubicin (hydrochloride) 5 µM: 0.95x vs 0.58x (z diff +4.4) | 0.033 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH; target measured in part of the lines; artifact flags |
| [[ITIH2]] | B | ITIH2 activity strengthens SQOR's drug response | lines that do not express ITIH2 (35) vs lines expressing it (7) | the lines without ITIH2 respond 0.83× as strongly (z diff +1.49); strongest at Topotecan (hydrochloride) 5 µM: 0.72x vs 0.41x (z diff +4.9) | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; target measured in part of the lines; artifact flags |
| [[SAA2]] | B | SAA2 activity raises SQOR's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 2.65× lower at baseline in the lines without SAA2 | 0.038 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3 |
| [[ZC3H12A]] | B | ZC3H12A activity raises SQOR's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 3.16× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[IL1R1]] | B | IL1R1 activity raises SQOR's level | lines that do not express IL1R1 (17) vs lines expressing it (33) | 2.24× lower at baseline in the lines without IL1R1 | 0.062 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, CXCL8, NR3C1 |
| [[ENOX1]] | B | ENOX1 activity raises SQOR's level | lines that do not express ENOX1 (12) vs lines expressing it (38) | 1.92× lower at baseline in the lines without ENOX1 | 0.063 | ⚠ within organs, on part of the lines; also absent: CYP1B1-AS1, HTR7, SLC1A3; maybe low, not absent |
| [[S100A9]] | B | S100A9 activity raises SQOR's level | lines that do not express S100A9 (42) vs lines expressing it (8) | 3.24× lower at baseline in the lines without S100A9 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, GSDMC, KRT20 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGTRAP]] | B | SQOR activity raises AGTRAP's level | lines that do not express SQOR (7) vs lines expressing it (43) | 1.68× lower at baseline in the lines without SQOR | 0.011 | ⚠ within organs, on part of the lines; also absent: SAT1, ITPR3, LRRC8E |
| [[ZC3H12A-DT]] | B | SQOR activity raises ZC3H12A-DT's level | lines that do not express SQOR (7) vs lines expressing it (43) | 2.01× lower at baseline in the lines without SQOR | 0.087 | ⚠ within organs, on part of the lines; also absent: SAT1, ITPR3, LRRC8E |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.574). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.1, 15.2); signed map (16.6, 31.9). **Vector** length 106, 26.6% of its response variance represented; |z| ≥ 3 in 1,138 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.6 | +8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.9 | +5.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.0 | +3.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.8 | +3.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.7 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -9.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.2 | -3.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.1 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -3.0 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -8.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -4.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -5.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.6 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | sulfide quinone oxidoreductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:45,631,148-45,691,281 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-44, SQR; previously SQRDL |
| Gene groups (HGNC) | Flavoproteins; Oxidoreductases |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 4 pathways, smallest: Sulfide oxidation to sulfate; Degradation of cysteine and homocysteine; Sulfur amino acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6N5](https://www.uniprot.org/uniprotkb/Q9Y6N5) (Sulfide:quinone oxidoreductase, mitochondrial):

> Catalyzes the oxidation of hydrogen sulfide with the help of a quinone, such as ubiquinone-10, giving rise to thiosulfate and ultimately to sulfane (molecular sulfur) atoms. Requires an additional electron acceptor; can use sulfite, sulfide or cyanide (in vitro). It is believed the in vivo electron acceptor is glutathione.

**Summary**, from NCBI Gene [58472](https://www.ncbi.nlm.nih.gov/gene/58472):

> The protein encoded by this gene may function in mitochondria to catalyze the conversion of sulfide to persulfides, thereby decreasing toxic concencrations of sulfide. Alternative splicing results in multiple transcript variants that encode the same protein. [provided by RefSeq, Sep 2012]

**Accessions** — [HGNC:20390](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20390) · Entrez [58472](https://www.ncbi.nlm.nih.gov/gene/58472) · UniProt [Q9Y6N5](https://www.uniprot.org/uniprotkb/Q9Y6N5) · Ensembl [ENSG00000137767](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137767)

## Data

Gene col 6062: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6062); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6062, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6062]; `tensor/DDL_lfc|DDL_z.npy` [6062]; `embed/gene_vectors.npy` [6062]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6062 or target_col == 6062). Every well: [[SQOR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SQOR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
