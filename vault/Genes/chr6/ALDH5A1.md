---
symbol: "ALDH5A1"
type: "gene"
col: 3349
ensembl_id: "ENSG00000112294"
name: "aldehyde dehydrogenase 5 family member A1"
location: "6p22.3"
module: 18
arm: "+"
pooled_cpm: 10.26
n_lines_expressing: 43
n_dd_up: 15
n_dd_down: 34
n_dd_up_clean: 11
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ALDH5A1

*aldehyde dehydrogenase 5 family member A1* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.31× (z +15.2, q 0e+00, up in 26 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.38× (z +5.8, q 1e-06, up in 15 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.482× (z -13.0, q 1e-35, down in 32 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MEST]] (+0.68, fdr 7e-06), [[DHRS4L2]] (+0.64, fdr 1e-05), [[SPATA20]] (+0.64, fdr 8e-06); moves opposite to [[MFSD11]] (-0.58, fdr 5e-05), [[PTPRH]] (-0.55, fdr 1e-05), [[MIR22HG]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PRTG]] → it (grade B ⚠); 8 go from it, the strongest it → [[FAXC]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3349.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.31×** | +15.2 | 0e+00 | 26/29 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.37×** | +14.8 | 0e+00 | 18/18 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.42×** | +10.4 | 5e-23 | 19/23 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +5.8 | 1e-06 | 15/41 (KATO III, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +4.6 | 4e-04 | 17/41 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +4.5 | 6e-04 | 14/41 (NCI-H2347, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.90×** | +4.3 | 0.001 | 9/38 (J82, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +4.3 | 0.001 | 15/41 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +4.0 | 0.004 | 11/40 (HT-29, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.015 | 11/41 (SW1417, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.3 | 0.044 | 10/33 (MIA PaCa-2, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.050 | 12/41 (NCI-H1573, LoVo, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.057 | 11/41 (HT-29, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.057 | 8/41 (C32, PANC-1, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.059 | 2/41 (LoVo, KATO III) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3349.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.482×** | -13.0 | 1e-35 | 32/39 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.417×** | -11.0 | 1e-25 | 26/40 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.440×** | -9.9 | 7e-21 | 30/40 (SNU-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.458×** | -9.8 | 2e-20 | 27/39 (NCI-H23, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.490×** | -9.0 | 4e-17 | 29/41 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.500×** | -8.7 | 3e-16 | 24/41 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.539×** | -7.8 | 7e-13 | 27/41 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.528×** | -7.5 | 3e-12 | 25/38 (MIA PaCa-2, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.549×** | -7.5 | 4e-12 | 22/41 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.579×** | -6.8 | 5e-10 | 20/41 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.593×** | -6.5 | 3e-09 | 23/41 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.719×** | -5.8 | 3e-07 | 20/41 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.645×** | -5.5 | 2e-06 | 19/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.667×** | -5.1 | 2e-05 | 15/41 (SW 900, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -4.9 | 3e-05 | 20/39 (Panc 03.27, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.667×** | -4.9 | 4e-05 | 21/40 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.768×** | -4.6 | 1e-04 | 18/41 (MIA PaCa-2, CHP-212, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3349. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 21.4 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 14.1 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 5.83× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -15.9) |
| [[SNU-1 (line)]] | wt | 41.6 | 0 | 7 | — | [[Harringtonine (drug)]] 5 µM 0.0891× (z -14.0) |
| [[J82 (line)]] | alt | 26.2 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 5.19× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -13.4) |
| [[SW480 (line)]] | alt | 17.3 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.259× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -9.8) |
| [[RKO (line)]] | wt | 19.9 | 0 | 4 | — | [[Harringtonine (drug)]] 0.5 µM 0.156× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 18.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.193× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 16.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -11.2) |
| [[A-427 (line)]] | wt | 25.9 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.311× (z -13.2) |
| [[A549 (line)]] | wt | 8.87 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0719× (z -13.1) |
| [[BT-474 (line)]] | alt | 8.74 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -8.7) |
| [[HT-29 (line)]] | alt | 5.57 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0885× (z -9.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 14.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 6.23 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 8.79 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -11.9) |
| [[SW48 (line)]] | wt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -8.9) |
| [[A-172 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3349), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEST]] | +0.68 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[DHRS4L2]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[SPATA20]] | +0.64 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[NUP210]] | +0.63 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[PON2]] | +0.63 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ADAM22]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[RAVER2]] | +0.61 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[B3GALNT1]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[DHX15]] | +0.61 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[FAM98B]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[TTPA]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[DHX9]] | +0.60 | +0.55 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD11]] | -0.58 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[PTPRH]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[MIR22HG]] | -0.54 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[C9orf24]] | -0.54 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[TPT1-AS1]] | -0.53 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[VRK3]] | -0.51 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SELENOK]] | -0.51 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[FBXL12]] | -0.50 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[RNF181]] | -0.50 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[PMM1]] | -0.50 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[ZBTB43]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[NIT1]] | -0.49 | -0.39 / -0.46 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRTG]] | B | PRTG activity raises ALDH5A1's level | lines that do not express PRTG (14) vs lines expressing it (36) | 1.28× lower at baseline in the lines without PRTG | 0.027 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[SEPTIN3]] | B | SEPTIN3 activity raises ALDH5A1's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 1.39× lower at baseline in the lines without SEPTIN3 | 0.077 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[EMID1]] | B | EMID1 activity raises ALDH5A1's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 1.67× lower at baseline in the lines without EMID1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[NUP210]] | C | NUP210 activity raises ALDH5A1's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 2.86× lower at baseline in the lines without NUP210 | 0.012 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A; co-absent with the target |
| [[FOXRED2]] | C | FOXRED2 activity raises ALDH5A1's level | lines that do not express FOXRED2 (3) vs lines expressing it (47) | 4.22× lower at baseline in the lines without FOXRED2 | 0.018 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: BRME1, NRTN, CSRP1-AS1; maybe low, not absent |
| [[GPLD1]] | C | GPLD1 activity raises ALDH5A1's level | lines that do not express GPLD1 (5) vs lines expressing it (45) | 3.98× lower at baseline in the lines without GPLD1 | 0.022 | ⚠ within organs, on part of the lines; also absent: PDE5A, ALDH5A1, CCDC144CP; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAXC]] | B | ALDH5A1 activity raises FAXC's level | lines that do not express ALDH5A1 (7) vs lines expressing it (43) | 2.18× lower at baseline in the lines without ALDH5A1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CMTM8, CXCL16, PRKCZ; its own permutation p |
| [[MIR22HG]] | B | ALDH5A1 activity lowers MIR22HG's level | lines that do not express ALDH5A1 (7) vs lines expressing it (43) | 1.61× higher at baseline in the lines without ALDH5A1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CMTM8, CXCL16, PRKCZ; its own permutation p |
| [[FN3K]] | B | ALDH5A1 activity raises FN3K's level | lines that do not express ALDH5A1 (7) vs lines expressing it (43) | 2.12× lower at baseline in the lines without ALDH5A1 | 0.078 | ⚠ within organs, on part of the lines; also absent: CMTM8, CXCL16, PRKCZ |
| [[DHX9]] | B | ALDH5A1 activity raises DHX9's level | lines that do not express ALDH5A1 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without ALDH5A1 | 0.089 | ⚠ within organs, on part of the lines; also absent: CMTM8, CXCL16, PRKCZ; its own permutation p |
| [[G3BP1]] | B | ALDH5A1 activity raises G3BP1's level | lines that do not express ALDH5A1 (7) vs lines expressing it (43) | 1.20× lower at baseline in the lines without ALDH5A1 | 0.089 | ⚠ within organs, on part of the lines; also absent: CMTM8, CXCL16, PRKCZ; its own permutation p |
| [[SPATA20]] | B | ALDH5A1 activity raises SPATA20's level | lines that do not express ALDH5A1 (7) vs lines expressing it (43) | 1.40× lower at baseline in the lines without ALDH5A1 | 0.096 | ⚠ within organs, on part of the lines; also absent: CMTM8, CXCL16, PRKCZ |
| [[NUP210]] | C | ALDH5A1 activity raises NUP210's level | lines that do not express ALDH5A1 (7) vs lines expressing it (43) | 5.39× lower at baseline in the lines without ALDH5A1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CMTM8, CXCL16, PRKCZ; co-absent with the target; its own permutation p |
| [[GPLD1]] | C | ALDH5A1 activity raises GPLD1's level | lines that do not express ALDH5A1 (7) vs lines expressing it (43) | 2.40× lower at baseline in the lines without ALDH5A1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CMTM8, CXCL16, PRKCZ; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.426). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-27.6, 23.8); signed map (15.8, -43.4). **Vector** length 75.6, 14.6% of its response variance represented; |z| ≥ 3 in 1,064 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +14.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +4.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.9 | +5.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.9 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +4.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.7 | +3.3 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -3.5 | -4.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.0 | -2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.3 | -11.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.2 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -4.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | aldehyde dehydrogenase 5 family member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:24,494,867-24,537,207 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SSADH, SSDH |
| Gene groups (HGNC) | Aldehyde dehydrogenases |
| Reactome | 4 pathways, smallest: GABA synthesis, release, reuptake and degradation; Neurotransmitter release cycle; Transmission across Chemical Synapses |
| Matched by | ensembl_id |

