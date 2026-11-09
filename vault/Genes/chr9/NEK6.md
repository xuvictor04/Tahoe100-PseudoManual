---
symbol: "NEK6"
type: "gene"
col: 4064
ensembl_id: "ENSG00000119408"
name: "NIMA related kinase 6"
location: "9q33.3"
module: 33
arm: "+"
pooled_cpm: 73.05
n_lines_expressing: 48
n_dd_up: 1
n_dd_down: 24
n_dd_up_clean: 1
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# NEK6

*NIMA related kinase 6* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Selinexor (drug)]] 0.05 µM: 1.41× (z +4.8, q 9e-04, up in 26 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 2.06×).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.216× (z -21.6, q 0e+00, down in 46 of 46 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNNM1]] (+0.59, fdr 3e-05), [[PFKM]] (+0.55, fdr 1e-04), [[SLC25A30]] (+0.55, fdr 6e-05); moves opposite to [[SOS2]] (-0.58, fdr 3e-05), [[RAB33B-AS1]] (-0.53, fdr 2e-04), [[FBXO11]] (-0.53, fdr 1e-03, ⚠ not reproduced), [[KIAA2026]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4064.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 2.06×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM |  | **1.41×** | +4.8 | 9e-04 | 26/46 (NCI-H1573, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.5 | 0.11 | 19/46 (AsPC-1, BT-474, …) | rises with dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.28× | +3.4 | 0.11 | 21/46 (KATO III, HT-29, …) | inconsistent across doses | position effect removed |
| [[Folic acid (drug)]] 5 µM |  | 1.17× | +3.1 | 0.29 | 10/46 (NCI-H1792, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4064.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.216×** | -21.6 | 0e+00 | 46/46 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.229×** | -20.8 | 0e+00 | 45/46 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.311×** | -16.5 | 0e+00 | 46/46 (A549, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.446×** | -16.1 | 0e+00 | 42/46 (J82, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.490×** | -9.7 | 4e-20 | 40/46 (A-172, RKO, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.505×** | -9.3 | 2e-18 | 40/48 (LOX-IMVI, C32, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.547×** | -8.5 | 2e-15 | 41/46 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.575×** | -7.8 | 4e-13 | 40/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.571×** | -7.6 | 2e-12 | 38/45 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.719×** | -6.6 | 2e-09 | 29/46 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.616×** | -6.6 | 2e-09 | 36/45 (J82, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.663×** | -5.8 | 3e-07 | 27/46 (LOX-IMVI, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.688×** | -5.3 | 6e-06 | 35/46 (KATO III, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.777×** | -5.0 | 2e-05 | 26/46 (A-172, Hs 766T, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.722×** | -4.4 | 4e-04 | 25/46 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~21% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.744×** | -3.9 | 0.003 | 24/46 (LOX-IMVI, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.592×** | -3.9 | 0.003 | 26/47 (A549, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4064. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 128 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -24.2) |
| [[A-172 (line)]] | wt | 101 | 1 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -14.9) |
| [[A549 (line)]] | wt | 144 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.107× (z -21.1) |
| [[C32 (line)]] | wt | 70.9 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -17.7) |
| [[J82 (line)]] | alt | 139 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -22.1) |
| [[MIA PaCa-2 (line)]] | alt | 54.9 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -19.0) |
| [[HOP62 (line)]] | alt | 61.0 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.110× (z -18.2) |
| [[PANC-1 (line)]] | alt | 84.1 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -23.3) |
| [[SW480 (line)]] | alt | 57.6 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -19.6) |
| [[Hs 766T (line)]] | wt | 70.9 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -13.7) |
| [[NCI-H460 (line)]] | wt | 48.5 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -17.9) |
| [[Panc 03.27 (line)]] | alt | 55.3 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.152× (z -15.4) |
| [[RPMI-7951 (line)]] | alt | 57.7 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -13.3) |
| [[SNU-423 (line)]] | alt | 167 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.123× (z -18.6) |
| [[A498 (line)]] | wt | 160 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -20.4) |
| [[COLO 205 (line)]] | alt | 95.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0832× (z -17.5) |
| [[HEC-1-A (line)]] | alt | 117 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.175× (z -16.9) |
| [[HS-578T (line)]] | alt | 67.0 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.199× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 65.0 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -15.7) |
| [[RKO (line)]] | wt | 63.1 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -12.5) |
| [[SW 900 (line)]] | alt | 46.2 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 111 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -20.0) |
| [[KATO III (line)]] | alt | 192 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -19.0) |
| [[SK-MEL-2 (line)]] | alt | 54.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -10.2) |
| [[HCT15 (line)]] | alt | 67.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.263× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 89.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -14.0) |
| [[hTERT-HPNE (line)]] | wt | 60.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 29.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -12.7) |
| [[NCI-H2030 (line)]] | alt | 33.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -14.4) |
| [[SNU-1 (line)]] | wt | 59.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.212× (z -10.7) |
| [[BT-474 (line)]] | alt | 106 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -13.0) |
| [[LoVo (line)]] | wt | 19.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.247× (z -9.8) |
| [[LS 180 (line)]] | wt | 55.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.270× (z -11.3) |
| [[AN3 CA (line)]] | alt | 57.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.125× (z -10.7) |
| [[C-33 A (line)]] | alt | 54.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.309× (z -8.5) |
| [[H4 (line)]] | wt | 70.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -12.7) |
| [[NCI-H2347 (line)]] | alt | 42.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -11.5) |
| [[SW 1271 (line)]] | alt | 112 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -10.6) |
| [[SW1417 (line)]] | alt | 27.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -11.2) |
| [[SW48 (line)]] | wt | 36.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -8.5) |
| [[A-427 (line)]] | wt | 15.3 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.63 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 44.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4064), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNNM1]] | +0.59 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[PFKM]] | +0.55 | +0.34 / +0.52 | both halves | 1e-04 |  |
| [[SLC25A30]] | +0.55 | +0.38 / +0.39 | both halves | 6e-05 |  |
| [[KIRREL1]] | +0.54 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[G3BP1]] | +0.51 | +0.32 / +0.50 | both halves | 2e-04 |  |
| [[SORD]] | +0.49 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[ZC3HAV1L]] | +0.47 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[SMYD2]] | +0.47 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[DDHD2]] | +0.46 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[ZNF589]] | +0.46 | +0.34 / +0.30 | both halves | 2e-04 |  |
| [[DIXDC1]] | +0.46 | +0.42 / +0.38 | both halves | 6e-05 |  |
| [[LRRC58]] | +0.46 | +0.20 / +0.42 | both halves | 7e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOS2]] | -0.58 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[RAB33B-AS1]] | -0.53 | -0.32 / -0.58 | both halves | 2e-04 |  |
| [[FBXO11]] | -0.53 | -0.18 / -0.41 | ⚠ not reproduced | 1e-03 |  |
| [[KIAA2026]] | -0.50 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[FBXW7]] | -0.50 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[SELENOK]] | -0.49 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[HEATR5A]] | -0.48 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[KIAA0232]] | -0.47 | -0.24 / -0.45 | both halves | 5e-04 |  |
| [[SHOC2]] | -0.46 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[ZBTB7A]] | -0.46 | -0.27 / -0.47 | both halves | 3e-04 |  |
| [[CDK13]] | -0.46 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[ANKHD1]] | -0.45 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[LINC00685]] | -0.45 | -0.44 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NEK6's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.274). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.1, -19.1); signed map (-19.0, -42.7). **Vector** length 89.4, 24.6% of its response variance represented; |z| ≥ 3 in 1,225 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.7 | -0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.2 | +3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.9 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.8 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +0.1 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +2.6 | +2.5 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.5 | +1.4 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.8 | -7.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -3.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.5 | -3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -5.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.3 | +0.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | NIMA related kinase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:124,257,606-124,353,307 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SID6-1512 |
| Gene groups (HGNC) | NIMA related kinase family |
| Reactome | 9 pathways, smallest: Activation of NIMA Kinases NEK9, NEK6, NEK7; Nuclear Pore Complex (NPC) Disassembly; Nuclear Envelope Breakdown |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HC98](https://www.uniprot.org/uniprotkb/Q9HC98) (Serine/threonine-protein kinase Nek6):

> Protein kinase which plays an important role in mitotic cell cycle progression. Required for chromosome segregation at metaphase-anaphase transition, robust mitotic spindle formation and cytokinesis. Phosphorylates ATF4, CIRSR, PTN, RAD26L, RBBP6, RPS7, RPS6KB1, TRIP4, STAT3 and histones H1 and H3. Phosphorylates KIF11 to promote mitotic spindle formation. Involved in G2/M phase cell cycle arrest induced by DNA damage. Inhibition of activity results in apoptosis. May contribute to tumorigenesis …

**Summary**, from NCBI Gene [10783](https://www.ncbi.nlm.nih.gov/gene/10783):

> The protein encoded by this gene is a kinase required for progression through the metaphase portion of mitosis. Inhibition of the encoded protein can lead to apoptosis. This protein also can enhance tumorigenesis by suppressing tumor cell senescence. Several transcript variants encoding a few different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:7749](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7749) · Entrez [10783](https://www.ncbi.nlm.nih.gov/gene/10783) · UniProt [Q9HC98](https://www.uniprot.org/uniprotkb/Q9HC98) · Ensembl [ENSG00000119408](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119408)

## Data

Gene col 4064: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4064); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4064, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4064]; `tensor/DDL_lfc|DDL_z.npy` [4064]; `embed/gene_vectors.npy` [4064]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4064 or target_col == 4064). Every well: [[NEK6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEK6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
