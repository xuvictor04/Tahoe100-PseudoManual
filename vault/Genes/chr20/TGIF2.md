---
symbol: "TGIF2"
type: "gene"
col: 4015
ensembl_id: "ENSG00000118707"
name: "TGFB induced factor homeobox 2"
location: "20q11.23"
module: 123
arm: "+"
pooled_cpm: 24.48
n_lines_expressing: 46
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# TGIF2

*TGFB induced factor homeobox 2* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.45× (z +36.0, q 0e+00, up in 41 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.491× (z -12.2, q 3e-31, down in 37 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFHX2]] (+0.69, fdr 1e-05), [[POGZ]] (+0.67, fdr 7e-06), [[RELB]] (+0.66, fdr 7e-06); moves opposite to [[ATP2C1]] (-0.61, fdr 1e-05), [[TPD52L2]] (-0.61, fdr 1e-05), [[STRAP]] (-0.60, fdr 1e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01776]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4015.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.45×** | +36.0 | 0e+00 | 41/44 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.72×** | +21.5 | 0e+00 | 40/44 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +7.0 | 6e-10 | 26/44 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +5.8 | 8e-07 | 25/43 (J82, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +5.3 | 2e-05 | 24/44 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.5 | 6e-04 | 19/44 (HT-29, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.012 | 12/43 (HepG2/C3A, NCI-H1792, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.8 | 0.012 | 1/44 (HOP62) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.24×** | +3.6 | 0.020 | 17/43 (NCI-H460, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +3.5 | 0.031 | 18/43 (CFPAC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.4 | 0.041 | 11/44 (PANC-1, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.21×** | +3.3 | 0.047 | 15/44 (J82, A-172, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.089 | 4/44 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4015.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.491×** | -12.2 | 3e-31 | 37/43 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.498×** | -11.3 | 6e-27 | 34/44 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.553×** | -9.5 | 6e-19 | 37/43 (LoVo, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.598×** | -8.5 | 3e-15 | 15/29 (Panc 03.27, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.642×** | -7.6 | 4e-12 | 25/41 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.739×** | -5.2 | 2e-05 | 16/43 (LS 180, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.725×** | -5.1 | 3e-05 | 18/37 (LOX-IMVI, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.577×** | -4.9 | 6e-05 | 18/37 (A-427, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.774×** | -4.4 | 7e-04 | 16/43 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.791×** | -4.0 | 0.003 | 19/43 (A-427, CFPAC-1, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.788×** | -3.9 | 0.005 | 16/43 (H4, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.682×** | -3.4 | 0.028 | 12/43 (MIA PaCa-2, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.683×** | -3.4 | 0.029 | 17/44 (NCI-H23, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.830×** | -3.2 | 0.057 | 9/44 (SW1417, A-172, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.704×** | -3.1 | 0.063 | 6/26 (NCI-H2347, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.884× | -3.0 | 0.097 | 10/44 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4015. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 32.4 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +13.0) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0613× (z -22.1) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.308× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 35.6 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +21.5) | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.300× (z -11.1) |
| [[A-172 (line)]] | wt | 35.1 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +23.1) | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -8.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 18.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.38× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.123× (z -12.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 30.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.13× (z +24.5) | [[Selinexor (drug)]] 5 µM 0.498× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 14.7 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +15.1) | [[Ixazomib citrate (drug)]] 5 µM 0.215× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 29.0 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.354× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 10.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +22.4) | — |
| [[SK-MEL-2 (line)]] | alt | 29.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -10.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 43.2 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.314× (z -12.2) |
| [[A549 (line)]] | wt | 9.88 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +17.9) | — |
| [[Hs 766T (line)]] | wt | 38.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.04× (z +20.5) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -9.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 43.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.163× (z -13.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 30.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +25.1) | — |
| [[RPMI-7951 (line)]] | alt | 35.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +15.6) | — |
| [[HepG2_C3A (line)]] | wt | 55.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +16.9) | — |
| [[HOP62 (line)]] | alt | 14.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +22.5) | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +10.4) | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.102× (z -9.2) |
| [[KATO III (line)]] | alt | 32.5 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 6.07× (z +14.9) | — |
| [[NCI-H1792 (line)]] | alt | 43.6 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 5.67× (z +12.4) | — |
| [[NCI-H2347 (line)]] | alt | 10.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.11× (z +16.4) | — |
| [[SNU-1 (line)]] | wt | 42.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +14.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 33.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +16.2) | — |
| [[AsPC-1 (line)]] | alt | 9.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 36.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +16.2) | — |
| [[COLO 205 (line)]] | alt | 13.9 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0794× (z -11.1) |
| [[H4 (line)]] | wt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +9.8) | — |
| [[LS 180 (line)]] | wt | 9.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +14.5) | — |
| [[RKO (line)]] | wt | 42.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.3) | — |
| [[SHP-77 (line)]] | alt | 8.58 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0969× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[SW 900 (line)]] | alt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.02× (z +13.1) | — |
| [[SW1417 (line)]] | alt | 27.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.9) | — |
| [[SW48 (line)]] | wt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.98× (z +12.9) | — |
| [[A498 (line)]] | wt | 5.88 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.90 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.56 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.17 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 70.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4015), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFHX2]] | +0.69 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[POGZ]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[RELB]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[AMOTL2]] | +0.65 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[EID2]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[FJX1]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[AJUBA]] | +0.62 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[TGIF2-RAB5IF]] | +0.61 | +0.66 / +0.49 | both halves | 1e-05 | ⚠ **readthrough risk**: TGIF2-RAB5IF lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[ZCCHC3]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[KLF10]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[IKBKE]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ADNP]] | +0.59 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[ZBTB2]] | +0.59 | +0.66 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP2C1]] | -0.61 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[TPD52L2]] | -0.61 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[STRAP]] | -0.60 | -0.59 / -0.54 | both halves | 1e-05 | pathway: Adherens junctions interactions |
| [[TIMM10B]] | -0.59 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[UFD1]] | -0.59 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[NTAN1]] | -0.58 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[YKT6]] | -0.58 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[YIPF1]] | -0.58 | -0.67 / -0.43 | both halves | 4e-05 |  |
| [[SAR1A]] | -0.57 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[AHSA1]] | -0.57 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ZCCHC17]] | -0.57 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[GDAP2]] | -0.57 | -0.61 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01776]] | B | LINC01776 activity raises TGIF2's level | lines that do not express LINC01776 (29) vs lines expressing it (21) | 1.46× lower at baseline in the lines without LINC01776 | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC01010, PHACTR1, NOG |
| [[MYO5A]] | B | MYO5A activity raises TGIF2's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 1.21× lower at baseline in the lines without MYO5A | 0.065 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.518). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.4, 6.9); signed map (42.3, 2.5). **Vector** length 116, 29.1% of its response variance represented; |z| ≥ 3 in 929 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Signaling by Hippo* (reactome, mean cos +0.58 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +10.6 | +21.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +10.5 | +36.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +7.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +5.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +3.9 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +2.8 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[Estrone sulfate (potassium) (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +3.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -7.4 | -12.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -7.1 | -11.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.8 | -9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.4 | -7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | -8.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.7 | -3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -4.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -3.1 | -5.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | TGFB induced factor homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:36,573,488-36,593,950 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | TALE class homeoboxes and pseudogenes |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 14 pathways, smallest: Downregulation of SMAD2/3:SMAD4 transcriptional activity; SMAD2/SMAD3:SMAD4 heterotrimer regulates transcription; Negative Regulation of CDH1 Gene Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZN2](https://www.uniprot.org/uniprotkb/Q9GZN2) (Homeobox protein TGIF2):

