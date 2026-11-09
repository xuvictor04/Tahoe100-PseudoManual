---
symbol: "PILRA"
type: "gene"
col: 1431
ensembl_id: "ENSG00000085514"
name: "paired immunoglobin like type 2 receptor alpha"
location: "7q22.1"
module: 38
arm: "+"
pooled_cpm: 15.4
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 12
n_dd_up_clean: 14
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 14
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# PILRA

*paired immunoglobin like type 2 receptor alpha* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.36× (z +16.6, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.608× (z -4.8, q 8e-04, down in 24 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.667× (z -3.9, q 0.018, down in 20 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM72]] (+0.86, fdr 7e-06), [[FNDC7]] (+0.85, fdr 7e-06), [[MYOCOS]] (+0.85, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[CCDC144CP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1431.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.36×** | +16.6 | 0e+00 | 42/46 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.39×** | +11.9 | 3e-30 | 42/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.32×** | +8.1 | 8e-14 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.27×** | +7.9 | 3e-13 | 32/46 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +6.6 | 6e-09 | 32/48 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +5.0 | 7e-05 | 25/46 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +4.9 | 8e-05 | 8/48 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +4.8 | 1e-04 | 28/48 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +4.6 | 3e-04 | 24/48 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +4.2 | 0.001 | 20/47 (NCI-H460, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.51×** | +3.9 | 0.004 | 19/48 (NCI-H460, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +3.9 | 0.004 | 18/47 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +3.9 | 0.004 | 17/48 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.52×** | +3.9 | 0.004 | 15/42 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.013 | 18/47 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.013 | 14/48 (A498, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.023 | 19/47 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1431.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.608×** | -4.8 | 8e-04 | 24/46 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.667×** | -3.9 | 0.018 | 20/47 (KATO III, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.664×** | -3.8 | 0.018 | 20/43 (RPMI-7951, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.664×** | -3.8 | 0.018 | 21/47 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.485×** | -3.7 | 0.028 | 16/44 (H4, SW480, …) | top dose only | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.679×** | -3.6 | 0.031 | 15/47 (MIA PaCa-2, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **0.684×** | -3.6 | 0.031 | 21/47 (AsPC-1, BT-474, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.686×** | -3.4 | 0.044 | 20/44 (SNU-423, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.515×** | -3.4 | 0.044 | 16/42 (NCI-H2030, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.708×** | -3.4 | 0.044 | 22/47 (BT-474, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.790×** | -3.3 | 0.058 | 13/48 (MIA PaCa-2, SW 1088, …) | top dose only | position effect removed |
| [[Bexarotene (drug)]] 5 µM |  | **0.721×** | -3.2 | 0.067 | 10/48 (NCI-H1573, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1431. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.41 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.8× (z +24.3) | — |
| [[BT-474 (line)]] | alt | 53.3 | 0 | 4 | — | [[Digitoxin (drug)]] 0.05 µM 0.177× (z -9.8) |
| [[SW480 (line)]] | alt | 16.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.243× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[A-172 (line)]] | wt | 11.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.22× (z +12.6) | [[Simotinib (drug)]] 5 µM 0.113× (z -9.6) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 7.47 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.155× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[C32 (line)]] | wt | 30.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.01× (z +13.1) | — |
| [[LoVo (line)]] | wt | 29.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 6.13 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.78× (z +10.9) | [[Tadalafil (drug)]] 0.05 µM 0.0936× (z -8.8) |
| [[SNU-423 (line)]] | alt | 12.7 | 0 | 2 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.101× (z -10.4) |
| [[SW1417 (line)]] | alt | 6.79 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.0984× (z -8.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 11.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0264× (z -14.7) |
| [[A549 (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 27.9 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0860× (z -10.9) |
| [[H4 (line)]] | wt | 18.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.34× (z +12.3) | — |
| [[HCT15 (line)]] | alt | 26.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 31.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 11.0 | 0 | 1 | — | [[Hydroxyurea (drug)]] 5 µM 0.0687× (z -8.6) |
| [[HOP62 (line)]] | alt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +11.5) | — |
| [[HT-29 (line)]] | alt | 8.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +9.1) | — |
| [[J82 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -10.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 8.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.69× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 17.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.92× (z +11.3) | — |
| [[NCI-H23 (line)]] | alt | 23.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +13.3) | — |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0942× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 18.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.00× (z +12.5) | — |
| [[SW 900 (line)]] | alt | 9.88 | 0 | 1 | — | [[Fenofibrate (drug)]] 5 µM 0.0633× (z -9.9) |
| [[SW48 (line)]] | wt | 28.8 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0589× (z -11.1) |
| [[A498 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1431), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM72]] | +0.86 | +0.88 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[FNDC7]] | +0.85 | +0.84 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[MYOCOS]] | +0.85 | +0.85 / +0.77 | both halves | 7e-06 |  |
| [[PYGM]] | +0.83 | +0.79 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[GARIN1A]] | +0.83 | +0.87 / +0.69 | both halves | 7e-06 |  |
| [[RFPL3S]] | +0.83 | +0.82 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[PITRM1-AS1]] | +0.82 | +0.80 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[AVIL]] | +0.82 | +0.80 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[IDI2-AS1]] | +0.82 | +0.86 / +0.75 | both halves | 7e-06 |  |
| [[NLGN3]] | +0.82 | +0.85 / +0.73 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.82 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.81 | +0.85 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 9, C 5. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC144CP]] | B | CCDC144CP activity raises PILRA's level | lines that do not express CCDC144CP (7) vs lines expressing it (43) | 2.01× lower at baseline in the lines without CCDC144CP | 0.011 | ⚠ within organs, on part of the lines; also absent: SNX10, CPPED1, GPLD1 |
| [[ASGR1]] | B | ASGR1 activity raises PILRA's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.51× lower at baseline in the lines without ASGR1 | 0.011 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[SLC26A4]] | B | SLC26A4 activity raises PILRA's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.80× lower at baseline in the lines without SLC26A4 | 0.016 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[XG]] | B | XG activity raises PILRA's level | lines that do not express XG (5) vs lines expressing it (45) | 2.16× lower at baseline in the lines without XG | 0.022 | ⚠ within organs, on part of the lines; also absent: TXNRD3, FSCN1, ELK3; maybe low, not absent |
| [[F2]] | B | F2 activity raises PILRA's level | lines that do not express F2 (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without F2 | 0.067 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[RUNDC3A-AS1]] | B | RUNDC3A-AS1 activity raises PILRA's level | lines that do not express RUNDC3A-AS1 (5) vs lines expressing it (45) | 2.01× lower at baseline in the lines without RUNDC3A-AS1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ERO1B, TEX14, TCTN1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PILRA's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[WNK4]] | B | WNK4 activity raises PILRA's level | lines that do not express WNK4 (5) vs lines expressing it (45) | 2.20× lower at baseline in the lines without WNK4 | 0.098 | ⚠ within organs, on part of the lines; also absent: TEX14, TMEM144, NEO1; maybe low, not absent |
| [[WTIP]] | B | WTIP activity raises PILRA's level | lines that do not express WTIP (5) vs lines expressing it (45) | 1.57× lower at baseline in the lines without WTIP | 0.099 | ⚠ within organs, on part of the lines; also absent: C5, BTG3; maybe low, not absent |
| [[NECAB2]] | C | NECAB2 activity raises PILRA's level | lines that do not express NECAB2 (3) vs lines expressing it (47) | 2.65× lower at baseline in the lines without NECAB2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, PARP11, DLG4; maybe low, not absent; its own permutation p |
| [[PHC1]] | C | PHC1 activity raises PILRA's level | lines that do not express PHC1 (4) vs lines expressing it (46) | 1.98× lower at baseline in the lines without PHC1 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, TPST1, TBKBP1 |
| [[MPP4]] | C | MPP4 activity raises PILRA's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 2.73× lower at baseline in the lines without MPP4 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.887). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.9, -15.9); signed map (16.2, 10.7). **Vector** length 103, 25.1% of its response variance represented; |z| ≥ 3 in 1,195 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +16.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.2 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +7.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +4.1 | +4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +11.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.5 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +4.2 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.8 | +2.4 |
|  | [[Cinacalcet (drug)]] 5 µM |  | +2.4 | +2.6 |
| fall | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -4.2 | -3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.0 | -3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.0 | -2.0 |
|  | [[NG25 (drug)]] 5 µM |  | -4.0 | -3.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -3.7 | -3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | paired immunoglobin like type 2 receptor alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,367,530-100,400,096 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FDF03 |
| Gene groups (HGNC) | V-set domain containing |
| Reactome | 2 pathways, smallest: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKJ1](https://www.uniprot.org/uniprotkb/Q9UKJ1) (Paired immunoglobulin-like type 2 receptor alpha):

> Paired receptors consist of highly related activating and inhibitory receptors and are widely involved in the regulation of the immune system. PILRA is thought to act as a cellular signaling inhibitory receptor by recruiting cytoplasmic phosphatases like PTPN6/SHP-1 and PTPN11/SHP-2 via their SH2 domains that block signal transduction through dephosphorylation of signaling molecules. Receptor for PIANP.; (Microbial infection) Acts as an entry co-receptor for herpes simplex virus 1.

**Summary**, from NCBI Gene [29992](https://www.ncbi.nlm.nih.gov/gene/29992):

> Cell signaling pathways rely on a dynamic interaction between activating and inhibiting processes. SHP-1-mediated dephosphorylation of protein tyrosine residues is central to the regulation of several cell signaling pathways. Two types of inhibitory receptor superfamily members are immunoreceptor tyrosine-based inhibitory motif (ITIM)-bearing receptors and their non-ITIM-bearing, activating counterparts. Control of cell signaling via SHP-1 is thought to occur through a balance between …

**Accessions** — [HGNC:20396](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20396) · Entrez [29992](https://www.ncbi.nlm.nih.gov/gene/29992) · UniProt [Q9UKJ1](https://www.uniprot.org/uniprotkb/Q9UKJ1) · Ensembl [ENSG00000085514](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085514)

## Data

Gene col 1431: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1431); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1431, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1431]; `tensor/DDL_lfc|DDL_z.npy` [1431]; `embed/gene_vectors.npy` [1431]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1431 or target_col == 1431). Every well: [[PILRA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PILRA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
