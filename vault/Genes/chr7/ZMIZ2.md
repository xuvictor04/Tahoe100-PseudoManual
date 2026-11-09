---
symbol: "ZMIZ2"
type: "gene"
col: 4347
ensembl_id: "ENSG00000122515"
name: "zinc finger MIZ-type containing 2"
location: "7p13"
module: 2
arm: "+"
pooled_cpm: 49.98
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ZMIZ2

*zinc finger MIZ-type containing 2* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.10× (z +18.6, q 0e+00, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.647× (z -10.9, q 5e-25, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCTD17]] (+0.62, fdr 2e-05), [[AGRN]] (+0.62, fdr 8e-06), [[BCAM]] (+0.59, fdr 2e-05); moves opposite to [[TIRAP]] (-0.63, fdr 3e-05), [[METTL4]] (-0.61, fdr 3e-05), [[TCEANC2]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TSPAN15]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4347.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.10×** | +18.6 | 0e+00 | 36/47 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.37×** | +15.2 | 0e+00 | 48/48 (HS-578T, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.38×** | +14.8 | 0e+00 | 44/48 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.29×** | +14.6 | 0e+00 | 48/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.24×** | +14.3 | 3e-44 | 46/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +9.3 | 2e-18 | 38/48 (NCI-H2347, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +6.8 | 1e-09 | 31/48 (RPMI-7951, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +4.9 | 6e-05 | 28/48 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +4.8 | 1e-04 | 24/49 (HEC-1-A, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +4.5 | 4e-04 | 23/48 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +4.3 | 8e-04 | 20/48 (HT-29, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 0.001 | 23/47 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.002 | 19/48 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.003 | 20/48 (A498, H4, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.21×** | +3.3 | 0.031 | 11/49 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.038 | 14/48 (PANC-1, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.057 | 13/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4347.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.647×** | -10.9 | 5e-25 | 38/48 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.744×** | -5.0 | 2e-04 | 28/48 (PANC-1, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[NG25 (drug)]] 5 µM |  | **0.640×** | -4.1 | 0.007 | 21/47 (NCI-H460, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.808×** | -3.8 | 0.021 | 19/48 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.813×** | -3.7 | 0.027 | 22/48 (C32, NCI-H2347, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.876× | -3.3 | 0.077 | 20/48 (NCI-H2347, HS-578T, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 0.837× | -3.2 | 0.13 | 16/48 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 0.721× | -3.0 | 0.17 | 19/43 (A498, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4347. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 79.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +18.4) | — |
| [[HOP62 (line)]] | alt | 33.4 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +15.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -8.6) |
| [[HS-578T (line)]] | alt | 42.8 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +11.7) | [[Selinexor (drug)]] 5 µM 0.432× (z -9.9) ⚠ cell-cycle shift, explains ~15% of this change |
| [[A498 (line)]] | wt | 57.0 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +16.8) | [[Bortezomib (drug)]] 5 µM 0.146× (z -9.1) ⚠ toxic |
| [[KATO III (line)]] | alt | 39.2 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 4.10× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -8.8) |
| [[HT-29 (line)]] | alt | 31.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +12.0) | — |
| [[RPMI-7951 (line)]] | alt | 72.3 | 3 | 1 | [[Harringtonine (drug)]] 5 µM 3.69× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -11.2) |
| [[SW480 (line)]] | alt | 57.4 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.10× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -16.6) |
| [[A-172 (line)]] | wt | 58.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +17.3) | — |
| [[H4 (line)]] | wt | 52.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +12.8) | — |
| [[hTERT-HPNE (line)]] | wt | 33.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0903× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 80.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.3) | [[Selinexor (drug)]] 5 µM 0.533× (z -10.3) ⚠ cell-cycle shift, explains ~15% of this change |
| [[NCI-H460 (line)]] | wt | 57.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -17.2) |
| [[SHP-77 (line)]] | alt | 33.8 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.99× (z +10.8) | — |
| [[SW 900 (line)]] | alt | 58.4 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -8.5) |
| [[SW1417 (line)]] | alt | 73.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +17.2) | — |
| [[A549 (line)]] | wt | 41.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.109× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 71.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.0) | — |
| [[J82 (line)]] | alt | 46.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +15.5) | — |
| [[Panc 03.27 (line)]] | alt | 87.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 88.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -10.7) |
| [[SNU-423 (line)]] | alt | 41.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +12.7) | — |
| [[BT-474 (line)]] | alt | 58.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +12.5) | — |
| [[C32 (line)]] | wt | 47.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 28.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 34.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.26× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 80.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -8.5) |
| [[LoVo (line)]] | wt | 43.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.45× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 90.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -17.3) |
| [[NCI-H1792 (line)]] | alt | 54.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -15.0) |
| [[PANC-1 (line)]] | alt | 47.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -12.8) |
| [[SW48 (line)]] | wt | 61.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +9.6) | — |
| [[A-427 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4347), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD17]] | +0.62 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[AGRN]] | +0.62 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[BCAM]] | +0.59 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[PLCD3]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[SDC4]] | +0.58 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[C15orf39]] | +0.57 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[TNKS1BP1]] | +0.57 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[RING1]] | +0.56 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[MFSD12]] | +0.56 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[JUNB]] | +0.55 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[NFKBIE]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[GGA1]] | +0.55 | +0.42 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIRAP]] | -0.63 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[METTL4]] | -0.61 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[TCEANC2]] | -0.58 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[MTRF1]] | -0.57 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[ISY1]] | -0.56 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[LRRC41]] | -0.55 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[COA6]] | -0.55 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ZNF460-AS1]] | -0.55 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[YARS2]] | -0.54 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[MRPL18]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[NSD3]] | -0.53 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[PSMB5]] | -0.53 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN15]] | B | TSPAN15 activity raises ZMIZ2's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 1.40× lower at baseline in the lines without TSPAN15 | 0.020 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[IER3]] | B | IER3 activity raises ZMIZ2's level | lines that do not express IER3 (5) vs lines expressing it (45) | 2.10× lower at baseline in the lines without IER3 | 0.028 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[HMSD]] | B | HMSD activity lowers ZMIZ2's level | lines that do not express HMSD (26) vs lines expressing it (24) | 1.21× higher at baseline in the lines without HMSD | 0.044 | ⚠ within organs, on part of the lines; also absent: LGSN, LRRN2, HEYL |
| [[PMEPA1]] | B | PMEPA1 activity raises ZMIZ2's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 1.77× lower at baseline in the lines without PMEPA1 | 0.046 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[PSMB5]] | B | PSMB5 activity raises ZMIZ2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SIGIRR]] | B | SIGIRR activity raises ZMIZ2's level | lines that do not express SIGIRR (9) vs lines expressing it (41) | 1.50× lower at baseline in the lines without SIGIRR | 0.073 | ⚠ within organs, on part of the lines; also absent: CLCF1, LTBR, MYOF |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.336). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-2.2, 21.4); signed map (-6.8, 28.5). **Vector** length 116, 30.6% of its response variance represented; |z| ≥ 3 in 1,099 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.0 | +14.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.6 | +14.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.6 | +14.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +9.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.7 | +15.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +3.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.6 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.6 | -10.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.3 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.4 | -3.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -5.0 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -1.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger MIZ-type containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:44,748,581-44,769,881 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1886, hZIMP7, ZIMP7, DKFZp761I2123, NET27 |
| Gene groups (HGNC) | Zinc fingers MIZ-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NF64](https://www.uniprot.org/uniprotkb/Q8NF64) (Zinc finger MIZ domain-containing protein 2):

> Increases ligand-dependent transcriptional activity of AR and other nuclear hormone receptors.

**Summary**, from NCBI Gene [83637](https://www.ncbi.nlm.nih.gov/gene/83637):

> ZMIZ2 and ZMIZ1 (MIM 607159) are members of a PIAS (see MIM 603566)-like family of proteins that interact with nuclear hormone receptors. ZMIZ2 interacts with androgen receptor (AR; MIM 313700) and enhances AR-mediated transcription (Huang et al., 2005 [PubMed 16051670]).[supplied by OMIM, May 2010]

**Accessions** — [HGNC:22229](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22229) · Entrez [83637](https://www.ncbi.nlm.nih.gov/gene/83637) · UniProt [Q8NF64](https://www.uniprot.org/uniprotkb/Q8NF64) · Ensembl [ENSG00000122515](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122515)

## Data

Gene col 4347: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4347); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4347, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4347]; `tensor/DDL_lfc|DDL_z.npy` [4347]; `embed/gene_vectors.npy` [4347]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4347 or target_col == 4347). Every well: [[ZMIZ2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZMIZ2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
