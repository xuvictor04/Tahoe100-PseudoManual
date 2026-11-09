---
symbol: "RPL22"
type: "gene"
col: 3781
ensembl_id: "ENSG00000116251"
name: "ribosomal protein L22"
location: "1p36.31"
module: 43
arm: "+"
pooled_cpm: 56.44
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPL22

*ribosomal protein L22* — 1p36.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.52× (z +15.1, q 0e+00, up in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +5.5, q 4e-06, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.738× (z -5.2, q 1e-04, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (C-33 A 0.324×, SNU-1 0.360×, A-427 0.443×, RKO 0.415×, …); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (CHP-212 0.100×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL21]] (+0.76, fdr 7e-06, ⚠ RPL21 in the vector space only through flagged drug-doses), [[RPL13A]] (+0.75, fdr 7e-06), [[RPL5]] (+0.75, fdr 7e-06), [[RPL14]] (+0.74, fdr 7e-06); moves opposite to [[SLC35A4]] (-0.65, fdr 1e-05), [[TNFRSF12A]] (-0.55, fdr 1e-05), [[MIS12]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3781.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.52×** | +15.1 | 0e+00 | 48/48 (RKO, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +11.9 | 3e-30 | 41/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.55×** | +10.4 | 5e-23 | 43/45 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.59×** | +5.6 | 4e-06 | 32/46 (KATO III, NCI-H460, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.5 | 4e-06 | 30/48 (NCI-H2347, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.3 | 0.002 | 29/47 (COLO 205, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.41×** | +4.2 | 0.003 | 30/47 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.1 | 0.003 | 29/46 (MIA PaCa-2, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.56×** | +3.8 | 0.008 | 30/46 (HOP62, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.53×** | +3.6 | 0.015 | 32/48 (RKO, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.045 | 26/50 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.2 | 0.057 | 21/47 (A-427, AsPC-1, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.063 | 22/48 (KATO III, SW 900, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +3.1 | 0.085 | 19/49 (LS 180, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.20× | +3.1 | 0.085 | 18/48 (LoVo, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3781.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (C-33 A 0.324×, SNU-1 0.360×, A-427 0.443×, RKO 0.415×, …); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (CHP-212 0.100×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.738×** | -5.2 | 1e-04 | 31/48 (C-33 A, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3781. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 26.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +10.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 56.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +11.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 99.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +12.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 52.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 82.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -9.2) |
| [[A-427 (line)]] | wt | 64.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 68.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 64.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +11.2) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 64.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.15× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 49.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 73.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +10.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 47.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +9.3) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 61.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 58.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.74× (z +13.4) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 53.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +12.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 43.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.92× (z +11.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 58.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +11.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 63.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -10.3) |
| [[A-172 (line)]] | wt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 49.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +12.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 51.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 43.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +9.9) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 91.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -12.4) |
| [[C32 (line)]] | wt | 38.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +9.1) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 69.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +9.1) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 42.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.100× (z -9.8) |
| [[COLO 205 (line)]] | alt | 33.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.29× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 52.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 111 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 50.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 48.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.90× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 81.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 40.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +10.6) | — |
| [[SK-MEL-2 (line)]] | alt | 51.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 95.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -12.2) |
| [[SNU-423 (line)]] | alt | 58.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 31.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 39.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +11.0) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 67.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3781), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 17 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL21]] ⚠ | +0.76 | +0.73 / +0.73 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL13A]] | +0.75 | +0.78 / +0.72 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL5]] | +0.75 | +0.78 / +0.74 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL14]] | +0.74 | +0.65 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[RPL23A]] | +0.74 | +0.75 / +0.67 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS15A]] | +0.74 | +0.75 / +0.71 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 995 |
| [[RPS4X]] | +0.72 | +0.69 / +0.73 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 997 |
| [[RPL30]] ⚠ | +0.71 | +0.62 / +0.72 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[EEF1G]] | +0.70 | +0.68 / +0.70 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 607 |
| [[EEF1B2]] | +0.70 | +0.59 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 838 |
| [[RPS6]] ⚠ | +0.70 | +0.69 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL37]] ⚠ | +0.69 | +0.67 / +0.68 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 998; ⚠ in the vector space only through flagged drug-doses |
| [[RPL7]] | +0.69 | +0.72 / +0.66 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS20]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS24]] | +0.69 | +0.69 / +0.66 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL27A]] | +0.68 | +0.66 / +0.68 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A4]] | -0.65 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | -0.55 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[MIS12]] | -0.54 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[ZNF724]] | -0.53 | -0.52 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.692). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.2, -30.1); signed map (-60.7, -6.9). **Vector** length 71.2, 19.5% of its response variance represented; |z| ≥ 3 in 614 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.60 to 19); *Translation initiation complex formation* (reactome, mean cos +0.60 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.60 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.2 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +0.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.1 | -0.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +0.2 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.0 | +0.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | +0.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.5 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | +0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | +0.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.8 | +2.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.31 — chr1:6,185,020-6,209,389 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EAP, L22, eL22 |
| Gene groups (HGNC) | L ribosomal proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P35268](https://www.uniprot.org/uniprotkb/P35268) (Large ribosomal subunit protein eL22):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6146](https://www.ncbi.nlm.nih.gov/gene/6146):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a cytoplasmic ribosomal protein that is a component of the 60S subunit. The protein belongs to the L22E family of ribosomal proteins. Its initiating methionine residue is post-translationally removed. The protein can bind specifically to Epstein-Barr …

**Accessions** — [HGNC:10315](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10315) · Entrez [6146](https://www.ncbi.nlm.nih.gov/gene/6146) · UniProt [P35268](https://www.uniprot.org/uniprotkb/P35268) · Ensembl [ENSG00000116251](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116251)

## Data

Gene col 3781: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3781); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3781, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3781]; `tensor/DDL_lfc|DDL_z.npy` [3781]; `embed/gene_vectors.npy` [3781]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3781 or target_col == 3781). Every well: [[RPL22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
