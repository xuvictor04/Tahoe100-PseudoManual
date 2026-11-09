---
symbol: "ANKRD7"
type: "gene"
col: 2707
ensembl_id: "ENSG00000106013"
name: "ankyrin repeat domain 7"
location: "7q31.31"
module: 26
arm: "+"
pooled_cpm: 6.48
n_lines_expressing: 39
n_dd_up: 35
n_dd_down: 7
n_dd_up_clean: 25
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 10
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# ANKRD7

*ankyrin repeat domain 7* — 7q31.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.17× (z +36.6, q 0e+00, up in 26 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Crizotinib (hydrochloride) (drug)]] 5 µM: 0.722× (z -4.0, q 0.016, down in 9 of 37 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAALC-AS1]] (+0.60, fdr 3e-05), [[LINC01482]] (+0.60, fdr 2e-05), [[NPR3]] (+0.60, fdr 1e-05); moves opposite to [[VIPR1]] (-0.50, fdr 8e-05), [[KIF3B]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 10 go from it, the strongest it → [[UPP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2707.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.17×** | +36.6 | 0e+00 | 26/27 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **6.09×** | +21.4 | 0e+00 | 29/32 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.89×** | +21.0 | 0e+00 | 27/30 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.98×** | +12.9 | 5e-36 | 3/10 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.62×** | +11.9 | 2e-30 | 21/32 (A-172, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.33×** | +10.0 | 1e-21 | 14/22 (CFPAC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.83×** | +7.4 | 8e-12 | 11/34 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +7.3 | 2e-11 | 2/12 (NCI-H2347, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.49×** | +7.0 | 2e-10 | 13/37 (A498, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.9 | 2e-10 | 7/36 (NCI-H2030, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +6.9 | 3e-10 | 13/35 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +6.4 | 8e-09 | 9/25 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +6.2 | 3e-08 | 10/29 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +6.1 | 4e-08 | 12/37 (NCI-H2347, SW 900, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.61×** | +5.6 | 6e-07 | 15/30 (LoVo, C32, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.55×** | +5.4 | 2e-06 | 9/31 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +5.2 | 5e-06 | 14/34 (NCI-H23, H4, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.002 | 9/34 (C32, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +3.9 | 0.002 | 10/32 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.26×** | +3.9 | 0.003 | 6/36 (SK-MEL-2, C32, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +3.8 | 0.003 | 7/35 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2707.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.722×** | -4.0 | 0.016 | 9/37 (C32, HOP62, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.714×** | -4.0 | 0.016 | 7/34 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.727×** | -3.9 | 0.016 | 13/27 (NCI-H1573, NCI-H23, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.747×** | -3.6 | 0.044 | 9/30 (NCI-H23, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.757×** | -3.4 | 0.057 | 9/35 (NCI-H23, C32, …) | rises with dose |  |
| [[crizotinib (drug)]] 5 µM |  | **0.749×** | -3.4 | 0.057 | 7/34 (RKO, LoVo, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | **0.764×** | -3.3 | 0.072 | 2/35 (LoVo, RPMI-7951) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.779× | -3.1 | 0.14 | 13/35 (C32, LOX-IMVI, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2707. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 41.0 | 0 | 7 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.108× (z -15.9) |
| [[C32 (line)]] | wt | 64.5 | 2 | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +9.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -12.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.230× (z -8.9) |
| [[A498 (line)]] | wt | 20.6 | 3 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.58× (z +19.3) | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -8.7) |
| [[A-172 (line)]] | wt | 8.15 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.88× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 1.94 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.8× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 14.5 | 2 | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.69× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.9) |
| [[HS-578T (line)]] | alt | 4.29 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 1.79 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 2.21 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 43.5× (z +14.7) | — |
| [[SW 900 (line)]] | alt | 7.44 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 5.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.65× (z +10.4) | — |
| [[COLO 205 (line)]] | alt | 6.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.7× (z +10.6) | — |
| [[LoVo (line)]] | wt | 2.45 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 34.4× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -10.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 2.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 3.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.21× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 3.75 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0332× (z -14.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 0.800 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.885 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.910 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.58 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2707), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAALC-AS1]] | +0.60 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[LINC01482]] | +0.60 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[NPR3]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PLD5P1]] | +0.59 | +0.40 / +0.57 | both halves | 4e-05 |  |
| [[TPTE2]] | +0.59 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[TMLHE-AS1]] | +0.59 | +0.56 / +0.26 | both halves | 4e-04 |  |
| [[CASC20]] | +0.59 | +0.53 / +0.37 | both halves | 8e-05 |  |
| [[SEC24B-AS1]] | +0.59 | +0.50 / +0.37 | both halves | 9e-05 |  |
| [[MAP7D2]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[LINC02641]] | +0.58 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[BVES-AS1]] | +0.58 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[MGC4859]] | +0.57 | +0.56 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VIPR1]] | -0.50 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[KIF3B]] | -0.49 | -0.38 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANKRD7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01358]] | B | LINC01358 activity raises ANKRD7's level | lines that do not express LINC01358 (14) vs lines expressing it (36) | 2.09× lower at baseline in the lines without LINC01358 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, BMPER, FRMD4A; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UPP2]] | B | ANKRD7 activity raises UPP2's level | lines that do not express ANKRD7 (11) vs lines expressing it (39) | 1.72× lower at baseline in the lines without ANKRD7 | 0.019 | ⚠ within organs, on part of the lines; also absent: PCDH15, LINC02398, ABCA12; maybe low, not absent |
| [[FRZB]] | B | ANKRD7 activity raises FRZB's level | lines that do not express ANKRD7 (11) vs lines expressing it (39) | 2.29× lower at baseline in the lines without ANKRD7 | 0.035 | ⚠ within organs, on part of the lines; also absent: PCDH15, LINC02398, ABCA12; maybe low, not absent |
| [[SNX31]] | B | ANKRD7 activity raises SNX31's level | lines that do not express ANKRD7 (11) vs lines expressing it (39) | 1.78× lower at baseline in the lines without ANKRD7 | 0.047 | ⚠ within organs, on part of the lines; also absent: PCDH15, LINC02398, ABCA12; maybe low, not absent |
| [[SLC26A7]] | B | ANKRD7 activity raises SLC26A7's level | lines that do not express ANKRD7 (11) vs lines expressing it (39) | 1.72× lower at baseline in the lines without ANKRD7 | 0.058 | ⚠ within organs, on part of the lines; also absent: PCDH15, LINC02398, ABCA12; maybe low, not absent |
| [[H2AZ1-DT]] | B | ANKRD7 activity raises H2AZ1-DT's level | lines that do not express ANKRD7 (11) vs lines expressing it (39) | 1.50× lower at baseline in the lines without ANKRD7 | 0.066 | ⚠ within organs, on part of the lines; also absent: PCDH15, LINC02398, ABCA12; maybe low, not absent |
| [[MEF2C-AS1]] | B | ANKRD7 activity raises MEF2C-AS1's level | lines that do not express ANKRD7 (11) vs lines expressing it (39) | 3.26× lower at baseline in the lines without ANKRD7 | 0.076 | ⚠ within organs, on part of the lines; also absent: PCDH15, LINC02398, ABCA12; maybe low, not absent |
| [[TPTE2]] | B | ANKRD7 activity raises TPTE2's level | lines that do not express ANKRD7 (11) vs lines expressing it (39) | 1.58× lower at baseline in the lines without ANKRD7 | 0.080 | ⚠ within organs, on part of the lines; also absent: PCDH15, LINC02398, ABCA12; maybe low, not absent |
| [[BAALC-AS1]] | B | ANKRD7 activity raises BAALC-AS1's level | lines that do not express ANKRD7 (11) vs lines expressing it (39) | 2.41× lower at baseline in the lines without ANKRD7 | 0.081 | ⚠ within organs, on part of the lines; also absent: PCDH15, LINC02398, ABCA12; maybe low, not absent |
| [[ARL10]] | B | ANKRD7 activity raises ARL10's level | lines that do not express ANKRD7 (11) vs lines expressing it (39) | 2.17× lower at baseline in the lines without ANKRD7 | 0.088 | ⚠ within organs, on part of the lines; also absent: PCDH15, LINC02398, ABCA12; maybe low, not absent |
| [[LINC02763]] | B | ANKRD7 activity raises LINC02763's level | lines that do not express ANKRD7 (11) vs lines expressing it (39) | 1.39× lower at baseline in the lines without ANKRD7 | 0.088 | ⚠ within organs, on part of the lines; also absent: PCDH15, LINC02398, ABCA12; maybe low, not absent |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (15.9, 18.8); signed map (21.1, 0.5). **Vector** length 64.3, 11.4% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +36.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +21.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +21.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +6.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +5.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -2.8 | -3.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.0 | -1.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.5 | -3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.3 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.2 | -3.4 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -1.1 | -4.0 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | +1.6 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.31 — chr7:118,214,669-118,496,171 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TSA806 |
| Gene groups (HGNC) | N-Ank proteins |
| Matched by | ensembl_id |

UniProt [Q92527](https://www.uniprot.org/uniprotkb/Q92527) carries no function annotation.

**Summary**, from NCBI Gene [56311](https://www.ncbi.nlm.nih.gov/gene/56311):

> Predicted to act upstream of or within blastocyst hatching. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18588](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18588) · Entrez [56311](https://www.ncbi.nlm.nih.gov/gene/56311) · UniProt [Q92527](https://www.uniprot.org/uniprotkb/Q92527) · Ensembl [ENSG00000106013](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106013)

## Data

Gene col 2707: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2707); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2707, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2707]; `tensor/DDL_lfc|DDL_z.npy` [2707]; `embed/gene_vectors.npy` [2707]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2707 or target_col == 2707). Every well: [[ANKRD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
