---
symbol: "ATF3"
type: "gene"
col: 8576
ensembl_id: "ENSG00000162772"
name: "activating transcription factor 3"
location: "1q32.3"
module: 93
arm: "+"
pooled_cpm: 78.79
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 24
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# ATF3

*activating transcription factor 3* — 1q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 9.90× (z +24.3, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.523× (z -4.2, q 0.017, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (HT-29 0.165×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 0.199×; ⚠ toxic; transcription drop); [[Phenylephrine (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.206×); [[Dexamethasone (drug)]] 0.5 µM in 1 line (NCI-H1573 0.170×); [[Econazole (drug)]] 5 µM in 1 line (NCI-H1573 0.243×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IQCN]] (+0.75, fdr 7e-06), [[JUN]] (+0.74, fdr 7e-06), [[KLF4]] (+0.68, fdr 7e-06); moves opposite to [[PARGP1]] (-0.63, fdr 1e-05), [[STARD3]] (-0.59, fdr 7e-06), [[CDK5RAP1]] (-0.57, fdr 1e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RASEF]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8576.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **9.90×** | +24.3 | 0e+00 | 45/47 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.78×** | +12.6 | 4e-34 | 43/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.65×** | +11.5 | 2e-28 | 41/47 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.68×** | +7.4 | 2e-11 | 37/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.58×** | +7.1 | 1e-10 | 40/48 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.47×** | +6.8 | 1e-09 | 37/48 (NCI-H460, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +5.3 | 9e-06 | 38/49 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +4.6 | 3e-04 | 32/49 (NCI-H460, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.84×** | +4.6 | 3e-04 | 38/48 (C-33 A, A-427, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.06×** | +4.4 | 7e-04 | 31/49 (NCI-H460, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.60×** | +4.4 | 7e-04 | 36/49 (AsPC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +4.3 | 9e-04 | 35/48 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **1.53×** | +4.2 | 0.001 | 35/50 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +4.0 | 0.003 | 26/46 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.83×** | +3.9 | 0.003 | 25/48 (NCI-H460, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.81×** | +3.9 | 0.004 | 35/48 (BT-474, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.007 | 27/48 (C-33 A, SW48, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8576.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (HT-29 0.165×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 0.199×; ⚠ toxic; transcription drop); [[Phenylephrine (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.206×); [[Dexamethasone (drug)]] 0.5 µM in 1 line (NCI-H1573 0.170×); [[Econazole (drug)]] 5 µM in 1 line (NCI-H1573 0.243×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.523×** | -4.2 | 0.017 | 30/48 (NCI-H1573, SW 900, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.557×** | -3.8 | 0.047 | 28/48 (NCI-H1573, SW 900, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | 0.425× | -3.3 | 0.16 | 25/47 (BT-474, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.619× | -3.1 | 0.23 | 32/49 (NCI-H1792, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.620× | -3.1 | 0.23 | 26/48 (COLO 205, Panc 03.27, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8576. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 87.7 | 3 | 5 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +23.4) | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 0.206× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 104 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +21.8) | — |
| [[A-172 (line)]] | wt | 59.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.8× (z +27.0) | — |
| [[A498 (line)]] | wt | 139 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.0× (z +24.9) | — |
| [[A549 (line)]] | wt | 77.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +21.7) | — |
| [[C32 (line)]] | wt | 59.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 52.4× (z +23.7) | — |
| [[J82 (line)]] | alt | 56.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.1× (z +22.2) | — |
| [[LoVo (line)]] | wt | 154 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +17.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 57.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +17.8) | — |
| [[SK-MEL-2 (line)]] | alt | 37.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.79× (z +15.6) | — |
| [[SW1417 (line)]] | alt | 67.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.75× (z +21.6) | — |
| [[A-427 (line)]] | wt | 72.0 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.43× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 84.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +20.1) | — |
| [[HS-578T (line)]] | alt | 43.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +19.9) | — |
| [[hTERT-HPNE (line)]] | wt | 79.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +19.2) | — |
| [[NCI-H2030 (line)]] | alt | 43.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.54× (z +17.2) | — |
| [[NCI-H23 (line)]] | alt | 46.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.25× (z +17.5) | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 89.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +22.9) | — |
| [[PANC-1 (line)]] | alt | 74.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +24.2) | — |
| [[SW48 (line)]] | wt | 82.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +12.4) | — |
| [[SW480 (line)]] | alt | 39.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.35× (z +14.4) | — |
| [[C-33 A (line)]] | alt | 57.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 123 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +23.3) | — |
| [[HEC-1-A (line)]] | alt | 25.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +16.2) | — |
| [[HOP62 (line)]] | alt | 39.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.8× (z +17.9) | — |
| [[LS 180 (line)]] | wt | 86.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +11.6) | — |
| [[NCI-H1792 (line)]] | alt | 54.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +17.4) | — |
| [[Panc 03.27 (line)]] | alt | 150 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.58× (z +15.3) | — |
| [[RPMI-7951 (line)]] | alt | 43.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +15.7) | — |
| [[SNU-423 (line)]] | alt | 66.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +20.0) | — |
| [[SW 900 (line)]] | alt | 84.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.6× (z +18.7) | — |
| [[BT-474 (line)]] | alt | 71.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +13.9) | — |
| [[COLO 205 (line)]] | alt | 70.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.90× (z +10.4) | — |
| [[H4 (line)]] | wt | 81.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +15.4) | — |
| [[HCT15 (line)]] | alt | 92.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.78× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 150 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +12.8) | — |
| [[Hs 766T (line)]] | wt | 52.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.78× (z +14.2) | — |
| [[HT-29 (line)]] | alt | 208 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[KATO III (line)]] | alt | 92.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 109 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +12.1) | — |
| [[RKO (line)]] | wt | 40.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +11.5) | — |
| [[SNU-1 (line)]] | wt | 44.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +9.8) | — |
| [[SW 1088 (line)]] | alt | 45.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.8× (z +10.5) | — |
| [[SW 1271 (line)]] | alt | 64.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.92× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8576), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCN]] | +0.75 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[JUN]] | +0.74 | +0.69 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS; STRING 999 |
| [[KLF4]] | +0.68 | +0.75 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 681 |
| [[IFRD1]] | +0.65 | +0.74 / +0.63 | both halves | 7e-06 | STRING 632 |
| [[PPP1R15A]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 896 |
| [[DUSP8]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[LINC02901]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[PRECSIT]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[IRF1]] | +0.60 | +0.67 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS; STRING 518 |
| [[TLE4]] | +0.59 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R15B]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SQSTM1]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS; STRING 522 |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARGP1]] | -0.63 | -0.49 / -0.70 | both halves | 1e-05 |  |
| [[STARD3]] | -0.59 | -0.58 / -0.60 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[CDK5RAP1]] | -0.57 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[PCGF6]] | -0.56 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[PDSS1]] | -0.56 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[SNRNP40]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[SNRPD1]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[TUBGCP4]] | -0.54 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[GTF3C2]] | -0.53 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[EEF1E1]] | -0.53 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[WDR5]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 | pathway: Co-inhibition by PD-1 |
| [[MFSD14CP]] | -0.52 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASEF]] | B | RASEF activity raises ATF3's level | lines that do not express RASEF (20) vs lines expressing it (30) | 1.43× lower at baseline in the lines without RASEF | 0.060 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[GATA6]] | B | GATA6 activity raises ATF3's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 1.51× lower at baseline in the lines without GATA6 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.3, 4.8); signed map (4.0, 20.5). **Vector** length 145, 54.8% of its response variance represented; |z| ≥ 3 in 1,252 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Binimetinib (drug)]] 5 µM |  | +7.5 | +4.4 |
|  | [[Trametinib (drug)]] 5 µM |  | +7.1 | +4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.1 | +3.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +6.0 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +5.2 | +3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.0 | +4.6 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.5 | -4.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | -4.5 | +1.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.1 | -3.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -1.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.4 | -2.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.0 | -3.0 |
|  | [[Carbamazepine (drug)]] 0.5 µM |  | -2.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | activating transcription factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.3 — chr1:212,565,334-212,620,777 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Activating transcription factor 3 family |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, UNFOLDED_PROTEIN_RESPONSE, APOPTOSIS, UV_RESPONSE_UP, HYPOXIA, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Reactome | 13 pathways, smallest: Response of EIF2AK1 (HRI) to heme deficiency; ATF4 activates genes in response to endoplasmic reticulum  stress; PERK regulates gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [P18847](https://www.uniprot.org/uniprotkb/P18847) (Cyclic AMP-dependent transcription factor ATF-3):

> This protein binds the cAMP response element (CRE) (consensus: 5'-GTGACGT[AC][AG]-3'), a sequence present in many viral and cellular promoters. Represses transcription from promoters with ATF sites. It may repress transcription by stabilizing the binding of inhibitory cofactors at the promoter.; [Isoform 2]: Activates transcription presumably by sequestering inhibitory cofactors away from the promoters.; [Isoform 3]: Stress-induced isoform, counteracts the transcriptional repression of isoform …

**Summary**, from NCBI Gene [467](https://www.ncbi.nlm.nih.gov/gene/467):

> This gene encodes a member of the mammalian activation transcription factor/cAMP responsive element-binding (CREB) protein family of transcription factors. This gene is induced by a variety of signals, including many of those encountered by cancer cells, and is involved in the complex process of cellular stress response. Multiple transcript variants encoding different isoforms have been found for this gene. It is possible that alternative splicing of this gene may be physiologically important …

**Accessions** — [HGNC:785](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:785) · Entrez [467](https://www.ncbi.nlm.nih.gov/gene/467) · UniProt [P18847](https://www.uniprot.org/uniprotkb/P18847) · Ensembl [ENSG00000162772](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162772)

## Data

Gene col 8576: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8576); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8576, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8576]; `tensor/DDL_lfc|DDL_z.npy` [8576]; `embed/gene_vectors.npy` [8576]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8576 or target_col == 8576). Every well: [[ATF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
