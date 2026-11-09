---
symbol: "SMAD3"
type: "gene"
col: 9394
ensembl_id: "ENSG00000166949"
name: "SMAD family member 3"
location: "15q22.33"
module: 78
arm: "+"
pooled_cpm: 560.12
n_lines_expressing: 44
n_dd_up: 6
n_dd_down: 47
n_dd_up_clean: 5
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 26
direction_downstream: 29
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# SMAD3

*SMAD family member 3* — 15q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.65× (z +6.9, q 2e-09, up in 30 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 47 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.179× (z -24.0, q 0e+00, down in 42 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFE2L3]] (+0.64, fdr 7e-06), [[MAP2K3]] (+0.61, fdr 1e-05), [[SYNJ2]] (+0.61, fdr 1e-05); moves opposite to [[XPOT]] (-0.55, fdr 3e-05), [[LINC00662]] (-0.53, fdr 1e-04), [[CMKLR2]] (-0.51, fdr 5e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[ARL14]] → it (grade B ⚠); 29 go from it, the strongest it → [[SHB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9394.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +6.9 | 2e-09 | 30/42 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.55×** | +6.1 | 3e-07 | 35/42 (BT-474, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.29×** | +6.0 | 3e-07 | 36/43 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +5.1 | 5e-05 | 33/42 (KATO III, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +4.8 | 2e-04 | 25/42 (BT-474, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.34×** | +4.1 | 0.004 | 27/41 (BT-474, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 47 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9394.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.179×** | -24.0 | 0e+00 | 42/42 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.185×** | -23.4 | 0e+00 | 42/42 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.418×** | -17.1 | 0e+00 | 38/43 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.321×** | -15.8 | 0e+00 | 42/42 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.383×** | -12.8 | 1e-35 | 38/41 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.445×** | -11.2 | 3e-27 | 39/43 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.452×** | -10.6 | 2e-24 | 37/39 (NCI-H1573, A549, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.521×** | -9.0 | 1e-17 | 35/42 (HOP62, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.535×** | -8.7 | 2e-16 | 35/42 (H4, RPMI-7951, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.401×** | -6.6 | 2e-09 | 40/42 (NCI-H1792, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.448×** | -5.8 | 3e-07 | 39/42 (NCI-H1792, A498, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.634×** | -5.6 | 1e-06 | 31/42 (COLO 205, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.471×** | -5.5 | 2e-06 | 38/42 (MIA PaCa-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.688×** | -5.2 | 9e-06 | 29/42 (H4, SNU-423, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.694×** | -5.1 | 2e-05 | 30/42 (H4, NCI-H1792, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.506×** | -4.9 | 2e-05 | 36/42 (NCI-H1792, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.516×** | -4.8 | 5e-05 | 36/42 (NCI-H1792, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.720×** | -4.5 | 2e-04 | 30/42 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.712×** | -4.5 | 2e-04 | 29/43 (H4, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9394. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 582 | 0 | 21 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.189× (z -15.0) |
| [[BT-474 (line)]] | alt | 270 | 7 (2 ⚠) | 9 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 4.78× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.171× (z -14.5) |
| [[LOX-IMVI (line)]] | wt | 402 | 0 | 14 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -15.9) |
| [[NCI-H1792 (line)]] | alt | 1,066 | 0 | 14 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -21.4) |
| [[HOP62 (line)]] | alt | 727 | 0 | 13 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.123× (z -23.1) |
| [[HS-578T (line)]] | alt | 560 | 3 | 10 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -20.4) |
| [[SK-MEL-2 (line)]] | alt | 394 | 0 | 13 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -21.3) |
| [[SNU-423 (line)]] | alt | 920 | 0 | 12 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -22.2) |
| [[NCI-H1573 (line)]] | alt | 804 | 4 (1 ⚠) | 7 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.69× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -23.3) |
| [[CFPAC-1 (line)]] | alt | 1,188 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.229× (z -17.0) |
| [[HEC-1-A (line)]] | alt | 834 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -27.2) |
| [[J82 (line)]] | alt | 556 | 1 | 8 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.140× (z -23.8) |
| [[PANC-1 (line)]] | alt | 1,042 | 1 | 8 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.47× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.108× (z -30.3) |
| [[SW 900 (line)]] | alt | 703 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -18.2) |
| [[A-172 (line)]] | wt | 213 | 3 | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.222× (z -13.4) |
| [[A498 (line)]] | wt | 752 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -17.3) |
| [[HepG2_C3A (line)]] | wt | 611 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.211× (z -17.1) |
| [[hTERT-HPNE (line)]] | wt | 572 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 490 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0956× (z -25.0) |
| [[Panc 03.27 (line)]] | alt | 834 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -20.2) |
| [[A549 (line)]] | wt | 1,576 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0781× (z -29.0) |
| [[COLO 205 (line)]] | alt | 855 | 1 | 6 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.66× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.142× (z -17.2) |
| [[Hs 766T (line)]] | wt | 620 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.138× (z -20.4) |
| [[LoVo (line)]] | wt | 346 | 4 (1 ⚠) | 3 | [[TAK-901 (drug)]] 5 µM 9.09× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.197× (z -21.5) |
| [[MIA PaCa-2 (line)]] | alt | 384 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.131× (z -22.0) |
| [[KATO III (line)]] | alt | 378 | 2 | 4 | [[Digitoxin (drug)]] 0.5 µM 3.01× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.213× (z -17.0) |
| [[RPMI-7951 (line)]] | alt | 504 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -14.4) |
| [[AsPC-1 (line)]] | alt | 859 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.101× (z -24.9) |
| [[HT-29 (line)]] | alt | 969 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0785× (z -17.9) |
| [[NCI-H2030 (line)]] | alt | 386 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -15.1) |
| [[NCI-H2347 (line)]] | alt | 466 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -15.2) |
| [[SW48 (line)]] | wt | 487 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0988× (z -19.1) |
| [[SW480 (line)]] | alt | 308 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -24.8) |
| [[C32 (line)]] | wt | 327 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -13.5) |
| [[CHP-212 (line)]] | wt | 433 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.227× (z -11.3) |
| [[LS 180 (line)]] | wt | 205 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -17.5) |
| [[SNU-1 (line)]] | wt | 182 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.247× (z -13.8) |
| [[SW 1271 (line)]] | alt | 698 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -15.0) |
| [[SW1417 (line)]] | alt | 322 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.385× (z -11.2) |
| [[HCT15 (line)]] | alt | 237 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.339× (z -10.2) |
| [[SW 1088 (line)]] | alt | 588 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.213× (z -9.2) |
| [[A-427 (line)]] | wt | 53.4 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 194 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 91.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 489 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 126 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 444 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.8 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 114 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 84.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9394), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFE2L3]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[MAP2K3]] | +0.61 | +0.56 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 422 |
| [[SYNJ2]] | +0.61 | +0.51 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[SHB]] | +0.59 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[ITGA3]] | +0.57 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[PMEPA1]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_TGF_BETA_SIGNALING; STRING 882 |
| [[RUNX1]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN; STRING 878 |
| [[CD44]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 690 |
| [[JAG1]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 523 |
| [[ECE1]] | +0.54 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[NCEH1]] | +0.53 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[FGD6]] | +0.53 | +0.50 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPOT]] | -0.55 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[LINC00662]] | -0.53 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[CMKLR2]] | -0.51 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[EIF2S2]] | -0.49 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[GARS1]] | -0.48 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[AARS1]] | -0.48 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[NARS1]] | -0.47 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[JDP2]] | -0.47 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[MIA2]] | -0.46 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[MTDH]] | -0.46 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[SARS1]] | -0.46 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[EPRS1]] | -0.46 | -0.36 / -0.44 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 21, C 5. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARL14]] | B | ARL14 activity raises SMAD3's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 1.99× lower at baseline in the lines without ARL14 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |
| [[AHR]] | B | AHR activity raises SMAD3's level | lines that do not express AHR (7) vs lines expressing it (43) | 3.02× lower at baseline in the lines without AHR | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[PLAU]] | B | PLAU activity raises SMAD3's level | lines that do not express PLAU (26) vs lines expressing it (24) | 2.35× lower at baseline in the lines without PLAU | 0.013 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[MIR3142HG]] | B | MIR3142HG activity raises SMAD3's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 2.15× lower at baseline in the lines without MIR3142HG | 0.016 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130 |
| [[RUNX1]] | B | RUNX1 activity raises SMAD3's level | lines that do not express RUNX1 (5) vs lines expressing it (45) | 4.26× lower at baseline in the lines without RUNX1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent |
| [[NRP2]] | B | NRP2 activity raises SMAD3's level | lines that do not express NRP2 (24) vs lines expressing it (26) | 2.04× lower at baseline in the lines without NRP2 | 0.024 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6 |
| [[PRKCA]] | B | PRKCA activity raises SMAD3's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 2.73× lower at baseline in the lines without PRKCA | 0.025 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[NHS]] | B | NHS activity raises SMAD3's level | lines that do not express NHS (17) vs lines expressing it (33) | 1.77× lower at baseline in the lines without NHS | 0.040 | ⚠ within organs, on part of the lines; also absent: ANKRD29, WNT7B, ABCC3 |
| [[F2RL1]] | B | F2RL1 activity raises SMAD3's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 1.76× lower at baseline in the lines without F2RL1 | 0.041 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |
| [[FGD6]] | B | FGD6 activity raises SMAD3's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 1.69× lower at baseline in the lines without FGD6 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[SDC4]] | B | SDC4 activity raises SMAD3's level | lines that do not express SDC4 (5) vs lines expressing it (45) | 4.49× lower at baseline in the lines without SDC4 | 0.060 | ⚠ within organs, on part of the lines; also absent: LAMB1, TGFBR2, PHLDA2; its own permutation p |
| [[SHB]] | B | SHB activity raises SMAD3's level | lines that do not express SHB (5) vs lines expressing it (45) | 3.89× lower at baseline in the lines without SHB | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 24, C 5. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SHB]] | B | SMAD3 activity raises SHB's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 3.20× lower at baseline in the lines without SMAD3 | 0.004 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[EHD1]] | B | SMAD3 activity raises EHD1's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 2.30× lower at baseline in the lines without SMAD3 | 0.005 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[SYNJ2]] | B | SMAD3 activity raises SYNJ2's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 3.29× lower at baseline in the lines without SMAD3 | 0.007 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[PKM]] | B | SMAD3 activity raises PKM's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 1.88× lower at baseline in the lines without SMAD3 | 0.009 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[SDC4]] | B | SMAD3 activity raises SDC4's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 4.47× lower at baseline in the lines without SMAD3 | 0.012 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[PRKCA]] | B | SMAD3 activity raises PRKCA's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 2.72× lower at baseline in the lines without SMAD3 | 0.013 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[PMEPA1]] | B | SMAD3 activity raises PMEPA1's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 2.79× lower at baseline in the lines without SMAD3 | 0.017 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[CAB39]] | B | SMAD3 activity raises CAB39's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 1.53× lower at baseline in the lines without SMAD3 | 0.024 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[TAGLN2]] | B | SMAD3 activity raises TAGLN2's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 2.98× lower at baseline in the lines without SMAD3 | 0.025 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[FGD6]] | B | SMAD3 activity raises FGD6's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 1.69× lower at baseline in the lines without SMAD3 | 0.026 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[IARS1]] | B | SMAD3 activity lowers IARS1's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 1.34× higher at baseline in the lines without SMAD3 | 0.036 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[AGRN]] | B | SMAD3 activity raises AGRN's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 1.80× lower at baseline in the lines without SMAD3 | 0.042 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.494). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.7, 1.8); signed map (4.3, 44.1). **Vector** length 120, 46.7% of its response variance represented; |z| ≥ 3 in 1,916 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | -2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.4 | +6.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | +4.4 | +4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.8 | +5.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.1 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | -0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +1.5 |
|  | [[Ferulic acid (drug)]] 0.5 µM |  | +2.2 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.4 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.8 | -4.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.6 | -5.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.3 | -5.8 |
|  | [[EX229 (drug)]] 5 µM |  | -6.2 | -4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.7 | -6.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -5.3 | -5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -9.0 |