**Function**, from UniProt [P51649](https://www.uniprot.org/uniprotkb/P51649) (Succinate-semialdehyde dehydrogenase, mitochondrial):

> Catalyzes one step in the degradation of the inhibitory neurotransmitter gamma-aminobutyric acid (GABA).

**Summary**, from NCBI Gene [7915](https://www.ncbi.nlm.nih.gov/gene/7915):

> This protein belongs to the aldehyde dehydrogenase family of proteins. This gene encodes a mitochondrial NAD(+)-dependent succinic semialdehyde dehydrogenase. A deficiency of this enzyme, known as 4-hydroxybutyricaciduria, is a rare inborn error in the metabolism of the neurotransmitter 4-aminobutyric acid (GABA). In response to the defect, physiologic fluids from patients accumulate GHB, a compound with numerous neuromodulatory properties. Two transcript variants encoding distinct isoforms …

**Accessions** — [HGNC:408](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:408) · Entrez [7915](https://www.ncbi.nlm.nih.gov/gene/7915) · UniProt [P51649](https://www.uniprot.org/uniprotkb/P51649) · Ensembl [ENSG00000112294](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112294)

## Data

Gene col 3349: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3349); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3349, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3349]; `tensor/DDL_lfc|DDL_z.npy` [3349]; `embed/gene_vectors.npy` [3349]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3349 or target_col == 3349). Every well: [[ALDH5A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDH5A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
