---
symbol: "HACE1"
type: "gene"
col: 1424
ensembl_id: "ENSG00000085382"
name: "HECT domain and ankyrin repeat containing E3 ubiquitin protein ligase 1"
location: "6q16.3"
module: 65
arm: "+"
pooled_cpm: 61.48
n_lines_expressing: 47
n_dd_up: 1
n_dd_down: 27
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 16
direction_downstream: 32
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# HACE1

*HECT domain and ankyrin repeat containing E3 ubiquitin protein ligase 1* — 6q16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.22× (z +4.0, q 0.041, up in 21 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.232× (z -29.3, q 0e+00, down in 44 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL6]] (+0.82, fdr 7e-06), [[ATG4C]] (+0.81, fdr 7e-06), [[FAM234B]] (+0.80, fdr 7e-06); moves opposite to [[PPP3CB-AS1]] (-0.75, fdr 1e-05), [[LINC00571]] (-0.75, fdr 1e-05), [[WARS2-AS1]] (-0.75, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[MPP2]] → it (grade B ⚠); 32 go from it, the strongest it → [[SH3PXD2B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1424.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.041 | 21/45 (LoVo, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.27× | +3.4 | 0.13 | 24/45 (KATO III, LS 180, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.57× | +3.3 | 0.13 | 20/46 (A-427, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | 1.26× | +3.3 | 0.13 | 21/45 (PANC-1, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | 1.27× | +3.2 | 0.13 | 18/45 (SHP-77, C-33 A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | 1.54× | +3.2 | 0.13 | 23/46 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1424.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.232×** | -29.3 | 0e+00 | 44/45 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.317×** | -16.3 | 0e+00 | 44/45 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.462×** | -15.5 | 0e+00 | 39/45 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.364×** | -14.3 | 2e-44 | 40/46 (HCT15, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.352×** | -14.2 | 6e-44 | 43/45 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.380×** | -13.2 | 8e-38 | 35/41 (MIA PaCa-2, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.438×** | -11.7 | 1e-29 | 38/45 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.442×** | -11.6 | 4e-29 | 39/45 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.588×** | -10.6 | 1e-24 | 42/45 (SNU-423, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.451×** | -10.4 | 1e-23 | 40/43 (H4, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.523×** | -9.2 | 2e-18 | 38/45 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.543×** | -8.6 | 3e-16 | 43/45 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.591×** | -7.2 | 3e-11 | 34/45 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.621×** | -6.7 | 6e-10 | 36/45 (NCI-H460, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.625×** | -6.6 | 1e-09 | 38/45 (C32, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.618×** | -6.5 | 2e-09 | 33/47 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.429×** | -6.3 | 1e-08 | 33/46 (HOP62, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.693×** | -5.2 | 6e-06 | 36/45 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.700×** | -4.9 | 3e-05 | 27/45 (NCI-H460, C32, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.562×** | -4.3 | 5e-04 | 27/45 (C32, Hs 766T, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1424. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 90.9 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -26.2) |
| [[NCI-H460 (line)]] | wt | 49.3 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -30.5) |
| [[MIA PaCa-2 (line)]] | alt | 108 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0990× (z -22.0) |
| [[HS-578T (line)]] | alt | 83.4 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -21.2) |
| [[SNU-423 (line)]] | alt | 118 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -27.4) |
| [[NCI-H2030 (line)]] | alt | 117 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -24.8) |
| [[A-172 (line)]] | wt | 66.4 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -26.2) |
| [[HOP62 (line)]] | alt | 67.5 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -23.8) |
| [[A498 (line)]] | wt | 51.6 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -14.5) |
| [[A549 (line)]] | wt | 50.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -17.5) |
| [[Hs 766T (line)]] | wt | 52.0 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -18.0) |
| [[PANC-1 (line)]] | alt | 61.6 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -23.2) |
| [[SNU-1 (line)]] | wt | 79.2 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -12.1) |
| [[SW480 (line)]] | alt | 42.2 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -15.9) |
| [[HCT15 (line)]] | alt | 73.5 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0594× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.198× (z -15.4) |
| [[HEC-1-A (line)]] | alt | 53.5 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -16.2) |
| [[hTERT-HPNE (line)]] | wt | 76.9 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -15.9) |
| [[NCI-H1573 (line)]] | alt | 24.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -14.3) |
| [[SW 900 (line)]] | alt | 59.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -16.4) |
| [[H4 (line)]] | wt | 92.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -22.7) |
| [[J82 (line)]] | alt | 68.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -21.5) |
| [[LOX-IMVI (line)]] | wt | 88.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -21.4) |
| [[NCI-H1792 (line)]] | alt | 97.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -20.2) |
| [[NCI-H2347 (line)]] | alt | 34.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -13.6) |
| [[RPMI-7951 (line)]] | alt | 68.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -20.1) |
| [[AN3 CA (line)]] | alt | 201 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0721× (z -16.8) |
| [[KATO III (line)]] | alt | 40.0 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.246× (z -15.2) |
| [[LoVo (line)]] | wt | 36.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -14.4) |
| [[SK-MEL-2 (line)]] | alt | 56.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.278× (z -9.9) |
| [[C-33 A (line)]] | alt | 253 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -10.5) |
| [[CHP-212 (line)]] | wt | 81.2 | 0 | 3 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0744× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 75.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -23.0) |
| [[Panc 03.27 (line)]] | alt | 35.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -12.2) |
| [[A-427 (line)]] | wt | 91.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -11.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 42.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 32.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -19.3) |
| [[LS 180 (line)]] | wt | 31.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -17.1) |
| [[SHP-77 (line)]] | alt | 112 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -14.6) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 68.0 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0595× (z -8.8) |
| [[SW 1271 (line)]] | alt | 89.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -10.7) |
| [[SW48 (line)]] | wt | 77.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -12.8) |
| [[HepG2_C3A (line)]] | wt | 28.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -10.6) |
| [[NCI-H661 (line)]] | alt | 77.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0738× (z -12.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 51.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -9.1) |
| [[SW1417 (line)]] | alt | 26.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.67 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1424), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL6]] | +0.82 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[ATG4C]] | +0.81 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[FAM234B]] | +0.80 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[VDAC3]] | +0.78 | +0.82 / +0.62 | both halves | 7e-06 |  |
| [[WASF3]] | +0.77 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[CDON]] | +0.76 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[SCAI]] | +0.75 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[POT1]] | +0.75 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[ARRB2]] | +0.75 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[PAPSS1]] | +0.73 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[NBPF3]] | +0.73 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[SNAPC3]] | +0.73 | +0.72 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP3CB-AS1]] | -0.75 | -0.69 / -0.51 | both halves | 1e-05 |  |
| [[LINC00571]] | -0.75 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | -0.75 | -0.74 / -0.50 | both halves | 1e-05 |  |
| [[INO80D]] | -0.73 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | -0.73 | -0.71 / -0.44 | both halves | 3e-05 |  |
| [[PCF11]] | -0.72 | -0.75 / -0.38 | both halves | 7e-05 |  |
| [[RAB30-DT]] | -0.71 | -0.71 / -0.53 | both halves | 1e-05 |  |
| [[ST7L]] | -0.71 | -0.74 / -0.40 | both halves | 4e-05 |  |
| [[C11orf58]] | -0.70 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[ARRDC3-AS1]] | -0.70 | -0.75 / -0.35 | both halves | 1e-04 |  |
| [[CCDC90B-AS1]] | -0.70 | -0.71 / -0.31 | both halves | 2e-04 |  |
| [[LINC01004]] | -0.69 | -0.66 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 13, C 3. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPP2]] | B | MPP2 activity raises HACE1's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 3.29× lower at baseline in the lines without MPP2 | 5e-04 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[STARD9]] | B | STARD9 activity raises HACE1's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 2.98× lower at baseline in the lines without STARD9 | 0.001 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[SLC22A3]] | B | SLC22A3 activity lowers HACE1's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 2.15× higher at baseline in the lines without SLC22A3 | 0.007 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[KATNAL1]] | B | KATNAL1 activity raises HACE1's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 2.64× lower at baseline in the lines without KATNAL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[SNTA1]] | B | SNTA1 activity raises HACE1's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 2.70× lower at baseline in the lines without SNTA1 | 0.012 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises HACE1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00888]] | B | LINC00888 activity raises HACE1's level | lines that do not express LINC00888 (7) vs lines expressing it (43) | 2.25× lower at baseline in the lines without LINC00888 | 0.041 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KIF3C, TBKBP1, GDAP1; maybe low, not absent |
| [[PMP22]] | B | PMP22 activity raises HACE1's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 1.88× lower at baseline in the lines without PMP22 | 0.055 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[ZHX2]] | B | ZHX2 activity strengthens HACE1's drug response | lines that do not express ZHX2 (7) vs lines expressing it (39) | the lines without ZHX2 respond 0.74× as strongly (z diff +0.84); strongest at Ouabain (Octahydrate) 5 µM: 0.79x vs 0.43x (z diff +4.5) | 0.075 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1; target measured in part of the lines; artifact flags |
| [[LIX1L]] | B | LIX1L activity raises HACE1's level | lines that do not express LIX1L (10) vs lines expressing it (38) | 2.12× lower at baseline in the lines without LIX1L | 0.089 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |
| [[LINC00857]] | B | LINC00857 activity lowers HACE1's level | lines that do not express LINC00857 (17) vs lines expressing it (33) | 1.91× higher at baseline in the lines without LINC00857 | 0.092 | ⚠ within organs, on part of the lines; also absent: KRT18, C19orf33, OCLN |
| [[TTLL7]] | B | TTLL7 activity raises HACE1's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 1.81× lower at baseline in the lines without TTLL7 | 0.093 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725 |

### Downstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 0, C 32. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH3PXD2B]] | C | HACE1 activity raises SH3PXD2B's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 4.12× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; co-absent with the target; its own permutation p |
| [[DNMT3B]] | C | HACE1 activity raises DNMT3B's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 3.99× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[SEPTIN6]] | C | HACE1 activity raises SEPTIN6's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 3.32× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[FAM234B]] | C | HACE1 activity raises FAM234B's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 2.98× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; co-absent with the target; its own permutation p |
| [[HDHD5]] | C | HACE1 activity raises HDHD5's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 2.81× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[SKP2]] | C | HACE1 activity raises SKP2's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 2.10× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[PRMT7]] | C | HACE1 activity raises PRMT7's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[CABIN1]] | C | HACE1 activity raises CABIN1's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[TRIT1]] | C | HACE1 activity raises TRIT1's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 2.01× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[GTPBP3]] | C | HACE1 activity raises GTPBP3's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.85× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[METTL17]] | C | HACE1 activity raises METTL17's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.71× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[REPS1]] | C | HACE1 activity raises REPS1's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.56× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.787). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (2.9, -10.3); signed map (-33.1, -7.4). **Vector** length 113, 38.4% of its response variance represented; |z| ≥ 3 in 1,188 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.4 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | +2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.9 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +4.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.8 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +0.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.6 | +2.2 |
|  | [[Fumaric acid (drug)]] 5 µM |  | +2.0 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.5 | -16.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -15.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.4 | -10.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -14.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.3 | -29.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -5.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.8 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | HECT domain and ankyrin repeat containing E3 ubiquitin protein ligase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.3 — chr6:104,728,094-104,859,919 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1320 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; HECT domain E3 ubiquitin protein ligases |
| Reactome | 8 pathways, smallest: Activation of STAT3 by cadherin engagement; Adherens junctions interactions; Cell-cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYU2](https://www.uniprot.org/uniprotkb/Q8IYU2) (E3 ubiquitin-protein ligase HACE1):

> E3 ubiquitin-protein ligase involved in Golgi membrane fusion and regulation of small GTPases. Acts as a regulator of Golgi membrane dynamics during the cell cycle: recruited to Golgi membrane by Rab proteins and regulates postmitotic Golgi membrane fusion. Acts by mediating ubiquitination during mitotic Golgi disassembly, ubiquitination serving as a signal for Golgi reassembly later, after cell division. Specifically binds GTP-bound RAC1, mediating ubiquitination and subsequent degradation of …

**Summary**, from NCBI Gene [57531](https://www.ncbi.nlm.nih.gov/gene/57531):

> This gene encodes a HECT domain and ankyrin repeat-containing ubiquitin ligase. The encoded protein is involved in specific tagging of target proteins, leading to their subcellular localization or proteasomal degradation. The protein is a potential tumor suppressor and is involved in the pathophysiology of several tumors, including Wilm's tumor. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:21033](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21033) · Entrez [57531](https://www.ncbi.nlm.nih.gov/gene/57531) · UniProt [Q8IYU2](https://www.uniprot.org/uniprotkb/Q8IYU2) · Ensembl [ENSG00000085382](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085382)

## Data

Gene col 1424: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1424); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1424, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1424]; `tensor/DDL_lfc|DDL_z.npy` [1424]; `embed/gene_vectors.npy` [1424]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1424 or target_col == 1424). Every well: [[HACE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HACE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
