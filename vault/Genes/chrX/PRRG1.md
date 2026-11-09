---
symbol: "PRRG1"
type: "gene"
col: 5151
ensembl_id: "ENSG00000130962"
name: "proline rich and Gla domain 1"
location: "Xp21.1"
module: 23
arm: "-"
pooled_cpm: 64.57
n_lines_expressing: 47
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 13
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# PRRG1

*proline rich and Gla domain 1* — Xp21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.53× (z +11.5, q 8e-28, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.557× (z -11.0, q 3e-25, down in 26 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.404× (z -9.2, q 4e-18, down in 35 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (SW1417 0.348×, BT-474 0.255×, Panc 03.27 0.403×, HT-29 0.367×, …); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (RKO 0.164×, A-427 0.156×, C32 0.176×, MIA PaCa-2 0.247×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 4 lines (RKO 0.130×, MIA PaCa-2 0.140×, SK-MEL-2 0.149×, HEC-1-A 0.211×); [[PH-797804 (drug)]] 5 µM in 1 line (HEC-1-A 0.219×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM241]] (+0.59, fdr 3e-05), [[ARHGAP8]] (+0.58, fdr 2e-05), [[PAX9]] (+0.55, fdr 5e-05); moves opposite to [[PIPOX]] (-0.56, fdr 3e-05), [[EFCAB6]] (-0.56, fdr 1e-05), [[GTF2IRD2]] (-0.55, fdr 3e-05).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[STON2]] → it (grade B ⚠); 13 go from it, the strongest it → cells under [[Lapatinib ditosylate (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5151.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +11.5 | 8e-28 | 44/45 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.60×** | +9.2 | 1e-17 | 39/45 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +9.1 | 1e-17 | 40/45 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +7.7 | 2e-12 | 38/45 (NCI-H2347, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +6.1 | 1e-07 | 31/45 (NCI-H1573, J82, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.76×** | +5.8 | 7e-07 | 27/45 (J82, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +5.2 | 2e-05 | 26/45 (BT-474, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 6e-04 | 25/45 (NCI-H2347, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +4.2 | 0.002 | 20/45 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.22×** | +3.8 | 0.007 | 19/45 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.028 | 14/44 (SW480, LS 180, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5151.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (SW1417 0.348×, BT-474 0.255×, Panc 03.27 0.403×, HT-29 0.367×, …); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (RKO 0.164×, A-427 0.156×, C32 0.176×, MIA PaCa-2 0.247×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 4 lines (RKO 0.130×, MIA PaCa-2 0.140×, SK-MEL-2 0.149×, HEC-1-A 0.211×); [[PH-797804 (drug)]] 5 µM in 1 line (HEC-1-A 0.219×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.557×** | -11.0 | 3e-25 | 26/39 (RPMI-7951, LoVo, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.556×** | -10.6 | 1e-23 | 28/42 (RKO, A-427, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.583×** | -10.5 | 1e-23 | 32/45 (H4, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.404×** | -9.2 | 4e-18 | 35/46 (RKO, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.770×** | -7.1 | 2e-10 | 27/45 (SW1417, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.816×** | -5.5 | 4e-06 | 24/45 (A549, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.823×** | -3.8 | 0.012 | 19/44 (HCT15, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.876× | -3.5 | 0.028 | 15/45 (SNU-423, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | 0.850× | -3.2 | 0.10 | 17/44 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5151. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 73.7 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.130× (z -10.7) |
| [[KATO III (line)]] | alt | 94.7 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.260× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -11.9) |
| [[LoVo (line)]] | wt | 54.1 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.78× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 75.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.247× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.140× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 32.6 | 3 | 1 | [[Tucidinostat (drug)]] 5 µM 2.46× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -9.3) |
| [[A-427 (line)]] | wt | 54.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 64.7 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 1.68× (z +8.5) | [[TAK-901 (drug)]] 5 µM 0.211× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 81.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -12.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 42.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.422× (z -10.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 79.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -14.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 58.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -14.7) |
| [[H4 (line)]] | wt | 78.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.9) ⚠ cell-cycle shift, explains ~80% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -15.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 64.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -11.0) ⚠ cell-cycle shift, explains ~80% of this change |
| [[LS 180 (line)]] | wt | 94.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 30.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.89× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 2.88× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 73.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.149× (z -9.8) |
| [[SNU-423 (line)]] | alt | 82.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.409× (z -9.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 136 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -12.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 83.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -11.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 53.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -13.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 95.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -10.1) |
| [[CHP-212 (line)]] | wt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -10.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 64.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -11.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 180 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -12.9) |
| [[RPMI-7951 (line)]] | alt | 68.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -17.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 46.0 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.220× (z -9.1) |
| [[SW1417 (line)]] | alt | 160 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -14.9) |
| [[SW48 (line)]] | wt | 43.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -11.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.42 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 97.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.43 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.88 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5151), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*31 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM241]] | +0.59 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[ARHGAP8]] | +0.58 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[PAX9]] | +0.55 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[EDA]] | +0.55 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[ANKS6]] | +0.54 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[ENDOD1]] | +0.52 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[METAP1]] | +0.51 | +0.52 / +0.37 | both halves | 8e-05 |  |
| [[USB1]] | +0.51 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[GNPNAT1]] | +0.51 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[STON2]] | +0.51 | +0.32 / +0.56 | both halves | 1e-04 |  |
| [[LMBR1]] | +0.51 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[CBLC]] | +0.50 | +0.41 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*69 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIPOX]] | -0.56 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[EFCAB6]] | -0.56 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[GTF2IRD2]] | -0.55 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[KAT6B]] | -0.55 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[OSCP1]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[GPAT4-AS1]] | -0.55 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[EFCAB2]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[BBOF1]] | -0.53 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[PPP5D1P-1]] | -0.53 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[ZCWPW1]] | -0.53 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[SP2]] | -0.52 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[COQ7]] | -0.52 | -0.49 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STON2]] | B | STON2 activity raises PRRG1's level | lines that do not express STON2 (19) vs lines expressing it (31) | 1.64× lower at baseline in the lines without STON2 | 0.013 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PRRG1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers PRRG1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CBLC]] | B | CBLC activity strengthens PRRG1's drug response | lines that do not express CBLC (28) vs lines expressing it (18) | the lines without CBLC respond 0.82× as strongly (z diff +0.79); rises at some drug-doses, falls at others (49% from rises): Idarubicin (hydrochloride) 5 µM: 0.87x vs 0.52x (z diff +5.8); Tucidinostat 5 µM: 1.49x vs 1.67x (z diff +1.5); Tucidinostat 0.5 µM: 1.57x vs 1.72x (z diff +1.1) | 0.094 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | PRRG1 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express PRRG1 (3) vs lines expressing it (45) | the lines without PRRG1: 0.71× the cells of the other lines | 0.010 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, S100A6, AIFM2 |
| cells under [[NVP-BHG712 (drug)]] 5 µM | C | PRRG1 activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express PRRG1 (3) vs lines expressing it (45) | the lines without PRRG1: 0.71× the cells of the other lines | 0.018 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, S100A6, AIFM2 |
| cells under [[Methylprednisolone succinate (drug)]] 0.5 µM | C | PRRG1 activity lowers the cells' numbers under Methylprednisolone succinate 0.5 µM (makes them more sensitive) | lines that do not express PRRG1 (3) vs lines expressing it (45) | the lines without PRRG1: 1.53× the cells of the other lines | 0.028 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, S100A6, AIFM2 |
| cells under [[Clopidogrel (drug)]] 0.05 µM | C | PRRG1 activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express PRRG1 (3) vs lines expressing it (45) | the lines without PRRG1: 0.66× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, S100A6, AIFM2 |
| cells under [[Irinotecan (drug)]] 0.5 µM | C | PRRG1 activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express PRRG1 (3) vs lines expressing it (45) | the lines without PRRG1: 0.68× the cells of the other lines | 0.036 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, S100A6, AIFM2 |
| cells under [[venetoclax (drug)]] 0.5 µM | C | PRRG1 activity raises the cells' numbers under venetoclax 0.5 µM (protects the cells) | lines that do not express PRRG1 (3) vs lines expressing it (45) | the lines without PRRG1: 0.71× the cells of the other lines | 0.038 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, S100A6, AIFM2 |
| [[GJA3]] | C | PRRG1 activity lowers GJA3's level | lines that do not express PRRG1 (3) vs lines expressing it (47) | 5.80× higher at baseline in the lines without PRRG1 | 0.040 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, S100A6, AIFM2 |
| cells under [[MK-3903 (drug)]] 0.05 µM | C | PRRG1 activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express PRRG1 (3) vs lines expressing it (45) | the lines without PRRG1: 0.75× the cells of the other lines | 0.046 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, S100A6, AIFM2 |
| cells under [[TAK-901 (drug)]] 0.05 µM | C | PRRG1 activity raises the cells' numbers under TAK-901 0.05 µM (protects the cells) | lines that do not express PRRG1 (3) vs lines expressing it (45) | the lines without PRRG1: 0.70× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, S100A6, AIFM2 |
| cells under [[Fulvestrant (drug)]] 5 µM | C | PRRG1 activity raises the cells' numbers under Fulvestrant 5 µM (protects the cells) | lines that do not express PRRG1 (3) vs lines expressing it (45) | the lines without PRRG1: 0.76× the cells of the other lines | 0.056 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, S100A6, AIFM2 |
| cells under [[c-Kit-IN-1 (drug)]] 0.5 µM | C | PRRG1 activity raises the cells' numbers under c-Kit-IN-1 0.5 µM (protects the cells) | lines that do not express PRRG1 (3) vs lines expressing it (45) | the lines without PRRG1: 0.69× the cells of the other lines | 0.067 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, S100A6, AIFM2 |
| [[RAB11B-AS1]] | C | PRRG1 activity raises RAB11B-AS1's level | lines that do not express PRRG1 (3) vs lines expressing it (47) | 2.07× lower at baseline in the lines without PRRG1 | 0.078 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, S100A6, AIFM2 |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.481). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (0.7, 15.1); signed map (-19.7, 36.7). **Vector** length 107, 27.2% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.6 | +11.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.0 | +9.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.9 | +7.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.6 | +5.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +5.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.4 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | -5.6 | -5.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.0 | -9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.1 | -10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.4 | -10.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -1.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.1 | -1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | proline rich and Gla domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp21.1 — chrX:37,349,309-37,457,292 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRGP1 |
| Gene groups (HGNC) | Proline rich and Gla domain containing |
| Matched by | ensembl_id |

UniProt [O14668](https://www.uniprot.org/uniprotkb/O14668) carries no function annotation.

**Summary**, from NCBI Gene [5638](https://www.ncbi.nlm.nih.gov/gene/5638):

> This gene encodes a vitamin K-dependent, gamma-carboxyglutamic acid (Gla)-containing, single-pass transmembrane protein. This protein contains a Gla domain at the N-terminus, preceded by a propeptide sequence required for post-translational gamma-carboxylation of specific glutamic acid residues by a vitamin K-dependent gamma-carboxylase. The C-terminus is proline-rich containing PPXY and PXXP motifs found in a variety of signaling and cytoskeletal proteins. This gene is highly expressed in the …

**Accessions** — [HGNC:9469](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9469) · Entrez [5638](https://www.ncbi.nlm.nih.gov/gene/5638) · UniProt [O14668](https://www.uniprot.org/uniprotkb/O14668) · Ensembl [ENSG00000130962](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130962)

## Data

Gene col 5151: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5151); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5151, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5151]; `tensor/DDL_lfc|DDL_z.npy` [5151]; `embed/gene_vectors.npy` [5151]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5151 or target_col == 5151). Every well: [[PRRG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRRG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
