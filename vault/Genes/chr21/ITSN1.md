---
symbol: "ITSN1"
type: "gene"
col: 13004
ensembl_id: "ENSG00000205726"
name: "intersectin 1"
location: "21q22.11"
module: 1
arm: "-"
pooled_cpm: 182.3
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ITSN1

*intersectin 1* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.51× (z +19.6, q 0e+00, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.768× (z -8.9, q 4e-16, down in 33 of 48 measured lines) ⚠ transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.629× (z -8.2, q 5e-14, down in 28 of 49 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAPGEF2]] (+0.53, fdr 1e-05), [[CDKL5]] (+0.53, fdr 1e-05), [[MYL6]] (+0.52, fdr 3e-05); moves opposite to [[ZNF12]] (-0.50, fdr 1e-04), [[TRIM32]] (-0.45, fdr 5e-05), [[SPATA2]] (-0.45, fdr 8e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MIR3142HG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13004.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +19.6 | 0e+00 | 36/48 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +18.0 | 0e+00 | 32/49 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +15.8 | 0e+00 | 44/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +13.2 | 7e-38 | 33/48 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +11.6 | 8e-29 | 39/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +10.8 | 3e-25 | 31/50 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +9.2 | 3e-18 | 36/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +8.3 | 1e-14 | 24/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.25×** | +7.6 | 2e-12 | 25/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.47×** | +6.8 | 8e-10 | 29/49 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.39×** | +5.8 | 3e-07 | 26/48 (RKO, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +5.0 | 2e-05 | 16/48 (SW1417, J82, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.15× | +4.6 | 2e-04 | 16/47 (LS 180, SNU-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.14× | +4.4 | 5e-04 | 16/47 (SNU-1, J82, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.001 | 20/47 (CFPAC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.09× | +4.0 | 0.003 | 14/48 (J82, SNU-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13004.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.768×** | -8.9 | 4e-16 | 33/48 (NCI-H2030, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.775×** | -8.2 | 5e-14 | 30/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.629×** | -8.2 | 5e-14 | 28/49 (NCI-H1792, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.803×** | -7.4 | 2e-11 | 26/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.759×** | -4.8 | 1e-04 | 18/38 (HS-578T, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.813×** | -3.6 | 0.025 | 15/49 (MIA PaCa-2, A549, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.895× | -3.6 | 0.027 | 16/48 (LOX-IMVI, BT-474, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change | 0.893× | -3.5 | 0.028 | 19/45 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.827×** | -3.3 | 0.051 | 18/45 (C32, H4, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13004. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 137 | 7 | 1 | [[Panobinostat (drug)]] 5 µM 2.20× (z +16.7) | [[Auranofin (drug)]] 5 µM 0.617× (z -10.3) |
| [[HT-29 (line)]] | alt | 81.6 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +19.8) | — |
| [[A-172 (line)]] | wt | 241 | 5 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +20.6) | [[TAK-901 (drug)]] 5 µM 0.369× (z -9.8) |
| [[C32 (line)]] | wt | 120 | 5 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +16.7) | [[Harringtonine (drug)]] 0.5 µM 0.494× (z -9.5) ⚠ cell-cycle shift, explains ~3% of this change |
| [[HEC-1-A (line)]] | alt | 189 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +13.8) | [[Dinaciclib (drug)]] 0.05 µM 0.578× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change |
| [[J82 (line)]] | alt | 119 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.38× (z +13.4) | — |
| [[LoVo (line)]] | wt | 139 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +26.6) | — |
| [[RKO (line)]] | wt | 140 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +21.9) | — |
| [[HOP62 (line)]] | alt | 156 | 3 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +13.6) | [[TAK-901 (drug)]] 5 µM 0.335× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 241 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +21.1) | [[Auranofin (drug)]] 5 µM 0.597× (z -8.9) |
| [[LS 180 (line)]] | wt | 257 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.546× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 266 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +17.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.414× (z -16.4) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 174 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +15.1) | — |
| [[PANC-1 (line)]] | alt | 158 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +19.8) | — |
| [[A-427 (line)]] | wt | 233 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +26.0) | — |
| [[AsPC-1 (line)]] | alt | 295 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 191 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +12.6) | — |
| [[SK-MEL-2 (line)]] | alt | 115 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +11.3) | — |
| [[SW1417 (line)]] | alt | 146 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.49× (z +14.1) | — |
| [[CFPAC-1 (line)]] | alt | 168 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +20.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.551× (z -9.4) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 83.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.0) | — |
| [[H4 (line)]] | wt | 215 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +13.7) | — |
| [[hTERT-HPNE (line)]] | wt | 161 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +12.5) | — |
| [[NCI-H1792 (line)]] | alt | 160 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +12.8) | [[TAK-901 (drug)]] 5 µM 0.270× (z -11.3) |
| [[SW48 (line)]] | wt | 164 | 2 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 445 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.437× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 107 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +14.0) | — |
| [[SNU-1 (line)]] | wt | 254 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.6) | — |
| [[SNU-423 (line)]] | alt | 143 | 1 | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +8.7) | [[TAK-901 (drug)]] 5 µM 0.375× (z -8.7) |
| [[A498 (line)]] | wt | 268 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.51× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 219 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 128 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +11.5) | — |
| [[Hs 766T (line)]] | wt | 322 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.477× (z -8.5) ⚠ toxic |
| [[HS-578T (line)]] | alt | 172 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.290× (z -9.1) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 233 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.585× (z -9.1) ⚠ transcription drop |
| [[NCI-H23 (line)]] | alt | 249 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +14.1) | — |
| [[SHP-77 (line)]] | alt | 187 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +10.4) | — |
| [[SW 900 (line)]] | alt | 137 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.56× (z +8.6) | — |
| [[A549 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 139 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 299 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 110 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13004), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAPGEF2]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[CDKL5]] | +0.53 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[MYL6]] | +0.52 | +0.44 / +0.50 | both halves | 3e-05 | pathway: EPH-Ephrin signaling |
| [[WDR44]] | +0.51 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[PDLIM5]] | +0.50 | +0.38 / +0.49 | both halves | 6e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[NMT2]] | +0.50 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[HECTD4]] | +0.50 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[ATP11C]] | +0.50 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[BMPR2]] | +0.50 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[FRYL]] | +0.49 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[KIF1B]] | +0.49 | +0.37 / +0.64 | both halves | 8e-05 | same gene group; pathway: HALLMARK_MITOTIC_SPINDLE |
| [[MAGI3]] | +0.49 | +0.46 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF12]] | -0.50 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[TRIM32]] | -0.45 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[SPATA2]] | -0.45 | -0.37 / -0.44 | both halves | 8e-05 | pathway: Death Receptor Signaling |
| [[ZNF112]] | -0.45 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[ZNF2]] | -0.44 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[NEPRO]] | -0.44 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[GSTO2]] | -0.44 | -0.29 / -0.39 | both halves | 2e-04 |  |
| [[ZNF232]] | -0.43 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[E2F6]] | -0.43 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[KAT14]] | -0.42 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[ZFP69B]] | -0.42 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[ZNF384]] | -0.41 | -0.48 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR3142HG]] | B | MIR3142HG activity lowers ITSN1's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 1.23× higher at baseline in the lines without MIR3142HG | 0.013 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130 |
| [[NTN4]] | B | NTN4 activity lowers ITSN1's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 1.21× higher at baseline in the lines without NTN4 | 0.029 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[TOP2A]] | B | TOP2A activity lowers ITSN1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.264). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.5, 2.8); signed map (-14.5, 18.9). **Vector** length 106, 27.8% of its response variance represented; |z| ≥ 3 in 1,394 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +10.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +19.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +18.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +2.6 |
|  | [[RMC-6236 (drug)]] 5 µM |  | +2.6 | +3.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.9 | -8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.0 | -7.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.8 | -8.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -4.3 | -8.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | intersectin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:33,642,400-33,899,861 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SH3P17, MGC134948, MGC134949; previously SH3D1A, ITSN |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs; C2 domain containing; EF-hand domain containing; SH3 domain containing |
| Hallmark sets | ADIPOGENESIS, MITOTIC_SPINDLE |
| Reactome | 21 pathways, smallest: EPHB-mediated forward signaling; NRAGE signals death through JNK; RHOQ GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15811](https://www.uniprot.org/uniprotkb/Q15811) (Intersectin-1):

> Adapter protein that provides a link between the endocytic membrane traffic and the actin assembly machinery. Acts as a guanine nucleotide exchange factor (GEF) for CDC42, and thereby stimulates actin nucleation mediated by WASL and the ARP2/3 complex. Plays a role in the assembly and maturation of clathrin-coated vesicles (By similarity). Recruits FCHSD2 to clathrin-coated pits. Involved in endocytosis of activated EGFR, and probably also other growth factor receptors (By similarity). Involved …

**Summary**, from NCBI Gene [6453](https://www.ncbi.nlm.nih.gov/gene/6453):

> The protein encoded by this gene is a cytoplasmic membrane-associated protein that indirectly coordinates endocytic membrane traffic with the actin assembly machinery. In addition, the encoded protein may regulate the formation of clathrin-coated vesicles and could be involved in synaptic vesicle recycling. This protein has been shown to interact with dynamin, CDC42, SNAP23, SNAP25, SPIN90, EPS15, EPN1, EPN2, and STN2. Multiple transcript variants encoding different isoforms have been found for …

**Accessions** — [HGNC:6183](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6183) · Entrez [6453](https://www.ncbi.nlm.nih.gov/gene/6453) · UniProt [Q15811](https://www.uniprot.org/uniprotkb/Q15811) · Ensembl [ENSG00000205726](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205726)

## Data

Gene col 13004: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13004); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13004, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13004]; `tensor/DDL_lfc|DDL_z.npy` [13004]; `embed/gene_vectors.npy` [13004]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13004 or target_col == 13004). Every well: [[ITSN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITSN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
