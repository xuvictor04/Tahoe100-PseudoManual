---
symbol: "TMEM237"
type: "gene"
col: 7915
ensembl_id: "ENSG00000155755"
name: "transmembrane protein 237"
location: "2q33.1"
module: 25
arm: "+"
pooled_cpm: 16.29
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# TMEM237

*transmembrane protein 237* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.46× (z +23.8, q 0e+00, up in 25 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.25× (z +6.3, q 3e-08, up in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A-172 5.50×, SW480 3.54×, A498 3.52×, PANC-1 3.40×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-172 8.33×, PANC-1 3.44×, A498 3.24×, NCI-H460 3.19×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-172 6.94×, PANC-1 3.09×, SW480 2.82×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.755× (z -5.3, q 6e-05, down in 17 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHFR]] (+0.70, fdr 2e-05), [[SRP9]] (+0.69, fdr 1e-05), [[MANEA]] (+0.69, fdr 1e-05); moves opposite to [[TRAPPC2B]] (-0.63, fdr 3e-05), [[RPL36AL]] (-0.62, fdr 2e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[RPL18]] (-0.60, fdr 1e-05, ⚠ RPL18 in the vector space only through flagged drug-doses), [[MRPL36]] (-0.60, fdr 5e-05), [[LINC00685]] (-0.58, fdr 1e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TUBA4A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7915.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A-172 5.50×, SW480 3.54×, A498 3.52×, PANC-1 3.40×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-172 8.33×, PANC-1 3.44×, A498 3.24×, NCI-H460 3.19×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-172 6.94×, PANC-1 3.09×, SW480 2.82×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.46×** | +23.8 | 0e+00 | 25/28 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.24×** | +23.5 | 0e+00 | 36/39 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +14.9 | 0e+00 | 24/32 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +6.3 | 3e-08 | 18/48 (RKO, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.37×** | +6.0 | 2e-07 | 16/42 (SW480, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.35×** | +6.0 | 2e-07 | 21/48 (A498, HEC-1-A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.22×** | +5.5 | 3e-06 | 18/47 (A-172, A498, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +5.4 | 5e-06 | 12/44 (HOP62, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.28×** | +5.0 | 4e-05 | 17/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +4.9 | 5e-05 | 15/48 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.26×** | +4.6 | 2e-04 | 9/47 (A498, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.22×** | +3.9 | 0.005 | 16/48 (A-172, A498, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 1.20× | +3.5 | 0.022 | 15/48 (A-172, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.13× | +3.3 | 0.034 | 15/47 (RPMI-7951, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.3 | 0.039 | 5/24 (A-172, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.044 | 4/48 (J82, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7915.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.755×** | -5.3 | 6e-05 | 17/48 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.817×** | -4.0 | 0.015 | 14/48 (KATO III, SW480, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -3.5 | 0.087 | 15/47 (NCI-H460, SW480, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.721×** | -3.4 | 0.088 | 13/46 (C32, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.855× | -3.1 | 0.15 | 10/47 (SW48, HT-29, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.848× | -3.1 | 0.15 | 9/47 (SW48, RKO, …) | inconsistent across doses |  |
| [[Ranolazine (drug)]] 0.05 µM |  | 0.856× | -3.1 | 0.15 | 4/47 (LoVo, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7915. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 21.3 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.33× (z +16.3) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.46× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.181× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 17.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +12.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 18.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +12.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 24.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.52× (z +12.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 12.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +10.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 15.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.18× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 33.7 | 0 | 2 | — | [[Alpelisib (drug)]] 5 µM 0.0708× (z -9.9) |
| [[A-427 (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 13.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.75× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 13.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.90× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 9.38 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.103× (z -9.1) ⚠ toxic; unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0986× (z -9.7) |
| [[J82 (line)]] | alt | 26.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 11.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 12.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.30× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 21.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 65.8 | 0 | 1 | — | [[Capmatinib (drug)]] 0.05 µM 0.0510× (z -12.4) |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0886× (z -10.4) ⚠ toxic |
| [[SW48 (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -9.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[AN3 CA (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7915), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHFR]] | +0.70 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[SRP9]] | +0.69 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[MANEA]] | +0.69 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[ALG10B]] | +0.67 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[TIMELESS]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[GPD2]] | +0.66 | +0.57 / +0.62 | both halves | 8e-06 |  |
| [[LANCL1]] | +0.66 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[ZWILCH]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[SCCPDH]] | +0.64 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ALG10]] | +0.64 | +0.57 / +0.60 | both halves | 8e-06 |  |
| [[POGLUT3]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[OXCT1]] | +0.63 | +0.53 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC2B]] | -0.63 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[RPL36AL]] ⚠ | -0.62 | -0.47 / -0.62 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL18]] ⚠ | -0.60 | -0.51 / -0.63 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL36]] | -0.60 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[NACA4P]] ⚠ | -0.59 | -0.43 / -0.61 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LINC00685]] | -0.58 | -0.35 / -0.62 | both halves | 1e-04 |  |
| [[IGBP1]] | -0.58 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[ZBTB7A]] | -0.57 | -0.37 / -0.64 | both halves | 8e-05 |  |
| [[MILIP]] | -0.57 | -0.21 / -0.60 | both halves | 7e-04 |  |
| [[EXOSC4]] | -0.56 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[ZNF765]] | -0.56 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[EMC6]] | -0.56 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[UXT]] | -0.55 | -0.39 / -0.62 | both halves | 5e-05 |  |
| [[TM2D2]] | -0.55 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[ZNF593]] | -0.54 | -0.30 / -0.54 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TUBA4A]] | B | TUBA4A activity lowers TMEM237's level | lines that do not express TUBA4A (13) vs lines expressing it (37) | 1.41× higher at baseline in the lines without TUBA4A | 0.027 | ⚠ within organs, on part of the lines; also absent: TNK1, ETV7, CDCP1; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises TMEM237's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.6, -18.5); signed map (-16.8, -39.7). **Vector** length 79.7, 14.3% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.3 | +23.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +23.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +14.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | +2.9 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.7 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.3 | +2.0 |
|  | [[Asciminib (drug)]] 0.05 µM |  | +1.3 | +1.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.3 | +2.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -4.0 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -4.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.1 | -1.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -2.9 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 237 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:201,620,184-201,643,570 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JBTS14; previously ALS2CR4 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96Q45](https://www.uniprot.org/uniprotkb/Q96Q45) (Transmembrane protein 237):

> Component of the transition zone in primary cilia. Required for ciliogenesis.

**Summary**, from NCBI Gene [65062](https://www.ncbi.nlm.nih.gov/gene/65062):

> The protein encoded by this gene is a tetraspanin protein that is thought to be involved in WNT signaling. Defects in this gene are a cause of Joubert syndrome-14. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:14432](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14432) · Entrez [65062](https://www.ncbi.nlm.nih.gov/gene/65062) · UniProt [Q96Q45](https://www.uniprot.org/uniprotkb/Q96Q45) · Ensembl [ENSG00000155755](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155755)

## Data

Gene col 7915: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7915); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7915, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7915]; `tensor/DDL_lfc|DDL_z.npy` [7915]; `embed/gene_vectors.npy` [7915]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7915 or target_col == 7915). Every well: [[TMEM237 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM237.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
