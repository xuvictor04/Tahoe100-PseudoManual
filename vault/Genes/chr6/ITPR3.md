---
symbol: "ITPR3"
type: "gene"
col: 1767
ensembl_id: "ENSG00000096433"
name: "inositol 1,4,5-trisphosphate receptor type 3"
location: "6p21.31"
module: 78
arm: "+"
pooled_cpm: 133.36
n_lines_expressing: 44
n_dd_up: 3
n_dd_down: 25
n_dd_up_clean: 0
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# ITPR3

*inositol 1,4,5-trisphosphate receptor type 3* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.41× (z +4.6, q 0.003, up in 22 of 43 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 2.86×, A-427 2.85×, LS 180 2.73×, COLO 205 3.97×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 3.30×, KATO III 2.66×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 2.63×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.572× (z -10.5, q 7e-23, down in 29 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEC]] (+0.71, fdr 7e-06), [[SLCO4A1]] (+0.66, fdr 1e-05), [[PLCB3]] (+0.65, fdr 7e-06); moves opposite to [[DCP1A]] (-0.62, fdr 2e-05), [[SPOP]] (-0.61, fdr 3e-05), [[GPBP1]] (-0.60, fdr 1e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PODXL]] → it (grade B ⚠); 3 go from it, the strongest it → [[ANXA5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1767.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 2.86×, A-427 2.85×, LS 180 2.73×, COLO 205 3.97×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 3.30×, KATO III 2.66×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 2.63×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +4.6 | 0.003 | 22/43 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +4.0 | 0.022 | 20/38 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +3.6 | 0.065 | 22/42 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.28× | +3.1 | 0.30 | 23/42 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1767.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.572×** | -10.5 | 7e-23 | 29/42 (NCI-H23, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.606×** | -9.4 | 1e-18 | 38/43 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.577×** | -7.3 | 5e-11 | 31/42 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.594×** | -6.9 | 7e-10 | 31/42 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.613×** | -6.2 | 5e-08 | 31/41 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.747×** | -5.3 | 1e-05 | 26/43 (C32, MIA PaCa-2, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.694×** | -4.8 | 1e-04 | 28/42 (HEC-1-A, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.696×** | -4.6 | 3e-04 | 24/42 (NCI-H23, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.782×** | -4.6 | 3e-04 | 28/42 (RKO, Hs 766T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.784×** | -4.5 | 3e-04 | 28/42 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.722×** | -4.2 | 0.002 | 25/41 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.744×** | -3.9 | 0.004 | 24/42 (SW48, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.782×** | -3.9 | 0.004 | 27/42 (MIA PaCa-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.571×** | -3.9 | 0.004 | 26/40 (HOP62, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.749×** | -3.8 | 0.005 | 25/43 (RKO, SK-MEL-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.762×** | -3.7 | 0.008 | 25/43 (MIA PaCa-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.593×** | -3.6 | 0.009 | 27/42 (RKO, J82, …) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.799×** | -3.2 | 0.036 | 22/44 (AsPC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | **0.784×** | -3.2 | 0.037 | 20/42 (SK-MEL-2, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1767. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 428 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -15.0) |
| [[MIA PaCa-2 (line)]] | alt | 354 | 0 | 7 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.664× (z -14.0) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -13.6) |
| [[LoVo (line)]] | wt | 89.6 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.30× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -15.7) |
| [[HOP62 (line)]] | alt | 234 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.240× (z -11.0) |
| [[RKO (line)]] | wt | 212 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -16.2) |
| [[A-427 (line)]] | wt | 66.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 257 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.324× (z -10.5) |
| [[HS-578T (line)]] | alt | 171 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -10.6) |
| [[LS 180 (line)]] | wt | 84.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -17.0) |
| [[A-172 (line)]] | wt | 206 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -9.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -8.7) |
| [[HCT15 (line)]] | alt | 100 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -13.5) |
| [[HT-29 (line)]] | alt | 160 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -12.4) |
| [[J82 (line)]] | alt | 122 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.294× (z -10.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.326× (z -9.8) |
| [[KATO III (line)]] | alt | 113 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 97.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -12.6) |
| [[NCI-H23 (line)]] | alt | 66.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -21.1) |
| [[RPMI-7951 (line)]] | alt | 123 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -14.2) |
| [[SK-MEL-2 (line)]] | alt | 85.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.5) |
| [[SNU-423 (line)]] | alt | 218 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.388× (z -9.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -9.4) |
| [[SW 1088 (line)]] | alt | 177 | 0 | 2 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0662× (z -11.3) |
| [[SW48 (line)]] | wt | 109 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -10.4) |
| [[BT-474 (line)]] | alt | 74.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -17.0) |
| [[C32 (line)]] | wt | 41.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.294× (z -8.7) |
| [[COLO 205 (line)]] | alt | 49.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +9.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 156 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.309× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 81.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -8.5) |
| [[PANC-1 (line)]] | alt | 145 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -10.7) |
| [[SW 900 (line)]] | alt | 56.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -10.4) |
| [[SW480 (line)]] | alt | 128 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -9.7) |
| [[A498 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.9 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 92.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 170 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.0 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 152 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1767), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEC]] | +0.71 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[SLCO4A1]] | +0.66 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[PLCB3]] | +0.65 | +0.72 / +0.59 | both halves | 7e-06 | pathway: Beta-catenin independent WNT signaling; STRING 967 |
| [[INF2]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[ARHGAP4]] | +0.64 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[MAPKAPK3]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 | pathway: Signaling by VEGF |
| [[ARHGDIA]] | +0.62 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[FLNA]] | +0.62 | +0.57 / +0.63 | both halves | 9e-06 | pathway: Platelet activation, signaling and aggregation |
| [[PLXNA1]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[CAPRIN2]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ACTN1]] | +0.60 | +0.63 / +0.56 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation |
| [[EHBP1L1]] | +0.60 | +0.68 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCP1A]] | -0.62 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[SPOP]] | -0.61 | -0.46 / -0.67 | both halves | 3e-05 |  |
| [[GPBP1]] | -0.60 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[PIGBOS1]] | -0.60 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[WDR83OS]] ⚠ | -0.57 | -0.45 / -0.59 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EAPP]] | -0.56 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[ZCCHC10]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[COIL]] | -0.55 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[TRAPPC2B]] | -0.55 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[RPRD2]] | -0.54 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[NDUFB4]] | -0.54 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[GTF2IRD2B]] | -0.54 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[PPP4R3A]] | -0.54 | -0.48 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PODXL]] | B | PODXL activity raises ITPR3's level | lines that do not express PODXL (24) vs lines expressing it (26) | 2.64× lower at baseline in the lines without PODXL | 0.003 | ⚠ within organs, on part of the lines; also absent: IL32, LGR6, SERPINB9; maybe low, not absent |
| [[CALB2]] | B | CALB2 activity raises ITPR3's level | lines that do not express CALB2 (23) vs lines expressing it (27) | 2.05× lower at baseline in the lines without CALB2 | 0.007 | ⚠ within organs, on part of the lines; also absent: CSF2, LINC02577, AADACP1 |
| [[SLCO4A1]] | B | SLCO4A1 activity raises ITPR3's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 2.57× lower at baseline in the lines without SLCO4A1 | 0.030 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises ITPR3's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[PLEC]] | C | PLEC activity raises ITPR3's level | lines that do not express PLEC (3) vs lines expressing it (47) | 3.93× lower at baseline in the lines without PLEC | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA5]] | B | ITPR3 activity raises ANXA5's level | lines that do not express ITPR3 (6) vs lines expressing it (44) | 2.15× lower at baseline in the lines without ITPR3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SAT1, LRRC8E, HTATIP2; its own permutation p |
| [[PAQR5]] | B | ITPR3 activity raises PAQR5's level | lines that do not express ITPR3 (6) vs lines expressing it (44) | 2.08× lower at baseline in the lines without ITPR3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SAT1, LRRC8E, HTATIP2; its own permutation p |
| [[FBRSL1]] | B | ITPR3 activity lowers FBRSL1's level | lines that do not express ITPR3 (6) vs lines expressing it (44) | 1.23× higher at baseline in the lines without ITPR3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SAT1, LRRC8E, HTATIP2; its own permutation p |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.9, -4.6); signed map (-8.0, 32.1). **Vector** length 126, 41.9% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +2.5 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | +4.0 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.7 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | -0.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +1.9 |
| fall | [[NG25 (drug)]] 5 µM |  | -5.7 | -3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.1 | -3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.7 | -3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.6 | -4.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -4.6 | -5.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | inositol 1,4,5-trisphosphate receptor type 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:33,620,365-33,696,574 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IP3R3 |
| Gene groups (HGNC) | Inositol 1,4,5-triphosphate receptors; Protein phosphatase 1 regulatory subunits |
| Reactome | 48 pathways, smallest: Elevation of cytosolic Ca2+ levels; Rituximab:MS4A1 (rituximab:CD20) targets B cells for antibody-dependent cellular cytotoxicity by NK cells; CLEC7A (Dectin-1) induces NFAT activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14573](https://www.uniprot.org/uniprotkb/Q14573) (Inositol 1,4,5-trisphosphate-gated calcium channel ITPR3):

> Inositol 1,4,5-trisphosphate-gated calcium channel that, upon 1D-myo-inositol 1,4,5-trisphosphate binding, transports calcium from the endoplasmic reticulum lumen to cytoplasm, thus releasing the intracellular calcium and therefore participates in cellular calcium ion homeostasis. 1D-myo-inositol 1,4,5-trisphosphate binds to the ligand-free channel without altering its global conformation, yielding the low-energy resting state, then progresses through resting-to preactivated transitions to the …

**Summary**, from NCBI Gene [3710](https://www.ncbi.nlm.nih.gov/gene/3710):

> This gene encodes a receptor for inositol 1,4,5-trisphosphate, a second messenger that mediates the release of intracellular calcium. The receptor contains a calcium channel at the C-terminus and the ligand-binding site at the N-terminus. Knockout studies in mice suggest that type 2 and type 3 inositol 1,4,5-trisphosphate receptors play a key role in exocrine secretion underlying energy metabolism and growth. [provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:6182](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6182) · Entrez [3710](https://www.ncbi.nlm.nih.gov/gene/3710) · UniProt [Q14573](https://www.uniprot.org/uniprotkb/Q14573) · Ensembl [ENSG00000096433](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000096433)

## Data

Gene col 1767: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1767); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1767, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1767]; `tensor/DDL_lfc|DDL_z.npy` [1767]; `embed/gene_vectors.npy` [1767]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1767 or target_col == 1767). Every well: [[ITPR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITPR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
