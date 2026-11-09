---
symbol: "ESRP1"
type: "gene"
col: 2457
ensembl_id: "ENSG00000104413"
name: "epithelial splicing regulatory protein 1"
location: "8q22.1"
module: 8
arm: "+"
pooled_cpm: 80.95
n_lines_expressing: 19
n_dd_up: 20
n_dd_down: 29
n_dd_up_clean: 14
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 66
direction_downstream: 104
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ESRP1

*epithelial splicing regulatory protein 1* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.81× (z +13.6, q 1e-39, up in 1 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.55× (z +7.5, q 1e-11, up in 0 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.463× (z -9.8, q 9e-20, down in 17 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALNT3]] (+0.78, fdr 7e-06), [[TMC4]] (+0.75, fdr 7e-06), [[TMEM125]] (+0.71, fdr 7e-06); moves opposite to [[BNC2]] (-0.50, fdr 5e-05), [[CPQ]] (-0.50, fdr 6e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 66 arrows point to it, the strongest [[TTC28]] → it (grade B ⚠); 104 go from it, the strongest it → [[PRRG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2457.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.81×** | +13.6 | 1e-39 | 1/18 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +9.2 | 1e-17 | 2/16 (AsPC-1, HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +7.5 | 1e-11 | 0/18 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.73×** | +7.3 | 5e-11 | 0/17 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.60×** | +6.2 | 5e-08 | 0/17 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +5.2 | 2e-05 | 0/16 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 2e-04 | 0/18 | all doses, flat | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.7 | 2e-04 | 5/17 (COLO 205, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.4 | 8e-04 | 0/19 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.37×** | +4.1 | 0.002 | 0/17 | inconsistent across doses |  |
| [[Dorzolamide (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.8 | 0.008 | 0/18 | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.009 | 1/17 (KATO III) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.014 | 0/18 | all doses, flat | position effect removed |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.016 | 0/18 | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.58×** | +3.4 | 0.023 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.56×** | +3.3 | 0.029 | 0/17 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.030 | 13/17 (BT-474, A-427, …) | top dose only |  |
| [[Erythromycin (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.039 | 0/17 | top dose only |  |
| [[Verteporfin (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.064 | 0/17 | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2457.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.463×** | -9.8 | 9e-20 | 17/17 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.483×** | -9.6 | 2e-19 | 17/17 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.533×** | -8.3 | 2e-14 | 16/17 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.630×** | -7.5 | 7e-12 | 17/17 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.595×** | -6.8 | 9e-10 | 17/17 (SW480, NCI-H2347, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.612×** | -6.5 | 9e-09 | 15/17 (NCI-H1573, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.622×** | -6.3 | 3e-08 | 17/17 (SW480, HT-29, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.661×** | -5.5 | 3e-06 | 17/17 (LoVo, HT-29, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.663×** | -5.4 | 4e-06 | 16/17 (SW480, HT-29, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.708×** | -4.6 | 3e-04 | 14/17 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.694×** | -4.4 | 4e-04 | 0/17 | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.767×** | -4.4 | 5e-04 | 17/17 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.543×** | -4.2 | 0.001 | 2/17 (SW480, A-427) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.583×** | -3.7 | 0.008 | 17/18 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.738×** | -3.7 | 0.008 | 0/17 | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.764×** | -3.6 | 0.013 | 0/17 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.757×** | -3.5 | 0.017 | 12/17 (SW48, SW480, …) | inconsistent across doses |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.771×** | -3.4 | 0.019 | 0/17 | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | **0.825×** | -3.3 | 0.027 | 15/17 (SW480, COLO 205, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2457. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 259 | 1 (1 ⚠) | 13 (8 ⚠) | [[Artesunate (drug)]] 5 µM 2.09× (z +8.5) ⚠ cell-cycle shift, explains ~43% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.0622× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.250× (z -15.7) |
| [[SW480 (line)]] | alt | 119 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -22.7) |
| [[HT-29 (line)]] | alt | 322 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -26.5) |
| [[NCI-H1573 (line)]] | alt | 178 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0752× (z -30.0) |
| [[KATO III (line)]] | alt | 336 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -15.8) |
| [[NCI-H2347 (line)]] | alt | 332 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -27.2) |
| [[COLO 205 (line)]] | alt | 287 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -24.3) |
| [[LoVo (line)]] | wt | 151 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -21.0) |
| [[BT-474 (line)]] | alt | 221 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -18.0) |
| [[CFPAC-1 (line)]] | alt | 100.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -26.0) |
| [[LS 180 (line)]] | wt | 249 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.269× (z -9.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.348× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 206 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -19.2) |
| [[HEC-1-A (line)]] | alt | 174 | 1 (1 ⚠) | 3 (2 ⚠) | [[Artesunate (drug)]] 5 µM 1.92× (z +8.6) ⚠ cell-cycle shift, explains ~43% of this change | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -11.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.491× (z -9.1) |
| [[HCT15 (line)]] | alt | 181 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -12.1) |
| [[A-427 (line)]] | wt | 49.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -10.8) |
| [[SW1417 (line)]] | alt | 200 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.367× (z -11.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.513× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 29.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -9.4) |
| [[A-172 (line)]] | wt | 6.13 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.68 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.69 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.57 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.23 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.84 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.05 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.36 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.28 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.90 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.94 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.13 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.76 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.11 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.16 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.88 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.68 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.02 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.62 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.26 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.43 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.49 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.26 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.57 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.17 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2457), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNT3]] | +0.78 | +0.79 / +0.76 | both halves | 7e-06 | pathway: Signaling by FGFR |
| [[TMC4]] | +0.75 | +0.77 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[TMEM125]] | +0.71 | +0.71 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[FUT3]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[INAVA]] | +0.66 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[PIP5K1B]] | +0.66 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ADCY4]] | +0.65 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[RORC]] | +0.63 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[SLC44A4]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[FAM83F]] | +0.63 | +0.52 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[OCLN]] | +0.62 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[MAL2]] | +0.61 | +0.68 / +0.50 | both halves | 1e-05 | STRING 578 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BNC2]] | -0.50 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[CPQ]] | -0.50 | -0.42 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*66 arrows, 66 of them with an alert ⚠; grade A 0, B 9, C 57. Shown: the 12 strongest; 54 more arrows (54 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC28]] | B | TTC28 activity lowers ESRP1's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 13.97× higher at baseline in the lines without TTC28 | 2e-04 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[SLC44A3]] | B | SLC44A3 activity raises ESRP1's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 4.40× lower at baseline in the lines without SLC44A3 | 0.018 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[SYTL1]] | B | SYTL1 activity raises ESRP1's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 6.10× lower at baseline in the lines without SYTL1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[TMEM51-AS1]] | B | TMEM51-AS1 activity raises ESRP1's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 4.32× lower at baseline in the lines without TMEM51-AS1 | 0.045 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |
| [[BNC2]] | B | BNC2 activity lowers ESRP1's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 7.26× higher at baseline in the lines without BNC2 | 0.053 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[FAM83E]] | B | FAM83E activity raises ESRP1's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 5.09× lower at baseline in the lines without FAM83E | 0.055 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[FBLIM1]] | B | FBLIM1 activity raises ESRP1's level | lines that do not express FBLIM1 (10) vs lines expressing it (40) | 4.26× lower at baseline in the lines without FBLIM1 | 0.074 | ⚠ within organs, on part of the lines; also absent: FAM83G, KITLG, DSG2 |
| [[IL17RE]] | B | IL17RE activity raises ESRP1's level | lines that do not express IL17RE (10) vs lines expressing it (40) | 4.60× lower at baseline in the lines without IL17RE | 0.079 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent |
| [[LINC03041]] | B | LINC03041 activity lowers ESRP1's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 10.95× higher at baseline in the lines without LINC03041 | 0.089 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent; its own permutation p |
| [[ST14]] | C | ST14 activity raises ESRP1's level | lines that do not express ST14 (32) vs lines expressing it (18) | 20.81× lower at baseline in the lines without ST14 | 9e-07 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1; co-absent with the target |
| [[TMEM125]] | C | TMEM125 activity raises ESRP1's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 22.16× lower at baseline in the lines without TMEM125 | 2e-06 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises ESRP1's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 19.59× lower at baseline in the lines without TMPRSS4 | 5e-06 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |

