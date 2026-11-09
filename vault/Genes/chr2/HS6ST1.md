---
symbol: "HS6ST1"
type: "gene"
col: 5895
ensembl_id: "ENSG00000136720"
name: "heparan sulfate 6-O-sulfotransferase 1"
location: "2q14.3"
module: 93
arm: "+"
pooled_cpm: 17.42
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# HS6ST1

*heparan sulfate 6-O-sulfotransferase 1* — 2q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.02× (z +22.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.707× (z -5.7, q 5e-06, down in 24 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.710× (z -5.6, q 5e-06, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCORL1]] (+0.54, fdr 4e-05), [[SGSM3-AS1]] (+0.50, fdr 1e-04), [[FAM222A]] (+0.50, fdr 1e-05); moves opposite to [[MSL3]] (-0.43, fdr 2e-04), [[COPS8-DT]] (-0.42, fdr 0.003, ⚠ not reproduced), [[ZCCHC4]] (-0.42, fdr 1e-04), [[POLR1HASP]] (-0.42, fdr 7e-04).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BIVM]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5895.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.02×** | +22.7 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.56×** | +21.7 | 0e+00 | 39/47 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.24×** | +19.2 | 0e+00 | 46/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.59×** | +15.6 | 0e+00 | 45/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +7.7 | 1e-12 | 29/48 (SW1417, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +7.5 | 7e-12 | 30/48 (SW1417, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +7.4 | 1e-11 | 26/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +6.9 | 3e-10 | 26/44 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +6.6 | 2e-09 | 26/46 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.39×** | +5.4 | 5e-06 | 22/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.81×** | +5.0 | 2e-05 | 9/46 (SW480, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +4.8 | 6e-05 | 19/47 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.23×** | +4.8 | 7e-05 | 21/48 (NCI-H1573, LoVo, …) | rises with dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +4.7 | 1e-04 | 13/48 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.33×** | +4.4 | 5e-04 | 14/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.20×** | +4.1 | 0.001 | 12/48 (CFPAC-1, BT-474, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.20×** | +3.0 | 0.092 | 13/47 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5895.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.707×** | -5.7 | 5e-06 | 24/46 (KATO III, CHP-212, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.710×** | -5.6 | 5e-06 | 23/48 (A-427, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.725×** | -5.3 | 2e-05 | 22/47 (NCI-H2030, HT-29, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.585×** | -4.6 | 7e-04 | 16/48 (HT-29, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.762×** | -4.5 | 9e-04 | 17/48 (PANC-1, HepG2/C3A, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.767×** | -4.4 | 0.001 | 22/47 (HepG2/C3A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.764×** | -4.1 | 0.004 | 17/35 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.853× | -3.7 | 0.015 | 13/48 (A-172, SNU-1, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -3.3 | 0.064 | 3/48 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.830× | -3.1 | 0.13 | 17/47 (HepG2/C3A, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5895. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 17.2 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change |
| [[LoVo (line)]] | wt | 26.5 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.235× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change |
| [[A498 (line)]] | wt | 13.8 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 21.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +11.5) | — |
| [[SW480 (line)]] | alt | 14.3 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +15.8) | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -15.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 16.1 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.32× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.196× (z -9.7) |
| [[J82 (line)]] | alt | 26.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.4) | — |
| [[LOX-IMVI (line)]] | wt | 8.84 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.68× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -8.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 14.3 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +12.4) | [[Harringtonine (drug)]] 0.05 µM 0.204× (z -8.9) |
| [[LS 180 (line)]] | wt | 16.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 8.86 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.64× (z +13.4) | — |
| [[BT-474 (line)]] | alt | 37.1 | 2 | 0 | [[Binimetinib (drug)]] 5 µM 3.91× (z +9.2) | — |
| [[C32 (line)]] | wt | 10.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +14.6) | — |
| [[HEC-1-A (line)]] | alt | 34.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +8.6) | [[Lonafarnib (drug)]] 5 µM 0.113× (z -10.6) ⚠ toxic |
| [[HS-578T (line)]] | alt | 11.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +11.0) | — |
| [[KATO III (line)]] | alt | 12.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.247× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +9.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -9.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 12.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.92× (z +17.4) | — |
| [[NCI-H2030 (line)]] | alt | 24.8 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.26× (z +9.2) | [[Auranofin (drug)]] 5 µM 0.280× (z -10.0) |
| [[A-172 (line)]] | wt | 23.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.14× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.106× (z -9.6) ⚠ transcription drop |
| [[AsPC-1 (line)]] | alt | 5.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +12.6) | — |
| [[COLO 205 (line)]] | alt | 7.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.41× (z +9.5) | — |
| [[H4 (line)]] | wt | 26.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +12.1) | — |
| [[HOP62 (line)]] | alt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.78× (z +15.8) | — |
| [[hTERT-HPNE (line)]] | wt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.34× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 7.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 22.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 7.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0750× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~68% of this change |
| [[SW 900 (line)]] | alt | 25.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +8.5) | — |
| [[A-427 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5895), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCORL1]] | +0.54 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[SGSM3-AS1]] | +0.50 | +0.60 / +0.36 | both halves | 1e-04 |  |
| [[FAM222A]] | +0.50 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[MEX3B]] | +0.49 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[RAB11FIP4]] | +0.48 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[TENT5C]] | +0.47 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[STARD5]] | +0.47 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[CNNM4]] | +0.47 | +0.36 / +0.56 | both halves | 9e-05 |  |
| [[SCN1B]] | +0.47 | +0.36 / +0.48 | both halves | 9e-05 |  |
| [[BCL2L11]] | +0.47 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[IQCN]] | +0.47 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[VASN]] | +0.46 | +0.52 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSL3]] | -0.43 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[COPS8-DT]] | -0.42 | -0.40 / -0.08 | ⚠ not reproduced | 0.003 |  |
| [[ZCCHC4]] | -0.42 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[POLR1HASP]] | -0.42 | -0.21 / -0.30 | both halves | 7e-04 |  |
| [[RMDN1]] | -0.42 | -0.25 / -0.25 | both halves | 4e-04 |  |
| [[GSTCD]] | -0.41 | -0.20 / -0.30 | both halves | 7e-04 |  |
| [[PRIMPOL]] | -0.41 | -0.25 / -0.35 | both halves | 4e-04 |  |
| [[CUL2]] | -0.41 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[COX10-DT]] | -0.40 | -0.24 / -0.08 | ⚠ not reproduced | 0.004 |  |
| [[SLC35B4]] | -0.39 | -0.34 / -0.25 | both halves | 4e-04 |  |
| [[VPS13B-DT]] | -0.39 | -0.29 / -0.22 | both halves | 6e-04 |  |
| [[BIVM]] | -0.39 | -0.44 / -0.10 | ⚠ not reproduced | 0.003 |  |
| [[DR1]] | -0.39 | -0.29 / -0.30 | both halves | 2e-04 |  |
| [[ATPSCKMT]] | -0.39 | -0.21 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BIVM]] | C | BIVM activity raises HS6ST1's level | lines that do not express BIVM (3) vs lines expressing it (47) | 2.46× lower at baseline in the lines without BIVM | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, RAPGEF4, SYCP2L; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.506). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.5, -30.3); signed map (-0.0, 16.7). **Vector** length 73.6, 13.7% of its response variance represented; |z| ≥ 3 in 1,183 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.9 | +21.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.9 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +6.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.1 | +4.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +1.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.5 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.1 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | heparan sulfate 6-O-sulfotransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.3 — chr2:128,236,716-128,318,868 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HS6ST |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Reactome | 4 pathways, smallest: HS-GAG biosynthesis; Heparan sulfate/heparin (HS-GAG) metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O60243](https://www.uniprot.org/uniprotkb/O60243) (Heparan-sulfate 6-O-sulfotransferase 1):

