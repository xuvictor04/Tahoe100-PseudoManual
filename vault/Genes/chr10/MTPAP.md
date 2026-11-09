---
symbol: "MTPAP"
type: "gene"
col: 2902
ensembl_id: "ENSG00000107951"
name: "mitochondrial poly(A) polymerase"
location: "10p11.23"
module: 1
arm: "+"
pooled_cpm: 26.95
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MTPAP

*mitochondrial poly(A) polymerase* — 10p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.27× (z +20.6, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.684× (z -6.5, q 6e-08, down in 20 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.811× (z -5.2, q 5e-05, down in 19 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UTP15]] (+0.76, fdr 7e-06), [[ZNF507]] (+0.76, fdr 7e-06), [[DIS3L]] (+0.76, fdr 7e-06); moves opposite to [[QSOX1]] (-0.69, fdr 7e-06), [[INPP5A]] (-0.65, fdr 1e-05), [[MYO9B]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PPP1R9A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2902.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.27×** | +20.6 | 0e+00 | 45/47 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.06×** | +19.9 | 0e+00 | 47/47 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.44×** | +15.7 | 0e+00 | 46/48 (SW480, LS 180, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.43×** | +15.1 | 0e+00 | 44/48 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.16×** | +13.7 | 2e-40 | 47/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.73×** | +12.2 | 2e-32 | 40/47 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.92×** | +11.6 | 4e-29 | 42/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +11.6 | 4e-29 | 41/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.92×** | +11.6 | 4e-29 | 41/48 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.79×** | +10.4 | 2e-23 | 36/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +7.7 | 9e-13 | 36/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +7.4 | 6e-12 | 30/46 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.9 | 2e-07 | 0/48 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +5.3 | 5e-06 | 26/47 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +4.8 | 5e-05 | 14/30 (LoVo, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +4.8 | 6e-05 | 22/48 (NCI-H1792, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.28×** | +4.2 | 9e-04 | 16/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +4.0 | 0.002 | 19/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[EX229 (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.040 | 4/47 (SK-MEL-2, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2902.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.684×** | -6.5 | 6e-08 | 20/37 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.811×** | -5.2 | 5e-05 | 19/48 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.770×** | -4.6 | 7e-04 | 23/48 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.774×** | -4.5 | 8e-04 | 20/48 (NCI-H2030, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.863× | -3.7 | 0.026 | 14/48 (A498, SW1417, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.820×** | -3.5 | 0.040 | 13/47 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.814×** | -3.5 | 0.040 | 11/48 (AsPC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.830×** | -3.3 | 0.071 | 13/47 (MIA PaCa-2, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2902. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 36.4 | 6 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.52× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.459× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 23.8 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +10.2) | — |
| [[LoVo (line)]] | wt | 24.0 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.65× (z +11.3) | — |
| [[NCI-H1792 (line)]] | alt | 32.3 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.10× (z +12.9) | — |
| [[RKO (line)]] | wt | 53.0 | 1 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 8.83× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -11.9) |
| [[A-172 (line)]] | wt | 19.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.163× (z -12.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 20.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.120× (z -12.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 28.5 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.43× (z +12.0) | — |
| [[NCI-H2030 (line)]] | alt | 59.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +10.0) | — |
| [[A498 (line)]] | wt | 29.7 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.87× (z +10.2) | — |
| [[A549 (line)]] | wt | 31.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +12.6) | — |
| [[AN3 CA (line)]] | alt | 36.0 | 0 | 2 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0724× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 23.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +13.3) | — |
| [[HEC-1-A (line)]] | alt | 34.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 16.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 18.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 23.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 23.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +11.3) | — |
| [[Panc 03.27 (line)]] | alt | 25.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +12.2) | — |
| [[PANC-1 (line)]] | alt | 20.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +12.1) | — |
| [[SNU-1 (line)]] | wt | 43.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.365× (z -8.9) |
| [[SW1417 (line)]] | alt | 40.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.369× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.79× (z +10.0) | — |
| [[J82 (line)]] | alt | 27.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.6) | — |
| [[KATO III (line)]] | alt | 21.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.21× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 31.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.26× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 28.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +10.5) | — |
| [[SW48 (line)]] | wt | 53.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -9.2) |
| [[A-427 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2902), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP15]] | +0.76 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.76 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[DIS3L]] | +0.76 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[QTRT2]] | +0.74 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[KICS2]] | +0.73 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[POLR1F]] | +0.73 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[DDX20]] | +0.72 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[MRRF]] | +0.72 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[AASDHPPT]] | +0.72 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[TGFBRAP1]] | +0.70 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[METAP1D]] | +0.70 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[VPS72]] | +0.70 | +0.64 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QSOX1]] | -0.69 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[INPP5A]] | -0.65 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[MYO9B]] | -0.65 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[RABGEF1]] | -0.63 | -0.60 / -0.70 | both halves | 7e-06 |  |
| [[APLP2]] | -0.62 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[F11R]] | -0.62 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[TMEM184B]] | -0.62 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[MBOAT7]] | -0.62 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[P4HB]] | -0.60 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[HSP90B1]] | -0.60 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[NDRG1]] | -0.60 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[ZCCHC17]] | -0.60 | -0.50 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R9A]] | B | PPP1R9A activity raises MTPAP's level | lines that do not express PPP1R9A (16) vs lines expressing it (34) | 1.72× lower at baseline in the lines without PPP1R9A | 0.007 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[HDAC6]] | B | HDAC6 activity raises MTPAP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.773). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.8, 5.4); signed map (2.5, -39.6). **Vector** length 81.7, 19.1% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +19.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.1 | +4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.0 | +11.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +7.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +4.7 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.5 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.4 | -0.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -4.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.2 | -4.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | +0.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | +0.0 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial poly(A) polymerase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.23 — chr10:30,309,801-30,374,448 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10486, SPAX4, TENT6; previously PAPD1 |
| Gene groups (HGNC) | Non-canonical poly(A) polymerases; Terminal nucleotidyltransferases |
| Reactome | 2 pathways, smallest: Mitochondrial mRNA modification; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVV4](https://www.uniprot.org/uniprotkb/Q9NVV4) (Poly(A) RNA polymerase, mitochondrial):

> Polymerase that creates the 3' poly(A) tail of mitochondrial transcripts. Can use all four nucleotides, but has higher activity with ATP and UTP (in vitro). Plays a role in replication-dependent histone mRNA degradation. May be involved in the terminal uridylation of mature histone mRNAs before their degradation is initiated. Might be responsible for the creation of some UAA stop codons which are not encoded in mtDNA.

**Summary**, from NCBI Gene [55149](https://www.ncbi.nlm.nih.gov/gene/55149):

> The protein encoded by this gene is a member of the DNA polymerase type-B-like family. This enzyme synthesizes the 3' poly(A) tail of mitochondrial transcripts and plays a role in replication-dependent histone mRNA degradation.[provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:25532](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25532) · Entrez [55149](https://www.ncbi.nlm.nih.gov/gene/55149) · UniProt [Q9NVV4](https://www.uniprot.org/uniprotkb/Q9NVV4) · Ensembl [ENSG00000107951](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107951)

## Data

Gene col 2902: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2902); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2902, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2902]; `tensor/DDL_lfc|DDL_z.npy` [2902]; `embed/gene_vectors.npy` [2902]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2902 or target_col == 2902). Every well: [[MTPAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTPAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
