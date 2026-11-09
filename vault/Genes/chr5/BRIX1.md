---
symbol: "BRIX1"
type: "gene"
col: 3466
ensembl_id: "ENSG00000113460"
name: "biogenesis of ribosomes BRX1"
location: "5p13.2"
module: 1
arm: "+"
pooled_cpm: 58.33
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# BRIX1

*biogenesis of ribosomes BRX1* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.22× (z +10.5, q 6e-23, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~62% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.83× (z +9.7, q 1e-19, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.335×, A498 0.464×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (AN3 CA 0.130×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.645×; ⚠ position not correctable).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAK1IP1]] (+0.79, fdr 7e-06), [[NIFK]] (+0.78, fdr 7e-06), [[SURF6]] (+0.77, fdr 7e-06); moves opposite to [[PSAP]] (-0.70, fdr 7e-06), [[IDS]] (-0.66, fdr 7e-06), [[GRN]] (-0.62, fdr 9e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[WHRN]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3466.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **2.22×** | +10.5 | 6e-23 | 44/48 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.83×** | +9.7 | 1e-19 | 47/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.55×** | +8.6 | 2e-15 | 47/48 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.16×** | +8.0 | 2e-13 | 48/49 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.44×** | +8.0 | 2e-13 | 47/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **2.26×** | +7.6 | 3e-12 | 44/48 (LS 180, NCI-H1573, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.16×** | +7.2 | 6e-11 | 45/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **2.17×** | +6.9 | 3e-10 | 41/47 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +5.9 | 3e-07 | 40/47 (LOX-IMVI, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.81×** | +5.5 | 2e-06 | 43/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.77×** | +5.3 | 6e-06 | 42/48 (LS 180, PANC-1, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.88×** | +5.2 | 1e-05 | 36/48 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +4.7 | 1e-04 | 37/48 (CFPAC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.72×** | +4.7 | 1e-04 | 29/45 (NCI-H1792, HT-29, …) | inconsistent across doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~82% of this change | **1.53×** | +4.0 | 0.003 | 29/47 (HT-29, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.18×** | +3.8 | 0.005 | 35/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.52×** | +3.6 | 0.009 | 28/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.05×** | +3.5 | 0.014 | 35/48 (SW1417, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.021 | 31/49 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.032 | 26/48 (SW 900, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.032 | 25/48 (CFPAC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.94×** | +3.2 | 0.032 | 28/48 (MIA PaCa-2, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.046 | 22/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.047 | 21/47 (NCI-H460, NCI-H23, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3466.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.335×, A498 0.464×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (AN3 CA 0.130×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.645×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.653× | -3.7 | 0.12 | 35/49 (A-427, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.716× | -3.1 | 0.37 | 27/47 (A-172, CHP-212, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3466. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 44.9 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.90× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 36.3 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +13.2) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.90× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 41.8 | 5 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.54× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.00× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 30.4 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +11.7) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.49× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 43.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 4.15× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 55.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +10.6) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 3.43× (z +9.6) | — |
| [[A549 (line)]] | wt | 40.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +12.5) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.65× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 30.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +11.9) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.81× (z +10.0) | — |
| [[H4 (line)]] | wt | 55.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +11.1) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.14× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 38.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +10.2) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.05× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 153 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +11.2) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.61× (z +10.0) | — |
| [[A498 (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 80.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 24.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +10.2) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[HEC-1-A (line)]] | alt | 46.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +8.5) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[HOP62 (line)]] | alt | 35.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.69× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 46.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.46× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 55.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +8.7) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[LoVo (line)]] | wt | 46.6 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.90× (z +8.9) ⚠ toxic; cell-cycle shift, explains ~37% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 57.2 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.645× (z -9.3) ⚠ position not correctable |
| [[RKO (line)]] | wt | 73.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 65.7 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.91× (z +8.7) | — |
| [[SW480 (line)]] | alt | 73.3 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.78× (z +10.3) | — |
| [[A-172 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 88.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 75.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3466), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAK1IP1]] | +0.79 | +0.83 / +0.73 | both halves | 7e-06 | STRING 898 |
| [[NIFK]] | +0.78 | +0.78 / +0.76 | both halves | 7e-06 | STRING 999 |
| [[SURF6]] | +0.77 | +0.76 / +0.74 | both halves | 7e-06 | STRING 960 |
| [[UTP14A]] | +0.77 | +0.81 / +0.69 | both halves | 7e-06 | STRING 651 |
| [[RRS1]] | +0.75 | +0.74 / +0.74 | both halves | 7e-06 | same gene group; STRING 977 |
| [[MRPL15]] | +0.75 | +0.69 / +0.78 | both halves | 7e-06 | STRING 462 |
| [[CEBPZ]] | +0.75 | +0.72 / +0.75 | both halves | 7e-06 | STRING 954 |
| [[LTV1]] | +0.73 | +0.75 / +0.73 | both halves | 7e-06 | STRING 908 |
| [[GEMIN6]] | +0.72 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[REXO4]] | +0.72 | +0.77 / +0.69 | both halves | 7e-06 | STRING 433 |
| [[NUFIP1]] | +0.72 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[RIOK1]] | +0.71 | +0.79 / +0.68 | both halves | 7e-06 | same gene group; STRING 447 |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSAP]] | -0.70 | -0.68 / -0.67 | both halves | 7e-06 |  |
| [[IDS]] | -0.66 | -0.59 / -0.70 | both halves | 7e-06 |  |
| [[GRN]] | -0.62 | -0.57 / -0.60 | both halves | 9e-06 |  |
| [[LAMP2]] | -0.62 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[NUCB1]] | -0.61 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[YPEL5]] | -0.61 | -0.65 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WHRN]] | C | WHRN activity raises BRIX1's level | lines that do not express WHRN (4) vs lines expressing it (46) | 1.59× lower at baseline in the lines without WHRN | 0.061 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, NKAIN1, KIAA1549; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.715). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-40.6, 0.5); signed map (-2.1, -40.9). **Vector** length 89.3, 34.5% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.52 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.54 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.53 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.5 | +7.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +8.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +3.0 | +10.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.7 | +3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +2.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -4.1 | +5.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.4 | +1.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.2 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.0 | -0.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | +0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -3.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.6 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | biogenesis of ribosomes BRX1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.2 — chr5:34,915,677-34,925,996 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BRIX, FLJ11100; previously BXDC2 |
| Gene groups (HGNC) | Brix domain containing; Ribosome biogenesis factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDN6](https://www.uniprot.org/uniprotkb/Q8TDN6) (Ribosome biogenesis protein BRX1 homolog):

> Required for biogenesis of the 60S ribosomal subunit.

**Summary**, from NCBI Gene [55299](https://www.ncbi.nlm.nih.gov/gene/55299):

> Enables RNA binding activity. Predicted to be involved in ribosomal large subunit assembly. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24170](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24170) · Entrez [55299](https://www.ncbi.nlm.nih.gov/gene/55299) · UniProt [Q8TDN6](https://www.uniprot.org/uniprotkb/Q8TDN6) · Ensembl [ENSG00000113460](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113460)

## Data

Gene col 3466: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3466); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3466, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3466]; `tensor/DDL_lfc|DDL_z.npy` [3466]; `embed/gene_vectors.npy` [3466]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3466 or target_col == 3466). Every well: [[BRIX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRIX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
