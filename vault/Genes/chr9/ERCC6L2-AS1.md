---
symbol: "ERCC6L2-AS1"
type: "gene"
col: 10633
ensembl_id: "ENSG00000175611"
name: "ERCC6L2 antisense RNA 1"
location: "9q22.32"
module: 23
arm: "+"
pooled_cpm: 10.84
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 12
n_dd_up_clean: 23
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ERCC6L2-AS1

*ERCC6L2 antisense RNA 1* — 9q22.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.13× (z +28.2, q 0e+00, up in 44 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.546× (z -7.4, q 1e-10, down in 30 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.566× (z -6.9, q 1e-09, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (70 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 30 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PBLD]] (+0.84, fdr 3e-04), [[LINC01004]] (+0.82, fdr 3e-05), [[PCNX4-DT]] (+0.82, fdr 4e-05); moves opposite to [[MAST3]] (-0.72, fdr 6e-04), [[ANKRD27]] (-0.71, fdr 1e-03, ⚠ one half only (not replicated)), [[NPHP4]] (-0.69, fdr 2e-04), [[GPRIN1]] (-0.69, fdr 3e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10633.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.13×** | +28.2 | 0e+00 | 44/44 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.89×** | +18.6 | 0e+00 | 37/43 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.72×** | +17.2 | 0e+00 | 39/44 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.55×** | +14.9 | 0e+00 | 38/45 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.20×** | +13.6 | 4e-40 | 40/48 (J82, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.94×** | +13.1 | 2e-37 | 41/45 (C32, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.80×** | +12.1 | 9e-32 | 32/39 (MIA PaCa-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.66×** | +8.7 | 2e-16 | 29/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.63×** | +5.9 | 2e-07 | 22/47 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +5.8 | 5e-07 | 22/47 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +5.3 | 7e-06 | 20/47 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +4.4 | 4e-04 | 17/48 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.38×** | +3.9 | 0.003 | 13/47 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.005 | 10/47 (LoVo, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.006 | 17/46 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.007 | 9/48 (LoVo, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10633.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.546×** | -7.4 | 1e-10 | 30/46 (SW1417, J82, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.566×** | -6.9 | 1e-09 | 28/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.588×** | -6.1 | 2e-07 | 25/46 (SW480, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.620×** | -5.8 | 9e-07 | 23/45 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.691×** | -4.5 | 8e-04 | 20/47 (SW480, HCT15, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.694×** | -4.4 | 9e-04 | 19/48 (PANC-1, SW480, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.719×** | -4.0 | 0.005 | 20/47 (LS 180, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.569×** | -3.6 | 0.024 | 15/45 (LOX-IMVI, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.750×** | -3.5 | 0.031 | 13/47 (RPMI-7951, C32, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.752×** | -3.3 | 0.051 | 15/39 (SK-MEL-2, HS-578T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.832×** | -3.1 | 0.083 | 15/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.773×** | -3.1 | 0.083 | 12/47 (LOX-IMVI, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10633. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.70 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.1× (z +17.8) | — |
| [[C32 (line)]] | wt | 12.3 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.99× (z +12.5) | — |
| [[HEC-1-A (line)]] | alt | 16.3 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.48× (z +17.8) | — |
| [[HOP62 (line)]] | alt | 8.24 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.73× (z +12.9) | — |
| [[J82 (line)]] | alt | 6.08 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.25× (z +12.9) | [[Digitoxin (drug)]] 5 µM 0.106× (z -9.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 22.2 | 4 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +11.8) | [[Ixazomib citrate (drug)]] 5 µM 0.258× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 5.51 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.87× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.58 | 4 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 25.0× (z +14.0) | — |
| [[HCT15 (line)]] | alt | 13.2 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.46× (z +11.6) | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0746× (z -9.5) |
| [[HT-29 (line)]] | alt | 13.5 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +9.9) | — |
| [[KATO III (line)]] | alt | 14.0 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +10.3) | — |
| [[LoVo (line)]] | wt | 11.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +12.7) | — |
| [[SNU-423 (line)]] | alt | 20.1 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +11.7) | [[Digitoxin (drug)]] 5 µM 0.180× (z -9.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 12.7 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +13.4) | [[Digitoxin (drug)]] 5 µM 0.140× (z -10.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 4.29 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.75× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 3.24 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.62× (z +10.2) | [[Talc (drug)]] 0.05 µM 0.0678× (z -8.6) |
| [[HS-578T (line)]] | alt | 6.47 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +13.3) | — |
| [[LS 180 (line)]] | wt | 20.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +10.9) | [[Docetaxel (drug)]] 0.05 µM 0.233× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 8.41 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.47× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 10.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +14.2) | — |
| [[Panc 03.27 (line)]] | alt | 9.50 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.05× (z +13.2) | — |
| [[RKO (line)]] | wt | 21.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +13.0) | — |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 1 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.85× (z +8.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.111× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[SW48 (line)]] | wt | 12.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.78× (z +9.4) | [[Pentoxifylline (drug)]] 0.5 µM 0.0710× (z -9.2) |
| [[A498 (line)]] | wt | 7.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.6× (z +18.2) | — |
| [[BT-474 (line)]] | alt | 5.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.8× (z +13.4) | — |
| [[NCI-H1573 (line)]] | alt | 9.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 5.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.70× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 5.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 11.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +14.3) | — |
| [[RPMI-7951 (line)]] | alt | 24.9 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 20.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +12.6) | — |
| [[SW 900 (line)]] | alt | 8.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.28× (z +10.0) | — |
| [[A-427 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10633), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 27 of them with an alert (⚠; 27 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBLD]] | +0.84 | +0.85 / +0.27 | both halves | 3e-04 |  |
| [[LINC01004]] | +0.82 | +0.80 / +0.43 | both halves | 3e-05 |  |
| [[PCNX4-DT]] | +0.82 | +0.84 / +0.41 | both halves | 4e-05 |  |
| [[THAP2]] | +0.81 | +0.83 / +0.46 | both halves | 3e-05 |  |
| [[TMEM202-AS1]] | +0.81 | +0.81 / +0.32 | both halves | 2e-04 | same gene group |
| [[MFF-DT]] | +0.81 | +0.75 / +0.34 | both halves | 1e-04 |  |
| [[MAILR]] | +0.80 | +0.81 / +0.38 | both halves | 6e-05 |  |
| [[MMADHC-DT]] | +0.79 | +0.83 / +0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[INO80D]] | +0.79 | +0.78 / +0.30 | both halves | 2e-04 |  |
| [[RFX3-DT]] | +0.78 | +0.80 / +0.34 | both halves | 1e-04 |  |
| [[PPP1R12A-AS2]] | +0.77 | +0.81 / +0.11 | ⚠ one half (not replicated) | 0.002 | same gene group |
| [[AK9]] | +0.77 | +0.84 / +0.33 | both halves | 1e-04 |  |
| [[WAC-AS1]] | +0.77 | +0.77 / +0.41 | both halves | 4e-05 | same gene group |
| [[KRBA2]] | +0.77 | +0.75 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | -0.72 | -0.66 / -0.21 | both halves | 6e-04 |  |
| [[ANKRD27]] | -0.71 | -0.72 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[NPHP4]] | -0.69 | -0.61 / -0.30 | both halves | 2e-04 |  |
| [[GPRIN1]] | -0.69 | -0.52 / -0.27 | both halves | 3e-04 |  |
| [[CEP131]] | -0.68 | -0.58 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[CAMK2G]] | -0.68 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[LPCAT4]] | -0.68 | -0.74 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[GNA12]] | -0.68 | -0.70 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ERCC6L2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.843). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (3.6, 14.5); signed map (24.2, -9.8). **Vector** length 102, 24.0% of its response variance represented; |z| ≥ 3 in 1,176 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.0 | +13.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +28.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +7.1 | +13.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +17.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +18.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +3.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +4.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -8.2 | -5.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -8.1 | -4.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.9 | -1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.5 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.7 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -4.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.4 | -2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | ERCC6L2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9q22.32 — chr9:95,759,231-95,876,049 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C9orf130, LINC00476 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q8WZB0](https://www.uniprot.org/uniprotkb/Q8WZB0) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27858) · Entrez [100128782](https://www.ncbi.nlm.nih.gov/gene/100128782) · UniProt [Q8WZB0](https://www.uniprot.org/uniprotkb/Q8WZB0) · Ensembl [ENSG00000175611](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175611)

## Data

Gene col 10633: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10633); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10633, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10633]; `tensor/DDL_lfc|DDL_z.npy` [10633]; `embed/gene_vectors.npy` [10633]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10633 or target_col == 10633). Every well: [[ERCC6L2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERCC6L2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
