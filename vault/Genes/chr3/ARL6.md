---
symbol: "ARL6"
type: "gene"
col: 3513
ensembl_id: "ENSG00000113966"
name: "ARF like GTPase 6"
location: "3q11.2"
module: 65
arm: "+"
pooled_cpm: 19.76
n_lines_expressing: 48
n_dd_up: 21
n_dd_down: 22
n_dd_up_clean: 20
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# ARL6

*ARF like GTPase 6* — 3q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.55× (z +22.5, q 0e+00, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.433× (z -12.4, q 9e-33, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HACE1]] (+0.82, fdr 7e-06), [[FAM234B]] (+0.82, fdr 7e-06), [[ATG4C]] (+0.81, fdr 7e-06); moves opposite to [[ZHX2]] (-0.70, fdr 1e-05), [[PPP3CB-AS1]] (-0.70, fdr 1e-05), [[LINC00571]] (-0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PLEKHA6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3513.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.55×** | +22.5 | 0e+00 | 46/46 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.46×** | +22.2 | 0e+00 | 44/45 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.71×** | +19.5 | 0e+00 | 46/46 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.70×** | +14.8 | 0e+00 | 43/46 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +11.4 | 8e-28 | 40/46 (LoVo, HT-29, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **3.45×** | +9.6 | 6e-20 | 41/46 (HEC-1-A, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.89×** | +9.5 | 2e-19 | 37/44 (HT-29, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +7.2 | 5e-11 | 30/45 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +5.3 | 7e-06 | 24/46 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.28×** | +5.1 | 2e-05 | 22/46 (HT-29, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.7 | 2e-04 | 15/42 (NCI-H2030, LS 180, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.80×** | +4.6 | 2e-04 | 16/45 (MIA PaCa-2, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.003 | 16/45 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.007 | 10/46 (A-172, Hs 766T, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.008 | 21/45 (NCI-H23, A-172, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.30×** | +3.7 | 0.009 | 10/44 (HS-578T, NCI-H460, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3513.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.433×** | -12.4 | 9e-33 | 37/46 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.575×** | -11.6 | 1e-28 | 33/45 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.463×** | -11.4 | 6e-28 | 31/40 (NCI-H2030, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.465×** | -11.0 | 9e-26 | 32/46 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.474×** | -10.7 | 1e-24 | 22/29 (NCI-H1792, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.636×** | -9.5 | 2e-19 | 33/46 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.540×** | -9.2 | 4e-18 | 30/45 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.540×** | -9.2 | 4e-18 | 28/45 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.547×** | -8.6 | 4e-16 | 26/43 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.600×** | -7.6 | 2e-12 | 29/45 (HCT15, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.611×** | -7.3 | 1e-11 | 28/45 (SW1417, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.707×** | -5.1 | 1e-05 | 24/46 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.736×** | -4.6 | 2e-04 | 17/45 (NCI-H460, C32, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -4.1 | 0.002 | 4/46 (SNU-423, SW 900, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.761×** | -4.1 | 0.002 | 14/45 (Panc 03.27, NCI-H460, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -4.0 | 0.002 | 16/45 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.765×** | -3.8 | 0.004 | 15/45 (HT-29, A-172, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.803×** | -3.3 | 0.034 | 15/46 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Idoxuridine (drug)]] 0.5 µM |  | **0.811×** | -3.1 | 0.049 | 8/45 (NCI-H1792, C32, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.801×** | -3.0 | 0.057 | 10/45 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3513. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.8 | 3 | 7 (1 ⚠) | [[Belinostat (drug)]] 5 µM 4.84× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -16.4) |
| [[C32 (line)]] | wt | 48.7 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -25.2) |
| [[NCI-H1792 (line)]] | alt | 26.2 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.49× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -17.4) |
| [[NCI-H2347 (line)]] | alt | 16.7 | 4 | 2 | [[Panobinostat (drug)]] 5 µM 6.52× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -11.9) |
| [[PANC-1 (line)]] | alt | 23.5 | 3 | 3 | [[Panobinostat (drug)]] 5 µM 4.51× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -11.9) |
| [[SW1417 (line)]] | alt | 9.51 | 4 | 2 | [[Belinostat (drug)]] 5 µM 10.1× (z +11.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.111× (z -11.0) |
| [[A-172 (line)]] | wt | 15.7 | 3 | 2 | [[Belinostat (drug)]] 5 µM 5.95× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -13.9) |
| [[HS-578T (line)]] | alt | 33.5 | 1 | 4 (1 ⚠) | [[Belinostat (drug)]] 5 µM 4.03× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -16.7) |
| [[J82 (line)]] | alt | 23.6 | 2 | 3 | [[Panobinostat (drug)]] 5 µM 4.28× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 16.9 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.96× (z +12.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 41.0 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -13.2) |
| [[SW480 (line)]] | alt | 13.1 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.46× (z +13.0) | [[Digitoxin (drug)]] 5 µM 0.319× (z -8.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 38.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.08× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -12.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 25.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.94× (z +12.1) | — |
| [[HT-29 (line)]] | alt | 12.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.08× (z +11.7) | — |
| [[LS 180 (line)]] | wt | 10.6 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 7.18× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.201× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 27.0 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.42× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -9.6) |
| [[A498 (line)]] | wt | 8.69 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.91× (z +12.4) | — |
| [[CFPAC-1 (line)]] | alt | 18.8 | 3 | 0 | [[Belinostat (drug)]] 5 µM 5.62× (z +11.4) | — |
| [[LoVo (line)]] | wt | 5.30 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.56× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 11.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.25× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 25.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.315× (z -10.2) |
| [[RKO (line)]] | wt | 12.2 | 3 | 0 | [[Belinostat (drug)]] 5 µM 9.93× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 29.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0755× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -9.5) |
| [[SNU-423 (line)]] | alt | 13.0 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 5.40× (z +8.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0812× (z -12.8) ⚠ toxic |
| [[C-33 A (line)]] | alt | 53.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 18.8 | 2 | 0 | [[Belinostat (drug)]] 5 µM 4.56× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 32.8 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.80× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 14.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.15× (z +9.2) | — |
| [[H4 (line)]] | wt | 26.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -8.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.163× (z -8.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 81.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -11.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 12.3 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0684× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3513), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACE1]] | +0.82 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[FAM234B]] | +0.82 | +0.82 / +0.71 | both halves | 7e-06 |  |
| [[ATG4C]] | +0.81 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[SNAPC3]] | +0.79 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[PDK3]] | +0.76 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[KCTD6]] | +0.76 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[CDON]] | +0.75 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[SDHAF3]] | +0.75 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[CABIN1]] | +0.72 | +0.75 / +0.49 | both halves | 1e-05 |  |
| [[WASF3]] | +0.72 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[FAM168A]] | +0.72 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[ATRN]] | +0.72 | +0.64 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZHX2]] | -0.70 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | -0.70 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[LINC00571]] | -0.69 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | -0.69 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[MMADHC-DT]] | -0.68 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[ATXN1L]] | -0.68 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[AVEN]] | -0.67 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[AKT1S1]] | -0.67 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[DGKH]] | -0.67 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[ITPA]] | -0.66 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[CFLAR]] | -0.66 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[ANKLE2]] | -0.66 | -0.60 / -0.57 | both halves | 9e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHA6]] | B | PLEKHA6 activity lowers ARL6's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 2.23× higher at baseline in the lines without PLEKHA6 | 0.022 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[TTLL7]] | B | TTLL7 activity raises ARL6's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 2.09× lower at baseline in the lines without TTLL7 | 0.031 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725 |
| [[ABL1]] | B | ABL1 activity lowers ARL6's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 4.2% of all compounds | 0.037 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DYNC2H1]] | B | DYNC2H1 activity raises ARL6's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 3.33× lower at baseline in the lines without DYNC2H1 | 0.057 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |
| [[MPP2]] | B | MPP2 activity raises ARL6's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 2.26× lower at baseline in the lines without MPP2 | 0.091 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[SMARCD3]] | C | SMARCD3 activity raises ARL6's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 2.81× lower at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[DDIT4]] | C | DDIT4 activity lowers ARL6's level | lines that do not express DDIT4 (3) vs lines expressing it (47) | 1.94× higher at baseline in the lines without DDIT4 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, TIMP1, UGDH; maybe low, not absent; its own permutation p |
| [[PLEKHA2]] | C | PLEKHA2 activity lowers ARL6's level | lines that do not express PLEKHA2 (4) vs lines expressing it (45) | 2.30× higher at baseline in the lines without PLEKHA2 | 0.098 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: LSMEM2, ENSG00000285868; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.768). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (7.9, -12.9); signed map (-32.4, -7.4). **Vector** length 124, 35.7% of its response variance represented; |z| ≥ 3 in 1,217 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.1 | +22.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.0 | +14.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.7 | +19.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.4 | +9.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.3 | +22.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +11.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.6 | +5.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +3.4 | +2.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +3.1 | +4.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.8 | -9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.8 | -11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.4 | -10.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.9 | -9.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.9 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.0 | -4.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.0 | -1.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.8 | -2.0 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -2.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q11.2 — chr3:97,764,521-97,801,229 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RP55; previously BBS3 |
| Gene groups (HGNC) | ARF GTPase family |
| Reactome | 5 pathways, smallest: BBSome-mediated cargo-targeting to cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0F7](https://www.uniprot.org/uniprotkb/Q9H0F7) (ADP-ribosylation factor-like protein 6):

> Involved in membrane protein trafficking at the base of the ciliary organelle. Mediates recruitment onto plasma membrane of the BBSome complex which would constitute a coat complex required for sorting of specific membrane proteins to the primary cilia. Together with BBS1, is necessary for correct trafficking of PKD1 to primary cilia (By similarity). Together with the BBSome complex and LTZL1, controls SMO ciliary trafficking and contributes to the sonic hedgehog (SHH) pathway regulation. May …

**Summary**, from NCBI Gene [84100](https://www.ncbi.nlm.nih.gov/gene/84100):

> The protein encoded by this gene belongs to the ARF-like (ADP ribosylation factor-like) sub-family of the ARF family of GTP-binding proteins which are involved in regulation of intracellular traffic. Mutations in this gene are associated with Bardet-Biedl syndrome (BBS). A vision-specific transcript, encoding long isoform BBS3L, has been described (PMID: 20333246). [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:13210](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13210) · Entrez [84100](https://www.ncbi.nlm.nih.gov/gene/84100) · UniProt [Q9H0F7](https://www.uniprot.org/uniprotkb/Q9H0F7) · Ensembl [ENSG00000113966](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113966)

## Data

Gene col 3513: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3513); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3513, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3513]; `tensor/DDL_lfc|DDL_z.npy` [3513]; `embed/gene_vectors.npy` [3513]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3513 or target_col == 3513). Every well: [[ARL6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
