---
symbol: "CASP4"
type: "gene"
col: 12310
ensembl_id: "ENSG00000196954"
name: "caspase 4"
location: "11q22.3"
module: 32
arm: "+"
pooled_cpm: 58.55
n_lines_expressing: 45
n_dd_up: 7
n_dd_down: 31
n_dd_up_clean: 7
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 17
direction_downstream: 4
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# CASP4

*caspase 4* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 1.51× (z +7.9, q 1e-12, up in 33 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.312× (z -31.6, q 0e+00, down in 39 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SP140L]] (+0.63, fdr 1e-05), [[TRIM38]] (+0.61, fdr 1e-05), [[TRIM56]] (+0.59, fdr 3e-05); moves opposite to [[SMPD4]] (-0.46, fdr 1e-04), [[CERCAM]] (-0.46, fdr 2e-04), [[MAN1B1]] (-0.44, fdr 1e-04).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[KCNQ3]] → it (grade B ⚠); 4 go from it, the strongest it → [[CA13]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12310.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +7.9 | 1e-12 | 33/43 (LoVo, HT-29, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +7.6 | 8e-12 | 31/43 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +5.5 | 8e-06 | 22/43 (NCI-H2347, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +4.8 | 2e-04 | 21/43 (LS 180, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +4.6 | 4e-04 | 21/43 (PANC-1, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.2 | 0.002 | 15/43 (LS 180, KATO III, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.51×** | +4.2 | 0.003 | 15/41 (AsPC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.20× | +3.4 | 0.047 | 13/42 (CFPAC-1, AsPC-1, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.047 | 10/43 (HS-578T, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.3 | 0.053 | 7/43 (SHP-77, SK-MEL-2, …) | rises with dose |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +3.1 | 0.11 | 7/43 (NCI-H1573, RKO, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.17× | +3.0 | 0.12 | 15/44 (HT-29, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12310.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.312×** | -31.6 | 0e+00 | 39/42 (NCI-H1573, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.270×** | -25.1 | 0e+00 | 42/43 (RKO, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.448×** | -21.7 | 0e+00 | 39/43 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.357×** | -19.7 | 0e+00 | 38/43 (RKO, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.401×** | -17.5 | 0e+00 | 40/43 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.471×** | -13.9 | 9e-42 | 36/43 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.545×** | -10.8 | 5e-25 | 27/37 (NCI-H1573, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.561×** | -10.6 | 2e-24 | 25/35 (SW480, HT-29, …) | all doses, flat | composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.699×** | -9.7 | 3e-20 | 33/44 (CFPAC-1, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.606×** | -9.2 | 2e-18 | 32/43 (NCI-H1573, RKO, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.614×** | -9.0 | 2e-17 | 30/45 (RKO, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.743×** | -8.0 | 6e-14 | 25/43 (COLO 205, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.667×** | -7.7 | 4e-13 | 27/43 (BT-474, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.756×** | -7.5 | 2e-12 | 29/44 (CFPAC-1, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.687×** | -7.2 | 3e-11 | 28/44 (BT-474, SHP-77, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.694×** | -7.0 | 1e-10 | 23/43 (LOX-IMVI, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.708×** | -6.6 | 2e-09 | 24/43 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.546×** | -6.1 | 5e-08 | 23/44 (RKO, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12310. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 259 | 0 | 16 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0472× (z -33.4) |
| [[NCI-H1573 (line)]] | alt | 119 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0465× (z -43.2) |
| [[BT-474 (line)]] | alt | 57.0 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -20.8) |
| [[HT-29 (line)]] | alt | 102 | 1 | 9 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.92× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.180× (z -18.2) |
| [[LOX-IMVI (line)]] | wt | 160 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -22.6) |
| [[COLO 205 (line)]] | alt | 139 | 1 | 8 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.74× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0637× (z -26.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.126× (z -19.9) |
| [[LoVo (line)]] | wt | 51.3 | 3 | 6 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.04× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -26.2) |
| [[KATO III (line)]] | alt | 83.5 | 1 | 7 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.34× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.0729× (z -25.8) |
| [[NCI-H460 (line)]] | wt | 63.3 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -23.0) |
| [[SW480 (line)]] | alt | 20.3 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.149× (z -16.1) |
| [[HepG2_C3A (line)]] | wt | 84.8 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -15.4) |
| [[SHP-77 (line)]] | alt | 31.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -19.7) |
| [[LS 180 (line)]] | wt | 57.4 | 2 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.45× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.233× (z -12.8) |
| [[SNU-423 (line)]] | alt | 91.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -14.5) |
| [[CFPAC-1 (line)]] | alt | 108 | 0 | 5 | — | [[Tofacitinib (drug)]] 5 µM 0.413× (z -11.1) |
| [[H4 (line)]] | wt | 103 | 0 | 5 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -11.9) |
| [[HCT15 (line)]] | alt | 48.7 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0849× (z -16.0) |
| [[HEC-1-A (line)]] | alt | 34.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -17.9) |
| [[HS-578T (line)]] | alt | 74.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -21.5) |
| [[NCI-H1792 (line)]] | alt | 104 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -17.7) |
| [[NCI-H2347 (line)]] | alt | 88.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -24.0) |
| [[PANC-1 (line)]] | alt | 39.8 | 2 (1 ⚠) | 3 | [[Harringtonine (drug)]] 0.5 µM 4.07× (z +13.9) | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -18.3) |
| [[MIA PaCa-2 (line)]] | alt | 64.6 | 1 | 3 | [[Homoharringtonine (drug)]] 0.05 µM 3.36× (z +9.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -15.7) |
| [[RPMI-7951 (line)]] | alt | 54.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -11.8) |
| [[A498 (line)]] | wt | 38.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -19.0) |
| [[AsPC-1 (line)]] | alt | 92.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -14.1) |
| [[SW 1271 (line)]] | alt | 153 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -12.7) |
| [[SW1417 (line)]] | alt | 36.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -11.4) |
| [[A-172 (line)]] | wt | 32.7 | 1 | 1 | [[Homoharringtonine (drug)]] 0.05 µM 3.28× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 48.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 28.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -10.1) |
| [[SW48 (line)]] | wt | 16.8 | 0 | 2 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0746× (z -9.3) |
| [[HOP62 (line)]] | alt | 20.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.42× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 57.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.9) |
| [[SW 900 (line)]] | alt | 51.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -9.2) |
| [[A-427 (line)]] | wt | 4.15 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 11.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.21 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 71.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12310), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SP140L]] | +0.63 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[TRIM38]] | +0.61 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[TRIM56]] | +0.59 | +0.44 / +0.70 | both halves | 3e-05 |  |
| [[GBP3]] | +0.57 | +0.54 / +0.59 | both halves | 1e-05 | pathway: Bacterial Infection Pathways; STRING 494 |
| [[RNASEL]] | +0.57 | +0.45 / +0.61 | both halves | 3e-05 | pathway: HALLMARK_APOPTOSIS |
| [[LCN2]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[IFI16]] | +0.53 | +0.40 / +0.59 | both halves | 5e-05 | STRING 427 |
| [[SP100]] | +0.53 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[SP110]] | +0.53 | +0.39 / +0.60 | both halves | 5e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[RBM11]] | +0.53 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[TNIP3]] | +0.53 | +0.33 / +0.59 | both halves | 1e-04 |  |
| [[BATF2]] | +0.52 | +0.35 / +0.59 | both halves | 1e-04 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMPD4]] | -0.46 | -0.32 / -0.47 | both halves | 1e-04 |  |
| [[CERCAM]] | -0.46 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[MAN1B1]] | -0.44 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[DDHD2]] | -0.44 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[PEBP1]] | -0.44 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[MAPK1]] | -0.43 | -0.26 / -0.52 | both halves | 4e-04 | pathway: Bacterial Infection Pathways |
| [[BACE1]] | -0.43 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[GLT8D1]] | -0.42 | -0.39 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 16, C 1. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNQ3]] | B | KCNQ3 activity strengthens CASP4's drug response | lines that do not express KCNQ3 (23) vs lines expressing it (21) | the lines without KCNQ3 respond 0.71× as strongly (z diff +2.40); strongest at Harringtonine 5 µM: 0.70x vs 0.46x (z diff +3.6) | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000236212, LINC02360, SLITRK4; target measured in part of the lines; artifact flags |
| [[IFI16]] | B | IFI16 activity raises CASP4's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.21× lower at baseline in the lines without IFI16 | 0.004 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[KCNQ3]] | B | KCNQ3 activity raises CASP4's level | lines that do not express KCNQ3 (26) vs lines expressing it (24) | 2.07× lower at baseline in the lines without KCNQ3 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000236212, LINC02360, SLITRK4 |
| [[IFI44]] | B | IFI44 activity raises CASP4's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.59× lower at baseline in the lines without IFI44 | 0.008 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[RNASEL]] | B | RNASEL activity raises CASP4's level | lines that do not express RNASEL (5) vs lines expressing it (45) | 4.00× lower at baseline in the lines without RNASEL | 0.024 | ⚠ within organs, on part of the lines; also absent: SP140L, KIFC3, DDX60; maybe low, not absent |
| [[SPINK1]] | B | SPINK1 activity raises CASP4's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 2.36× lower at baseline in the lines without SPINK1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3 |
| [[ENKUR]] | B | ENKUR activity raises CASP4's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 1.96× lower at baseline in the lines without ENKUR | 0.047 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[CA13]] | B | CA13 activity raises CASP4's level | lines that do not express CA13 (9) vs lines expressing it (41) | 2.44× lower at baseline in the lines without CA13 | 0.048 | ⚠ within organs, on part of the lines; also absent: CA3, PLSCR2, TRIB1; maybe low, not absent |
| [[CARD6]] | B | CARD6 activity raises CASP4's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 2.18× lower at baseline in the lines without CARD6 | 0.049 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[TNIP3]] | B | TNIP3 activity raises CASP4's level | lines that do not express TNIP3 (33) vs lines expressing it (17) | 1.91× lower at baseline in the lines without TNIP3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TMPRSS15, INHBA |
| [[GBP3]] | B | GBP3 activity raises CASP4's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 3.00× lower at baseline in the lines without GBP3 | 0.059 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[MMP13]] | B | MMP13 activity raises CASP4's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 1.82× lower at baseline in the lines without MMP13 | 0.073 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA13]] | B | CASP4 activity raises CA13's level | lines that do not express CASP4 (5) vs lines expressing it (45) | 2.68× lower at baseline in the lines without CASP4 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: S100A13, SP100, KIFC3 |
| [[SP140L]] | B | CASP4 activity raises SP140L's level | lines that do not express CASP4 (5) vs lines expressing it (45) | 3.27× lower at baseline in the lines without CASP4 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: S100A13, SP100, KIFC3 |
| [[IFI44]] | B | CASP4 activity raises IFI44's level | lines that do not express CASP4 (5) vs lines expressing it (45) | 3.61× lower at baseline in the lines without CASP4 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: S100A13, SP100, KIFC3 |
| [[TRIM38]] | C | CASP4 activity raises TRIM38's level | lines that do not express CASP4 (5) vs lines expressing it (45) | 5.84× lower at baseline in the lines without CASP4 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: S100A13, SP100, KIFC3; co-absent with the target |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.446). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.0, 54.9); signed map (61.2, 32.8). **Vector** length 127, 39.2% of its response variance represented; |z| ≥ 3 in 1,415 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.0 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.7 | +7.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.7 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +6.9 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +0.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.7 | +2.4 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -6.3 | -9.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -5.2 | -7.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.7 | -7.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.4 | -7.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.5 | -4.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.2 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | caspase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:104,942,866-104,969,366 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ICE(rel)II, ICH-2, TX |
| Gene groups (HGNC) | Caspases; Caspase recruitment domain containing |
| Hallmark sets | APOPTOSIS, COMPLEMENT, INTERFERON_GAMMA_RESPONSE |
| Reactome | 12 pathways, smallest: CASP4-mediated substrate cleavage; CASP4 inflammasome assembly; Enterobacterial factors antagonize host defense |
| Matched by | ensembl_id |

