---
symbol: "ID2"
type: "gene"
col: 3713
ensembl_id: "ENSG00000115738"
name: "inhibitor of DNA binding 2"
location: "2p25.1"
module: 59
arm: "+"
pooled_cpm: 32.04
n_lines_expressing: 46
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# ID2

*inhibitor of DNA binding 2* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.80× (z +15.7, q 0e+00, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.866× (z -4.0, q 0.025, down in 13 of 45 measured lines) ⚠ position not correctable. The strongest without an alert is [[5-Azacytidine (drug)]] 5 µM: 0.624× (z -3.9, q 0.025, down in 25 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H661 0.0843×, A-172 0.183×, C-33 A 0.248×, SHP-77 0.274×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (C-33 A 0.219×, AN3 CA 0.193×, SHP-77 0.365×; ⚠ cell-cycle shift, explains ~49% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H661 0.0407×, AN3 CA 0.0634×, SHP-77 0.258×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYLIP]] (+0.66, fdr 7e-06), [[SIRT1]] (+0.55, fdr 1e-05), [[VASN]] (+0.55, fdr 2e-05); moves opposite to [[THOC5]] (-0.52, fdr 3e-05), [[GCN1]] (-0.50, fdr 4e-05), [[MTG1]] (-0.49, fdr 2e-04).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[ID2-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3713.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.80×** | +15.7 | 0e+00 | 40/44 (AsPC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.28×** | +9.9 | 1e-20 | 36/44 (NCI-H2030, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.07×** | +9.3 | 2e-18 | 34/44 (NCI-H2030, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.19×** | +9.2 | 5e-18 | 32/44 (A498, KATO III, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.81×** | +8.3 | 2e-14 | 33/44 (A498, SW 900, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.46×** | +7.5 | 6e-12 | 33/44 (A-427, SNU-423, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.46×** | +7.5 | 6e-12 | 33/44 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +6.2 | 3e-08 | 30/42 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.95×** | +5.6 | 2e-06 | 28/43 (SW480, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.96×** | +5.4 | 4e-06 | 30/44 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.89×** | +5.3 | 7e-06 | 26/44 (KATO III, AsPC-1, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.87×** | +5.2 | 8e-06 | 32/44 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.89×** | +5.1 | 2e-05 | 29/43 (NCI-H2030, MIA PaCa-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +4.6 | 2e-04 | 23/44 (KATO III, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.73×** | +4.4 | 5e-04 | 28/42 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.022 | 18/44 (NCI-H2347, A498, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.058 | 17/44 (RPMI-7951, HOP62, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.062 | 20/43 (NCI-H2347, SNU-423, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3713.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H661 0.0843×, A-172 0.183×, C-33 A 0.248×, SHP-77 0.274×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (C-33 A 0.219×, AN3 CA 0.193×, SHP-77 0.365×; ⚠ cell-cycle shift, explains ~49% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H661 0.0407×, AN3 CA 0.0634×, SHP-77 0.258×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.866× | -4.0 | 0.025 | 13/45 (hTERT-HPNE, SNU-1, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.624×** | -3.9 | 0.025 | 25/44 (LoVo, SW480, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.639×** | -3.7 | 0.038 | 24/44 (SW1417, C-33 A, …) | inconsistent across doses |  |
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.689× | -3.1 | 0.28 | 16/44 (SW1417, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3713. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.7 | 7 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +11.5) | — |
| [[A498 (line)]] | wt | 9.53 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.0× (z +19.1) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +11.7) | — |
| [[AsPC-1 (line)]] | alt | 11.1 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +15.8) | — |
| [[LOX-IMVI (line)]] | wt | 11.6 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.98× (z +13.4) | — |
| [[C-33 A (line)]] | alt | 148 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -13.8) ⚠ cell-cycle shift, explains ~49% of this change |
| [[KATO III (line)]] | alt | 26.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.34× (z +14.7) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 24.7 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +12.7) | — |
| [[CFPAC-1 (line)]] | alt | 34.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +12.3) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +11.4) | — |
| [[SHP-77 (line)]] | alt | 111 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -9.4) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SW 900 (line)]] | alt | 15.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +9.8) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 202 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0634× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 18.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.74× (z +11.5) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 20.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +11.3) | — |
| [[LS 180 (line)]] | wt | 32.2 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.10× (z +8.8) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 9.76 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +12.4) | — |
| [[NCI-H661 (line)]] | alt | 169 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0407× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 36.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +12.7) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[A-172 (line)]] | wt | 48.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 42.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.45× (z +9.1) | — |
| [[A549 (line)]] | wt | 27.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 38.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +9.9) | — |
| [[C32 (line)]] | wt | 10.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +13.2) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[HEC-1-A (line)]] | alt | 26.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.17× (z +13.2) | — |
| [[HOP62 (line)]] | alt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.77× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 16.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +9.4) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H2347 (line)]] | alt | 13.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +12.8) | — |
| [[Panc 03.27 (line)]] | alt | 33.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.54× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 11.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.65× (z +11.8) | — |
| [[CHP-212 (line)]] | wt | 55.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 188 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.81 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.14 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.76 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3713), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYLIP]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[SIRT1]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[VASN]] | +0.55 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[AVPI1]] | +0.55 | +0.43 / +0.65 | both halves | 4e-05 |  |
| [[ID3]] | +0.53 | +0.48 / +0.57 | both halves | 2e-05 | same gene group; pathway: HALLMARK_TGF_BETA_SIGNALING; STRING 545 |
| [[BASP1]] | +0.52 | +0.45 / +0.59 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[EFNA1]] | +0.51 | +0.44 / +0.49 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ID2-AS1]] | +0.51 | +0.50 / +0.57 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CXXC5]] | +0.51 | +0.33 / +0.61 | both halves | 1e-04 |  |
| [[MARCKS]] | +0.51 | +0.52 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[PNRC1]] | +0.50 | +0.45 / +0.53 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[DLL1]] | +0.50 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[H2AJ]] | +0.50 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC5]] | -0.52 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[GCN1]] | -0.50 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[MTG1]] | -0.49 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[DCTD]] | -0.49 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[SZT2]] | -0.48 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[TMEM181]] | -0.47 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[ZDHHC6]] | -0.47 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[E2F4]] | -0.47 | -0.39 / -0.47 | both halves | 5e-05 | STRING 632 |
| [[TREX2]] | -0.46 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[MTA1]] | -0.46 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[ACSF3]] | -0.46 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[CYP2D7]] | -0.46 | -0.44 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ID2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ID2-AS1]] | C | ID2-AS1 activity raises ID2's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 4.25× lower at baseline in the lines without ID2-AS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ID2-AS1]] | C | ID2 activity raises ID2-AS1's level | lines that do not express ID2 (4) vs lines expressing it (46) | 2.38× lower at baseline in the lines without ID2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GAL3ST1, ID2-AS1, MYO15B; co-absent with the target; its own permutation p |
| [[LINC00847]] | C | ID2 activity raises LINC00847's level | lines that do not express ID2 (4) vs lines expressing it (46) | 1.54× lower at baseline in the lines without ID2 | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GAL3ST1, ID2-AS1, MYO15B |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.502). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (29.2, -30.5); signed map (-5.7, 13.6). **Vector** length 105, 30.0% of its response variance represented; |z| ≥ 3 in 1,022 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +15.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +7.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.0 | +2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.7 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.2 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.0 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.0 | -2.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.3 | -2.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -3.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.7 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | inhibitor of DNA binding 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:8,678,845-8,684,461 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GIG8, bHLHb26 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; Inhibitor of DNA binding family |
| Hallmark sets | TGF_BETA_SIGNALING, XENOBIOTIC_METABOLISM, KRAS_SIGNALING_UP, ESTROGEN_RESPONSE_LATE, EPITHELIAL_MESENCHYMAL_TRANSITION, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 5 pathways, smallest: NGF-stimulated transcription; Nuclear Events (kinase and transcription factor activation); Signaling by NTRK1 (TRKA) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02363](https://www.uniprot.org/uniprotkb/Q02363) (DNA-binding protein inhibitor ID-2):

> Transcriptional regulator (lacking a basic DNA binding domain) which negatively regulates the basic helix-loop-helix (bHLH) transcription factors by forming heterodimers and inhibiting their DNA binding and transcriptional activity. Implicated in regulating a variety of cellular processes, including cellular growth, senescence, differentiation, apoptosis, angiogenesis, and neoplastic transformation. Inhibits skeletal muscle and cardiac myocyte differentiation. Regulates the circadian clock by …

**Summary**, from NCBI Gene [3398](https://www.ncbi.nlm.nih.gov/gene/3398):

> The protein encoded by this gene belongs to the inhibitor of DNA binding family, members of which are transcriptional regulators that contain a helix-loop-helix (HLH) domain but not a basic domain. Members of the inhibitor of DNA binding family inhibit the functions of basic helix-loop-helix transcription factors in a dominant-negative manner by suppressing their heterodimerization partners through the HLH domains. This protein may play a role in negatively regulating cell differentiation. A …

**Accessions** — [HGNC:5361](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5361) · Entrez [3398](https://www.ncbi.nlm.nih.gov/gene/3398) · UniProt [Q02363](https://www.uniprot.org/uniprotkb/Q02363) · Ensembl [ENSG00000115738](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115738)

## Data

Gene col 3713: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3713); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3713, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3713]; `tensor/DDL_lfc|DDL_z.npy` [3713]; `embed/gene_vectors.npy` [3713]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3713 or target_col == 3713). Every well: [[ID2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ID2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
