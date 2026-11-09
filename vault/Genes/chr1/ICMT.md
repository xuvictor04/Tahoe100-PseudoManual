---
symbol: "ICMT"
type: "gene"
col: 3780
ensembl_id: "ENSG00000116237"
name: "isoprenylcysteine carboxyl methyltransferase"
location: "1p36.31"
module: 20
arm: "+"
pooled_cpm: 17.62
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# ICMT

*isoprenylcysteine carboxyl methyltransferase* — 1p36.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.76× (z +18.8, q 0e+00, up in 38 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.57× (z +6.2, q 4e-08, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.772× (z -5.2, q 1e-04, down in 27 of 48 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 0.691× (z -4.9, q 2e-04, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFDP1]] (+0.80, fdr 7e-06), [[SIGMAR1]] (+0.80, fdr 7e-06), [[TMEM109]] (+0.77, fdr 7e-06); moves opposite to [[TERF2IP]] (-0.72, fdr 7e-06), [[SPATC1]] (-0.69, fdr 1e-05), [[ZMYM5]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MCM3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3780.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.76×** | +18.8 | 0e+00 | 38/39 (Hs 766T, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.97×** | +14.8 | 0e+00 | 28/28 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.77×** | +14.4 | 7e-45 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.38×** | +12.3 | 2e-32 | 42/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.24×** | +11.4 | 4e-28 | 43/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.37×** | +11.3 | 1e-27 | 30/37 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.60×** | +6.7 | 2e-09 | 28/48 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **1.59×** | +6.3 | 2e-08 | 27/44 (SW480, PANC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.57×** | +6.2 | 4e-08 | 27/48 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +5.6 | 1e-06 | 23/44 (AsPC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.48×** | +5.4 | 4e-06 | 21/44 (A549, SNU-423, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +4.9 | 5e-05 | 24/47 (HepG2/C3A, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +4.7 | 1e-04 | 18/47 (A498, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.39×** | +4.6 | 1e-04 | 19/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.34×** | +4.2 | 0.001 | 20/45 (A498, NCI-H460, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.59×** | +3.5 | 0.019 | 11/45 (NCI-H2347, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.028 | 5/48 (A-427, KATO III, …) | inconsistent across doses | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.23×** | +2.9 | 0.077 | 5/48 (A498, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +2.9 | 0.077 | 8/48 (SW 900, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Berbamine (drug)]] 0.05 µM |  | **1.23×** | +2.9 | 0.079 | 7/48 (C32, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3780.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.772×** | -5.2 | 1e-04 | 27/48 (Hs 766T, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.691×** | -4.9 | 2e-04 | 21/47 (PANC-1, SW 1088, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.791×** | -4.7 | 6e-04 | 22/46 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.732×** | -4.4 | 0.002 | 19/47 (LS 180, KATO III, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.725×** | -4.4 | 0.002 | 20/47 (HepG2/C3A, Hs 766T, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.602×** | -3.7 | 0.017 | 17/47 (LoVo, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | 0.733× | -3.1 | 0.15 | 9/48 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.797× | -3.0 | 0.18 | 7/48 (KATO III, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.72 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3780. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 13.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.86× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[Hs 766T (line)]] | wt | 15.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 7.87× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[AZD2858 (drug)]] 0.5 µM 0.0996× (z -9.3) ⚠ toxic |
| [[HS-578T (line)]] | alt | 27.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.72× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[LoVo (line)]] | wt | 19.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Digitoxin (drug)]] 5 µM 0.230× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.452× (z -8.9) |
| [[PANC-1 (line)]] | alt | 18.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.54× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW480 (line)]] | alt | 17.6 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.77× (z +10.3) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[A498 (line)]] | wt | 16.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[C32 (line)]] | wt | 17.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -9.3) ⚠ cell-cycle shift, explains ~49% of this change |
| [[HT-29 (line)]] | alt | 19.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.89× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 16.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.64× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H1573 (line)]] | alt | 17.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.257× (z -8.9) ⚠ cell-cycle shift, explains ~49% of this change |
| [[NCI-H1792 (line)]] | alt | 6.48 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 12.7× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Alpelisib (drug)]] 0.05 µM 0.0497× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 18.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-427 (line)]] | wt | 31.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.306× (z -9.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A549 (line)]] | wt | 10.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.26× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[AsPC-1 (line)]] | alt | 6.75 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0851× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 13.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.76× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HEC-1-A (line)]] | alt | 29.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HepG2_C3A (line)]] | wt | 24.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 16.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.43× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.60× (z +8.8) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H2030 (line)]] | alt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -9.8) |
| [[SNU-423 (line)]] | alt | 8.72 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.40× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-172 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3780), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFDP1]] | +0.80 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[SIGMAR1]] | +0.80 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[TMEM109]] | +0.77 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[PRKDC]] | +0.74 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[MTHFD1]] | +0.73 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[TUBG1]] | +0.72 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[VMA21]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[ANKRD52]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[SSX2IP]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[CS]] | +0.68 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[CDCA7]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[PRPS1]] | +0.68 | +0.58 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERF2IP]] | -0.72 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[SPATC1]] | -0.69 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.69 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[NOXRED1]] | -0.68 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[TRNAU1AP]] | -0.66 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[TTC36-AS1]] | -0.66 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[ZNF791]] | -0.65 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[CCDC174]] | -0.64 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[SYF2]] | -0.64 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[SNHG32]] | -0.64 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[WASHC1]] | -0.64 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[EIF3J-DT]] | -0.64 | -0.58 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCM3]] | C | MCM3 activity raises ICMT's level | lines that do not express MCM3 (3) vs lines expressing it (47) | 1.80× lower at baseline in the lines without MCM3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.627). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.2, -33.1); signed map (-28.2, -42.9). **Vector** length 96.6, 23.0% of its response variance represented; |z| ≥ 3 in 967 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +4.8 | +18.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +4.7 | +14.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | +4.4 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +3.9 | +11.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +3.4 | +11.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +6.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.4 | +2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +4.7 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +1.8 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.2 | -2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.8 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -4.6 | -2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.1 | -4.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.5 | -5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.1 | -1.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.1 | -1.2 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -2.0 | -2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | isoprenylcysteine carboxyl methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.31 — chr1:6,221,193-6,235,972 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PCCMT, HSTE14, PPMT |
| Gene groups (HGNC) | Membrane-bound methyltransferase family; N- and C-terminal methyltransferases |
| Reactome | 5 pathways, smallest: RAS processing; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation; RAF/MAP kinase cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [O60725](https://www.uniprot.org/uniprotkb/O60725) (Protein-S-isoprenylcysteine O-methyltransferase):

> Catalyzes the post-translational methylation of isoprenylated C-terminal cysteine residues.

**Summary**, from NCBI Gene [23463](https://www.ncbi.nlm.nih.gov/gene/23463):

> This gene encodes the third of three enzymes that posttranslationally modify isoprenylated C-terminal cysteine residues in certain proteins and target those proteins to the cell membrane. This enzyme localizes to the endoplasmic reticulum. Alternative splicing may result in other transcript variants, but the biological validity of those transcripts has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5350](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5350) · Entrez [23463](https://www.ncbi.nlm.nih.gov/gene/23463) · UniProt [O60725](https://www.uniprot.org/uniprotkb/O60725) · Ensembl [ENSG00000116237](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116237)

## Data

Gene col 3780: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3780); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3780, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3780]; `tensor/DDL_lfc|DDL_z.npy` [3780]; `embed/gene_vectors.npy` [3780]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3780 or target_col == 3780). Every well: [[ICMT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ICMT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
