---
symbol: "DBF4B"
type: "gene"
col: 8450
ensembl_id: "ENSG00000161692"
name: "DBF4B-CDC7 kinase regulatory subunit"
location: "17q21.31"
module: 71
arm: "+"
pooled_cpm: 26.34
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# DBF4B

*DBF4B-CDC7 kinase regulatory subunit* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.35× (z +39.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.703× (z -9.5, q 9e-19, down in 30 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.693× (z -7.0, q 3e-10, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASF1B]] (+0.76, fdr 7e-06), [[CDC25C]] (+0.73, fdr 7e-06), [[RFWD3]] (+0.73, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8450.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.35×** | +39.6 | 0e+00 | 47/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +15.2 | 0e+00 | 37/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +13.3 | 5e-38 | 37/48 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +9.1 | 2e-17 | 28/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.54×** | +8.2 | 2e-14 | 32/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.50×** | +7.7 | 9e-13 | 32/47 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.39×** | +6.2 | 4e-08 | 25/47 (NCI-H23, HS-578T, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.37×** | +6.0 | 1e-07 | 23/47 (NCI-H23, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.36×** | +5.8 | 4e-07 | 25/47 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +4.6 | 2e-04 | 16/47 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.3 | 9e-04 | 0/48 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.26×** | +4.3 | 9e-04 | 17/46 (HCT15, Panc 03.27, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.003 | 12/47 (HOP62, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.23×** | +3.9 | 0.003 | 16/47 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +3.8 | 0.006 | 17/48 (LoVo, A549, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.009 | 11/47 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 0.5 µM |  | 1.20× | +3.4 | 0.023 | 8/47 (NCI-H460, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8450.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.703×** | -9.5 | 9e-19 | 30/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.630×** | -8.8 | 3e-16 | 34/48 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.645×** | -8.4 | 1e-14 | 28/43 (NCI-H23, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.673×** | -7.3 | 6e-11 | 20/35 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.693×** | -7.0 | 3e-10 | 27/47 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.773×** | -6.9 | 4e-10 | 30/48 (HS-578T, SHP-77, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.702×** | -4.8 | 1e-04 | 18/44 (NCI-H460, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.771×** | -4.8 | 1e-04 | 21/47 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.765×** | -4.7 | 1e-04 | 19/40 (SW1417, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.793×** | -4.4 | 5e-04 | 14/47 (C-33 A, CHP-212, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.807×** | -4.1 | 0.002 | 14/48 (SHP-77, A498, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.835× | -3.4 | 0.027 | 15/47 (SW 900, MIA PaCa-2, …) | two highest doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.830×** | -3.4 | 0.027 | 17/47 (NCI-H2030, SW1417, …) | top dose only |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.782×** | -3.4 | 0.033 | 5/48 (SW480, A-172, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Penfluridol (drug)]] 5 µM |  | 0.841× | -3.2 | 0.055 | 12/47 (AN3 CA, NCI-H661, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8450. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 55.2 | 0 | 4 (2 ⚠) | — | [[Silodosin (drug)]] 5 µM 0.0691× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 39.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.30× (z +30.1) | — |
| [[HOP62 (line)]] | alt | 32.7 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -10.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 38.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.117× (z -17.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 32.4 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +17.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.362× (z -9.0) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 41.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.86× (z +22.0) | — |
| [[Panc 03.27 (line)]] | alt | 32.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.81× (z +23.6) | — |
| [[SW1417 (line)]] | alt | 23.0 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.61× (z +16.0) | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -11.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 26.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.46× (z +27.2) | — |
| [[A498 (line)]] | wt | 32.6 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0857× (z -25.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 17.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -9.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 47.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -9.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 21.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +12.1) | [[Silodosin (drug)]] 5 µM 0.212× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 16.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 20.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.45× (z +19.6) | [[Belzutifan (drug)]] 5 µM 0.0567× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 29.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.90× (z +18.0) | — |
| [[NCI-H23 (line)]] | alt | 52.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.368× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 24.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.6) | [[Selinexor (drug)]] 5 µM 0.398× (z -10.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 24.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +22.6) | — |
| [[SK-MEL-2 (line)]] | alt | 48.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 20.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.86× (z +15.2) | — |
| [[A-172 (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.413× (z -8.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 42.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.413× (z -10.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 19.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +16.6) | — |
| [[HCT15 (line)]] | alt | 34.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.00× (z +17.4) | — |
| [[Hs 766T (line)]] | wt | 17.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +13.3) | — |
| [[HS-578T (line)]] | alt | 19.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +14.2) | — |
| [[HT-29 (line)]] | alt | 15.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.20× (z +17.8) | — |
| [[KATO III (line)]] | alt | 24.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.38× (z +19.8) | — |
| [[LoVo (line)]] | wt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.90× (z +18.8) | — |
| [[LOX-IMVI (line)]] | wt | 28.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.54× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 15.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +12.7) | — |
| [[PANC-1 (line)]] | alt | 23.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +19.9) | — |
| [[RKO (line)]] | wt | 30.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +13.0) | — |
| [[RPMI-7951 (line)]] | alt | 21.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.60× (z +14.6) | — |
| [[SNU-1 (line)]] | wt | 27.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 22.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +11.9) | — |
| [[AsPC-1 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8450), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASF1B]] | +0.76 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[CDC25C]] | +0.73 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[RFWD3]] | +0.73 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[CENPO]] | +0.73 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[LRR1]] | +0.72 | +0.62 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[HAUS8]] | +0.72 | +0.69 / +0.79 | both halves | 7e-06 |  |
| [[GTSE1]] | +0.71 | +0.70 / +0.81 | both halves | 7e-06 |  |
| [[C21orf58]] | +0.71 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[WDR62]] | +0.71 | +0.72 / +0.74 | both halves | 7e-06 | STRING 457 |
| [[TACC3]] | +0.71 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[CDCA5]] | +0.69 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[KIF2C]] | +0.69 | +0.70 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DBF4B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[AURKB]] | C | AURKB activity raises DBF4B's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.90× lower at baseline in the lines without AURKB | 0.061 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises DBF4B's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 1.98× lower at baseline in the lines without NDC80 | 0.070 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[MELK]], [[TK1]] | C | MELK, TK1 activity raises DBF4B's level | lines that do not express MELK, TK1 (3) vs lines expressing them (47) | 2.17× lower at baseline in the lines without MELK, TK1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.749). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.5, -49.1); signed map (-42.4, -44.0). **Vector** length 119, 31.4% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +39.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +15.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +13.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +9.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +3.3 | +8.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.2 | +3.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +1.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -8.3 | -9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.9 | -6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.3 | -4.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -6.2 | -8.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.1 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | DBF4B-CDC7 kinase regulatory subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:44,708,608-44,752,264 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13087, DRF1, ASKL1, chifb, ZDBF1B |
| Gene groups (HGNC) | Zinc fingers DBF-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFT6](https://www.uniprot.org/uniprotkb/Q8NFT6) (Protein DBF4 homolog B):

> Regulatory subunit for CDC7 which activates its kinase activity thereby playing a central role in DNA replication and cell proliferation. Required for progression of S and M phases. The complex CDC7-DBF4B selectively phosphorylates MCM2 subunit at 'Ser-40' and then is involved in regulating the initiation of DNA replication during cell cycle.

**Summary**, from NCBI Gene [80174](https://www.ncbi.nlm.nih.gov/gene/80174):

> This gene encodes a regulator of the cell division cycle 7 homolog (S. cerevisiae) protein, a serine-threonine kinase which links cell cycle regulation to genome duplication. This protein localizes to the nucleus and, in complex with the cell division cycle 7 homolog (S. cerevisiae) protein, may facilitate M phase progression. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:17883](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17883) · Entrez [80174](https://www.ncbi.nlm.nih.gov/gene/80174) · UniProt [Q8NFT6](https://www.uniprot.org/uniprotkb/Q8NFT6) · Ensembl [ENSG00000161692](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161692)

## Data

Gene col 8450: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8450); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8450, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8450]; `tensor/DDL_lfc|DDL_z.npy` [8450]; `embed/gene_vectors.npy` [8450]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8450 or target_col == 8450). Every well: [[DBF4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DBF4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
