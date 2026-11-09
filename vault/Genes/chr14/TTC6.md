---
symbol: "TTC6"
type: "gene"
col: 6351
ensembl_id: "ENSG00000139865"
name: "tetratricopeptide repeat domain 6"
location: "14q21.1"
module: 68
arm: "+"
pooled_cpm: 16.46
n_lines_expressing: 35
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 10
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# TTC6

*tetratricopeptide repeat domain 6* — 14q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.15× (z +16.9, q 0e+00, up in 26 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.474× (z -7.8, q 3e-12, down in 26 of 33 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02542]] (+0.76, fdr 1e-05), [[FOXA1]] (+0.74, fdr 7e-06, ⚠ same locus), [[RIPK2-DT]] (+0.74, fdr 7e-06), [[LINC00571]] (+0.72, fdr 4e-05); moves opposite to [[BRAT1]] (-0.69, fdr 1e-05), [[NBPF3]] (-0.67, fdr 4e-05), [[MINK1]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 10 go from it, the strongest it → [[SLC9A6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6351.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.15×** | +16.9 | 0e+00 | 26/29 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.12×** | +16.7 | 0e+00 | 25/29 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.60×** | +9.9 | 5e-21 | 23/28 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.63×** | +9.3 | 2e-18 | 10/20 (LoVo, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +7.9 | 4e-13 | 7/17 (LOX-IMVI, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.90×** | +6.7 | 2e-09 | 17/32 (HOP62, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +5.9 | 3e-07 | 12/25 (SW48, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +5.4 | 4e-06 | 18/31 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.70×** | +5.3 | 6e-06 | 15/31 (RKO, HepG2/C3A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.4 | 7e-04 | 16/29 (HOP62, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.35×** | +4.2 | 0.001 | 16/33 (CFPAC-1, HepG2/C3A, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.1 | 0.002 | 10/31 (LS 180, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.005 | 10/31 (LoVo, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.009 | 7/33 (HOP62, J82, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.40×** | +3.5 | 0.019 | 15/31 (HepG2/C3A, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6351.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.474×** | -7.8 | 3e-12 | 26/33 (HT-29, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.476×** | -7.8 | 3e-12 | 23/32 (NCI-H1792, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.590×** | -5.5 | 7e-06 | 20/33 (HT-29, SHP-77, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.668×** | -4.2 | 0.003 | 19/30 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.486×** | -3.9 | 0.009 | 15/31 (RKO, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.709×** | -3.6 | 0.030 | 20/30 (LS 180, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.698×** | -3.5 | 0.035 | 13/33 (NCI-H2347, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.543×** | -3.3 | 0.053 | 13/28 (SW 900, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.729×** | -3.3 | 0.053 | 12/33 (NCI-H2030, NCI-H1792, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.731×** | -3.3 | 0.053 | 13/31 (NCI-H1573, HCT15, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.731×** | -3.3 | 0.053 | 14/33 (BT-474, NCI-H2030, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.746×** | -3.1 | 0.096 | 11/32 (BT-474, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.738×** | -3.1 | 0.096 | 8/32 (BT-474, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6351. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 43.4 | 1 | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.0685× (z -16.6) |
| [[NCI-H460 (line)]] | wt | 40.0 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +22.3) | [[Belinostat (drug)]] 5 µM 0.233× (z -9.6) |
| [[SW48 (line)]] | wt | 18.9 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +13.9) | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0745× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 43.3 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +14.0) | [[Digitoxin (drug)]] 5 µM 0.270× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.283× (z -9.2) |
| [[HOP62 (line)]] | alt | 6.16 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.4× (z +20.1) | — |
| [[LoVo (line)]] | wt | 8.42 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +19.0) | — |
| [[LS 180 (line)]] | wt | 10.7 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +17.9) | [[Belinostat (drug)]] 0.5 µM 0.114× (z -11.0) |
| [[BT-474 (line)]] | alt | 148 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -11.3) |
| [[HT-29 (line)]] | alt | 28.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -12.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.117× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 37.5 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -8.6) |
| [[SHP-77 (line)]] | alt | 37.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.247× (z -8.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HCT15 (line)]] | alt | 10.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.39× (z +10.8) | — |
| [[HepG2_C3A (line)]] | wt | 36.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.93× (z +16.9) | — |
| [[J82 (line)]] | alt | 6.36 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.1× (z +16.8) | — |
| [[NCI-H2030 (line)]] | alt | 40.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +10.5) | [[Digitoxin (drug)]] 5 µM 0.202× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SW 900 (line)]] | alt | 27.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +8.7) | [[PH-797804 (drug)]] 5 µM 0.0253× (z -9.3) |
| [[C-33 A (line)]] | alt | 21.9 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0730× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.45× (z +13.6) | — |
| [[LOX-IMVI (line)]] | wt | 8.47 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0729× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.110× (z -8.6) |
| [[A-172 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.01 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6351), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 7 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02542]] | +0.76 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[FOXA1]] | +0.74 | +0.81 / +0.64 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[RIPK2-DT]] | +0.74 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[LINC00571]] | +0.72 | +0.71 / +0.42 | both halves | 4e-05 |  |
| [[MMADHC-DT]] | +0.72 | +0.66 / +0.34 | both halves | 1e-04 |  |
| [[NEB]] | +0.70 | +0.71 / +0.32 | both halves | 2e-04 |  |
| [[PATL2]] | +0.70 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[PPP1R12A-AS2]] | +0.69 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[CCDC90B-AS1]] | +0.69 | +0.64 / +0.35 | both halves | 1e-04 |  |
| [[CFAP70]] | +0.69 | +0.69 / +0.40 | both halves | 5e-05 | same gene group |
| [[LINC02889]] | +0.69 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[BTG3-AS1]] | +0.69 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[MZF1-AS1]] | +0.68 | +0.63 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRAT1]] | -0.69 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[NBPF3]] | -0.67 | -0.67 / -0.41 | both halves | 4e-05 |  |
| [[MINK1]] | -0.65 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[LPCAT4]] | -0.64 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[TBC1D2B]] | -0.64 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[MAST3]] | -0.63 | -0.54 / -0.28 | both halves | 3e-04 |  |
| [[PIGF]] | -0.63 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[SDHAF3]] | -0.63 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[AP2S1]] | -0.62 | -0.56 / -0.29 | both halves | 3e-04 |  |
| [[PHKA2]] | -0.62 | -0.58 / -0.33 | both halves | 1e-04 |  |
| [[SLC9A6]] | -0.62 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[ZDHHC9]] | -0.62 | -0.66 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TTC6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLSCR2]] | B | PLSCR2 activity raises TTC6's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 1.78× lower at baseline in the lines without PLSCR2 | 0.046 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers TTC6's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[RBPMS]] | B | RBPMS activity raises TTC6's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without RBPMS | 0.062 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[SLC2A9]] | B | SLC2A9 activity raises TTC6's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 2.58× lower at baseline in the lines without SLC2A9 | 0.093 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[FOXA1]] | C | FOXA1 activity raises TTC6's level | lines that do not express FOXA1 (22) vs lines expressing it (28) | 4.20× lower at baseline in the lines without FOXA1 | 0.001 | ⚠ within organs, on part of the lines; also absent: MYO5C, SPINT1, COBL; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC9A6]] | B | TTC6 activity lowers SLC9A6's level | lines that do not express TTC6 (15) vs lines expressing it (35) | 1.17× higher at baseline in the lines without TTC6 | 0.036 | ⚠ within organs, on part of the lines; also absent: SLC27A2, FOXA1, LIMCH1; maybe low, not absent |
| [[MYRFL]] | B | TTC6 activity raises MYRFL's level | lines that do not express TTC6 (15) vs lines expressing it (35) | 2.68× lower at baseline in the lines without TTC6 | 0.037 | ⚠ within organs, on part of the lines; also absent: SLC27A2, FOXA1, LIMCH1; maybe low, not absent |
| [[SLC4A4]] | B | TTC6 activity raises SLC4A4's level | lines that do not express TTC6 (15) vs lines expressing it (35) | 1.64× lower at baseline in the lines without TTC6 | 0.063 | ⚠ within organs, on part of the lines; also absent: SLC27A2, FOXA1, LIMCH1; maybe low, not absent |
| [[ADGRF4]] | B | TTC6 activity raises ADGRF4's level | lines that do not express TTC6 (15) vs lines expressing it (35) | 1.59× lower at baseline in the lines without TTC6 | 0.076 | ⚠ within organs, on part of the lines; also absent: SLC27A2, FOXA1, LIMCH1; maybe low, not absent |
| [[NEK11]] | B | TTC6 activity raises NEK11's level | lines that do not express TTC6 (15) vs lines expressing it (35) | 1.24× lower at baseline in the lines without TTC6 | 0.081 | ⚠ within organs, on part of the lines; also absent: SLC27A2, FOXA1, LIMCH1; maybe low, not absent |
| [[NUP160]] | B | TTC6 activity lowers NUP160's level | lines that do not express TTC6 (15) vs lines expressing it (35) | 1.12× higher at baseline in the lines without TTC6 | 0.083 | ⚠ within organs, on part of the lines; also absent: SLC27A2, FOXA1, LIMCH1; maybe low, not absent |
| [[DUSP16]] | B | TTC6 activity raises DUSP16's level | lines that do not express TTC6 (15) vs lines expressing it (35) | 1.88× lower at baseline in the lines without TTC6 | 0.085 | ⚠ within organs, on part of the lines; also absent: SLC27A2, FOXA1, LIMCH1; maybe low, not absent |
| [[PLSCR2]] | B | TTC6 activity raises PLSCR2's level | lines that do not express TTC6 (15) vs lines expressing it (35) | 1.67× lower at baseline in the lines without TTC6 | 0.088 | ⚠ within organs, on part of the lines; also absent: SLC27A2, FOXA1, LIMCH1; maybe low, not absent |
| [[ACTR5]] | B | TTC6 activity lowers ACTR5's level | lines that do not express TTC6 (15) vs lines expressing it (35) | 1.05× higher at baseline in the lines without TTC6 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC27A2, FOXA1, LIMCH1; maybe low, not absent |
| [[FOXA1]] | C | TTC6 activity raises FOXA1's level | lines that do not express TTC6 (15) vs lines expressing it (35) | 3.54× lower at baseline in the lines without TTC6 | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC27A2, FOXA1, LIMCH1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (14.8, 13.1); signed map (24.0, -6.5). **Vector** length 93.1, 23.1% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.3 | +16.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +9.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +16.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +6.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +5.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +1.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.3 | +3.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.1 | -7.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.9 | -7.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.1 | -5.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.8 | -3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.9 | -3.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.9 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.9 | -1.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.4 | -3.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.1 — chr14:37,595,629-38,041,442 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously NCRNA00291, C14orf25 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q86TZ1](https://www.uniprot.org/uniprotkb/Q86TZ1) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:19739](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19739) · Entrez [319089](https://www.ncbi.nlm.nih.gov/gene/319089) · UniProt [Q86TZ1](https://www.uniprot.org/uniprotkb/Q86TZ1) · Ensembl [ENSG00000139865](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139865)

## Data

Gene col 6351: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6351); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6351, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6351]; `tensor/DDL_lfc|DDL_z.npy` [6351]; `embed/gene_vectors.npy` [6351]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6351 or target_col == 6351). Every well: [[TTC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
