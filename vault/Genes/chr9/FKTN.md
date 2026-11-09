---
symbol: "FKTN"
type: "gene"
col: 2797
ensembl_id: "ENSG00000106692"
name: "fukutin"
location: "9q31.2"
module: 1
arm: "+"
pooled_cpm: 47.19
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# FKTN

*fukutin* — 9q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.65× (z +7.8, q 4e-12, up in 31 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.29× (z +4.0, q 0.010, up in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 3.51×, LoVo 2.66×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 3.02×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.438× (z -18.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRP15]] (+0.79, fdr 7e-06), [[AGK]] (+0.77, fdr 7e-06), [[FARSB]] (+0.75, fdr 7e-06); moves opposite to [[NARF]] (-0.76, fdr 7e-06), [[TESK2]] (-0.68, fdr 1e-05), [[CDK2AP2]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2797.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 3.51×, LoVo 2.66×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 3.02×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +7.8 | 4e-12 | 31/42 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.29×** | +5.7 | 3e-06 | 26/48 (AsPC-1, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +5.3 | 3e-05 | 27/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.010 | 23/48 (SW480, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.017 | 18/48 (Hs 766T, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.26× | +3.2 | 0.13 | 14/48 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.24× | +3.2 | 0.13 | 17/45 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2797.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.438×** | -18.9 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.386×** | -15.4 | 0e+00 | 43/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.454×** | -12.8 | 3e-35 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.534×** | -10.2 | 3e-22 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.575×** | -9.0 | 3e-17 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.573×** | -8.7 | 3e-16 | 31/48 (SW480, SNU-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -7.2 | 5e-11 | 32/48 (SW48, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.707×** | -5.6 | 1e-06 | 31/48 (SW480, SHP-77, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.699×** | -5.6 | 1e-06 | 24/47 (J82, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.787×** | -3.4 | 0.045 | 19/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.821×** | -3.2 | 0.066 | 9/48 (SW1417, PANC-1, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.875× | -3.1 | 0.097 | 6/48 (NCI-H2347, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.877× | -3.0 | 0.11 | 14/48 (SNU-1, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2797. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 50.4 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -20.0) |
| [[J82 (line)]] | alt | 70.0 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 73.0 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -14.4) |
| [[HT-29 (line)]] | alt | 32.2 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -12.9) |
| [[PANC-1 (line)]] | alt | 53.7 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.314× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.331× (z -13.2) |
| [[RKO (line)]] | wt | 105 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -17.6) |
| [[SNU-1 (line)]] | wt | 74.5 | 0 | 5 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.265× (z -14.5) |
| [[COLO 205 (line)]] | alt | 33.5 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -11.4) |
| [[HOP62 (line)]] | alt | 34.5 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -12.3) |
| [[LoVo (line)]] | wt | 29.9 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.66× (z +8.7) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.307× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -11.0) |
| [[HCT15 (line)]] | alt | 45.7 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.224× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 82.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -19.8) |
| [[RPMI-7951 (line)]] | alt | 70.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -13.3) |
| [[SHP-77 (line)]] | alt | 45.3 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.271× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 69.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +11.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -11.9) |
| [[SNU-423 (line)]] | alt | 49.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -11.1) |
| [[SW1417 (line)]] | alt | 35.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -12.7) |
| [[A-427 (line)]] | wt | 40.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.02× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 37.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.224× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 57.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 34.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -13.2) |
| [[SW48 (line)]] | wt | 37.5 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -9.5) |
| [[A549 (line)]] | wt | 40.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -9.6) |
| [[AN3 CA (line)]] | alt | 60.4 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.111× (z -12.0) |
| [[C32 (line)]] | wt | 41.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 25.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -9.9) |
| [[H4 (line)]] | wt | 45.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -14.0) |
| [[Hs 766T (line)]] | wt | 59.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.322× (z -9.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 28.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -8.6) |
| [[KATO III (line)]] | alt | 37.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -13.0) |
| [[LS 180 (line)]] | wt | 32.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 54.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 59.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.353× (z -10.0) |
| [[SW 1271 (line)]] | alt | 74.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 65.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 125 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2797), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP15]] | +0.79 | +0.75 / +0.79 | both halves | 7e-06 |  |
| [[AGK]] | +0.77 | +0.63 / +0.83 | both halves | 7e-06 | STRING 436 |
| [[FARSB]] | +0.75 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[N6AMT1]] | +0.72 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[DRG2]] | +0.72 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[MAK16]] | +0.71 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[CCT2]] | +0.71 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[DPH6]] | +0.70 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[MRRF]] | +0.70 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[GTF2H3]] | +0.69 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[NAA15]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[IMPACT]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NARF]] | -0.76 | -0.72 / -0.75 | both halves | 7e-06 |  |
| [[TESK2]] | -0.68 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[CDK2AP2]] | -0.68 | -0.49 / -0.75 | both halves | 1e-05 |  |
| [[ZNHIT1]] | -0.66 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[KMT5C]] | -0.65 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[NDUFA2]] | -0.64 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[TAF5]] | -0.63 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[TSC22D4]] | -0.63 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[SSR4]] | -0.62 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[RAB40C]] | -0.61 | -0.56 / -0.71 | both halves | 1e-05 |  |
| [[GNAS]] | -0.60 | -0.66 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FKTN's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.775). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.3, -39.3); signed map (0.6, -38.6). **Vector** length 105, 28.4% of its response variance represented; |z| ≥ 3 in 918 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.3 | +2.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +5.0 | +5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +3.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | -0.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.8 | -18.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -8.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -7.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -15.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -5.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.6 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | fukutin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.2 — chr9:105,558,122-105,653,820 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LGMD2M; previously FCMD |
| Reactome | 3 pathways, smallest: Matriglycan biosynthesis on DAG1; DAG1 glycosylations; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O75072](https://www.uniprot.org/uniprotkb/O75072) (Ribitol-5-phosphate transferase FKTN):

> Catalyzes the transfer of a ribitol-phosphate from CDP-ribitol to the distal N-acetylgalactosamine of the phosphorylated O-mannosyl trisaccharide (N-acetylgalactosamine-beta-3-N-acetylglucosamine-beta-4-(phosphate-6-)mannose), a carbohydrate structure present in alpha-dystroglycan (DAG1). This constitutes the first step in the formation of the ribitol 5-phosphate tandem repeat which links the phosphorylated O-mannosyl trisaccharide to the ligand binding moiety composed of repeats of …

**Summary**, from NCBI Gene [2218](https://www.ncbi.nlm.nih.gov/gene/2218):

> The protein encoded by this gene is a putative transmembrane protein that is localized to the cis-Golgi compartment, where it may be involved in the glycosylation of alpha-dystroglycan in skeletal muscle. The encoded protein is thought to be a glycosyltransferase and could play a role in brain development. Defects in this gene are a cause of Fukuyama-type congenital muscular dystrophy (FCMD), Walker-Warburg syndrome (WWS), limb-girdle muscular dystrophy type 2M (LGMD2M), and dilated …

**Accessions** — [HGNC:3622](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3622) · Entrez [2218](https://www.ncbi.nlm.nih.gov/gene/2218) · UniProt [O75072](https://www.uniprot.org/uniprotkb/O75072) · Ensembl [ENSG00000106692](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106692)

## Data

Gene col 2797: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2797); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2797, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2797]; `tensor/DDL_lfc|DDL_z.npy` [2797]; `embed/gene_vectors.npy` [2797]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2797 or target_col == 2797). Every well: [[FKTN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FKTN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
