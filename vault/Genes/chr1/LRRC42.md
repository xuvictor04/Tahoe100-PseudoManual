---
symbol: "LRRC42"
type: "gene"
col: 3777
ensembl_id: "ENSG00000116212"
name: "leucine rich repeat containing 42"
location: "1p32.3"
module: 85
arm: "+"
pooled_cpm: 28.76
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# LRRC42

*leucine rich repeat containing 42* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.23× (z +4.5, q 0.004, up in 17 of 48 measured lines) ⚠ unreliable plate only.
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.397× (z -28.5, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD27]] (+0.72, fdr 5e-05), [[TMUB1]] (+0.72, fdr 7e-06), [[SDHAP1]] (+0.71, fdr 1e-05); moves opposite to [[MMADHC-DT]] (-0.65, fdr 0.002, ⚠ one half only (not replicated)), [[PPP1R12A-AS2]] (-0.63, fdr 4e-04), [[LINC01004]] (-0.63, fdr 0.002, ⚠ one half only (not replicated)), [[BAZ2B]] (-0.63, fdr 2e-04), [[LPXN]] (-0.62, fdr 1e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3777.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +4.5 | 0.004 | 17/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.19× | +3.6 | 0.10 | 11/47 (C32, PANC-1, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.23 | 9/48 (NCI-H2030, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.0 | 0.23 | 12/47 (NCI-H1573, A-427, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.23 | 12/46 (SNU-423, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3777.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.397×** | -28.5 | 0e+00 | 41/47 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.526×** | -19.8 | 0e+00 | 42/47 (HS-578T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.484×** | -15.8 | 0e+00 | 35/47 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.518×** | -13.8 | 4e-41 | 35/48 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.560×** | -12.2 | 6e-32 | 37/46 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.598×** | -10.8 | 4e-25 | 35/48 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.647×** | -9.1 | 5e-18 | 25/36 (H4, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.700×** | -7.8 | 4e-13 | 25/42 (H4, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.726×** | -7.0 | 2e-10 | 28/47 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.728×** | -7.0 | 2e-10 | 24/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.803×** | -6.8 | 6e-10 | 24/48 (SNU-1, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.728×** | -6.4 | 7e-09 | 23/41 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.774×** | -5.6 | 9e-07 | 23/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -5.5 | 2e-06 | 23/48 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.801×** | -4.8 | 5e-05 | 19/48 (AsPC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.826×** | -4.0 | 0.002 | 14/48 (A-172, HS-578T, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.847× | -3.6 | 0.010 | 5/48 (LoVo, A498, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.892× | -3.5 | 0.013 | 12/48 (HOP62, HS-578T, …) | top dose only | position effect removed |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 0.872× | -3.0 | 0.082 | 6/48 (LoVo, SW 1088, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3777. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 40.7 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -23.3) |
| [[A498 (line)]] | wt | 33.1 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -13.5) |
| [[HS-578T (line)]] | alt | 47.2 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -16.8) |
| [[HOP62 (line)]] | alt | 29.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -13.3) |
| [[hTERT-HPNE (line)]] | wt | 25.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.5) |
| [[LoVo (line)]] | wt | 28.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -24.9) |
| [[NCI-H1792 (line)]] | alt | 26.5 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -13.3) |
| [[SW480 (line)]] | alt | 31.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -17.5) |
| [[CFPAC-1 (line)]] | alt | 33.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -14.0) |
| [[H4 (line)]] | wt | 37.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0748× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 33.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -11.0) |
| [[LS 180 (line)]] | wt | 26.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -18.1) |
| [[NCI-H2347 (line)]] | alt | 33.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -16.0) |
| [[Panc 03.27 (line)]] | alt | 31.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -15.4) |
| [[RKO (line)]] | wt | 27.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 37.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -14.0) |
| [[HCT15 (line)]] | alt | 38.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.295× (z -11.2) |
| [[Hs 766T (line)]] | wt | 39.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -11.9) |
| [[J82 (line)]] | alt | 31.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -18.2) |
| [[SNU-1 (line)]] | wt | 46.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.389× (z -9.0) |
| [[SW1417 (line)]] | alt | 45.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -14.9) |
| [[BT-474 (line)]] | alt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -10.6) |
| [[COLO 205 (line)]] | alt | 22.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -14.1) |
| [[HepG2_C3A (line)]] | wt | 29.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -8.6) |
| [[HT-29 (line)]] | alt | 23.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -10.5) |
| [[KATO III (line)]] | alt | 16.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 32.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.346× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 26.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -9.9) |
| [[SW 900 (line)]] | alt | 21.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -9.6) |
| [[SW48 (line)]] | wt | 29.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -11.3) |
| [[A-427 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3777), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD27]] | +0.72 | +0.74 / +0.40 | both halves | 5e-05 |  |
| [[TMUB1]] | +0.72 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[SDHAP1]] | +0.71 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[YIF1B]] | +0.70 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[RNF41]] | +0.70 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[MPST]] | +0.69 | +0.73 / +0.44 | both halves | 3e-05 |  |
| [[HSPB11]] | +0.68 | +0.70 / +0.48 | both halves | 2e-05 | ⚠ same locus (0.4 kb: neighbours can correlate without regulation) |
| [[SLC27A1]] | +0.67 | +0.69 / +0.31 | both halves | 2e-04 |  |
| [[MAST3]] | +0.67 | +0.64 / +0.29 | both halves | 2e-04 |  |
| [[SDHAP2]] | +0.67 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[LRFN3]] | +0.67 | +0.64 / +0.34 | both halves | 1e-04 |  |
| [[FHIP1B]] | +0.66 | +0.71 / +0.42 | both halves | 4e-05 |  |
| [[PCMT1]] | +0.65 | +0.69 / +0.25 | both halves | 4e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMADHC-DT]] | -0.65 | -0.73 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[PPP1R12A-AS2]] | -0.63 | -0.69 / -0.24 | both halves | 4e-04 |  |
| [[LINC01004]] | -0.63 | -0.69 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[BAZ2B]] | -0.63 | -0.67 / -0.32 | both halves | 2e-04 |  |
| [[LPXN]] | -0.62 | -0.65 / -0.35 | both halves | 1e-04 |  |
| [[CRPPA]] | -0.62 | -0.58 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[TIA1]] | -0.62 | -0.70 / -0.32 | both halves | 2e-04 |  |
| [[ARRDC3-AS1]] | -0.62 | -0.67 / -0.27 | both halves | 3e-04 |  |
| [[ERCC6L2]] | -0.61 | -0.64 / -0.30 | both halves | 2e-04 |  |
| [[ANXA2R-AS1]] | -0.61 | -0.65 / -0.31 | both halves | 2e-04 |  |
| [[ZNF341-AS1]] | -0.61 | -0.61 / -0.26 | both halves | 4e-04 |  |
| [[ZBED5]] | -0.61 | -0.67 / -0.25 | both halves | 4e-04 |  |
| [[ST7L]] | -0.60 | -0.68 / -0.23 | both halves | 5e-04 |  |
| [[ZNF462]] | -0.60 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[LINC01829]] | -0.59 | -0.60 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises LRRC42's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.734). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (1.5, -14.2); signed map (-38.8, 0.7). **Vector** length 90.0, 19.0% of its response variance represented; |z| ≥ 3 in 934 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.1 | +3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | -1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | -2.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.2 | -4.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | -1.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.0 | +1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +1.9 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -15.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -28.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.7 | -13.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 42 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:53,946,077-53,968,168 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC8974 |
| Matched by | ensembl_id |

UniProt [Q9Y546](https://www.uniprot.org/uniprotkb/Q9Y546) carries no function annotation.

**Summary**, from NCBI Gene [115353](https://www.ncbi.nlm.nih.gov/gene/115353):

> Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28792](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28792) · Entrez [115353](https://www.ncbi.nlm.nih.gov/gene/115353) · UniProt [Q9Y546](https://www.uniprot.org/uniprotkb/Q9Y546) · Ensembl [ENSG00000116212](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116212)

## Data

Gene col 3777: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3777); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3777, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3777]; `tensor/DDL_lfc|DDL_z.npy` [3777]; `embed/gene_vectors.npy` [3777]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3777 or target_col == 3777). Every well: [[LRRC42 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC42.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
