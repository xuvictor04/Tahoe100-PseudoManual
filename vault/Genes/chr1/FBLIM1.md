---
symbol: "FBLIM1"
type: "gene"
col: 8522
ensembl_id: "ENSG00000162458"
name: "filamin binding LIM protein 1"
location: "1p36.21"
module: 31
arm: "+"
pooled_cpm: 16.99
n_lines_expressing: 40
n_dd_up: 2
n_dd_down: 29
n_dd_up_clean: 0
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 13
direction_downstream: 13
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# FBLIM1

*filamin binding LIM protein 1* — 1p36.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.52× (z +6.6, q 2e-08, up in 12 of 23 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HS-578T 4.30×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HS-578T 3.67×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.249× (z -22.7, q 0e+00, down in 37 of 38 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INAVA]] (+0.57, fdr 2e-05), [[DEF6]] (+0.51, fdr 3e-05), [[ADCY4]] (+0.50, fdr 4e-05); moves opposite to [[WDPCP]] (-0.44, fdr 2e-04), [[MTR]] (-0.42, fdr 5e-05), [[USP37]] (-0.42, fdr 5e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[LASTR]] → it (grade B ⚠); 13 go from it, the strongest it → [[ARHGAP27]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8522.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HS-578T 4.30×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HS-578T 3.67×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +6.6 | 2e-08 | 12/23 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +5.8 | 2e-06 | 14/32 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | 1.22× | +3.2 | 0.24 | 13/38 (KATO III, SNU-423, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 1.20× | +3.1 | 0.30 | 2/37 (SW 900, NCI-H1573) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8522.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.249×** | -22.7 | 0e+00 | 37/38 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.257×** | -22.2 | 0e+00 | 38/38 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.420×** | -20.0 | 0e+00 | 32/38 (COLO 205, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.309×** | -19.2 | 0e+00 | 37/38 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.528×** | -14.7 | 0e+00 | 29/36 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.429×** | -13.3 | 2e-38 | 30/38 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.468×** | -12.4 | 2e-33 | 32/38 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.469×** | -12.4 | 3e-33 | 28/37 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.472×** | -12.3 | 8e-33 | 32/38 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.588×** | -8.3 | 5e-15 | 21/38 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.590×** | -8.3 | 6e-15 | 25/37 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.616×** | -7.9 | 1e-13 | 20/36 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.397×** | -7.9 | 1e-13 | 24/38 (KATO III, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.666×** | -6.6 | 1e-09 | 22/38 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.679×** | -6.3 | 1e-08 | 21/37 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.480×** | -6.3 | 1e-08 | 20/38 (SW480, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.488×** | -6.1 | 3e-08 | 19/37 (HOP62, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.752×** | -4.7 | 1e-04 | 15/37 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.746×** | -4.6 | 1e-04 | 12/37 (SW 900, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8522. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.1 | 0 | 15 (6 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -18.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.135× (z -17.1) |
| [[LoVo (line)]] | wt | 22.4 | 0 | 10 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.151× (z -14.1) |
| [[HepG2_C3A (line)]] | wt | 120 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0932× (z -19.0) |
| [[COLO 205 (line)]] | alt | 43.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -17.4) |
| [[LS 180 (line)]] | wt | 42.1 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -18.4) |
| [[A-172 (line)]] | wt | 26.3 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.191× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 39.3 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.138× (z -16.0) |
| [[CFPAC-1 (line)]] | alt | 16.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -12.0) |
| [[HOP62 (line)]] | alt | 24.6 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -15.6) |
| [[HT-29 (line)]] | alt | 9.52 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0926× (z -12.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.180× (z -8.8) |
| [[KATO III (line)]] | alt | 63.8 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0997× (z -22.4) |
| [[MIA PaCa-2 (line)]] | alt | 16.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -15.7) |
| [[HS-578T (line)]] | alt | 35.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.150× (z -13.4) |
| [[J82 (line)]] | alt | 22.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.2) |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 25.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -15.3) |
| [[SHP-77 (line)]] | alt | 8.17 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0486× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 6.72 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0802× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 9.92 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.160× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 7.11 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.189× (z -9.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[Panc 03.27 (line)]] | alt | 6.45 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -8.5) |
| [[SNU-423 (line)]] | alt | 15.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.187× (z -8.9) |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.124× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 9.34 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.231× (z -10.1) |
| [[SW48 (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.141× (z -9.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-427 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.20 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.88 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8522), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INAVA]] | +0.57 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[DEF6]] | +0.51 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[ADCY4]] | +0.50 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[CARD11]] | +0.50 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[LPAR2]] | +0.49 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[TLDC2]] | +0.49 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[TTC9]] | +0.49 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[LPAR5]] | +0.48 | +0.44 / +0.38 | both halves | 7e-05 |  |
| [[IFNLR1]] | +0.48 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[CRYBG2]] | +0.47 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[FUT3]] | +0.47 | +0.40 / +0.29 | both halves | 2e-04 |  |
| [[GMIP]] | +0.46 | +0.41 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDPCP]] | -0.44 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[MTR]] | -0.42 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[USP37]] | -0.42 | -0.23 / -0.41 | both halves | 5e-04 |  |
| [[CFAP210]] | -0.42 | -0.29 / -0.43 | both halves | 3e-04 |  |
| [[WHAMMP1]] | -0.42 | -0.14 / -0.45 | ⚠ not reproduced | 0.002 |  |
| [[CCDC7]] | -0.41 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[CABIN1]] | -0.41 | -0.18 / -0.49 | ⚠ not reproduced | 9e-04 |  |
| [[ALMS1]] | -0.41 | -0.26 / -0.42 | both halves | 3e-04 |  |
| [[UBR5]] | -0.40 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[TDP1]] | -0.40 | -0.21 / -0.40 | both halves | 7e-04 |  |
| [[SSBP2]] | -0.40 | -0.23 / -0.42 | both halves | 5e-04 |  |
| [[CNNM3]] | -0.40 | -0.24 / -0.35 | both halves | 5e-04 |  |
| [[MLLT3]] | -0.39 | -0.24 / -0.40 | both halves | 5e-04 |  |
| [[SIN3A]] | -0.38 | -0.20 / -0.39 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LASTR]] | B | LASTR activity raises FBLIM1's level | lines that do not express LASTR (22) vs lines expressing it (28) | 2.22× lower at baseline in the lines without LASTR | 0.017 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent |
| [[EPHX4]] | B | EPHX4 activity raises FBLIM1's level | lines that do not express EPHX4 (16) vs lines expressing it (34) | 2.20× lower at baseline in the lines without EPHX4 | 0.019 | ⚠ within organs, on part of the lines; also absent: GALNT6, NOD2 |
| [[INAVA]], [[MROH3P]] | B | INAVA, MROH3P activity raises FBLIM1's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 1.74× lower at baseline in the lines without INAVA, MROH3P | 0.023 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[TOP2A]] | B | TOP2A activity raises FBLIM1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EPS8L3]] | B | EPS8L3 activity raises FBLIM1's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 2.23× lower at baseline in the lines without EPS8L3 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[ADCY4]] | B | ADCY4 activity raises FBLIM1's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 1.91× lower at baseline in the lines without ADCY4 | 0.049 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[LPAR5]] | B | LPAR5 activity raises FBLIM1's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 1.69× lower at baseline in the lines without LPAR5 | 0.060 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[MYO7B]] | B | MYO7B activity raises FBLIM1's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 1.80× lower at baseline in the lines without MYO7B | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[LCK]] | B | LCK activity strengthens FBLIM1's drug response | lines that do not express LCK (22) vs lines expressing it (16) | the lines without LCK respond 0.76× as strongly (z diff +1.79); strongest at Homoharringtonine 5 µM: 0.51x vs 0.31x (z diff +4.1) | 0.085 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[LCK]] | B | LCK activity raises FBLIM1's level | lines that do not express LCK (31) vs lines expressing it (19) | 2.06× lower at baseline in the lines without LCK | 0.085 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent |
| [[CDH1]] | B | CDH1 activity raises FBLIM1's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 2.02× lower at baseline in the lines without CDH1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[ACOT11]] | B | ACOT11 activity raises FBLIM1's level | lines that do not express ACOT11 (11) vs lines expressing it (39) | 2.37× lower at baseline in the lines without ACOT11 | 0.088 | ⚠ within organs, on part of the lines; also absent: GALM, GALNT6, MROH7; maybe low, not absent |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP27]] | B | FBLIM1 activity raises ARHGAP27's level | lines that do not express FBLIM1 (10) vs lines expressing it (40) | 2.09× lower at baseline in the lines without FBLIM1 | 0.040 | ⚠ within organs, on part of the lines; also absent: FAM83G, KITLG, DSG2 |
| [[INAVA]] | B | FBLIM1 activity raises INAVA's level | lines that do not express FBLIM1 (10) vs lines expressing it (40) | 2.94× lower at baseline in the lines without FBLIM1 | 0.044 | ⚠ within organs, on part of the lines; also absent: FAM83G, KITLG, DSG2 |
| [[ACOT11]] | B | FBLIM1 activity raises ACOT11's level | lines that do not express FBLIM1 (10) vs lines expressing it (40) | 2.93× lower at baseline in the lines without FBLIM1 | 0.058 | ⚠ within organs, on part of the lines; also absent: FAM83G, KITLG, DSG2 |
| [[MROH3P]] | B | FBLIM1 activity raises MROH3P's level | lines that do not express FBLIM1 (10) vs lines expressing it (40) | 2.51× lower at baseline in the lines without FBLIM1 | 0.060 | ⚠ within organs, on part of the lines; also absent: FAM83G, KITLG, DSG2 |
| [[IFNLR1]] | B | FBLIM1 activity raises IFNLR1's level | lines that do not express FBLIM1 (10) vs lines expressing it (40) | 2.57× lower at baseline in the lines without FBLIM1 | 0.068 | ⚠ within organs, on part of the lines; also absent: FAM83G, KITLG, DSG2 |
| [[ESRP1]] | B | FBLIM1 activity raises ESRP1's level | lines that do not express FBLIM1 (10) vs lines expressing it (40) | 4.26× lower at baseline in the lines without FBLIM1 | 0.074 | ⚠ within organs, on part of the lines; also absent: FAM83G, KITLG, DSG2 |
| [[C1orf116]] | B | FBLIM1 activity raises C1orf116's level | lines that do not express FBLIM1 (10) vs lines expressing it (40) | 3.18× lower at baseline in the lines without FBLIM1 | 0.078 | ⚠ within organs, on part of the lines; also absent: FAM83G, KITLG, DSG2 |
| [[CDH1]] | B | FBLIM1 activity raises CDH1's level | lines that do not express FBLIM1 (10) vs lines expressing it (40) | 4.36× lower at baseline in the lines without FBLIM1 | 0.084 | ⚠ within organs, on part of the lines; also absent: FAM83G, KITLG, DSG2 |
| [[B3GNT3]] | B | FBLIM1 activity raises B3GNT3's level | lines that do not express FBLIM1 (10) vs lines expressing it (40) | 2.71× lower at baseline in the lines without FBLIM1 | 0.090 | ⚠ within organs, on part of the lines; also absent: FAM83G, KITLG, DSG2 |
| [[KDF1]] | B | FBLIM1 activity raises KDF1's level | lines that do not express FBLIM1 (10) vs lines expressing it (40) | 2.17× lower at baseline in the lines without FBLIM1 | 0.091 | ⚠ within organs, on part of the lines; also absent: FAM83G, KITLG, DSG2 |
| [[TLDC2]] | B | FBLIM1 activity raises TLDC2's level | lines that do not express FBLIM1 (10) vs lines expressing it (40) | 1.70× lower at baseline in the lines without FBLIM1 | 0.096 | ⚠ within organs, on part of the lines; also absent: FAM83G, KITLG, DSG2 |
| [[TMC4]] | B | FBLIM1 activity raises TMC4's level | lines that do not express FBLIM1 (10) vs lines expressing it (40) | 2.36× lower at baseline in the lines without FBLIM1 | 0.099 | ⚠ within organs, on part of the lines; also absent: FAM83G, KITLG, DSG2 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.462). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.6, 58.4); signed map (58.1, 11.8). **Vector** length 67.8, 13.0% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.4 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.4 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +0.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.3 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.5 | -6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -3.0 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -2.0 | -2.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -12.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -0.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | filamin binding LIM protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.21 — chr1:15,756,607-15,786,594 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBLP-1, CAL, migfilin |
| Gene groups (HGNC) | LIM domain containing |
| Reactome | 3 pathways, smallest: Cell-extracellular matrix interactions; Cell junction organization; Cell-Cell communication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUP2](https://www.uniprot.org/uniprotkb/Q8WUP2) (Filamin-binding LIM protein 1):

> Serves as an anchoring site for cell-ECM adhesion proteins and filamin-containing actin filaments. Is implicated in cell shape modulation (spreading) and motility. May participate in the regulation of filamin-mediated cross-linking and stabilization of actin filaments. May also regulate the assembly of filamin-containing signaling complexes that control actin assembly. Promotes dissociation of FLNA from ITGB3 and ITGB7. Promotes activation of integrins and regulates integrin-mediated cell-cell …

**Summary**, from NCBI Gene [54751](https://www.ncbi.nlm.nih.gov/gene/54751):

> This gene encodes a protein with an N-terminal filamin-binding domain, a central proline-rich domain, and, multiple C-terminal LIM domains. This protein localizes at cell junctions and may link cell adhesion structures to the actin cytoskeleton. This protein may be involved in the assembly and stabilization of actin-filaments and likely plays a role in modulating cell adhesion, cell morphology and cell motility. This protein also localizes to the nucleus and may affect cardiomyocyte …

**Accessions** — [HGNC:24686](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24686) · Entrez [54751](https://www.ncbi.nlm.nih.gov/gene/54751) · UniProt [Q8WUP2](https://www.uniprot.org/uniprotkb/Q8WUP2) · Ensembl [ENSG00000162458](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162458)

## Data

Gene col 8522: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8522); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8522, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8522]; `tensor/DDL_lfc|DDL_z.npy` [8522]; `embed/gene_vectors.npy` [8522]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8522 or target_col == 8522). Every well: [[FBLIM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBLIM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
