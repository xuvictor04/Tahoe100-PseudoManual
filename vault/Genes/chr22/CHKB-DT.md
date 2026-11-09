---
symbol: "CHKB-DT"
type: "gene"
col: 12989
ensembl_id: "ENSG00000205559"
name: "CHKB divergent transcript"
location: "22q13.33"
module: 10
arm: "+"
pooled_cpm: 6.76
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 15
n_dd_up_clean: 14
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CHKB-DT

*CHKB divergent transcript* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.69× (z +14.7, q 0e+00, up in 38 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.284× (z -10.0, q 7e-21, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM9B-AS1]] (+0.64, fdr 4e-05), [[F8]] (+0.64, fdr 4e-05), [[SEPTIN7-DT]] (+0.62, fdr 1e-04); moves opposite to [[NDRG3]] (-0.56, fdr 8e-05), [[AGO1]] (-0.56, fdr 1e-05), [[SUDS3]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC02175]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RELA-DT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12989.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.69×** | +14.7 | 0e+00 | 38/38 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.82×** | +10.3 | 3e-22 | 33/36 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.03×** | +8.8 | 2e-16 | 40/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.85×** | +8.3 | 1e-14 | 41/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +6.9 | 7e-10 | 28/39 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.28×** | +6.6 | 5e-09 | 32/47 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +6.2 | 4e-08 | 25/42 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +5.7 | 7e-07 | 3/11 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.81×** | +4.7 | 1e-04 | 23/46 (SW480, LS 180, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.74×** | +4.3 | 0.001 | 17/31 (KATO III, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.70×** | +3.9 | 0.005 | 17/47 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.006 | 17/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.61×** | +3.8 | 0.007 | 16/45 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.36×** | +3.2 | 0.049 | 14/46 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.50×** | +3.2 | 0.049 | 6/28 (NCI-H2030, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.48×** | +3.1 | 0.066 | 12/44 (PANC-1, NCI-H23, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.52×** | +3.1 | 0.072 | 9/44 (A498, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12989.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.284×** | -10.0 | 7e-21 | 40/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.286×** | -9.9 | 7e-21 | 33/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.319×** | -9.1 | 2e-17 | 32/40 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.401×** | -7.2 | 6e-11 | 32/46 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.412×** | -7.0 | 2e-10 | 29/44 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.435×** | -6.2 | 4e-08 | 27/43 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.561×** | -4.6 | 4e-04 | 23/44 (PANC-1, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.572×** | -4.1 | 0.004 | 20/47 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.605×** | -4.0 | 0.004 | 21/47 (SK-MEL-2, A549, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.627×** | -3.7 | 0.011 | 17/44 (RPMI-7951, C-33 A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.627×** | -3.7 | 0.011 | 20/47 (CFPAC-1, NCI-H23, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.429×** | -3.5 | 0.021 | 17/38 (NCI-H1792, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.642×** | -3.4 | 0.032 | 18/37 (NCI-H1573, A549, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.760×** | -3.1 | 0.085 | 17/45 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.656×** | -3.1 | 0.085 | 15/45 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12989. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 13.6 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0628× (z -17.6) |
| [[SW480 (line)]] | alt | 6.99 | 3 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +10.7) | [[Digitoxin (drug)]] 5 µM 0.0354× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.112× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 15.0 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -9.7) |
| [[LS 180 (line)]] | wt | 5.12 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.82× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 9.28 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.46× (z +11.7) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.126× (z -8.5) |
| [[A-427 (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0947× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 19.3 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0788× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0990× (z -9.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 7.04 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0568× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 13.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 4.66 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0321× (z -8.7) |
| [[KATO III (line)]] | alt | 7.13 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.101× (z -8.7) |
| [[LoVo (line)]] | wt | 8.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 3.33 | 0 | 1 | — | [[Peretinoin (drug)]] 0.5 µM 0.0477× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 9.99 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1792 (line)]] | alt | 3.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.96× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 5.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.04× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 9.30 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 3.43 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0595× (z -10.3) |
| [[SW 900 (line)]] | alt | 3.84 | 0 | 1 | — | [[Acetazolamide (drug)]] 5 µM 0.0432× (z -9.4) |
| [[A-172 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12989), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM9B-AS1]] | +0.64 | +0.77 / +0.42 | both halves | 4e-05 |  |
| [[F8]] | +0.64 | +0.81 / +0.42 | both halves | 4e-05 |  |
| [[SEPTIN7-DT]] | +0.62 | +0.79 / +0.35 | both halves | 1e-04 | same gene group |
| [[WTAP]] | +0.62 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[ACKR2]] | +0.61 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[SOCS3-DT]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 | same gene group |
| [[FAM174B]] | +0.61 | +0.74 / +0.31 | both halves | 2e-04 |  |
| [[BOLA1]] | +0.60 | +0.73 / +0.46 | both halves | 2e-05 |  |
| [[DDX59-AS1]] | +0.59 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[RBM8A]] | +0.58 | +0.63 / +0.38 | both halves | 6e-05 |  |
| [[BDNF-AS]] | +0.58 | +0.77 / +0.32 | both halves | 1e-04 |  |
| [[ANKHD1-DT]] | +0.58 | +0.80 / +0.39 | both halves | 6e-05 | same gene group |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG3]] | -0.56 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[AGO1]] | -0.56 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[SUDS3]] | -0.54 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[APMAP]] | -0.52 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[GFM2]] | -0.52 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02175]] | B | LINC02175 activity raises CHKB-DT's level | lines that do not express LINC02175 (7) vs lines expressing it (43) | 1.57× lower at baseline in the lines without LINC02175 | 0.027 | ⚠ within organs, on part of the lines; also absent: CEP41, LRRIQ3, FAM182B; maybe low, not absent |
| [[RDM1P5]] | B | RDM1P5 activity raises CHKB-DT's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.81× lower at baseline in the lines without RDM1P5 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[LINC02175]] | B | LINC02175 activity strengthens CHKB-DT's drug response | lines that do not express LINC02175 (7) vs lines expressing it (40) | the lines without LINC02175 respond 0.64× as strongly (z diff +1.42); strongest at Ouabain (Octahydrate) 5 µM: 0.54x vs 0.23x (z diff +3.4) | 0.065 | ⚠ within organs, on part of the lines; also absent: CEP41, LRRIQ3, FAM182B; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[FAM66C]] | B | FAM66C activity raises CHKB-DT's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.45× lower at baseline in the lines without FAM66C | 0.095 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[EFCAB6]] | B | EFCAB6 activity raises CHKB-DT's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.71× lower at baseline in the lines without EFCAB6 | 0.098 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[ANKRD20A21P]] | B | ANKRD20A21P activity raises CHKB-DT's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.42× lower at baseline in the lines without ANKRD20A21P | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[LRRIQ3]] | C | LRRIQ3 activity raises CHKB-DT's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.50× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RELA-DT]] | C | CHKB-DT's natural level strengthens RELA-DT's drug response | CHKB-DT's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.65, reverse -0.09; direction not clear | 0.077 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.3, 27.1); signed map (35.2, -6.5). **Vector** length 64.3, 11.6% of its response variance represented; |z| ≥ 3 in 1,202 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +14.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +6.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +1.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +2.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.3 | +3.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.7 | -7.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.4 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -4.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -3.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -3.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.1 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +1.8 |

## What is on record

|  |  |
|---|---|
| Name | CHKB divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 22q13.33 — chr22:50,583,026-50,595,634 (+) |
| Ensembl biotype | lncRNA |
| Also known as | TCONS_00029632, HRAT; previously CHKB-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40146](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40146) · Entrez [100144603](https://www.ncbi.nlm.nih.gov/gene/100144603) · Ensembl [ENSG00000205559](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205559)

## Data

Gene col 12989: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12989); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12989, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12989]; `tensor/DDL_lfc|DDL_z.npy` [12989]; `embed/gene_vectors.npy` [12989]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12989 or target_col == 12989). Every well: [[CHKB-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHKB-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
