---
symbol: "GCLC"
type: "gene"
col: 6
ensembl_id: "ENSG00000001084"
name: "glutamate-cysteine ligase catalytic subunit"
location: "6p12.1"
module: 117
arm: "+"
pooled_cpm: 141.64
n_lines_expressing: 46
n_dd_up: 38
n_dd_down: 2
n_dd_up_clean: 32
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 14
direction_downstream: 3
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# GCLC

*glutamate-cysteine ligase catalytic subunit* — 6p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.33× (z +15.6, q 0e+00, up in 33 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.744× (z -5.3, q 7e-05, down in 23 of 38 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A-427 0.180×, C-33 A 0.135×, NCI-H1573 0.164×, LS 180 0.234×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (KATO III 0.163×, COLO 205 0.228×, LoVo 0.287×, HT-29 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H1573 0.282×, SHP-77 0.420×, SW480 0.577×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1573 0.204×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01564]] (+0.63, fdr 7e-06, ⚠ same locus), [[AKR1C1]] (+0.62, fdr 1e-05), [[NMRAL2P]] (+0.61, fdr 1e-05), [[ZFAND5]] (+0.61, fdr 1e-05); moves opposite to [[TCP11L1]] (-0.42, fdr 6e-05), [[CEP170P1]] (-0.40, fdr 1e-04), [[PHF10]] (-0.40, fdr 8e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[CYP4F3]] → it (grade B ⚠); 3 go from it, the strongest it → [[GAREM1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.33×** | +15.6 | 0e+00 | 33/44 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +15.6 | 0e+00 | 28/44 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.98×** | +12.6 | 2e-34 | 33/44 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +12.1 | 2e-31 | 30/44 (LS 180, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.79×** | +10.8 | 6e-25 | 33/44 (SNU-423, COLO 205, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.75×** | +10.3 | 4e-23 | 40/44 (COLO 205, Panc 03.27, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +10.2 | 1e-22 | 30/44 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +10.0 | 1e-21 | 30/44 (Panc 03.27, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +9.8 | 1e-20 | 32/43 (NCI-H23, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.63×** | +8.5 | 1e-15 | 31/44 (Panc 03.27, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +8.1 | 4e-14 | 22/45 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +7.6 | 1e-12 | 22/44 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +7.3 | 2e-11 | 26/44 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +7.0 | 1e-10 | 25/44 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +6.8 | 5e-10 | 23/44 (NCI-H460, BT-474, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +5.7 | 5e-07 | 24/44 (A-427, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A-427 0.180×, C-33 A 0.135×, NCI-H1573 0.164×, LS 180 0.234×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (KATO III 0.163×, COLO 205 0.228×, LoVo 0.287×, HT-29 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H1573 0.282×, SHP-77 0.420×, SW480 0.577×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1573 0.204×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.744×** | -5.3 | 7e-05 | 23/38 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.859× | -4.0 | 0.019 | 21/44 (KATO III, SW48, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.817×** | -3.8 | 0.032 | 23/44 (KATO III, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 99.2 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +12.4) | — |
| [[A-427 (line)]] | wt | 46.4 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.94× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.180× (z -16.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 69.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +13.7) | — |
| [[LS 180 (line)]] | wt | 193 | 2 | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 3.76× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -13.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 61.3 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.36× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 740 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.119× (z -16.2) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.282× (z -14.2) |
| [[BT-474 (line)]] | alt | 45.0 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.96× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +10.0) | — |
| [[C32 (line)]] | wt | 50.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 216 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.319× (z -10.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 956 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.42× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 80.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.5) | — |
| [[KATO III (line)]] | alt | 338 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 100 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.49× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 54.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.20× (z +12.6) | — |
| [[HT-29 (line)]] | alt | 420 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 57.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.4) | — |
| [[LoVo (line)]] | wt | 185 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.44× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 64.4 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.31× (z +12.9) | — |
| [[PANC-1 (line)]] | alt | 86.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.94× (z +12.3) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 220 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 379 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 41.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 84.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 170 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.33× (z +11.2) | — |
| [[RKO (line)]] | wt | 61.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +11.2) | — |
| [[SK-MEL-2 (line)]] | alt | 40.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +12.9) | — |
| [[AN3 CA (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.187× (z -11.3) ⚠ transcription drop |
| [[C-33 A (line)]] | alt | 72.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -16.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 132 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.69× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 45.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 121 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -11.9) |
| [[SW 900 (line)]] | alt | 62.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.38× (z +8.8) | — |
| [[SW480 (line)]] | alt | 240 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.577× (z -9.0) |
| [[A-172 (line)]] | wt | 28.9 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 91.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 270 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.6 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01564]] | +0.63 | +0.67 / +0.61 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[AKR1C1]] | +0.62 | +0.63 / +0.57 | both halves | 1e-05 | STRING 743 |
| [[NMRAL2P]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ZFAND5]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[NEBL]] | +0.56 | +0.45 / +0.66 | both halves | 3e-05 | **novel candidate** |
| [[NMRAL2P-1]] | +0.56 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SLC7A11]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM; STRING 674 |
| [[PIR]] | +0.53 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[GAREM1]] | +0.53 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[JDP2]] | +0.51 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[SGPP2]] | +0.50 | +0.43 / +0.45 | both halves | 4e-05 |  |
| [[HKDC1]] | +0.50 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[MAP2]] | +0.49 | +0.51 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCP11L1]] | -0.42 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[CEP170P1]] | -0.40 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[PHF10]] | -0.40 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[KIRREL1]] | -0.39 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[TYK2]] | -0.39 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[CEP135]] | -0.38 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[TGFBR1]] | -0.38 | -0.36 / -0.38 | both halves | 9e-05 |  |
| [[VEGFC]] | -0.37 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[PLAU]] | -0.37 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[TLE5]] | -0.37 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[FAM110A]] | -0.37 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[RHOJ]] | -0.37 | -0.34 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP4F3]] | B | CYP4F3 activity raises GCLC's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 2.76× lower at baseline in the lines without CYP4F3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[AKR1C2]] | B | AKR1C2 activity raises GCLC's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 2.23× lower at baseline in the lines without AKR1C2 | 0.003 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2 |
| [[LINC01564]] | B | LINC01564 activity raises GCLC's level | lines that do not express LINC01564 (24) vs lines expressing it (26) | 2.85× lower at baseline in the lines without LINC01564 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC03040, INAVA, CYP4F11; maybe low, not absent |
| [[CDHR2]] | B | CDHR2 activity raises GCLC's level | lines that do not express CDHR2 (30) vs lines expressing it (20) | 2.89× lower at baseline in the lines without CDHR2 | 0.007 | ⚠ within organs, on part of the lines; also absent: VIL1, NPSR1-AS1, EPS8L3; maybe low, not absent |
| [[CYP4F11]] | B | CYP4F11 activity raises GCLC's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 2.21× lower at baseline in the lines without CYP4F11 | 0.019 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4 |
| [[SGPP2]] | B | SGPP2 activity raises GCLC's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 2.60× lower at baseline in the lines without SGPP2 | 0.021 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[GCNT3]] | B | GCNT3 activity raises GCLC's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.12× lower at baseline in the lines without GCNT3 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[NMRAL2P]] | B | NMRAL2P activity raises GCLC's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 1.74× lower at baseline in the lines without NMRAL2P | 0.038 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[AKR1C1]] | B | AKR1C1 activity raises GCLC's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 1.50× lower at baseline in the lines without AKR1C1 | 0.057 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU |
| [[AKR1C3]] | B | AKR1C3 activity raises GCLC's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 1.83× lower at baseline in the lines without AKR1C3 | 0.077 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[COBL]] | B | COBL activity raises GCLC's level | lines that do not express COBL (23) vs lines expressing it (27) | 2.50× lower at baseline in the lines without COBL | 0.086 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7 |
| [[KIRREL1]] | B | KIRREL1 activity lowers GCLC's level | lines that do not express KIRREL1 (8) vs lines expressing it (42) | 2.68× higher at baseline in the lines without KIRREL1 | 0.095 | ⚠ within organs, on part of the lines; also absent: BEX3, ARHGAP31, ROBO3 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAREM1]] | C | GCLC activity raises GAREM1's level | lines that do not express GCLC (4) vs lines expressing it (46) | 5.24× lower at baseline in the lines without GCLC | 0.021 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LRRC8B; maybe low, not absent |
| [[FAM135A]] | C | GCLC activity raises FAM135A's level | lines that do not express GCLC (4) vs lines expressing it (46) | 2.53× lower at baseline in the lines without GCLC | 0.028 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LRRC8B; maybe low, not absent |
| [[HECTD1]] | C | GCLC activity raises HECTD1's level | lines that do not express GCLC (4) vs lines expressing it (46) | 1.60× lower at baseline in the lines without GCLC | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LRRC8B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.562). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-9.0, 47.4); signed map (52.6, -10.2). **Vector** length 112, 29.9% of its response variance represented; |z| ≥ 3 in 1,355 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Synthesis of bile acids and bile salts via 27-hydroxycholesterol* (reactome, mean cos +0.51 to 3); *Synthesis of bile acids and bile salts via 24-hydroxycholesterol* (reactome, mean cos +0.51 to 3); *Synthesis of bile acids and bile salts via 7alpha-hydroxycholesterol* (reactome, mean cos +0.51 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.5 | +12.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.9 | +8.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.9 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | +10.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.0 | +4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +1.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -6.2 | -4.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -4.6 | -3.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +0.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -2.8 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -1.6 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.8 | -0.8 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -1.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.7 | -2.2 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | glutamate-cysteine ligase catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.1 — chr6:53,497,341-53,616,970 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GCS; previously GLCLC, GLCL |
| Gene groups (HGNC) | Ligases; Glutamate-cysteine ligase subunits |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, XENOBIOTIC_METABOLISM, HEME_METABOLISM, GLYCOLYSIS, MTORC1_SIGNALING |
| Reactome | 12 pathways, smallest: Glutathione synthesis and recycling; NFE2L2 regulating anti-oxidant/detoxification enzymes; Metabolic disorders of biological oxidation enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [P48506](https://www.uniprot.org/uniprotkb/P48506) (Glutamate--cysteine ligase catalytic subunit):

> Catalyzes the ATP-dependent ligation of L-glutamate and L-cysteine and participates in the first and rate-limiting step in glutathione biosynthesis.

**Summary**, from NCBI Gene [2729](https://www.ncbi.nlm.nih.gov/gene/2729):

> Glutamate-cysteine ligase, also known as gamma-glutamylcysteine synthetase is the first rate-limiting enzyme of glutathione synthesis. The enzyme consists of two subunits, a heavy catalytic subunit and a light regulatory subunit. This locus encodes the catalytic subunit, while the regulatory subunit is derived from a different gene located on chromosome 1p22-p21. Mutations at this locus have been associated with hemolytic anemia due to deficiency of gamma-glutamylcysteine synthetase and …

**Accessions** — [HGNC:4311](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4311) · Entrez [2729](https://www.ncbi.nlm.nih.gov/gene/2729) · UniProt [P48506](https://www.uniprot.org/uniprotkb/P48506) · Ensembl [ENSG00000001084](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000001084)

## Data

Gene col 6: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6]; `tensor/DDL_lfc|DDL_z.npy` [6]; `embed/gene_vectors.npy` [6]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6 or target_col == 6). Every well: [[GCLC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCLC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
