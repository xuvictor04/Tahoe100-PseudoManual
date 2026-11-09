---
symbol: "BICDL1"
type: "gene"
col: 5660
ensembl_id: "ENSG00000135127"
name: "BICD family like cargo adaptor 1"
location: "12q24.23"
module: 34
arm: "+"
pooled_cpm: 27.04
n_lines_expressing: 38
n_dd_up: 42
n_dd_down: 4
n_dd_up_clean: 30
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 12
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# BICDL1

*BICD family like cargo adaptor 1* — 12q24.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 6.88× (z +34.4, q 0e+00, up in 35 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.748× (z -7.3, q 1e-10, down in 22 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.199×, SW1417 0.422×, SW48 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H23 0.177×, SHP-77 0.274×, LoVo 0.358×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 3 lines (A-427 0.440×, LoVo 0.473×, SK-MEL-2 0.396×); [[Binimetinib (drug)]] 5 µM in 1 line (NCI-H23 0.323×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[S100A11]] (+0.53, fdr 4e-05), [[SFN]] (+0.52, fdr 1e-04), [[GPR153]] (+0.52, fdr 4e-05); moves opposite to [[RDM1P5]] (-0.49, fdr 7e-04), [[EPHX2]] (-0.46, fdr 3e-04), [[A1CF]] (-0.46, fdr 2e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SFN]] → it (grade B ⚠); 12 go from it, the strongest it → [[TGFB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 17 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5660.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **6.88×** | +34.4 | 0e+00 | 35/36 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.04×** | +32.1 | 0e+00 | 35/36 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **5.73×** | +31.2 | 0e+00 | 35/36 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.27×** | +20.7 | 0e+00 | 29/36 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.76×** | +18.1 | 0e+00 | 35/36 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.92×** | +16.4 | 0e+00 | 30/36 (PANC-1, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.80×** | +14.8 | 0e+00 | 26/36 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.16×** | +13.7 | 5e-41 | 24/35 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.21×** | +13.6 | 2e-40 | 22/36 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.96×** | +12.0 | 1e-31 | 29/35 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.49×** | +11.7 | 1e-29 | 31/36 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.84×** | +10.9 | 4e-26 | 27/36 (SW480, COLO 205, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.88×** | +10.9 | 7e-26 | 25/35 (SW1417, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.79×** | +10.4 | 9e-24 | 27/36 (COLO 205, SHP-77, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +10.1 | 2e-22 | 21/34 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +8.5 | 4e-16 | 23/35 (NCI-H460, J82, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +7.1 | 3e-11 | 22/36 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.48×** | +7.0 | 9e-11 | 24/36 (NCI-H2347, Panc 03.27, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.9 | 1e-10 | 15/36 (MIA PaCa-2, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5660.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.199×, SW1417 0.422×, SW48 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H23 0.177×, SHP-77 0.274×, LoVo 0.358×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 3 lines (A-427 0.440×, LoVo 0.473×, SK-MEL-2 0.396×); [[Binimetinib (drug)]] 5 µM in 1 line (NCI-H23 0.323×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.748×** | -7.3 | 1e-10 | 22/36 (A-427, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.465×** | -7.1 | 3e-10 | 23/35 (LoVo, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.832×** | -4.6 | 8e-04 | 11/36 (AsPC-1, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.823×** | -3.8 | 0.018 | 12/36 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.839× | -3.7 | 0.023 | 14/36 (NCI-H23, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.945× | -3.6 | 0.033 | 5/36 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.847× | -3.2 | 0.12 | 7/36 (SW480, NCI-H23, …) | two highest doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 0.718× | -3.1 | 0.14 | 10/23 (HT-29, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.61 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5660. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 39.4 | 13 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.90× (z +21.3) | — |
| [[LoVo (line)]] | wt | 74.6 | 4 (1 ⚠) | 5 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.50× (z +13.2) | [[Selinexor (drug)]] 5 µM 0.473× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 21.2 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.76× (z +14.1) | — |
| [[SHP-77 (line)]] | alt | 127 | 4 (4 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +9.6) ⚠ cell-cycle shift, explains ~38% of this change | [[Dinaciclib (drug)]] 5 µM 0.199× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 16.1 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 10.5× (z +18.0) | — |
| [[A549 (line)]] | wt | 9.47 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 14.8× (z +12.0) | — |
| [[HT-29 (line)]] | alt | 35.4 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.46× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0524× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 46.6 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.36× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Binimetinib (drug)]] 5 µM 0.323× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 27.2 | 4 | 1 | [[Panobinostat (drug)]] 0.5 µM 7.01× (z +12.6) | [[Selinexor (drug)]] 5 µM 0.396× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 39.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.27× (z +14.6) | — |
| [[C32 (line)]] | wt | 8.19 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +11.8) | — |
| [[COLO 205 (line)]] | alt | 16.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.56× (z +12.8) | — |
| [[HEC-1-A (line)]] | alt | 12.5 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 10.2× (z +13.1) | — |
| [[J82 (line)]] | alt | 12.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 10.3× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 35.0 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.84× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 8.26 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 9.16× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 12.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 9.36× (z +11.0) | — |
| [[A-172 (line)]] | wt | 7.54 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.90× (z +10.5) | — |
| [[A-427 (line)]] | wt | 99.2 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.61× (z +9.7) | [[Selinexor (drug)]] 5 µM 0.440× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 29.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.03× (z +10.9) | — |
| [[KATO III (line)]] | alt | 27.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.50× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.22 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 28.1× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 31.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.47× (z +14.7) | — |
| [[NCI-H2030 (line)]] | alt | 17.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.88× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 98.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.16× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.422× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 30.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.86× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 10.4 | 2 | 0 | [[Belinostat (drug)]] 5 µM 13.8× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 26.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.92× (z +10.0) | — |
| [[SW 900 (line)]] | alt | 9.26 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 11.8× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 18.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.94× (z +8.5) | — |
| [[SW48 (line)]] | wt | 58.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 5.59 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.37 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.99 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.31 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.70 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5660), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[S100A11]] | +0.53 | +0.45 / +0.40 | both halves | 4e-05 |  |
| [[SFN]] | +0.52 | +0.54 / +0.35 | both halves | 1e-04 |  |
| [[GPR153]] | +0.52 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[SLC35E4]] | +0.52 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[EPHA2-AS1]] | +0.51 | +0.33 / +0.52 | both halves | 1e-04 |  |
| [[FRMD8]] | +0.51 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[TIAM1]] | +0.50 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[CDYL2]] | +0.50 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[RTN2]] | +0.50 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[ZBTB46]] | +0.49 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[KLF13]] | +0.49 | +0.35 / +0.40 | both halves | 1e-04 |  |
| [[STK10]] | +0.48 | +0.55 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RDM1P5]] | -0.49 | -0.44 / -0.21 | both halves | 7e-04 |  |
| [[EPHX2]] | -0.46 | -0.42 / -0.28 | both halves | 3e-04 |  |
| [[A1CF]] | -0.46 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[TESMIN]] | -0.44 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[MINDY1]] | -0.44 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[EIF2D]] | -0.44 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[FUBP1]] | -0.43 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[SERPINF1]] | -0.43 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[KLHL14]] | -0.43 | -0.42 / -0.24 | both halves | 4e-04 |  |
| [[PPP4R3B]] | -0.42 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[HINT3]] | -0.42 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[WBP11]] | -0.42 | -0.38 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SFN]] | B | SFN activity raises BICDL1's level | lines that do not express SFN (20) vs lines expressing it (30) | 3.01× lower at baseline in the lines without SFN | 0.018 | ⚠ within organs, on part of the lines; also absent: KRT18, ESRP2, SH2D3A |
| [[CPLX1]] | B | CPLX1 activity raises BICDL1's level | lines that do not express CPLX1 (9) vs lines expressing it (41) | 3.37× lower at baseline in the lines without CPLX1 | 0.051 | ⚠ within organs, on part of the lines; also absent: LLGL2, CASZ1, MNX1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers BICDL1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGFB1]] | B | BICDL1 activity lowers TGFB1's level | lines that do not express BICDL1 (12) vs lines expressing it (38) | 2.98× higher at baseline in the lines without BICDL1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857 |
| [[ZNRF1]] | B | BICDL1 activity lowers ZNRF1's level | lines that do not express BICDL1 (12) vs lines expressing it (38) | 1.70× higher at baseline in the lines without BICDL1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857 |
| [[SFN]] | B | BICDL1 activity raises SFN's level | lines that do not express BICDL1 (12) vs lines expressing it (38) | 3.13× lower at baseline in the lines without BICDL1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857 |
| [[HMOX2]] | B | BICDL1 activity raises HMOX2's level | lines that do not express BICDL1 (12) vs lines expressing it (38) | 1.38× lower at baseline in the lines without BICDL1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857 |
| [[METRNL]] | B | BICDL1 activity lowers METRNL's level | lines that do not express BICDL1 (12) vs lines expressing it (38) | 2.40× higher at baseline in the lines without BICDL1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857 |
| [[MYO9B]] | B | BICDL1 activity lowers MYO9B's level | lines that do not express BICDL1 (12) vs lines expressing it (38) | 1.48× higher at baseline in the lines without BICDL1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857 |
| [[CORO2B]] | B | BICDL1 activity lowers CORO2B's level | lines that do not express BICDL1 (12) vs lines expressing it (38) | 2.12× higher at baseline in the lines without BICDL1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857 |
| [[LRP8]] | B | BICDL1 activity weakens LRP8's drug response | lines that do not express BICDL1 (11) vs lines expressing it (35) | the lines without BICDL1 respond 0.97× as strongly (z diff +0.00); strongest at Dinaciclib 0.05 µM: 4.36x vs 1.81x (z diff -3.5) | 0.057 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857; target measured in part of the lines; both ways; artifact flags |
| [[BAIAP2L1]] | B | BICDL1 activity raises BAIAP2L1's level | lines that do not express BICDL1 (12) vs lines expressing it (38) | 2.45× lower at baseline in the lines without BICDL1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857 |
| [[RDH13]] | B | BICDL1 activity raises RDH13's level | lines that do not express BICDL1 (12) vs lines expressing it (38) | 1.70× lower at baseline in the lines without BICDL1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857 |
| [[RHOF]] | B | BICDL1 activity raises RHOF's level | lines that do not express BICDL1 (12) vs lines expressing it (38) | 2.22× lower at baseline in the lines without BICDL1 | 0.093 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857 |
| [[AMACR]] | B | BICDL1 activity raises AMACR's level | lines that do not express BICDL1 (12) vs lines expressing it (38) | 1.26× lower at baseline in the lines without BICDL1 | 0.098 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.465). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.1, 31.4); signed map (-6.2, 42.8). **Vector** length 91.0, 21.5% of its response variance represented; |z| ≥ 3 in 1,197 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +16.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.3 | +4.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.3 | +3.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.2 | +10.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.1 | +3.7 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.6 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +10.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.7 | -7.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -2.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.5 | -7.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -1.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.1 | -4.6 |
|  | [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | -2.1 | -2.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.1 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | BICD family like cargo adaptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.23 — chr12:119,989,236-120,094,494 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ26450, BICDR-1; previously CCDC64 |
| Gene groups (HGNC) | BICD family cargo adaptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZP65](https://www.uniprot.org/uniprotkb/Q6ZP65) (BICD family-like cargo adapter 1):

> Acts as an adapter protein linking the dynein motor complex to various cargos and converts dynein from a non-processive to a highly processive motor in the presence of dynactin. Facilitates the interaction between dynein and dynactin and activates dynein processivity (the ability to move along a microtubule for a long distance without falling off the track). Predominantly recruits 2 dyneins, which increases both the force and speed of the microtubule motor. Component of secretory vesicle …

**Summary**, from NCBI Gene [92558](https://www.ncbi.nlm.nih.gov/gene/92558):

> Predicted to enable dynactin binding activity and small GTPase binding activity. Predicted to be involved in Golgi to secretory granule transport; neuron projection development; and vesicle transport along microtubule. Predicted to be located in centrosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28095](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28095) · Entrez [92558](https://www.ncbi.nlm.nih.gov/gene/92558) · UniProt [Q6ZP65](https://www.uniprot.org/uniprotkb/Q6ZP65) · Ensembl [ENSG00000135127](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135127)

## Data

Gene col 5660: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5660); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5660, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5660]; `tensor/DDL_lfc|DDL_z.npy` [5660]; `embed/gene_vectors.npy` [5660]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5660 or target_col == 5660). Every well: [[BICDL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BICDL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
