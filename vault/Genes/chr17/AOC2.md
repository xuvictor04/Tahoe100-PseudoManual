---
symbol: "AOC2"
type: "gene"
col: 5217
ensembl_id: "ENSG00000131480"
name: "amine oxidase copper containing 2"
location: "17q21.31"
module: 37
arm: "+"
pooled_cpm: 3.08
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 5
n_dd_up_clean: 19
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# AOC2

*amine oxidase copper containing 2* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.63× (z +21.3, q 0e+00, up in 35 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM: 0.609× (z -4.4, q 0.006, down in 8 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYH3]] (+0.65, fdr 1e-05), [[GLIPR1-AS1]] (+0.64, fdr 4e-05), [[SLC9A5]] (+0.63, fdr 1e-05); moves opposite to [[TMEM14A]] (-0.58, fdr 4e-05), [[TTC3P1]] (-0.57, fdr 2e-04), [[BBS5]] (-0.57, fdr 5e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5217.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.63×** | +21.3 | 0e+00 | 35/35 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.35×** | +18.1 | 0e+00 | 32/36 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.80×** | +10.9 | 2e-25 | 29/34 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **3.09×** | +9.8 | 1e-20 | 38/46 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **3.31×** | +9.7 | 5e-20 | 29/43 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **3.28×** | +9.6 | 8e-20 | 12/17 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.15×** | +9.3 | 2e-18 | 21/31 (NCI-H460, SW480, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.75×** | +8.8 | 8e-17 | 30/44 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.82×** | +8.3 | 4e-15 | 27/36 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.42×** | +7.7 | 9e-13 | 29/47 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.41×** | +7.6 | 1e-12 | 29/45 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.23×** | +6.2 | 3e-08 | 13/48 (A-427, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.02×** | +6.1 | 4e-08 | 19/42 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.86×** | +5.4 | 3e-06 | 17/43 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +5.3 | 3e-06 | 9/27 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.2 | 8e-06 | 10/45 (A-172, NCI-H2347, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +5.2 | 8e-06 | 17/44 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +4.7 | 7e-05 | 16/43 (HEC-1-A, NCI-H460, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.66×** | +4.4 | 3e-04 | 10/40 (A-427, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +4.2 | 7e-04 | 6/46 (HS-578T, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.005 | 5/45 (NCI-H460, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.57×** | +3.7 | 0.005 | 5/42 (HEC-1-A, SW1417, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5217.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM |  | **0.609×** | -4.4 | 0.006 | 8/45 (COLO 205, H4, …) | all doses, flat | position effect removed |
| [[Sodium Salicylate (drug)]] 5 µM |  | **0.727×** | -4.0 | 0.016 | 13/45 (Panc 03.27, C-33 A, …) | rises with dose | position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.646×** | -3.9 | 0.019 | 9/46 (CHP-212, SW 1271, …) | all doses, flat | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.748×** | -3.7 | 0.034 | 11/43 (HT-29, SK-MEL-2, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.480×** | -3.4 | 0.079 | 2/18 (HEC-1-A, SW480) | top dose only | noisy plate (z scaled); position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 5 µM |  | 0.702× | -3.2 | 0.15 | 6/46 (CHP-212, CFPAC-1, …) | all doses, flat | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | 0.690× | -3.1 | 0.18 | 12/42 (LoVo, NCI-H1573, …) | top dose only | position effect removed |
| [[Busulfan (drug)]] 0.05 µM |  | 0.714× | -3.0 | 0.19 | 10/43 (Panc 03.27, SW480, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.77 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5217. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.64 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.53× (z +10.6) | — |
| [[SW480 (line)]] | alt | 3.89 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +9.0) | — |
| [[A-172 (line)]] | wt | 2.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +8.9) | — |
| [[A498 (line)]] | wt | 4.89 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +9.0) | — |
| [[A549 (line)]] | wt | 2.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 2.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.74× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 2.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.26× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 3.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.11× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 3.07 | 0 | 1 | — | [[Levobupivacaine (hydrochloride) (drug)]] 0.05 µM 0.0615× (z -8.5) |
| [[PANC-1 (line)]] | alt | 1.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.03× (z +10.2) | — |
| [[A-427 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.960 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5217), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYH3]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[GLIPR1-AS1]] | +0.64 | +0.69 / +0.41 | both halves | 4e-05 |  |
| [[SLC9A5]] | +0.63 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[CCDC17]] | +0.61 | +0.72 / +0.36 | both halves | 1e-04 |  |
| [[SMIM15-AS1]] | +0.61 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[UBAP1L]] | +0.61 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[TMED6]] | +0.61 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[OVGP1]] | +0.60 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[CFAP53]] | +0.60 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[LINC02936]] | +0.60 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[TG]] | +0.60 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[PPP1R3F]] | +0.59 | +0.63 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM14A]] | -0.58 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[TTC3P1]] | -0.57 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[BBS5]] | -0.57 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[ACACB]] | -0.56 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[CAT]] | -0.56 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[PAFAH1B3]] | -0.56 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[HPF1]] | -0.55 | -0.28 / -0.37 | both halves | 3e-04 |  |
| [[PKIG]] | -0.54 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[MNAT1]] | -0.54 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[FRG1CP]] | -0.54 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[LPCAT2]] | -0.54 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[FAM13B]] | -0.53 | -0.54 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AOC2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.505). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.1, -14.6); signed map (14.3, 3.7). **Vector** length 57.7, 8.06% of its response variance represented; |z| ≥ 3 in 1,239 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +21.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | +3.4 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | +18.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.8 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +4.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +3.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -3.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -1.7 | +7.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.4 |
|  | [[AZD-8055 (drug)]] 5 µM |  | -1.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | amine oxidase copper containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:42,844,580-42,850,707 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAO, DAO2 |
| Gene groups (HGNC) | Amine oxidase copper containing family |
| Reactome | 2 pathways, smallest: Phase I - Functionalization of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [O75106](https://www.uniprot.org/uniprotkb/O75106) (Amine oxidase):

> Catalyzes the oxidative deamination of primary amines to the corresponding aldehydes with the concomitant production of hydrogen peroxide and ammonia. Has a preference for 2-phenylethylamine, tryptamine and tyramine. Could also act on methylamine and benzylamine but much less efficiently.

**Summary**, from NCBI Gene [314](https://www.ncbi.nlm.nih.gov/gene/314):

> Copper amine oxidases catalyze the oxidative conversion of amines to aldehydes and ammonia in the presence of copper and quinone cofactor. This gene shows high sequence similarity to copper amine oxidases from various species ranging from bacteria to mammals. The protein contains several conserved motifs including the active site of amine oxidases and the histidine residues that likely bind copper. It may be a critical modulator of signal transmission in retina, possibly by degrading the …

**Accessions** — [HGNC:549](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:549) · Entrez [314](https://www.ncbi.nlm.nih.gov/gene/314) · UniProt [O75106](https://www.uniprot.org/uniprotkb/O75106) · Ensembl [ENSG00000131480](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131480)

## Data

Gene col 5217: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5217); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5217, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5217]; `tensor/DDL_lfc|DDL_z.npy` [5217]; `embed/gene_vectors.npy` [5217]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5217 or target_col == 5217). Every well: [[AOC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AOC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
