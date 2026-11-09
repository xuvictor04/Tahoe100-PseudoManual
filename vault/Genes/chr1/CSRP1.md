---
symbol: "CSRP1"
type: "gene"
col: 8225
ensembl_id: "ENSG00000159176"
name: "cysteine and glycine rich protein 1"
location: "1q32.1"
module: 78
arm: "+"
pooled_cpm: 37.64
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 15
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# CSRP1

*cysteine and glycine rich protein 1* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.80× (z +11.8, q 3e-29, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.475× (z -14.9, q 0e+00, down in 38 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYH9]] (+0.70, fdr 7e-06), [[COTL1]] (+0.68, fdr 1e-05), [[WDR1]] (+0.67, fdr 7e-06); moves opposite to [[NUDT2]] (-0.69, fdr 1e-05), [[HIGD2A]] (-0.69, fdr 7e-06), [[COA6]] (-0.66, fdr 1e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8225.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +11.8 | 3e-29 | 32/46 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +9.7 | 1e-19 | 35/41 (C32, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +8.1 | 8e-14 | 27/34 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +6.2 | 6e-08 | 26/38 (SNU-423, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +6.2 | 6e-08 | 27/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +6.1 | 1e-07 | 28/46 (RPMI-7951, SNU-423, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +5.9 | 4e-07 | 23/46 (A-172, A549, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +4.9 | 5e-05 | 21/46 (HCT15, A-172, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +4.9 | 6e-05 | 27/46 (HCT15, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +4.8 | 1e-04 | 24/46 (hTERT-HPNE, A-172, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.38×** | +4.6 | 2e-04 | 24/46 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +4.2 | 0.001 | 18/46 (A-172, SNU-423, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.002 | 22/46 (HCT15, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +4.0 | 0.003 | 22/46 (LS 180, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.27×** | +3.3 | 0.031 | 17/45 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.040 | 15/47 (SW480, HCT15, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8225.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.475×** | -14.9 | 0e+00 | 38/45 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.468×** | -10.8 | 1e-24 | 38/46 (H4, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.503×** | -9.7 | 4e-20 | 37/45 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.574×** | -7.9 | 6e-13 | 34/45 (H4, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.612×** | -7.0 | 4e-10 | 34/46 (LOX-IMVI, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.647×** | -5.8 | 5e-07 | 30/45 (LOX-IMVI, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.673×** | -5.6 | 2e-06 | 29/46 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -5.3 | 8e-06 | 27/45 (H4, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.815×** | -4.1 | 0.002 | 20/46 (NCI-H460, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.749×** | -4.1 | 0.002 | 20/46 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.586×** | -4.0 | 0.004 | 20/41 (LOX-IMVI, A549, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.748×** | -4.0 | 0.004 | 21/43 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.716×** | -3.4 | 0.032 | 15/46 (LOX-IMVI, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.792×** | -3.2 | 0.062 | 15/45 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Resveratrol (drug)]] 5 µM |  | 0.858× | -3.1 | 0.084 | 12/47 (LOX-IMVI, SW48, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.810×** | -3.0 | 0.098 | 17/44 (COLO 205, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8225. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 80.4 | 0 | 8 (3 ⚠) | — | [[TAK-901 (drug)]] 0.05 µM 0.200× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 132 | 4 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.34× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -18.4) |
| [[PANC-1 (line)]] | alt | 30.8 | 6 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.48× (z +10.4) | [[Ixazomib citrate (drug)]] 5 µM 0.356× (z -8.8) |
| [[HOP62 (line)]] | alt | 46.8 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +17.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -10.8) |
| [[SW480 (line)]] | alt | 18.6 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 3.29× (z +10.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -10.2) |
| [[H4 (line)]] | wt | 63.6 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0923× (z -14.9) |
| [[A-172 (line)]] | wt | 58.3 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 6.72× (z +14.8) | — |
| [[A549 (line)]] | wt | 106 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +12.4) | — |
| [[C32 (line)]] | wt | 64.2 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +10.3) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -10.4) |
| [[SNU-423 (line)]] | alt | 35.2 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +13.7) | — |
| [[hTERT-HPNE (line)]] | wt | 61.4 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +14.0) | [[Ixazomib citrate (drug)]] 5 µM 0.260× (z -9.5) |
| [[J82 (line)]] | alt | 35.1 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.153× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.288× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 16.0 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 48.5 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 6.43× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 39.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 24.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +9.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 22.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -12.1) |
| [[Hs 766T (line)]] | wt | 27.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 55.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +14.9) | — |
| [[RKO (line)]] | wt | 27.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 32.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -8.8) |
| [[A-427 (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.250× (z -8.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 27.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +14.2) | — |
| [[COLO 205 (line)]] | alt | 18.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 37.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -9.9) |
| [[HS-578T (line)]] | alt | 29.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 19.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -8.8) |
| [[KATO III (line)]] | alt | 23.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 16.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -10.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 27.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -15.2) |
| [[A498 (line)]] | wt | 3.48 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8225), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYH9]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[COTL1]] | +0.68 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[WDR1]] | +0.67 | +0.65 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_COAGULATION |
| [[ARHGDIA]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[CORO1C]] | +0.65 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[TPM4]] | +0.65 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[BCAN-AS2]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[ACTN1]] | +0.61 | +0.48 / +0.59 | both halves | 2e-05 | STRING 574 |
| [[ZYX]] | +0.60 | +0.67 / +0.51 | both halves | 1e-05 | STRING 694 |
| [[PLEC]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[ANXA5]] | +0.59 | +0.49 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |
| [[CLIC1]] | +0.59 | +0.55 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT2]] | -0.69 | -0.57 / -0.70 | both halves | 1e-05 |  |
| [[HIGD2A]] | -0.69 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[COA6]] | -0.66 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[SOS1]] | -0.64 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[MZT2A]] | -0.62 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[ASB7]] | -0.60 | -0.50 / -0.68 | both halves | 1e-05 |  |
| [[GPBP1L1]] | -0.59 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[ZNF148]] | -0.59 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ELMOD3]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[TMEM11-DT]] | -0.58 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[MIR4458HG]] | -0.58 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[SNX13]] | -0.58 | -0.62 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CSRP1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.8, 25.4); signed map (-7.3, 35.0). **Vector** length 125, 34.0% of its response variance represented; |z| ≥ 3 in 1,227 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.9 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +6.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.5 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +6.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.6 | +2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.5 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +2.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.1 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.5 | -14.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -5.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.4 | -9.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.2 | -7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.5 | -5.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.7 | -4.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.7 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -5.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.0 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | cysteine and glycine rich protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:201,483,530-201,509,456 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CSRP, D1S181E; previously CYRP |
| Gene groups (HGNC) | LIM domain containing |
| Hallmark sets | COAGULATION, COMPLEMENT |
| Reactome | 2 pathways, smallest: Response to metal ions; Cellular responses to stimuli |
| Matched by | ensembl_id |

**Function**, from UniProt [P21291](https://www.uniprot.org/uniprotkb/P21291) (Cysteine and glycine-rich protein 1):

> Could play a role in neuronal development.

**Summary**, from NCBI Gene [1465](https://www.ncbi.nlm.nih.gov/gene/1465):

> This gene encodes a member of the cysteine-rich protein (CSRP) family. This gene family includes a group of LIM domain proteins, which may be involved in regulatory processes important for development and cellular differentiation. The LIM/double zinc-finger motif found in this gene product occurs in proteins with critical functions in gene regulation, cell growth, and somatic differentiation. Alternatively spliced transcript variants have been described. [provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:2469](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2469) · Entrez [1465](https://www.ncbi.nlm.nih.gov/gene/1465) · UniProt [P21291](https://www.uniprot.org/uniprotkb/P21291) · Ensembl [ENSG00000159176](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159176)

## Data

Gene col 8225: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8225); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8225, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8225]; `tensor/DDL_lfc|DDL_z.npy` [8225]; `embed/gene_vectors.npy` [8225]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8225 or target_col == 8225). Every well: [[CSRP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSRP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
