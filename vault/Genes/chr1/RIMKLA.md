---
symbol: "RIMKLA"
type: "gene"
col: 10799
ensembl_id: "ENSG00000177181"
name: "ribosomal modification protein rimK like family member A"
location: "1p34.2"
module: 134
arm: "+"
pooled_cpm: 19.53
n_lines_expressing: 42
n_dd_up: 5
n_dd_down: 28
n_dd_up_clean: 4
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# RIMKLA

*ribosomal modification protein rimK like family member A* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.53× (z +10.8, q 3e-24, up in 30 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.263× (z -33.6, q 0e+00, down in 37 of 39 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM117B]] (+0.70, fdr 1e-05), [[GPR160]] (+0.65, fdr 1e-05), [[ARFGEF3]] (+0.63, fdr 1e-05); moves opposite to [[EFCAB2]] (-0.58, fdr 4e-05), [[TM9SF5P]] (-0.53, fdr 2e-04), [[AVEN]] (-0.50, fdr 1e-04).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ARFGEF3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10799.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +10.8 | 3e-24 | 30/40 (Panc 03.27, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +7.0 | 1e-09 | 24/40 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Roxadustat (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.018 | 9/40 (SNU-1, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.26×** | +3.8 | 0.022 | 12/38 (C32, A549, …) | inconsistent across doses | low cells (technical?) |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **1.24×** | +3.6 | 0.031 | 9/39 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.16 | 4/40 (C32, HOP62, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10799.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.263×** | -33.6 | 0e+00 | 37/39 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.245×** | -24.1 | 0e+00 | 32/36 (J82, C32, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.283×** | -21.6 | 0e+00 | 34/39 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.313×** | -20.6 | 0e+00 | 38/40 (SNU-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.320×** | -20.2 | 0e+00 | 37/39 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.322×** | -20.2 | 0e+00 | 33/37 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.408×** | -15.9 | 0e+00 | 36/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.414×** | -15.7 | 0e+00 | 28/35 (MIA PaCa-2, J82, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.577×** | -13.8 | 1e-41 | 29/38 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.472×** | -13.3 | 9e-39 | 36/40 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.499×** | -11.4 | 2e-28 | 20/28 (NCI-H460, HCT15, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.531×** | -10.8 | 1e-25 | 16/25 (MIA PaCa-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.713×** | -8.5 | 8e-16 | 27/40 (SNU-1, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.631×** | -7.9 | 2e-13 | 23/38 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -7.3 | 9e-12 | 27/39 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.697×** | -6.4 | 5e-09 | 18/40 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.798×** | -5.6 | 6e-07 | 16/40 (SNU-1, Hs 766T, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.759×** | -4.9 | 3e-05 | 18/39 (SNU-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.775×** | -4.5 | 2e-04 | 15/40 (SW480, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.781×** | -4.4 | 4e-04 | 16/39 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10799. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.0 | 0 | 16 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0701× (z -33.7) |
| [[MIA PaCa-2 (line)]] | alt | 40.0 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0832× (z -31.2) |
| [[J82 (line)]] | alt | 26.4 | 0 | 11 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0310× (z -25.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.205× (z -17.4) |
| [[C32 (line)]] | wt | 44.8 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0396× (z -32.5) |
| [[HT-29 (line)]] | alt | 23.7 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.241× (z -15.4) |
| [[LS 180 (line)]] | wt | 38.8 | 0 | 9 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.225× (z -12.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.366× (z -12.3) |
| [[NCI-H1792 (line)]] | alt | 26.3 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -16.0) |
| [[SNU-1 (line)]] | wt | 49.6 | 0 | 9 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0630× (z -17.6) |
| [[SW480 (line)]] | alt | 28.1 | 0 | 9 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.177× (z -17.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.352× (z -15.2) |
| [[LoVo (line)]] | wt | 48.0 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -16.2) |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -16.9) |
| [[HEC-1-A (line)]] | alt | 11.8 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -17.7) |
| [[NCI-H1573 (line)]] | alt | 16.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -17.6) |
| [[NCI-H2030 (line)]] | alt | 21.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -22.0) |
| [[NCI-H23 (line)]] | alt | 14.8 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0977× (z -12.6) |
| [[SW 900 (line)]] | alt | 19.4 | 0 | 7 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0416× (z -18.7) |
| [[A-427 (line)]] | wt | 27.4 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -16.5) |
| [[CFPAC-1 (line)]] | alt | 36.8 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0912× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -16.9) |
| [[HCT15 (line)]] | alt | 43.5 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0973× (z -21.6) |
| [[PANC-1 (line)]] | alt | 12.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -19.9) |
| [[RKO (line)]] | wt | 21.5 | 0 | 5 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0413× (z -17.4) ⚠ toxic · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0651× (z -14.9) |
| [[SW48 (line)]] | wt | 30.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -18.5) |
| [[A-172 (line)]] | wt | 5.80 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -10.6) |
| [[A549 (line)]] | wt | 11.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -16.7) |
| [[SHP-77 (line)]] | alt | 57.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.437× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0777× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.183× (z -9.2) |
| [[Hs 766T (line)]] | wt | 13.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0907× (z -17.2) |
| [[SW1417 (line)]] | alt | 18.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -11.7) |
| [[AN3 CA (line)]] | alt | 45.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -8.6) |
| [[BT-474 (line)]] | alt | 9.11 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0936× (z -9.4) |
| [[HOP62 (line)]] | alt | 7.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 7.53 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -12.3) |
| [[RPMI-7951 (line)]] | alt | 7.07 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -8.7) |
| [[A498 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10799), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM117B]] | +0.70 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[GPR160]] | +0.65 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ARFGEF3]] | +0.63 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[SLC2A3]] | +0.63 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[MRPL17]] | +0.62 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.62 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[PGK1]] | +0.61 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[HK1]] | +0.61 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[TFB1M]] | +0.60 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[FAM234B]] | +0.60 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[WASF3]] | +0.60 | +0.55 / +0.39 | both halves | 5e-05 |  |
| [[WDR45B]] | +0.60 | +0.54 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB2]] | -0.58 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[TM9SF5P]] | -0.53 | -0.57 / -0.29 | both halves | 2e-04 |  |
| [[AVEN]] | -0.50 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[CFLAR]] | -0.50 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[QTRT1]] | -0.49 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[CYB5D2]] | -0.49 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[PKN2-AS1]] | -0.49 | -0.47 / -0.19 | ⚠ not reproduced | 9e-04 |  |
| [[EFCAB6]] | -0.49 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[RABL2A]] | -0.49 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[DNAI4]] | -0.49 | -0.48 / -0.12 | ⚠ not reproduced | 0.002 |  |
| [[ITPA]] | -0.49 | -0.40 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RIMKLA's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[WSCD1]] | B | WSCD1 activity raises RIMKLA's level | lines that do not express WSCD1 (23) vs lines expressing it (27) | 2.12× lower at baseline in the lines without WSCD1 | 0.047 | ⚠ within organs, on part of the lines; also absent: JPH3, FAR2P1, ANKRD20A11P |
| [[KDM2B-DT]] | B | KDM2B-DT activity raises RIMKLA's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 1.12× lower at baseline in the lines without KDM2B-DT | 0.081 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARFGEF3]] | B | RIMKLA activity raises ARFGEF3's level | lines that do not express RIMKLA (8) vs lines expressing it (42) | 2.70× lower at baseline in the lines without RIMKLA | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000290927, PLEKHH1, NRTN; its own permutation p |

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.726). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.8, -12.8); signed map (-36.3, 27.1). **Vector** length 96.0, 23.1% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +7.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +1.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.6 | +2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.3 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +1.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.9 | -24.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.4 | -8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -5.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.5 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.4 | -15.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.3 | -2.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.2 | -0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal modification protein rimK like family member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:42,380,792-42,424,232 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC47816, RP11-157D18.1, NAAGS-II; previously FAM80A |
| Gene groups (HGNC) | ATP-grasp fold containing; Ribosomal modification protein rimK like family |
| Reactome | 2 pathways, smallest: Glutamate and glutamine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXN7](https://www.uniprot.org/uniprotkb/Q8IXN7) (N-acetylaspartylglutamate synthase A):

> Catalyzes the synthesis of N-acetyl-L-aspartyl-L-glutamate (NAAG) and N-acetyl-L-aspartyl-L-glutamyl-L-glutamate.

**Summary**, from NCBI Gene [284716](https://www.ncbi.nlm.nih.gov/gene/284716):

> Predicted to enable N-acetyl-L-aspartate-L-glutamate ligase activity. Predicted to be involved in L-amino acid metabolic process. Predicted to be located in cytosol. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28725](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28725) · Entrez [284716](https://www.ncbi.nlm.nih.gov/gene/284716) · UniProt [Q8IXN7](https://www.uniprot.org/uniprotkb/Q8IXN7) · Ensembl [ENSG00000177181](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177181)

## Data

Gene col 10799: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10799); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10799, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10799]; `tensor/DDL_lfc|DDL_z.npy` [10799]; `embed/gene_vectors.npy` [10799]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10799 or target_col == 10799). Every well: [[RIMKLA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIMKLA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