**Function**, from UniProt [P49662](https://www.uniprot.org/uniprotkb/P49662) (Caspase-4):

> Inflammatory caspase that acts as the effector of the non-canonical inflammasome by mediating lipopolysaccharide (LPS)-induced pyroptosis. Also indirectly activates the NLRP3 and NLRP6 inflammasomes. Acts as a thiol protease that cleaves a tetrapeptide after an Asp residue at position P1: catalyzes cleavage of CGAS, GSDMD and IL18. Effector of the non-canonical inflammasome independently of NLRP3 inflammasome and CASP1: the non-canonical inflammasome promotes pyroptosis through GSDMD cleavage …

**Summary**, from NCBI Gene [837](https://www.ncbi.nlm.nih.gov/gene/837):

> This gene encodes a protein that is a member of the cysteine-aspartic acid protease (caspase) family. Sequential activation of caspases plays a central role in the execution-phase of cell apoptosis. Caspases exist as inactive proenzymes composed of a prodomain and a large and small protease subunit. Activation of caspases requires proteolytic processing at conserved internal aspartic residues to generate a heterodimeric enzyme consisting of the large and small subunits. This caspase is able to …

**Accessions** — [HGNC:1505](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1505) · Entrez [837](https://www.ncbi.nlm.nih.gov/gene/837) · UniProt [P49662](https://www.uniprot.org/uniprotkb/P49662) · Ensembl [ENSG00000196954](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196954)

## Data

Gene col 12310: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12310); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12310, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12310]; `tensor/DDL_lfc|DDL_z.npy` [12310]; `embed/gene_vectors.npy` [12310]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12310 or target_col == 12310). Every well: [[CASP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
