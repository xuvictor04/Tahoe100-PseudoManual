---
symbol: "GTF2A1"
type: "gene"
col: 9118
ensembl_id: "ENSG00000165417"
name: "general transcription factor IIA subunit 1"
location: "14q31.1"
module: 25
arm: "+"
pooled_cpm: 52.71
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# GTF2A1

*general transcription factor IIA subunit 1* — 14q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.73× (z +14.4, q 1e-44, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.675× (z -7.3, q 2e-10, down in 33 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.748× (z -5.4, q 2e-05, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRELID3B]] (+0.66, fdr 1e-05), [[GTF2H3]] (+0.63, fdr 1e-05), [[ZBTB37]] (+0.63, fdr 7e-06); moves opposite to [[HIGD2A]] (-0.64, fdr 1e-05), [[COPS9]] (-0.56, fdr 1e-05), [[SNHG25]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9118.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +14.4 | 1e-44 | 40/48 (AsPC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +8.2 | 9e-14 | 36/48 (SNU-423, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +7.9 | 6e-13 | 36/48 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +7.7 | 3e-12 | 37/48 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +7.6 | 3e-12 | 35/48 (RKO, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +7.6 | 3e-12 | 31/48 (J82, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +7.3 | 2e-11 | 31/48 (RKO, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +7.2 | 5e-11 | 34/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +6.9 | 2e-10 | 34/48 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +5.7 | 8e-07 | 30/48 (RKO, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +4.6 | 2e-04 | 28/48 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~8% of this change | **1.21×** | +3.6 | 0.017 | 14/47 (RPMI-7951, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +3.4 | 0.027 | 21/43 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.055 | 14/47 (HS-578T, SW 900, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.065 | 18/49 (COLO 205, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.065 | 6/48 (SW480, SW 900, …) | inconsistent across doses | position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.096 | 7/48 (NCI-H2030, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9118.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.675×** | -7.3 | 2e-10 | 33/47 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.748×** | -5.4 | 2e-05 | 25/48 (BT-474, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.763×** | -4.8 | 3e-04 | 24/48 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.788×** | -4.4 | 0.001 | 23/48 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.791×** | -4.3 | 0.002 | 25/48 (SW48, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.818×** | -3.7 | 0.019 | 19/48 (C-33 A, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.824×** | -3.6 | 0.024 | 21/48 (SW48, NCI-H2030, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.819×** | -3.6 | 0.024 | 23/48 (C32, SW48, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.825×** | -3.6 | 0.024 | 17/47 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~8% of this change | **0.823×** | -3.5 | 0.030 | 19/47 (MIA PaCa-2, H4, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.750× | -3.1 | 0.11 | 15/48 (HS-578T, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9118. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 46.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +18.2) | — |
| [[RKO (line)]] | wt | 71.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +17.5) | — |
| [[COLO 205 (line)]] | alt | 64.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +15.6) | — |
| [[SW48 (line)]] | wt | 68.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.212× (z -11.6) |
| [[C32 (line)]] | wt | 73.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -8.5) |
| [[LS 180 (line)]] | wt | 40.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.369× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change |
| [[MIA PaCa-2 (line)]] | alt | 63.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +8.8) ⚠ cell-cycle shift, explains ~12% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.384× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~8% of this change |
| [[NCI-H1573 (line)]] | alt | 60.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.406× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 59.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +13.6) | — |
| [[SHP-77 (line)]] | alt | 48.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0932× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change |
| [[SK-MEL-2 (line)]] | alt | 58.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +15.9) | — |
| [[A-427 (line)]] | wt | 84.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -11.5) |
| [[BT-474 (line)]] | alt | 53.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.244× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 43.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +13.5) | — |
| [[CHP-212 (line)]] | wt | 43.6 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.109× (z -9.7) |
| [[HOP62 (line)]] | alt | 43.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 49.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 38.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +8.5) | — |
| [[J82 (line)]] | alt | 40.1 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.05× (z +9.4) | — |
| [[KATO III (line)]] | alt | 47.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +13.7) | — |
| [[LOX-IMVI (line)]] | wt | 37.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 39.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.14× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 69.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.0) | — |
| [[PANC-1 (line)]] | alt | 54.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 51.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.55× (z +8.9) | — |
| [[SW 1271 (line)]] | alt | 53.2 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0808× (z -8.8) |
| [[SW 900 (line)]] | alt | 67.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.3) | — |
| [[SW1417 (line)]] | alt | 49.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +14.0) | — |
| [[SW480 (line)]] | alt | 73.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.1) | — |
| [[A-172 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9118), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRELID3B]] | +0.66 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[GTF2H3]] | +0.63 | +0.63 / +0.57 | both halves | 1e-05 | pathway: HIV Infection; STRING 989 |
| [[ZBTB37]] | +0.63 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ZNF510]] | +0.61 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[GMFB]] | +0.60 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[AKAP11]] | +0.59 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[FAM114A2]] | +0.59 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[BBS10]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[IPO8]] | +0.58 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[DNAJA2]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[ALG10]] | +0.57 | +0.39 / +0.64 | both halves | 6e-05 |  |
| [[ZNF816]] | +0.57 | +0.64 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIGD2A]] | -0.64 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[COPS9]] | -0.56 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[SNHG25]] | -0.55 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[HIC2]] | -0.55 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[NDUFA4]] | -0.54 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[UBL5]] | -0.54 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[NDUFA1]] | -0.54 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[ATP5MG]] | -0.53 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[MZT2B]] | -0.53 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[ZBTB20-AS5]] | -0.53 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[C2]] | -0.53 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[RPS19]] | -0.53 | -0.41 / -0.56 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GTF2A1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.502). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-31.8, -17.0); signed map (0.6, -35.9). **Vector** length 105, 25.4% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.2 | +8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.2 | +7.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.8 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +14.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +5.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.2 | +2.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.5 | -7.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.9 | -5.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.8 | -4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.3 | -3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.6 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -0.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIA subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q31.1 — chr14:81,175,452-81,221,377 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TFIIA |
| Gene groups (HGNC) | General transcription factor IIA complex subunits; Small nucleolar RNA protein coding host genes |
| Reactome | 16 pathways, smallest: HIV Transcription Initiation; RNA Polymerase II HIV Promoter Escape; RNA Polymerase II Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [P52655](https://www.uniprot.org/uniprotkb/P52655) (Transcription initiation factor IIA subunit 1):

> TFIIA is a component of the transcription machinery of RNA polymerase II and plays an important role in transcriptional activation. TFIIA in a complex with TBP mediates transcriptional activity.

**Summary**, from NCBI Gene [2957](https://www.ncbi.nlm.nih.gov/gene/2957):

> Accurate transcription initiation on TATA-containing class II genes involves the ordered assembly of RNA polymerase II (POLR2A; MIM 180660) and several general initiation factors (summarized by DeJong and Roeder, 1993 [PubMed 8224848]). One of these factors is TFIIA, which when purified from HeLa extracts consists of 35-, 19-, and 12-kD subunits.[supplied by OMIM, Jul 2010]

**Accessions** — [HGNC:4646](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4646) · Entrez [2957](https://www.ncbi.nlm.nih.gov/gene/2957) · UniProt [P52655](https://www.uniprot.org/uniprotkb/P52655) · Ensembl [ENSG00000165417](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165417)

## Data

Gene col 9118: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9118); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9118, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9118]; `tensor/DDL_lfc|DDL_z.npy` [9118]; `embed/gene_vectors.npy` [9118]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9118 or target_col == 9118). Every well: [[GTF2A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
