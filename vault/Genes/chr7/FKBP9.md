---
symbol: "FKBP9"
type: "gene"
col: 4359
ensembl_id: "ENSG00000122642"
name: "FKBP prolyl isomerase 9"
location: "7p14.3"
module: 29
arm: "+"
pooled_cpm: 44.33
n_lines_expressing: 48
n_dd_up: 3
n_dd_down: 18
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# FKBP9

*FKBP prolyl isomerase 9* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.09× (z +8.5, q 8e-15, up in 29 of 39 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 3.62×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (A549 3.47×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 2.92×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.191× (z -28.1, q 0e+00, down in 45 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTSZ]] (+0.82, fdr 7e-06), [[CRTAP]] (+0.81, fdr 7e-06), [[PPT1]] (+0.77, fdr 7e-06); moves opposite to [[ZNF593]] (-0.74, fdr 1e-05), [[SMIM26]] (-0.71, fdr 8e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[CROCCP2-1]] (-0.71, fdr 7e-06), [[MED19]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FKBP9P1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[IRX5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4359.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 3.62×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (A549 3.47×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 2.92×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +8.5 | 8e-15 | 29/39 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +6.2 | 2e-07 | 30/44 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +4.6 | 1e-03 | 25/41 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4359.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.191×** | -28.1 | 0e+00 | 45/45 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.229×** | -17.7 | 0e+00 | 40/44 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.223×** | -17.3 | 0e+00 | 46/46 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.472×** | -9.0 | 3e-17 | 40/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.578×** | -6.6 | 6e-09 | 34/46 (SW480, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.585×** | -6.4 | 1e-08 | 34/46 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.593×** | -6.3 | 3e-08 | 34/46 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.606×** | -6.0 | 1e-07 | 34/45 (SW480, COLO 205, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.666×** | -4.9 | 7e-05 | 27/46 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.713×** | -4.0 | 0.003 | 24/46 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.719×** | -3.7 | 0.010 | 22/46 (SHP-77, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.728×** | -3.6 | 0.013 | 24/41 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.741×** | -3.6 | 0.015 | 25/46 (SHP-77, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.814×** | -3.4 | 0.023 | 21/46 (SHP-77, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.817×** | -3.4 | 0.026 | 19/44 (SW480, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.766×** | -3.2 | 0.052 | 21/46 (HT-29, SHP-77, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.777×** | -3.0 | 0.081 | 17/46 (H4, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4359. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 110 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0863× (z -26.8) |
| [[LoVo (line)]] | wt | 72.2 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0465× (z -35.6) |
| [[SHP-77 (line)]] | alt | 185 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0478× (z -30.5) |
| [[C32 (line)]] | wt | 113 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -20.5) |
| [[COLO 205 (line)]] | alt | 71.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0271× (z -29.7) |
| [[NCI-H460 (line)]] | wt | 40.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -23.8) |
| [[SK-MEL-2 (line)]] | alt | 51.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -15.6) |
| [[A-172 (line)]] | wt | 79.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -18.3) |
| [[A549 (line)]] | wt | 33.6 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -14.5) |
| [[Hs 766T (line)]] | wt | 36.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -19.9) |
| [[LS 180 (line)]] | wt | 43.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0880× (z -27.8) |
| [[A-427 (line)]] | wt | 42.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.62× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 37.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0980× (z -24.1) |
| [[BT-474 (line)]] | alt | 27.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -15.7) |
| [[C-33 A (line)]] | alt | 38.7 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.132× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.346× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 32.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -15.7) |
| [[HOP62 (line)]] | alt | 39.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -22.9) |
| [[HT-29 (line)]] | alt | 38.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0916× (z -19.5) |
| [[KATO III (line)]] | alt | 67.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -25.4) |
| [[MIA PaCa-2 (line)]] | alt | 41.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0796× (z -18.1) |
| [[NCI-H23 (line)]] | alt | 33.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0729× (z -25.2) |
| [[PANC-1 (line)]] | alt | 37.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -20.6) |
| [[SNU-423 (line)]] | alt | 21.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -18.4) |
| [[CFPAC-1 (line)]] | alt | 15.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 38.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.157× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 19.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -13.0) |
| [[NCI-H2030 (line)]] | alt | 27.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -17.3) |
| [[NCI-H2347 (line)]] | alt | 16.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -16.5) |
| [[Panc 03.27 (line)]] | alt | 24.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -11.8) |
| [[SW 1088 (line)]] | alt | 104 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0345× (z -11.7) |
| [[SW 900 (line)]] | alt | 18.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -13.7) |
| [[SW1417 (line)]] | alt | 29.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -17.6) |
| [[A498 (line)]] | wt | 41.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -9.8) |
| [[H4 (line)]] | wt | 71.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0863× (z -20.4) |
| [[HCT15 (line)]] | alt | 31.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -10.3) |
| [[HS-578T (line)]] | alt | 46.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -10.0) |
| [[J82 (line)]] | alt | 28.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 26.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 38.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -14.6) |
| [[SW 1271 (line)]] | alt | 25.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0795× (z -9.5) |
| [[SW48 (line)]] | wt | 33.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -11.7) |
| [[AN3 CA (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.39 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4359), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSZ]] | +0.82 | +0.76 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[CRTAP]] | +0.81 | +0.78 / +0.78 | both halves | 7e-06 |  |
| [[PPT1]] | +0.77 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[DHFR]] | +0.76 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[RPN1]] | +0.75 | +0.65 / +0.81 | both halves | 7e-06 |  |
| [[SELENON]] | +0.75 | +0.72 / +0.72 | both halves | 7e-06 | same gene group |
| [[EMC1]] | +0.74 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[LAMP1]] | +0.73 | +0.56 / +0.76 | both halves | 1e-05 |  |
| [[CDK16]] | +0.73 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[DDOST]] | +0.73 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[EIF4H]] | +0.72 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[ERMP1]] | +0.72 | +0.64 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF593]] | -0.74 | -0.57 / -0.78 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.71 | -0.58 / -0.72 | both halves | 8e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CROCCP2-1]] | -0.71 | -0.70 / -0.72 | both halves | 7e-06 |  |
| [[MED19]] | -0.69 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[PIGBOS1]] | -0.69 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[ATF4]] | -0.68 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[MRPL46]] | -0.67 | -0.49 / -0.69 | both halves | 1e-05 |  |
| [[MRPS18C]] | -0.66 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[NKAP]] | -0.66 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[TMEM70]] | -0.65 | -0.57 / -0.68 | both halves | 9e-06 |  |
| [[ERVK3-1]] | -0.65 | -0.56 / -0.75 | both halves | 1e-05 |  |
| [[ZNF503]] | -0.65 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[FDX2]] | -0.64 | -0.51 / -0.72 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FKBP9P1]] | B | FKBP9P1 activity raises FKBP9's level | lines that do not express FKBP9P1 (10) vs lines expressing it (40) | 2.09× lower at baseline in the lines without FKBP9P1 | 0.040 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRX5]] | C | FKBP9's natural level strengthens IRX5's drug response | FKBP9's natural level across 38 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.28; direction not clear | 0.069 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.821). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.5, -22.3); signed map (-23.0, -38.6). **Vector** length 101, 27.1% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.4 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.4 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.1 | +6.2 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +4.5 | +0.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +4.2 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | -0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.7 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -17.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.3 | -9.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.2 | -17.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.5 | -28.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | FKBP prolyl isomerase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:32,957,404-33,006,930 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FKBP60, FKBP63 |
| Gene groups (HGNC) | EF-hand domain containing; FKBP prolyl isomerase family |
| Reactome | 3 pathways, smallest: Association of TriC/CCT with target proteins during biosynthesis; Chaperonin-mediated protein folding; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [O95302](https://www.uniprot.org/uniprotkb/O95302) (Peptidyl-prolyl cis-trans isomerase FKBP9):

> PPIases accelerate the folding of proteins during protein synthesis.

**Summary**, from NCBI Gene [11328](https://www.ncbi.nlm.nih.gov/gene/11328):

> Predicted to enable calcium ion binding activity and peptidyl-prolyl cis-trans isomerase activity. Predicted to be involved in protein folding. Predicted to be active in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3725](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3725) · Entrez [11328](https://www.ncbi.nlm.nih.gov/gene/11328) · UniProt [O95302](https://www.uniprot.org/uniprotkb/O95302) · Ensembl [ENSG00000122642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122642)

## Data

Gene col 4359: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4359); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4359, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4359]; `tensor/DDL_lfc|DDL_z.npy` [4359]; `embed/gene_vectors.npy` [4359]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4359 or target_col == 4359). Every well: [[FKBP9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FKBP9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
