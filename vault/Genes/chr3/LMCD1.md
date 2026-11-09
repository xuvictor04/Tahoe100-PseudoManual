---
symbol: "LMCD1"
type: "gene"
col: 983
ensembl_id: "ENSG00000071282"
name: "LIM and cysteine rich domains 1"
location: "3p25.3"
module: 15
arm: "-"
pooled_cpm: 31.87
n_lines_expressing: 39
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# LMCD1

*LIM and cysteine rich domains 1* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 6.12× (z +21.5, q 0e+00, up in 33 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.552× (z -10.0, q 9e-21, down in 27 of 35 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUFT1]] (+0.66, fdr 7e-06), [[NEDD9]] (+0.65, fdr 1e-05), [[LIMA1]] (+0.60, fdr 1e-05); moves opposite to [[PPP1R26-AS1]] (-0.58, fdr 3e-05), [[GPALPP1]] (-0.56, fdr 2e-04), [[VPS13B-DT]] (-0.56, fdr 8e-05).
> It sits in the **-** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[ARL4A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 983.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **6.12×** | +21.5 | 0e+00 | 33/37 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **5.67×** | +20.5 | 0e+00 | 33/37 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.08×** | +16.6 | 0e+00 | 31/36 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.45×** | +15.0 | 0e+00 | 32/37 (A498, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.44×** | +10.5 | 7e-24 | 28/37 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.38×** | +10.2 | 1e-22 | 29/36 (NCI-H2347, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.57×** | +5.8 | 4e-07 | 21/37 (A549, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.43×** | +4.5 | 6e-04 | 16/37 (NCI-H460, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.30×** | +4.3 | 9e-04 | 17/36 (NCI-H1792, NCI-H2347, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +4.1 | 0.002 | 17/36 (NCI-H1792, A549, …) | top dose only | cell-cycle shift (explains ~19% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.011 | 12/37 (HepG2/C3A, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.021 | 10/37 (Hs 766T, HepG2/C3A, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.058 | 11/37 (HepG2/C3A, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.2 | 0.058 | 7/30 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 983.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.552×** | -10.0 | 9e-21 | 27/35 (HepG2/C3A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.615×** | -5.6 | 7e-06 | 24/37 (SNU-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.722×** | -5.5 | 7e-06 | 21/37 (C32, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.642×** | -5.3 | 2e-05 | 20/33 (HS-578T, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.652×** | -5.1 | 4e-05 | 20/36 (A549, SW1417, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.655×** | -5.0 | 4e-05 | 19/35 (HepG2/C3A, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -4.1 | 0.003 | 18/35 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.735×** | -3.7 | 0.017 | 14/37 (HepG2/C3A, C32, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.817×** | -3.4 | 0.040 | 15/37 (RPMI-7951, SW480, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.823×** | -3.3 | 0.054 | 11/37 (SW 900, SW 1271, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.05 µM |  | 0.759× | -3.1 | 0.11 | 13/36 (KATO III, BT-474, …) | all doses, flat |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.777× | -3.0 | 0.11 | 15/36 (AsPC-1, SW480, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.777× | -3.0 | 0.11 | 11/36 (NCI-H2030, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 983. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 73.9 | 10 (2 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 3.15× (z +12.2) | — |
| [[HepG2_C3A (line)]] | wt | 278 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0812× (z -17.6) |
| [[C32 (line)]] | wt | 95.5 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0362× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -12.5) |
| [[A498 (line)]] | wt | 16.8 | 5 | 1 | [[Panobinostat (drug)]] 0.5 µM 6.83× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 25.5 | 6 | 0 | [[Dexamethasone (drug)]] 5 µM 15.0× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 18.1 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.90× (z +13.1) | — |
| [[NCI-H460 (line)]] | wt | 17.4 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 14.9× (z +15.6) | — |
| [[HEC-1-A (line)]] | alt | 31.3 | 1 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.48× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -12.8) |
| [[J82 (line)]] | alt | 10.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 16.3× (z +14.4) | — |
| [[NCI-H1792 (line)]] | alt | 14.3 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 11.3× (z +11.9) | — |
| [[SNU-1 (line)]] | wt | 146 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0622× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -14.2) |
| [[A549 (line)]] | wt | 44.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.31× (z +11.1) | — |
| [[H4 (line)]] | wt | 8.19 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 36.3× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 12.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 19.4× (z +12.1) | — |
| [[KATO III (line)]] | alt | 39.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 12.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.2× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 36.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.94× (z +12.9) | — |
| [[RPMI-7951 (line)]] | alt | 25.7 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.75× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0625× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 13.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 14.4× (z +11.5) | — |
| [[SW1417 (line)]] | alt | 25.9 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.34× (z +10.2) | — |
| [[A-427 (line)]] | wt | 11.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.05× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 14.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.66× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 54.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -10.3) |
| [[SW 900 (line)]] | alt | 81.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 111 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -10.7) |
| [[LS 180 (line)]] | wt | 9.38 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.80× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 36.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -8.9) |
| [[A-172 (line)]] | wt | 4.18 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.31 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.88 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.68 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.10 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.47 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.89 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.83 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.93 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.71 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 87.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 983), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUFT1]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[NEDD9]] | +0.65 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[LIMA1]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 | same gene group |
| [[SPATA13]] | +0.59 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[EZR]] | +0.57 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[MYO1E]] | +0.57 | +0.38 / +0.45 | both halves | 7e-05 |  |
| [[KLF2]] | +0.57 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[RHOB]] | +0.56 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[MAN1A1]] | +0.56 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[VCL]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[TRIB1]] | +0.54 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[JUN]] | +0.54 | +0.46 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R26-AS1]] | -0.58 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[GPALPP1]] | -0.56 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[VPS13B-DT]] | -0.56 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[TSTD3]] | -0.55 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[URM1]] | -0.54 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[SLC12A9]] | -0.53 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[PTPN9]] | -0.53 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[TMEM68]] | -0.52 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[SAP30L-AS1]] | -0.52 | -0.32 / -0.35 | both halves | 1e-04 |  |
| [[GOT1-DT]] | -0.51 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[ANXA2R-OT1]] | -0.51 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[PNISR-AS1]] | -0.51 | -0.19 / -0.48 | ⚠ not reproduced | 9e-04 |  |
| [[ANGEL2]] | -0.50 | -0.36 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises LMCD1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CA8]] | B | CA8 activity raises LMCD1's level | lines that do not express CA8 (27) vs lines expressing it (23) | 1.47× lower at baseline in the lines without CA8 | 0.078 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[BAMBI]] | B | BAMBI activity raises LMCD1's level | lines that do not express BAMBI (16) vs lines expressing it (34) | 1.81× lower at baseline in the lines without BAMBI | 0.080 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, ACKR3, CADPS2; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARL4A]] | B | LMCD1 activity raises ARL4A's level | lines that do not express LMCD1 (11) vs lines expressing it (39) | 1.47× lower at baseline in the lines without LMCD1 | 0.013 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SEC24B-AS1]] | B | LMCD1 activity lowers SEC24B-AS1's level | lines that do not express LMCD1 (11) vs lines expressing it (39) | 1.40× higher at baseline in the lines without LMCD1 | 0.075 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[IFFO2]] | B | LMCD1 activity raises IFFO2's level | lines that do not express LMCD1 (11) vs lines expressing it (39) | 1.48× lower at baseline in the lines without LMCD1 | 0.076 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CA8]] | B | LMCD1 activity raises CA8's level | lines that do not express LMCD1 (11) vs lines expressing it (39) | 2.53× lower at baseline in the lines without LMCD1 | 0.077 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[POLR1HASP]] | B | LMCD1 activity lowers POLR1HASP's level | lines that do not express LMCD1 (11) vs lines expressing it (39) | 1.40× higher at baseline in the lines without LMCD1 | 0.092 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **-** arm (projection on the module's main direction -0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (29.8, 8.3); signed map (1.5, 23.6). **Vector** length 106, 25.0% of its response variance represented; |z| ≥ 3 in 1,134 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +15.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.0 | +10.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +20.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +21.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +10.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.2 | +4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +5.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -10.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -4.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.3 | -5.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.1 | -3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.3 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | LIM and cysteine rich domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:8,501,807-8,574,668 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | LIM domain containing |
| Reactome | 1 pathways, smallest: Surfactant metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZU5](https://www.uniprot.org/uniprotkb/Q9NZU5) (LIM and cysteine-rich domains protein 1):

> Transcriptional cofactor that restricts GATA6 function by inhibiting DNA-binding, resulting in repression of GATA6 transcriptional activation of downstream target genes. Represses GATA6-mediated trans activation of lung- and cardiac tissue-specific promoters. Inhibits DNA-binding by GATA4 and GATA1 to the cTNC promoter (By similarity). Plays a critical role in the development of cardiac hypertrophy via activation of calcineurin/nuclear factor of activated T-cells signaling pathway.

**Summary**, from NCBI Gene [29995](https://www.ncbi.nlm.nih.gov/gene/29995):

> This gene encodes a member of the LIM-domain family of zinc finger proteins. The encoded protein contains an N-terminal cysteine-rich domain and two C-terminal LIM domains. The presence of LIM domains suggests involvement in protein-protein interactions. The protein may act as a co-regulator of transcription along with other transcription factors. Alternate splicing results in multiple transcript variants of this gene. [provided by RefSeq, May 2013]

**Accessions** — [HGNC:6633](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6633) · Entrez [29995](https://www.ncbi.nlm.nih.gov/gene/29995) · UniProt [Q9NZU5](https://www.uniprot.org/uniprotkb/Q9NZU5) · Ensembl [ENSG00000071282](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071282)

## Data

Gene col 983: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 983); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 983, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 983]; `tensor/DDL_lfc|DDL_z.npy` [983]; `embed/gene_vectors.npy` [983]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 983 or target_col == 983). Every well: [[LMCD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMCD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
