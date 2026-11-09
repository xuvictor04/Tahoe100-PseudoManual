---
symbol: "TMEM217"
type: "gene"
col: 10288
ensembl_id: "ENSG00000172738"
name: "transmembrane protein 217"
location: "6p21.2"
module: 35
arm: "+"
pooled_cpm: 6.7
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 10
n_dd_up_clean: 29
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# TMEM217

*transmembrane protein 217* — 6p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.13× (z +17.9, q 0e+00, up in 36 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.470× (z -6.8, q 7e-09, down in 26 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00863]] (+0.74, fdr 1e-05), [[PDCD6IP-DT]] (+0.74, fdr 7e-06), [[GSK3B-DT]] (+0.72, fdr 1e-05); moves opposite to [[BRAT1]] (-0.65, fdr 2e-05), [[PIP4P2]] (-0.65, fdr 1e-05), [[SPATA6]] (-0.64, fdr 2e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10288.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.13×** | +17.9 | 0e+00 | 36/38 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.19×** | +9.9 | 1e-20 | 32/46 (PANC-1, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.81×** | +9.2 | 5e-18 | 27/38 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +8.7 | 5e-16 | 22/37 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.32×** | +7.2 | 6e-11 | 22/36 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +6.4 | 2e-08 | 19/39 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +6.2 | 4e-08 | 8/18 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.64×** | +6.2 | 4e-08 | 21/45 (HT-29, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.87×** | +5.6 | 2e-06 | 21/44 (HCT15, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.74×** | +4.9 | 5e-05 | 13/42 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.73×** | +4.7 | 1e-04 | 19/43 (Panc 03.27, SHP-77, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.66×** | +4.5 | 3e-04 | 16/43 (Panc 03.27, HT-29, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.65×** | +4.5 | 3e-04 | 17/45 (Panc 03.27, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +4.4 | 4e-04 | 7/28 (HS-578T, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +4.2 | 0.001 | 2/13 (HS-578T, PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.60×** | +4.2 | 0.001 | 17/39 (HT-29, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.62×** | +4.1 | 0.001 | 15/40 (HT-29, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +3.8 | 0.004 | 17/45 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.54×** | +3.8 | 0.004 | 14/46 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10288.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.470×** | -6.8 | 7e-09 | 26/38 (SW480, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.553×** | -5.3 | 3e-05 | 23/38 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.602×** | -4.6 | 9e-04 | 17/47 (NCI-H1792, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.623×** | -4.3 | 0.003 | 24/47 (Panc 03.27, LoVo, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.643×** | -4.0 | 0.008 | 17/43 (NCI-H1792, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.742×** | -3.8 | 0.013 | 16/45 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Erlotinib (drug)]] 5 µM |  | **0.648×** | -3.7 | 0.014 | 16/42 (LoVo, A-427, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.756×** | -3.6 | 0.024 | 13/44 (A498, NCI-H2347, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.679×** | -3.5 | 0.031 | 17/46 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.696×** | -3.3 | 0.061 | 15/47 (COLO 205, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10288. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 19.4 | 0 | 3 (2 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.0843× (z -9.2) |
| [[PANC-1 (line)]] | alt | 5.26 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.89× (z +12.9) | [[Digitoxin (drug)]] 5 µM 0.0945× (z -11.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 7.99 | 0 | 2 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0826× (z -9.1) ⚠ transcription drop; unreliable plate only · without an alert: [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0696× (z -9.0) |
| [[HOP62 (line)]] | alt | 4.49 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.12× (z +10.5) | — |
| [[SW480 (line)]] | alt | 4.67 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +10.5) | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.134× (z -9.3) |
| [[A-172 (line)]] | wt | 4.61 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.5 µM 0.0620× (z -8.9) |
| [[C32 (line)]] | wt | 2.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.9× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.87× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 4.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.22× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 4.85 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.0782× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.119× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 6.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.12× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 20.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.06× (z +8.7) | — |
| [[RKO (line)]] | wt | 11.3 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0726× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 5.84 | 0 | 1 | — | [[Zileuton (drug)]] 0.5 µM 0.0459× (z -9.3) |
| [[SW1417 (line)]] | alt | 3.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.81× (z +9.9) | — |
| [[A-427 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10288), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00863]] | +0.74 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[PDCD6IP-DT]] | +0.74 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[GSK3B-DT]] | +0.72 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[LINC00571]] | +0.71 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[ZNF341-AS1]] | +0.69 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[CLIP1]] | +0.67 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[GARIN1A]] | +0.67 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[PBLD]] | +0.67 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[LINC01829]] | +0.66 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | +0.66 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[RNF103-CHMP3]] | +0.65 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[CCDC73]] | +0.65 | +0.58 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRAT1]] | -0.65 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[PIP4P2]] | -0.65 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[SPATA6]] | -0.64 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[FAM102B]] | -0.61 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[RSAD1]] | -0.61 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[SDHAF3]] | -0.61 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[IFT172]] | -0.60 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[THRA]] | -0.59 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[PIK3R2]] | -0.59 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[NBPF3]] | -0.59 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[ATG4C]] | -0.59 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ELP1]] | -0.58 | -0.50 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers TMEM217's level | compounds that target MAP2K1: 4 of 4 raise it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.2% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers TMEM217's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RBPMS]] | B | RBPMS activity raises TMEM217's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 1.53× lower at baseline in the lines without RBPMS | 0.078 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[LINC01829]] | C | LINC01829 activity lowers TMEM217's level | lines that do not express LINC01829 (3) vs lines expressing it (47) | 2.33× higher at baseline in the lines without LINC01829 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PARP11, GNG12-AS1, LINC02763; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (9.7, 10.5); signed map (22.6, -6.2). **Vector** length 104, 23.4% of its response variance represented; |z| ≥ 3 in 1,202 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +17.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.3 | +9.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +5.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +6.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.1 | +4.5 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -4.3 | -4.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.2 | -6.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.6 | -4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -3.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.1 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -3.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.6 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 217 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:37,212,180-37,258,155 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ355M6.2; previously C6orf128 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N7C4](https://www.uniprot.org/uniprotkb/Q8N7C4) (Transmembrane protein 217):

> Transmembrane protein essential for sperm motility and male fertility. Forms a complex with SLC9C1 in the flagellum, which regulates sperm motility by maintaining the stability of soluble adenylyl cyclase, which produces cAMP to power flagellar movement.

**Summary**, from NCBI Gene [221468](https://www.ncbi.nlm.nih.gov/gene/221468):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21238](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21238) · Entrez [221468](https://www.ncbi.nlm.nih.gov/gene/221468) · UniProt [Q8N7C4](https://www.uniprot.org/uniprotkb/Q8N7C4) · Ensembl [ENSG00000172738](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172738)

## Data

Gene col 10288: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10288); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10288, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10288]; `tensor/DDL_lfc|DDL_z.npy` [10288]; `embed/gene_vectors.npy` [10288]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10288 or target_col == 10288). Every well: [[TMEM217 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM217.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
