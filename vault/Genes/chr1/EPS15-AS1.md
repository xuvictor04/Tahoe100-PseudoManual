---
symbol: "EPS15-AS1"
type: "gene"
col: 13572
ensembl_id: "ENSG00000227070"
name: "EPS15 antisense RNA 1"
location: "1p32.3"
module: 35
arm: "+"
pooled_cpm: 6.52
n_lines_expressing: 38
n_dd_up: 19
n_dd_down: 12
n_dd_up_clean: 17
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# EPS15-AS1

*EPS15 antisense RNA 1* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 10.1× (z +31.2, q 0e+00, up in 26 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.398× (z -8.8, q 9e-16, down in 23 of 33 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.415× (z -4.4, q 0.001, down in 14 of 26 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NINJ2]] (+0.68, fdr 3e-04), [[MMADHC-DT]] (+0.67, fdr 3e-04), [[ANXA2R-AS1]] (+0.66, fdr 5e-05); moves opposite to [[ARRB2]] (-0.62, fdr 2e-04), [[SH3PXD2B]] (-0.59, fdr 6e-05), [[ZNF445]] (-0.59, fdr 2e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[IMPDH2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13572.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **10.1×** | +31.2 | 0e+00 | 26/27 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.81×** | +16.2 | 0e+00 | 18/23 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **5.21×** | +15.2 | 0e+00 | 24/29 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.40×** | +11.9 | 3e-30 | 11/28 (HEC-1-A, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.33×** | +11.5 | 3e-28 | 17/32 (HEC-1-A, Panc 03.27, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.43×** | +8.2 | 3e-14 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.93×** | +6.3 | 2e-08 | 16/31 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +5.3 | 7e-06 | 12/27 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.63×** | +4.5 | 4e-04 | 13/30 (COLO 205, SW48, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.54×** | +4.2 | 0.002 | 9/31 (SW480, LS 180, …) | rises with dose | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.53×** | +4.1 | 0.002 | 9/30 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.51×** | +4.0 | 0.004 | 8/32 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.007 | 6/32 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.5 | 0.020 | 3/21 (HEC-1-A, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.65×** | +3.4 | 0.025 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.42×** | +3.4 | 0.027 | 7/31 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.036 | 2/22 (SW480, LOX-IMVI) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13572.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.398×** | -8.8 | 9e-16 | 23/33 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.453×** | -7.5 | 1e-11 | 19/33 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.542×** | -5.8 | 1e-06 | 18/32 (HT-29, KATO III, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.620×** | -4.6 | 7e-04 | 22/32 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.415×** | -4.4 | 0.001 | 14/26 (HT-29, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.459×** | -3.9 | 0.010 | 11/28 (MIA PaCa-2, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.614×** | -3.3 | 0.060 | 11/33 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.515×** | -3.3 | 0.060 | 13/26 (LoVo, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.709×** | -3.3 | 0.060 | 9/32 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.518×** | -3.3 | 0.060 | 13/22 (HT-29, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.712×** | -3.2 | 0.063 | 7/31 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.710×** | -3.1 | 0.097 | 7/31 (A549, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13572. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 33.3 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0683× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.303× (z -10.2) |
| [[SW480 (line)]] | alt | 6.00 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.128× (z -11.1) ⚠ cell-cycle shift, explains ~58% of this change |
| [[COLO 205 (line)]] | alt | 26.1 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0776× (z -13.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[LS 180 (line)]] | wt | 22.1 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -11.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 31.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.134× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 5.75 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.43× (z +12.7) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0886× (z -10.1) |
| [[KATO III (line)]] | alt | 17.4 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.151× (z -10.3) ⚠ cell-cycle shift, explains ~48% of this change |
| [[LoVo (line)]] | wt | 19.6 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.125× (z -12.7) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 6.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.85× (z +12.2) | — |
| [[A549 (line)]] | wt | 2.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.9× (z +8.8) | — |
| [[C32 (line)]] | wt | 2.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.6× (z +10.4) | — |
| [[HCT15 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -9.4) ⚠ cell-cycle shift, explains ~41% of this change |
| [[HS-578T (line)]] | alt | 1.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.5× (z +8.8) | — |
| [[J82 (line)]] | alt | 2.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.77× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 1.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 8.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 2.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +13.1) | — |
| [[SW1417 (line)]] | alt | 4.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.54× (z +9.5) | — |
| [[A-172 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.696 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.915 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13572), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NINJ2]] | +0.68 | +0.75 / +0.27 | both halves | 3e-04 |  |
| [[MMADHC-DT]] | +0.67 | +0.71 / +0.27 | both halves | 3e-04 |  |
| [[ANXA2R-AS1]] | +0.66 | +0.70 / +0.39 | both halves | 5e-05 | same gene group |
| [[NEK8]] | +0.65 | +0.68 / +0.34 | both halves | 1e-04 |  |
| [[PPP1R12A-AS2]] | +0.65 | +0.63 / +0.33 | both halves | 1e-04 | same gene group |
| [[ASH1L]] | +0.65 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[KLF3-AS1]] | +0.64 | +0.52 / +0.43 | both halves | 3e-05 | same gene group |
| [[FAM174B]] | +0.64 | +0.57 / +0.38 | both halves | 7e-05 |  |
| [[PRKCH-AS1]] | +0.63 | +0.60 / +0.53 | both halves | 1e-05 | same gene group |
| [[TFAP2A-AS1]] | +0.63 | +0.68 / +0.30 | both halves | 2e-04 | same gene group |
| [[EFCAB5]] | +0.63 | +0.70 / +0.22 | both halves | 6e-04 |  |
| [[MED13]] | +0.62 | +0.51 / +0.27 | both halves | 3e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARRB2]] | -0.62 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[SH3PXD2B]] | -0.59 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[ZNF445]] | -0.59 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[HACE1]] | -0.58 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[FBXW2]] | -0.58 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[RIMS3]] | -0.58 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[FAM234B]] | -0.57 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[SEMA4F]] | -0.57 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[NDRG3]] | -0.57 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[NBPF3]] | -0.57 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[YIF1B]] | -0.56 | -0.62 / -0.04 | ⚠ one half (not replicated) | 0.005 |  |
| [[STARD3NL]] | -0.56 | -0.52 / -0.37 | both halves | 7e-05 |  |
| [[POT1]] | -0.56 | -0.50 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EPS15-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GRHL2]] | B | GRHL2 activity raises EPS15-AS1's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 3.18× lower at baseline in the lines without GRHL2 | 0.036 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[BTC]] | B | BTC activity raises EPS15-AS1's level | lines that do not express BTC (20) vs lines expressing it (30) | 2.09× lower at baseline in the lines without BTC | 0.073 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |
| [[BANK1]] | B | BANK1 activity raises EPS15-AS1's level | lines that do not express BANK1 (12) vs lines expressing it (38) | 1.71× lower at baseline in the lines without BANK1 | 0.084 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IMPDH2]] | B | EPS15-AS1 activity lowers IMPDH2's level | lines that do not express EPS15-AS1 (12) vs lines expressing it (38) | 1.29× higher at baseline in the lines without EPS15-AS1 | 0.050 | ⚠ within organs, on part of the lines; also absent: RND1; maybe low, not absent |
| [[MLX]] | B | EPS15-AS1 activity lowers MLX's level | lines that do not express EPS15-AS1 (12) vs lines expressing it (38) | 1.24× higher at baseline in the lines without EPS15-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: RND1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.595). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (9.1, 14.2); signed map (24.0, -6.7). **Vector** length 79.4, 17.8% of its response variance represented; |z| ≥ 3 in 932 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +31.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +16.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +15.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +11.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +11.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.5 | +2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.5 | +2.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -4.5 | -4.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -8.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -4.0 | -7.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -3.9 | -5.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -3.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.3 | -4.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.1 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | EPS15 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p32.3 — chr1:51,518,288-51,561,651 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40219](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40219) · Entrez [105378720](https://www.ncbi.nlm.nih.gov/gene/105378720) · Ensembl [ENSG00000227070](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227070)

## Data

Gene col 13572: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13572); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13572, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13572]; `tensor/DDL_lfc|DDL_z.npy` [13572]; `embed/gene_vectors.npy` [13572]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13572 or target_col == 13572). Every well: [[EPS15-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPS15-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
