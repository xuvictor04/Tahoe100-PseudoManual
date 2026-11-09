---
symbol: "LDHB"
type: "gene"
col: 3268
ensembl_id: "ENSG00000111716"
name: "lactate dehydrogenase B"
location: "12p12.1"
module: 170
arm: "-"
pooled_cpm: 156.33
n_lines_expressing: 43
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# LDHB

*lactate dehydrogenase B* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.93× (z +15.0, q 0e+00, up in 42 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.44× (z +3.5, q 0.041, up in 28 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.614× (z -6.5, q 6e-08, down in 30 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (RKO 0.322×, NCI-H23 0.318×, SW480 0.344×, A-427 0.422×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM97]] (+0.67, fdr 1e-05), [[CRTAP]] (+0.66, fdr 9e-06), [[HSPD1]] (+0.66, fdr 7e-06); moves opposite to [[CHMP4A]] (-0.66, fdr 1e-05), [[NDUFAF1]] (-0.64, fdr 1e-05), [[CYP20A1]] (-0.62, fdr 3e-05).
> It sits in the **-** arm of [[Module 170]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HOMER3]] → it (grade C ⚠); 2 go from it, the strongest it → [[RPL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3268.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **4.93×** | +15.0 | 0e+00 | 42/42 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **4.23×** | +13.1 | 1e-36 | 38/38 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.95×** | +9.4 | 8e-19 | 39/39 (J82, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **1.71×** | +4.9 | 1e-04 | 36/40 (C32, NCI-H1792, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~74% of this change | **1.53×** | +4.0 | 0.007 | 33/41 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.45×** | +3.5 | 0.041 | 28/41 (NCI-H460, H4, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.041 | 28/41 (C32, A-172, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.4 | 0.041 | 26/40 (CFPAC-1, J82, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.061 | 28/41 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.080 | 28/41 (HOP62, SW 900, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.26×** | +3.1 | 0.097 | 27/41 (NCI-H1792, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3268.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (RKO 0.322×, NCI-H23 0.318×, SW480 0.344×, A-427 0.422×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.614×** | -6.5 | 6e-08 | 30/41 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.466×** | -3.7 | 0.052 | 36/42 (NCI-H23, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.539× | -3.0 | 0.38 | 27/43 (NCI-H23, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3268. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 148 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.42× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -9.9) |
| [[A-172 (line)]] | wt | 83.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A498 (line)]] | wt | 200 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[C32 (line)]] | wt | 91.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.08× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[CFPAC-1 (line)]] | alt | 105 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HOP62 (line)]] | alt | 140 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.36× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 214 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 105 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.0× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H23 (line)]] | alt | 310 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 170 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.28× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 154 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -8.7) |
| [[SW480 (line)]] | alt | 221 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -12.4) |
| [[A-427 (line)]] | wt | 403 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -10.7) |
| [[A549 (line)]] | wt | 228 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.38× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 183 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.06× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[C-33 A (line)]] | alt | 250 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -10.6) |
| [[HCT15 (line)]] | alt | 206 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[Hs 766T (line)]] | wt | 95.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.05× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HS-578T (line)]] | alt | 83.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.28× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 101 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.90× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 192 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.95× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LOX-IMVI (line)]] | wt | 234 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1573 (line)]] | alt | 107 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.50× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 256 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2347 (line)]] | alt | 221 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +12.1) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[PANC-1 (line)]] | alt | 150 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SHP-77 (line)]] | alt | 54.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 145 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.13× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW 900 (line)]] | alt | 180 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.43× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW48 (line)]] | wt | 229 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[CHP-212 (line)]] | wt | 204 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[H4 (line)]] | wt | 117 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.71× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 215 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 171 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[RKO (line)]] | wt | 313 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -14.7) |
| [[RPMI-7951 (line)]] | alt | 84.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.32× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SNU-1 (line)]] | wt | 235 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.7) |
| [[SW1417 (line)]] | alt | 110 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AsPC-1 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 20.7 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 13.2 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 177 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3268), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM97]] | +0.67 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[CRTAP]] | +0.66 | +0.75 / +0.57 | both halves | 9e-06 |  |
| [[HSPD1]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[PARP1]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[GGCT]] | +0.62 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[STT3B]] | +0.62 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[PRDX3]] | +0.62 | +0.68 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[NME2]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[HNRNPA1]] | +0.61 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[METAP1]] | +0.61 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[PRKDC]] | +0.61 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[CDCA7L]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP4A]] | -0.66 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[NDUFAF1]] | -0.64 | -0.55 / -0.52 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[CYP20A1]] | -0.62 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[MED18]] | -0.62 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[HARBI1]] | -0.62 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[NECAP2]] | -0.62 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[TJAP1]] | -0.60 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[MIR22HG]] | -0.59 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[FLT3LG]] | -0.58 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[YJU2B]] | -0.57 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[TSG101]] | -0.57 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[GORASP1]] | -0.57 | -0.48 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOMER3]] | C | HOMER3 activity raises LDHB's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 2.49× lower at baseline in the lines without HOMER3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPL3]] | B | LDHB activity raises RPL3's level | lines that do not express LDHB (7) vs lines expressing it (43) | 1.33× lower at baseline in the lines without LDHB | 0.089 | ⚠ within organs, on part of the lines; also absent: E2F7, ANKRD44, TMOD2; its own permutation p |
| [[RPL4]] | B | LDHB activity raises RPL4's level | lines that do not express LDHB (7) vs lines expressing it (43) | 1.30× lower at baseline in the lines without LDHB | 0.089 | ⚠ within organs, on part of the lines; also absent: E2F7, ANKRD44, TMOD2; its own permutation p |

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **-** arm (projection on the module's main direction -0.719). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-22.5, -11.5); signed map (-29.0, -33.6). **Vector** length 66.9, 24.7% of its response variance represented; |z| ≥ 3 in 669 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.9 | +2.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +0.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +2.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +1.6 | -1.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +1.5 | -1.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.5 | -1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.3 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.6 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -3.5 | +15.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -0.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.0 | +1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.0 | +2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.9 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | lactate dehydrogenase B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.1 — chr12:21,635,342-21,757,857 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | L-lactate dehydrogenase family |
| Hallmark sets | P53_PATHWAY, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 2 pathways, smallest: Pyruvate metabolism; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P07195](https://www.uniprot.org/uniprotkb/P07195) (L-lactate dehydrogenase B chain):

> Interconverts simultaneously and stereospecifically pyruvate and lactate with concomitant interconversion of NADH and NAD(+).

**Summary**, from NCBI Gene [3945](https://www.ncbi.nlm.nih.gov/gene/3945):

> This gene encodes the B subunit of lactate dehydrogenase enzyme, which catalyzes the interconversion of pyruvate and lactate with concomitant interconversion of NADH and NAD+ in a post-glycolysis process. Alternatively spliced transcript variants have been found for this gene. Recent studies have shown that a C-terminally extended isoform is produced by use of an alternative in-frame translation termination codon via a stop codon readthrough mechanism, and that this isoform is localized in the …

**Accessions** — [HGNC:6541](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6541) · Entrez [3945](https://www.ncbi.nlm.nih.gov/gene/3945) · UniProt [P07195](https://www.uniprot.org/uniprotkb/P07195) · Ensembl [ENSG00000111716](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111716)

## Data

Gene col 3268: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3268); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3268, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3268]; `tensor/DDL_lfc|DDL_z.npy` [3268]; `embed/gene_vectors.npy` [3268]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3268 or target_col == 3268). Every well: [[LDHB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LDHB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
