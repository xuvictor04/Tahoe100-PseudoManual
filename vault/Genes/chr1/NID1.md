---
symbol: "NID1"
type: "gene"
col: 3859
ensembl_id: "ENSG00000116962"
name: "nidogen 1"
location: "1q42.3"
module: 54
arm: "-"
pooled_cpm: 34.6
n_lines_expressing: 30
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# NID1

*nidogen 1* — 1q42.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.26× (z +36.5, q 0e+00, up in 27 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.598× (z -7.3, q 2e-10, down in 19 of 28 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEPTIN11]] (+0.64, fdr 1e-05), [[ATN1]] (+0.60, fdr 2e-05), [[ITGAV]] (+0.59, fdr 1e-05); moves opposite to [[PET117]] (-0.66, fdr 3e-04), [[MRPS26]] (-0.64, fdr 1e-04), [[RPP21]] (-0.63, fdr 3e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[COL7A1]] → it (grade C ⚠); 3 go from it, the strongest it → [[RPL17]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3859.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.26×** | +36.5 | 0e+00 | 27/28 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.41×** | +17.2 | 0e+00 | 26/26 (SW480, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +10.8 | 8e-25 | 21/24 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +10.2 | 2e-22 | 23/25 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +9.0 | 4e-17 | 15/27 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +8.6 | 1e-15 | 16/27 (AsPC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +8.0 | 1e-13 | 16/28 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +6.7 | 1e-09 | 18/25 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +5.4 | 5e-06 | 18/28 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.31×** | +3.7 | 0.011 | 15/26 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.30×** | +3.6 | 0.014 | 12/26 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.29×** | +3.5 | 0.019 | 14/28 (SW480, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.29×** | +3.4 | 0.025 | 12/26 (NCI-H460, SW480, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.4 | 0.025 | 6/21 (HOP62, HEC-1-A, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3859.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.598×** | -7.3 | 2e-10 | 19/28 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.642×** | -6.0 | 4e-07 | 18/26 (J82, C-33 A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.678×** | -5.3 | 2e-05 | 20/26 (hTERT-HPNE, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.699×** | -5.1 | 5e-05 | 15/28 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.792×** | -4.7 | 3e-04 | 13/28 (Panc 03.27, A498, …) | rises with dose | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.723×** | -4.6 | 4e-04 | 15/28 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.722×** | -4.3 | 0.002 | 13/26 (A-172, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.767×** | -3.8 | 0.011 | 16/28 (SW 1088, HOP62, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.777×** | -3.6 | 0.021 | 13/27 (SW480, SW 1271, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.786×** | -3.4 | 0.033 | 13/27 (J82, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.799×** | -3.2 | 0.067 | 12/28 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.800×** | -3.2 | 0.067 | 11/27 (HOP62, hTERT-HPNE, …) | two highest doses | position effect removed |
| [[Terfenadine (drug)]] 5 µM |  | 0.863× | -3.0 | 0.12 | 7/28 (A498, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3859. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 27.7 | 12 (6 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 31.9× (z +42.3) | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 14.8 | 13 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 185× (z +35.8) | — |
| [[HEC-1-A (line)]] | alt | 95.3 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +22.4) | — |
| [[AsPC-1 (line)]] | alt | 21.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 60.1× (z +31.0) | — |
| [[PANC-1 (line)]] | alt | 32.8 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +40.9) | — |
| [[C32 (line)]] | wt | 19.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.3× (z +29.9) | — |
| [[NCI-H2347 (line)]] | alt | 62.3 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +22.2) | [[Harringtonine (drug)]] 0.5 µM 0.344× (z -10.3) |
| [[HOP62 (line)]] | alt | 65.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.80× (z +26.2) | — |
| [[C-33 A (line)]] | alt | 82.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.20× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.170× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 54.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +20.3) | — |
| [[RPMI-7951 (line)]] | alt | 120 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.9× (z +36.8) | — |
| [[SW 900 (line)]] | alt | 48.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +33.2) | — |
| [[A-172 (line)]] | wt | 159 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +26.7) | — |
| [[CFPAC-1 (line)]] | alt | 24.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +16.8) | — |
| [[H4 (line)]] | wt | 41.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.96× (z +18.0) | — |
| [[J82 (line)]] | alt | 60.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +18.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.295× (z -10.2) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 25.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.91× (z +18.3) | — |
| [[SNU-423 (line)]] | alt | 56.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +19.6) | — |
| [[A-427 (line)]] | wt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +12.4) | — |
| [[A498 (line)]] | wt | 137 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +19.2) | — |
| [[A549 (line)]] | wt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.7× (z +21.2) | — |
| [[hTERT-HPNE (line)]] | wt | 88.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.231× (z -9.7) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +20.2) | — |
| [[AN3 CA (line)]] | alt | 4.75 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 87.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.10 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3859), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*31 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN11]] | +0.64 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ATN1]] | +0.60 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[ITGAV]] | +0.59 | +0.51 / +0.52 | both halves | 1e-05 | pathway: Extracellular matrix organization; STRING 568 |
| [[THOC6]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[TUG1]] | +0.58 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[MYO1C]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[COL4A1]] | +0.57 | +0.43 / +0.61 | both halves | 3e-05 | pathway: Degradation of the extracellular matrix; STRING 855 |
| [[CHD4]] | +0.56 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[LAMC1]] | +0.56 | +0.36 / +0.56 | both halves | 9e-05 | pathway: Degradation of the extracellular matrix; STRING 997 |
| [[NR2F1-AS1]] | +0.55 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[RGL2]] | +0.55 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[RAB1B]] | +0.55 | +0.33 / +0.50 | both halves | 1e-04 |  |

