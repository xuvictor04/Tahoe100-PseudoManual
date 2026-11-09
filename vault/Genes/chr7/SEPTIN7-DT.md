---
symbol: "SEPTIN7-DT"
type: "gene"
col: 13680
ensembl_id: "ENSG00000228878"
name: "SEPTIN7 divergent transcript"
location: "7p14.2"
module: 23
arm: "+"
pooled_cpm: 4.06
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 15
n_dd_up_clean: 18
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# SEPTIN7-DT

*SEPTIN7 divergent transcript* — 7p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.36× (z +29.3, q 0e+00, up in 38 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.523× (z -6.7, q 1e-08, down in 21 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC37A3]] (+0.90, fdr 7e-06), [[TMEM202-AS1]] (+0.89, fdr 7e-06), [[OXA1L-DT]] (+0.85, fdr 1e-05); moves opposite to [[FAM118A]] (-0.71, fdr 2e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PYROXD2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13680.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.36×** | +29.3 | 0e+00 | 38/38 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.33×** | +21.5 | 0e+00 | 32/37 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.98×** | +11.3 | 2e-27 | 30/37 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.83×** | +10.4 | 5e-23 | 24/35 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.90×** | +10.2 | 2e-22 | 8/9 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +7.6 | 4e-12 | 24/37 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.66×** | +7.5 | 6e-12 | 16/47 (A-172, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +6.7 | 1e-09 | 10/24 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.77×** | +5.9 | 2e-07 | 16/45 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +5.4 | 3e-06 | 1/5 (A498) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.69×** | +5.4 | 3e-06 | 16/42 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.60×** | +4.9 | 5e-05 | 9/47 (C32, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +4.4 | 5e-04 | 14/45 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.29×** | +3.7 | 0.008 | 8/46 (PANC-1, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +3.7 | 0.008 | 8/42 (NCI-H1573, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.013 | 7/45 (H4, LS 180, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.44×** | +3.5 | 0.015 | 5/30 (NCI-H460, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.027 | 13/42 (LoVo, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belzutifan (drug)]] 5 µM |  | **1.83×** | +3.3 | 0.030 | 1/24 (HEC-1-A) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13680.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.523×** | -6.7 | 1e-08 | 21/46 (PANC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.548×** | -5.9 | 1e-06 | 16/43 (HEC-1-A, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.577×** | -5.7 | 3e-06 | 18/45 (NCI-H1792, C32, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.581×** | -5.6 | 3e-06 | 20/33 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.591×** | -5.4 | 7e-06 | 20/43 (PANC-1, RPMI-7951, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.627×** | -4.8 | 1e-04 | 18/42 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.630×** | -4.8 | 2e-04 | 12/46 (HS-578T, AN3 CA, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.638×** | -4.6 | 2e-04 | 18/46 (HOP62, PANC-1, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.628×** | -4.6 | 2e-04 | 14/27 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.649×** | -4.4 | 5e-04 | 21/45 (PANC-1, A-172, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.686×** | -3.9 | 0.005 | 8/45 (SW48, SNU-423, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.688×** | -3.9 | 0.005 | 9/47 (A-172, PANC-1, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.692×** | -3.8 | 0.006 | 8/46 (PANC-1, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.702×** | -3.7 | 0.010 | 10/46 (C32, AN3 CA, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.560×** | -3.1 | 0.066 | 6/14 (NCI-H460, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13680. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.22 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +14.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0637× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[PANC-1 (line)]] | alt | 6.32 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.55× (z +15.4) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.145× (z -10.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.180× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 4.67 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.00× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.0453× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Furosemide (drug)]] 0.5 µM 0.0610× (z -9.5) |
| [[C32 (line)]] | wt | 10.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +10.2) | — |
| [[HOP62 (line)]] | alt | 4.15 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.86× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 3.19 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.4× (z +11.7) | — |
| [[LoVo (line)]] | wt | 3.09 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.7× (z +14.6) | — |
| [[LOX-IMVI (line)]] | wt | 4.86 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +14.1) | — |
| [[NCI-H23 (line)]] | alt | 7.72 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +13.8) | — |
| [[A-172 (line)]] | wt | 8.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.53× (z +13.7) | — |
| [[A498 (line)]] | wt | 2.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.6× (z +14.6) | — |
| [[AsPC-1 (line)]] | alt | 1.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 58.2× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 10.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0620× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 8.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 2.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.8× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 1.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.6× (z +8.9) | — |
| [[J82 (line)]] | alt | 2.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.33× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 4.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.70× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 3.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.28× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 5.79 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +11.8) | — |
| [[NCI-H2347 (line)]] | alt | 2.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.12× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 2.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.9× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 5.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.60× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 8.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +15.6) | — |
| [[SNU-423 (line)]] | alt | 2.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 2.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.3× (z +11.0) | — |
| [[SW480 (line)]] | alt | 2.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +9.6) | — |
| [[A-427 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13680), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC37A3]] | +0.90 | +0.88 / +0.66 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.89 | +0.89 / +0.65 | both halves | 7e-06 |  |
| [[OXA1L-DT]] | +0.85 | +0.85 / +0.53 | both halves | 1e-05 | same gene group |
| [[INTS6-AS1]] | +0.85 | +0.85 / +0.65 | both halves | 7e-06 |  |
| [[F8]] | +0.84 | +0.87 / +0.56 | both halves | 1e-05 |  |
| [[ATE1OSP]] | +0.84 | +0.84 / +0.52 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.83 | +0.83 / +0.45 | both halves | 3e-05 |  |
| [[PPP1R3F]] | +0.83 | +0.81 / +0.58 | both halves | 7e-06 |  |
| [[THAP2]] | +0.83 | +0.85 / +0.46 | both halves | 3e-05 |  |
| [[PCNX4-DT]] | +0.82 | +0.85 / +0.48 | both halves | 2e-05 | same gene group |
| [[MAD2L1-DT]] | +0.81 | +0.81 / +0.49 | both halves | 1e-05 | same gene group |
| [[CHD1-DT]] | +0.81 | +0.80 / +0.50 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM118A]] | -0.71 | -0.67 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PYROXD2]] | B | PYROXD2 activity lowers SEPTIN7-DT's level | lines that do not express PYROXD2 (7) vs lines expressing it (43) | 1.57× higher at baseline in the lines without PYROXD2 | 0.021 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SEPTIN7-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ST8SIA5]] | B | ST8SIA5 activity raises SEPTIN7-DT's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without ST8SIA5 | 0.091 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[HECTD2]] | B | HECTD2 activity raises SEPTIN7-DT's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 2.13× lower at baseline in the lines without HECTD2 | 0.098 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[FBXO38-DT]] | C | FBXO38-DT activity raises SEPTIN7-DT's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 1.62× lower at baseline in the lines without FBXO38-DT | 0.075 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.856). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (6.2, 15.9); signed map (26.8, -9.0). **Vector** length 82.9, 15.4% of its response variance represented; |z| ≥ 3 in 1,161 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +29.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.9 | +21.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.9 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +10.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +5.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +5.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -5.9 | -4.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.6 | -5.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -4.9 | -3.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.8 | -6.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -4.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | SEPTIN7 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7p14.2 — chr7:35,751,856-35,800,949 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously SEPT7-AS1, SEPTIN7-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51153](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51153) · Entrez [101928545](https://www.ncbi.nlm.nih.gov/gene/101928545) · Ensembl [ENSG00000228878](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228878)

## Data

Gene col 13680: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13680); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13680, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13680]; `tensor/DDL_lfc|DDL_z.npy` [13680]; `embed/gene_vectors.npy` [13680]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13680 or target_col == 13680). Every well: [[SEPTIN7-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEPTIN7-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
