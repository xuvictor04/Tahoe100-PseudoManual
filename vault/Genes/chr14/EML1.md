---
symbol: "EML1"
type: "gene"
col: 833
ensembl_id: "ENSG00000066629"
name: "EMAP like 1"
location: "14q32.2"
module: 13
arm: "+"
pooled_cpm: 16.08
n_lines_expressing: 37
n_dd_up: 13
n_dd_down: 16
n_dd_up_clean: 13
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 18
direction_downstream: 9
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# EML1

*EMAP like 1* — 14q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.55× (z +5.4, q 4e-05, up in 19 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.536× (z -7.7, q 1e-11, down in 25 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.653× (z -7.4, q 4e-11, down in 19 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRIN2A]] (+0.66, fdr 9e-06), [[VSTM4]] (+0.61, fdr 3e-05), [[MYLK]] (+0.58, fdr 1e-05); moves opposite to [[STXBP5-AS1]] (-0.49, fdr 6e-05), [[PRRG2]] (-0.46, fdr 2e-04), [[UGP2]] (-0.45, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[KIRREL3]] → it (grade B ⚠); 9 go from it, the strongest it → [[OLFML2A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 833.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +5.4 | 4e-05 | 19/35 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 0.003 | 12/34 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +4.3 | 0.003 | 14/35 (SK-MEL-2, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +4.3 | 0.003 | 11/34 (J82, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.004 | 13/35 (J82, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +4.0 | 0.006 | 13/35 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.006 | 13/35 (A-172, PANC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.006 | 12/35 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.008 | 15/35 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.011 | 13/35 (HOP62, A-172, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.011 | 15/35 (SW 900, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.023 | 12/33 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.71×** | +3.4 | 0.025 | 9/35 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 833.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.536×** | -7.7 | 1e-11 | 25/34 (NCI-H23, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.653×** | -7.4 | 4e-11 | 19/32 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.584×** | -6.6 | 7e-09 | 23/35 (NCI-H2030, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.593×** | -6.4 | 2e-08 | 22/35 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.602×** | -6.2 | 5e-08 | 21/35 (AN3 CA, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.633×** | -5.6 | 2e-06 | 18/35 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.627×** | -5.5 | 3e-06 | 18/31 (C-33 A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.441×** | -5.3 | 1e-05 | 21/35 (AN3 CA, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.453×** | -5.1 | 2e-05 | 16/33 (HOP62, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.697×** | -4.4 | 4e-04 | 19/35 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -4.4 | 4e-04 | 19/34 (C-33 A, A-172, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.697×** | -4.4 | 4e-04 | 16/35 (H4, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -4.1 | 0.002 | 14/33 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.714×** | -3.9 | 0.004 | 15/35 (HOP62, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.804×** | -3.8 | 0.005 | 14/35 (A-172, SNU-1, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.836× | -3.1 | 0.057 | 12/35 (hTERT-HPNE, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 833. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 57.7 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.212× (z -10.9) ⚠ toxic · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -10.5) |
| [[A-172 (line)]] | wt | 32.8 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.116× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -10.2) |
| [[H4 (line)]] | wt | 37.6 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +8.5) | [[Clobetasol propionate (drug)]] 0.05 µM 0.0897× (z -10.9) |
| [[HOP62 (line)]] | alt | 46.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -16.1) |
| [[MIA PaCa-2 (line)]] | alt | 20.9 | 1 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 1.87× (z +11.2) ⚠ position not correctable | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 6.19 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0472× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 32.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -9.8) |
| [[A-427 (line)]] | wt | 24.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.219× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 43.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0688× (z -11.8) |
| [[BT-474 (line)]] | alt | 6.66 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0750× (z -9.4) |
| [[Hs 766T (line)]] | wt | 14.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -8.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 54.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -13.0) |
| [[J82 (line)]] | alt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.94× (z +13.9) | — |
| [[LoVo (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[NCI-H23 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 13.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.201× (z -11.1) |
| [[PANC-1 (line)]] | alt | 31.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 31.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -8.7) |
| [[SNU-423 (line)]] | alt | 22.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -8.5) |
| [[A498 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.98 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 833), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRIN2A]] | +0.66 | +0.57 / +0.61 | both halves | 9e-06 | **novel candidate** |
| [[VSTM4]] | +0.61 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[MYLK]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[AFF3]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[TIMP3]] | +0.58 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[SLC8A1]] | +0.57 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ABI3BP]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[SYNPO]] | +0.56 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[EVC]] | +0.56 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[COL7A1]] | +0.56 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[ADAMTS16]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ZMIZ1]] | +0.55 | +0.46 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STXBP5-AS1]] | -0.49 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[PRRG2]] | -0.46 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[UGP2]] | -0.45 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[SLC19A2]] | -0.44 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[ADAMTS9]] | -0.44 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[POC1B-AS1]] | -0.43 | -0.30 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 12, C 6. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIRREL3]] | B | KIRREL3 activity raises EML1's level | lines that do not express KIRREL3 (36) vs lines expressing it (14) | 3.57× lower at baseline in the lines without KIRREL3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN |
| [[MEG3]] | B | MEG3 activity raises EML1's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 2.99× lower at baseline in the lines without MEG3 | 0.025 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8 |
| [[MIR493HG]] | B | MIR493HG activity raises EML1's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 3.21× lower at baseline in the lines without MIR493HG | 0.029 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252 |
| [[P3H2]] | B | P3H2 activity raises EML1's level | lines that do not express P3H2 (28) vs lines expressing it (22) | 2.40× lower at baseline in the lines without P3H2 | 0.030 | ⚠ within organs, on part of the lines; also absent: P3H2-AS1, SRGN, SPOCK1 |
| [[SIRLNT]] | B | SIRLNT activity raises EML1's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 3.47× lower at baseline in the lines without SIRLNT | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[PLEKHG4B]] | B | PLEKHG4B activity raises EML1's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 2.81× lower at baseline in the lines without PLEKHG4B | 0.038 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1 |
| [[OLFML2A]] | B | OLFML2A activity raises EML1's level | lines that do not express OLFML2A (20) vs lines expressing it (30) | 2.54× lower at baseline in the lines without OLFML2A | 0.048 | ⚠ within organs, on part of the lines; also absent: GBX1, FMNL1-DT, SCN5A |
| [[PDGFRB]] | B | PDGFRB activity raises EML1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 3.49× lower at baseline in the lines without PDGFRB | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[COL1A2]] | B | COL1A2 activity raises EML1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 3.40× lower at baseline in the lines without COL1A2 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5 |
| [[FBN1]] | B | FBN1 activity raises EML1's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 2.98× lower at baseline in the lines without FBN1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[COL5A3]] | B | COL5A3 activity raises EML1's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 2.06× lower at baseline in the lines without COL5A3 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[INSYN2B]] | B | INSYN2B activity raises EML1's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 2.94× lower at baseline in the lines without INSYN2B | 0.099 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OLFML2A]] | B | EML1 activity raises OLFML2A's level | lines that do not express EML1 (13) vs lines expressing it (37) | 2.70× lower at baseline in the lines without EML1 | 0.049 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FGF2, PYGO1 |
| [[P3H2]] | B | EML1 activity raises P3H2's level | lines that do not express EML1 (13) vs lines expressing it (37) | 2.94× lower at baseline in the lines without EML1 | 0.064 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FGF2, PYGO1 |
| [[CCDC3]] | B | EML1 activity raises CCDC3's level | lines that do not express EML1 (13) vs lines expressing it (37) | 1.75× lower at baseline in the lines without EML1 | 0.070 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FGF2, PYGO1 |
| [[COL5A1]] | B | EML1 activity raises COL5A1's level | lines that do not express EML1 (13) vs lines expressing it (37) | 6.17× lower at baseline in the lines without EML1 | 0.086 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FGF2, PYGO1 |
| [[PDGFC]] | B | EML1 activity raises PDGFC's level | lines that do not express EML1 (13) vs lines expressing it (37) | 3.59× lower at baseline in the lines without EML1 | 0.089 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FGF2, PYGO1 |
| [[ATRNL1]] | B | EML1 activity raises ATRNL1's level | lines that do not express EML1 (13) vs lines expressing it (37) | 3.80× lower at baseline in the lines without EML1 | 0.093 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FGF2, PYGO1 |
| [[DLG1]] | B | EML1 activity raises DLG1's level | lines that do not express EML1 (13) vs lines expressing it (37) | 1.17× lower at baseline in the lines without EML1 | 0.095 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FGF2, PYGO1 |
| [[SLC8A1]] | C | EML1 activity raises SLC8A1's level | lines that do not express EML1 (13) vs lines expressing it (37) | 4.83× lower at baseline in the lines without EML1 | 0.073 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FGF2, PYGO1; co-absent with the target |
| [[NHSL2]] | C | EML1 activity raises NHSL2's level | lines that do not express EML1 (13) vs lines expressing it (37) | 2.43× lower at baseline in the lines without EML1 | 0.078 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FGF2, PYGO1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.535). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.3, 18.3); signed map (28.7, 47.2). **Vector** length 82.5, 18.9% of its response variance represented; |z| ≥ 3 in 961 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.1 | +1.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +0.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.0 | -0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +3.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -4.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.4 | -1.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.4 | -0.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.3 | -0.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | EMAP like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.2 — chr14:99,737,693-99,942,060 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EMAP, HuEMAP, ELP79; previously EMAPL |
| Gene groups (HGNC) | WD repeat domain containing; EMAP like |
| Matched by | ensembl_id |

