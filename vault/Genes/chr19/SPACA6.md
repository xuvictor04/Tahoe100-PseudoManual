---
symbol: "SPACA6"
type: "gene"
col: 11272
ensembl_id: "ENSG00000182310"
name: "sperm acrosome associated 6"
location: "19q13.41"
module: 21
arm: "+"
pooled_cpm: 23.43
n_lines_expressing: 47
n_dd_up: 1
n_dd_down: 23
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SPACA6

*sperm acrosome associated 6* — 19q13.41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.17× (z +6.4, q 8e-08, up in 14 of 45 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 1 line (A498 3.39×; ⚠ cell-cycle shift, explains ~69% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 6.37×; ⚠ cell-cycle shift, explains ~57% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.42×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.276× (z -15.3, q 0e+00, down in 44 of 45 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.445× (z -9.6, q 1e-19, down in 35 of 43 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAA38]] (+0.61, fdr 3e-05), [[ZNF846]] (+0.57, fdr 6e-05), [[FBXO2]] (+0.55, fdr 3e-05); moves opposite to [[TTC13]] (-0.50, fdr 6e-05), [[DNAJC10]] (-0.46, fdr 4e-05), [[MRPS10]] (-0.45, fdr 4e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[OOEP]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11272.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 1 line (A498 3.39×; ⚠ cell-cycle shift, explains ~69% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 6.37×; ⚠ cell-cycle shift, explains ~57% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.42×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +6.4 | 8e-08 | 14/45 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.34×** | +4.9 | 2e-04 | 28/45 (LS 180, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.32× | +3.3 | 0.17 | 17/45 (LS 180, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.31× | +3.2 | 0.18 | 11/44 (H4, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | 1.30× | +3.1 | 0.18 | 14/45 (Hs 766T, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.32× | +3.1 | 0.18 | 9/45 (H4, A498, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11272.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.276×** | -15.3 | 0e+00 | 44/45 (HOP62, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.314×** | -13.7 | 2e-40 | 42/45 (HOP62, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.353×** | -12.4 | 7e-33 | 40/45 (HOP62, SW 900, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.445×** | -9.6 | 1e-19 | 35/43 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.501×** | -7.9 | 3e-13 | 19/29 (J82, HCT15, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.628×** | -7.8 | 6e-13 | 24/44 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **0.532×** | -7.5 | 5e-12 | 28/38 (J82, A-427, …) | rises with dose | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.535×** | -7.1 | 6e-11 | 28/44 (HEC-1-A, RPMI-7951, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.555×** | -6.7 | 1e-09 | 28/43 (RPMI-7951, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.572×** | -6.6 | 2e-09 | 30/45 (MIA PaCa-2, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.586×** | -6.4 | 1e-08 | 29/45 (HOP62, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **0.639×** | -5.1 | 1e-05 | 23/43 (BT-474, NCI-H2347, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.681×** | -4.4 | 5e-04 | 23/44 (HCT15, HOP62, …) | two highest doses | composition shift; position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.698×** | -4.1 | 0.002 | 18/45 (MIA PaCa-2, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.710×** | -4.1 | 0.002 | 21/45 (J82, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.548×** | -3.7 | 0.006 | 20/45 (HOP62, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.756×** | -3.2 | 0.040 | 18/44 (HOP62, NCI-H1792, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.759×** | -3.1 | 0.044 | 18/44 (SW 900, A-427, …) | rises with dose | position effect removed |
| [[vincristine (drug)]] 0.05 µM |  | **0.769×** | -2.9 | 0.082 | 12/44 (C-33 A, A-427, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.626×** | -2.9 | 0.089 | 11/44 (MIA PaCa-2, HCT15, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.61 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11272. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 54.4 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -12.1) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -10.2) |
| [[BT-474 (line)]] | alt | 42.4 | 0 | 7 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0637× (z -16.2) ⚠ toxic; cell-cycle shift, explains ~57% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0824× (z -15.3) |
| [[HOP62 (line)]] | alt | 54.2 | 0 | 7 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0965× (z -18.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -11.9) |
| [[RPMI-7951 (line)]] | alt | 60.9 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -12.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -11.7) |
| [[J82 (line)]] | alt | 64.9 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0919× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.330× (z -9.1) |
| [[HCT15 (line)]] | alt | 59.7 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[HEC-1-A (line)]] | alt | 42.8 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.276× (z -11.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 24.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -9.9) |
| [[A-172 (line)]] | wt | 17.3 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0573× (z -18.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[CHP-212 (line)]] | wt | 44.2 | 0 | 3 (3 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0695× (z -11.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW 900 (line)]] | alt | 49.3 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.133× (z -13.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A498 (line)]] | wt | 31.5 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.39× (z +10.0) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[KATO III (line)]] | alt | 11.9 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.180× (z -8.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 20.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 16.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -9.7) |
| [[SNU-1 (line)]] | wt | 37.6 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.210× (z -8.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SNU-423 (line)]] | alt | 27.9 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0959× (z -12.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 26.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[A549 (line)]] | wt | 27.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.283× (z -8.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[AN3 CA (line)]] | alt | 24.2 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.0755× (z -8.6) |
| [[C-33 A (line)]] | alt | 40.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 6.72 | 0 | 1 | — | [[Bestatin (drug)]] 5 µM 0.0537× (z -8.7) |
| [[H4 (line)]] | wt | 38.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.127× (z -10.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HepG2_C3A (line)]] | wt | 11.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +9.6) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[LS 180 (line)]] | wt | 16.1 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0348× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.241× (z -9.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H2347 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.245× (z -10.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[AsPC-1 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11272), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA38]] | +0.61 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[ZNF846]] | +0.57 | +0.39 / +0.56 | both halves | 6e-05 |  |
| [[FBXO2]] | +0.55 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[RENO1]] | +0.54 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[ZNF529-AS1]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[ZKSCAN7-AS1]] | +0.53 | +0.28 / +0.53 | both halves | 3e-04 |  |
| [[PABPN1]] | +0.53 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[PCGF3]] | +0.51 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[IER5L]] | +0.50 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[CCDC65]] | +0.48 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[TSC22D4]] | +0.48 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[GPN2]] | +0.47 | +0.27 / +0.48 | both halves | 3e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC13]] | -0.50 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[DNAJC10]] | -0.46 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[MRPS10]] | -0.45 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[PRKDC]] | -0.45 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[STK39]] | -0.42 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[LARS1]] | -0.41 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[GTF3A]] ⚠ | -0.41 | -0.40 / -0.46 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OOEP]] | C | SPACA6 activity lowers OOEP's level | lines that do not express SPACA6 (3) vs lines expressing it (47) | 2.16× higher at baseline in the lines without SPACA6 | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLE6, ZNF14, ZNF547 |
| [[ZBTB8OS]] | C | SPACA6 activity raises ZBTB8OS's level | lines that do not express SPACA6 (3) vs lines expressing it (47) | 1.24× lower at baseline in the lines without SPACA6 | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLE6, ZNF14, ZNF547; its own permutation p |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.455). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.2, 28.6); signed map (36.2, 0.5). **Vector** length 92.2, 21.8% of its response variance represented; |z| ≥ 3 in 990 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +5.8 | +4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.7 | -1.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.0 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +0.1 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | +3.0 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | -0.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +0.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | -0.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | -2.8 | -7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.7 | -4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.4 | -15.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -0.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -4.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | sperm acrosome associated 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.41 — chr19:51,688,346-51,712,387 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LET7EH; previously NCRNA00085, LINC00085, SPACA6P |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Gamete adhesion and fusion factors; Trimeric sperm complex |
| Matched by | ensembl_id |

**Function**, from UniProt [W5XKT8](https://www.uniprot.org/uniprotkb/W5XKT8) (Sperm acrosome membrane-associated protein 6):

> Sperm protein required for fusion of sperm with the egg membrane during fertilization (By similarity). May regulate the expression of sperm surface protein DCST2 (By similarity).

**Summary**, from NCBI Gene [147650](https://www.ncbi.nlm.nih.gov/gene/147650):

> Enables protein-macromolecule adaptor activity. Involved in sperm-egg recognition. Is active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27113](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27113) · Entrez [147650](https://www.ncbi.nlm.nih.gov/gene/147650) · UniProt [W5XKT8](https://www.uniprot.org/uniprotkb/W5XKT8) · Ensembl [ENSG00000182310](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182310)

## Data

Gene col 11272: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11272); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11272, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11272]; `tensor/DDL_lfc|DDL_z.npy` [11272]; `embed/gene_vectors.npy` [11272]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11272 or target_col == 11272). Every well: [[SPACA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPACA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
