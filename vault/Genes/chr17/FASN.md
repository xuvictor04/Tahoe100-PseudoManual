---
symbol: "FASN"
type: "gene"
col: 9840
ensembl_id: "ENSG00000169710"
name: "fatty acid synthase"
location: "17q25.3"
module: 86
arm: "+"
pooled_cpm: 52.94
n_lines_expressing: 49
n_dd_up: 43
n_dd_down: 2
n_dd_up_clean: 32
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# FASN

*fatty acid synthase* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (11 with an alert ⚠); the strongest is [[Cepharanthine (drug)]] 5 µM: 2.90× (z +15.0, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.633× (z -4.4, q 0.005, down in 23 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.190×, BT-474 0.262×, RKO 0.307×); [[Harringtonine (drug)]] 5 µM in 3 lines (LS 180 0.150×, A-427 0.271×, BT-474 0.244×; ⚠ cell-cycle shift, explains ~51% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.121×, BT-474 0.219×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHCR7]] (+0.78, fdr 7e-06), [[ACLY]] (+0.72, fdr 7e-06), [[PCSK9]] (+0.71, fdr 7e-06); moves opposite to [[ZCCHC9]] (-0.47, fdr 1e-04), [[SNRPB2]] (-0.46, fdr 3e-04), [[NKAP]] (-0.45, fdr 2e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9840.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **2.90×** | +15.0 | 0e+00 | 47/47 (NCI-H23, HOP62, …) | top dose only | position effect removed |
| [[Berbamine (drug)]] 5 µM |  | **2.48×** | +12.9 | 2e-35 | 44/48 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.61×** | +12.3 | 1e-32 | 37/40 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.37×** | +12.2 | 7e-32 | 41/44 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +10.8 | 6e-25 | 41/47 (A549, A-172, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +9.3 | 2e-18 | 34/46 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.58×** | +8.7 | 2e-16 | 37/44 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **2.11×** | +7.2 | 6e-11 | 43/46 (HOP62, SW 900, …) | top dose only |  |
| [[Posaconazole (drug)]] 5 µM |  | **2.10×** | +7.1 | 7e-11 | 38/47 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift |
| [[Entrectinib (drug)]] 5 µM |  | **2.03×** | +7.1 | 8e-11 | 38/46 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.95×** | +6.6 | 2e-09 | 39/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +6.5 | 5e-09 | 30/46 (NCI-H1792, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.82×** | +5.8 | 4e-07 | 34/46 (HEC-1-A, C-33 A, …) | top dose only | plate-row cell shift; position effect removed |
| [[Bexarotene (drug)]] 0.5 µM |  | **1.75×** | +5.6 | 1e-06 | 34/47 (SHP-77, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Berbamine (drug)]] 0.5 µM |  | **1.66×** | +5.0 | 2e-05 | 36/47 (LS 180, HT-29, …) | rises with dose |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.65×** | +4.8 | 6e-05 | 29/47 (C32, NCI-H460, …) | top dose only | plate-row cell shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.7 | 9e-05 | 26/46 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +4.6 | 1e-04 | 26/46 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bexarotene (drug)]] 0.05 µM |  | **1.58×** | +4.6 | 2e-04 | 27/47 (C-33 A, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 5 µM |  | **1.59×** | +4.4 | 3e-04 | 25/47 (HOP62, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9840.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.190×, BT-474 0.262×, RKO 0.307×); [[Harringtonine (drug)]] 5 µM in 3 lines (LS 180 0.150×, A-427 0.271×, BT-474 0.244×; ⚠ cell-cycle shift, explains ~51% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.121×, BT-474 0.219×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.633×** | -4.4 | 0.005 | 23/46 (J82, KATO III, …) | top dose only | position effect removed |
| [[Afatinib (drug)]] 0.5 µM |  | **0.752×** | -4.0 | 0.016 | 32/48 (A-427, BT-474, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.701× | -3.3 | 0.17 | 22/46 (SNU-1, LS 180, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.739× | -3.1 | 0.30 | 17/47 (LS 180, A-172, …) | inconsistent across doses | position effect removed |
| [[Quinestrol (drug)]] 5 µM |  | 0.811× | -3.0 | 0.30 | 19/48 (KATO III, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9840. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 23.1 | 8 (3 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 5.93× (z +14.8) | — |
| [[NCI-H460 (line)]] | wt | 45.7 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.29× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.22× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 21.5 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +10.9) | — |
| [[A-172 (line)]] | wt | 41.8 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +11.4) | — |
| [[NCI-H1792 (line)]] | alt | 32.9 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +14.1) | — |
| [[A549 (line)]] | wt | 22.5 | 5 (1 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 6.84× (z +13.8) | — |
| [[CFPAC-1 (line)]] | alt | 25.1 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 32.7 | 5 | 0 | [[Berbamine (drug)]] 5 µM 3.41× (z +11.2) | — |
| [[LoVo (line)]] | wt | 46.1 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.15× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Berbamine (drug)]] 5 µM 3.23× (z +11.3) | — |
| [[BT-474 (line)]] | alt | 306 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -12.2) |
| [[J82 (line)]] | alt | 33.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.14× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 81.1 | 3 (1 ⚠) | 1 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 3.49× (z +10.5) | [[Harringtonine (drug)]] 5 µM 0.150× (z -11.0) ⚠ cell-cycle shift, explains ~51% of this change |
| [[MIA PaCa-2 (line)]] | alt | 71.4 | 4 (1 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 3.38× (z +11.3) | — |
| [[A-427 (line)]] | wt | 126 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -16.9) |
| [[C-33 A (line)]] | alt | 84.3 | 3 | 0 | [[Cepharanthine (drug)]] 5 µM 5.08× (z +14.4) | — |
| [[HT-29 (line)]] | alt | 50.8 | 3 (1 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 4.59× (z +12.9) | — |
| [[NCI-H23 (line)]] | alt | 35.2 | 3 (1 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 6.59× (z +16.2) | — |
| [[SW480 (line)]] | alt | 49.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +12.0) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 48.1 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 2.72× (z +10.9) | — |
| [[C32 (line)]] | wt | 51.6 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.75× (z +10.0) | — |
| [[H4 (line)]] | wt | 21.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 46.3 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 5.00× (z +14.7) | — |
| [[LOX-IMVI (line)]] | wt | 41.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.07× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 22.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.61× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 35.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.43× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.02× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 28.4 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 5.88× (z +13.3) | — |
| [[COLO 205 (line)]] | alt | 25.4 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 4.82× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 44.6 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 3.94× (z +9.1) | — |
| [[KATO III (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.187× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 26.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 39.6 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 3.31× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 32.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 80.2 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 2.75× (z +9.1) | — |
| [[RKO (line)]] | wt | 86.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -11.2) |
| [[SHP-77 (line)]] | alt | 44.8 | 1 | 0 | [[Bexarotene (drug)]] 0.5 µM 4.51× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9840), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHCR7]] | +0.78 | +0.83 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 757 |
| [[ACLY]] | +0.72 | +0.65 / +0.76 | both halves | 7e-06 | same gene group; pathway: ChREBP activates metabolic gene expression; STRING 994 |
| [[PCSK9]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[DHCR24]] | +0.70 | +0.72 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_FATTY_ACID_METABOLISM; STRING 635 |
| [[ACAT2]] | +0.70 | +0.74 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 571 |
| [[FADS2]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 712 |
| [[SCD]] | +0.69 | +0.69 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 960 |
| [[HMGCS1]] | +0.68 | +0.71 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 840 |
| [[ACACA]] | +0.67 | +0.64 / +0.70 | both halves | 7e-06 | pathway: Activation of gene expression by SREBF (SREBP); STRING 998 |
| [[PCYT2]] | +0.66 | +0.81 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[HMGCR]] | +0.66 | +0.73 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 820 |
| [[CYP51A1]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 619 |

## Genes that move opposite

*18 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC9]] | -0.47 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[SNRPB2]] | -0.46 | -0.28 / -0.58 | both halves | 3e-04 | pathway: Dengue Virus-Host Interactions |
| [[NKAP]] | -0.45 | -0.29 / -0.52 | both halves | 2e-04 |  |
| [[CWF19L2]] | -0.44 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[SMIM26]] ⚠ | -0.44 | -0.23 / -0.57 | both halves | 5e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[SEC62]] | -0.44 | -0.29 / -0.54 | both halves | 3e-04 |  |
| [[PIGBOS1]] | -0.44 | -0.23 / -0.55 | both halves | 5e-04 |  |
| [[GPATCH11]] | -0.43 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[C18orf21]] | -0.43 | -0.26 / -0.50 | both halves | 4e-04 |  |
| [[MRPS18C]] | -0.43 | -0.18 / -0.55 | ⚠ one half (not replicated) | 9e-04 |  |
| [[CIR1]] | -0.42 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[BTG1]] | -0.42 | -0.25 / -0.52 | both halves | 4e-04 |  |
| [[CROCCP2-1]] | -0.42 | -0.21 / -0.53 | both halves | 7e-04 |  |
| [[MFAP1]] | -0.42 | -0.27 / -0.54 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.731). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.6, -49.8); signed map (-52.0, 31.8). **Vector** length 145, 48.9% of its response variance represented; |z| ≥ 3 in 1,492 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *cholesterol synthesis* (control, mean cos +0.58 to 22); *Cholesterol biosynthesis* (reactome, mean cos +0.58 to 20); *mTORC1 signaling* (hallmark, mean cos +0.57 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +11.0 | +15.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.5 | +12.3 |
|  | [[Berbamine (drug)]] 5 µM |  | +8.1 | +12.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +12.2 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +6.6 | +7.2 |
|  | [[Posaconazole (drug)]] 5 µM |  | +5.6 | +7.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +5.2 | +3.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.7 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.1 | -3.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -3.3 | -0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | fatty acid synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,078,338-82,098,294 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FAS, SDR27X1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily; 7BS orphan methyltransferases; 3-hydroxyacyl-[acyl-carrier-protein] dehydratases; Thioester hydrolases; Acyltransferases |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, FATTY_ACID_METABOLISM, ESTROGEN_RESPONSE_EARLY |
| Reactome | 18 pathways, smallest: ChREBP activates metabolic gene expression; NR1H2 & NR1H3 regulate gene expression linked to lipogenesis; Vitamin B5 (pantothenate) metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P49327](https://www.uniprot.org/uniprotkb/P49327) (Fatty acid synthase):

> Fatty acid synthetase is a multifunctional enzyme that catalyzes the de novo biosynthesis of long-chain saturated fatty acids starting from acetyl-CoA and malonyl-CoA in the presence of NADPH. This multifunctional protein contains 7 catalytic activities and a site for the binding of the prosthetic group 4'-phosphopantetheine of the acyl carrier protein ([ACP]) domain.; (Microbial infection) Fatty acid synthetase activity is required for SARS coronavirus-2/SARS-CoV-2 replication.

**Summary**, from NCBI Gene [2194](https://www.ncbi.nlm.nih.gov/gene/2194):

> The enzyme encoded by this gene is a multifunctional protein. Its main function is to catalyze the synthesis of palmitate from acetyl-CoA and malonyl-CoA, in the presence of NADPH, into long-chain saturated fatty acids. In some cancer cell lines, this protein has been found to be fused with estrogen receptor-alpha (ER-alpha), in which the N-terminus of FAS is fused in-frame with the C-terminus of ER-alpha. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3594) · Entrez [2194](https://www.ncbi.nlm.nih.gov/gene/2194) · UniProt [P49327](https://www.uniprot.org/uniprotkb/P49327) · Ensembl [ENSG00000169710](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169710)

## Data

Gene col 9840: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9840); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9840, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9840]; `tensor/DDL_lfc|DDL_z.npy` [9840]; `embed/gene_vectors.npy` [9840]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9840 or target_col == 9840). Every well: [[FASN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FASN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
