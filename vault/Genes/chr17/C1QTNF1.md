---
symbol: "C1QTNF1"
type: "gene"
col: 10445
ensembl_id: "ENSG00000173918"
name: "C1q and TNF related 1"
location: "17q25.3"
module: 14
arm: "+"
pooled_cpm: 12.05
n_lines_expressing: 30
n_dd_up: 12
n_dd_down: 27
n_dd_up_clean: 12
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 11
direction_downstream: 14
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# C1QTNF1

*C1q and TNF related 1* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.66× (z +9.3, q 9e-18, up in 12 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.231× (z -18.9, q 0e+00, down in 26 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1QTNF1-AS1]] (+0.76, fdr 7e-06, ⚠ same locus), [[WAKMAR2]] (+0.63, fdr 1e-05), [[MSC]] (+0.62, fdr 1e-05), [[ZC3H12A]] (+0.61, fdr 2e-05); moves opposite to [[LINC02935]] (-0.49, fdr 9e-05), [[STRN]] (-0.49, fdr 1e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[RHCG]] → it (grade B ⚠); 14 go from it, the strongest it → [[IRAK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10445.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +9.3 | 9e-18 | 12/27 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.95×** | +8.3 | 2e-14 | 15/27 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.97×** | +7.4 | 3e-11 | 14/27 (HOP62, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 0.001 | 11/26 (A-172, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.026 | 4/28 (NCI-H2030, C32, …) | rises with dose |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.32×** | +3.6 | 0.026 | 5/27 (NCI-H2030, A549, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.026 | 6/27 (SNU-423, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.032 | 9/27 (HOP62, H4, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.19× | +3.3 | 0.066 | 5/27 (A-172, HOP62, …) | top dose only | position effect removed |
| [[Cytarabine (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.070 | 6/27 (hTERT-HPNE, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.070 | 4/27 (HOP62, KATO III, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.070 | 5/27 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.086 | 4/27 (Panc 03.27, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Oxaprozin (drug)]] 0.5 µM |  | 1.26× | +3.0 | 0.10 | 7/27 (NCI-H2030, AsPC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10445.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.231×** | -18.9 | 0e+00 | 26/28 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.255×** | -17.6 | 0e+00 | 25/27 (NCI-H23, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.260×** | -17.4 | 0e+00 | 26/28 (NCI-H23, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.387×** | -12.2 | 4e-32 | 22/28 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.417×** | -11.3 | 2e-27 | 22/27 (NCI-H23, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.450×** | -10.3 | 7e-23 | 21/28 (NCI-H23, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.461×** | -10.0 | 2e-21 | 18/27 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.464×** | -9.9 | 3e-21 | 20/24 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.468×** | -9.8 | 1e-20 | 21/27 (SNU-423, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.490×** | -9.2 | 3e-18 | 19/27 (RKO, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.495×** | -9.1 | 7e-18 | 17/26 (NCI-H23, SNU-423, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.495×** | -9.0 | 8e-18 | 21/28 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.497×** | -8.5 | 9e-16 | 18/27 (SNU-423, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.548×** | -7.4 | 4e-12 | 13/23 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.579×** | -7.0 | 9e-11 | 18/28 (HOP62, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.629×** | -6.0 | 9e-08 | 16/27 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.453×** | -5.3 | 3e-06 | 15/27 (NCI-H23, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10445. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 64.0 | 0 | 18 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0260× (z -30.9) |
| [[HOP62 (line)]] | alt | 26.5 | 3 | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.69× (z +20.3) | [[Panobinostat (drug)]] 5 µM 0.121× (z -14.9) |
| [[NCI-H1792 (line)]] | alt | 84.0 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0180× (z -30.2) |
| [[HS-578T (line)]] | alt | 29.0 | 3 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 9.25× (z +19.6) | [[Panobinostat (drug)]] 0.5 µM 0.0590× (z -17.6) |
| [[SNU-423 (line)]] | alt | 45.1 | 2 | 6 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.0533× (z -20.1) |
| [[A-172 (line)]] | wt | 30.8 | 3 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +13.5) | [[Panobinostat (drug)]] 5 µM 0.0808× (z -17.0) |
| [[RPMI-7951 (line)]] | alt | 66.4 | 0 | 7 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.135× (z -14.4) |
| [[SW480 (line)]] | alt | 8.46 | 0 | 7 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0872× (z -14.9) |
| [[A549 (line)]] | wt | 73.7 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0266× (z -27.4) |
| [[RKO (line)]] | wt | 5.85 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0654× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 19.8 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.23× (z +15.5) | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -9.6) |
| [[SW1417 (line)]] | alt | 5.89 | 0 | 2 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0939× (z -8.9) |
| [[C32 (line)]] | wt | 6.97 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0952× (z -8.7) |
| [[H4 (line)]] | wt | 12.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0324× (z -12.2) |
| [[J82 (line)]] | alt | 4.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.07× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 6.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.93× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.137× (z -8.9) |
| [[SW 900 (line)]] | alt | 8.13 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0890× (z -8.5) |
| [[A-427 (line)]] | wt | 0.685 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.987 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.914 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.977 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.735 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.811 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10445), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1QTNF1-AS1]] | +0.76 | +0.73 / +0.60 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[WAKMAR2]] | +0.63 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[MSC]] | +0.62 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[ZC3H12A]] | +0.61 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[S100A3]] | +0.60 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[IKBKE]] | +0.60 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ZC3H12C]] | +0.60 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[SLC2A6]] | +0.60 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[EBI3]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[TNFAIP3]] | +0.59 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[CCL5]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SOD2]] | +0.58 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[SSPN]] | +0.58 | +0.61 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02935]] | -0.49 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[STRN]] | -0.49 | -0.42 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHCG]] | B | RHCG activity raises C1QTNF1's level | lines that do not express RHCG (33) vs lines expressing it (17) | 2.73× lower at baseline in the lines without RHCG | 0.020 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[ARNT2]] | B | ARNT2 activity raises C1QTNF1's level | lines that do not express ARNT2 (22) vs lines expressing it (28) | 2.89× lower at baseline in the lines without ARNT2 | 0.030 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, NRN1, LINC02015 |
| [[LINC02015]] | B | LINC02015 activity raises C1QTNF1's level | lines that do not express LINC02015 (27) vs lines expressing it (23) | 2.62× lower at baseline in the lines without LINC02015 | 0.065 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, CRLF2, PXDN |
| [[ARNT2-DT]] | B | ARNT2-DT activity raises C1QTNF1's level | lines that do not express ARNT2-DT (27) vs lines expressing it (23) | 2.60× lower at baseline in the lines without ARNT2-DT | 0.079 | ⚠ within organs, on part of the lines; also absent: ARNT2, SOX11, ENSG00000233491 |
| [[TOP2A]] | B | TOP2A activity lowers C1QTNF1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SYNPO]] | B | SYNPO activity raises C1QTNF1's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 3.00× lower at baseline in the lines without SYNPO | 0.093 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[ICAM1]] | B | ICAM1 activity raises C1QTNF1's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 2.34× lower at baseline in the lines without ICAM1 | 0.093 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[C1QTNF1-AS1]] | C | C1QTNF1-AS1 activity raises C1QTNF1's level | lines that do not express C1QTNF1-AS1 (24) vs lines expressing it (26) | 3.60× lower at baseline in the lines without C1QTNF1-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ADAMTS12, ENSG00000287335, FBLN2; maybe low, not absent; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises C1QTNF1's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 5.31× lower at baseline in the lines without PAPPA | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[GYPC]] | C | GYPC activity raises C1QTNF1's level | lines that do not express GYPC (35) vs lines expressing it (15) | 4.53× lower at baseline in the lines without GYPC | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4; co-absent with the target |
| [[MSC]] | C | MSC activity raises C1QTNF1's level | lines that do not express MSC (34) vs lines expressing it (16) | 3.98× lower at baseline in the lines without MSC | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 7, C 7. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRAK2]] | B | C1QTNF1 activity raises IRAK2's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 1.74× lower at baseline in the lines without C1QTNF1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3 |
| [[RUNX2]] | B | C1QTNF1 activity raises RUNX2's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 2.78× lower at baseline in the lines without C1QTNF1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3 |
| [[RFTN1]] | B | C1QTNF1 activity raises RFTN1's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 2.53× lower at baseline in the lines without C1QTNF1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3 |
| [[LINC01828]] | B | C1QTNF1 activity raises LINC01828's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 2.03× lower at baseline in the lines without C1QTNF1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3 |
| [[DSE]] | B | C1QTNF1 activity raises DSE's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 1.85× lower at baseline in the lines without C1QTNF1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3 |
| [[RHCG]] | B | C1QTNF1 activity raises RHCG's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 1.75× lower at baseline in the lines without C1QTNF1 | 0.095 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3 |
| [[HIVEP2]] | B | C1QTNF1 activity raises HIVEP2's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 1.36× lower at baseline in the lines without C1QTNF1 | 0.096 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3 |
| [[TNC]] | C | C1QTNF1 activity raises TNC's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 4.59× lower at baseline in the lines without C1QTNF1 | 0.015 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3; co-absent with the target |
| [[C1QTNF1-AS1]] | C | C1QTNF1 activity raises C1QTNF1-AS1's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 1.53× lower at baseline in the lines without C1QTNF1 | 0.045 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3; co-absent with the target |
| [[SLC43A3]] | C | C1QTNF1 activity raises SLC43A3's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 4.34× lower at baseline in the lines without C1QTNF1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3; co-absent with the target |
| [[PAPPA]] | C | C1QTNF1 activity raises PAPPA's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 3.09× lower at baseline in the lines without C1QTNF1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3; co-absent with the target |
| [[GYPC]] | C | C1QTNF1 activity raises GYPC's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 3.42× lower at baseline in the lines without C1QTNF1 | 0.059 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.5, 7.9); signed map (28.7, 5.3). **Vector** length 79.1, 18.6% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NF-kB* (control, mean cos +0.50 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +9.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +7.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.9 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.8 | +3.3 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -11.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -12.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.9 | -17.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | C1q and TNF related 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:79,022,814-79,049,788 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CTRP1, ZSIG37, GIP, FLJ90694 |
| Gene groups (HGNC) | C1q and TNF related |
| Matched by | ensembl_id |

UniProt [Q9BXJ1](https://www.uniprot.org/uniprotkb/Q9BXJ1) carries no function annotation.

**Summary**, from NCBI Gene [114897](https://www.ncbi.nlm.nih.gov/gene/114897):

> Enables collagen binding activity. Involved in several processes, including negative regulation of platelet aggregation; positive regulation of aldosterone secretion; and positive regulation of cytosolic calcium ion concentration. Located in obsolete extracellular space and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14324](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14324) · Entrez [114897](https://www.ncbi.nlm.nih.gov/gene/114897) · UniProt [Q9BXJ1](https://www.uniprot.org/uniprotkb/Q9BXJ1) · Ensembl [ENSG00000173918](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173918)

## Data

Gene col 10445: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10445); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10445, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10445]; `tensor/DDL_lfc|DDL_z.npy` [10445]; `embed/gene_vectors.npy` [10445]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10445 or target_col == 10445). Every well: [[C1QTNF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1QTNF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
