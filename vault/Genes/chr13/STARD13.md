---
symbol: "STARD13"
type: "gene"
col: 5422
ensembl_id: "ENSG00000133121"
name: "StAR related lipid transfer domain containing 13"
location: "13q13.1"
module: 120
arm: "+"
pooled_cpm: 83.16
n_lines_expressing: 43
n_dd_up: 6
n_dd_down: 19
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 8
direction_downstream: 3
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# STARD13

*StAR related lipid transfer domain containing 13* — 13q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.98× (z +8.4, q 3e-14, up in 26 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.536× (z -10.8, q 2e-24, down in 34 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCN1]] (+0.63, fdr 7e-06), [[ETS1]] (+0.62, fdr 1e-05), [[RASAL2]] (+0.60, fdr 1e-05); moves opposite to [[SMG1P5]] (-0.56, fdr 3e-05), [[TMEM50B]] (-0.54, fdr 1e-05), [[KCTD7]] (-0.53, fdr 3e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[FRMD4A]] → it (grade B ⚠); 3 go from it, the strongest it → [[CSTF2T]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5422.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.98×** | +8.4 | 3e-14 | 26/41 (NCI-H23, A-427, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.46×** | +5.8 | 2e-06 | 25/42 (HOP62, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +4.7 | 4e-04 | 21/41 (NCI-H23, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.43×** | +4.4 | 0.001 | 21/40 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.44×** | +4.3 | 0.002 | 21/40 (SK-MEL-2, NCI-H1573, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.38×** | +4.0 | 0.007 | 26/41 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5422.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.536×** | -10.8 | 2e-24 | 34/42 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.472×** | -8.9 | 2e-16 | 33/40 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.489×** | -8.4 | 7e-15 | 25/35 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.467×** | -7.7 | 2e-12 | 30/42 (SHP-77, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.579×** | -6.7 | 2e-09 | 27/41 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.646×** | -5.4 | 8e-06 | 28/41 (NCI-H2030, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.675×** | -4.8 | 1e-04 | 27/41 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.690×** | -4.4 | 7e-04 | 23/43 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.699×** | -4.4 | 7e-04 | 22/41 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.707×** | -4.3 | 0.001 | 26/41 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.526×** | -4.1 | 0.002 | 27/41 (LOX-IMVI, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.714×** | -3.8 | 0.007 | 22/38 (KATO III, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.736×** | -3.8 | 0.007 | 21/41 (RKO, LOX-IMVI, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.752×** | -3.5 | 0.020 | 22/41 (NCI-H23, LoVo, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **0.820×** | -3.4 | 0.023 | 18/41 (BT-474, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.757×** | -3.2 | 0.043 | 20/41 (NCI-H2030, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Terfenadine (drug)]] 5 µM |  | 0.842× | -3.0 | 0.094 | 18/41 (Hs 766T, LoVo, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.788×** | -2.9 | 0.100 | 18/41 (C32, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5422. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 207 | 0 | 10 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.177× (z -14.6) ⚠ toxic; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -13.0) |
| [[SW480 (line)]] | alt | 82.7 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.255× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -11.4) |
| [[A498 (line)]] | wt | 131 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -14.6) |
| [[NCI-H1792 (line)]] | alt | 99.6 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.298× (z -9.9) |
| [[HOP62 (line)]] | alt | 128 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 17.1× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -11.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 321 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 171 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -14.1) |
| [[C32 (line)]] | wt | 185 | 0 | 4 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0377× (z -12.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 120 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 79.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +20.7) | [[Dinaciclib (drug)]] 5 µM 0.184× (z -13.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 90.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +12.2) | — |
| [[Hs 766T (line)]] | wt | 117 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 79.9 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.84× (z +11.1) | [[Harringtonine (drug)]] 5 µM 0.322× (z -10.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -10.0) |
| [[A-427 (line)]] | wt | 32.7 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.91× (z +12.2) | — |
| [[A549 (line)]] | wt | 100 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.44× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -10.0) |
| [[AN3 CA (line)]] | alt | 87.9 | 0 | 2 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0612× (z -11.8) |
| [[COLO 205 (line)]] | alt | 36.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -13.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 95.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[PANC-1 (line)]] | alt | 66.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.230× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.288× (z -9.4) |
| [[SHP-77 (line)]] | alt | 33.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0929× (z -13.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 113 | 2 (1 ⚠) | 0 | [[Daptomycin (drug)]] 5 µM 3.45× (z +9.4) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 3.28× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 74.0 | 2 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.33× (z +8.9) | — |
| [[AsPC-1 (line)]] | alt | 63.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -13.0) |
| [[CHP-212 (line)]] | wt | 79.3 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0546× (z -9.3) |
| [[H4 (line)]] | wt | 81.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 23.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 52.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.234× (z -10.5) |
| [[SNU-423 (line)]] | alt | 118 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.5× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.2 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 100 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 237 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.41 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.96 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 45.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5422), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCN1]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ETS1]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[RASAL2]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[SRGAP1]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 | pathway: CDC42 GTPase cycle |
| [[LINC00707]] | +0.59 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[DDAH1]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[NAV3]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ABL2]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[FRMD6]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[TRPC4]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[SFTA1P]] | +0.56 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[GPR176]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG1P5]] | -0.56 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[TMEM50B]] | -0.54 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[KCTD7]] | -0.53 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[CAPN10]] | -0.51 | -0.57 / -0.40 | both halves | 4e-05 |  |
| [[C20orf96]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[GIT1]] | -0.51 | -0.62 / -0.39 | both halves | 6e-05 | pathway: CDC42 GTPase cycle |
| [[DCUN1D4]] | -0.50 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[AZIN2]] | -0.50 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[SEC61A2]] | -0.48 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[CBFA2T2]] | -0.48 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[FAM102A]] | -0.47 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[RAD9A]] | -0.47 | -0.44 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMD4A]] | B | FRMD4A activity raises STARD13's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 3.22× lower at baseline in the lines without FRMD4A | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[GLIPR1]] | B | GLIPR1 activity raises STARD13's level | lines that do not express GLIPR1 (21) vs lines expressing it (29) | 2.77× lower at baseline in the lines without GLIPR1 | 0.040 | ⚠ within organs, on part of the lines; also absent: STC1, ENSG00000253891, ENSG00000230615; maybe low, not absent |
| [[BICC1]] | B | BICC1 activity raises STARD13's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 2.32× lower at baseline in the lines without BICC1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[ALPK2]] | B | ALPK2 activity raises STARD13's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 2.75× lower at baseline in the lines without ALPK2 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4 |
| [[PDCD1LG2]] | B | PDCD1LG2 activity raises STARD13's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 2.57× lower at baseline in the lines without PDCD1LG2 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |
| [[CCBE1]] | B | CCBE1 activity raises STARD13's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 2.25× lower at baseline in the lines without CCBE1 | 0.076 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[S1PR3]] | B | S1PR3 activity raises STARD13's level | lines that do not express S1PR3 (21) vs lines expressing it (29) | 1.92× lower at baseline in the lines without S1PR3 | 0.088 | ⚠ within organs, on part of the lines; also absent: BASP1, VEGFC, SPANXA2-OT1 |
| [[ITPR2]] | B | ITPR2 activity raises STARD13's level | lines that do not express ITPR2 (5) vs lines expressing it (45) | 3.59× lower at baseline in the lines without ITPR2 | 0.098 | ⚠ within organs, on part of the lines; also absent: ITPR2-AS1, ENSG00000286162, SPATA17; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSTF2T]] | B | STARD13 activity raises CSTF2T's level | lines that do not express STARD13 (7) vs lines expressing it (43) | 1.35× lower at baseline in the lines without STARD13 | 0.010 | ⚠ within organs, on part of the lines |
| [[STARD13-AS]] | B | STARD13 activity raises STARD13-AS's level | lines that do not express STARD13 (7) vs lines expressing it (43) | 1.42× lower at baseline in the lines without STARD13 | 0.011 | ⚠ within organs, on part of the lines |
| [[VGLL3]] | B | STARD13 activity lowers VGLL3's level | lines that do not express STARD13 (7) vs lines expressing it (43) | 1.71× higher at baseline in the lines without STARD13 | 0.054 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.706). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.9, 11.8); signed map (13.0, 40.6). **Vector** length 127, 39.5% of its response variance represented; |z| ≥ 3 in 1,153 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.5 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.4 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +4.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.3 | +4.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.5 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.4 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +2.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.9 | +1.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +4.8 | +2.1 |
| fall | [[Artesunate (drug)]] 5 µM |  | -4.5 | -3.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.1 | -2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -10.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.3 | -1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.2 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | StAR related lipid transfer domain containing 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.1 — chr13:33,103,137-33,350,630 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GT650, DLC2, ARHGAP37; previously LINC00464 |
| Gene groups (HGNC) | Rho GTPase activating proteins; StAR related lipid transfer domain containing |
| Reactome | 7 pathways, smallest: RHOB GTPase cycle; RHOC GTPase cycle; RHOA GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3M8](https://www.uniprot.org/uniprotkb/Q9Y3M8) (StAR-related lipid transfer protein 13):

> GTPase-activating protein for RhoA, and perhaps for Cdc42. May be involved in regulation of cytoskeletal reorganization, cell proliferation and cell motility. Acts a tumor suppressor in hepatocellular carcinoma cells.

**Summary**, from NCBI Gene [90627](https://www.ncbi.nlm.nih.gov/gene/90627):

> This gene encodes a protein which contains an N-terminal sterile alpha motif (SAM) for protein-protein interactions, followed by an ATP/GTP-binding motif, a GTPase-activating protein (GAP) domain, and a C-terminal STAR-related lipid transfer (START) domain. It may be involved in regulation of cytoskeletal reorganization, cell proliferation, and cell motility, and acts as a tumor suppressor in hepatoma cells. The gene is located in a region of chromosome 13 that is associated with loss of …

**Accessions** — [HGNC:19164](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19164) · Entrez [90627](https://www.ncbi.nlm.nih.gov/gene/90627) · UniProt [Q9Y3M8](https://www.uniprot.org/uniprotkb/Q9Y3M8) · Ensembl [ENSG00000133121](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133121)

## Data

Gene col 5422: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5422); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5422, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5422]; `tensor/DDL_lfc|DDL_z.npy` [5422]; `embed/gene_vectors.npy` [5422]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5422 or target_col == 5422). Every well: [[STARD13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STARD13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
