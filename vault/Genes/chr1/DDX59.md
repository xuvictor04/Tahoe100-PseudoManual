---
symbol: "DDX59"
type: "gene"
col: 3970
ensembl_id: "ENSG00000118197"
name: "DEAD-box helicase 59"
location: "1q32.1"
module: 46
arm: "+"
pooled_cpm: 26.16
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 21
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# DDX59

*DEAD-box helicase 59* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +10.8, q 1e-24, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.369× (z -20.4, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SENP8]] (+0.77, fdr 1e-05), [[FBXW4]] (+0.76, fdr 7e-06), [[TSTD3]] (+0.73, fdr 2e-05); moves opposite to [[FCHO1]] (-0.66, fdr 3e-05), [[SMYD3]] (-0.63, fdr 1e-04), [[CADM4]] (-0.62, fdr 1e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NOVA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3970.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +10.8 | 1e-24 | 33/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +6.1 | 3e-07 | 23/45 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 0.008 | 16/47 (C32, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.21×** | +3.5 | 0.064 | 9/48 (RKO, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.18× | +3.4 | 0.070 | 9/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.089 | 6/48 (RKO, SW 900, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.34× | +3.1 | 0.14 | 6/48 (A498, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3970.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.369×** | -20.4 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.410×** | -18.3 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.428×** | -17.4 | 0e+00 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.530×** | -13.0 | 1e-36 | 36/46 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.548×** | -12.3 | 8e-33 | 42/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.598×** | -10.5 | 5e-24 | 37/48 (NCI-H23, NCI-H460, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.605×** | -9.9 | 4e-21 | 35/46 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.655×** | -8.7 | 3e-16 | 26/46 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.770×** | -7.6 | 2e-12 | 27/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.772×** | -7.5 | 3e-12 | 25/47 (H4, PANC-1, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.706×** | -7.1 | 5e-11 | 30/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.716×** | -6.6 | 2e-09 | 24/48 (PANC-1, SNU-423, …) | top dose only | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.554×** | -6.3 | 1e-08 | 22/48 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.589×** | -5.7 | 6e-07 | 21/48 (NCI-H1792, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.763×** | -5.5 | 1e-06 | 19/48 (PANC-1, SK-MEL-2, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.810×** | -4.3 | 5e-04 | 19/47 (NCI-H2030, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.824×** | -4.0 | 0.002 | 17/46 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.706×** | -3.7 | 0.006 | 15/46 (SK-MEL-2, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[ML264 (drug)]] 0.05 µM |  | **0.829×** | -3.6 | 0.008 | 9/48 (HCT15, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3970. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 36.8 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.266× (z -16.2) |
| [[NCI-H460 (line)]] | wt | 38.8 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -16.5) |
| [[NCI-H23 (line)]] | alt | 32.6 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -12.1) |
| [[SW480 (line)]] | alt | 19.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.294× (z -12.0) |
| [[LoVo (line)]] | wt | 21.5 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.218× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 42.8 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.242× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 27.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -11.7) |
| [[A-427 (line)]] | wt | 29.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -10.2) |
| [[A-172 (line)]] | wt | 22.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.296× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 19.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.261× (z -8.8) |
| [[C32 (line)]] | wt | 84.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.342× (z -9.6) |
| [[Hs 766T (line)]] | wt | 28.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 17.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -9.7) |
| [[J82 (line)]] | alt | 23.1 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.320× (z -9.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.356× (z -8.8) |
| [[LS 180 (line)]] | wt | 18.4 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.246× (z -9.9) |
| [[SNU-423 (line)]] | alt | 25.4 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.307× (z -9.0) |
| [[H4 (line)]] | wt | 24.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -13.4) ⚠ cell-cycle shift, explains ~70% of this change |
| [[HEC-1-A (line)]] | alt | 28.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.406× (z -8.5) |
| [[HOP62 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.323× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[KATO III (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change |
| [[LOX-IMVI (line)]] | wt | 22.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 29.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.315× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 21.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.232× (z -9.8) |
| [[SHP-77 (line)]] | alt | 21.9 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.105× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 25.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -10.0) |
| [[SW 900 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.252× (z -8.6) ⚠ toxic |
| [[A498 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3970), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SENP8]] | +0.77 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[FBXW4]] | +0.76 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[TSTD3]] | +0.73 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[ANGEL2]] | +0.71 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[MFF-DT]] | +0.69 | +0.52 / +0.27 | both halves | 3e-04 |  |
| [[FAIM]] | +0.69 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[RNF146]] | +0.68 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[PBLD]] | +0.68 | +0.45 / +0.29 | both halves | 2e-04 |  |
| [[SEC24B-AS1]] | +0.68 | +0.55 / +0.39 | both halves | 5e-05 |  |
| [[PPP1R8]] | +0.68 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[ZNF460-AS1]] | +0.67 | +0.58 / +0.35 | both halves | 1e-04 |  |
| [[C2orf42]] | +0.65 | +0.53 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHO1]] | -0.66 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[SMYD3]] | -0.63 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[CADM4]] | -0.62 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[CMIP]] | -0.61 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[EDA]] | -0.61 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[ST3GAL5]] | -0.60 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[TNIK]] | -0.60 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[GDF11]] | -0.60 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[ATP1A3]] | -0.60 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[LRBA]] | -0.59 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[SH3PXD2B]] | -0.58 | -0.40 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOVA2]] | B | NOVA2 activity raises DDX59's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 1.34× lower at baseline in the lines without NOVA2 | 0.028 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[RAB39A]] | B | RAB39A activity raises DDX59's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 1.27× lower at baseline in the lines without RAB39A | 0.092 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.729). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-8.1, 15.8); signed map (24.2, -22.2). **Vector** length 90.4, 19.7% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +10.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.7 | +6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.1 | +4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +0.9 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -7.3 | -12.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.8 | -13.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.2 | -18.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -10.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.0 | -6.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.6 | -2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 59 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:200,623,896-200,669,907 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564B1023, ZNHIT5 |
| Gene groups (HGNC) | Zinc fingers HIT-type; DEAD-box helicases |
| Matched by | ensembl_id |

UniProt [Q5T1V6](https://www.uniprot.org/uniprotkb/Q5T1V6) carries no function annotation.

**Summary**, from NCBI Gene [83479](https://www.ncbi.nlm.nih.gov/gene/83479):

> Predicted to enable RNA helicase activity and mRNA binding activity. Located in nucleoplasm. Implicated in orofaciodigital syndrome V. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25360](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25360) · Entrez [83479](https://www.ncbi.nlm.nih.gov/gene/83479) · UniProt [Q5T1V6](https://www.uniprot.org/uniprotkb/Q5T1V6) · Ensembl [ENSG00000118197](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118197)

## Data

Gene col 3970: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3970); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3970, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3970]; `tensor/DDL_lfc|DDL_z.npy` [3970]; `embed/gene_vectors.npy` [3970]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3970 or target_col == 3970). Every well: [[DDX59 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX59.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
