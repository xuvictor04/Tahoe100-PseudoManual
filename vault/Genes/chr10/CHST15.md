---
symbol: "CHST15"
type: "gene"
col: 11233
ensembl_id: "ENSG00000182022"
name: "carbohydrate sulfotransferase 15"
location: "10q26.13"
module: 141
arm: "+"
pooled_cpm: 63.84
n_lines_expressing: 37
n_dd_up: 1
n_dd_down: 30
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# CHST15

*carbohydrate sulfotransferase 15* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.27× (z +4.8, q 0.001, up in 17 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (PANC-1 4.17×, HS-578T 2.16×, J82 2.37×, HOP62 2.42×); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 4.56×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.201× (z -22.1, q 0e+00, down in 34 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA1]] (+0.57, fdr 2e-05), [[ZNF597]] (+0.55, fdr 3e-05), [[DIO3OS]] (+0.53, fdr 2e-05); moves opposite to [[SLC9A6]] (-0.46, fdr 2e-04), [[ZFP14]] (-0.44, fdr 1e-04), [[MTM1]] (-0.44, fdr 2e-04).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[KRT23]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LTBP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11233.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (PANC-1 4.17×, HS-578T 2.16×, J82 2.37×, HOP62 2.42×); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 4.56×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +4.8 | 0.001 | 17/35 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11233.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.201×** | -22.1 | 0e+00 | 34/35 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.211×** | -21.5 | 0e+00 | 35/35 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.271×** | -18.0 | 0e+00 | 35/35 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.517×** | -9.1 | 2e-17 | 28/35 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.538×** | -8.0 | 1e-13 | 26/34 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.674×** | -7.7 | 1e-12 | 23/36 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.590×** | -7.0 | 2e-10 | 24/37 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.604×** | -7.0 | 2e-10 | 27/35 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.592×** | -7.0 | 2e-10 | 24/35 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.604×** | -6.7 | 1e-09 | 22/28 (HepG2/C3A, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.625×** | -6.5 | 5e-09 | 27/35 (HEC-1-A, SW 1088, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.634×** | -6.3 | 2e-08 | 20/35 (HepG2/C3A, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.726×** | -6.2 | 2e-08 | 25/35 (SW480, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.453×** | -5.7 | 5e-07 | 25/36 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.676×** | -5.0 | 2e-05 | 18/29 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.696×** | -5.0 | 2e-05 | 19/35 (HepG2/C3A, SW48, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.742×** | -4.1 | 0.001 | 17/35 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[NG25 (drug)]] 5 µM |  | **0.577×** | -4.0 | 0.002 | 16/35 (NCI-H1573, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.771×** | -3.6 | 0.009 | 17/35 (A-427, NCI-H1573, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.783×** | -3.4 | 0.019 | 17/35 (COLO 205, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11233. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 140 | 0 | 23 (11 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0583× (z -26.7) |
| [[HepG2_C3A (line)]] | wt | 347 | 0 | 19 (11 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0657× (z -23.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.100× (z -21.4) |
| [[COLO 205 (line)]] | alt | 187 | 0 | 12 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0658× (z -21.7) |
| [[HEC-1-A (line)]] | alt | 146 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -19.8) |
| [[HOP62 (line)]] | alt | 36.0 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.128× (z -14.3) |
| [[SNU-423 (line)]] | alt | 127 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -15.8) |
| [[A498 (line)]] | wt | 121 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.274× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 128 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -16.1) |
| [[HS-578T (line)]] | alt | 67.5 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.192× (z -14.0) |
| [[J82 (line)]] | alt | 29.9 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.154× (z -13.9) |
| [[KATO III (line)]] | alt | 78.8 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.159× (z -13.9) |
| [[NCI-H1573 (line)]] | alt | 87.7 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.189× (z -15.0) |
| [[RPMI-7951 (line)]] | alt | 92.3 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.141× (z -14.8) |
| [[A-172 (line)]] | wt | 32.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -14.5) |
| [[H4 (line)]] | wt | 66.8 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.125× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 38.6 | 0 | 4 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.471× (z -18.2) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.194× (z -11.2) |
| [[RKO (line)]] | wt | 77.2 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.211× (z -13.1) |
| [[SW1417 (line)]] | alt | 76.1 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -11.0) |
| [[A549 (line)]] | wt | 38.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -12.2) |
| [[NCI-H2347 (line)]] | alt | 91.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 79.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.160× (z -18.8) |
| [[Panc 03.27 (line)]] | alt | 105 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -14.6) |
| [[SW 900 (line)]] | alt | 110 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -10.3) |
| [[PANC-1 (line)]] | alt | 29.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +18.0) | — |
| [[SW48 (line)]] | wt | 98.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -10.3) |
| [[AN3 CA (line)]] | alt | 61.9 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0737× (z -12.5) |
| [[BT-474 (line)]] | alt | 37.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.208× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 36.1 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.220× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0939× (z -15.1) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[A-427 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.65 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.76 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.36 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.17 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.56 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.99 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.30 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.52 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.04 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.82 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11233), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA1]] | +0.57 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ZNF597]] | +0.55 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[DIO3OS]] | +0.53 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[LINC00460]] | +0.53 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[COQ8B]] | +0.52 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[SERPINA1]] | +0.51 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[LINC02320]] | +0.50 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[PALD1]] | +0.50 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[MMP25]] | +0.50 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[ABR]] | +0.49 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[IL4R]] | +0.49 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[SCAT1]] | +0.49 | +0.49 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A6]] | -0.46 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[ZFP14]] | -0.44 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[MTM1]] | -0.44 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[GINM1]] | -0.43 | -0.41 / -0.29 | both halves | 3e-04 |  |
| [[ATP8A1]] | -0.43 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[KRAS]] | -0.42 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[STK38]] | -0.41 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[KIF3A]] | -0.41 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[SEC61A2]] | -0.41 | -0.39 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT23]] | B | KRT23 activity raises CHST15's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 3.77× lower at baseline in the lines without KRT23 | 0.011 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP |
| [[FOXQ1]] | B | FOXQ1 activity raises CHST15's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 2.24× lower at baseline in the lines without FOXQ1 | 0.041 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[LINC00460]] | B | LINC00460 activity raises CHST15's level | lines that do not express LINC00460 (31) vs lines expressing it (19) | 2.24× lower at baseline in the lines without LINC00460 | 0.045 | ⚠ within organs, on part of the lines; also absent: LINC02335, LINC01605, KISS1 |
| [[TNNT2]] | B | TNNT2 activity raises CHST15's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.20× lower at baseline in the lines without TNNT2 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[ZC3H12A]] | B | ZC3H12A activity raises CHST15's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 3.04× lower at baseline in the lines without ZC3H12A | 0.071 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent |
| [[KRT23]] | B | KRT23 activity strengthens CHST15's drug response | lines that do not express KRT23 (27) vs lines expressing it (10) | the lines without KRT23 respond 0.78× as strongly (z diff +1.90); strongest at Idarubicin (hydrochloride) 5 µM: 0.77x vs 0.45x (z diff +4.2) | 0.087 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP; target measured in part of the lines; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LTBP2]] | B | CHST15 activity raises LTBP2's level | lines that do not express CHST15 (13) vs lines expressing it (37) | 2.09× lower at baseline in the lines without CHST15 | 0.098 | ⚠ within organs, on part of the lines; also absent: SH2D4A |

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.456). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.4, 6.8); signed map (8.2, 34.3). **Vector** length 97.7, 25.8% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +4.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.7 | -0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | -0.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.8 | +0.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.7 | +0.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.3 | -6.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.6 | -4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -0.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | carbohydrate sulfotransferase 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:124,007,668-124,093,598 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GALNAC4S-6ST, BRAG, KIAA0598 |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Reactome | 5 pathways, smallest: DS-GAG biosynthesis; CS-GAG biosynthesis; Chondroitin sulfate/dermatan sulfate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7LFX5](https://www.uniprot.org/uniprotkb/Q7LFX5) (Carbohydrate sulfotransferase 15):

> Sulfotransferase that transfers sulfate from 3'-phosphoadenosine 5'-phosphosulfate (PAPS) to the C-6 hydroxyl group of the GalNAc 4-sulfate residue of chondroitin sulfate A and forms chondroitin sulfate E containing GlcA-GalNAc(4,6-SO(4)) repeating units. It also transfers sulfate to a unique non-reducing terminal sequence, GalNAc(4SO4)-GlcA(2SO4)-GalNAc(6SO4), to yield a highly sulfated structure similar to the structure found in thrombomodulin chondroitin sulfate. May also act as a B-cell …

**Summary**, from NCBI Gene [51363](https://www.ncbi.nlm.nih.gov/gene/51363):

> Chondroitin sulfate (CS) is a glycosaminoglycan which is an important structural component of the extracellular matrix and which links to proteins to form proteoglycans. Chondroitin sulfate E (CS-E) is an isomer of chondroitin sulfate in which the C-4 and C-6 hydroxyl groups are sulfated. This gene encodes a type II transmembrane glycoprotein that acts as a sulfotransferase to transfer sulfate to the C-6 hydroxal group of chondroitin sulfate. This gene has also been identified as being …

**Accessions** — [HGNC:18137](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18137) · Entrez [51363](https://www.ncbi.nlm.nih.gov/gene/51363) · UniProt [Q7LFX5](https://www.uniprot.org/uniprotkb/Q7LFX5) · Ensembl [ENSG00000182022](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182022)

## Data

Gene col 11233: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11233); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11233, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11233]; `tensor/DDL_lfc|DDL_z.npy` [11233]; `embed/gene_vectors.npy` [11233]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11233 or target_col == 11233). Every well: [[CHST15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHST15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
