---
symbol: "SYNE1"
type: "gene"
col: 5158
ensembl_id: "ENSG00000131018"
name: "spectrin repeat containing nuclear envelope protein 1"
location: "6q25.2"
module: 28
arm: "+"
pooled_cpm: 47.41
n_lines_expressing: 40
n_dd_up: 37
n_dd_down: 6
n_dd_up_clean: 32
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# SYNE1

*spectrin repeat containing nuclear envelope protein 1* — 6q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.40× (z +37.0, q 0e+00, up in 35 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[HI-TOPK-032 (drug)]] 5 µM: 0.576× (z -3.7, q 0.060, down in 17 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LURAP1L-AS1]] (+0.73, fdr 7e-06), [[RIPK2-DT]] (+0.65, fdr 1e-05), [[PRECSIT]] (+0.64, fdr 1e-05); moves opposite to [[FBH1]] (-0.62, fdr 1e-05), [[CTNNBIP1]] (-0.62, fdr 1e-05), [[SRGAP2D]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LINC01435]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZXDA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5158.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.40×** | +37.0 | 0e+00 | 35/37 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.02×** | +23.5 | 0e+00 | 35/37 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.73×** | +12.6 | 4e-34 | 33/38 (NCI-H1573, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.52×** | +12.1 | 3e-31 | 31/38 (HEC-1-A, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.90×** | +8.4 | 5e-15 | 25/38 (SK-MEL-2, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.82×** | +7.8 | 4e-13 | 27/38 (J82, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +7.2 | 5e-11 | 23/31 (A549, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +7.1 | 7e-11 | 20/34 (HEC-1-A, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +6.2 | 3e-08 | 22/35 (A549, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +5.6 | 1e-06 | 20/38 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +5.5 | 2e-06 | 22/38 (NCI-H2347, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +5.1 | 2e-05 | 17/37 (SNU-423, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.30×** | +4.8 | 6e-05 | 19/38 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +4.5 | 3e-04 | 19/38 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.39×** | +4.2 | 8e-04 | 19/37 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +4.2 | 1e-03 | 21/37 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.003 | 18/37 (NCI-H23, C32, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.003 | 13/38 (NCI-H2030, HEC-1-A, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.003 | 15/38 (A549, NCI-H1792, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5158.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.576×** | -3.7 | 0.060 | 17/37 (hTERT-HPNE, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.758×** | -3.7 | 0.060 | 18/37 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.827×** | -3.6 | 0.060 | 20/38 (LOX-IMVI, H4, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.766×** | -3.5 | 0.060 | 14/37 (SK-MEL-2, SNU-423, …) | two highest doses | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.603×** | -3.4 | 0.078 | 10/37 (HT-29, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.770×** | -3.3 | 0.083 | 17/37 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5158. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 154 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +21.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -10.4) ⚠ cell-cycle shift, explains ~13% of this change |
| [[A549 (line)]] | wt | 80.3 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +26.7) | — |
| [[SK-MEL-2 (line)]] | alt | 63.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +27.0) | — |
| [[A-427 (line)]] | wt | 36.9 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +32.5) | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -10.8) |
| [[C-33 A (line)]] | alt | 116 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 10.1× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 16.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 221× (z +33.5) | — |
| [[LOX-IMVI (line)]] | wt | 158 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.31× (z +26.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -10.7) ⚠ cell-cycle shift, explains ~13% of this change |
| [[LS 180 (line)]] | wt | 12.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +16.9) | [[Digitoxin (drug)]] 5 µM 0.0579× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 20.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 177× (z +34.5) | — |
| [[NCI-H460 (line)]] | wt | 54.0 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.24× (z +14.8) | — |
| [[SW480 (line)]] | alt | 13.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.4× (z +22.7) | — |
| [[A498 (line)]] | wt | 87.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.39× (z +24.2) | — |
| [[AsPC-1 (line)]] | alt | 20.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.0× (z +23.3) | — |
| [[C32 (line)]] | wt | 53.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 8.76× (z +13.1) | — |
| [[CFPAC-1 (line)]] | alt | 62.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +26.2) | — |
| [[CHP-212 (line)]] | wt | 120 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +12.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.237× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[HEC-1-A (line)]] | alt | 45.1 | 3 | 0 | [[Auranofin (drug)]] 5 µM 15.2× (z +19.2) | — |
| [[Hs 766T (line)]] | wt | 55.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.89× (z +19.5) | — |
| [[HT-29 (line)]] | alt | 56.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +25.6) | — |
| [[LoVo (line)]] | wt | 17.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 34.0× (z +28.8) | [[Digitoxin (drug)]] 5 µM 0.119× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 71.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.9× (z +24.7) | — |
| [[NCI-H2347 (line)]] | alt | 14.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +17.7) | — |
| [[SNU-423 (line)]] | alt | 89.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +27.9) | — |
| [[HOP62 (line)]] | alt | 39.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +13.9) | — |
| [[HS-578T (line)]] | alt | 38.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +13.4) | [[Digitoxin (drug)]] 5 µM 0.266× (z -8.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 169 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +28.6) | — |
| [[SW 900 (line)]] | alt | 59.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +12.7) | — |
| [[AN3 CA (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0916× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[H4 (line)]] | wt | 60.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -10.6) ⚠ cell-cycle shift, explains ~13% of this change |
| [[HepG2_C3A (line)]] | wt | 148 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.36× (z +16.6) | — |
| [[hTERT-HPNE (line)]] | wt | 183 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -8.9) ⚠ cell-cycle shift, explains ~13% of this change |
| [[NCI-H1792 (line)]] | alt | 47.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +12.3) | — |
| [[RKO (line)]] | wt | 36.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -9.5) |
| [[SW 1271 (line)]] | alt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.5× (z +11.8) | — |
| [[BT-474 (line)]] | alt | 7.12 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.97 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.09 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 9.45 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.31 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.59 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.34 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5158), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LURAP1L-AS1]] | +0.73 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[RIPK2-DT]] | +0.65 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[PRECSIT]] | +0.64 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[CFL2]] | +0.64 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[DST]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[ZMYM4]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ZXDB]] | +0.60 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[USP40]] | +0.60 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[COL12A1]] | +0.59 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[TIAM2]] | +0.59 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[LINC01435]] | +0.59 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[USP16]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBH1]] | -0.62 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[CTNNBIP1]] | -0.62 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[SRGAP2D]] | -0.62 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[STARD3]] | -0.61 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[SMARCD2]] | -0.61 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[SNHG30]] | -0.60 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[SDHAP2]] | -0.60 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[CCT6P3-1]] | -0.60 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[ZNF250]] | -0.59 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[SMG1P5]] | -0.59 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.59 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[ZMYND19]] | -0.58 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01435]] | B | LINC01435 activity raises SYNE1's level | lines that do not express LINC01435 (37) vs lines expressing it (13) | 3.20× lower at baseline in the lines without LINC01435 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000203434, TMPRSS15, ENSG00000224865 |
| [[ADAMTS1]] | B | ADAMTS1 activity raises SYNE1's level | lines that do not express ADAMTS1 (26) vs lines expressing it (24) | 3.38× lower at baseline in the lines without ADAMTS1 | 0.029 | ⚠ within organs, on part of the lines; also absent: SALL1, ENSG00000289600, ADAM12 |
| [[ALPK2]] | B | ALPK2 activity raises SYNE1's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 3.62× lower at baseline in the lines without ALPK2 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4 |
| [[NMRAL2P-1]] | B | NMRAL2P-1 activity raises SYNE1's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.69× lower at baseline in the lines without NMRAL2P-1 | 0.068 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[SYNPO]] | B | SYNPO activity raises SYNE1's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 2.61× lower at baseline in the lines without SYNPO | 0.079 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[ZNF474]] | B | ZNF474 activity raises SYNE1's level | lines that do not express ZNF474 (6) vs lines expressing it (44) | 3.91× lower at baseline in the lines without ZNF474 | 0.088 | ⚠ within organs, on part of the lines; also absent: RBFOX1, NEK10, LINC01524; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZXDA]] | B | SYNE1 activity lowers ZXDA's level | lines that do not express SYNE1 (10) vs lines expressing it (40) | 1.35× higher at baseline in the lines without SYNE1 | 0.098 | ⚠ within organs, on part of the lines; also absent: DPYS, SGCE, SPX |

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.504). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (15.7, 13.0); signed map (24.4, 4.9). **Vector** length 118, 31.5% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.5 | +23.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.5 | +37.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.0 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.7 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.5 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.5 | +12.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.7 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +4.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -0.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -3.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.9 | -0.8 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | spectrin repeat containing nuclear envelope protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.2 — chr6:152,121,687-152,637,801 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SYNE-1B, KIAA0796, 8B, Nesprin-1, enaptin, MYNE1, CPG2, dJ45H2.2; previously C6orf98 |
| Gene groups (HGNC) | Spectrin repeat containing nuclear envelope family; KASH domain containing |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 4 pathways, smallest: Meiotic synapsis; Meiosis; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NF91](https://www.uniprot.org/uniprotkb/Q8NF91) (Nesprin-1):

> Multi-isomeric modular protein which forms a linking network between organelles and the actin cytoskeleton to maintain the subcellular spatial organization. As a component of the LINC (LInker of Nucleoskeleton and Cytoskeleton) complex involved in the connection between the nuclear lamina and the cytoskeleton. The nucleocytoplasmic interactions established by the LINC complex play an important role in the transmission of mechanical forces across the nuclear envelope and in nuclear movement and …

**Summary**, from NCBI Gene [23345](https://www.ncbi.nlm.nih.gov/gene/23345):

> This gene encodes a spectrin repeat containing protein expressed in skeletal and smooth muscle, and peripheral blood lymphocytes, that localizes to the nuclear membrane. Mutations in this gene have been associated with autosomal recessive spinocerebellar ataxia 8, also referred to as autosomal recessive cerebellar ataxia type 1 or recessive ataxia of Beauce. Alternatively spliced transcript variants encoding different isoforms have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17089](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17089) · Entrez [23345](https://www.ncbi.nlm.nih.gov/gene/23345) · UniProt [Q8NF91](https://www.uniprot.org/uniprotkb/Q8NF91) · Ensembl [ENSG00000131018](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131018)

## Data

Gene col 5158: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5158); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5158, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5158]; `tensor/DDL_lfc|DDL_z.npy` [5158]; `embed/gene_vectors.npy` [5158]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5158 or target_col == 5158). Every well: [[SYNE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYNE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
