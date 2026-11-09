---
symbol: "DNAJC11"
type: "gene"
col: 153
ensembl_id: "ENSG00000007923"
name: "DnaJ heat shock protein family (Hsp40) member C11"
location: "1p36.31"
module: 1
arm: "+"
pooled_cpm: 42.36
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 9
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# DNAJC11

*DnaJ heat shock protein family (Hsp40) member C11* — 1p36.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.64× (z +8.1, q 3e-13, up in 41 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.36× (z +7.1, q 4e-10, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.519× (z -10.7, q 1e-23, down in 38 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.624× (z -7.6, q 6e-12, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UTP20]] (+0.82, fdr 7e-06), [[GPATCH4]] (+0.80, fdr 7e-06), [[ALG8]] (+0.79, fdr 7e-06); moves opposite to [[FBXO33]] (-0.76, fdr 7e-06), [[MOSPD3]] (-0.73, fdr 7e-06), [[ARL3]] (-0.73, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[NR3C2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 153.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.64×** | +8.1 | 3e-13 | 41/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +7.1 | 4e-10 | 39/48 (CFPAC-1, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +6.7 | 5e-09 | 29/48 (LOX-IMVI, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +5.6 | 3e-06 | 32/48 (LoVo, PANC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.4 | 7e-06 | 27/47 (Hs 766T, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +5.1 | 3e-05 | 26/48 (NCI-H1573, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +4.9 | 6e-05 | 27/47 (PANC-1, LoVo, …) | all doses, flat | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.003 | 23/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.60×** | +4.0 | 0.004 | 21/47 (NCI-H1573, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.6 | 0.016 | 21/48 (NCI-H1573, COLO 205, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.26×** | +3.6 | 0.016 | 22/48 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.52×** | +3.6 | 0.017 | 14/48 (LoVo, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.22×** | +3.2 | 0.059 | 16/48 (NCI-H1792, BT-474, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.061 | 17/48 (AsPC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.062 | 17/47 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.083 | 16/47 (SW480, NCI-H1573, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.20×** | +3.0 | 0.083 | 14/48 (H4, Panc 03.27, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.41×** | +2.9 | 0.100 | 14/48 (Hs 766T, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 153.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.519×** | -10.7 | 1e-23 | 38/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.624×** | -7.6 | 6e-12 | 31/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.633×** | -7.4 | 2e-11 | 34/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.651×** | -7.0 | 5e-10 | 28/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.725×** | -5.2 | 2e-05 | 26/48 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.800×** | -5.1 | 3e-05 | 24/48 (PANC-1, HepG2/C3A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.789×** | -3.8 | 0.010 | 23/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.793×** | -3.8 | 0.012 | 21/48 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.818×** | -3.2 | 0.074 | 18/48 (NCI-H2030, HepG2/C3A, …) | two highest doses |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.874× | -3.1 | 0.12 | 11/48 (Panc 03.27, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 153. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 65.4 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.212× (z -19.8) |
| [[SW480 (line)]] | alt | 58.5 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 76.2 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.388× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 47.8 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.307× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 65.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.110× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -11.0) |
| [[SW48 (line)]] | wt | 63.2 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0852× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~61% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.277× (z -8.9) |
| [[HCT15 (line)]] | alt | 52.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.307× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[SNU-1 (line)]] | wt | 47.2 | 0 | 2 (1 ⚠) | — | [[Canagliflozin (drug)]] 0.05 µM 0.173× (z -10.1) |
| [[BT-474 (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.326× (z -8.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 60.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.424× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[LOX-IMVI (line)]] | wt | 24.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.249× (z -10.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 58.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.371× (z -8.6) |
| [[A-172 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 153), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP20]] | +0.82 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[GPATCH4]] | +0.80 | +0.81 / +0.74 | both halves | 7e-06 |  |
| [[ALG8]] | +0.79 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.79 | +0.81 / +0.69 | both halves | 7e-06 | STRING 473 |
| [[EMG1]] | +0.77 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[ABCE1]] | +0.77 | +0.78 / +0.73 | both halves | 7e-06 |  |
| [[DHX37]] | +0.77 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[MAPKAPK5]] | +0.76 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[MCM3AP]] | +0.75 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[MTHFSD]] | +0.75 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[CPSF2]] | +0.74 | +0.79 / +0.62 | both halves | 7e-06 |  |
| [[ANAPC7]] | +0.74 | +0.77 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO33]] | -0.76 | -0.70 / -0.69 | both halves | 7e-06 |  |
| [[MOSPD3]] | -0.73 | -0.73 / -0.60 | both halves | 7e-06 |  |
| [[ARL3]] | -0.73 | -0.70 / -0.60 | both halves | 7e-06 | pathway: Organelle biogenesis and maintenance |
| [[CBFA2T2]] | -0.72 | -0.77 / -0.55 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.72 | -0.73 / -0.59 | both halves | 7e-06 |  |
| [[PPP1R2]] | -0.71 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[AHDC1]] | -0.71 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[DNAAF3]] | -0.71 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[SLC17A7]] | -0.70 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[TNNI3]] | -0.69 | -0.60 / -0.58 | both halves | 8e-06 |  |
| [[PLEKHH3]] | -0.69 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[ANG]] | -0.69 | -0.65 / -0.66 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C2]] | B | NR3C2 activity lowers DNAJC11's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.32× higher at baseline in the lines without NR3C2 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[TSPAN33]] | B | TSPAN33 activity raises DNAJC11's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.36× lower at baseline in the lines without TSPAN33 | 0.069 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[SLC17A7]] | B | SLC17A7 activity raises DNAJC11's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 1.26× lower at baseline in the lines without SLC17A7 | 0.071 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DNAJC11's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises DNAJC11's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TSPAN33]] | B | TSPAN33 activity strengthens DNAJC11's drug response | lines that do not express TSPAN33 (12) vs lines expressing it (36) | the lines without TSPAN33 respond 0.83× as strongly (z diff +0.62); strongest at Panobinostat 5 µM: 0.88x vs 0.61x (z diff +3.3) | 0.094 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[BMF]] | C | BMF activity lowers DNAJC11's level | lines that do not express BMF (4) vs lines expressing it (46) | 1.51× higher at baseline in the lines without BMF | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285868; maybe low, not absent; its own permutation p |
| [[SLC25A23]] | C | SLC25A23's natural level weakens DNAJC11's drug response | SLC25A23's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.19; direction not clear | 0.099 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.808). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.7, -32.2); signed map (1.6, -42.4). **Vector** length 127, 36.2% of its response variance represented; |z| ≥ 3 in 1,018 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.51 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.51 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.52 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +5.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.5 | +8.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.8 | +6.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.5 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.3 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +7.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.8 | +4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.7 | +4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.3 | +2.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.2 | -5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.1 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -5.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.8 | -7.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.3 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -1.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.4 | -3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.31 — chr1:6,634,168-6,701,924 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10737 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Reactome | 3 pathways, smallest: Cristae formation; Mitochondrial biogenesis; Organelle biogenesis and maintenance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVH1](https://www.uniprot.org/uniprotkb/Q9NVH1) (DnaJ homolog subfamily C member 11):

> [Isoform 1]: Required for mitochondrial inner membrane organization. Seems to function through its association with the MICOS complex and the mitochondrial outer membrane sorting assembly machinery (SAM) complex.

**Summary**, from NCBI Gene [55735](https://www.ncbi.nlm.nih.gov/gene/55735):

> Involved in cristae formation. Located in MICOS complex and SAM complex. Part of MIB complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25570](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25570) · Entrez [55735](https://www.ncbi.nlm.nih.gov/gene/55735) · UniProt [Q9NVH1](https://www.uniprot.org/uniprotkb/Q9NVH1) · Ensembl [ENSG00000007923](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007923)

## Data

Gene col 153: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 153); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 153, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 153]; `tensor/DDL_lfc|DDL_z.npy` [153]; `embed/gene_vectors.npy` [153]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 153 or target_col == 153). Every well: [[DNAJC11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
