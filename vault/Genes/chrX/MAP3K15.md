---
symbol: "MAP3K15"
type: "gene"
col: 11133
ensembl_id: "ENSG00000180815"
name: "mitogen-activated protein kinase kinase kinase 15"
location: "Xp22.12"
module: 132
arm: "+"
pooled_cpm: 16.37
n_lines_expressing: 31
n_dd_up: 3
n_dd_down: 29
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 9
direction_downstream: 11
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# MAP3K15

*mitogen-activated protein kinase kinase kinase 15* — Xp22.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.48× (z +6.3, q 2e-07, up in 13 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (17 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.322× (z -17.5, q 0e+00, down in 26 of 28 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ISM2]] (+0.57, fdr 1e-05), [[UPK1A-AS1]] (+0.57, fdr 1e-05), [[C2orf72]] (+0.56, fdr 2e-05); moves opposite to [[MYO7B]] (-0.43, fdr 1e-04), [[BACE1]] (-0.43, fdr 1e-04), [[SLC25A46]] (-0.41, fdr 1e-04).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 11 go from it, the strongest it → [[CECR2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11133.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +6.3 | 2e-07 | 13/29 (NCI-H1573, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.8 | 4e-04 | 8/29 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.33×** | +4.5 | 0.001 | 9/29 (SW480, CFPAC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11133.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.322×** | -17.5 | 0e+00 | 26/28 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.498×** | -15.8 | 0e+00 | 25/28 (NCI-H2347, A549, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.424×** | -13.7 | 1e-40 | 23/29 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.549×** | -13.6 | 7e-40 | 25/29 (NCI-H1792, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.483×** | -11.7 | 2e-29 | 22/29 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.513×** | -10.7 | 9e-25 | 23/28 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.527×** | -10.3 | 9e-23 | 22/29 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.514×** | -10.2 | 9e-23 | 22/27 (NCI-H1792, HCT15, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.529×** | -10.2 | 1e-22 | 21/29 (SNU-1, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.582×** | -8.3 | 5e-15 | 19/29 (NCI-H2030, SNU-1, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.422×** | -7.2 | 3e-11 | 21/29 (NCI-H2347, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.623×** | -7.0 | 1e-10 | 17/24 (SNU-423, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **0.670×** | -6.4 | 6e-09 | 20/27 (NCI-H1792, HepG2/C3A, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.690×** | -6.0 | 1e-07 | 13/29 (SNU-1, SW480, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.783×** | -5.5 | 1e-06 | 19/29 (SNU-423, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.826×** | -4.3 | 4e-04 | 16/29 (SK-MEL-2, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.763×** | -4.3 | 4e-04 | 12/29 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.645×** | -3.7 | 0.006 | 15/28 (LoVo, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.811×** | -3.4 | 0.016 | 5/29 (A-172, AN3 CA, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.824×** | -3.1 | 0.038 | 8/29 (H4, SNU-423, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.822×** | -3.0 | 0.050 | 8/29 (AN3 CA, SNU-423, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.884× | -2.8 | 0.092 | 6/29 (NCI-H2347, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11133. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 49.2 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -24.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -17.4) |
| [[NCI-H1792 (line)]] | alt | 96.4 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -23.9) |
| [[SNU-423 (line)]] | alt | 23.9 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -16.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.119× (z -11.1) |
| [[PANC-1 (line)]] | alt | 24.3 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -20.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -15.3) |
| [[SNU-1 (line)]] | wt | 48.1 | 0 | 7 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0629× (z -16.8) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.0742× (z -15.8) |
| [[A-172 (line)]] | wt | 17.0 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -14.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.166× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 19.7 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0836× (z -17.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -9.9) |
| [[SW480 (line)]] | alt | 24.0 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -12.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -10.1) |
| [[A549 (line)]] | wt | 31.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -21.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.169× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 26.2 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -12.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.158× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 20.5 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.128× (z -15.8) |
| [[SK-MEL-2 (line)]] | alt | 24.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -14.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -11.4) |
| [[A-427 (line)]] | wt | 47.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.319× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 29.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0605× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[LoVo (line)]] | wt | 17.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -11.1) |
| [[HOP62 (line)]] | alt | 11.4 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.141× (z -11.2) ⚠ toxic |
| [[HCT15 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0860× (z -10.1) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 9.56 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[NCI-H1573 (line)]] | alt | 7.20 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -9.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 8.26 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0651× (z -9.6) |
| [[A498 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.17 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11133), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISM2]] | +0.57 | +0.51 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[UPK1A-AS1]] | +0.57 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[C2orf72]] | +0.56 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[NEXMIF]] | +0.54 | +0.54 / +0.41 | both halves | 4e-05 | **novel candidate** |
| [[SDK1]] | +0.53 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[SULT4A1]] | +0.52 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[APBA2]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[MAPT]] | +0.51 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[BRSK2]] | +0.50 | +0.43 / +0.40 | both halves | 4e-05 |  |
| [[TMEM74B]] | +0.49 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[RAB6B]] | +0.47 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[SNX10]] | +0.47 | +0.46 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO7B]] | -0.43 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[BACE1]] | -0.43 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[SLC25A46]] | -0.41 | -0.47 / -0.32 | both halves | 1e-04 |  |
| [[TTLL11]] | -0.40 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[SLC35B3]] | -0.40 | -0.49 / -0.24 | both halves | 4e-04 |  |
| [[UGT1A9]] | -0.40 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[GCNT3]] | -0.38 | -0.39 / -0.29 | both halves | 2e-04 |  |
| [[SEPTIN9-DT]] | -0.38 | -0.39 / -0.24 | both halves | 5e-04 |  |
| [[PTPRB]] | -0.38 | -0.42 / -0.22 | both halves | 6e-04 |  |
| [[TMEM232]] | -0.37 | -0.43 / -0.24 | both halves | 5e-04 |  |
| [[GNA14]] | -0.37 | -0.41 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MAP3K15's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RAB6B]] | B | RAB6B activity raises MAP3K15's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 2.37× lower at baseline in the lines without RAB6B | 0.062 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS |
| [[TCF7L1]] | B | TCF7L1 activity raises MAP3K15's level | lines that do not express TCF7L1 (12) vs lines expressing it (38) | 2.55× lower at baseline in the lines without TCF7L1 | 0.067 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A |
| [[BRSK2]] | B | BRSK2 activity raises MAP3K15's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 2.10× lower at baseline in the lines without BRSK2 | 0.078 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[LINC02575]] | B | LINC02575 activity raises MAP3K15's level | lines that do not express LINC02575 (32) vs lines expressing it (18) | 2.46× lower at baseline in the lines without LINC02575 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000289309, LINC01205, MSRB3-AS1 |
| [[FAM124A]] | B | FAM124A activity raises MAP3K15's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 2.33× lower at baseline in the lines without FAM124A | 0.084 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1 |
| [[UPK1A-AS1]] | B | UPK1A-AS1 activity raises MAP3K15's level | lines that do not express UPK1A-AS1 (18) vs lines expressing it (32) | 2.53× lower at baseline in the lines without UPK1A-AS1 | 0.099 | ⚠ within organs, on part of the lines; also absent: CERS4, SUSD5, WIPF1 |
| [[STOX2]] | C | STOX2 activity raises MAP3K15's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 2.42× lower at baseline in the lines without STOX2 | 0.030 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27; co-absent with the target |
| [[RASGEF1C]] | C | RASGEF1C activity raises MAP3K15's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 2.93× lower at baseline in the lines without RASGEF1C | 0.0997 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CECR2]] | B | MAP3K15 activity raises CECR2's level | lines that do not express MAP3K15 (19) vs lines expressing it (31) | 2.97× lower at baseline in the lines without MAP3K15 | 0.016 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| [[CYS1]] | B | MAP3K15 activity raises CYS1's level | lines that do not express MAP3K15 (19) vs lines expressing it (31) | 1.70× lower at baseline in the lines without MAP3K15 | 0.033 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| [[KIF1A]] | B | MAP3K15 activity raises KIF1A's level | lines that do not express MAP3K15 (19) vs lines expressing it (31) | 2.90× lower at baseline in the lines without MAP3K15 | 0.042 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| cells under [[Ouabain (Octahydrate) (drug)]] 0.05 µM | B | MAP3K15 activity lowers the cells' numbers under Ouabain (Octahydrate) 0.05 µM (makes them more sensitive) | lines that do not express MAP3K15 (19) vs lines expressing it (29) | the lines without MAP3K15: 1.21× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| [[CASKIN1]] | B | MAP3K15 activity raises CASKIN1's level | lines that do not express MAP3K15 (19) vs lines expressing it (31) | 1.70× lower at baseline in the lines without MAP3K15 | 0.045 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| [[HOMER2]] | B | MAP3K15 activity raises HOMER2's level | lines that do not express MAP3K15 (19) vs lines expressing it (31) | 2.21× lower at baseline in the lines without MAP3K15 | 0.056 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| cells under [[AZD2858 (drug)]] 0.5 µM | B | MAP3K15 activity lowers the cells' numbers under AZD2858 0.5 µM (makes them more sensitive) | lines that do not express MAP3K15 (19) vs lines expressing it (29) | the lines without MAP3K15: 1.24× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| [[C2orf72]] | B | MAP3K15 activity raises C2orf72's level | lines that do not express MAP3K15 (19) vs lines expressing it (31) | 1.64× lower at baseline in the lines without MAP3K15 | 0.070 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| [[MAPT]] | B | MAP3K15 activity raises MAPT's level | lines that do not express MAP3K15 (19) vs lines expressing it (31) | 2.60× lower at baseline in the lines without MAP3K15 | 0.073 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| [[RASSF2]] | B | MAP3K15 activity raises RASSF2's level | lines that do not express MAP3K15 (19) vs lines expressing it (31) | 1.75× lower at baseline in the lines without MAP3K15 | 0.083 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| [[ISM2]] | B | MAP3K15 activity raises ISM2's level | lines that do not express MAP3K15 (19) vs lines expressing it (31) | 1.75× lower at baseline in the lines without MAP3K15 | 0.0996 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.506). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.5, 45.1); signed map (-29.3, 35.3). **Vector** length 69.6, 15.8% of its response variance represented; |z| ≥ 3 in 778 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +6.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.2 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +4.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.3 | -0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.3 | +0.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.1 | -10.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.2 | -10.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | -1.8 | -5.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -0.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -1.6 | -4.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.1 | -3.0 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.12 — chrX:19,360,056-19,515,508 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA723P2.3, FLJ16518, ASK3 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; STE11 kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZN16](https://www.uniprot.org/uniprotkb/Q6ZN16) (Mitogen-activated protein kinase kinase kinase 15):

> Serine/threonine kinase which acts as a component of the MAP kinase signal transduction pathway. Once activated, acts as an upstream activator of the p38 MAPK signal transduction cascade through the phosphorylation and activation of several MAP kinase kinases. May function in a signal transduction pathway that is activated by various cell stresses and leads to apoptosis. Involved in phosphorylation of WNK4 in response to osmotic stress or hypotonic low-chloride stimulation via the p38 MAPK …

**Summary**, from NCBI Gene [389840](https://www.ncbi.nlm.nih.gov/gene/389840):

> The protein encoded by this gene is a member of the mitogen-activated protein kinase (MAPK) family. These family members function in a protein kinase signal transduction cascade, where an activated MAPK kinase kinase (MAP3K) phosphorylates and activates a specific MAPK kinase (MAP2K), which then activates a specific MAPK. This MAP3K protein plays an essential role in apoptotic cell death triggered by cellular stresses. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:31689](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31689) · Entrez [389840](https://www.ncbi.nlm.nih.gov/gene/389840) · UniProt [Q6ZN16](https://www.uniprot.org/uniprotkb/Q6ZN16) · Ensembl [ENSG00000180815](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180815)

## Data

Gene col 11133: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11133); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11133, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11133]; `tensor/DDL_lfc|DDL_z.npy` [11133]; `embed/gene_vectors.npy` [11133]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11133 or target_col == 11133). Every well: [[MAP3K15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
