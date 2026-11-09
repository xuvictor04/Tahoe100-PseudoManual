---
symbol: "SHQ1"
type: "gene"
col: 6921
ensembl_id: "ENSG00000144736"
name: "SHQ1, H/ACA ribonucleoprotein assembly factor"
location: "3p13"
module: 40
arm: "+"
pooled_cpm: 47.52
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# SHQ1

*SHQ1, H/ACA ribonucleoprotein assembly factor* — 3p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.05× (z +18.8, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.662× (z -7.0, q 2e-09, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H23 0.143×, SK-MEL-2 0.240×, NCI-H1573 0.218×, SW480 0.483×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SHP-77 0.0973×, SK-MEL-2 0.312×, NCI-H1792 0.191×, C-33 A 0.203×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.05 µM in 2 lines (RKO 0.294×, SNU-1 0.255×); [[Harringtonine (drug)]] 0.5 µM in 1 line (HOP62 0.400×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF121]] (+0.76, fdr 7e-06), [[RPA1]] (+0.73, fdr 7e-06), [[SDHAP1]] (+0.72, fdr 1e-05); moves opposite to [[FKRP]] (-0.70, fdr 4e-05), [[LIG4]] (-0.69, fdr 1e-05), [[RAB30-DT]] (-0.69, fdr 9e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF606]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6921.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.05×** | +18.8 | 0e+00 | 47/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.76×** | +17.1 | 0e+00 | 48/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.62×** | +16.2 | 0e+00 | 47/48 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.85×** | +9.2 | 5e-18 | 42/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +7.5 | 9e-12 | 36/48 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.44×** | +6.1 | 9e-08 | 39/48 (HOP62, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +5.9 | 3e-07 | 32/48 (RKO, SW1417, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +5.6 | 2e-06 | 32/48 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +4.8 | 1e-04 | 28/48 (LOX-IMVI, RKO, …) | all doses, flat | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +4.8 | 1e-04 | 33/48 (HEC-1-A, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.56×** | +3.9 | 0.005 | 20/44 (NCI-H1792, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +3.9 | 0.005 | 18/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.006 | 18/48 (NCI-H2030, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.009 | 19/48 (RKO, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.031 | 18/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6921.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H23 0.143×, SK-MEL-2 0.240×, NCI-H1573 0.218×, SW480 0.483×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SHP-77 0.0973×, SK-MEL-2 0.312×, NCI-H1792 0.191×, C-33 A 0.203×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.05 µM in 2 lines (RKO 0.294×, SNU-1 0.255×); [[Harringtonine (drug)]] 0.5 µM in 1 line (HOP62 0.400×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.662×** | -7.0 | 2e-09 | 38/48 (HOP62, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.705×** | -5.9 | 1e-06 | 28/48 (RKO, SNU-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.781×** | -5.8 | 1e-06 | 31/48 (HOP62, HS-578T, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.732×** | -5.1 | 6e-05 | 22/42 (SHP-77, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.756×** | -4.7 | 3e-04 | 22/47 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **0.759×** | -4.7 | 3e-04 | 24/47 (Panc 03.27, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 5 µM |  | 0.855× | -3.7 | 0.015 | 11/48 (A498, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.822×** | -3.3 | 0.065 | 20/48 (AsPC-1, SNU-423, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.821× | -3.1 | 0.13 | 15/47 (NCI-H2347, AsPC-1, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 0.825× | -3.0 | 0.15 | 16/44 (AN3 CA, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6921. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 60.8 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.68× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.483× (z -10.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 57.6 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.92× (z +10.3) | [[Docetaxel (drug)]] 0.05 µM 0.218× (z -14.6) ⚠ transcription drop; cell-cycle shift, explains ~41% of this change |
| [[PANC-1 (line)]] | alt | 42.3 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.452× (z -9.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 99.5 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.95× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -14.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 49.7 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.10× (z +12.0) | [[Harringtonine (drug)]] 0.5 µM 0.400× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 53.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.43× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 47.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.76× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -14.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 42.9 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.28× (z +11.3) | [[Homoharringtonine (drug)]] 0.05 µM 0.294× (z -9.5) |
| [[SW 900 (line)]] | alt | 47.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.83× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.37× (z +8.6) | — |
| [[A-172 (line)]] | wt | 29.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.13× (z +11.1) | — |
| [[A549 (line)]] | wt | 57.7 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.09× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.303× (z -10.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 27.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +11.0) | — |
| [[C32 (line)]] | wt | 36.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.25× (z +10.3) | — |
| [[HEC-1-A (line)]] | alt | 53.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.97× (z +15.5) | — |
| [[J82 (line)]] | alt | 44.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.54× (z +11.7) | — |
| [[LoVo (line)]] | wt | 38.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.88× (z +12.5) | — |
| [[LS 180 (line)]] | wt | 39.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.50× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 34.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.00× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 45.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.86× (z +13.6) | — |
| [[NCI-H460 (line)]] | wt | 31.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.94× (z +13.4) | — |
| [[RPMI-7951 (line)]] | alt | 97.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.92× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -9.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 60.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +12.2) | — |
| [[A498 (line)]] | wt | 71.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -10.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 26.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.90× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 27.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.76× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.191× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 57.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.62× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -18.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 54.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.91× (z +8.6) | — |
| [[A-427 (line)]] | wt | 39.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.83× (z +9.1) | — |
| [[C-33 A (line)]] | alt | 58.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -11.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 23.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.95× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 62.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -9.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 26.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.167× (z -9.4) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 73.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.95× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 21.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.75× (z +9.3) | — |
| [[KATO III (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.403× (z -8.8) ⚠ transcription drop; cell-cycle shift, explains ~41% of this change |
| [[MIA PaCa-2 (line)]] | alt | 44.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.79× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 82.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0973× (z -22.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 44.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.255× (z -8.7) |
| [[AN3 CA (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6921), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF121]] | +0.76 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[RPA1]] | +0.73 | +0.71 / +0.67 | both halves | 7e-06 | pathway: Chromosome Maintenance |
| [[SDHAP1]] | +0.72 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[PIK3R2]] | +0.71 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.71 | +0.71 / +0.58 | both halves | 8e-06 |  |
| [[IQCB1]] | +0.69 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.69 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[THOC3]] | +0.69 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[PHKA2]] | +0.69 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[TAF5L]] | +0.69 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[NUDT21]] | +0.69 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[OXNAD1]] | +0.68 | +0.61 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKRP]] | -0.70 | -0.73 / -0.41 | both halves | 4e-05 |  |
| [[LIG4]] | -0.69 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[RAB30-DT]] | -0.69 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[KRCC1]] | -0.68 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[SKIL]] | -0.68 | -0.68 / -0.53 | both halves | 1e-05 |  |
| [[LZIC]] | -0.68 | -0.73 / -0.46 | both halves | 2e-05 |  |
| [[BAZ2B]] | -0.68 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[TIA1]] | -0.68 | -0.74 / -0.40 | both halves | 5e-05 |  |
| [[APLF]] | -0.67 | -0.70 / -0.44 | both halves | 3e-05 |  |
| [[ZNF764]] | -0.67 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[ZBED5]] | -0.67 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | -0.66 | -0.65 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF606]] | B | ZNF606 activity raises SHQ1's level | lines that do not express ZNF606 (13) vs lines expressing it (37) | 1.25× lower at baseline in the lines without ZNF606 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, C19orf18, ZNF569 |
| [[HACE1]] | C | HACE1 activity raises SHQ1's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.82× lower at baseline in the lines without HACE1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-5.9, -15.2); signed map (-39.1, -12.3). **Vector** length 104, 28.2% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.8 | +17.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +18.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.0 | +16.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +9.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.1 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +3.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.3 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +3.7 |
|  | [[EX229 (drug)]] 0.05 µM |  | +1.8 | +1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.7 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -11.9 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -9.5 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.9 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.3 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.0 | -5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | SHQ1, H/ACA ribonucleoprotein assembly factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p13 — chr3:72,749,277-72,861,914 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10539, Shq1p |
| Reactome | 5 pathways, smallest: Telomere Extension By Telomerase; Extension of Telomeres; Telomere Maintenance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PI26](https://www.uniprot.org/uniprotkb/Q6PI26) (Protein SHQ1 homolog):

> Required for the quantitative accumulation of H/ACA ribonucleoproteins (RNPs), including telomerase, probably through the stabilization of DKC1, from the time of its synthesis until its association with NOP10, NHP2, and NAF1 at the nascent H/ACA RNA.

**Summary**, from NCBI Gene [55164](https://www.ncbi.nlm.nih.gov/gene/55164):

> SHQ1 assists in the assembly of H/ACA-box ribonucleoproteins that function in the processing of ribosomal RNAs, modification of spliceosomal small nuclear RNAs, and stabilization of telomerase (see MIM 602322) (Grozdanov et al., 2009 [PubMed 19383767]).[supplied by OMIM, Dec 2010]

**Accessions** — [HGNC:25543](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25543) · Entrez [55164](https://www.ncbi.nlm.nih.gov/gene/55164) · UniProt [Q6PI26](https://www.uniprot.org/uniprotkb/Q6PI26) · Ensembl [ENSG00000144736](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144736)

## Data

Gene col 6921: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6921); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6921, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6921]; `tensor/DDL_lfc|DDL_z.npy` [6921]; `embed/gene_vectors.npy` [6921]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6921 or target_col == 6921). Every well: [[SHQ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHQ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