### Downstream of this gene

*104 arrows, 104 of them with an alert ⚠; grade A 0, B 41, C 63. Shown: the 12 strongest; 92 more arrows (92 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRRG2]] | B | ESRP1 activity raises PRRG2's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 3.41× lower at baseline in the lines without ESRP1 | 3e-05 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[SLC44A3]] | B | ESRP1 activity raises SLC44A3's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 3.69× lower at baseline in the lines without ESRP1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[FAM83E]] | B | ESRP1 activity raises FAM83E's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 4.61× lower at baseline in the lines without ESRP1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[TTC28]] | B | ESRP1 activity lowers TTC28's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 6.54× higher at baseline in the lines without ESRP1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[ARHGEF16]] | B | ESRP1 activity raises ARHGEF16's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 3.65× lower at baseline in the lines without ESRP1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[ELMO3]] | B | ESRP1 activity raises ELMO3's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 2.76× lower at baseline in the lines without ESRP1 | 1e-03 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[IL17RE]] | B | ESRP1 activity raises IL17RE's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 3.24× lower at baseline in the lines without ESRP1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[BNC2]] | B | ESRP1 activity lowers BNC2's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 6.60× higher at baseline in the lines without ESRP1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[SYTL1]] | B | ESRP1 activity raises SYTL1's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 3.13× lower at baseline in the lines without ESRP1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[LINC03041]] | B | ESRP1 activity lowers LINC03041's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 2.38× higher at baseline in the lines without ESRP1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[DLG3]] | B | ESRP1 activity raises DLG3's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 3.46× lower at baseline in the lines without ESRP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[TMEM51-AS1]] | B | ESRP1 activity raises TMEM51-AS1's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without ESRP1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.8, 55.2); signed map (58.1, 6.0). **Vector** length 104, 46.0% of its response variance represented; |z| ≥ 3 in 639 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +13.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +9.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.6 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +3.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.0 | +6.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -0.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | +1.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -5.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.6 | -4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -3.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.3 | -4.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.1 | -2.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | epithelial splicing regulatory protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:94,641,074-94,707,466 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20171; previously RBM35A |
| Gene groups (HGNC) | RNA binding motif containing; Epithelial splicing regulatory protein family |
| Reactome | 7 pathways, smallest: FGFR2 alternative splicing; Signaling by FGFR2; Signaling by BRAF and RAF1 fusions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NXG1](https://www.uniprot.org/uniprotkb/Q6NXG1) (Epithelial splicing regulatory protein 1):

> mRNA splicing factor that regulates the formation of epithelial cell-specific isoforms. Specifically regulates the expression of FGFR2-IIIb, an epithelial cell-specific isoform of FGFR2. Also regulates the splicing of CD44, CTNND1, ENAH, 3 transcripts that undergo changes in splicing during the epithelial-to-mesenchymal transition (EMT). Acts by directly binding specific sequences in mRNAs. Binds the GU-rich sequence motifs in the ISE/ISS-3, a cis-element regulatory region present in the mRNA …

**Summary**, from NCBI Gene [54845](https://www.ncbi.nlm.nih.gov/gene/54845):

> ESPR1 is an epithelial cell-type-specific splicing regulator (Warzecha et al., 2009 [PubMed 19285943]).[supplied by OMIM, Aug 2009]

**Accessions** — [HGNC:25966](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25966) · Entrez [54845](https://www.ncbi.nlm.nih.gov/gene/54845) · UniProt [Q6NXG1](https://www.uniprot.org/uniprotkb/Q6NXG1) · Ensembl [ENSG00000104413](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104413)

## Data

Gene col 2457: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2457); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2457, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2457]; `tensor/DDL_lfc|DDL_z.npy` [2457]; `embed/gene_vectors.npy` [2457]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2457 or target_col == 2457). Every well: [[ESRP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ESRP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
