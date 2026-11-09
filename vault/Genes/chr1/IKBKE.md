---
symbol: "IKBKE"
type: "gene"
col: 15415
ensembl_id: "ENSG00000263528"
name: "inhibitor of nuclear factor kappa B kinase subunit epsilon"
location: "1q32.1"
module: 14
arm: "+"
pooled_cpm: 14.75
n_lines_expressing: 46
n_dd_up: 9
n_dd_down: 34
n_dd_up_clean: 9
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 15
direction_downstream: 8
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# IKBKE

*inhibitor of nuclear factor kappa B kinase subunit epsilon* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 3.40× (z +14.5, q 4e-45, up in 36 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.365× (z -12.5, q 5e-33, down in 40 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[S100A3]] (+0.67, fdr 1e-05), [[ZNF620]] (+0.65, fdr 7e-06), [[BCL3]] (+0.65, fdr 7e-06); moves opposite to [[MTFR1]] (-0.58, fdr 1e-05), [[DCUN1D2]] (-0.58, fdr 3e-05), [[MFN1]] (-0.56, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[GBP5]] → it (grade B ⚠); 8 go from it, the strongest it → [[GBP2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15415.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **3.40×** | +14.5 | 4e-45 | 36/42 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.25×** | +14.1 | 6e-43 | 33/42 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +6.7 | 5e-09 | 21/40 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +5.1 | 4e-05 | 21/40 (A549, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.51×** | +5.1 | 4e-05 | 21/42 (A-172, A549, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.019 | 12/43 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.019 | 17/44 (AsPC-1, A549, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.036 | 13/42 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.056 | 10/44 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15415.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.365×** | -12.5 | 5e-33 | 40/43 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.383×** | -11.9 | 4e-30 | 34/41 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.402×** | -11.3 | 3e-27 | 36/43 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.439×** | -10.2 | 3e-22 | 28/42 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.471×** | -9.3 | 1e-18 | 30/42 (SW480, COLO 205, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.471×** | -9.3 | 1e-18 | 32/42 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.493×** | -8.8 | 1e-16 | 26/43 (A498, SNU-423, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.502×** | -8.6 | 8e-16 | 30/41 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.620×** | -8.4 | 3e-15 | 25/40 (SW480, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.534×** | -7.8 | 4e-13 | 28/42 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.535×** | -7.5 | 4e-12 | 25/36 (Hs 766T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.555×** | -7.3 | 1e-11 | 24/43 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.559×** | -7.2 | 3e-11 | 27/43 (SW480, COLO 205, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.544×** | -7.1 | 4e-11 | 23/41 (COLO 205, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.630×** | -5.7 | 4e-07 | 20/43 (SNU-423, CFPAC-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.656×** | -5.2 | 6e-06 | 24/43 (Panc 03.27, SW480, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.450×** | -5.2 | 8e-06 | 19/41 (A498, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.661×** | -5.1 | 9e-06 | 23/43 (H4, HEC-1-A, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.774×** | -4.5 | 2e-04 | 17/44 (Panc 03.27, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15415. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.9 | 0 | 16 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0514× (z -25.5) |
| [[COLO 205 (line)]] | alt | 32.9 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0365× (z -24.5) |
| [[HEC-1-A (line)]] | alt | 43.8 | 1 | 9 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0845× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 31.6 | 0 | 5 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0778× (z -14.9) |
| [[A-172 (line)]] | wt | 13.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +13.4) | — |
| [[SNU-423 (line)]] | alt | 36.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.168× (z -11.1) |
| [[H4 (line)]] | wt | 14.0 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0881× (z -9.4) |
| [[Hs 766T (line)]] | wt | 25.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0938× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 8.98 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.138× (z -9.0) |
| [[J82 (line)]] | alt | 10.7 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.22× (z +15.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.124× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 35.8 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -10.9) |
| [[HOP62 (line)]] | alt | 13.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.74× (z +16.4) | — |
| [[NCI-H460 (line)]] | wt | 5.72 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +10.3) | [[Digitoxin (drug)]] 0.5 µM 0.170× (z -9.1) |
| [[SNU-1 (line)]] | wt | 10.2 | 0 | 2 | — | [[Digitoxin (drug)]] 0.05 µM 0.0358× (z -9.8) |
| [[A-427 (line)]] | wt | 4.76 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0450× (z -11.2) |
| [[A498 (line)]] | wt | 21.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.210× (z -9.5) |
| [[A549 (line)]] | wt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 4.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +10.9) | — |
| [[C32 (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.124× (z -9.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0815× (z -9.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 9.99 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0527× (z -10.1) |
| [[HT-29 (line)]] | alt | 8.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 1 | — | [[Clofarabine (drug)]] 0.5 µM 0.105× (z -8.5) |
| [[LoVo (line)]] | wt | 7.53 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 15.1× (z +13.1) | — |
| [[LOX-IMVI (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -9.0) ⚠ cell-cycle shift, explains ~17% of this change |
| [[LS 180 (line)]] | wt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 18.3 | 0 | 1 | — | [[venetoclax (drug)]] 5 µM 0.0452× (z -9.5) |
| [[SHP-77 (line)]] | alt | 5.56 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0301× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 14.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -10.9) |
| [[SW1417 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -10.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15415), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[S100A3]] | +0.67 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[ZNF620]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[BCL3]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 | same gene group; STRING 413 |
| [[IL4I1]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[TIFA]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 | pathway: MyD88-independent TLR4 cascade |
| [[STAT5A]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[TNFAIP2]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[STAP2]] | +0.63 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[NFKBIE]] | +0.63 | +0.66 / +0.63 | both halves | 7e-06 | STRING 453 |
| [[CCL5]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 | STRING 473 |
| [[REPIN1]] | +0.62 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[CCL2]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTFR1]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[DCUN1D2]] | -0.58 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[MFN1]] | -0.56 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[BCAP31]] | -0.55 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[TIMM10B]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[DIP2A]] | -0.54 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[FAM20B]] | -0.54 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[CDC42BPB]] | -0.54 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[TPD52L2]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[NIPA2]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[SLC41A3]] | -0.53 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[CPSF4]] | -0.53 | -0.61 / -0.35 | both halves | 1e-04 | pathway: Dengue Virus-Host Interactions |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 13, C 2. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP5]] | B | GBP5 activity raises IKBKE's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 1.95× lower at baseline in the lines without GBP5 | 8e-04 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |
| [[GATA6]] | B | GATA6 activity raises IKBKE's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 2.02× lower at baseline in the lines without GATA6 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[IL15]] | B | IL15 activity raises IKBKE's level | lines that do not express IL15 (10) vs lines expressing it (40) | 2.65× lower at baseline in the lines without IL15 | 0.010 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[SLC43A3]] | B | SLC43A3 activity raises IKBKE's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 1.84× lower at baseline in the lines without SLC43A3 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261 |
| [[GBP1]] | B | GBP1 activity raises IKBKE's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.02× lower at baseline in the lines without GBP1 | 0.017 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[GBP2]] | B | GBP2 activity raises IKBKE's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.36× lower at baseline in the lines without GBP2 | 0.017 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[STING1]] | B | STING1 activity raises IKBKE's level | lines that do not express STING1 (17) vs lines expressing it (33) | 1.72× lower at baseline in the lines without STING1 | 0.038 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |
| [[DMRTA1]] | B | DMRTA1 activity raises IKBKE's level | lines that do not express DMRTA1 (19) vs lines expressing it (31) | 1.84× lower at baseline in the lines without DMRTA1 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC01239, CFAP20DC, NALCN |
| [[STAT5A]] | B | STAT5A activity raises IKBKE's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.69× lower at baseline in the lines without STAT5A | 0.050 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[MAML2]] | B | MAML2 activity raises IKBKE's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 2.40× lower at baseline in the lines without MAML2 | 0.068 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[TRIP6]] | B | TRIP6 activity raises IKBKE's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 2.00× lower at baseline in the lines without TRIP6 | 0.070 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[PSTPIP2]] | B | PSTPIP2 activity raises IKBKE's level | lines that do not express PSTPIP2 (20) vs lines expressing it (30) | 1.48× lower at baseline in the lines without PSTPIP2 | 0.075 | ⚠ within organs, on part of the lines; also absent: NEDD9, CARD11, BCAT1 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP2]] | C | IKBKE activity raises GBP2's level | lines that do not express IKBKE (4) vs lines expressing it (46) | 5.62× lower at baseline in the lines without IKBKE | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SP100, NAT1, NDRG1; its own permutation p |
| [[TIFA]] | C | IKBKE activity raises TIFA's level | lines that do not express IKBKE (4) vs lines expressing it (46) | 2.01× lower at baseline in the lines without IKBKE | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SP100, NAT1, NDRG1; its own permutation p |
| [[EBI3]] | C | IKBKE activity lowers EBI3's level | lines that do not express IKBKE (4) vs lines expressing it (46) | 1.81× higher at baseline in the lines without IKBKE | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SP100, NAT1, NDRG1; its own permutation p |
| [[KLC1]] | C | IKBKE activity raises KLC1's level | lines that do not express IKBKE (4) vs lines expressing it (46) | 1.30× lower at baseline in the lines without IKBKE | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SP100, NAT1, NDRG1; its own permutation p |
| [[NINJ1]] | C | IKBKE activity raises NINJ1's level | lines that do not express IKBKE (4) vs lines expressing it (46) | 2.64× lower at baseline in the lines without IKBKE | 0.085 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SP100, NAT1, NDRG1 |
| [[DZIP3]] | C | IKBKE activity lowers DZIP3's level | lines that do not express IKBKE (4) vs lines expressing it (46) | 2.29× higher at baseline in the lines without IKBKE | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SP100, NAT1, NDRG1; its own permutation p |
| [[DPY19L2P2]] | C | IKBKE activity lowers DPY19L2P2's level | lines that do not express IKBKE (4) vs lines expressing it (46) | 2.11× higher at baseline in the lines without IKBKE | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SP100, NAT1, NDRG1; its own permutation p |
| [[PER2]] | C | IKBKE activity raises PER2's level | lines that do not express IKBKE (4) vs lines expressing it (46) | 2.09× lower at baseline in the lines without IKBKE | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SP100, NAT1, NDRG1 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.2, 5.9); signed map (43.7, 5.9). **Vector** length 112, 29.9% of its response variance represented; |z| ≥ 3 in 1,138 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *IkBA variant leads to EDA-ID* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +11.3 | +14.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +11.1 | +14.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.1 | +6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +3.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +5.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.8 | -11.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.3 | -9.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.7 | -5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -12.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.6 | -7.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.6 | -5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -7.8 |

## What is on record

|  |  |
|---|---|
| Name | inhibitor of nuclear factor kappa B kinase subunit epsilon |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:206,470,476-206,496,889 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IKKE, IKK-i, KIAA0151 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; I kappa B kinase family |
| Reactome | 36 pathways, smallest: Regulation of TBK1, IKKε-mediated activation of IRF3, IRF7 upon TLR3 ligation; SUMOylation of immune response proteins; Regulation of TBK1, IKKε (IKBKE)-mediated activation of IRF3, IRF7 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14164](https://www.uniprot.org/uniprotkb/Q14164) (Inhibitor of nuclear factor kappa-B kinase subunit epsilon):

> Serine/threonine kinase that plays an essential role in regulating inflammatory responses to viral infection, through the activation of the type I IFN, NF-kappa-B and STAT signaling. Also involved in TNFA and inflammatory cytokines, like Interleukin-1, signaling. Following activation of viral RNA sensors, such as RIG-I-like receptors, associates with DDX3X and phosphorylates interferon regulatory factors (IRFs), IRF3 and IRF7, as well as DDX3X. This activity allows subsequent homodimerization …

**Summary**, from NCBI Gene [9641](https://www.ncbi.nlm.nih.gov/gene/9641):

> IKBKE is a noncanonical I-kappa-B (see MIM 164008) kinase (IKK) that is essential for regulating antiviral signaling pathways. IKBKE has also been identified as a breast cancer (MIM 114480) oncogene and is amplified and overexpressed in over 30% of breast carcinomas and breast cancer cell lines (Hutti et al., 2009 [PubMed 19481526]).[supplied by OMIM, Oct 2009]

**Accessions** — [HGNC:14552](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14552) · Entrez [9641](https://www.ncbi.nlm.nih.gov/gene/9641) · UniProt [Q14164](https://www.uniprot.org/uniprotkb/Q14164) · Ensembl [ENSG00000263528](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000263528)

## Data

Gene col 15415: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15415); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15415, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15415]; `tensor/DDL_lfc|DDL_z.npy` [15415]; `embed/gene_vectors.npy` [15415]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15415 or target_col == 15415). Every well: [[IKBKE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IKBKE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
