---
symbol: "TEAD4"
type: "gene"
col: 12486
ensembl_id: "ENSG00000197905"
name: "TEA domain transcription factor 4"
location: "12p13.33"
module: 5
arm: "+"
pooled_cpm: 46.71
n_lines_expressing: 47
n_dd_up: 8
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TEAD4

*TEA domain transcription factor 4* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.61× (z +9.1, q 3e-17, up in 30 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +8.4, q 1e-14, up in 27 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.549× (z -16.2, q 0e+00, down in 41 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOP2]] (+0.64, fdr 7e-06), [[PPRC1]] (+0.64, fdr 7e-06), [[UTP4]] (+0.63, fdr 7e-06); moves opposite to [[NDUFA5]] (-0.56, fdr 3e-05), [[PREPL]] (-0.56, fdr 1e-05), [[FPGT]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TRABD2B]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RIMKLB]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12486.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.61×** | +9.1 | 3e-17 | 30/45 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +8.4 | 1e-14 | 27/44 (NCI-H1573, LoVo, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +4.9 | 2e-04 | 21/45 (SW 900, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.27×** | +4.4 | 0.001 | 15/45 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.26×** | +4.4 | 0.001 | 20/45 (A-427, HCT15, …) | two highest doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.004 | 13/45 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.012 | 19/45 (SNU-1, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.20×** | +3.6 | 0.027 | 13/45 (NCI-H1573, SW 900, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.075 | 15/44 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.083 | 10/45 (A549, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.12 | 18/45 (SNU-1, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12486.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.549×** | -16.2 | 0e+00 | 41/45 (RKO, C32, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.582×** | -10.3 | 1e-22 | 39/45 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.702×** | -9.5 | 3e-19 | 35/45 (C32, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.653×** | -8.1 | 6e-14 | 33/45 (C32, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.745×** | -7.9 | 2e-13 | 31/45 (C32, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.667×** | -7.7 | 9e-13 | 30/45 (RKO, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.661×** | -7.6 | 2e-12 | 28/45 (LoVo, SW48, …) | top dose only | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.666×** | -7.2 | 5e-11 | 29/42 (SW48, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.521×** | -6.5 | 4e-09 | 27/44 (A-427, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | **0.524×** | -6.5 | 6e-09 | 28/44 (H4, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.715×** | -6.4 | 8e-09 | 31/45 (RKO, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.729×** | -6.0 | 8e-08 | 25/43 (C-33 A, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.556×** | -5.9 | 2e-07 | 26/44 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.740×** | -5.7 | 4e-07 | 26/45 (SK-MEL-2, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.742×** | -5.5 | 2e-06 | 23/40 (C-33 A, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Saquinavir (drug)]] 5 µM |  | **0.823×** | -5.2 | 6e-06 | 19/45 (MIA PaCa-2, A549, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.786×** | -4.6 | 1e-04 | 24/45 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.637×** | -4.5 | 2e-04 | 23/45 (RKO, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12486. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 91.3 | 0 | 9 (3 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.395× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 95.4 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.448× (z -11.9) |
| [[RKO (line)]] | wt | 98.4 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.341× (z -16.1) |
| [[C-33 A (line)]] | alt | 103 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -19.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 54.2 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +8.8) | [[Harringtonine (drug)]] 5 µM 0.351× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 27.6 | 3 (2 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.15× (z +9.5) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.7) | [[Selinexor (drug)]] 5 µM 0.474× (z -8.8) |
| [[SW48 (line)]] | wt | 50.5 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -13.9) ⚠ cell-cycle shift, explains ~85% of this change |
| [[BT-474 (line)]] | alt | 44.2 | 0 | 3 (3 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.223× (z -10.0) ⚠ toxic |
| [[C32 (line)]] | wt | 63.9 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.336× (z -13.7) |
| [[MIA PaCa-2 (line)]] | alt | 90.8 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.410× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 132 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.334× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.563× (z -9.4) |
| [[SNU-1 (line)]] | wt | 93.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.80× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.191× (z -12.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 185 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.533× (z -9.4) |
| [[H4 (line)]] | wt | 32.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.170× (z -9.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 59.0 | 0 | 2 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.220× (z -11.7) |
| [[J82 (line)]] | alt | 54.6 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.480× (z -10.4) |
| [[A549 (line)]] | wt | 35.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -15.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HEC-1-A (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.139× (z -9.2) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 16.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 34.8 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.412× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 44.8 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.542× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 50.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -18.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 47.1 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.459× (z -9.6) |
| [[A-172 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12486), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOP2]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[PPRC1]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[UTP4]] | +0.63 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[SLFNL1-AS1]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[NOP16]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ADCY3]] | +0.59 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SCLY]] | +0.59 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[KCNJ14]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[PUS1]] | +0.59 | +0.57 / +0.58 | both halves | 8e-06 |  |
| [[ZNF276]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[MYO19]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SLC7A6]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA5]] | -0.56 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[PREPL]] | -0.56 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[FPGT]] | -0.54 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[CLCN3]] | -0.54 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[DYNC2LI1]] | -0.53 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[PEX2]] | -0.52 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[VAMP7]] | -0.51 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[CISD2]] | -0.50 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[MAGED2]] | -0.50 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[LINC00888]] | -0.50 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[ATP6V1A]] | -0.49 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[CAT]] | -0.49 | -0.49 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRABD2B]] | B | TRABD2B activity raises TEAD4's level | lines that do not express TRABD2B (19) vs lines expressing it (31) | 1.42× lower at baseline in the lines without TRABD2B | 0.082 | ⚠ within organs, on part of the lines; also absent: FAM110B, ULK2, COL4A4 |
| [[C16orf74]] | B | C16orf74 activity raises TEAD4's level | lines that do not express C16orf74 (11) vs lines expressing it (39) | 1.84× lower at baseline in the lines without C16orf74 | 0.082 | ⚠ within organs, on part of the lines; also absent: EPHA2, ABLIM2, FAM83H; maybe low, not absent |
| [[RIMKLB]] | B | RIMKLB activity raises TEAD4's level | lines that do not express RIMKLB (13) vs lines expressing it (37) | 1.10× lower at baseline in the lines without RIMKLB | 0.0997 | ⚠ within organs, on part of the lines; also absent: DNAAF9, GJC1, ANKRD6 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIMKLB]] | C | TEAD4 activity raises RIMKLB's level | lines that do not express TEAD4 (3) vs lines expressing it (47) | 2.39× lower at baseline in the lines without TEAD4 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MMP25, MPP4, CDHR3; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.601). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.2, -37.0); signed map (2.0, -50.4). **Vector** length 125, 33.8% of its response variance represented; |z| ≥ 3 in 1,175 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +8.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +9.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +5.0 | +4.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.8 | +4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.6 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.1 | +2.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +3.0 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -10.4 | -16.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -7.1 | -7.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.2 | -10.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.1 | -6.4 |
|  | [[NG25 (drug)]] 5 µM |  | -3.9 | -5.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.8 | -9.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.8 | -6.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.7 | -8.1 |

