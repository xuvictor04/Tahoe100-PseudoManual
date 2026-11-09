---
symbol: "SNX33"
type: "gene"
col: 10403
ensembl_id: "ENSG00000173548"
name: "sorting nexin 33"
location: "15q24.2"
module: 20
arm: "+"
pooled_cpm: 18.31
n_lines_expressing: 48
n_dd_up: 0
n_dd_down: 31
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# SNX33

*sorting nexin 33* — 15q24.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.157× (z -29.8, q 0e+00, down in 43 of 44 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LLGL1]] (+0.52, fdr 2e-05), [[KCTD10]] (+0.52, fdr 1e-05), [[STK35]] (+0.51, fdr 1e-05); moves opposite to [[RALGAPA1]] (-0.55, fdr 1e-05), [[THOC2]] (-0.55, fdr 3e-05), [[FAM193A]] (-0.50, fdr 2e-04).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC2A1]] → it (grade C ⚠); 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10403.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.157×** | -29.8 | 0e+00 | 43/44 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.188×** | -19.1 | 0e+00 | 41/43 (hTERT-HPNE, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.202×** | -18.2 | 0e+00 | 45/46 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.179×** | -17.3 | 0e+00 | 42/45 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.224×** | -17.1 | 0e+00 | 43/45 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.323×** | -12.9 | 5e-36 | 44/46 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.379×** | -11.1 | 1e-26 | 39/46 (NCI-H460, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.384×** | -10.9 | 8e-26 | 40/44 (NCI-H460, LS 180, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.447×** | -8.1 | 3e-14 | 32/40 (NCI-H460, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.452×** | -8.0 | 8e-14 | 23/28 (Hs 766T, A549, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **0.493×** | -7.7 | 8e-13 | 25/34 (Panc 03.27, Hs 766T, …) | all doses, flat | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.518×** | -7.5 | 3e-12 | 37/45 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.496×** | -7.4 | 6e-12 | 23/31 (Panc 03.27, LOX-IMVI, …) | all doses, flat | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.518×** | -6.6 | 1e-09 | 27/39 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.569×** | -6.1 | 4e-08 | 22/45 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.605×** | -5.7 | 3e-07 | 26/46 (LOX-IMVI, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.676×** | -4.5 | 2e-04 | 22/45 (HOP62, H4, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.680×** | -4.1 | 9e-04 | 19/44 (HOP62, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.704×** | -4.0 | 0.002 | 19/44 (HOP62, J82, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.786×** | -3.9 | 0.002 | 19/45 (SK-MEL-2, A-172, …) | rises with dose | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **0.748×** | -3.3 | 0.020 | 12/45 (HOP62, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.770×** | -3.0 | 0.059 | 10/46 (CHP-212, NCI-H2347, …) | top dose only |  |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.766×** | -2.9 | 0.074 | 12/45 (LS 180, A-172, …) | inconsistent across doses |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.841× | -2.8 | 0.098 | 10/45 (HepG2/C3A, A498, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.59 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10403. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.3 | 0 | 14 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0313× (z -24.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0452× (z -22.2) |
| [[HOP62 (line)]] | alt | 29.7 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0381× (z -30.5) |
| [[LOX-IMVI (line)]] | wt | 27.3 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0537× (z -24.3) |
| [[Hs 766T (line)]] | wt | 33.1 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -19.0) |
| [[HEC-1-A (line)]] | alt | 19.1 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -20.9) |
| [[hTERT-HPNE (line)]] | wt | 34.5 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0123× (z -23.5) |
| [[J82 (line)]] | alt | 39.1 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0883× (z -17.6) |
| [[A549 (line)]] | wt | 30.7 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -18.7) |
| [[H4 (line)]] | wt | 32.7 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0680× (z -17.1) |
| [[Panc 03.27 (line)]] | alt | 21.6 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0696× (z -16.4) |
| [[SNU-423 (line)]] | alt | 32.6 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0819× (z -15.3) |
| [[A-172 (line)]] | wt | 44.1 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0960× (z -17.7) |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0936× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 31.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0295× (z -22.8) |
| [[AsPC-1 (line)]] | alt | 15.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0709× (z -19.6) |
| [[CFPAC-1 (line)]] | alt | 19.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -18.1) |
| [[NCI-H2347 (line)]] | alt | 18.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0948× (z -21.6) |
| [[PANC-1 (line)]] | alt | 22.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -24.4) |
| [[RPMI-7951 (line)]] | alt | 30.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0512× (z -23.7) |
| [[SW480 (line)]] | alt | 6.75 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -16.2) |
| [[HS-578T (line)]] | alt | 16.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -17.1) |
| [[HT-29 (line)]] | alt | 13.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -14.8) |
| [[KATO III (line)]] | alt | 16.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -15.6) |
| [[LoVo (line)]] | wt | 10.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -11.1) |
| [[C-33 A (line)]] | alt | 13.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0732× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0863× (z -10.1) |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0453× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.213× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0724× (z -10.8) |
| [[RKO (line)]] | wt | 13.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -9.9) |
| [[SHP-77 (line)]] | alt | 8.93 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0874× (z -12.9) |
| [[SK-MEL-2 (line)]] | alt | 9.83 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0617× (z -10.8) |
| [[SW 900 (line)]] | alt | 6.87 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -10.3) |
| [[A498 (line)]] | wt | 20.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -8.5) |
| [[BT-474 (line)]] | alt | 6.45 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -9.6) |
| [[C32 (line)]] | wt | 12.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -11.1) |
| [[HCT15 (line)]] | alt | 9.03 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0826× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HepG2_C3A (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0838× (z -9.4) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 7.61 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0773× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[NCI-H2030 (line)]] | alt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0927× (z -19.0) |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -16.6) |
| [[A-427 (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10403), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LLGL1]] | +0.52 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[KCTD10]] | +0.52 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[STK35]] | +0.51 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[MLF2]] | +0.51 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[MAPK7]] | +0.51 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[USF1]] | +0.50 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[SPATA2]] | +0.49 | +0.38 / +0.43 | both halves | 6e-05 |  |
| [[CHSY1]] | +0.49 | +0.56 / +0.40 | both halves | 4e-05 |  |
| [[MTFR1L]] | +0.49 | +0.44 / +0.37 | both halves | 7e-05 |  |
| [[SLC2A1]] | +0.49 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[PPFIA4]] | +0.49 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[EIF1AD]] | +0.48 | +0.52 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALGAPA1]] | -0.55 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[THOC2]] | -0.55 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[FAM193A]] | -0.50 | -0.43 / -0.29 | both halves | 2e-04 |  |
| [[XIAP]] | -0.49 | -0.57 / -0.18 | ⚠ one half (not replicated) | 0.001 |  |
| [[BRAF]] | -0.49 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[CLASP2]] | -0.49 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[SCMH1]] | -0.48 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[FNDC3A]] | -0.47 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[AHI1]] | -0.47 | -0.60 / -0.41 | both halves | 4e-05 | same gene group |
| [[CUX1]] | -0.46 | -0.60 / -0.27 | both halves | 3e-04 |  |
| [[EXOC6]] | -0.46 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[PIGL]] | -0.46 | -0.54 / -0.37 | both halves | 7e-05 |  |
| [[USP34]] | -0.46 | -0.21 / -0.33 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC2A1]] | C | SLC2A1 activity raises SNX33's level | lines that do not express SLC2A1 (4) vs lines expressing it (46) | 3.10× lower at baseline in the lines without SLC2A1 | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | SNX33's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | SNX33's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.60 | 0.491 over the table, 0.077 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.261). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-17.8, -55.1); signed map (-24.3, 3.4). **Vector** length 73.3, 16.6% of its response variance represented; |z| ≥ 3 in 1,195 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | -0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +3.5 | -3.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.2 | +0.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | -0.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +2.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | -4.4 | -7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | -4.1 | -8.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.7 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -19.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -3.6 | -10.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.5 | -1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.2 — chr15:75,647,912-75,662,301 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC32065, SH3PXD3C, SNX30; previously SH3PX3 |
| Gene groups (HGNC) | PX-BAR domain containing; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WV41](https://www.uniprot.org/uniprotkb/Q8WV41) (Sorting nexin-33):

> Plays a role in the reorganization of the cytoskeleton, endocytosis and cellular vesicle trafficking via its interactions with membranes, WASL, DNM1 and DNM2. Acts both during interphase and at the end of mitotic cell divisions. Required for efficient progress through mitosis and cytokinesis. Required for normal formation of the cleavage furrow at the end of mitosis. Modulates endocytosis of cell-surface proteins, such as APP and PRNP; this then modulates the secretion of APP and PRNP peptides. …

**Summary**, from NCBI Gene [257364](https://www.ncbi.nlm.nih.gov/gene/257364):

> The protein encoded by this gene is involved in cytoskeletal reorganization, vesicle trafficking, endocytosis, and mitosis. The encoded protein is essential for the creation of the cleavage furrow during mitosis and for completion of mitosis. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:28468](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28468) · Entrez [257364](https://www.ncbi.nlm.nih.gov/gene/257364) · UniProt [Q8WV41](https://www.uniprot.org/uniprotkb/Q8WV41) · Ensembl [ENSG00000173548](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173548)

## Data

Gene col 10403: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10403); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10403, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10403]; `tensor/DDL_lfc|DDL_z.npy` [10403]; `embed/gene_vectors.npy` [10403]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10403 or target_col == 10403). Every well: [[SNX33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
