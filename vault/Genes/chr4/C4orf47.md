---
symbol: "C4orf47"
type: "gene"
col: 12949
ensembl_id: "ENSG00000205129"
name: "cilia and flagella associated protein 96"
location: "4q35.1"
module: 144
arm: "+"
pooled_cpm: 50.69
n_lines_expressing: 47
n_dd_up: 5
n_dd_down: 45
n_dd_up_clean: 4
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 4
direction_downstream: 11
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# C4orf47

*cilia and flagella associated protein 96* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.88× (z +11.0, q 4e-25, up in 35 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 45 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.273× (z -22.4, q 0e+00, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FUT11]] (+0.75, fdr 7e-06), [[EFCAB3P1]] (+0.73, fdr 7e-06), [[SAP30-DT]] (+0.70, fdr 7e-06); moves opposite to [[ELAC2]] (-0.61, fdr 1e-05), [[OCRL]] (-0.61, fdr 1e-05), [[AGPS]] (-0.58, fdr 1e-05).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NR2F2-AS1]] → it (grade B ⚠); 11 go from it, the strongest it → [[CCDC18-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12949.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +11.0 | 4e-25 | 35/45 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.60×** | +5.8 | 2e-06 | 33/45 (KATO III, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +5.6 | 5e-06 | 33/45 (LoVo, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.022 | 20/44 (SW480, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.34×** | +3.6 | 0.030 | 18/45 (A-172, HOP62, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.21× | +3.2 | 0.12 | 16/45 (SW480, LoVo, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +3.1 | 0.13 | 17/45 (A-172, A498, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.29× | +3.1 | 0.13 | 19/45 (A-172, C-33 A, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.13 | 18/45 (LoVo, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 19 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 45 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12949.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.273×** | -22.4 | 0e+00 | 42/44 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.162×** | -21.3 | 0e+00 | 44/45 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.193×** | -19.3 | 0e+00 | 39/44 (LOX-IMVI, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.224×** | -18.2 | 0e+00 | 41/44 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.293×** | -14.9 | 0e+00 | 42/45 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.300×** | -14.6 | 0e+00 | 40/45 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.340×** | -12.6 | 1e-34 | 29/36 (HCT15, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.393×** | -11.4 | 5e-28 | 32/43 (H4, J82, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.414×** | -10.7 | 5e-25 | 40/45 (NCI-H460, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.425×** | -10.4 | 2e-23 | 35/44 (PANC-1, C-33 A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.421×** | -9.9 | 2e-21 | 41/45 (LOX-IMVI, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.453×** | -9.6 | 3e-20 | 37/45 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.228×** | -9.4 | 2e-19 | 41/44 (MIA PaCa-2, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.462×** | -9.4 | 3e-19 | 31/45 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.254×** | -8.7 | 1e-16 | 38/46 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.512×** | -8.1 | 2e-14 | 28/45 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.615×** | -5.7 | 4e-07 | 27/45 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.706×** | -4.2 | 6e-04 | 24/44 (CFPAC-1, SNU-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.719×** | -4.0 | 0.001 | 21/45 (CFPAC-1, Panc 03.27, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12949. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 80.0 | 0 | 21 (7 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0436× (z -26.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.125× (z -25.5) |
| [[NCI-H460 (line)]] | wt | 78.4 | 0 | 17 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0680× (z -22.5) |
| [[H4 (line)]] | wt | 126 | 0 | 15 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0290× (z -23.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0974× (z -21.5) |
| [[MIA PaCa-2 (line)]] | alt | 98.0 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0193× (z -32.3) |
| [[SNU-423 (line)]] | alt | 91.4 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -23.0) |
| [[HS-578T (line)]] | alt | 97.1 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0668× (z -30.2) |
| [[NCI-H1792 (line)]] | alt | 120 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -17.8) |
| [[PANC-1 (line)]] | alt | 43.3 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -25.8) |
| [[SW480 (line)]] | alt | 64.1 | 0 | 13 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.126× (z -17.2) |
| [[HCT15 (line)]] | alt | 172 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0415× (z -23.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -17.3) |
| [[C-33 A (line)]] | alt | 86.7 | 0 | 10 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0786× (z -18.3) |
| [[CFPAC-1 (line)]] | alt | 81.8 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -15.1) |
| [[HOP62 (line)]] | alt | 79.7 | 1 | 8 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.5) | [[Ixazomib citrate (drug)]] 5 µM 0.171× (z -13.5) |
| [[J82 (line)]] | alt | 59.6 | 0 | 9 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0790× (z -22.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.275× (z -17.0) |
| [[RPMI-7951 (line)]] | alt | 94.9 | 0 | 9 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0881× (z -16.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.194× (z -16.5) |
| [[LS 180 (line)]] | wt | 35.2 | 2 (1 ⚠) | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.31× (z +14.2) | [[Harringtonine (drug)]] 5 µM 0.0786× (z -14.7) |
| [[NCI-H23 (line)]] | alt | 59.0 | 0 | 8 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0412× (z -23.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.156× (z -20.4) |
| [[NCI-H1573 (line)]] | alt | 53.7 | 1 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +9.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -9.8) |
| [[A-172 (line)]] | wt | 48.8 | 2 | 4 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.39× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -15.0) |
| [[C32 (line)]] | wt | 61.0 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.120× (z -12.6) |
| [[CHP-212 (line)]] | wt | 54.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 37.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -13.4) |
| [[HT-29 (line)]] | alt | 24.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 50.1 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0951× (z -13.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.217× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 55.4 | 0 | 5 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0216× (z -14.7) |
| [[A-427 (line)]] | wt | 27.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -13.2) |
| [[A549 (line)]] | wt | 19.9 | 0 | 4 | — | [[Harringtonine (drug)]] 0.5 µM 0.1000× (z -12.0) |
| [[Hs 766T (line)]] | wt | 30.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -12.5) |
| [[LoVo (line)]] | wt | 32.5 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.51× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SW 900 (line)]] | alt | 45.0 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.121× (z -13.6) |
| [[BT-474 (line)]] | alt | 24.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -12.4) |
| [[HepG2_C3A (line)]] | wt | 35.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 26.5 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.190× (z -9.6) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.226× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 20.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -11.8) |
| [[RKO (line)]] | wt | 15.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +11.3) | [[Harringtonine (drug)]] 0.5 µM 0.0769× (z -12.1) |
| [[AN3 CA (line)]] | alt | 38.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.104× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 25.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +12.6) | — |
| [[A498 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.87 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.40 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.37 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 26.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12949), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUT11]] | +0.75 | +0.69 / +0.79 | both halves | 7e-06 |  |
| [[EFCAB3P1]] | +0.73 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[SAP30-DT]] | +0.70 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[SLC35E3]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[TAGAP-AS1]] | +0.66 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[RSBN1]] | +0.65 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[POM121C]] | +0.64 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[ZNF248]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[RSRP1]] | +0.64 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[RBPJ]] | +0.64 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ZNF654]] | +0.63 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[ZSWIM5]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELAC2]] | -0.61 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[OCRL]] | -0.61 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[AGPS]] | -0.58 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[FARSB]] | -0.58 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[API5]] | -0.57 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[LAS1L]] | -0.57 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[PRELID3B]] | -0.56 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[IPO8]] | -0.56 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[PRPS1]] | -0.56 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[POGK]] | -0.55 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[HERC2]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[PDHA1]] | -0.54 | -0.44 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR2F2-AS1]] | B | NR2F2-AS1 activity raises C4orf47's level | lines that do not express NR2F2-AS1 (8) vs lines expressing it (42) | 2.90× lower at baseline in the lines without NR2F2-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: TMEFF1, RIMKLB, LHFPL6 |
| [[SYCP2L]] | B | SYCP2L activity raises C4orf47's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 2.35× lower at baseline in the lines without SYCP2L | 0.061 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |
| [[NRN1]] | B | NRN1 activity raises C4orf47's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.64× lower at baseline in the lines without NRN1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[EFCAB3P1]] | C | EFCAB3P1 activity raises C4orf47's level | lines that do not express EFCAB3P1 (3) vs lines expressing it (47) | 3.80× lower at baseline in the lines without EFCAB3P1 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FRZB, ENSG00000273184, CLEC2D; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC18-AS1]] | C | C4orf47 activity raises CCDC18-AS1's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 2.54× lower at baseline in the lines without C4orf47 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |
| [[HIF1A-AS3]] | C | C4orf47 activity raises HIF1A-AS3's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 2.46× lower at baseline in the lines without C4orf47 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |
| [[FUT11]] | C | C4orf47 activity raises FUT11's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 2.16× lower at baseline in the lines without C4orf47 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |
| [[SPACDR]] | C | C4orf47 activity raises SPACDR's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 2.06× lower at baseline in the lines without C4orf47 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |
| [[NDUFC1]] | C | C4orf47 activity raises NDUFC1's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 1.70× lower at baseline in the lines without C4orf47 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |
| [[TMEM269]] | C | C4orf47 activity raises TMEM269's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 1.74× lower at baseline in the lines without C4orf47 | 0.070 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4 |
| [[TPT1-AS1]] | C | C4orf47 activity raises TPT1-AS1's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 1.89× lower at baseline in the lines without C4orf47 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4 |
| [[NR2F2-AS1]] | C | C4orf47 activity raises NR2F2-AS1's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 5.09× lower at baseline in the lines without C4orf47 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |
| [[SEC31B]] | C | C4orf47 activity raises SEC31B's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 2.11× lower at baseline in the lines without C4orf47 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |
| [[ZNF248]] | C | C4orf47 activity raises ZNF248's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 1.70× lower at baseline in the lines without C4orf47 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |
| [[DARS1-AS1]] | C | C4orf47 activity raises DARS1-AS1's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 1.86× lower at baseline in the lines without C4orf47 | 0.094 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4 |

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.784). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.0, -18.8); signed map (-33.3, 26.3). **Vector** length 110, 39.3% of its response variance represented; |z| ≥ 3 in 1,474 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +11.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.7 | +3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.9 | -10.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.8 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | -1.5 |
|  | [[Sulfatinib (drug)]] 5 µM |  | +2.7 | +1.3 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.7 | +1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.5 | +0.7 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -6.2 | -12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -5.9 | -11.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.4 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.0 | -14.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.7 | -19.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -10.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.8 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.4 | -1.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -3.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 96 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:185,426,249-185,449,826 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LOC441054; previously C4orf47 |
| Matched by | ensembl_id |

UniProt [A7E2U8](https://www.uniprot.org/uniprotkb/A7E2U8) carries no function annotation.

**Summary**, from NCBI Gene [441054](https://www.ncbi.nlm.nih.gov/gene/441054):

> Located in 9+0 non-motile cilium; centrosome; and cytoplasmic microtubule. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34346](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34346) · Entrez [441054](https://www.ncbi.nlm.nih.gov/gene/441054) · UniProt [A7E2U8](https://www.uniprot.org/uniprotkb/A7E2U8) · Ensembl [ENSG00000205129](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205129)

## Data

Gene col 12949: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12949); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12949, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12949]; `tensor/DDL_lfc|DDL_z.npy` [12949]; `embed/gene_vectors.npy` [12949]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12949 or target_col == 12949). Every well: [[C4orf47 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C4orf47.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