## What is on record

|  |  |
|---|---|
| Name | TEA domain transcription factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:2,959,330-3,040,676 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TEF-3, TEFR-1, EFTR-2, RTEF-1; previously TCF13L1 |
| Gene groups (HGNC) | TEA domain transcription factors |
| Hallmark sets | MYOGENESIS |
| Reactome | 12 pathways, smallest: RUNX3 regulates YAP1-mediated transcription; Zygotic genome activation (ZGA); Formation of axial mesoderm |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15561](https://www.uniprot.org/uniprotkb/Q15561) (Transcriptional enhancer factor TEF-3):

> Transcription factor which plays a key role in the Hippo signaling pathway, a pathway involved in organ size control and tumor suppression by restricting proliferation and promoting apoptosis. The core of this pathway is composed of a kinase cascade wherein MST1/MST2, in complex with its regulatory protein SAV1, phosphorylates and activates LATS1/2 in complex with its regulatory protein MOB1, which in turn phosphorylates and inactivates YAP1 oncoprotein and WWTR1/TAZ. Acts by mediating gene …

**Summary**, from NCBI Gene [7004](https://www.ncbi.nlm.nih.gov/gene/7004):

> This gene product is a member of the transcriptional enhancer factor (TEF) family of transcription factors, which contain the TEA/ATTS DNA-binding domain. It is preferentially expressed in the skeletal muscle, and binds to the M-CAT regulatory element found in promoters of muscle-specific genes to direct their gene expression. Alternatively spliced transcripts encoding distinct isoforms, some of which are translated through the use of a non-AUG (UUG) initiation codon, have been described for …

**Accessions** — [HGNC:11717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11717) · Entrez [7004](https://www.ncbi.nlm.nih.gov/gene/7004) · UniProt [Q15561](https://www.uniprot.org/uniprotkb/Q15561) · Ensembl [ENSG00000197905](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197905)

## Data

Gene col 12486: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12486); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12486, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12486]; `tensor/DDL_lfc|DDL_z.npy` [12486]; `embed/gene_vectors.npy` [12486]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12486 or target_col == 12486). Every well: [[TEAD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEAD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