> Transcriptional repressor, which probably repress transcription by binding directly the 5'-CTGTCAA-3' DNA sequence or by interacting with TGF-beta activated SMAD proteins. Probably represses transcription via the recruitment of histone deacetylase proteins.

**Summary**, from NCBI Gene [60436](https://www.ncbi.nlm.nih.gov/gene/60436):

> The protein encoded by this gene is a DNA-binding homeobox protein and a transcriptional repressor, which appears to repress transcription by recruiting histone deacetylases to TGF beta-responsive genes. This gene is amplified and over-expressed in some ovarian cancers. Alternative splicing results in multiple transcript variants. A related pseudogene has been identified on chromosome 1. Read-through transcription also exists between this gene and the neighboring downstream C20orf24 (chromosome …

**Accessions** — [HGNC:15764](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15764) · Entrez [60436](https://www.ncbi.nlm.nih.gov/gene/60436) · UniProt [Q9GZN2](https://www.uniprot.org/uniprotkb/Q9GZN2) · Ensembl [ENSG00000118707](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118707)

## Data

Gene col 4015: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4015); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4015, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4015]; `tensor/DDL_lfc|DDL_z.npy` [4015]; `embed/gene_vectors.npy` [4015]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4015 or target_col == 4015). Every well: [[TGIF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TGIF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
