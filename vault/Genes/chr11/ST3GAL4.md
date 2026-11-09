---
symbol: "ST3GAL4"
type: "gene"
col: 3113
ensembl_id: "ENSG00000110080"
name: "ST3 beta-galactoside alpha-2,3-sialyltransferase 4"
location: "11q24.2"
module: 148
arm: "-"
pooled_cpm: 35.7
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 22
n_dd_up_clean: 5
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# ST3GAL4

*ST3 beta-galactoside alpha-2,3-sialyltransferase 4* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 0.05 µM: 1.28× (z +5.0, q 1e-04, up in 17 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.435× (z -26.3, q 0e+00, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP8]] (+0.63, fdr 4e-05), [[PIK3C2B]] (+0.61, fdr 1e-05), [[PRR5]] (+0.61, fdr 4e-05); moves opposite to [[SLC30A9]] (-0.62, fdr 1e-05), [[THAP2]] (-0.60, fdr 2e-04), [[METTL6]] (-0.60, fdr 4e-05).
> It sits in the **-** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3113.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.28×** | +5.0 | 1e-04 | 17/47 (A549, HEC-1-A, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +5.0 | 1e-04 | 15/48 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.35×** | +4.7 | 4e-04 | 17/45 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.23×** | +4.6 | 7e-04 | 19/48 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.22×** | +4.4 | 0.001 | 15/47 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 1.20× | +4.0 | 0.005 | 11/47 (SW1417, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.5 | 0.044 | 1/49 (MIA PaCa-2) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.17× | +3.4 | 0.057 | 16/47 (A549, NCI-H1573, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.11 | 3/48 (A-427, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | 1.32× | +3.1 | 0.11 | 7/48 (NCI-H2347, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.10× | +3.1 | 0.11 | 6/48 (NCI-H2347, HepG2/C3A, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.1 | 0.11 | 10/48 (A549, NCI-H1573, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3113.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.435×** | -26.3 | 0e+00 | 38/47 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.349×** | -21.1 | 0e+00 | 41/47 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.433×** | -18.0 | 0e+00 | 34/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.581×** | -17.2 | 0e+00 | 43/48 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.528×** | -14.3 | 4e-44 | 37/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.558×** | -13.0 | 9e-37 | 36/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.342×** | -12.1 | 1e-31 | 31/49 (PANC-1, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.578×** | -11.8 | 3e-30 | 32/46 (A-172, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.625×** | -10.5 | 6e-24 | 33/48 (Panc 03.27, KATO III, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.671×** | -8.9 | 3e-17 | 28/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -8.2 | 1e-14 | 25/48 (LS 180, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.701×** | -8.0 | 9e-14 | 29/48 (SNU-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.712×** | -7.6 | 2e-12 | 27/48 (LS 180, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.734×** | -6.9 | 2e-10 | 24/46 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.720×** | -6.8 | 4e-10 | 20/38 (NCI-H2030, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.567×** | -6.4 | 6e-09 | 21/47 (HOP62, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.836× | -5.7 | 5e-07 | 20/48 (A-427, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3113. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 72.8 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0861× (z -23.8) |
| [[HT-29 (line)]] | alt | 86.3 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0730× (z -21.2) |
| [[KATO III (line)]] | alt | 41.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0634× (z -18.3) |
| [[PANC-1 (line)]] | alt | 39.8 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -27.5) |
| [[HEC-1-A (line)]] | alt | 30.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -14.8) |
| [[LOX-IMVI (line)]] | wt | 27.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0923× (z -28.3) |
| [[NCI-H2030 (line)]] | alt | 44.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -20.5) |
| [[Panc 03.27 (line)]] | alt | 74.1 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -15.8) |
| [[SW480 (line)]] | alt | 20.4 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.264× (z -18.0) |
| [[A-427 (line)]] | wt | 22.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -12.8) |
| [[AsPC-1 (line)]] | alt | 29.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -14.4) |
| [[Hs 766T (line)]] | wt | 32.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -13.4) |
| [[LoVo (line)]] | wt | 52.7 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 28.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0897× (z -16.6) |
| [[NCI-H1573 (line)]] | alt | 48.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.99× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 25.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -22.4) |
| [[SW1417 (line)]] | alt | 44.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -20.9) |
| [[NCI-H460 (line)]] | wt | 22.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -10.4) |
| [[A498 (line)]] | wt | 31.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 59.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -12.0) |
| [[A-172 (line)]] | wt | 23.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -15.0) |
| [[A549 (line)]] | wt | 29.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -15.8) |
| [[C-33 A (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.146× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[CFPAC-1 (line)]] | alt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -9.4) |
| [[HOP62 (line)]] | alt | 31.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.216× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 18.9 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0771× (z -8.5) |
| [[RKO (line)]] | wt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0537× (z -15.8) |
| [[SNU-1 (line)]] | wt | 20.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0363× (z -16.8) |
| [[SW 1271 (line)]] | alt | 24.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0898× (z -8.9) |
| [[SW 900 (line)]] | alt | 19.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -8.5) |
| [[SW48 (line)]] | wt | 17.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -12.8) |
| [[AN3 CA (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3113), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP8]] | +0.63 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[PIK3C2B]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[PRR5]] | +0.61 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[RHPN2]] | +0.60 | +0.55 / +0.38 | both halves | 6e-05 |  |
| [[PEDS1]] | +0.59 | +0.55 / +0.35 | both halves | 1e-04 |  |
| [[FOXK1]] | +0.59 | +0.67 / +0.36 | both halves | 9e-05 |  |
| [[CFD]] | +0.59 | +0.43 / +0.34 | both halves | 1e-04 |  |
| [[DOK4]] | +0.59 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[MAST3]] | +0.59 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[PNKD]] | +0.58 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[CBLC]] | +0.58 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[TSEN54]] | +0.57 | +0.49 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC30A9]] | -0.62 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[THAP2]] | -0.60 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[METTL6]] | -0.60 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[HSDL2-AS1]] | -0.59 | -0.56 / -0.29 | both halves | 2e-04 |  |
| [[UBE3B]] | -0.58 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[LINC01829]] | -0.58 | -0.52 / -0.29 | both halves | 3e-04 |  |
| [[MCTS1]] | -0.58 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[TUG1]] | -0.57 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ARRDC3-AS1]] | -0.57 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[UBE2D3-AS1]] | -0.57 | -0.49 / -0.29 | both halves | 3e-04 |  |
| [[N4BP2]] | -0.57 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[CCDC90B-AS1]] | -0.56 | -0.46 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ST3GAL4's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **-** arm (projection on the module's main direction -0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.4, 4.5); signed map (-19.1, 34.3). **Vector** length 101, 24.2% of its response variance represented; |z| ≥ 3 in 1,277 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.7 | +4.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +1.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.0 | +4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.8 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +2.2 | +1.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.1 | -10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -17.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -14.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -11.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -8.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | ST3 beta-galactoside alpha-2,3-sialyltransferase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:126,355,640-126,440,344 (+) |
| Ensembl biotype | protein_coding |
| Also known as | STZ, SAT3, FLJ11867; previously CGS23, SIAT4, NANTA3, SIAT4C |
| Gene groups (HGNC) | Sialyltransferases |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 29 pathways, smallest: Maturation of protein 3a_9683673; Maturation of protein 3a_9694719; Lewis blood group biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q11206](https://www.uniprot.org/uniprotkb/Q11206) (CMP-N-acetylneuraminate-beta-galactosamide-alpha-2,3-sialyltransferase 4):

> A beta-galactoside alpha2-3 sialyltransferase involved in terminal sialylation of glycoproteins and glycolipids. Catalyzes the transfer of sialic acid (N-acetyl-neuraminic acid; Neu5Ac) from the nucleotide sugar donor CMP-Neu5Ac onto acceptor Galbeta-(1->3)-GalNAc- and Galbeta-(1->4)-GlcNAc-terminated glycoconjugates through an alpha2-3 linkage. Plays a major role in hemostasis. Responsible for sialylation of plasma VWF/von Willebrand factor, preventing its recognition by asialoglycoprotein …

**Summary**, from NCBI Gene [6484](https://www.ncbi.nlm.nih.gov/gene/6484):

> This gene encodes a member of the glycosyltransferase 29 family, a group of enzymes involved in protein glycosylation. The encoded protein is targeted to Golgi membranes but may be proteolytically processed and secreted. The gene product may also be involved in the increased expression of sialyl Lewis X antigen seen in inflammatory responses. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:10864](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10864) · Entrez [6484](https://www.ncbi.nlm.nih.gov/gene/6484) · UniProt [Q11206](https://www.uniprot.org/uniprotkb/Q11206) · Ensembl [ENSG00000110080](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110080)

## Data

Gene col 3113: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3113); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3113, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3113]; `tensor/DDL_lfc|DDL_z.npy` [3113]; `embed/gene_vectors.npy` [3113]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3113 or target_col == 3113). Every well: [[ST3GAL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST3GAL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
