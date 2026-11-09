---
symbol: "EIF2S1"
type: "gene"
col: 5495
ensembl_id: "ENSG00000134001"
name: "eukaryotic translation initiation factor 2 subunit alpha"
location: "14q23.3"
module: 4
arm: "+"
pooled_cpm: 65.23
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# EIF2S1

*eukaryotic translation initiation factor 2 subunit alpha* — 14q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (21 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 8.90× (z +23.0, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Binimetinib (drug)]] 5 µM: 0.845× (z -3.7, q 0.041, down in 17 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Omeprazole (drug)]] 0.5 µM in 1 line (SW 1271 0.0565×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.540×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FARSB]] (+0.78, fdr 7e-06), [[NUP155]] (+0.77, fdr 7e-06), [[POLR1A]] (+0.76, fdr 7e-06); moves opposite to [[SAT2]] (-0.71, fdr 7e-06), [[GABARAPL2]] (-0.71, fdr 7e-06), [[VPS37D]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 23 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5495.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **8.90×** | +23.0 | 0e+00 | 49/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.31×** | +16.8 | 0e+00 | 47/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **4.67×** | +16.2 | 0e+00 | 46/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.20×** | +15.8 | 0e+00 | 47/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.06×** | +14.5 | 1e-45 | 46/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.93×** | +12.7 | 6e-35 | 38/44 (KATO III, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.85×** | +12.4 | 2e-33 | 37/49 (SNU-423, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.83×** | +12.1 | 7e-32 | 43/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.75×** | +11.2 | 2e-27 | 45/48 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +10.1 | 3e-22 | 36/48 (CFPAC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +9.1 | 7e-18 | 36/48 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.29×** | +7.3 | 1e-11 | 25/48 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.45×** | +6.9 | 3e-10 | 29/45 (SW480, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **1.40×** | +6.5 | 3e-09 | 29/47 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.5 | 3e-09 | 31/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +5.7 | 4e-07 | 31/48 (SW480, HOP62, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +5.4 | 2e-06 | 30/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +4.6 | 1e-04 | 26/48 (SNU-423, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.54×** | +4.6 | 1e-04 | 29/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.48×** | +4.1 | 7e-04 | 24/48 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.48×** | +4.1 | 8e-04 | 22/48 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.002 | 21/48 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.007 | 19/47 (NCI-H1573, SNU-423, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.20×** | +3.5 | 0.007 | 21/47 (SW48, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5495.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Omeprazole (drug)]] 0.5 µM in 1 line (SW 1271 0.0565×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.540×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Binimetinib (drug)]] 5 µM |  | 0.845× | -3.7 | 0.041 | 17/49 (HCT15, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.833× | -3.7 | 0.041 | 17/48 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.835× | -3.7 | 0.041 | 17/48 (A-172, RKO, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.740×** | -3.6 | 0.041 | 22/48 (LoVo, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.841× | -3.5 | 0.048 | 19/48 (HOP62, COLO 205, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.851× | -3.3 | 0.098 | 17/48 (KATO III, NCI-H2030, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.766× | -3.2 | 0.11 | 10/48 (COLO 205, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.859× | -3.1 | 0.14 | 12/48 (SW 1271, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5495. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 57.0 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.53× (z +11.8) | — |
| [[SNU-423 (line)]] | alt | 44.6 | 10 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.61× (z +10.5) | — |
| [[SW480 (line)]] | alt | 93.5 | 10 (7 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 12.4× (z +17.7) | — |
| [[CFPAC-1 (line)]] | alt | 52.8 | 8 (6 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.8× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 55.4 | 8 (5 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 12.4× (z +13.3) | — |
| [[NCI-H460 (line)]] | wt | 56.6 | 8 (6 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.58× (z +14.3) | — |
| [[A549 (line)]] | wt | 66.0 | 7 (5 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.80× (z +13.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 70.5 | 7 (5 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 16.4× (z +14.7) | — |
| [[LoVo (line)]] | wt | 62.5 | 6 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 17.6× (z +16.9) | — |
| [[KATO III (line)]] | alt | 65.7 | 5 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 14.1× (z +14.4) | — |
| [[LOX-IMVI (line)]] | wt | 59.2 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.46× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.63× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 49.2 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.6× (z +13.1) | — |
| [[Hs 766T (line)]] | wt | 42.7 | 4 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 13.7× (z +11.8) | — |
| [[NCI-H2347 (line)]] | alt | 50.0 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.50× (z +9.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.57× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 58.2 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 9.84× (z +16.3) | — |
| [[RPMI-7951 (line)]] | alt | 69.2 | 4 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.32× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 53.2 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.61× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 65.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 10.7× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 45.1 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.66× (z +9.2) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.42× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 142 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 8.26× (z +12.7) | — |
| [[Panc 03.27 (line)]] | alt | 84.1 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.5× (z +13.7) | — |
| [[A-172 (line)]] | wt | 39.8 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.16× (z +9.5) | — |
| [[A-427 (line)]] | wt | 73.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.75× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 76.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.20× (z +9.7) | — |
| [[COLO 205 (line)]] | alt | 48.3 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 35.6× (z +13.5) | — |
| [[HEC-1-A (line)]] | alt | 62.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.96× (z +13.9) | — |
| [[LS 180 (line)]] | wt | 51.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 18.8× (z +14.5) | — |
| [[NCI-H2030 (line)]] | alt | 111 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.89× (z +12.4) | — |
| [[RKO (line)]] | wt | 105 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.28× (z +11.8) | — |
| [[SW1417 (line)]] | alt | 61.5 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.56× (z +12.1) | — |
| [[A498 (line)]] | wt | 48.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.36× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[AsPC-1 (line)]] | alt | 46.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.67× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 74.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.3× (z +10.2) | — |
| [[H4 (line)]] | wt | 49.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.3× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 36.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.91× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 46.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.25× (z +8.7) | — |
| [[J82 (line)]] | alt | 89.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.51× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 116 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.78× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 75.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | — |
| [[SW 1271 (line)]] | alt | 61.9 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0565× (z -10.1) |
| [[AN3 CA (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 70.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 77.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5495), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FARSB]] | +0.78 | +0.74 / +0.81 | both halves | 7e-06 | STRING 711 |
| [[NUP155]] | +0.77 | +0.74 / +0.77 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[POLR1A]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 | STRING 436 |
| [[EFTUD2]] | +0.75 | +0.66 / +0.77 | both halves | 7e-06 | STRING 484 |
| [[EIF4G1]] | +0.75 | +0.72 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 986 |
| [[ABCF2]] | +0.75 | +0.72 / +0.77 | both halves | 7e-06 | STRING 479 |
| [[XRCC5]] | +0.73 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[LAS1L]] | +0.72 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[PSME3]] | +0.71 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[RUVBL1]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 | STRING 486 |
| [[PRKDC]] | +0.71 | +0.67 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[NCBP1]] | +0.70 | +0.65 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAT2]] | -0.71 | -0.68 / -0.68 | both halves | 7e-06 |  |
| [[GABARAPL2]] | -0.71 | -0.60 / -0.80 | both halves | 7e-06 | STRING 421 |
| [[VPS37D]] | -0.69 | -0.60 / -0.78 | both halves | 7e-06 |  |
| [[TESK2]] | -0.67 | -0.61 / -0.66 | both halves | 7e-06 |  |
| [[ZFAND2B]] | -0.66 | -0.57 / -0.70 | both halves | 1e-05 |  |
| [[VAMP2]] | -0.66 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[PNISR]] | -0.65 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[SNHG9]] | -0.65 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[HOTAIRM1]] | -0.65 | -0.51 / -0.70 | both halves | 1e-05 |  |
| [[STARD10]] | -0.64 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | -0.64 | -0.52 / -0.72 | both halves | 1e-05 |  |
| [[SIRT2]] | -0.64 | -0.64 / -0.66 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EIF2S1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.735). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-19.8, -33.2); signed map (-7.9, -44.8). **Vector** length 114, 36.7% of its response variance represented; |z| ≥ 3 in 1,355 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.60 to 4); *Prefoldin mediated transfer of substrate  to CCT/TriC* (reactome, mean cos +0.52 to 5); *Cooperation of Prefoldin and TriC/CCT  in actin and tubulin folding* (reactome, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.5 | +23.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +8.8 | +16.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.6 | +11.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.4 | +12.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.9 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.7 | +4.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.6 | -3.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -3.9 | -3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.4 | -2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 2 subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.3 — chr14:67,360,328-67,386,516 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EIF-2alpha, EIF2A; previously EIF2 |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 24 pathways, smallest: Recycling of eIF2:GDP; Cellular response to mitochondrial stress; Response of EIF2AK1 (HRI) to heme deficiency |
| Matched by | ensembl_id |

**Function**, from UniProt [P05198](https://www.uniprot.org/uniprotkb/P05198) (Eukaryotic translation initiation factor 2 subunit 1):

> Member of the eIF2 complex that functions in the early steps of protein synthesis by forming a ternary complex with GTP and initiator tRNA. This complex binds to a 40S ribosomal subunit, followed by mRNA binding to form a 43S pre-initiation complex (43S PIC). Junction of the 60S ribosomal subunit to form the 80S initiation complex is preceded by hydrolysis of the GTP bound to eIF2 and release of an eIF2-GDP binary complex. In order for eIF2 to recycle and catalyze another round of initiation, …

**Summary**, from NCBI Gene [1965](https://www.ncbi.nlm.nih.gov/gene/1965):

> The translation initiation factor EIF2 catalyzes the first regulated step of protein synthesis initiation, promoting the binding of the initiator tRNA to 40S ribosomal subunits. Binding occurs as a ternary complex of methionyl-tRNA, EIF2, and GTP. EIF2 is composed of 3 nonidentical subunits, the 36-kD EIF2-alpha subunit (EIF2S1), the 38-kD EIF2-beta subunit (EIF2S2; MIM 603908), and the 52-kD EIF2-gamma subunit (EIF2S3; MIM 300161). The rate of formation of the ternary complex is modulated by …

**Accessions** — [HGNC:3265](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3265) · Entrez [1965](https://www.ncbi.nlm.nih.gov/gene/1965) · UniProt [P05198](https://www.uniprot.org/uniprotkb/P05198) · Ensembl [ENSG00000134001](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134001)

## Data

Gene col 5495: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5495); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5495, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5495]; `tensor/DDL_lfc|DDL_z.npy` [5495]; `embed/gene_vectors.npy` [5495]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5495 or target_col == 5495). Every well: [[EIF2S1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF2S1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