**Function**, from UniProt [O00423](https://www.uniprot.org/uniprotkb/O00423) (Echinoderm microtubule-associated protein-like 1):

> Modulates the assembly and organization of the microtubule cytoskeleton, and probably plays a role in regulating the orientation of the mitotic spindle and the orientation of the plane of cell division. Required for normal proliferation of neuronal progenitor cells in the developing brain and for normal brain development. Does not affect neuron migration per se.

**Summary**, from NCBI Gene [2009](https://www.ncbi.nlm.nih.gov/gene/2009):

> Human echinoderm microtubule-associated protein-like is a strong candidate for the Usher syndrome type 1A gene. Usher syndromes (USHs) are a group of genetic disorders consisting of congenital deafness, retinitis pigmentosa, and vestibular dysfunction of variable onset and severity depending on the genetic type. The disease process in USHs involves the entire brain and is not limited to the posterior fossa or auditory and visual systems. The USHs are catagorized as type I (USH1A, USH1B, USH1C, …

**Accessions** — [HGNC:3330](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3330) · Entrez [2009](https://www.ncbi.nlm.nih.gov/gene/2009) · UniProt [O00423](https://www.uniprot.org/uniprotkb/O00423) · Ensembl [ENSG00000066629](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066629)

## Data

Gene col 833: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 833); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 833, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 833]; `tensor/DDL_lfc|DDL_z.npy` [833]; `embed/gene_vectors.npy` [833]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 833 or target_col == 833). Every well: [[EML1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EML1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