> 6-O-sulfation enzyme which catalyzes the transfer of sulfate from 3'-phosphoadenosine 5'-phosphosulfate (PAPS) to position 6 of the N-sulfoglucosamine residue (GlcNS) of heparan sulfate. Critical for normal neuronal development where it may play a role in neuron branching. May also play a role in limb development (By similarity). May prefer iduronic acid (By similarity).

**Summary**, from NCBI Gene [9394](https://www.ncbi.nlm.nih.gov/gene/9394):

> The protein encoded by this gene is a member of the heparan sulfate biosynthetic enzyme family. Heparan sulfate biosynthetic enzymes are key components in generating a myriad of distinct heparan sulfate fine structures that carry out multiple biological activities. This enzyme is a type II integral membrane protein and is responsible for 6-O-sulfation of heparan sulfate. This enzyme does not share significant sequence similarity with other known sulfotransferases. A pseudogene located on …

**Accessions** — [HGNC:5201](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5201) · Entrez [9394](https://www.ncbi.nlm.nih.gov/gene/9394) · UniProt [O60243](https://www.uniprot.org/uniprotkb/O60243) · Ensembl [ENSG00000136720](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136720)

## Data

Gene col 5895: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5895); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5895, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5895]; `tensor/DDL_lfc|DDL_z.npy` [5895]; `embed/gene_vectors.npy` [5895]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5895 or target_col == 5895). Every well: [[HS6ST1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HS6ST1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
