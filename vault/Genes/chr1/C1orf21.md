---
symbol: "C1orf21"
type: "gene"
col: 3815
ensembl_id: "ENSG00000116667"
name: "chromosome 1 open reading frame 21"
location: "1q25.3"
module: 95
arm: "-"
pooled_cpm: 74.53
n_lines_expressing: 41
n_dd_up: 0
n_dd_down: 35
n_dd_up_clean: 0
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# C1orf21

*chromosome 1 open reading frame 21* — 1q25.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 2 lines (NCI-H460 2.22×, CFPAC-1 2.28×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (NCI-H1573 3.03×); [[Panobinostat (drug)]] 0.05 µM in 1 line (NCI-H460 2.79×; ⚠ cell-cycle shift, explains ~0% of this change); [[Peretinoin (drug)]] 5 µM in 1 line (NCI-H1573 4.17×).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.252× (z -36.7, q 0e+00, down in 38 of 38 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HACE1]] (+0.70, fdr 2e-05), [[WASF3]] (+0.69, fdr 3e-05), [[IDH2]] (+0.63, fdr 1e-05); moves opposite to [[WARS2-AS1]] (-0.61, fdr 4e-04), [[C11orf58]] (-0.61, fdr 5e-05), [[RFX3-DT]] (-0.60, fdr 4e-04).
> It sits in the **-** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[GAL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3815.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 2 lines (NCI-H460 2.22×, CFPAC-1 2.28×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (NCI-H1573 3.03×); [[Panobinostat (drug)]] 0.05 µM in 1 line (NCI-H460 2.79×; ⚠ cell-cycle shift, explains ~0% of this change); [[Peretinoin (drug)]] 5 µM in 1 line (NCI-H1573 4.17×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +4.6 | 0.003 | 14/39 (A498, RPMI-7951, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.4 | 0.22 | 14/39 (NCI-H460, RKO, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | 1.37× | +3.2 | 0.30 | 14/40 (A-427, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3815.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.252×** | -36.7 | 0e+00 | 38/38 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.205×** | -29.8 | 0e+00 | 38/38 (H4, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.295×** | -22.1 | 0e+00 | 37/39 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.402×** | -15.9 | 0e+00 | 30/34 (C-33 A, A-427, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.437×** | -15.6 | 0e+00 | 35/39 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.474×** | -13.5 | 1e-39 | 23/32 (A-172, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.498×** | -13.1 | 2e-37 | 34/39 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.511×** | -12.6 | 1e-34 | 31/39 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.513×** | -12.5 | 3e-34 | 28/38 (A-172, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -11.6 | 2e-29 | 26/40 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.547×** | -10.9 | 6e-26 | 28/39 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.574×** | -10.0 | 7e-22 | 28/37 (RKO, C32, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.597×** | -9.7 | 2e-20 | 32/39 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.600×** | -9.6 | 4e-20 | 31/39 (BT-474, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.703×** | -9.3 | 4e-19 | 28/39 (A-172, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.643×** | -8.3 | 5e-15 | 25/39 (LoVo, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.646×** | -8.2 | 9e-15 | 29/39 (SNU-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.647×** | -8.2 | 1e-14 | 25/39 (C32, A-172, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.639×** | -8.1 | 2e-14 | 26/41 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.530×** | -6.2 | 1e-08 | 19/40 (LoVo, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3815. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 366 | 0 | 19 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -30.7) |
| [[LoVo (line)]] | wt | 185 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0997× (z -46.1) |
| [[A-172 (line)]] | wt | 206 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -20.1) |
| [[HS-578T (line)]] | alt | 131 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -19.8) |
| [[HOP62 (line)]] | alt | 74.7 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -27.9) |
| [[LOX-IMVI (line)]] | wt | 195 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0771× (z -33.0) |
| [[RKO (line)]] | wt | 110 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -30.2) |
| [[LS 180 (line)]] | wt | 186 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -26.5) |
| [[SNU-423 (line)]] | alt | 123 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -13.8) |
| [[BT-474 (line)]] | alt | 63.9 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -15.0) |
| [[A-427 (line)]] | wt | 85.1 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0575× (z -34.5) |
| [[CHP-212 (line)]] | wt | 307 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -13.6) |
| [[NCI-H460 (line)]] | wt | 30.0 | 3 (2 ⚠) | 5 | [[Tucidinostat (drug)]] 5 µM 2.22× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -14.2) |
| [[COLO 205 (line)]] | alt | 48.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -12.7) |
| [[J82 (line)]] | alt | 167 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -22.5) |
| [[H4 (line)]] | wt | 143 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0122× (z -36.9) |
| [[Hs 766T (line)]] | wt | 41.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -18.1) |
| [[HT-29 (line)]] | alt | 111 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -28.8) |
| [[SK-MEL-2 (line)]] | alt | 173 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -27.1) |
| [[HCT15 (line)]] | alt | 48.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -18.3) |
| [[RPMI-7951 (line)]] | alt | 88.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -16.6) |
| [[SW 900 (line)]] | alt | 82.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -14.1) |
| [[AsPC-1 (line)]] | alt | 38.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -16.4) |
| [[HEC-1-A (line)]] | alt | 28.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -18.9) |
| [[NCI-H1573 (line)]] | alt | 18.9 | 2 | 2 | [[Vinblastine (sulfate) (drug)]] 5 µM 3.03× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.7) |
| [[SHP-77 (line)]] | alt | 132 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -9.7) |
| [[SW1417 (line)]] | alt | 42.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -15.7) |
| [[SW48 (line)]] | wt | 68.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -14.0) |
| [[C-33 A (line)]] | alt | 124 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0590× (z -22.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 18.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -11.9) |
| [[A498 (line)]] | wt | 75.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.455× (z -9.5) |
| [[A549 (line)]] | wt | 20.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 31.6 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.28× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.234× (z -11.2) |
| [[SNU-1 (line)]] | wt | 26.4 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.134× (z -10.2) |
| [[SW 1271 (line)]] | alt | 36.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -9.1) |
| [[AN3 CA (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.03 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 121 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.37 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.71 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.57 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3815), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACE1]] | +0.70 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[WASF3]] | +0.69 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[IDH2]] | +0.63 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[CDON]] | +0.60 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[MCUB]] | +0.60 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[ARL6]] | +0.60 | +0.59 / +0.33 | both halves | 1e-04 |  |
| [[SPTLC2]] | +0.59 | +0.59 / +0.39 | both halves | 6e-05 |  |
| [[ARHGEF26]] | +0.59 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[HK1]] | +0.59 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[HERC3]] | +0.59 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[OSBPL6]] | +0.58 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[LPCAT2]] | +0.58 | +0.57 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WARS2-AS1]] | -0.61 | -0.70 / -0.24 | both halves | 4e-04 |  |
| [[C11orf58]] | -0.61 | -0.65 / -0.39 | both halves | 5e-05 |  |
| [[RFX3-DT]] | -0.60 | -0.68 / -0.26 | both halves | 4e-04 |  |
| [[HCG11]] | -0.60 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[INO80D]] | -0.60 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[RAB30-DT]] | -0.59 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[BAZ2B]] | -0.59 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[ST7L]] | -0.58 | -0.66 / -0.33 | both halves | 1e-04 |  |
| [[DHRS12]] | -0.58 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[PPP3CB-AS1]] | -0.58 | -0.65 / -0.29 | both halves | 3e-04 |  |
| [[CCDC90B-AS1]] | -0.57 | -0.70 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[ERMAP]] | -0.57 | -0.63 / -0.23 | both halves | 5e-04 |  |
| [[LINC00174]] | -0.57 | -0.60 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises C1orf21's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LIMCH1]] | B | LIMCH1 activity raises C1orf21's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.93× lower at baseline in the lines without LIMCH1 | 0.088 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAL]] | B | C1orf21 activity lowers GAL's level | lines that do not express C1orf21 (9) vs lines expressing it (41) | 1.94× higher at baseline in the lines without C1orf21 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, GALNT8 |
| [[HCG11]] | B | C1orf21 activity lowers HCG11's level | lines that do not express C1orf21 (9) vs lines expressing it (41) | 2.11× higher at baseline in the lines without C1orf21 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, GALNT8 |
| [[SLC1A1]] | B | C1orf21 activity raises SLC1A1's level | lines that do not express C1orf21 (9) vs lines expressing it (41) | 2.90× lower at baseline in the lines without C1orf21 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, GALNT8 |
| [[RNF152]] | B | C1orf21 activity raises RNF152's level | lines that do not express C1orf21 (9) vs lines expressing it (41) | 3.38× lower at baseline in the lines without C1orf21 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, GALNT8 |

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **-** arm (projection on the module's main direction -0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (3.4, 7.0); signed map (-41.4, 17.1). **Vector** length 107, 29.8% of its response variance represented; |z| ≥ 3 in 1,380 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.8 | +1.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.4 | +3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.9 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +4.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | -0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +2.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -15.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.2 | -29.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -9.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.6 | -2.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.3 | -22.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.6 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -5.1 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -2.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 1 open reading frame 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:184,387,029-184,629,019 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PIG13 |
| Matched by | ensembl_id |

UniProt [Q9H246](https://www.uniprot.org/uniprotkb/Q9H246) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:15494](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15494) · Entrez [81563](https://www.ncbi.nlm.nih.gov/gene/81563) · UniProt [Q9H246](https://www.uniprot.org/uniprotkb/Q9H246) · Ensembl [ENSG00000116667](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116667)

## Data

Gene col 3815: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3815); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3815, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3815]; `tensor/DDL_lfc|DDL_z.npy` [3815]; `embed/gene_vectors.npy` [3815]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3815 or target_col == 3815). Every well: [[C1orf21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1orf21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