## Genes that move opposite

*69 of its nearest partners move opposite, 6 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PET117]] | -0.66 | -0.29 / -0.69 | both halves | 3e-04 |  |
| [[MRPS26]] | -0.64 | -0.34 / -0.65 | both halves | 1e-04 |  |
| [[RPP21]] | -0.63 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[NOL7]] ⚠ | -0.59 | -0.35 / -0.56 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[LAMTOR5]] | -0.59 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[GTF2H2]] | -0.59 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[POP7]] | -0.59 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[ZNHIT3]] | -0.58 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ATP5MJ]] | -0.58 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[MRPL34]] | -0.58 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[CAMLG]] | -0.57 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[CRYZL1]] | -0.57 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[GTF2H2B]] | -0.57 | -0.52 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL7A1]] | C | COL7A1 activity raises NID1's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 4.59× lower at baseline in the lines without COL7A1 | 0.021 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPL17]] | B | NID1 activity lowers RPL17's level | lines that do not express NID1 (20) vs lines expressing it (30) | 1.39× higher at baseline in the lines without NID1 | 0.093 | ⚠ within organs, on part of the lines; also absent: COL4A2, FBXO17, COL4A1 |
| [[COL4A2]] | C | NID1 activity raises COL4A2's level | lines that do not express NID1 (20) vs lines expressing it (30) | 6.62× lower at baseline in the lines without NID1 | 0.026 | ⚠ within organs, on part of the lines; also absent: COL4A2, FBXO17, COL4A1; co-absent with the target |
| [[COL4A1]] | C | NID1 activity raises COL4A1's level | lines that do not express NID1 (20) vs lines expressing it (30) | 5.31× lower at baseline in the lines without NID1 | 0.075 | ⚠ within organs, on part of the lines; also absent: COL4A2, FBXO17, COL4A1; co-absent with the target |

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.694). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.3, -14.4); signed map (13.8, -10.1). **Vector** length 88.8, 23.0% of its response variance represented; |z| ≥ 3 in 761 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.2 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.9 | +10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.9 | +36.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.7 | +17.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.4 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -7.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -2.1 | -3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.6 | -3.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | nidogen 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.3 — chr1:235,975,830-236,065,109 (-) |
| Ensembl biotype | protein_coding |
| Also known as | entactin; previously NID |
| Reactome | 3 pathways, smallest: Laminin interactions; Degradation of the extracellular matrix; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P14543](https://www.uniprot.org/uniprotkb/P14543) (Nidogen-1):

> Sulfated glycoprotein widely distributed in basement membranes and tightly associated with laminin. Also binds to collagen IV and perlecan. It probably has a role in cell-extracellular matrix interactions.

**Summary**, from NCBI Gene [4811](https://www.ncbi.nlm.nih.gov/gene/4811):

> This gene encodes a member of the nidogen family of basement membrane glycoproteins. The protein interacts with several other components of basement membranes, and may play a role in cell interactions with the extracellular matrix. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7821](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7821) · Entrez [4811](https://www.ncbi.nlm.nih.gov/gene/4811) · UniProt [P14543](https://www.uniprot.org/uniprotkb/P14543) · Ensembl [ENSG00000116962](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116962)

## Data

Gene col 3859: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3859); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3859, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3859]; `tensor/DDL_lfc|DDL_z.npy` [3859]; `embed/gene_vectors.npy` [3859]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3859 or target_col == 3859). Every well: [[NID1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NID1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
