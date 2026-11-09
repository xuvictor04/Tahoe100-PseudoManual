---
symbol: "RPL6"
type: "gene"
col: 1559
ensembl_id: "ENSG00000089009"
name: "ribosomal protein L6"
location: "12q24.13"
module: 20
arm: "+"
pooled_cpm: 71.44
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# RPL6

*ribosomal protein L6* — 12q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (14 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.47× (z +9.8, q 9e-20, up in 48 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (AN3 CA 0.180×, C-33 A 0.336×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.312×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS3A]] (+0.89, fdr 7e-06), [[RPSA]] (+0.75, fdr 7e-06), [[SUMO1]] (+0.69, fdr 7e-06); moves opposite to [[NUDT16L1]] (-0.65, fdr 1e-05), [[ERVK3-1]] (-0.61, fdr 7e-06), [[INAFM1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PTGFRN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 15 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1559.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.47×** | +9.8 | 9e-20 | 48/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.39×** | +9.5 | 3e-19 | 44/49 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.47×** | +9.5 | 3e-19 | 33/44 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **4.67×** | +8.8 | 1e-16 | 41/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +8.2 | 3e-14 | 44/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +7.9 | 2e-13 | 38/45 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +5.9 | 3e-07 | 34/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.46×** | +5.2 | 2e-05 | 29/37 (AsPC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.58×** | +5.0 | 4e-05 | 33/48 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.37×** | +4.9 | 7e-05 | 29/49 (NCI-H2347, CFPAC-1, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +4.6 | 2e-04 | 34/48 (HT-29, KATO III, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +4.5 | 3e-04 | 38/48 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +4.5 | 4e-04 | 31/48 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.51×** | +4.3 | 6e-04 | 30/50 (A-172, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.9 | 0.004 | 4/50 (NCI-H1792, LS 180, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.95×** | +3.8 | 0.005 | 32/48 (AsPC-1, A498, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.006 | 30/49 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.015 | 28/48 (SW480, LoVo, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 0.05 µM |  | **1.35×** | +3.3 | 0.024 | 28/48 (SW 900, Panc 03.27, …) | all doses, flat | position effect removed |
| [[Bergenin (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.029 | 24/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.033 | 23/48 (NCI-H460, KATO III, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.039 | 23/48 (SHP-77, SW480, …) | all doses, flat | position effect removed |
| [[OTS514 (drug)]] 5 µM |  | **1.72×** | +3.1 | 0.039 | 19/46 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Lapatinib ditosylate (drug)]] 5 µM |  | **1.69×** | +3.0 | 0.051 | 22/48 (SW480, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.31×** | +2.9 | 0.061 | 22/48 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1559.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (AN3 CA 0.180×, C-33 A 0.336×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.312×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.627× | -3.7 | 0.11 | 33/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 0.5 µM |  | 0.748× | -3.3 | 0.32 | 24/48 (NCI-H23, RKO, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1559. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 97.4 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.43× (z +9.2) | — |
| [[SW480 (line)]] | alt | 86.9 | 4 (2 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 6.89× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 83.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[PANC-1 (line)]] | alt | 77.1 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.55× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 68.6 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.44× (z +9.1) | — |
| [[C-33 A (line)]] | alt | 97.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 57.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.92× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 12.0× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 89.3 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.58× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 77.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A549 (line)]] | wt | 64.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.26× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[AN3 CA (line)]] | alt | 87.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 47.7 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.58× (z +9.0) ⚠ toxic | — |
| [[COLO 205 (line)]] | alt | 44.3 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.21× (z +10.0) ⚠ toxic | — |
| [[HT-29 (line)]] | alt | 56.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[KATO III (line)]] | alt | 53.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 61.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[Panc 03.27 (line)]] | alt | 45.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SHP-77 (line)]] | alt | 130 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.98× (z +9.3) ⚠ toxic | — |
| [[SW 900 (line)]] | alt | 46.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.92× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 76.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 90.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 92.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 113 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 78.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 99.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 106 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 75.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1559), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS3A]] | +0.89 | +0.84 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPSA]] | +0.75 | +0.68 / +0.82 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[SUMO1]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[EEF1A1]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 994 |
| [[RPL10]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL18A]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS7]] | +0.65 | +0.59 / +0.69 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL14]] | +0.65 | +0.69 / +0.60 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[RPIA]] | +0.64 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[RNPS1]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[RPS18]] | +0.63 | +0.65 / +0.63 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[DHX15]] | +0.63 | +0.64 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 466 |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT16L1]] | -0.65 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[ERVK3-1]] | -0.61 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.61 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[PIAS4]] | -0.60 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[EGLN2]] | -0.60 | -0.54 / -0.70 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | -0.59 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[YIF1A]] | -0.58 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[KRTCAP2]] | -0.57 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[TUBB4B]] | -0.57 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[TMEM205]] | -0.57 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[DYNLL1]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[DNAL4]] | -0.55 | -0.45 / -0.62 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTGFRN]] | B | PTGFRN activity lowers RPL6's level | lines that do not express PTGFRN (8) vs lines expressing it (42) | 1.12× higher at baseline in the lines without PTGFRN | 0.076 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.682). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-27.6, -25.5); signed map (-22.2, -35.2). **Vector** length 100, 27.8% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosomal scanning and start codon recognition* (reactome, mean cos +0.66 to 6); *Translation initiation complex formation* (reactome, mean cos +0.66 to 6); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.66 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.4 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +6.6 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +6.0 | +9.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.0 | +4.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +9.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.3 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | +0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -0.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | +0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.4 | +3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | +2.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.5 | -2.9 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -2.4 | -0.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.9 | -2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.9 | -0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.13 — chr12:112,405,189-112,418,838 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAXREB107, L6, eL6; previously TXREB1 |
| Gene groups (HGNC) | L ribosomal proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02878](https://www.uniprot.org/uniprotkb/Q02878) (Large ribosomal subunit protein eL6):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.; (Microbial infection) Specifically binds to domain C of the Tax-responsive enhancer element in the long terminal repeat of HTLV-I.

**Summary**, from NCBI Gene [6128](https://www.ncbi.nlm.nih.gov/gene/6128):

> This gene encodes a protein component of the 60S ribosomal subunit. This protein can bind specifically to domain C of the tax-responsive enhancer element of human T-cell leukemia virus type 1, and may participate in tax-mediated transactivation of transcription. As is typical for genes encoding ribosomal proteins, there are multiple processed pseudogenes of this gene dispersed throughout the genome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:10362](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10362) · Entrez [6128](https://www.ncbi.nlm.nih.gov/gene/6128) · UniProt [Q02878](https://www.uniprot.org/uniprotkb/Q02878) · Ensembl [ENSG00000089009](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089009)

## Data

Gene col 1559: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1559); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1559, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1559]; `tensor/DDL_lfc|DDL_z.npy` [1559]; `embed/gene_vectors.npy` [1559]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1559 or target_col == 1559). Every well: [[RPL6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
