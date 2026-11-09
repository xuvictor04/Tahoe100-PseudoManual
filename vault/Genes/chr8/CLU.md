---
symbol: "CLU"
type: "gene"
col: 4231
ensembl_id: "ENSG00000120885"
name: "clusterin"
location: "8p21.1"
module: 60
arm: "+"
pooled_cpm: 87.73
n_lines_expressing: 39
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 8
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# CLU

*clusterin* — 8p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (14 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 5.34× (z +16.6, q 0e+00, up in 34 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0413×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2H]] (+0.58, fdr 3e-05), [[HSPB1]] (+0.58, fdr 1e-05), [[SORBS1]] (+0.55, fdr 2e-05); moves opposite to [[UBIAD1]] (-0.57, fdr 3e-05), [[CAD]] (-0.54, fdr 2e-05), [[SRM]] (-0.51, fdr 2e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[CTNNA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4231.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **5.34×** | +16.6 | 0e+00 | 34/37 (HEC-1-A, HCT15, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **5.07×** | +16.0 | 0e+00 | 37/37 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **3.04×** | +15.5 | 0e+00 | 37/37 (LS 180, RKO, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **3.03×** | +15.5 | 0e+00 | 32/37 (NCI-H2030, HOP62, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.61×** | +15.1 | 0e+00 | 37/37 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.18×** | +14.1 | 3e-43 | 36/37 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.95×** | +13.0 | 6e-37 | 31/32 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.65×** | +12.1 | 8e-32 | 35/37 (HEC-1-A, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.36×** | +11.1 | 1e-26 | 33/34 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.02×** | +10.9 | 5e-26 | 34/37 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.96×** | +10.7 | 4e-25 | 33/37 (HEC-1-A, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.86×** | +10.4 | 1e-23 | 33/37 (NCI-H23, HCT15, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +10.0 | 6e-22 | 35/38 (HepG2/C3A, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **6.17×** | +9.4 | 2e-19 | 32/33 (HEC-1-A, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.32×** | +8.3 | 3e-15 | 35/37 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.28×** | +8.2 | 1e-14 | 28/37 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.00×** | +6.9 | 2e-10 | 31/37 (NCI-H23, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.6 | 6e-07 | 32/37 (A-172, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +5.6 | 8e-07 | 27/39 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.31×** | +4.9 | 2e-05 | 23/38 (HEC-1-A, LS 180, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4231.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0413×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Folic acid (drug)]] 5 µM |  | 0.775× | -3.6 | 0.13 | 24/37 (A498, KATO III, …) | inconsistent across doses | position effect removed |
| [[Pentagastrin (drug)]] 5 µM |  | 0.778× | -3.5 | 0.13 | 19/37 (H4, HCT15, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4231. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 72.4 | 16 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.87× (z +21.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 12.8× (z +17.8) | — |
| [[LS 180 (line)]] | wt | 23.4 | 14 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 9.80× (z +16.7) | — |
| [[SW480 (line)]] | alt | 65.2 | 14 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 7.62× (z +15.3) | — |
| [[HEC-1-A (line)]] | alt | 52.0 | 13 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 17.6× (z +21.4) | — |
| [[HOP62 (line)]] | alt | 38.4 | 13 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +22.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 4.46× (z +13.5) | — |
| [[KATO III (line)]] | alt | 68.8 | 12 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 12.9× (z +14.9) | — |
| [[HCT15 (line)]] | alt | 82.4 | 11 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 24.3× (z +17.8) | — |
| [[RKO (line)]] | wt | 42.0 | 10 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 5.40× (z +14.2) | — |
| [[SW48 (line)]] | wt | 61.4 | 10 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 24.0× (z +15.9) | — |
| [[A498 (line)]] | wt | 43.9 | 9 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.56× (z +13.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 32.9 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +12.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 8.85× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 59.3 | 8 (4 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.18× (z +11.7) | — |
| [[A549 (line)]] | wt | 128 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.00× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.46× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 134 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.36× (z +12.1) | — |
| [[C-33 A (line)]] | alt | 34.6 | 6 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 5.62× (z +10.0) | — |
| [[H4 (line)]] | wt | 139 | 6 | 0 | [[Bortezomib (drug)]] 0.05 µM 5.09× (z +10.6) | — |
| [[J82 (line)]] | alt | 41.4 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.62× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 93.9 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 21.0× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.85× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 43.2 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.46× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 107 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 15.3× (z +17.7) | — |
| [[A-172 (line)]] | wt | 239 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 99.6 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 11.5× (z +16.0) | — |
| [[CFPAC-1 (line)]] | alt | 26.7 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.62× (z +18.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.36× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 25.3 | 5 | 0 | [[Auranofin (drug)]] 5 µM 17.9× (z +14.7) | — |
| [[NCI-H2030 (line)]] | alt | 210 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.98× (z +22.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.05× (z +15.1) | — |
| [[NCI-H460 (line)]] | wt | 205 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.43× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 104 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HepG2_C3A (line)]] | wt | 130 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 99.1 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +15.3) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[AN3 CA (line)]] | alt | 47.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +9.2) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 77.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +11.9) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[Hs 766T (line)]] | wt | 947 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H661 (line)]] | alt | 140 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0413× (z -14.4) |
| [[RPMI-7951 (line)]] | alt | 72.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.55× (z +9.2) | — |
| [[A-427 (line)]] | wt | 10.00 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.96 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 18.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 17.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.87 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4231), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2H]] | +0.58 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[HSPB1]] | +0.58 | +0.55 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS; STRING 464 |
| [[SORBS1]] | +0.55 | +0.48 / +0.63 | both halves | 2e-05 | pathway: HALLMARK_MYOGENESIS |
| [[ANXA1]] | +0.54 | +0.34 / +0.59 | both halves | 1e-04 | pathway: HALLMARK_APOPTOSIS; STRING 415 |
| [[CAST]] | +0.54 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[TMC1]] | +0.53 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[SOD1]] | +0.53 | +0.42 / +0.59 | both halves | 4e-05 | pathway: HALLMARK_APOPTOSIS |
| [[PSAP]] | +0.53 | +0.28 / +0.61 | both halves | 3e-04 | pathway: Platelet activation, signaling and aggregation |
| [[TAX1BP1]] | +0.52 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[MAPRE3]] | +0.51 | +0.50 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_MYOGENESIS |
| [[DSG2]] | +0.50 | +0.31 / +0.41 | both halves | 2e-04 |  |
| [[MAPRE2]] | +0.50 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBIAD1]] | -0.57 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[CAD]] | -0.54 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[SRM]] | -0.51 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[ENTR1]] | -0.50 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[SFXN2]] | -0.50 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[B4GALT2]] | -0.49 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[RFWD3]] | -0.49 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[C1orf109]] | -0.49 | -0.22 / -0.53 | both halves | 6e-04 |  |
| [[URB2]] | -0.48 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[LYAR]] | -0.48 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[DHX33]] | -0.47 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[ACTR3B]] | -0.47 | -0.19 / -0.39 | ⚠ not reproduced | 8e-04 |  |
| [[CDK10]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CLU's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MYH14]] | B | MYH14 activity lowers CLU's level | lines that do not express MYH14 (21) vs lines expressing it (29) | 2.13× higher at baseline in the lines without MYH14 | 0.048 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTNNA1]] | B | CLU activity lowers CTNNA1's level | lines that do not express CLU (11) vs lines expressing it (39) | 1.36× higher at baseline in the lines without CLU | 0.006 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ADSL]] | B | CLU activity raises ADSL's level | lines that do not express CLU (11) vs lines expressing it (39) | 1.49× lower at baseline in the lines without CLU | 0.014 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MYH14]] | B | CLU activity lowers MYH14's level | lines that do not express CLU (11) vs lines expressing it (39) | 3.47× higher at baseline in the lines without CLU | 0.016 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TIPIN]] | B | CLU activity raises TIPIN's level | lines that do not express CLU (11) vs lines expressing it (39) | 1.41× lower at baseline in the lines without CLU | 0.020 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HSPB1]] | B | CLU activity strengthens HSPB1's drug response | lines that do not express CLU (10) vs lines expressing it (37) | the lines without CLU respond 1.13× as strongly (z diff -0.13); strongest at Dinaciclib 0.5 µM: 2.50x vs 4.27x (z diff +2.5) | 0.033 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[MYO18A]] | B | CLU activity strengthens MYO18A's drug response | lines that do not express CLU (11) vs lines expressing it (37) | the lines without CLU respond 0.73× as strongly (z diff +0.86); strongest at Digitoxin 5 µM: 0.84x vs 0.59x (z diff +2.8) | 0.034 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[RAB11FIP1]] | B | CLU activity lowers RAB11FIP1's level | lines that do not express CLU (11) vs lines expressing it (39) | 1.93× higher at baseline in the lines without CLU | 0.048 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SKP1]] | B | CLU activity lowers SKP1's level | lines that do not express CLU (11) vs lines expressing it (39) | 1.13× higher at baseline in the lines without CLU | 0.093 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.395). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-11.4, 9.7); signed map (-11.1, 32.7). **Vector** length 91.2, 25.8% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +15.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +8.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.2 | +12.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.5 | +10.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.3 | +10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +16.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.2 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.3 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | +0.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | +0.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | clusterin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.1 — chr8:27,596,917-27,614,700 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SGP-2, SP-40, TRPM-2, KUB1, CLU1, CLU2; previously CLI, APOJ |
| Gene groups (HGNC) | Complement system regulators and receptors; MicroRNA protein coding host genes |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, COAGULATION, MYOGENESIS, APOPTOSIS, COMPLEMENT |
| Reactome | 13 pathways, smallest: Terminal pathway of complement; Antimicrobial peptides; Regulation of Complement cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [P10909](https://www.uniprot.org/uniprotkb/P10909) (Clusterin):

> [Isoform 1]: Functions as extracellular chaperone that prevents aggregation of non native proteins. Prevents stress-induced aggregation of blood plasma proteins. Inhibits formation of amyloid fibrils by APP, APOC2, B2M, CALCA, CSN3, SNCA and aggregation-prone LYZ variants (in vitro). Does not require ATP. Maintains partially unfolded proteins in a state appropriate for subsequent refolding by other chaperones, such as HSPA8/HSC70. Does not refold proteins by itself. Binding to cell surface …

**Summary**, from NCBI Gene [1191](https://www.ncbi.nlm.nih.gov/gene/1191):

> The protein encoded by this gene is a secreted chaperone that can under some stress conditions also be found in the cell cytosol. It has been suggested to be involved in several basic biological events such as cell death, tumor progression, and neurodegenerative disorders. Alternate splicing results in both coding and non-coding variants.[provided by RefSeq, May 2011]

**Accessions** — [HGNC:2095](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2095) · Entrez [1191](https://www.ncbi.nlm.nih.gov/gene/1191) · UniProt [P10909](https://www.uniprot.org/uniprotkb/P10909) · Ensembl [ENSG00000120885](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120885)

## Data

Gene col 4231: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4231); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4231, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4231]; `tensor/DDL_lfc|DDL_z.npy` [4231]; `embed/gene_vectors.npy` [4231]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4231 or target_col == 4231). Every well: [[CLU — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLU.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
