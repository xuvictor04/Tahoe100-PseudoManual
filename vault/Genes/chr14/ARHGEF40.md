---
symbol: "ARHGEF40"
type: "gene"
col: 9186
ensembl_id: "ENSG00000165801"
name: "Rho guanine nucleotide exchange factor 40"
location: "14q11.2"
module: 14
arm: "+"
pooled_cpm: 15.26
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 21
n_dd_up_clean: 5
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# ARHGEF40

*Rho guanine nucleotide exchange factor 40* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.34× (z +18.2, q 0e+00, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.530× (z -9.6, q 4e-19, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CX3CL1]] (+0.66, fdr 7e-06), [[TEF]] (+0.65, fdr 1e-05), [[BTN2A2]] (+0.64, fdr 1e-05); moves opposite to [[ARHGEF7]] (-0.57, fdr 3e-05), [[STRAP]] (-0.55, fdr 3e-05), [[BTAF1]] (-0.55, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ANO9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9186.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.34×** | +18.2 | 0e+00 | 35/46 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.22×** | +11.7 | 5e-29 | 34/47 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.022 | 13/46 (LS 180, NCI-H460, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.034 | 7/45 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.059 | 8/47 (HepG2/C3A, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.13 | 13/47 (AsPC-1, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.23× | +3.1 | 0.14 | 13/46 (AsPC-1, MIA PaCa-2, …) | all doses, flat | position effect removed |
| [[Cobimetinib (drug)]] 0.05 µM |  | 1.24× | +3.1 | 0.14 | 9/46 (SNU-423, BT-474, …) | all doses, flat | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.22× | +3.0 | 0.14 | 10/47 (LS 180, J82, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.22× | +3.0 | 0.14 | 12/46 (MIA PaCa-2, SW480, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9186.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.530×** | -9.6 | 4e-19 | 36/47 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.551×** | -9.0 | 5e-17 | 29/47 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.622×** | -7.2 | 1e-10 | 28/47 (SNU-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.411×** | -7.0 | 3e-10 | 23/45 (HOP62, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.651×** | -6.5 | 1e-08 | 26/47 (A-172, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.671×** | -6.0 | 1e-07 | 22/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.785×** | -5.2 | 2e-05 | 22/47 (C32, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.581×** | -4.3 | 0.001 | 18/47 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.753×** | -4.3 | 0.001 | 20/47 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.819×** | -4.3 | 0.001 | 17/47 (SK-MEL-2, SW 1088, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.766×** | -3.8 | 0.007 | 16/46 (Panc 03.27, SW1417, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.628×** | -3.7 | 0.011 | 15/45 (AN3 CA, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.786×** | -3.6 | 0.012 | 15/46 (COLO 205, LOX-IMVI, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.779×** | -3.6 | 0.012 | 18/43 (MIA PaCa-2, COLO 205, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.646×** | -3.4 | 0.021 | 11/47 (NCI-H460, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.797×** | -3.4 | 0.022 | 15/45 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.811×** | -3.2 | 0.051 | 12/46 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.813×** | -3.1 | 0.056 | 6/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9186. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 20.7 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +15.3) | [[Panobinostat (drug)]] 5 µM 0.295× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 15.7 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.166× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 32.7 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +14.7) | [[Panobinostat (drug)]] 5 µM 0.232× (z -9.9) |
| [[COLO 205 (line)]] | alt | 23.2 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.165× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 13.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +16.5) | — |
| [[J82 (line)]] | alt | 19.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.96× (z +21.8) | — |
| [[LOX-IMVI (line)]] | wt | 18.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.189× (z -9.9) ⚠ cell-cycle shift, explains ~2% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.218× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 23.8 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.168× (z -12.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.271× (z -9.5) |
| [[PANC-1 (line)]] | alt | 7.09 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +14.5) | — |
| [[SNU-1 (line)]] | wt | 17.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +10.3) | [[Digitoxin (drug)]] 0.5 µM 0.122× (z -9.0) |
| [[A498 (line)]] | wt | 22.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.3) | — |
| [[A549 (line)]] | wt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +10.5) | — |
| [[BT-474 (line)]] | alt | 8.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +8.9) | — |
| [[C32 (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 5.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.21× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 17.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +15.4) | — |
| [[HS-578T (line)]] | alt | 20.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.40 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0524× (z -12.3) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 4.98 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -8.5) ⚠ cell-cycle shift, explains ~84% of this change |
| [[NCI-H2347 (line)]] | alt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +12.9) | — |
| [[RKO (line)]] | wt | 17.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 38.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 24.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.2) | — |
| [[A-427 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9186), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CX3CL1]] | +0.66 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[TEF]] | +0.65 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[BTN2A2]] | +0.64 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[SIX5]] | +0.63 | +0.65 / +0.57 | both halves | 8e-06 |  |
| [[SLC2A6]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[SYNPO]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[MARCKS]] | +0.61 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[TRIM47]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[CCDC102A]] | +0.61 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[ZNF318]] | +0.61 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[STAP2]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ZFHX2]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF7]] | -0.57 | -0.66 / -0.43 | both halves | 3e-05 | same gene group; pathway: Cell death signalling via NRAGE, NRIF and NADE |
| [[STRAP]] | -0.55 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[BTAF1]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[PPHLN1]] | -0.55 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[EIF3H]] | -0.54 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[PMPCA]] | -0.54 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[NUTF2]] | -0.54 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[ZNF749]] | -0.54 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[FBXW2]] | -0.53 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[MDH2]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[TXNDC12]] | -0.53 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[DCAF13]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANO9]] | B | ANO9 activity lowers ARHGEF40's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 1.60× higher at baseline in the lines without ANO9 | 0.062 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.671). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.8, 5.8); signed map (18.1, -12.5). **Vector** length 98.0, 21.8% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.0 | +18.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +10.4 | +11.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.9 | +3.7 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.6 | -9.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -9.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -4.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.5 | -1.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.5 | -6.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -4.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -7.0 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 40 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:21,070,273-21,090,248 (+) |
| Ensembl biotype | protein_coding |
| Also known as | solo, FLJ10357 |
| Gene groups (HGNC) | Dbl family Rho GEFs |
| Reactome | 12 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; Cell death signalling via NRAGE, NRIF and NADE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TER5](https://www.uniprot.org/uniprotkb/Q8TER5) (Rho guanine nucleotide exchange factor 40):

> Acts as a guanine nucleotide exchange factor (GEF) for RHOA and RHOC. Promotes actin stress fiber formation, force-induced stress fiber reinforcement and organization of KRT8/KRT18 networks via activation of RHOA/ROCK signaling, which is mediated by N-terminus KRT18 binding. Regulates the formation or maintenance of properly elongated morphology of epithelial tubules, via mediation of the organization and orientation of KRT18 filaments (By similarity). Promotes RHOA-dependent, cell-cell contact …

**Summary**, from NCBI Gene [55701](https://www.ncbi.nlm.nih.gov/gene/55701):

> This gene encodes a protein similar to guanosine nucleotide exchange factors for Rho GTPases. The encoded protein contains in its C-terminus a GEF domain involved in exchange activity and a pleckstrin homology domain. Alternatively spliced transcripts that encode different proteins have been described. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:25516](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25516) · Entrez [55701](https://www.ncbi.nlm.nih.gov/gene/55701) · UniProt [Q8TER5](https://www.uniprot.org/uniprotkb/Q8TER5) · Ensembl [ENSG00000165801](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165801)

## Data

Gene col 9186: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9186); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9186, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9186]; `tensor/DDL_lfc|DDL_z.npy` [9186]; `embed/gene_vectors.npy` [9186]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9186 or target_col == 9186). Every well: [[ARHGEF40 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF40.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