## What is on record

|  |  |
|---|---|
| Name | SMAD family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.33 — chr15:67,063,763-67,195,173 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JV15-2, HsT17436; previously MADH3 |
| Gene groups (HGNC) | SMAD family |
| Hallmark sets | TGF_BETA_SIGNALING, UV_RESPONSE_DN, TNFA_SIGNALING_VIA_NFKB, G2M_CHECKPOINT |
| Reactome | 44 pathways, smallest: Loss of Function of SMAD4 in Cancer; SMAD2/3 MH2 Domain Mutants in Cancer; SMAD4 MH2 Domain Mutants in Cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [P84022](https://www.uniprot.org/uniprotkb/P84022) (SMAD family member 3):

> Receptor-regulated SMAD (R-SMAD) that is an intracellular signal transducer and transcriptional modulator activated by TGF-beta (transforming growth factor) and activin type 1 receptor kinases. Binds the TRE element in the promoter region of many genes that are regulated by TGF-beta and, on formation of the SMAD3/SMAD4 complex, activates transcription. Also can form a SMAD3/SMAD4/JUN/FOS complex at the AP-1/SMAD site to regulate TGF-beta-mediated transcription. Has an inhibitory effect on wound …

**Summary**, from NCBI Gene [4088](https://www.ncbi.nlm.nih.gov/gene/4088):

> The SMAD family of proteins are a group of intracellular signal transducer proteins similar to the gene products of the Drosophila gene 'mothers against decapentaplegic' (Mad) and the C. elegans gene Sma. The SMAD3 protein functions in the transforming growth factor-beta signaling pathway, and transmits signals from the cell surface to the nucleus, regulating gene activity and cell proliferation. This protein forms a complex with other SMAD proteins and binds DNA, functioning both as a …

**Accessions** — [HGNC:6769](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6769) · Entrez [4088](https://www.ncbi.nlm.nih.gov/gene/4088) · UniProt [P84022](https://www.uniprot.org/uniprotkb/P84022) · Ensembl [ENSG00000166949](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166949)

## Data

Gene col 9394: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9394); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9394, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9394]; `tensor/DDL_lfc|DDL_z.npy` [9394]; `embed/gene_vectors.npy` [9394]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9394 or target_col == 9394). Every well: [[SMAD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMAD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
