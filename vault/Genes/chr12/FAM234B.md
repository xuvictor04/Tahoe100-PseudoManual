---
symbol: "FAM234B"
type: "gene"
col: 1399
ensembl_id: "ENSG00000084444"
name: "family with sequence similarity 234 member B"
location: "12p13.1"
module: 134
arm: "+"
pooled_cpm: 17.42
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 17
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 13
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# FAM234B

*family with sequence similarity 234 member B* — 12p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.34× (z +5.7, q 8e-06, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.358× (z -19.8, q 0e+00, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL6]] (+0.82, fdr 7e-06), [[HACE1]] (+0.80, fdr 7e-06), [[WASF3]] (+0.74, fdr 7e-06); moves opposite to [[ZHX2]] (-0.67, fdr 1e-05), [[PPP3CB-AS1]] (-0.65, fdr 1e-05), [[GGPS1]] (-0.64, fdr 3e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[GALNT16]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1399.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +5.7 | 8e-06 | 25/46 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +5.3 | 3e-05 | 22/46 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +5.0 | 1e-04 | 20/45 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.42×** | +4.8 | 3e-04 | 22/46 (A498, LoVo, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.004 | 21/45 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.30×** | +3.5 | 0.040 | 18/46 (NCI-H2347, A498, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +3.4 | 0.051 | 12/46 (SW480, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.26× | +3.1 | 0.13 | 13/45 (NCI-H23, C-33 A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1399.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.358×** | -19.8 | 0e+00 | 37/45 (LOX-IMVI, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.410×** | -11.7 | 5e-29 | 40/46 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.425×** | -11.6 | 5e-29 | 32/45 (C32, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.470×** | -9.9 | 7e-21 | 30/45 (C32, SNU-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.519×** | -8.6 | 1e-15 | 32/46 (NCI-H23, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.545×** | -8.0 | 2e-13 | 32/45 (SNU-1, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.561×** | -7.9 | 3e-13 | 31/45 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.701×** | -6.8 | 6e-10 | 27/45 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.608×** | -6.8 | 8e-10 | 25/42 (NCI-H23, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.618×** | -6.6 | 3e-09 | 28/45 (SNU-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.626×** | -6.4 | 9e-09 | 30/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.746×** | -5.7 | 8e-07 | 27/46 (C32, SW48, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.678×** | -5.3 | 5e-06 | 22/45 (SNU-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.749×** | -3.9 | 0.003 | 15/46 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.753×** | -3.9 | 0.004 | 19/46 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | 0.836× | -3.4 | 0.019 | 11/46 (SW 1088, HOP62, …) | all doses, flat | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.805×** | -2.9 | 0.100 | 8/45 (BT-474, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1399. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 68.2 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -23.5) |
| [[NCI-H2030 (line)]] | alt | 33.4 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 35.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -17.0) |
| [[SNU-1 (line)]] | wt | 38.9 | 0 | 5 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0965× (z -12.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.213× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 28.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0595× (z -25.5) |
| [[MIA PaCa-2 (line)]] | alt | 25.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 17.3 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.0947× (z -16.2) |
| [[NCI-H1792 (line)]] | alt | 41.5 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.53× (z +18.9) | [[Harringtonine (drug)]] 5 µM 0.152× (z -14.2) |
| [[PANC-1 (line)]] | alt | 10.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -16.4) |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 3 | — | [[Furosemide (drug)]] 0.5 µM 0.0589× (z -11.9) |
| [[A-172 (line)]] | wt | 7.70 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.107× (z -9.5) |
| [[A549 (line)]] | wt | 13.7 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.128× (z -10.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.258× (z -9.9) |
| [[HCT15 (line)]] | alt | 15.3 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0994× (z -9.7) ⚠ transcription drop; cell-cycle shift, explains ~99% of this change |
| [[HEC-1-A (line)]] | alt | 16.7 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.230× (z -9.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.370× (z -9.8) |
| [[HOP62 (line)]] | alt | 19.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -17.1) |
| [[J82 (line)]] | alt | 14.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -15.0) |
| [[SHP-77 (line)]] | alt | 12.0 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.118× (z -9.4) ⚠ toxic · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.135× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 21.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0711× (z -20.9) |
| [[SNU-423 (line)]] | alt | 16.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -19.0) |
| [[SW 900 (line)]] | alt | 19.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -11.1) |
| [[SW480 (line)]] | alt | 17.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.324× (z -9.5) |
| [[AN3 CA (line)]] | alt | 33.2 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0968× (z -8.7) |
| [[C-33 A (line)]] | alt | 64.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.8) |
| [[COLO 205 (line)]] | alt | 9.18 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.110× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 7.82 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -9.2) |
| [[HS-578T (line)]] | alt | 14.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.200× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 14.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0857× (z -10.3) |
| [[LoVo (line)]] | wt | 12.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.87× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -9.9) |
| [[RKO (line)]] | wt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -8.6) |
| [[SW48 (line)]] | wt | 25.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -10.2) |
| [[A-427 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1399), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL6]] | +0.82 | +0.82 / +0.71 | both halves | 7e-06 |  |
| [[HACE1]] | +0.80 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[WASF3]] | +0.74 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[SMARCD3]] | +0.73 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[CABIN1]] | +0.72 | +0.81 / +0.52 | both halves | 1e-05 |  |
| [[TRIT1]] | +0.72 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[PDK3]] | +0.71 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[FAM168A]] | +0.71 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[SDHAF3]] | +0.71 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[TPD52]] | +0.70 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[ATG4C]] | +0.69 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[YEATS2]] | +0.68 | +0.76 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZHX2]] | -0.67 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | -0.65 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[GGPS1]] | -0.64 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[WARS2-AS1]] | -0.64 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[C11orf58]] | -0.64 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[ITPRIPL2]] | -0.62 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[LINC00571]] | -0.61 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[MMADHC-DT]] | -0.61 | -0.67 / -0.31 | both halves | 2e-04 |  |
| [[PTPRK]] | -0.61 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[CREBBP]] | -0.60 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[UNK]] | -0.59 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[INO80D]] | -0.59 | -0.52 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 10, C 3. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT16]] | B | GALNT16 activity raises FAM234B's level | lines that do not express GALNT16 (8) vs lines expressing it (42) | 2.44× lower at baseline in the lines without GALNT16 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000237356, PRKAR2B, FRG1-DT; maybe low, not absent |
| [[MPP2]] | B | MPP2 activity raises FAM234B's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 2.02× lower at baseline in the lines without MPP2 | 0.010 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[TOP2A]] | B | TOP2A activity raises FAM234B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TMEM145]] | B | TMEM145 activity raises FAM234B's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 2.13× lower at baseline in the lines without TMEM145 | 0.048 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers FAM234B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers FAM234B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ISM2]] | B | ISM2 activity raises FAM234B's level | lines that do not express ISM2 (9) vs lines expressing it (41) | 1.82× lower at baseline in the lines without ISM2 | 0.070 | ⚠ within organs, on part of the lines; also absent: DYSF, CSRP2, LINC02609; maybe low, not absent |
| [[SLC22A3]] | B | SLC22A3 activity lowers FAM234B's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 1.80× higher at baseline in the lines without SLC22A3 | 0.070 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[FZD3]] | B | FZD3 activity raises FAM234B's level | lines that do not express FZD3 (9) vs lines expressing it (41) | 2.01× lower at baseline in the lines without FZD3 | 0.089 | ⚠ within organs, on part of the lines; also absent: FBXO16, SLC16A10, LINC02456; maybe low, not absent; its own permutation p |
| [[PCED1B]] | B | PCED1B activity lowers FAM234B's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 1.91× higher at baseline in the lines without PCED1B | 0.089 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[ASIC1]] | C | ASIC1 activity raises FAM234B's level | lines that do not express ASIC1 (3) vs lines expressing it (47) | 2.69× lower at baseline in the lines without ASIC1 | 0.050 | ⚠ few lines (3 vs 47); across organs; also absent: TBC1D19, C1orf216, ZNF391 |
| [[HACE1]] | C | HACE1 activity raises FAM234B's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 2.98× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.761). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.8, -12.9); signed map (-33.0, -7.4). **Vector** length 105, 24.9% of its response variance represented; |z| ≥ 3 in 1,018 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +5.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +4.6 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +4.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +5.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.4 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +3.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.8 | -11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.2 | -19.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -11.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -5.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.8 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -2.0 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -2.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 234 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.1 — chr12:13,044,381-13,142,521 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1467 |
| Matched by | ensembl_id |

UniProt [A2RU67](https://www.uniprot.org/uniprotkb/A2RU67) carries no function annotation.

**Summary**, from NCBI Gene [57613](https://www.ncbi.nlm.nih.gov/gene/57613):

> Predicted to be located in membrane and microtubule organizing center. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29288](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29288) · Entrez [57613](https://www.ncbi.nlm.nih.gov/gene/57613) · UniProt [A2RU67](https://www.uniprot.org/uniprotkb/A2RU67) · Ensembl [ENSG00000084444](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084444)

## Data

Gene col 1399: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1399); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1399, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1399]; `tensor/DDL_lfc|DDL_z.npy` [1399]; `embed/gene_vectors.npy` [1399]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1399 or target_col == 1399). Every well: [[FAM234B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM234B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
