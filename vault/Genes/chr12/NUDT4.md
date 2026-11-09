---
symbol: "NUDT4"
type: "gene"
col: 10407
ensembl_id: "ENSG00000173598"
name: "nudix hydrolase 4"
location: "12q22"
module: 29
arm: "-"
pooled_cpm: 74.33
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 17
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# NUDT4

*nudix hydrolase 4* — 12q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.81× (z +14.3, q 2e-43, up in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.46× (z +6.4, q 2e-08, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Anethole trithione (drug)]] 0.5 µM: 0.777× (z -4.3, q 0.008, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (C-33 A 0.118×, LoVo 0.349×, NCI-H23 0.262×, AsPC-1 0.440×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (LS 180 0.294×, SW480 0.369×, KATO III 0.443×, AsPC-1 0.454×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 0.329×, LoVo 0.540×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIME1]] (+0.61, fdr 1e-05), [[XYLT1]] (+0.58, fdr 1e-05), [[BEX2]] (+0.54, fdr 1e-05); moves opposite to [[BPNT2]] (-0.60, fdr 1e-05), [[BANF1]] (-0.53, fdr 2e-05), [[EMC1]] (-0.51, fdr 6e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[CLRN3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10407.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.81×** | +14.3 | 2e-43 | 38/48 (A-172, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.88×** | +10.3 | 1e-22 | 36/48 (C32, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +7.7 | 3e-12 | 39/47 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +6.4 | 2e-08 | 34/48 (RKO, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.40×** | +5.7 | 1e-06 | 27/48 (A-172, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +5.2 | 2e-05 | 33/48 (NCI-H2030, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.33×** | +4.8 | 1e-04 | 30/46 (SW 900, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +4.5 | 5e-04 | 27/47 (LS 180, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.46×** | +4.5 | 5e-04 | 26/48 (Panc 03.27, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.28×** | +4.2 | 0.002 | 26/47 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.1 | 0.002 | 20/48 (NCI-H1792, A-172, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.006 | 21/48 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.25×** | +3.8 | 0.006 | 19/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.009 | 19/46 (SW1417, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.011 | 15/48 (A498, HCT15, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.012 | 13/48 (SW 900, LS 180, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.015 | 14/48 (LoVo, HOP62, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.017 | 13/48 (LS 180, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.039 | 12/48 (A498, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.20×** | +2.9 | 0.083 | 12/47 (hTERT-HPNE, C-33 A, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.19× | +2.9 | 0.084 | 11/48 (CFPAC-1, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +2.8 | 0.091 | 16/48 (A498, HT-29, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10407.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (C-33 A 0.118×, LoVo 0.349×, NCI-H23 0.262×, AsPC-1 0.440×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (LS 180 0.294×, SW480 0.369×, KATO III 0.443×, AsPC-1 0.454×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 0.329×, LoVo 0.540×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.777×** | -4.3 | 0.008 | 25/48 (Hs 766T, Panc 03.27, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.820× | -3.2 | 0.43 | 14/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10407. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 50.7 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.85× (z +18.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.68× (z +8.9) | — |
| [[SW480 (line)]] | alt | 230 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -18.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 35.8 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +19.8) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A498 (line)]] | wt | 48.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +19.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.90× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 56.1 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.10× (z +19.6) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H460 (line)]] | wt | 61.5 | 3 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.43× (z +9.2) ⚠ toxic | — |
| [[AsPC-1 (line)]] | alt | 242 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.440× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[HEC-1-A (line)]] | alt | 34.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +15.0) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[HS-578T (line)]] | alt | 44.3 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.57× (z +12.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[LoVo (line)]] | wt | 184 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[MIA PaCa-2 (line)]] | alt | 38.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +14.3) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SNU-423 (line)]] | alt | 50.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +14.7) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A549 (line)]] | wt | 44.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +10.3) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[C-33 A (line)]] | alt | 46.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[CFPAC-1 (line)]] | alt | 94.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.7) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[HOP62 (line)]] | alt | 31.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +15.9) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[J82 (line)]] | alt | 38.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +11.8) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[KATO III (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.443× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 84.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 29.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +15.4) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H23 (line)]] | alt | 37.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[NCI-H2347 (line)]] | alt | 44.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +12.1) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[Panc 03.27 (line)]] | alt | 49.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.6) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[PANC-1 (line)]] | alt | 31.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +10.8) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[RKO (line)]] | wt | 54.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.96× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 33.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +8.7) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 86.6 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.72× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW 900 (line)]] | alt | 41.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +11.4) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A-427 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 108 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 63.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 97.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10407), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIME1]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[XYLT1]] | +0.58 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[BEX2]] | +0.54 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[BMP4]] | +0.53 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[ZNF503]] | +0.52 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[CBX4]] | +0.52 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[LINC02253]] | +0.52 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[CYP3A5]] | +0.51 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[RPAIN]] | +0.51 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[RNF43]] | +0.51 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[KLF3]] | +0.51 | +0.48 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[TNFRSF14-AS1]] | +0.51 | +0.57 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BPNT2]] | -0.60 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[BANF1]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[EMC1]] | -0.51 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[AIDA]] | -0.51 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[PAICS]] | -0.49 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[LRP11]] | -0.49 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[PPT1]] | -0.49 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[PIGT]] | -0.48 | -0.29 / -0.52 | both halves | 3e-04 |  |
| [[RNPS1]] | -0.47 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[RPN1]] | -0.47 | -0.37 / -0.52 | both halves | 9e-05 |  |
| [[BRCC3]] | -0.47 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[BLTP2]] | -0.47 | -0.48 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLRN3]] | B | CLRN3 activity raises NUDT4's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 2.77× lower at baseline in the lines without CLRN3 | 1e-03 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13 |
| [[HSD17B2]] | B | HSD17B2 activity raises NUDT4's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 2.22× lower at baseline in the lines without HSD17B2 | 0.001 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |
| [[TOX3]] | B | TOX3 activity raises NUDT4's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 1.95× lower at baseline in the lines without TOX3 | 0.003 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[HNF4A]] | B | HNF4A activity raises NUDT4's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 2.28× lower at baseline in the lines without HNF4A | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |
| [[RASSF6]] | B | RASSF6 activity raises NUDT4's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 1.76× lower at baseline in the lines without RASSF6 | 0.004 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[EPS8L3]] | B | EPS8L3 activity raises NUDT4's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 2.33× lower at baseline in the lines without EPS8L3 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[INPP5D]] | B | INPP5D activity raises NUDT4's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 2.26× lower at baseline in the lines without INPP5D | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5 |
| [[MYO7B]] | B | MYO7B activity raises NUDT4's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 1.75× lower at baseline in the lines without MYO7B | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[IL20RA]] | B | IL20RA activity raises NUDT4's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 2.11× lower at baseline in the lines without IL20RA | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10 |
| [[GPR35]] | B | GPR35 activity raises NUDT4's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 1.80× lower at baseline in the lines without GPR35 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[LINC03040]] | B | LINC03040 activity raises NUDT4's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 1.80× lower at baseline in the lines without LINC03040 | 0.015 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2 |
| [[FOXQ1]] | B | FOXQ1 activity raises NUDT4's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 1.83× lower at baseline in the lines without FOXQ1 | 0.023 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.450). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (16.8, 52.7); signed map (67.2, 12.6). **Vector** length 101, 25.0% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +6.7 | +14.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.4 | +7.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.9 | +10.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +1.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.7 | +4.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +1.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -1.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.1 | -4.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -2.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | nudix hydrolase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q22 — chr12:93,377,883-93,408,146 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DIPP2, HDCMB47P, KIAA0487, DIPP2alpha, DIPP2beta |
| Gene groups (HGNC) | Nudix hydrolase family |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 2 pathways, smallest: Synthesis of pyrophosphates in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZJ9](https://www.uniprot.org/uniprotkb/Q9NZJ9) (Diphosphoinositol polyphosphate phosphohydrolase 2):

> Cleaves the beta-phosphate from diphosphoinositol polyphosphates such as PP-InsP5 (diphosphoinositol pentakisphosphate), PP-InsP4 (diphosphoinositol tetrakisphosphate) and [PP]2-InsP4 (bisdiphosphoinositol tetrakisphosphate), suggesting that it may play a role in signal transduction. Diadenosine polyphosphates, particularly Ap6A (P(1),P(6)-bis(5a-adenosyl) hexaphosphate) and Ap5A (P(1),P(5)-bis(5'-adenosyl) pentaphosphate) are downstream effectors of a signaling cascade that regulates cardiac …

**Summary**, from NCBI Gene [11163](https://www.ncbi.nlm.nih.gov/gene/11163):

> The protein encoded by this gene regulates the turnover of diphosphoinositol polyphosphates. The turnover of these high-energy diphosphoinositol polyphosphates represents a molecular switching activity with important regulatory consequences. Molecular switching by diphosphoinositol polyphosphates may contribute to regulating intracellular trafficking. Several alternatively spliced transcript variants have been described, but the full-length nature of some variants has not been determined. …

**Accessions** — [HGNC:8051](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8051) · Entrez [11163](https://www.ncbi.nlm.nih.gov/gene/11163) · UniProt [Q9NZJ9](https://www.uniprot.org/uniprotkb/Q9NZJ9) · Ensembl [ENSG00000173598](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173598)

## Data

Gene col 10407: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10407); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10407, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10407]; `tensor/DDL_lfc|DDL_z.npy` [10407]; `embed/gene_vectors.npy` [10407]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10407 or target_col == 10407). Every well: [[NUDT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
