---
symbol: "ANKRD18B"
type: "gene"
col: 13750
ensembl_id: "ENSG00000230453"
name: "ankyrin repeat domain 18B"
location: "9p13.3"
module: 202
arm: "+"
pooled_cpm: 7.64
n_lines_expressing: 27
n_dd_up: 29
n_dd_down: 10
n_dd_up_clean: 22
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 9
direction_downstream: 18
tags: ["gene", "module/202"]
generated_by: "tahoemap"
---

# ANKRD18B

*ankyrin repeat domain 18B* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.86× (z +22.7, q 0e+00, up in 23 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.423× (z -10.3, q 4e-22, down in 18 of 25 measured lines).
> Its strongest partners by |cos| (76 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLS3-AS1]] (+0.73, fdr 3e-05), [[GALNT7-DT]] (+0.72, fdr 4e-04), [[PCNX4-DT]] (+0.71, fdr 4e-04); moves opposite to [[CABLES2]] (-0.68, fdr 1e-04), [[YIF1B]] (-0.68, fdr 8e-04, ⚠ one half only (not replicated)), [[YIPF1]] (-0.65, fdr 4e-05), [[SNRPD2]] (-0.65, fdr 6e-05).
> It is in [[Module 202]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PAG1]] → it (grade B ⚠); 18 go from it, the strongest it → [[C7orf31]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13750.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.86×** | +22.7 | 0e+00 | 23/24 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.85×** | +17.7 | 0e+00 | 19/22 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.58×** | +14.1 | 9e-43 | 12/13 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.17×** | +13.7 | 7e-41 | 15/19 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.98×** | +11.5 | 2e-28 | 23/25 (Panc 03.27, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.47×** | +10.0 | 2e-21 | 10/16 (SW 900, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +8.7 | 2e-16 | 18/24 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +8.6 | 5e-16 | 13/23 (HOP62, SW 900, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.07×** | +8.0 | 6e-14 | 17/24 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +7.6 | 2e-12 | 16/23 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +7.4 | 7e-12 | 13/24 (NCI-H460, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +6.3 | 2e-08 | 9/25 (HOP62, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.67×** | +6.1 | 4e-08 | 15/24 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.65×** | +6.0 | 9e-08 | 17/25 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +5.3 | 4e-06 | 10/22 (A-427, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +5.2 | 6e-06 | 16/25 (A549, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +4.4 | 4e-04 | 12/25 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +4.3 | 4e-04 | 14/24 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.007 | 7/25 (A549, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13750.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.423×** | -10.3 | 4e-22 | 18/25 (Panc 03.27, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.512×** | -8.0 | 3e-13 | 16/25 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.553×** | -7.1 | 3e-10 | 19/25 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.698×** | -4.3 | 0.002 | 13/25 (Panc 03.27, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.700×** | -4.3 | 0.002 | 12/23 (SHP-77, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.521×** | -4.1 | 0.004 | 14/23 (Panc 03.27, A498, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.741×** | -3.6 | 0.026 | 7/25 (A549, NCI-H2030, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.820×** | -3.4 | 0.054 | 11/25 (A-427, A549, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.764×** | -3.2 | 0.075 | 12/24 (MIA PaCa-2, H4, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.765×** | -3.2 | 0.075 | 2/24 (NCI-H1573, SHP-77) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13750. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.4 | 4 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +16.1) | [[Panobinostat (drug)]] 5 µM 0.248× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 23.4 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -13.9) |
| [[A549 (line)]] | wt | 32.6 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +9.9) | [[Belinostat (drug)]] 5 µM 0.212× (z -9.7) |
| [[HOP62 (line)]] | alt | 3.66 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +12.9) | [[Rifaximin (drug)]] 5 µM 0.0440× (z -10.2) |
| [[SW 900 (line)]] | alt | 9.20 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.84× (z +13.2) | — |
| [[A-172 (line)]] | wt | 8.62 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +8.9) | [[Belinostat (drug)]] 5 µM 0.0854× (z -11.4) |
| [[CHP-212 (line)]] | wt | 25.5 | 0 | 2 | — | [[Drospirenone (drug)]] 0.5 µM 0.0651× (z -10.0) |
| [[J82 (line)]] | alt | 16.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +11.6) | — |
| [[SHP-77 (line)]] | alt | 17.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -10.0) |
| [[SNU-423 (line)]] | alt | 11.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +8.9) | — |
| [[A-427 (line)]] | wt | 17.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.255× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 17.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +11.2) | — |
| [[hTERT-HPNE (line)]] | wt | 9.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.29× (z +10.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.159× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 7.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 7.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +13.6) | — |
| [[NCI-H23 (line)]] | alt | 17.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -10.9) |
| [[PANC-1 (line)]] | alt | 4.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +9.0) | — |
| [[A498 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.986 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.763 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.954 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.894 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.978 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.904 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.797 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.22 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13750), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 18 of them with an alert (⚠; 18 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLS3-AS1]] | +0.73 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[GALNT7-DT]] | +0.72 | +0.60 / +0.25 | both halves | 4e-04 |  |
| [[PCNX4-DT]] | +0.71 | +0.66 / +0.25 | both halves | 4e-04 |  |
| [[PATL2]] | +0.70 | +0.68 / +0.28 | both halves | 3e-04 |  |
| [[CACNA2D1]] | +0.70 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[MZF1-AS1]] | +0.69 | +0.64 / +0.24 | both halves | 5e-04 |  |
| [[PBLD]] | +0.69 | +0.59 / +0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[PPP1R12A-AS2]] | +0.69 | +0.61 / +0.22 | both halves | 6e-04 |  |
| [[MMADHC-DT]] | +0.69 | +0.55 / +0.32 | both halves | 2e-04 |  |
| [[FRG1-DT]] | +0.68 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[MYLK-AS1]] | +0.68 | +0.60 / +0.24 | both halves | 4e-04 |  |
| [[RIPK2-DT]] | +0.68 | +0.65 / +0.31 | both halves | 2e-04 |  |
| [[PKN2-AS1]] | +0.68 | +0.64 / +0.21 | both halves | 7e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CABLES2]] | -0.68 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[YIF1B]] | -0.68 | -0.54 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[YIPF1]] | -0.65 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[SNRPD2]] | -0.65 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[MAST3]] | -0.65 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[SLC27A1]] | -0.65 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[ATRN]] | -0.64 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[ANAPC11]] | -0.63 | -0.56 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[SLC2A3]] | -0.63 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[RNF41]] | -0.63 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[TECPR1]] | -0.63 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[MPG]] | -0.62 | -0.74 / -0.23 | both halves | 5e-04 |  |
| [[EFNA4]] | -0.62 | -0.51 / -0.29 | both halves | 2e-04 |  |
| [[TMEM256]] | -0.62 | -0.53 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAG1]] | B | PAG1 activity strengthens ANKRD18B's drug response | lines that do not express PAG1 (7) vs lines expressing it (18) | the lines without PAG1 respond 0.73× as strongly (z diff +1.66); strongest at Epirubicin (hydrochloride) 5 µM: 1.14x vs 2.36x (z diff +3.6) | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers ANKRD18B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FRG1-DT]] | B | FRG1-DT activity raises ANKRD18B's level | lines that do not express FRG1-DT (7) vs lines expressing it (43) | 3.05× lower at baseline in the lines without FRG1-DT | 0.072 | ⚠ within organs, on part of the lines; also absent: GALNT16, ENSG00000272438, PRKAR2B; maybe low, not absent |
| [[SLC16A1-AS1]] | B | SLC16A1-AS1 activity raises ANKRD18B's level | lines that do not express SLC16A1-AS1 (5) vs lines expressing it (45) | 2.82× lower at baseline in the lines without SLC16A1-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: P3H4, SLC16A1, DUSP19 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ANKRD18B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ANKRD18B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MIR1915HG]] | B | MIR1915HG activity weakens ANKRD18B's drug response | lines that do not express MIR1915HG (6) vs lines expressing it (19) | the lines without MIR1915HG respond 1.58× as strongly (z diff -2.12); strongest at Dinaciclib 0.05 µM: 3.13x vs 1.63x (z diff -3.4) | 0.095 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[LRRK2]] | C | LRRK2 activity raises ANKRD18B's level | lines that do not express LRRK2 (25) vs lines expressing it (25) | 2.66× lower at baseline in the lines without LRRK2 | 0.035 | ⚠ within organs, on part of the lines; also absent: FAM110B, GFRA1, ADAMTS1; co-absent with the target |
| [[DPY19L2]] | C | DPY19L2 activity raises ANKRD18B's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 2.50× lower at baseline in the lines without DPY19L2 | 0.086 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 16, C 2. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C7orf31]] | B | ANKRD18B activity raises C7orf31's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.59× lower at baseline in the lines without ANKRD18B | 0.014 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[CTBP1-DT]] | B | ANKRD18B activity raises CTBP1-DT's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.19× lower at baseline in the lines without ANKRD18B | 0.025 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[FRG1-DT]] | B | ANKRD18B activity raises FRG1-DT's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.70× lower at baseline in the lines without ANKRD18B | 0.030 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[PBLD]] | B | ANKRD18B activity raises PBLD's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.19× lower at baseline in the lines without ANKRD18B | 0.038 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[CTBP1-DT]] | B | ANKRD18B activity strengthens CTBP1-DT's drug response | lines that do not express ANKRD18B (22) vs lines expressing it (25) | the lines without ANKRD18B respond 0.93× as strongly (z diff +0.45); strongest at Digitoxin 5 µM: 0.36x vs 0.24x (z diff +2.1) | 0.054 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2; target measured in part of the lines; both ways; artifact flags |
| [[TMEM202-AS1]] | B | ANKRD18B activity raises TMEM202-AS1's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.16× lower at baseline in the lines without ANKRD18B | 0.068 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[TM9SF5P]] | B | ANKRD18B activity raises TM9SF5P's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.48× lower at baseline in the lines without ANKRD18B | 0.071 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[VPS35L]] | B | ANKRD18B activity raises VPS35L's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 2.28× lower at baseline in the lines without ANKRD18B | 0.078 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[TENM3-AS1]] | B | ANKRD18B activity raises TENM3-AS1's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.59× lower at baseline in the lines without ANKRD18B | 0.080 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[ATP6V1E2]] | B | ANKRD18B activity raises ATP6V1E2's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.50× lower at baseline in the lines without ANKRD18B | 0.081 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[EIF1B-AS1]] | B | ANKRD18B activity raises EIF1B-AS1's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.26× lower at baseline in the lines without ANKRD18B | 0.088 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[ZC3H4]] | B | ANKRD18B activity lowers ZC3H4's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.14× higher at baseline in the lines without ANKRD18B | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |

## Where it sits

- **Module**: [[Module 202]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.831). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.4, 12.4); signed map (25.4, -12.0). **Vector** length 73.8, 19.1% of its response variance represented; |z| ≥ 3 in 621 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +22.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +13.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +17.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +1.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.5 | -10.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.9 | -7.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.9 | -8.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.3 | -4.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -4.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 18B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:33,524,251-33,608,848 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA255A11.3 |
| Gene groups (HGNC) | N-Ank proteins |
| Matched by | ensembl_id |

UniProt [A2A2Z9](https://www.uniprot.org/uniprotkb/A2A2Z9) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:23644](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23644) · Entrez [441459](https://www.ncbi.nlm.nih.gov/gene/441459) · UniProt [A2A2Z9](https://www.uniprot.org/uniprotkb/A2A2Z9) · Ensembl [ENSG00000230453](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000230453)

## Data

Gene col 13750: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13750); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13750, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13750]; `tensor/DDL_lfc|DDL_z.npy` [13750]; `embed/gene_vectors.npy` [13750]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13750 or target_col == 13750). Every well: [[ANKRD18B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD18B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
